"""Landscape presentation adapter over the original SWF scene and input routes.

Coordinates are logical points. Rendering reads the existing scene; layout and
scroll offsets are presentation state and never write MovieClip transforms.
"""
from dataclasses import dataclass
from copy import copy
import argparse
import math
import io
from .resources import asset_directory, read_asset
from pathlib import Path

from .runtime import get, U, truth
from .display_list import Matrix
from .action_entry import control_path
from .setup_menu import SetupMenu


@dataclass
class ScrollPane:
    offset: float = 0
    velocity: float = 0
    limit: float = 0

    def move(self, delta):
        self.offset = max(0., min(self.limit, self.offset + delta))

    def step(self, seconds):
        self.move(self.velocity * seconds)
        self.velocity *= math.exp(-10 * seconds)
        if self.offset in (0, self.limit):
            self.velocity = 0


@dataclass
class Patch:
    source: object
    target: object
    clip: object

    def original(self, point):
        if not self.clip.collidepoint(point) or not self.target.collidepoint(point):
            return None
        return (self.source.x + (point[0]-self.target.x)*self.source.w/self.target.w,
                self.source.y + (point[1]-self.target.y)*self.source.h/self.target.h)


class LandscapeUI:
    labels = ('Resources', 'Production', 'Technology', 'Mass Media', 'Direct Attack',
              'Prepared Attack', 'Defense', 'Propaganda', 'Diplomacy')
    groups = ('Rockets', 'Aircraft', 'Special Carriers', 'Warheads', 'Bioloads',
              'Infantry', 'Intelligence', 'Defense')

    def __init__(self, menu, size=(1194, 552), safe=(44, 0, 44, 21)):
        import pygame
        self.pg, self.menu, self.safe = pygame, menu, safe
        self.navigation, self.equipment = ScrollPane(), ScrollPane()
        self.patches, self.targets = [], []
        self.gesture = None
        self.fonts = {}
        self.resize(size)

    def resize(self, size):
        pg = self.pg
        self.size = tuple(size)
        self.density = min(size[0]/896, size[1]/414)
        self.width, self.height = (round(n/self.density) for n in size)
        left, top, right, bottom = self.safe
        self.content = pg.Rect(left+4, top+4, self.width-left-right-8, self.height-top-bottom-8)
        x,y,w,h = self.content
        lw, rw, gap = round(w*.215), round(w*.265), 5
        self.left = pg.Rect(x,y,lw,h)
        self.right = pg.Rect(x+w-rw,y,rw,h)
        self.center = pg.Rect(x+lw+gap,y,w-lw-rw-gap*2,h)
        header=64;footer=64
        self.nav_panel=pg.Rect(x,y+header,lw,h-header-80)
        self.nav = self.nav_panel.inflate(-16,-24);self.nav.y+=4
        self.stock = pg.Rect(self.right.x+7,y+40,rw-14,h-40-footer-5)
        self.map_frame=pg.Rect(self.center.x,y+header,self.center.w,h-header-footer-5)
        self.map=self.map_frame.inflate(-12,-12)
        self.messages=pg.Rect(self.center.x,self.map_frame.bottom+5,round(self.center.w*.67),footer)
        self.score=pg.Rect(self.messages.right+4,self.messages.y,self.center.right-self.messages.right-4,footer)
        self.action_rect=pg.Rect(self.right.x,self.messages.y,self.right.w,footer)
        self.patches, self.targets = [], []
        self.equipment_cells=[]

    def point(self, pixel):
        return pixel[0]/self.density, pixel[1]/self.density

    def font(self, size):
        if size not in self.fonts:
            self.fonts[size] = self.pg.font.Font(io.BytesIO(read_asset(next(asset_directory('fonts').glob('1_*.ttf*')))), size)
        return self.fonts[size]

    def text(self, screen, text, pos, size=18, color=(219,232,235)):
        screen.blit(self.font(size).render(str(text), True, color), pos)

    def panel(self, screen, rect, title=None):
        self.skin.panel(screen,rect,title,self.font(10))

    def label(self, screen, text, rect, size=12, color=(225,233,235), center=False):
        pg=self.pg;rect=pg.Rect(rect)
        while size>8 and self.font(size).size(str(text))[0]>rect.w:
            size-=1
        image=self.font(size).render(str(text),True,color)
        position=image.get_rect(center=rect.center) if center else image.get_rect(midleft=(rect.x,rect.centery))
        previous=screen.get_clip();screen.set_clip(previous.clip(rect));screen.blit(image,position);screen.set_clip(previous)

    def button(self, screen, rect, text, action, selected=False):
        self.skin.button(screen,rect,selected)
        self.label(screen,text,rect.inflate(-8,-4),12,center=True)
        self.targets.append((rect.copy(),action))

    def crop(self, frame, rect):
        r=self.pg.Rect(rect);scale=frame.get_width()/800
        return frame.subsurface(self.pg.Rect(round(r.x*scale),round(r.y*scale),round(r.w*scale),round(r.h*scale)))

    def patch(self, screen, source_frame, source, destination, clip=None):
        pg=self.pg; source=pg.Rect(source); destination=pg.Rect(destination)
        # Each authored region keeps one uniform scale. Extra map width remains
        # ocean rather than stretching terrain or cropping corner islands.
        ratio=min(destination.w/source.w,destination.h/source.h)
        target=pg.Rect(0,0,max(1,round(source.w*ratio)),max(1,round(source.h*ratio)))
        target.center=destination.center
        previous=screen.get_clip(); clip=destination if clip is None else clip
        screen.set_clip(clip)
        screen.blit(pg.transform.smoothscale(self.crop(source_frame,source),target.size),target)
        screen.set_clip(previous)
        self.patches.append(Patch(source,target,clip.copy()))

    def draw(self):
        pg=self.pg;screen=pg.Surface((self.width,self.height));screen.fill((4,9,12))
        self.patches=[];self.targets=[];self.equipment_cells=[]
        m=self.menu
        if not m.gameplay or (m.lifecycle and m.lifecycle.status):
            self.patch(screen,m.surface(pg),(0,0,800,600),self.content)
            return pg.transform.smoothscale(screen,self.size)
        from .surface_renderer import SurfaceRenderer
        from .iphone_skin import MobileSkin
        if not hasattr(self,'skin'):self.skin=MobileSkin(m,pg)
        if not hasattr(self,'hud_cache') or self.hud_cache.renderer is not m.renderer:
            self.hud_cache=SurfaceRenderer(m.renderer,pg)
        original=self.hud_cache.frame(m.tree)
        self.panel(screen,self.content)
        logo=pg.Rect(self.left.x,self.left.y,self.left.w,62)
        self.skin.panel(screen,logo)
        self.patch(screen,self.skin.source,(4,12,174,102),logo.inflate(-14,-5))
        self.draw_portraits(screen,original)
        self.draw_navigation(screen,original)
        self.draw_equipment(screen,original)
        self.panel(screen,self.map_frame)
        self.draw_map(screen)
        # Simple actions keep the map visible. Complex source workflows are
        # available in a deliberate drawer instead of replacing the whole map.
        action=get(m.model,'userSelectedActionBtn')
        center=get(m.gameplay.interface,'centerScreen').node
        if action!=getattr(self,'last_action',None):
            self.details_open=action in ('production','research','diplomacy','help')
            self.last_action=action
        if not m.playback and center.frame!=1 and getattr(self,'details_open',False):
            self.panel(screen,self.map_frame)
            self.patch(screen,original,(205,135,365,275),self.map)
            back=pg.Rect(self.map.right-52,self.map.y+2,50,22)
            self.button(screen,back,'MAP',lambda:setattr(self,'details_open',False))
        self.draw_footer(screen,original)
        return pg.transform.smoothscale(screen,self.size)

    def draw_portraits(self,screen,original):
        pg=self.pg
        header=pg.Rect(self.center.x,self.center.y,self.center.w,62)
        self.panel(screen,header)
        width=min(84,(header.w-16)//4)
        start=header.centerx-width*2
        for i in range(4):
            dest=pg.Rect(start+i*width,header.y+3,width-3,51)
            self.skin.panel(screen,dest)
            # Faces retain uniform sampling; the surround can widen independently.
            self.patch(screen,original,(211+i*93,18,61,65),dest.inflate(-10,-5))
            color=((213,58,44),(229,150,38),(43,164,198),(229,208,34))[i]
            pg.draw.line(screen,color,(dest.x+8,dest.y+2),(dest.right-9,dest.y+2),2)
        strip=pg.Rect(header.x+6,header.bottom-12,header.w-12,10)
        self.patch(screen,original,(207,95,360,17),strip)

    def draw_map(self,screen):
        from .surface_renderer import SurfaceRenderer
        from .iphone_map import IslandCamera
        m=self.menu;scene=m.active_scene
        battle=m.playback.battle.node if m.playback else m.gameplay.battle.node
        if not hasattr(self,'map_cache') or self.map_cache.renderer is not scene.renderer:
            self.map_cache=SurfaceRenderer(scene.renderer,self.pg)
        self.camera=IslandCamera(self.map,m)
        view=self.camera.tree(battle)
        # The original water symbol contains only inter-island strips, so lay
        # an authored ocean swatch underneath the widened gaps, then composite
        # the unchanged terrain textures with premultiplied alpha.
        pg=self.pg
        water=pg.transform.smoothscale(self.skin.crop((358,159,48,50)),self.map.size)
        screen.blit(water,self.map)
        self.map_cache._signatures={};self.map_cache.invalid_transforms=set()
        size=(self.map.w*2,self.map.h*2)
        layer=pg.Surface(size,pg.SRCALPHA)
        terrain=getattr(self,'terrain_cache',{})
        for node in view.ordered():
            if not node.name.startswith('land0'):continue
            key=(self.map.size,self.map_cache.signature(node),view.matrix)
            if key not in terrain:
                from PIL import Image
                sprite,position=self.map_cache.paint(node,(view,),0,size)
                if not sprite.get_width() or not sprite.get_height():continue
                image=Image.frombytes('RGBA',sprite.get_size(),pg.image.tobytes(sprite,'RGBA'))
                from PIL import ImageChops, ImageFilter
                mask=Image.new('L',image.size)
                values=[]
                for r,g,b,a in getattr(image,'get_flattened_data',image.getdata)():
                    blue=min(b-r-12,b-g-4)
                    values.append(round(255*(1-max(0,min(1,blue/14)))))
                mask.putdata(values)
                # Remove one-pixel grid/water remnants without changing the
                # basis or aspect of the terrain artwork.
                mask=mask.filter(ImageFilter.MedianFilter(3))
                image=Image.merge('RGBA',tuple(ImageChops.multiply(band,mask) for band in image.split()))
                terrain[key]=(pg.image.frombytes(image.tobytes(),image.size,'RGBA'),position)
            sprite,position=terrain[key];layer.blit(sprite,position,special_flags=pg.BLEND_PREMULTIPLIED)
        # Keep only the current camera's terrain entries (bounded across resize).
        self.terrain_cache={key:value for key,value in terrain.items() if key[0]==self.map.size}
        overlay=copy(view)
        overlay.children={n.depth:n for n in view.ordered() if not n.name.startswith('land0') and n.character_id not in (5259,5260) and not n.name.startswith(('water_overlay_','citypos','swp','twp'))}
        sprite,position=self.map_cache.paint(overlay,(),0,size)
        layer.blit(sprite,position,special_flags=pg.BLEND_PREMULTIPLIED)
        layer=pg.transform.smoothscale(layer,self.map.size)
        screen.blit(layer,self.map,special_flags=pg.BLEND_PREMULTIPLIED)
        self.patches.append(self.camera)

    def draw_navigation(self,screen,original):
        pg=self.pg;pane=self.navigation;row=44
        self.panel(screen,self.nav_panel,'MAIN PANEL')
        pane.limit=max(0,len(self.labels)*row-self.nav.h);pane.move(0)
        actions=('resources','production','research','religion','attack','preAttack','defense','propaganda','diplomacy')
        previous=screen.get_clip();screen.set_clip(self.nav)
        for i,label in enumerate(self.labels):
            rect=pg.Rect(self.nav.x,self.nav.y+i*row-round(pane.offset),self.nav.w-7,40)
            if not rect.colliderect(self.nav):continue
            selected=get(self.menu.model,'userSelectedActionBtn')==actions[i]
            self.skin.button(screen,rect,selected)
            icon_rect=pg.Rect(rect.x+4,rect.y+5,30,30)
            screen.blit(self.skin.icon(actions[i],28),(icon_rect.x,icon_rect.y))
            self.label(screen,label.upper(),pg.Rect(rect.x+38,rect.y,rect.w-42,rect.h),12)
            self.targets.append((rect.clip(self.nav),lambda i=i:self.choose_action(i)))
        screen.set_clip(previous)
        self.scrollbar(screen,self.nav,pane,len(self.labels)*row)
        info=pg.Rect(self.left.x,self.nav_panel.bottom+5,self.left.w,self.left.bottom-self.nav_panel.bottom-5)
        self.panel(screen,info,'INFO PANEL')
        self.draw_stats(screen,info)

    def choose_action(self,index):
        action=('resources','production','research','religion','attack','preAttack','defense','propaganda','diplomacy')[index]
        if get(self.menu.model,'userSelectedActionBtn')==action:
            self.details_open=not getattr(self,'details_open',False)
        else:
            self.menu.press(f'btn{index+1}')

    def draw_stats(self,screen,rect):
        pg=self.pg;m=self.menu;human=m.game.human
        inner=rect.inflate(-14,-17);inner.y+=4
        self.skin.well(screen,inner)
        labels=('FUNDS','technology','propaganda','population','spy')
        funds=f'$ {round(get(human,"turnMoney")*1000000):,}'
        row=max(10,inner.h//5)
        for i,name in enumerate(labels):
            y=inner.y+i*row
            self.label(screen,name,pg.Rect(inner.x+4,y,inner.w*.43,row),10)
            if not i:
                self.label(screen,funds,pg.Rect(inner.x+inner.w*.43,y,inner.w*.55,row),10,(255,215,0))
                continue
            x=inner.x+inner.w*.47;w=inner.w*.49
            pg.draw.rect(screen,(5,13,17),(x,y+3,w,row-5))
            bar=get(self.menu.gameplay.interface,f'statBar{i}')
            mask=get(bar,'statMask');value=get(mask,'_xscale')
            value=0 if value is U else max(0,min(100,value))
            for t in range(max(0,round(w*value/100))):
                f=t/max(1,w);pg.draw.line(screen,(255,round(45+190*f),0),(x+t,y+3),(x+t,y+row-3))

    def draw_equipment(self,screen,original):
        pg=self.pg
        toolbar=pg.Rect(self.right.x,self.right.y,self.right.w,34);self.panel(screen,toolbar)
        self.button(screen,pg.Rect(toolbar.x+7,toolbar.y+6,toolbar.w*.35,23),'HELP',lambda:self.menu.press('btn_help'))
        self.button(screen,pg.Rect(toolbar.x+toolbar.w*.39,toolbar.y+6,toolbar.w*.44,23),'FULL SCREEN',self.toggle_fullscreen)
        gear=pg.Rect(toolbar.right-26,toolbar.y+5,23,24)
        screen.blit(self.skin.icon('gear',23),(gear.x,gear.y));self.targets.append((gear,lambda:self.menu.press('btn38')))
        frame=self.stock.inflate(12,10);self.panel(screen,frame)
        buttons=[b for b in get(self.menu.gameplay.hud,'stockBtn_arr') if b is not U]
        sections=[]
        for group in range(1,9):
            members=[b for b in buttons if get(b,'stockPanelNum')==group]
            sections.append((group,members))
        # Two-column categories follow the source inventory order. Wide carrier
        # labels retain a full row. All item cells are separate click targets.
        rows=[];y=0
        for group,members in sections:
            columns=1 if group==3 else 2
            height=26+math.ceil(len(members)/columns)*36+6
            rows.append((group,members,columns,y,height));y+=height+5
        pane=self.equipment;pane.limit=max(0,y-self.stock.h);pane.move(0)
        previous=screen.get_clip();screen.set_clip(self.stock)
        for group,members,columns,offset,height in rows:
            card=pg.Rect(self.stock.x,self.stock.y+offset-round(pane.offset),self.stock.w-8,height)
            if not card.colliderect(self.stock):continue
            self.panel(screen,card)
            self.label(screen,self.groups[group-1],pg.Rect(card.x+37,card.y+3,card.w-44,22),12)
            icon=('rocket','plane','ship','warhead','bio','attack','spy','defense')[group-1]
            screen.blit(self.skin.icon(icon,30),(card.x+5,card.y+27))
            body_x=card.x+38;body_w=card.w-43
            for index,item in enumerate(members):
                # Source rows alternate columns rather than sorting by label.
                if columns==2:
                    row=index%2 if len(members)>2 else 0
                    col=index//2 if len(members)>2 else index
                else:row=index;col=0
                rect=pg.Rect(body_x+col*body_w/columns,card.y+25+row*36,body_w/columns,36)
                amount=get(item,'_stockAmount');enabled=amount is not U and amount>=0
                color=(219,231,236) if enabled else (122,145,155)
                count=pg.Rect(rect.right-24,rect.y+5,22,24)
                self.skin.well(screen,count)
                self.label(screen,str(amount) if enabled else '-',count,12,color,center=True)
                self.label(screen,str(get(item,'label')),pg.Rect(rect.x+1,rect.y,rect.w-27,rect.h),10,color)
                path=control_path(get(item,'overlayMC').node)
                hit=rect.clip(self.stock)
                self.targets.append((hit,lambda path=path:self.menu.press(path)))
                self.equipment_cells.append((get(item,'relatedWeapon'),hit))
        screen.set_clip(previous);self.scrollbar(screen,self.stock,pane,y)

    def scrollbar(self,screen,rect,pane,total):
        if not pane.limit:return
        pg=self.pg;track=pg.Rect(rect.right-5,rect.y+4,4,rect.h-8)
        pg.draw.rect(screen,(5,14,19),track,border_radius=2)
        height=max(22,track.h*rect.h/total)
        thumb=pg.Rect(track.x,track.y+(track.h-height)*pane.offset/pane.limit,4,height)
        pg.draw.rect(screen,(142,164,176),thumb,border_radius=2)
        for y,sign in ((rect.top,1),(rect.bottom,-1)):
            pg.draw.polygon(screen,(201,214,219),[(rect.right-8,y+sign*6),(rect.right-2,y+sign*6),(rect.right-5,y+sign*1)])

    def draw_footer(self,screen,original):
        pg=self.pg;m=self.menu
        self.panel(screen,self.messages)
        well=self.messages.inflate(-12,-12);self.skin.well(screen,well)
        action=get(m.model,'userSelectedActionBtn')
        center=get(m.gameplay.interface,'centerScreen').node
        pending=center.frame!=1 and truth(action) and not m.playback
        if pending and not getattr(self,'details_open',False):
            self.label(screen,str(action).replace('religion','Mass media').upper(),pg.Rect(well.x+4,well.y+1,well.w-8,18),11,(62,246,40))
            for i,(caption,fn) in enumerate((('DETAILS',lambda:setattr(self,'details_open',True)),('CANCEL',lambda:m.press('btnCancel')),('ACCEPT',lambda:m.press('btnAccept')))):
                rect=pg.Rect(well.x+3+i*(well.w-6)/3,well.bottom-25,(well.w-12)/3,22)
                self.button(screen,rect,caption,fn)
        else:
            messages=[get(msg,'_msg') for msg in get(m.game.human,'shortMSG_arr') if truth(get(msg,'_msg'))]
            text=' '.join(str(line).replace('<br />',' ') for line in messages[-2:]) or 'Choose two actions, then confirm.'
            words=text.split();lines=[];line=''
            for word in words:
                candidate=(line+' '+word).strip()
                if self.font(11).size(candidate)[0]>well.w-12 and line:lines.append(line);line=word
                else:line=candidate
            if line:lines.append(line)
            for i,line in enumerate(lines[-3:]):
                self.label(screen,line,pg.Rect(well.x+5,well.y+4+i*14,well.w-10,14),11,(61,242,32))
        self.panel(screen,self.score,'SCORE')
        count=self.score.inflate(-12,-25);count.y+=5;self.skin.well(screen,count)
        self.label(screen,str(round(get(m.game.human,'score'))),count,14,center=True)
        self.panel(screen,self.action_rect,'NEXT ACTION')
        rect=self.action_rect.inflate(-10,-15);rect.y+=5
        width=round((rect.w-32)/2)
        for i,name in enumerate(('btn44','btn45')):
            target=pg.Rect(rect.x+i*(width+2),rect.y,width,rect.h)
            self.label(screen,'FIRST ACTION' if i==0 else 'SECOND ACTION',pg.Rect(target.x,target.y,target.w,10),8,center=True)
            art=pg.Rect(target.x,target.y+10,target.w,target.h-11)
            screen.blit(pg.transform.smoothscale(self.crop(original,(216+i*149,544,140,44)),art.size),art)
            action=get(get(m.game.human,'turnActionArr')[i],'action')
            if truth(action):self.label(screen,str(action).replace('religion','Media').upper(),target.inflate(-8,-16),9,(255,194,63),center=True)
            self.targets.append((target,lambda name=name:m.press(name)))
        confirm=pg.Rect(rect.right-28,rect.y,28,rect.h)
        self.label(screen,'CONFIRM',pg.Rect(confirm.x-2,confirm.y,32,10),7,center=True)
        art=pg.Rect(confirm.x,confirm.y+10,confirm.w,confirm.h-11)
        screen.blit(pg.transform.smoothscale(self.crop(original,(515,541,47,50)),art.size),art)
        self.targets.append((confirm,lambda:m.press('btn46')))

    def toggle_fullscreen(self):
        self.menu.fullscreen_requested=not self.menu.fullscreen_requested

    def stage(self,point):
        for patch in reversed(self.patches):
            original=patch.original(point)
            if original is not None:return original
        return None

    def down(self,pixel,now):
        p=self.point(pixel)
        pane=self.navigation if self.nav.collidepoint(p) else self.equipment if self.stock.collidepoint(p) else None
        custom=next(((rect,fn) for rect,fn in reversed(self.targets) if rect.collidepoint(p)),None)
        self.gesture={'start':p,'last':p,'time':now,'pane':pane,'drag':False,'custom':custom}
        if pane:pane.velocity=0
        elif custom is None and self.stage(p) is not None:
            self.menu.motion(self.stage(p));self.menu.click(self.stage(p))

    def motion(self,pixel,now):
        p=self.point(pixel);g=self.gesture
        if g and g['pane']:
            dy=g['last'][1]-p[1]
            if abs(p[1]-g['start'][1])>8:g['drag']=True
            if g['drag']:
                g['pane'].move(dy)
                g['pane'].velocity=max(-1800,min(1800,dy/max(.008,now-g['time'])))
            g['last'],g['time']=p,now
        else:
            stage=self.stage(p)
            if stage is not None:self.menu.motion(stage)
            elif self.menu.gameplay:self.menu.motion((799,599))

    def up(self,pixel,now):
        p=self.point(pixel);g=self.gesture;self.gesture=None
        if not g:return
        if not g['drag'] and math.dist(p,g['start'])<=10:
            # Scroll panels activate on release, so swipes never select a weapon.
            custom=g.get('custom')
            if custom and custom[0].collidepoint(p):custom[1]()
        self.menu.release(self.stage(p) or self.menu.host.pointer)

    def wheel(self,pixel,amount):
        p=self.point(pixel)
        pane=self.navigation if self.nav.collidepoint(p) else self.equipment if self.stock.collidepoint(p) else None
        if pane:pane.velocity=0;pane.move(-amount*48)

    def step(self,seconds):
        if not self.gesture:
            self.navigation.step(seconds);self.equipment.step(seconds)


def run(ui):
    pg=ui.pg;m=ui.menu
    from .menu_audio import PygameMenuAudio
    screen=pg.display.set_mode(ui.size,pg.RESIZABLE)
    pg.display.set_caption('World Domination II - iPhone landscape preview')
    try:
        try:m.audio.connect(PygameMenuAudio(m.audio,pg))
        except pg.error:pass
        clock=pg.time.Clock();accumulator=0.;running=True;finger=None;fullscreen=False
        while running:
            dt=min(clock.tick(60)/1000,.25);now=pg.time.get_ticks()/1000
            for e in pg.event.get():
                if e.type==pg.QUIT:running=False
                elif e.type==pg.VIDEORESIZE:
                    screen=pg.display.set_mode((max(640,e.w),max(300,e.h)),pg.RESIZABLE);ui.resize(screen.get_size())
                elif e.type==pg.FINGERDOWN and finger is None:
                    finger=e.finger_id;ui.down((e.x*ui.size[0],e.y*ui.size[1]),now)
                elif e.type==pg.FINGERMOTION and e.finger_id==finger:ui.motion((e.x*ui.size[0],e.y*ui.size[1]),now)
                elif e.type==pg.FINGERUP and e.finger_id==finger:
                    ui.up((e.x*ui.size[0],e.y*ui.size[1]),now);finger=None
                elif e.type in (pg.MOUSEMOTION,pg.MOUSEBUTTONDOWN,pg.MOUSEBUTTONUP) and not getattr(e,'touch',False) and finger is None:
                    if e.type==pg.MOUSEMOTION:ui.motion(e.pos,now)
                    elif e.button==1:
                        if e.type==pg.MOUSEBUTTONDOWN:ui.down(e.pos,now)
                        else:ui.up(e.pos,now)
                elif e.type==pg.MOUSEWHEEL:ui.wheel(pg.mouse.get_pos(),getattr(e,'precise_y',e.y))
                elif e.type==pg.TEXTINPUT:m.text_entry.insert(e.text)
                elif e.type==pg.KEYDOWN:
                    if not m.text_entry.key(e.key,getattr(e,'mod',0)):
                        if e.key==pg.K_ESCAPE:running=False
                        elif e.key==pg.K_p:
                            m.host.clock.paused=not m.host.clock.paused;m.audio.pause(m.host.clock.paused)
                elif e.type==pg.WINDOWFOCUSLOST:
                    ui.gesture=None;finger=None;m.release(m.host.pointer);m.text_entry.focus(None)
            accumulator+=dt*24;ticks=int(accumulator);accumulator-=ticks
            m.audio.poll();m.step(ticks);ui.step(dt)
            if m.fullscreen_requested!=fullscreen:
                fullscreen=m.fullscreen_requested
                screen=pg.display.set_mode((0,0) if fullscreen else ui.size,pg.FULLSCREEN if fullscreen else pg.RESIZABLE)
                ui.resize(screen.get_size())
            screen.blit(ui.draw(),(0,0));pg.display.flip()
    finally:
        if m.playback:m.playback.finish()
        m.audio.close();pg.quit()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--width',type=int,default=1194);parser.add_argument('--height',type=int,default=552)
    parser.add_argument('--safe-area',type=float,nargs=4,default=(44,0,44,21),metavar=('LEFT','TOP','RIGHT','BOTTOM'))
    parser.add_argument('--seed',type=int,default=0)
    parser.add_argument('--start-game',action='store_true');parser.add_argument('--instant-battles',action='store_true')
    parser.add_argument('--screenshot',type=Path)
    args=parser.parse_args()
    if args.width<640 or args.height<300 or args.width<=args.height:parser.error('Use a landscape viewport of at least 640 x 300.')
    if min(args.safe_area)<0 or args.safe_area[0]+args.safe_area[2]>200 or args.safe_area[1]+args.safe_area[3]>80:parser.error('Safe-area insets are outside the supported preview range.')
    import pygame
    pygame.init();menu=SetupMenu(args.seed)
    if args.start_game:
        menu.press('splashScreenMC')
        for i in range(1,5):menu.press(f'BTN_allLeaders_screen{i}')
        menu.start_game()
    ui=LandscapeUI(menu,(args.width,args.height),args.safe_area)
    if args.screenshot:
        pygame.display.set_mode((1,1), pygame.HIDDEN)
        args.screenshot.parent.mkdir(parents=True,exist_ok=True)
        pygame.image.save(ui.draw(),str(args.screenshot));menu.audio.close();pygame.quit()
    else:
        menu.play_battles=not args.instant_battles
        run(ui)
