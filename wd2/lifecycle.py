"""Original end-game timelines and in-window restart presentation."""
from contextlib import contextmanager
import random

from .action_entry import control_path, visible
from .runtime import ASObject, U, get, truth


class Lifecycle:
    def __init__(self, menu):
        self.menu, self.game = menu, menu.game
        self.rt, self.host = menu.rt, menu.host
        self.status = None
        self.missing_calls = {}
        self.presentation_rng = random.Random()
        self.presentation_rng.setstate(self.rt.rng.getstate())

    @contextmanager
    def scope(self):
        original_model, original_rng = get(self.rt.globals, 'model'), self.rt.rng
        original_missing = self.rt.missing_calls
        self.rt.missing_calls = self.missing_calls
        math_object = get(self.rt.globals, 'Math')
        original_random = get(math_object, 'random')
        self.rt.globals.set('model', self.model)
        self.rt.rng = self.presentation_rng
        math_object.set('random', self.presentation_rng.random)
        try:
            yield
        finally:
            self.rt.globals.set('model', original_model)
            self.rt.rng = original_rng
            math_object.set('random', original_random)
            self.rt.missing_calls = original_missing

    def check(self):
        if self.status:
            return
        if not truth(get(self.game.human, 'alive')):
            status = 'lost'
        elif len(get(self.game.model, 'activePlayerArr')) == 1:
            status = 'win'
        else:
            return
        self.status = status
        # The score animation changes its own counters and may zero a cheated
        # score. Keep those writes and visual RNG off the resolved game.
        self.model = ASObject(self.game.model.props.copy(), cls=self.game.model.cls, rt=self.rt)
        self.model.set('human', ASObject(self.game.human.props.copy(), cls=self.game.human.cls, rt=self.rt))
        view = self.view = ASObject(cls=self.rt.classes['View'], rt=self.rt)
        for key, value in [('model', self.model), ('view_interface', self.menu.gameplay.hud),
                           ('presenter_interface', self.menu.gameplay.presenter),
                           ('presenter', self.game.presenter), ('battleSrcMC', self.menu.gameplay.battle)]:
            view.set(key, value)
        self.source_show = get(view, 'end_game_sequence')
        self.source_score = get(view, 'end_game_sequence_2')
        view.set('end_game_sequence', self.show)
        view.set('end_game_sequence_2', self.score)
        get(self.host.root, 'endGameMC').set('presenter_interface', self.menu.gameplay.presenter)
        with self.scope():
            self.rt.invoke(view, 'interface_before_end_game_sequence', status)

    def show(self, status):
        with self.scope():
            self.rt.call(self.source_show, self.view, [status])

    def score(self, status):
        with self.scope():
            self.rt.call(self.source_score, self.view, [status])
        end = get(self.host.root, 'endGameMC')
        callback = get(end, 'onEnterFrame')
        if callback is not U:
            def tick():
                with self.scope():
                    self.rt.call(callback, end, [])
            end.set('onEnterFrame', tick)
        get(end, 'btn_new').set('onPress', self.menu.restart)

    def controls(self):
        root = get(self.host.root, 'endGameMC').node
        return [n for n in root.walk() if visible(n) and get(self.host.wrap(n), 'onPress') is not U]

    def press(self, name):
        if name in ('btn38', 'btn39'):
            return self.host.dispatch(self.menu.gameplay.interface.node.named(name), 'onPress')
        node = next((n for n in self.controls() if control_path(n) == name or n.name == name), None)
        return self.host.dispatch(node, 'onPress') if node else U

    def control_at(self, pos):
        for node in reversed(self.controls()):
            b = self.menu.renderer.control_bounds(node)
            if b and b[0] <= pos[0] <= b[2] and b[1] <= pos[1] <= b[3]:
                return control_path(node)
        return None
