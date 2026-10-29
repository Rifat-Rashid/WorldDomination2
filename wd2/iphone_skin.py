"""Mobile-only metallic chrome and vector pictograms over reviewed game assets."""
import math
from copy import copy
from .display_list import Matrix


class MobileSkin:
    def __init__(self, menu, pg):
        from .surface_renderer import SurfaceRenderer
        self.pg = pg
        # One immutable, high-resolution chrome source. No live selection text
        # or orange action state is ever sampled for a mobile button texture.
        def clone(node,parent=None):
            view=copy(node);view.parent=parent
            view.children={depth:clone(child,view) for depth,child in node.children.items()}
            if node.name=='centerScreen':view.visible=False
            if node.name.startswith('scrn') and node.symbol.timeline:
                view.goto_and_stop(1)
            return view
        root = clone(menu.tree)
        root.matrix = Matrix(a=3, d=3)
        self.source = SurfaceRenderer(menu.renderer, pg).frame(root, (2400, 1800)).copy()
        self.cache = {}
        self.icons = {}
        self.texture = self.crop((45, 4, 110, 12)).copy()

    def crop(self, rect):
        x,y,w,h = rect
        return self.source.subsurface(self.pg.Rect(round(x*3),round(y*3),round(w*3),round(h*3)))

    def nine(self, source, size, edge=8):
        pg=self.pg; key=(source,tuple(size),edge)
        if key in self.cache:return self.cache[key]
        image=self.crop(source);sw,sh=image.get_size();dw,dh=map(int,size)
        result=pg.Surface((dw,dh))
        e=min(edge,dw//3,dh//3);se=edge*3
        xs=(0,se,sw-se,sw);ys=(0,se,sh-se,sh)
        dx=(0,e,dw-e,dw);dy=(0,e,dh-e,dh)
        for j in range(3):
            for i in range(3):
                patch=image.subsurface((xs[i],ys[j],xs[i+1]-xs[i],ys[j+1]-ys[j]))
                result.blit(pg.transform.smoothscale(patch,(dx[i+1]-dx[i],dy[j+1]-dy[j])),(dx[i],dy[j]))
        if len(self.cache)>=96:self.cache.pop(next(iter(self.cache)))
        self.cache[key]=result
        return result

    def panel(self,screen,rect,title=None,font=None):
        pg=self.pg
        pg.draw.rect(screen,(5,14,20),rect,border_radius=7)
        pg.draw.rect(screen,(108,139,152),rect.inflate(-2,-2),1,border_radius=6)
        inner=rect.inflate(-7,-7)
        tile=pg.transform.smoothscale(self.texture,(160,14))
        previous=screen.get_clip();screen.set_clip(previous.clip(inner))
        for y in range(inner.top,inner.bottom,14):
            for x in range(inner.left,inner.right,160):screen.blit(tile,(x,y))
        tint=pg.Surface(inner.size,pg.SRCALPHA);tint.fill((0,30,49,130));screen.blit(tint,inner)
        screen.set_clip(previous)
        pg.draw.line(screen,(121,152,165),(rect.x+8,rect.y+2),(rect.right-8,rect.y+2))
        pg.draw.line(screen,(5,13,18),(rect.x+8,rect.bottom-3),(rect.right-8,rect.bottom-3))
        if rect.h>42:
            for x,y in ((rect.x+5,rect.y+6),(rect.right-6,rect.y+6),(rect.x+5,rect.bottom-7),(rect.right-6,rect.bottom-7)):
                pg.draw.circle(screen,(73,106,120),(x,y),3)
                pg.draw.circle(screen,(4,14,20),(x,y),2)
                pg.draw.line(screen,(146,169,179),(x-1,y-2),(x+1,y-2))
        if title and font:
            label=font.render(title,True,(191,209,213));plate=label.get_rect(center=(rect.centerx,rect.y+5)).inflate(14,1)
            pg.draw.rect(screen,(18,34,43),plate,border_radius=5);screen.blit(label,label.get_rect(center=plate.center))

    def button(self,screen,rect,selected=False):
        pg=self.pg
        screen.blit(self.nine((14,144,127,18),rect.size,4),rect)
        inner=rect.inflate(-5,-6)
        for y in range(inner.h):
            f=y/max(1,inner.h-1)
            top=(42,90,115) if selected else (48,66,75)
            bottom=(12,47,68) if selected else (11,23,29)
            color=tuple(round(a+(b-a)*f) for a,b in zip(top,bottom))
            pg.draw.line(screen,color,(inner.x,inner.y+y),(inner.right-1,inner.y+y))
        pg.draw.line(screen,(116,147,163),(rect.x+5,rect.y+3),(rect.right-5,rect.y+3))

    def well(self,screen,rect):
        pg=self.pg
        pg.draw.rect(screen,(82,110,123),rect,border_radius=4)
        inner=rect.inflate(-3,-3)
        for y in range(inner.h):
            f=y/max(1,inner.h-1)
            color=(round(22*(1-f)),round(43*(1-f)+5),round(50*(1-f)+7))
            pg.draw.line(screen,color,(inner.x,inner.y+y),(inner.right-1,inner.y+y))
        pg.draw.line(screen,(121,152,163),(rect.x+4,rect.y+1),(rect.right-4,rect.y+1))

    def icon(self,name,size,color=(225,233,235)):
        key=(name,size,color)
        if key in self.icons:return self.icons[key]
        pg=self.pg; k=3;s=pg.Surface((96,96),pg.SRCALPHA)
        def pts(points):return [(round(x*k),round(y*k)) for x,y in points]
        def line(points,width=1.5,c=color):pg.draw.lines(s,c,False,pts(points),max(1,round(width*k)))
        def poly(points,c=color):pg.draw.polygon(s,c,pts(points))
        def circle(p,r,c=color,width=0):pg.draw.circle(s,c,pts([p])[0],round(r*k),round(width*k))
        def ellipse(rect,width=1.3,c=color):pg.draw.ellipse(s,c,[round(v*k) for v in rect],round(width*k))
        if name=='resources':
            for x,y in ((5,18),(13,10),(21,16)):
                for j in range(3):ellipse((x,y+j*3,8,4))
                line([(x,y+2),(x,y+8)]);line([(x+8,y+2),(x+8,y+8)])
        elif name=='production':
            poly([(3,28),(3,16),(10,12),(10,18),(17,13),(17,20),(28,20),(28,28)])
            poly([(21,19),(22,4),(26,4),(27,20)])
            for x in (7,13,19,25):pg.draw.rect(s,(32,57,67),(x*k,23*k,2*k,4*k))
        elif name=='research':
            line([(12,3),(20,3)]);line([(14,3),(14,12),(6,26),(7,29),(25,29),(26,26),(18,12),(18,3)])
            poly([(10,22),(22,22),(25,27),(7,27)],(185,211,219))
        elif name in ('religion','propaganda'):
            if name=='religion':
                poly([(5,7),(8,21),(20,25),(24,22)],(180,207,218));line([(7,5),(27,25)],2);line([(19,15),(25,9)],2);line([(15,24),(13,29),(24,29)],2)
            else:
                pg.draw.rect(s,color,(4*k,10*k,24*k,18*k),2*k,border_radius=3*k);line([(12,3),(17,8),(24,2)]);pg.draw.rect(s,color,(8*k,14*k,13*k,10*k),k,border_radius=2*k);circle((25,16),1)
        elif name=='attack':
            circle((16,16),10,width=2)
            for p in [[(16,1),(16,10)],[(16,22),(16,31)],[(1,16),(10,16)],[(22,16),(31,16)]]:line(p,2)
        elif name in ('preAttack','rocket'):
            poly([(9,23),(12,12),(24,2),(26,4),(24,16),(17,25)],(217,230,234));poly([(12,20),(6,22),(5,29),(13,25)],(181,42,30));poly([(21,17),(24,23),(19,29),(17,24)],(181,42,30));circle((20,9),2,(55,93,109));line([(10,27),(7,31)],2)
        elif name=='defense':
            line([(5,5),(16,2),(27,5),(25,20),(16,30),(7,20),(5,5)],2);line([(16,6),(16,25)],1)
        elif name=='diplomacy':
            line([(2,12),(9,7),(15,10),(20,7),(30,13),(23,25),(17,27),(8,21),(2,12)],2);line([(9,15),(15,10),(24,18),(20,23),(16,19)],2);line([(9,22),(13,17)],2)
        elif name=='plane':
            poly([(16,1),(19,13),(30,22),(29,25),(19,21),(20,28),(24,31),(16,29),(8,31),(12,28),(13,21),(3,25),(2,22),(13,13)],(218,230,235));line([(16,4),(16,27)],1,(108,137,149))
        elif name=='ship':
            poly([(2,19),(28,17),(24,26),(8,29)],(165,187,197));poly([(6,15),(24,12),(29,16),(3,20)],(217,229,233));poly([(16,6),(20,5),(21,13),(15,15)],(185,205,211));line([(17,5),(17,1)],1)
        elif name=='warhead':
            yellow=(255,186,36);circle((16,16),14,yellow);circle((16,16),12,(10,20,25));circle((16,16),3,yellow)
            for angle in (30,150,270):
                a=math.radians(angle);points=[(16+5*math.cos(a-.45),16+5*math.sin(a-.45)),(16+11*math.cos(a-.45),16+11*math.sin(a-.45)),(16+11*math.cos(a+.45),16+11*math.sin(a+.45)),(16+5*math.cos(a+.45),16+5*math.sin(a+.45))];poly(points,yellow)
        elif name=='bio':
            yellow=(240,161,38);circle((16,17),3,yellow)
            for x,y in ((16,9),(9,22),(23,22)):
                circle((x,y),7,yellow);circle((x,y),5,(20,40,49))
            for a in (90,210,330):
                a=math.radians(a);line([(16+3*math.cos(a),17+3*math.sin(a)),(16+8*math.cos(a),17+8*math.sin(a))],2,yellow)
        elif name=='spy':
            poly([(4,13),(8,8),(24,8),(28,13),(25,15),(7,15)]);poly([(10,8),(12,3),(21,3),(23,8)]);line([(8,19),(14,19),(16,21),(19,19),(25,19)],3);line([(5,30),(9,24),(23,24),(28,30)],3)
        elif name=='gear':
            circle((16,16),10,width=4)
            for a in range(0,360,45):
                a=math.radians(a);line([(16+9*math.cos(a),16+9*math.sin(a)),(16+14*math.cos(a),16+14*math.sin(a))],5)
        else:circle((16,16),10,width=2)
        result=pg.transform.smoothscale(s,(size,size));self.icons[key]=result;return result
