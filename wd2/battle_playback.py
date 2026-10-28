"""Recovered battle presentation on an isolated copy of a resolved turn.

The canonical Game still resolves each turn synchronously. This copy owns all
animation callbacks, visual casualties and random calls; none can reach Game.
"""
from .runtime import ASArray, ASClass, ASFunction, ASObject, Scope, Runtime, U, get, obj, NativeClass
from .generated import register_all


class PresentationSnapshot:
    def __init__(self, game):
        self.rt = Runtime()
        register_all(self.rt)
        self.memo = {}
        self.model = self.copy(game.model)
        self.rt.rng.setstate(game.rt.rng.getstate())
        self.rt.globals.set('model', self.model)

    def copy(self, value):
        if id(value) in self.memo:
            return self.memo[id(value)]
        if isinstance(value, ASClass):
            return self.rt.classes[value.name]
        if isinstance(value, ASFunction):
            target = ASFunction(value.fn)
            self.memo[id(value)] = target
            target.closure = self.copy(value.closure)
            return target
        if isinstance(value, Scope):
            target = Scope(self.rt, U, [], [], [])
            self.memo[id(value)] = target
            target.this = self.copy(value.this)
            target.closure, target.owner = self.copy(value.closure), value.owner
            target.values = {k: self.copy(v) for k, v in value.values.items()}
            return target
        if isinstance(value, ASObject):
            cls = self.rt.classes[value.cls.name] if value.cls else None
            target = ASArray() if isinstance(value, ASArray) else ASObject(cls=cls, rt=self.rt)
            self.memo[id(value)] = target
            props = {}
            if value.cls:
                for source_cls in reversed(value.cls.lineage()):
                    source_cls.initialize_fields()
                    props.update(source_cls.prototype.props)
            props.update(value.props)
            target.props = {k: self.copy(v) for k, v in props.items()}
            if isinstance(value, ASArray):
                target.items = [self.copy(v) for v in value.items]
            return target
        # Native host closures must never retain the live game or headless host.
        if callable(value):
            return U
        if isinstance(value, dict):
            return {k: self.copy(v) for k, v in value.items()}
        if isinstance(value, (list, tuple)):
            return [self.copy(v) for v in value]
        return value


class BattlePlayback:
    def __init__(self, menu, snapshot):
        from .movieclip_host import MovieClipHost
        from .original_gameplay import color_object
        from .menu_audio import MenuAudio
        from .menu_renderer import MenuRenderer
        from .generated import Main
        from .setup_menu import reachable
        self.menu, self.rt, self.model = menu, snapshot.rt, snapshot.model
        self.tree = menu.document.root(10)
        scripts = reachable(menu.document, [5766]+[sid for sid, s in menu.document.symbols.items() if s.linkage and s.kind == 39])
        self.host = MovieClipHost(self.rt, self.tree, scripts)
        for node in self.tree.ordered():
            if node.name:
                node.visible = node.name == 'battleMC'
            node.playing = False
        self.tree.playing = False
        self.rt.globals.set('TextFormat', NativeClass(lambda: obj()))
        self.rt.globals.set('Color', NativeClass(color_object))
        def broadcaster(target):
            target.set('addListener', lambda *args: U)
        self.rt.globals.set('AsBroadcaster', obj({'initialize': broadcaster}))
        self.rt.globals.set('debug', obj({'skip_battle_animation': False}))
        for path in ('bioCloud.as', 'cloud.as', 'spaceRocket_smoke.as', 'spaceRocket_trail_element.as'):
            self.rt.call(self.rt.scripts[path], self.rt.globals, [])
        self.audio = MenuAudio(self.rt, menu.document)
        self.audio.backend = menu.audio.backend
        for name, fn in [('play_sound_by_action', Main.f_1), ('play_sound_by_building', Main.f_2),
                         ('play_sound_by_event', Main.f_3), ('explosion_sound_by_mc_name', Main.f_4)]:
            self.rt.globals.set(name, ASFunction(fn))
        self.presenter = self.rt.new('Presenter', self.model)
        self.rt.globals.set('presenter', self.presenter)
        self.battle = get(self.host.root, 'battleMC')
        self.view = self.rt.new('View', self.model, self.presenter,
                                get(self.host.root, 'interfaceMC'), self.battle)
        self.rt.globals.set('view', self.view)
        self.presenter.set('view', self.view)
        self.hud = self.rt.new('View_interface', get(self.host.root, 'interfaceMC'))
        self.rt.globals.set('view_interface', self.hud)
        interface = self.rt.new('Presenter_interface')
        for key, value in [('model', self.model), ('view_interface', self.hud),
                           ('view', self.view), ('presenter', self.presenter)]:
            interface.set(key, value)
        self.rt.globals.set('presenter_interface', interface)
        self.view.set('presenter_interface', interface)
        self.view.set('view_interface', self.hud)
        for player in get(self.model, 'playerArr'):
            for city in get(player, 'cityArr'):
                city.set('mapMC', self.battle)
                self.rt.invoke(self.view, 'spawnCity', city, 'battleMap')
        self.rt.invoke(self.view, 'setMapFrames')
        self.rt.invoke(self.view, 'resetActionBuildings')
        self.rt.invoke(self.view, 'updateCities')
        self.rt.invoke(self.view, 'changeOver', 'toBattle')
        self.done = False
        self.presenter.set('endBattle', self.finish)
        self.host.enter(self.battle.node)
        self.rt.invoke(self.presenter, 'initBattle')
        self.renderer = MenuRenderer(menu.document, menu.renderer.assets, self.host)

    def finish(self):
        self.done = True
        self.host.clock.timers.clear()
        self.audio.close()

    def step(self, ticks=1):
        for _ in range(ticks):
            if self.done:
                break
            self.rt.reset_budget()
            self.host.clock.step()
