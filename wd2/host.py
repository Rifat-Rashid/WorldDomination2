"""Explicit non-rendering host for testing recovered gameplay independently of Flash."""
from .runtime import ASObject, U, obj


class HeadlessHost:
    def __init__(self,rt):
        self.rt=rt; self.effects={}; self.state='playing'
        rt.globals.set('clearInterval',lambda *args:U)
        rt.globals.set('setInterval',self.interval)
        rt.globals.set('debug',obj({'skip_battle_animation':True}))
        for name in ('play_sound_by_action','play_sound_by_building','play_sound_by_event','explosion_sound_by_mc_name'):
            rt.globals.set(name,self.effect(name))
    def effect(self,name):
        def call(*args): self.effects[name]=self.effects.get(name,0)+1; return U
        return call
    def interval(self,*args):
        self.effects['setInterval']=self.effects.get('setInterval',0)+1
        return 0
    def clip(self):
        clip=obj({'_currentframe':1,'_visible':True,'_x':0,'_y':0})
        clip.set('gotoAndStop',lambda frame:clip.set('_currentframe',frame))
        clip.set('gotoAndPlay',lambda frame:clip.set('_currentframe',frame))
        for name in ('play','stop','removeMovieClip','setTransform'): clip.set(name,self.effect(name))
        return clip
    def view(self,battle):
        view=obj({'battleSrcMC':battle})
        for name in ('updateCities','updateView','resetActionBuildings','setMapFrames','updateIMG','setFaceFrames','colorCities','update_flags','city_shrink_sequence'):
            view.set(name,self.effect(name))
        def change(state):
            self.state=state; return U
        view.set('changeOver',change)
        return view
