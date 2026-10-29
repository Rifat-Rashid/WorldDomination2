"""Presentation-only widescreen island spacing with reversible city hit geometry."""
from copy import copy
import math
from .display_list import Matrix
from .runtime import get


class IslandCamera:
    # Preserve the center island and the four source quadrants. Only the ocean
    # distances between islands grow; every terrain/sprite basis stays uniform.
    centers=((425,345),(140,145),(665,145),(150,500),(665,490))

    def __init__(self,rect,menu):
        import pygame
        self.pg=pygame;self.target=pygame.FRect(rect);self.clip=rect.copy();self.menu=menu
        self.scale=min(rect.w/800,rect.h/600)
        self.margin=(rect.w-800*self.scale)/2
        self.offset=(rect.x+self.margin,rect.y+(rect.h-600*self.scale)/2)
        self.city_groups={prefix+str(get(c,"cityID")):i for i,p in enumerate(menu.game.players) for c in get(p,'cityArr') for prefix in ('city','crosshair')}
        self.hits=[]
        for i,player in enumerate(menu.game.players):
            for city in get(player,'cityArr'):
                clip=menu.gameplay.city_clips.get(get(city,'cityID'))
                if clip is None:continue
                bounds=menu.renderer.control_bounds(clip.node)
                if bounds:
                    x0,y0=self.project((bounds[0]-205)/.46,(bounds[1]-135)/.46,i)
                    x1,y1=self.project((bounds[2]-205)/.46,(bounds[3]-135)/.46,i)
                    anchor=self.project(get(city,'xPos'),get(city,'yPos'),i)
                    self.hits.append((pygame.FRect(x0,y0,x1-x0,y1-y0),i,anchor))

    def shift(self,island):
        return -self.margin if island in (1,3) else self.margin if island in (2,4) else 0

    def project(self,x,y,island=0):
        return (self.offset[0]+x*self.scale+self.shift(island),self.offset[1]+y*self.scale)

    def original(self,point):
        if not self.clip.collidepoint(point):return None
        candidates=[(math.dist(point,anchor),island) for bounds,island,anchor in self.hits if bounds.collidepoint(point)]
        if candidates:island=min(candidates)[1]
        else:
            island=min(range(5),key=lambda i:math.dist(point,self.project(*self.centers[i],i)))
        return (205+(point[0]-self.offset[0]-self.shift(island))/self.scale*.46,
                135+(point[1]-self.offset[1])/self.scale*.46)

    def group(self,node):
        name=node.name or ''
        if name in self.city_groups:return self.city_groups[name]
        prefixes=('land0','land_outline_','water_overlay_','flag','carrier','ab','sub_','citypos','swp','twp')
        for prefix in prefixes:
            if name.startswith(prefix):
                rest=name[len(prefix):]
                if rest and rest[0].isdigit():return int(rest[0])
        return None

    def tree(self,battle):
        root=copy(battle);root.children={}
        root.matrix=Matrix(a=self.scale*2,d=self.scale*2,tx=self.margin*2,
                           ty=(self.target.h-600*self.scale))
        for child in battle.ordered():
            node=copy(child);matrix=child.matrix
            group=self.group(child)
            if group is not None and group<5:
                matrix=Matrix(matrix.a,matrix.b,matrix.c,matrix.d,matrix.tx+self.shift(group)/self.scale,matrix.ty)
            elif child.depth>300 and child.name not in self.city_groups:
                # Moving unit origins travel smoothly through the extra ocean.
                delta=max(-1,min(1,(matrix.tx-400)/200))*self.margin/self.scale
                matrix=Matrix(matrix.a,matrix.b,matrix.c,matrix.d,matrix.tx+delta,matrix.ty)
            node.matrix=matrix;root.children[node.depth]=node
        return root
