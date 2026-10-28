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
        self.content = pg.Rect(left+6, top+6, self.width-left-right-12, self.height-top-bottom-12)
        x,y,w,h = self.content
        lw, rw, gap = round(w*.20), round(w*.25), 8
        self.left = pg.Rect(x,y,lw,h)
        self.right = pg.Rect(x+w-rw,y,rw,h)
        self.center = pg.Rect(x+lw+gap,y,w-lw-rw-gap*2,h)
        self.nav = pg.Rect(x+5,y+66,lw-10,max(44,h-142))
        self.stock = pg.Rect(self.right.x+5,y+54,rw-10,h-59)
        self.map = pg.Rect(self.center.x,y+76,self.center.w,h-76-104)
        self.patches, self.targets = [], []

    def point(self, pixel):
        return pixel[0]/self.density, pixel[1]/self.density

    def font(self, size):
        if size not in self.fonts:
            self.fonts[size] = self.pg.font.Font(io.BytesIO(read_asset(next(asset_directory('fonts').glob('1_*.ttf*')))), size)
        return self.fonts[size]

    def text(self, screen, text, pos, size=18, color=(219,232,235)):
        screen.blit(self.font(size).render(str(text), True, color), pos)

    def panel(self, screen, rect):
        self.pg.draw.rect(screen,(23,43,53),rect,border_radius=7)
        self.pg.draw.rect(screen,(89,118,129),rect,2,border_radius=7)

    def button(self, screen, rect, text, action, selected=False):
        self.pg.draw.rect(screen,(27,78,105) if selected else (32,52,61),rect,border_radius=5)
        self.pg.draw.rect(screen,(100,130,141),rect,1,border_radius=5)
        image = self.font(17).render(text,True,(237,244,244))
        screen.blit(image,image.get_rect(center=rect.center))
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
        pg=self.pg; screen=pg.Surface((self.width,self.height))
        screen.fill((5,12,17)); self.patches=[]; self.targets=[]
        m=self.menu
        if not m.gameplay or (m.lifecycle and m.lifecycle.status):
            self.patch(screen,m.surface(pg),(0,0,800,600),self.content)
            return pg.transform.smoothscale(screen,self.size)
        # Canonical HUD stays available while the separate battle graph plays.
        from .surface_renderer import SurfaceRenderer
        cache=getattr(self,'hud_cache',None)
        if cache is None or cache.renderer is not m.renderer:
            self.hud_cache=SurfaceRenderer(m.renderer,pg)
        original=self.hud_cache.frame(m.tree)
        for rect in (self.left,self.center,self.right):self.panel(screen,rect)
        self.patch(screen,original,(0,0,184,122),pg.Rect(self.left.x+5,self.left.y+4,self.left.w-10,58))
        self.draw_navigation(screen,original)
        self.draw_equipment(screen,original)
        self.patch(screen,original,(202,4,380,112),pg.Rect(self.center.x+4,self.center.y+4,self.center.w-8,68))
        pg.draw.rect(screen,(8,48,75),self.map)
        center=get(m.gameplay.interface,'centerScreen').node
        if not m.playback and center.frame!=1:
            self.patch(screen,original,(205,135,365,275),self.map)
        else:
            self.draw_map(screen)
        self.draw_footer(screen,original)
        return pg.transform.smoothscale(screen,self.size)

    def draw_map(self,screen):
        from .surface_renderer import SurfaceRenderer
        m=self.menu;scene=m.active_scene
        battle=m.playback.battle.node if m.playback else m.gameplay.battle.node
        cache=getattr(self,'map_cache',None)
        if cache is None or cache.renderer is not scene.renderer:
            self.map_cache=SurfaceRenderer(scene.renderer,self.pg)
        # Draw the existing battle subtree into a wider camera. Only a copy of
        # the root transform changes; every island, sprite and animation keeps
        # its authored local coordinates and one common scale.
        scale=min(self.map.w/800,self.map.h/600)
        view=copy(battle)
        view.matrix=Matrix(a=scale*2,d=scale*2,tx=(self.map.w-800*scale))
        frame=self.map_cache.frame(view,(self.map.w*2,self.map.h*2),(8,48,75))
        screen.blit(self.pg.transform.smoothscale(frame,self.map.size),self.map)
        source_w=self.map.w/scale*.46
        source=self.pg.FRect(205-(source_w-368)/2,135,source_w,276)
        # Camera mapping uses floating-point rectangles to avoid shifting city
        # hit tests when the viewport changes by a single pixel.
        self.patches.append(Patch(source,self.pg.FRect(self.map),self.map.copy()))

    def draw_navigation(self, screen, original):
        pg=self.pg; pane=self.navigation; row=48
        pane.limit=max(0,len(self.labels)*row-self.nav.h);pane.move(0)
        previous=screen.get_clip();screen.set_clip(self.nav)
        for i,label in enumerate(self.labels):
            rect=pg.Rect(self.nav.x,self.nav.y+i*row-round(pane.offset),self.nav.w-7,44)
            if not rect.colliderect(self.nav):continue
            # Original metallic button and its selected state, with a readable
            # label laid over the center and a 44-point target per menu item.
            src=pg.Rect(8,141+i*30,165,27)
            screen.blit(pg.transform.smoothscale(self.crop(original,src),rect.size),rect)
            selected=get(self.menu.model,'userSelectedActionBtn')==('resources','production','research','religion','attack','preAttack','defense','propaganda','diplomacy')[i]
            pg.draw.rect(screen,(24,73,96) if selected else (29,44,51),rect.inflate(-10,-10),border_radius=3)
            self.text(screen,label,(rect.x+9,rect.y+14),17)
            self.targets.append((rect.clip(self.nav),lambda i=i:self.menu.press(f'btn{i+1}')))
        screen.set_clip(previous);self.scrollbar(screen,self.nav,pane,len(self.labels)*row)
        info=pg.Rect(self.left.x+5,self.nav.bottom+7,self.left.w-10,self.left.bottom-self.nav.bottom-12)
        self.patch(screen,original,(7,432,165,85),info)

    def draw_equipment(self, screen, original):
        pg=self.pg
        self.button(screen,pg.Rect(self.right.x+5,self.right.y+5,(self.right.w-15)//2,44),'Help',lambda:self.menu.press('btn_help'))
        self.button(screen,pg.Rect(self.right.centerx+2,self.right.y+5,(self.right.w-15)//2,44),'Full screen',self.toggle_fullscreen)
        buttons=[b for b in get(self.menu.gameplay.hud,'stockBtn_arr') if b is not U]
        rows=[];group=None;y=0
        for b in buttons:
            section=get(b,'stockPanelNum')
            if section!=group:
                rows.append(('heading',self.groups[int(section)-1],y));y+=28;group=section
            rows.append(('button',b,y));y+=48
        pane=self.equipment;pane.limit=max(0,y-self.stock.h);pane.move(0)
        previous=screen.get_clip();screen.set_clip(self.stock)
        for kind,item,offset in rows:
            rect=pg.Rect(self.stock.x,self.stock.y+offset-round(pane.offset),self.stock.w-7,44 if kind=='button' else 26)
            if not rect.colliderect(self.stock):continue
            if kind=='heading':
                self.text(screen,item,(rect.x+3,rect.y+5),18);continue
            bounds=self.menu.renderer.control_bounds(get(item,'overlayMC').node)
            src=pg.Rect(math.floor(bounds[0]),math.floor(bounds[1]),math.ceil(bounds[2]-bounds[0]),24)
            pg.draw.rect(screen,(14,28,35),rect,border_radius=4)
            # Preserve the original label, stock display and metallic selector.
            texture=self.crop(original,(10,141,130,27))
            screen.blit(pg.transform.smoothscale(texture,rect.size),rect)
            pg.draw.rect(screen,(24,43,53),rect.inflate(-8,-8),border_radius=3)
            amount=get(item,'_stockAmount')
            enabled=amount is not U and amount>=0
            color=(223,233,235) if enabled else (126,144,151)
            label=str(get(item,'label'))
            self.text(screen,label,(rect.x+8,rect.y+13),15,color)
            count=pg.Rect(rect.right-47,rect.y+8,39,28)
            pg.draw.rect(screen,(8,22,29),count,border_radius=4)
            pg.draw.rect(screen,(93,126,140),count,1,border_radius=4)
            image=self.font(17).render(str(amount) if enabled else '-',True,color)
            screen.blit(image,image.get_rect(center=count.center))
            path=control_path(get(item,'overlayMC').node)
            self.targets.append((rect.clip(self.stock),lambda path=path:self.menu.press(path)))
        screen.set_clip(previous);self.scrollbar(screen,self.stock,pane,y)

    def scrollbar(self,screen,rect,pane,total):
        if not pane.limit:return
        track=self.pg.Rect(rect.right-5,rect.y,4,rect.h)
        self.pg.draw.rect(screen,(9,20,26),track,border_radius=2)
        height=max(18,rect.h*rect.h/total)
        thumb=self.pg.Rect(track.x,track.y+(rect.h-height)*pane.offset/pane.limit,4,height)
        self.pg.draw.rect(screen,(146,164,166),thumb,border_radius=2)

    def draw_footer(self,screen,original):
        pg=self.pg;m=self.menu
        y=self.map.bottom+5
        messages=[get(msg,'_msg') for msg in get(m.game.human,'shortMSG_arr') if truth(get(msg,'_msg'))]
        if not messages:messages=['Choose two actions, then confirm.']
        clip=pg.Rect(self.center.x+5,y,self.center.w-10,46)
        previous=screen.get_clip();screen.set_clip(clip)
        for i,line in enumerate(messages[-2:]):
            self.text(screen,str(line).replace('<br />',' '),(clip.x,clip.y+i*19),16,(57,242,35))
        screen.set_clip(previous)
        width=(self.center.w-20)//3
        for i,(label,name) in enumerate((('First action','btn44'),('Second action','btn45'),('Confirm','btn46'))):
            action=get(get(m.game.human,'turnActionArr')[i],'action') if i<2 else U
            caption=str(action).replace('preAttack','Prepared').title() if truth(action) else label
            self.button(screen,pg.Rect(self.center.x+5+i*(width+5),self.center.bottom-49,width,44),caption,lambda name=name:m.press(name),truth(action))

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
        self.gesture={'start':p,'last':p,'time':now,'pane':pane,'drag':False}
        if pane:pane.velocity=0
        elif self.stage(p) is not None:
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
            for rect,action in reversed(self.targets):
                if rect.collidepoint(p):action();break
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
