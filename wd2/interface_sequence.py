"""Recovered timed HUD startup/return without re-running resolved game rules."""
from contextlib import contextmanager

from .runtime import ASObject, U, get, number


class InterfaceSequence:
    def __init__(self, menu, initial=False):
        self.menu, self.rt, self.host = menu, menu.rt, menu.host
        self.presenter = menu.game.presenter
        original = get(self.rt.globals,'view')
        # Keep the established headless city/update methods. Only View's timed
        # interface methods are added; casualties and turn finalization stay out.
        self.view = ASObject(original.props.copy(),cls=self.rt.classes['View'],rt=self.rt)
        for name,value in [('model',menu.model),('presenter',self.presenter),
                           ('view_interface',menu.gameplay.hud),
                           ('presenter_interface',menu.gameplay.presenter)]:
            self.view.set(name,value)
        self.timers = set()
        self.missing_calls = {}
        self.done = False
        if initial:
            menu.model.set('view_leader_MCs_played','false')
            menu.model.set('view_leader_MCs_played_count',0)
        timer = self.interval(self.view,'to_interface_timed_3',5)
        self.presenter.set('allUnitsDone_intervalID',timer)

    @contextmanager
    def scope(self):
        old_view = get(self.rt.globals,'view')
        old_interval = get(self.rt.globals,'setInterval')
        old_missing = self.rt.missing_calls
        self.rt.missing_calls = self.missing_calls
        self.rt.globals.set('view',self.view)
        self.rt.globals.set('setInterval',self.interval)
        try:
            with self.host.presentation_randomness():
                yield
        finally:
            self.rt.globals.set('view',old_view)
            self.rt.globals.set('setInterval',old_interval)
            self.rt.missing_calls = old_missing

    def interval(self,*args):
        if len(args) >= 3 and isinstance(args[1],str):
            target,method,period,*params = args
            invoke = lambda:self.rt.invoke(target,method,*params)
        else:
            fn,period,*params = args
            invoke = lambda:self.rt.call(fn,self.rt.globals,params)
        def callback():
            with self.scope():
                invoke()
            timer = get(self.presenter,'allUnitsDone_intervalID')
            if (not self.done and timer not in self.host.clock.timers
                    and get(self.menu.model,'view_leader_MCs_played') == 'done'):
                self.done = True
        timer = self.host.clock.set_interval(callback,number(period))
        self.timers.add(timer)
        return timer

    def cancel(self):
        for timer in self.timers:
            self.host.clock.clear_interval(timer)
        leader_timer = get(self.menu.model,'view_leader_MCs_sequence_interval_id')
        if leader_timer is not U:
            self.host.clock.clear_interval(leader_timer)
        self.menu.model.set('view_leader_MCs_played','done')
        self.done = True
