"""Transactional original setup -> existing Game engine -> original scene bindings."""
from .game import Game
from .generated import register_all
from .host import HeadlessHost
from .movieclip_host import MovieClipHost
from .runtime import ASObject, NativeClass, Runtime, U, arr, get, obj, truth, number
from .display_list import ColorTransform


def color_object(target=U):
    def transform(data):
        if hasattr(target, 'node'):
            mult = tuple(number(get(data, c+'a'))/100 if get(data, c+'a') is not U else 1 for c in 'rgba')
            add = tuple(number(get(data, c+'b')) if get(data, c+'b') is not U else 0 for c in 'rgba')
            target.node.color = ColorTransform(mult, add)
    def rgb(value):
        value = int(number(value))
        transform(obj({'ra': 0, 'ga': 0, 'ba': 0, 'rb': value >> 16 & 255,
                       'gb': value >> 8 & 255, 'bb': value & 255}))
    return obj({'setTransform': transform, 'setRGB': rgb})


def validate_setup(menu):
    model = menu.menu_model
    leaders = list(get(model, 'selected_leader_arr'))
    if not truth(get(menu.presenter, 'allow_game_start')):
        raise ValueError('Select at least one opponent before starting')
    if not 1 <= len(leaders) <= 4 or len(set(leaders)) != len(leaders):
        raise ValueError('Choose one to four different opponents')
    if any(not isinstance(i, int) or not 0 <= i < 19 for i in leaders):
        raise ValueError('Invalid opponent selection')
    config = {'selected_leader_arr': leaders}
    for key, allowed in [('difficulty', range(3)), ('player_color', range(1, 6)),
                         ('selected_building', range(1, 6))]:
        value = get(model, key)
        if value not in allowed:
            raise ValueError(f'Invalid setup option: {key}')
        config[key] = value
    return config


class PresentedGame(Game):
    def advance(self):
        # Preserve the existing headless turn contract: visual intervals are
        # omitted during resolution, not replayed later by the presentation clock.
        saved = {key: get(self.rt.globals, key) for key in ('setInterval', 'clearInterval')}
        callback = getattr(self, 'on_turn_results', None)
        had_results = 'turnResults' in self.presenter.props
        source_results = get(self.presenter, 'turnResults')
        if callback:
            def capture():
                self.rt.call(source_results, self.presenter, [])
                callback(self)
            self.presenter.set('turnResults', capture)
        self.rt.globals.set('setInterval', self.host.interval)
        self.rt.globals.set('clearInterval', lambda *args: U)
        try:
            return super().advance()
        finally:
            if callback:
                if had_results:
                    self.presenter.set('turnResults', source_results)
                else:
                    self.presenter.delete('turnResults')
            for key, value in saved.items():
                self.rt.globals.set(key, value)


def build_session(menu):
    """Build in isolation; the visible menu and its RNG stay intact on failure.

    No Game constructor/default nations run here. The recovered menu presenter
    creates the selected players exactly once; Game methods adopt those objects.
    """
    config = validate_setup(menu)
    rt = Runtime()
    rt.rng.setstate(menu.rt.rng.getstate())
    register_all(rt)
    headless = HeadlessHost(rt)
    tree = menu.document.root(10)
    host = MovieClipHost(rt, tree, isolate_frame_rng=True)
    for node in tree.walk():
        node.playing = False
    rt.globals.set('TextFormat', NativeClass(lambda: obj()))
    rt.globals.set('Color', NativeClass(color_object))
    model = rt.new('Model')
    rt.globals.set('model', model)
    model.set('turn', 0)
    model.set('decisionPoints', rt.new('DecisionPoints'))
    presenter = rt.new('Presenter', model)
    rt.globals.set('presenter', presenter)
    view = headless.view(get(host.root, 'battleMC'))
    view.set('textFormats', rt.new('TextFormats'))
    view.set('srcMC', get(host.root, 'interfaceMC'))
    rt.globals.set('view', view)
    presenter.set('view', view)
    # Explicitly bounded presentation dependencies; source setup/rules execute.
    interface_stub = obj()
    for name in ('update_top_plrColor', 'update_color_dots', 'reset_leader_stat_bars',
                 'updateView', 'debug_automate_func'):
        interface_stub.set(name, headless.effect(name))
    rt.globals.set('presenter_interface', interface_stub)
    rt.globals.set('view_interface', obj({'interfaceMC': get(host.root, 'interfaceMC'),
                                         'actionTube1': obj(), 'actionTube2': obj()}))
    menu_model = rt.new('Model_gameMenu')
    for key, value in config.items():
        menu_model.set(key, arr(value) if isinstance(value, list) else value)
    pm = rt.new('Presenter_gameMenu')
    pm.set('model', menu_model)
    pm.set('view', obj({'hide_gameMenu': lambda: get(host.root, 'gameMenu').set('_visible', False)}))
    rt.globals.set('model_gameMenu', menu_model)
    rt.globals.set('presenter_gameMenu', pm)
    # Source method owns color allocation, AI personalities, setup RNG and city creation.
    rt.invoke(pm, 'btn_pressed_start')
    game = PresentedGame.__new__(PresentedGame)
    game.rt, game.host, game.model, game.presenter = rt, headless, model, presenter
    game.players, game.human = get(model, 'playerArr'), get(model, 'human')
    game.events = []
    for i, player in enumerate(game.players):
        for j, city in enumerate(get(player, 'cityArr')):
            xy = get(model, 'cityPositions')[i][j]
            rt.invoke(city, 'setMapVars', get(host.root, 'battleMC'), 0, xy[0], xy[1])
            city.set('theme', get(player, 'buildingSet_id'))
            clip = headless.clip()
            clip.set('mc', headless.clip())
            clip.set('propagandaBeams', headless.clip())
            clip.set('propagandaBeams2', headless.clip())
            city.set('image', clip)
            city.set('prevPopulation', get(city, 'population'))
            clip.set('_currentframe', get(city, 'size_and_frame'))
    return game, host, tree, menu_model, pm


class OriginalGameplay:
    def __init__(self, game, host, tree):
        self.game, self.host, self.tree = game, host, tree
        self.rt = game.rt
        self.interface = get(host.root, 'interfaceMC')
        self.battle = get(host.root, 'battleMC')
        self.city_clips = {}
        from .setup_menu import reachable
        city_symbols = {host.linkages[get(city,'citySet')]
                        for player in game.players for city in get(player,'cityArr')}
        host.script_symbols.update(reachable(tree, [4658,*city_symbols]))
        for node in self.interface.node.walk():
            node.playing = bool(node.symbol.timeline)
        host.enter(self.interface.node)
        self.hud = self.rt.new('View_interface', self.interface)
        self.rt.globals.set('view_interface', self.hud)
        self.presenter = self.rt.new('Presenter_interface')
        self.presenter.set('model', game.model)
        self.presenter.set('view_interface', self.hud)
        self.presenter.set('view', get(self.rt.globals, 'view'))
        self.presenter.set('presenter', game.presenter)
        self.rt.globals.set('presenter_interface', self.presenter)
        self.source_view = ASObject(cls=self.rt.classes['View'], rt=self.rt)
        self.source_view.set('model', game.model)
        self.source_view.set('battleSrcMC', self.battle)
        self.source_view.set('srcMC', self.interface)
        # View.changeOver('toInterface')'s original viewport, in stage pixels.
        for key, value in [('_x', 205), ('_y', 135), ('_xscale', 46), ('_yscale', 46)]:
            self.battle.set(key, value)
        for name in ('introMovie', 'splashScreenMC', 'gameMenu', 'endGameMC', 'full_version_MC'):
            get(host.root, name).set('_visible', False)
        self.interface.set('_visible', True)
        from .action_entry import ActionEntry
        self.actions = ActionEntry(self)
        self.refresh()

    @property
    def selected_action(self):
        value = get(self.game.model, 'userSelectedActionBtn')
        return value if truth(value) else None

    def resolve(self):
        if (not truth(get(self.game.human, 'allActionsSet'))
                or not truth(get(self.game.human, 'alive'))
                or truth(get(self.game.human, 'diplomacyPendingArr')[0])):
            return
        owner = getattr(self, 'owner', None)
        if owner and owner.interface_sequence:
            owner.interface_sequence.cancel()
            owner.interface_sequence = None
        # View.changeOver clears transient sound clips before entering battle.
        # The adapter resolves rules synchronously, so restore that lifecycle
        # step on the canonical session before copying the presentation model.
        self.rt.invoke(self.game.presenter, 'remove_played_sound_objects')
        if owner and owner.play_battles:
            from .battle_playback import PresentationSnapshot
            self.game.on_turn_results = lambda game: setattr(owner, '_battle_snapshot', PresentationSnapshot(game))
        try:
            self.game.advance()  # Exactly one synchronous canonical resolution.
        finally:
            self.game.on_turn_results = None
        self.actions.after_turn()
        self.refresh()
        if owner and owner.play_battles:
            from .battle_playback import BattlePlayback
            owner.playback = BattlePlayback(owner, owner._battle_snapshot)
            del owner._battle_snapshot
        elif owner and owner.lifecycle:
            owner.lifecycle.check()

    def refresh(self):
        r, g = self.rt, self.game
        r.invoke(self.source_view, 'setMapFrames')
        r.invoke(self.source_view, 'resetActionBuildings')
        r.invoke(self.source_view, 'update_flags')
        r.invoke(self.presenter, 'update_statistics')
        r.invoke(self.presenter, 'update_top_plrColor')
        r.invoke(self.presenter, 'update_color_dots')
        r.invoke(self.hud, 'update_highScore', get(g.human, 'score'))
        for i in range(1, 5):
            player = g.players[i]
            if player is U:
                r.invoke(self.hud, 'update_leaderFace', i, 20, True, True)
            else:
                r.invoke(self.hud, 'update_leaderFace', i, get(player, 'faceFrame'), get(player, 'alive'), False, True)
        for player in g.players:
            for city in get(player, 'cityArr'):
                cid = get(city, 'cityID')
                if cid not in self.city_clips:
                    self.city_clips[cid] = r.invoke(self.battle, 'attachMovie', get(city, 'citySet'), f'city{cid}', get(city, 'image_depth'))
                clip = self.city_clips[cid]
                clip.set('_x', get(city, 'xPos'))
                clip.set('_y', get(city, 'yPos'))
                clip.set('_xscale', 80)
                clip.set('_yscale', 80)
                r.invoke(clip, 'gotoAndStop', get(get(city, 'image'), '_currentframe'))
        self.actions.update()
        self.interface.set('turn', get(g.model, 'turn'))
        self.interface.set('activePlayer', get(g.human, 'playerNum'))

    def controls(self):
        return self.actions.controls()
