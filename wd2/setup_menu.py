"""Original splash, setup and bounded gameplay scene driven by recovered AS2."""
import argparse
import io
import json
import sys
from pathlib import Path

from .generated import register_all
from .generated.Main import f_8 as show_menu
from .generated.Main import f_1 as play_action_sound
from .menu_audio import MenuAudio, PygameMenuAudio
from .movieclip_host import MovieClipHost
from .menu_renderer import MenuRenderer
from .runtime import Runtime, ASObject, ASFunction, NativeClass, get, obj, U
from .scene_renderer import SVGAssets
from .swf_scene import ROOT, SWFDocument
from .scene_data import load_scene


def reachable(document, seeds):
    found, pending = set(), list(seeds)
    while pending:
        sid = pending.pop()
        if sid in found:
            continue
        found.add(sid)
        timeline = document.symbols[sid].timeline
        if timeline:
            pending.extend(op.values['character_id'] for ops in timeline.frames for op in ops
                           if 'character_id' in op.values)
    return found


class CachedAssets(SVGAssets):
    def __init__(self):
        super().__init__()
        self.cache = {}

    def load(self, symbol):
        if symbol.character_id not in self.cache:
            self.cache[symbol.character_id] = super().load(symbol)
        return self.cache[symbol.character_id]


class SetupMenu:
    def __init__(self, seed=0, document=None):
        self.document = document or load_scene()
        self.tree = self.document.root(10)
        self.rt = Runtime(seed)  # Dedicated menu RNG; no Game instance is touched.
        register_all(self.rt)
        scripts = reachable(self.document, (5882, 5907))
        self.host = MovieClipHost(self.rt, self.tree, scripts)
        self.root = self.host.root
        # Unbound regions remain inspection state, not uncontrolled gameplay.
        for node in self.tree.walk():
            if node.character_id not in scripts:
                node.playing = False
        self.host.enter(self.tree.named('gameMenu'))
        self.host.enter(self.tree.named('splashScreenMC'))
        self.effects = []
        self.rt.globals.set('play_sound_by_action', lambda name: self.effects.append(('sound', name)))
        self.rt.globals.set('TextFormat', NativeClass(lambda: obj()))
        self.model = self.rt.new('Model')
        self.rt.globals.set('model', self.model)
        # Main.as:28-52, menu-only dependencies. Execute original View methods
        # on a scoped instance without constructing its combat/interface side.
        view = ASObject(cls=self.rt.classes['View'], rt=self.rt)
        view.set('model', self.model)
        view.set('battleSrcMC', get(self.root, 'battleMC'))
        view.set('textFormats', self.rt.new('TextFormats'))
        self.rt.globals.set('view', view)
        self.menu_model = self.rt.new('Model_gameMenu')
        self.presenter = self.rt.new('Presenter_gameMenu')
        self.view = self.rt.new('View_gameMenu', get(self.root, 'gameMenu'))
        for name, value in (('model_gameMenu', self.menu_model), ('presenter_gameMenu', self.presenter),
                            ('view_gameMenu', self.view)):
            self.rt.globals.set(name, value)
        self.menu_model.set('presenter', self.presenter)
        self.presenter.set('model', self.menu_model)
        self.presenter.set('view', self.view)
        self.rt.invoke(self.presenter, 'initialize_gameMenu')
        # Original Main/Presenter_interface audio wiring, scoped to the menu.
        self.audio = MenuAudio(self.rt, self.document)
        interface = ASObject(cls=self.rt.classes['Presenter_interface'], rt=self.rt)
        interface.set('model', self.model)
        interface.set('view', view)
        self.rt.globals.set('presenter_interface', interface)
        self.rt.globals.set('play_sound_by_action', ASFunction(play_action_sound))
        view.set('srcMC', self.rt.invoke(self.root, 'createEmptyMovieClip', 'menu_sound_mc',
                                        self.rt.invoke(self.root, 'getNextHighestDepth')))
        theme_clip = self.rt.invoke(self.root, 'createEmptyMovieClip', 'theme_sound_mc',
                                    self.rt.invoke(self.root, 'getNextHighestDepth'))
        theme = self.rt.new('Sound', theme_clip)
        self.rt.invoke(theme, 'attachSound', 'WDTheme.wav')
        self.audio.theme = theme
        self.model.set('theme_sound', theme)
        self.rt.invoke(get(self.model, 'option'), 'setMusic')
        # Our entry starts at the title splash, where the original intro's final
        # frame / Main intro handler calls this method to start looping music.
        self.rt.invoke(interface, 'init_theme_snd')
        # Main.as:108-124 visibility and the exact translated splash callback.
        for name in ('introMovie', 'interfaceMC', 'gameMenu', 'endGameMC', 'full_version_MC'):
            get(self.root, name).set('_visible', False)
        splash = get(self.root, 'splashScreenMC')
        splash.set('_visible', True)
        splash.set('onPress', ASFunction(show_menu))
        self.renderer = MenuRenderer(self.document, CachedAssets(), self.host)
        self.hovered = None
        self.bounds = {n.name: self.renderer.control_bounds(n) for n in self.tree.named('gameMenu').ordered()
                       if n.name and get(self.host.wrap(n), 'onPress') is not U}
        self.game = None
        self.gameplay = None
        self.last_error = None

    def start_game(self):
        if self.game is not None:
            return self.game
        from .original_gameplay import build_session, OriginalGameplay
        try:
            game, host, tree, menu_model, presenter = build_session(self)
            gameplay = OriginalGameplay(game, host, tree)
        except ValueError as error:
            self.last_error = str(error)
            return None
        # Commit only after source setup and the original presentation are ready.
        old_option = get(self.model, 'option')
        for key in ('music', 'sound'):
            get(game.model, 'option').set(key, get(old_option, key))
        game.model.set('theme_sound', self.audio.theme)
        self.audio.rt = game.rt
        game.rt.globals.set('Sound', NativeClass(self.audio.new_sound))
        game.rt.globals.set('play_sound_by_action', ASFunction(play_action_sound))
        host.clock.ticks = self.host.clock.ticks
        host.clock.paused = self.host.clock.paused
        self.game, self.gameplay = game, gameplay
        self.rt, self.host, self.tree, self.root = game.rt, host, tree, host.root
        self.model, self.menu_model, self.presenter = game.model, menu_model, presenter
        self.renderer = MenuRenderer(self.document, self.renderer.assets, host)
        self.hovered = None
        self.last_error = None
        return game

    def press(self, name):
        """Dispatch original callbacks by instance name (also used by validation)."""
        if name == 'btn_start':
            return self.start_game()
        if self.gameplay:
            node = next((n for n in self.gameplay.controls() if n.name == name), None)
            if node:
                return self.host.dispatch(node, 'onPress')
            return U
        node = self.tree.named('splashScreenMC') if name == 'splashScreenMC' else self.tree.named('gameMenu').named(name)
        if node is None:
            raise ValueError(f'No setup control {name}')
        return self.host.dispatch(node, 'onPress')

    def png(self):
        return self.renderer.png(self.tree)

    def surface(self, pygame):
        from .surface_renderer import SurfaceRenderer
        cached = getattr(self, '_surface_renderer', None)
        if cached is None or cached.renderer is not self.renderer:
            self._surface_renderer = SurfaceRenderer(self.renderer, pygame)
        return self._surface_renderer.frame(self.tree)

    def control_at(self, pos):
        if self.gameplay:
            for node in reversed(self.gameplay.controls()):
                bounds = self.renderer.control_bounds(node)
                if node.visible and bounds and bounds[0] <= pos[0] <= bounds[2] and bounds[1] <= pos[1] <= bounds[3]:
                    return node.name
            return None
        if self.tree.named('splashScreenMC').visible:
            return 'splashScreenMC'
        if not self.tree.named('gameMenu').visible:
            return None
        for node in reversed(self.tree.named('gameMenu').ordered()):
            bounds = self.bounds.get(node.name)
            if node.visible and bounds and bounds[0] <= pos[0] <= bounds[2] and bounds[1] <= pos[1] <= bounds[3]:
                return node.name
        return None

    def click(self, pos):
        name = self.control_at(pos)
        if name:
            self.press(name)

    def motion(self, pos):
        if self.gameplay:
            return
        name = self.control_at(pos)
        if name != self.hovered:
            menu = self.tree.named('gameMenu')
            if self.hovered and menu.named(self.hovered):
                self.host.dispatch(menu.named(self.hovered), 'onRollOut')
            if name and menu.named(name):
                self.host.dispatch(menu.named(name), 'onRollOver')
            self.hovered = name

    def snapshot(self):
        if self.game:
            return {'scene': 'gameplay', 'game': self.game.snapshot(), 'ticks': self.host.clock.ticks,
                    'selected_leaders': list(get(self.menu_model, 'selected_leader_arr'))}
        return {'selected_leaders': list(get(self.menu_model, 'selected_leader_arr')),
                'difficulty': get(self.menu_model, 'difficulty'),
                'color': get(self.menu_model, 'player_color'),
                'building': get(self.menu_model, 'selected_building'),
                'missing_calls': dict(self.rt.missing_calls), 'ticks': self.host.clock.ticks}

    def save(self, path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(self.png())
        report = {'state': self.snapshot(), 'rendering': self.renderer.report,
                  'audio': {'theme': self.audio.theme.linkage, 'music_enabled': get(get(self.model, 'option'), 'music'),
                            'device_connected': self.audio.backend is not None},
                  'scope': 'Recovered setup and original HUD; synchronous existing game engine, Resources and Mass Media controls.'}
        path.with_suffix('.json').write_text(json.dumps(report, indent=2), encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--screenshot', type=Path)
    parser.add_argument('--select-first', action='store_true')
    parser.add_argument('--splash', action='store_true', help='Capture the initialized title splash')
    parser.add_argument('--start-game', action='store_true', help='Start after selecting the first opponent')
    parser.add_argument('--smoke', action='store_true', help='Start and resolve one turn through original controls')
    parser.add_argument('--svg-renderer', action='store_true', help='Use the uncached SVG window renderer')
    args = parser.parse_args()
    menu = SetupMenu(args.seed)
    if (args.screenshot and not args.splash) or args.select_first or args.start_game or args.smoke:
        menu.press('splashScreenMC')
    if args.select_first or args.start_game or args.smoke:
        menu.press('BTN_allLeaders_screen1')
    if args.start_game or args.smoke:
        menu.press('btn_start')
    if args.smoke:
        for name in ('btn1', 'btnAccept', 'btn4', 'btnAccept', 'btn46'):
            menu.press(name)
    if args.screenshot:
        menu.save(args.screenshot)
        return
    run_window(menu, cached=not args.svg_renderer)


def run_window(menu, cached=True):
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('World Domination II')
    pacing = pygame.time.Clock()
    accumulator = 0
    try:
        try:
            menu.audio.connect(PygameMenuAudio(menu.audio, pygame))
        except pygame.error as error:
            pygame.display.set_caption(f'World Domination II — audio unavailable: {error}')
            print(f'Audio unavailable: {error}', file=sys.stderr)
        running = True
        while running:
            accumulator += pacing.tick(24) * 24
            ticks, accumulator = divmod(accumulator, 1000)
            menu.audio.poll()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    menu.host.clock.paused = not menu.host.clock.paused
                    menu.audio.pause(menu.host.clock.paused)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    menu.click(event.pos)
                elif event.type == pygame.MOUSEMOTION:
                    menu.motion(event.pos)
            menu.host.clock.step(ticks)
            frame = menu.surface(pygame) if cached else pygame.image.load(io.BytesIO(menu.png()))
            screen.blit(frame, (0, 0))
            pygame.display.flip()
    finally:
        menu.audio.close()
        pygame.quit()


if __name__ == '__main__':
    main()
