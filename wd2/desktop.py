"""Playable Python interface for the recovered game model (not Flash UI parity)."""
from pathlib import Path
import argparse
import html
import io
import json
import math
import os
import re
import time

from .game import Game
from .city_layer import CityLayer
from .resources import asset_directory, read_asset
from .runtime import get, truth, number, U

ROOT=Path(__file__).resolve().parents[1]
ACTIONS=[('resources','Resources'),('production','Production'),('research','Research'),('religion','Mass media'),('attack','Direct attack'),('preAttack','Prepare / fire'),('defense','Defense'),('propaganda','Propaganda'),('diplomacy','Diplomacy')]
COLORS=[(87,180,255),(246,105,109),(238,177,77),(177,145,241),(90,204,162)]


class Desktop:
    def __init__(self,seed=0,difficulty=1):
        import pygame
        self.pg=pygame; pygame.init()
        self.screen=pygame.display.set_mode((1160,820)); pygame.display.set_caption('World Domination II — Python port')
        self.font=pygame.font.SysFont('Segoe UI',16); self.small=pygame.font.SysFont('Segoe UI',13); self.title=pygame.font.SysFont('Segoe UI',27,bold=True)
        self.big=pygame.font.SysFont('Segoe UI',21,bold=True)
        self.seed,self.difficulty=seed,difficulty; self.game=Game(seed,difficulty)
        self.map=pygame.image.load(ROOT/'assets/map.png').convert_alpha()
        self.city_layer=CityLayer(pygame)
        self.action='resources'; self.choice_index=0; self.target=1; self.city=0; self.percent=50
        self.notice='Select two actions, then resolve the turn.'; self.error=False; self.buttons=[]; self.messages=[]; self.music=False
        self.last_resolve=0; self.effects=[]

    def text(self,s,x,y,color=(221,229,233),font=None):
        self.screen.blit((font or self.font).render(str(s),True,color),(x,y))

    def wrap(self,s,x,y,width,color=(170,187,197),font=None,max_lines=4):
        font=font or self.small; line=''; lines=[]
        for word in str(s).split():
            if font.size(line+' '+word)[0]>width and line: lines.append(line); line=word
            else: line=(line+' '+word).strip()
        if line: lines.append(line)
        for i,line in enumerate(lines[:max_lines]): self.text(line,x,y+i*19,color,font)

    def button(self,label,rect,callback,selected=False,enabled=True):
        pg=self.pg; rect=pg.Rect(rect); color=(39,88,111) if selected else (34,48,59)
        if not enabled: color=(24,32,40)
        elif rect.collidepoint(pg.mouse.get_pos()): color=tuple(min(c+15,255) for c in color)
        pg.draw.rect(self.screen,color,rect,border_radius=5)
        pg.draw.rect(self.screen,(88,171,193) if selected else (55,74,87),rect,1,border_radius=5)
        font=self.small if len(label)>15 else self.font
        pic=font.render(label,True,(233,241,245) if enabled else (95,110,119)); self.screen.blit(pic,pic.get_rect(center=rect.center))
        if enabled: self.buttons.append((rect,callback))

    def choose_action(self,action): self.action=action; self.choice_index=0; self.error=False

    def choices(self):
        g=self.game; stock=get(g.human,'weaponStock'); weapons=list(get(stock,'weaponArr'))+[get(stock,'antiAir'),get(stock,'antiRocket')]
        available=lambda w:truth(get(w,'active')) and number(get(w,'inStock'))-number(get(w,'inUse'))>0
        if self.action=='research':
            return [(get(t,'techName'),f"{get(t,'prettyName')}  /  ${get(t,'cost')}M") for t in get(get(g.human,'techTree'),'techArr') if not truth(get(t,'invented')) and (get(t,'techLevel')==1 or truth(get(get(t,'requiredTech'),'invented')))]
        if self.action=='production': return [(s,s.title()) for s in ['rockets','planes','special','warhead','bioload','soldier','spy','defense']]
        if self.action=='diplomacy': return [(i,f'{row[0].title()} ${row[2]}M / {row[1]} turns') for i,row in enumerate(get(g.model,'diplomacy_options_arr'))]
        if self.action=='attack': weapons=[w for w in weapons if get(w,'weaponType') in ('soldier','spy')]
        elif self.action=='defense': weapons=[w for w in weapons if get(w,'weaponType')=='anti']
        elif self.action=='preAttack':
            if get(g.human,'preAttackStatus')=='ready':
                carrier=get(g.human,'preAttackWeapon'); ctype=get(carrier,'weaponType')
                if ctype=='ship': weapons=[w for w in weapons if get(w,'weaponType')=='plane']
                elif ctype=='space': weapons=[w for w in weapons if get(w,'weaponName')=='specialLoad']
                else: weapons=[w for w in weapons if get(w,'weaponCategory')=='payload' and (ctype=='sub' or number(get(w,'weaponLevel'))<=number(get(carrier,'weaponLevel')))]
            else: weapons=[w for w in weapons if get(w,'weaponCategory') in ('carrier','specialCarrier')]
        else: return []
        return [(get(w,'weaponName'),f"{get(w,'prettyName')}  /  {get(w,'inStock')} available") for w in weapons if available(w)]

    def cycle(self,step): self.choice_index+=step

    def queue(self):
        choices=self.choices(); value=choices[self.choice_index%len(choices)][0] if choices else None
        options={'target':self.target,'city':self.city}
        if self.action in ('attack','defense'): options['weapon']=value
        elif self.action=='preAttack':
            options['payload' if get(self.game.human,'preAttackStatus')=='ready' else 'weapon']=value
        elif self.action=='production': options.update(category=value,percent=self.percent)
        elif self.action=='research': options['tech']=value
        elif self.action=='diplomacy': options['diplomacy']=value if value is not None else 0
        try:
            self.game.queue(self.action,**options); self.notice='Action queued. Choose another action or resolve the turn.'; self.error=False
        except ValueError as exc: self.notice=str(exc); self.error=True

    def clear(self): self.game.clear_actions(); self.notice='Action slots cleared.'; self.error=False

    def resolve(self):
        try:
            result=self.game.advance(); self.error=False; self.last_resolve=time.monotonic()
            self.notice=f'Turn {result["turn"]} resolved.'
            for message in get(self.game.human,'shortMSG_arr'):
                text=html.unescape(re.sub('<[^>]*>',' ',str(get(message,'_msg')))).strip()
                if text: self.messages.insert(0,text)
            self.effects=[]
            for event in self.game.events:
                if event.get('_item')=='battle' and event.get('_city') is not None:
                    self.effects.append((event['_city'],event.get('_casualties') or 0))
        except ValueError as exc: self.notice=str(exc); self.error=True

    def new_game(self):
        self.game=Game(self.seed,self.difficulty); self.messages=[]; self.effects=[]; self.notice='New game ready.'; self.error=False

    def toggle_music(self):
        try:
            if self.music: self.pg.mixer.music.stop(); self.music=False
            else:
                track=next(asset_directory('audio').glob('*WDTheme*'))
                self._music_stream=io.BytesIO(read_asset(track))
                self.pg.mixer.music.load(self._music_stream, 'mp3'); self.pg.mixer.music.play(-1); self.pg.mixer.music.set_volume(.3); self.music=True
        except (StopIteration,self.pg.error) as exc: self.notice='Audio unavailable: '+str(exc); self.error=True

    def draw(self):
        pg=self.pg; g=self.game; self.buttons=[]; self.screen.fill((13,22,30))
        self.text('WORLD DOMINATION II',20,14,font=self.title)
        self.text('Recovered game logic · Python desktop edition',22,49,(134,159,175),self.small)
        self.button('New game',(842,18,94,34),self.new_game)
        self.button('Music: on' if self.music else 'Music: off',(946,18,95,34),self.toggle_music)
        self.button('Exit',(1051,18,89,34),lambda:pg.event.post(pg.event.Event(pg.QUIT)))
        self.text(f'TURN {get(g.model,"turn")}     FUNDS ${get(g.human,"money")}M     POPULATION {get(g.human,"population")}M     MEDIA {get(g.human,"religion")}/100',22,82,(218,226,230),self.big)
        self.screen.blit(self.map,(20,120)); pg.draw.rect(self.screen,(69,88,99),(19,119,802,602),1)
        for i,j,city in self.city_layer.ordered_cities(g):
            x=20+number(get(city,'xPos')); y=120+number(get(city,'yPos')); pop=number(get(city,'population'))
            if pop>0: pg.draw.ellipse(self.screen,(*COLORS[i],),(x-23,y-10,46,20),2)
            self.city_layer.draw(self.screen,city,(20,120))
            if self.target==i and self.city==j: pg.draw.ellipse(self.screen,(255,241,167),(x-29,y-13,58,27),3)
            if pop<=0: continue
            label=self.small.render(f'{pop:g}M',True,(248,248,237)); box=label.get_rect(center=(x,y+15)); pg.draw.rect(self.screen,(20,33,40),box.inflate(9,3),border_radius=3); self.screen.blit(label,box)
        elapsed=time.monotonic()-self.last_resolve
        if elapsed<2:
            for city_id,casualties in self.effects:
                c=g.rt.invoke(g.model,'getCityByID',city_id); x=20+number(get(c,'xPos')); y=120+number(get(c,'yPos'))
                pg.draw.circle(self.screen,(255,151,66),(int(x),int(y)),int(15+elapsed*25),2)
                self.text(f'-{casualties}M',x-15,y-60-elapsed*10,(255,225,147))
        # The right panel deliberately exposes the model's actions directly.
        pg.draw.rect(self.screen,(19,31,40),(836,120,308,601),border_radius=7)
        self.text('COMMAND',852,134,(137,177,195),self.small)
        for index,(action,label) in enumerate(ACTIONS):
            self.button(label,(850+(index%2)*143,162+(index//2)*37,136,31),lambda a=action:self.choose_action(a),self.action==action)
        self.text('TARGET',852,357,(137,177,195),self.small)
        self.button('<',(850,382,30,31),lambda:self.change_target(-1))
        self.text(('Your nation' if self.target==0 else f'Nation {self.target}')+f' / city {self.city+1}',891,387,COLORS[self.target],self.small)
        self.button('>',(1103,382,30,31),lambda:self.change_target(1))
        self.text('Click a city on the map to select it.',852,420,(121,144,159),self.small)
        choices=self.choices()
        if choices:
            value,label=choices[self.choice_index%len(choices)]
            self.button('<',(850,458,30,34),lambda:self.cycle(-1)); self.button('>',(1103,458,30,34),lambda:self.cycle(1))
            self.wrap(label,891,457,199,(226,233,235),max_lines=2)
            self.text(f'{self.choice_index%len(choices)+1} of {len(choices)}',852,498,(129,155,168),self.small)
        elif self.action in ('resources','religion','propaganda'):
            desc={'resources':'Collect resources from your living cities.','religion':'Increase mass media influence.','propaganda':'Attract citizens from the selected enemy city.'}[self.action]
            self.wrap(desc,852,458,275,max_lines=3)
        else: self.wrap('No available options. Research or produce the required equipment.',852,458,270,max_lines=3)
        if self.action=='production':
            self.button('-',(850,523,30,28),lambda:self.change_percent(-10)); self.text(f'Budget: {self.percent}% of ${get(g.human,"turnMoney")}M',889,527,font=self.small); self.button('+',(1103,523,30,28),lambda:self.change_percent(10))
        elif self.action=='preAttack':
            status=get(g.human,'preAttackStatus'); self.wrap('Choose a payload to fire.' if status=='ready' else 'Prepare a carrier now, choose its payload next turn.',852,524,275,max_lines=2)
        self.button('Queue action',(850,568,283,36),self.queue,selected=True)
        for i,ta in enumerate(get(g.human,'turnActionArr')):
            action=get(ta,'action'); self.text(f'{i+1}. '+(str(action) if truth(action) else 'Empty action slot'),852,615+i*24,(184,205,216),self.small)
        self.button('Clear',(850,675,78,32),self.clear)
        self.button('Resolve turn',(938,675,195,32),self.resolve,selected=True,enabled=truth(get(g.human,'allActionsSet')) and truth(get(g.human,'alive')))
        self.wrap(self.notice,22,735,790,(255,152,134) if self.error else (207,220,225),max_lines=2)
        if self.messages: self.wrap(self.messages[0],22,778,790,(150,177,191),max_lines=1)
        self.text('Simplified visuals; Flash animation parity is unfinished.',841,745,(121,144,159),self.small)
        self.text('Original logic and assets. No Flash runtime required.',841,769,(121,144,159),self.small)
        if not truth(get(g.human,'alive')): self.text('YOUR NATION HAS FALLEN',260,365,(255,220,200),self.title)
        elif len(get(g.model,'activePlayerArr'))==1: self.text('WORLD DOMINATION',275,365,(255,235,173),self.title)

    def change_target(self,delta): self.target=(self.target+delta)%5
    def change_percent(self,delta): self.percent=max(10,min(100,self.percent+delta))

    def click(self,pos):
        for rect,callback in reversed(self.buttons):
            if rect.collidepoint(pos): callback(); return
        best=None
        for i,p in enumerate(self.game.players):
            for j,c in enumerate(get(p,'cityArr')):
                distance=math.hypot(pos[0]-20-number(get(c,'xPos')),pos[1]-120-number(get(c,'yPos')))
                if distance<40 and (best is None or distance<best[0]): best=(distance,i,j)
        if best: _,self.target,self.city=best

    def run(self,screenshot=None,smoke=False):
        pg=self.pg
        if smoke:
            self.draw(); self.choose_action('resources'); self.queue(); self.choose_action('religion'); self.queue(); self.resolve(); self.draw()
        if screenshot:
            self.draw(); pg.image.save(self.screen,screenshot); pg.quit(); return
        clock=pg.time.Clock(); running=True
        while running:
            for event in pg.event.get():
                if event.type==pg.QUIT: running=False
                elif event.type==pg.MOUSEBUTTONDOWN and event.button==1: self.click(event.pos)
                elif event.type==pg.KEYDOWN and event.key==pg.K_RETURN and truth(get(self.game.human,'allActionsSet')): self.resolve()
            self.draw(); pg.display.flip(); clock.tick(30)
        pg.quit()


def main():
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--seed',type=int,default=0); parser.add_argument('--difficulty',type=int,choices=[0,1,2],default=1)
    parser.add_argument('--screenshot',type=Path); parser.add_argument('--smoke',action='store_true'); args=parser.parse_args()
    if args.screenshot: os.environ['SDL_VIDEODRIVER']='dummy'; args.screenshot.parent.mkdir(parents=True,exist_ok=True)
    Desktop(args.seed,args.difficulty).run(args.screenshot,args.smoke)


if __name__=='__main__': main()
