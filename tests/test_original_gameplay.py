import hashlib
import io
import json

from PIL import Image
import pytest

from wd2.game import Game
from wd2.runtime import U, get, arr, truth
from wd2.setup_menu import SetupMenu


def selected_menu(difficulty=1):
    menu = SetupMenu(0)
    menu.press('splashScreenMC')
    menu.press(f'btn{difficulty+1}')
    menu.press('BTN_allLeaders_screen1')
    menu.press('BTN_allLeaders_screen2')
    return menu


def test_start_preserves_source_configuration_and_is_idempotent():
    menu = selected_menu(2)
    assert menu.game is None
    game = menu.press('btn_start')
    assert game is not None and len(game.players) == 3
    assert game.human is get(game.model, 'human')
    assert get(game.model, 'difficulty_level') == 2
    assert get(game.human, 'religion_code') == 'jew'
    assert get(game.human, 'buildingSet_id') == 'jewish_buildings'
    assert get(game.human, 'playerColor') == 'green'
    assert get(game.human, 'population') == 400
    assert [get(p, 'faceFrame') for p in game.players.items[1:]] == [1, 2]
    assert [get(p, 'religion_code') for p in game.players.items[1:]] == ['chr', 'mus']
    assert len({get(p, 'playerColor') for p in game.players}) == 3
    assert sum(truth(get(p, 'special_person')) for p in game.players.items[1:]) <= 1
    assert sum(truth(get(p, 'suicide_person')) for p in game.players.items[1:]) <= 1
    assert all(len(get(p, 'cityArr')) == 5 for p in game.players)
    state, rng = game.snapshot(), game.rt.rng.getstate()
    assert menu.press('btn_start') is game
    assert game.snapshot() == state and game.rt.rng.getstate() == rng


def test_invalid_setup_and_failed_presentation_leave_menu_and_rng_intact(monkeypatch):
    menu = SetupMenu(0)
    menu.press('splashScreenMC')
    before, rng = menu.snapshot(), menu.rt.rng.getstate()
    assert menu.press('btn_start') is None
    assert menu.snapshot() == before and menu.rt.rng.getstate() == rng
    assert not truth(get(menu.model, 'game_initiated'))
    menu.press('BTN_allLeaders_screen1')
    before, rng = menu.snapshot(), menu.rt.rng.getstate()
    from wd2.original_gameplay import OriginalGameplay
    def fail(*args):
        raise ValueError('Presentation initialization failed')
    monkeypatch.setattr(OriginalGameplay, '__init__', fail)
    assert menu.start_game() is None
    assert menu.game is None and menu.snapshot() == before and menu.rt.rng.getstate() == rng
    assert menu.tree.named('gameMenu').visible


def test_original_controls_accept_actions_resolve_once_and_update_hud():
    menu = selected_menu()
    menu.start_game()
    game = menu.game
    assert not menu.tree.named('gameMenu').visible
    assert menu.tree.named('interfaceMC').visible
    assert menu.gameplay.battle.node.matrix.tx == 205
    assert get(menu.gameplay.battle, '_xscale') == 46
    assert len(menu.gameplay.city_clips) == 15
    # Stage position of the actual original Resources button.
    menu.click((75, 150))
    assert menu.gameplay.selected_action == 'resources'
    menu.press('btnAccept')
    assert get(get(game.human, 'turnActionArr')[0], 'action') == 'resources'
    menu.press('btn4'); menu.press('btnAccept')
    assert truth(get(game.human, 'allActionsSet'))
    menu.press('btn46')
    assert get(game.model, 'turn') == 1
    assert get(game.human, 'money') >= 100
    assert get(menu.gameplay.interface, 'turn') == 1
    assert get(menu.gameplay.interface, 'activePlayer') == 0
    assert '$ 106.000.000' in get(get(menu.gameplay.interface, 'statTxt'), 'text')
    assert 'TURN 1' in get(get(menu.gameplay.interface, 'shortMSG_textField'), 'text')
    menu.press('btn46')  # Disabled/empty actions cannot resolve twice.
    assert get(game.model, 'turn') == 1
    before, rng = game.snapshot(), game.rt.rng.getstate()
    assert Image.open(io.BytesIO(menu.png())).size == (800, 600)
    menu.png()
    assert game.snapshot() == before and game.rt.rng.getstate() == rng


def test_same_turn_defeat_and_no_presentation_replay_of_gameplay_callbacks():
    menu = selected_menu()
    game = menu.start_game()
    game.model.set('doTurn', lambda: game.model.set('turn', get(game.model, 'turn')+1))
    enemy = game.players[1]
    for i, city in enumerate(get(enemy, 'cityArr')):
        city.set('population', 1 if i == 0 else 0)
        city.set('prevPopulation', 1 if i == 0 else 0)
    game.queue('attack', weapon='soldier1', target=1, city=0)
    game.queue('resources')
    menu.press('btn46')
    assert not truth(get(enemy, 'alive')) and get(enemy, 'population') == 0
    assert len([e for e in game.events if e.get('_item') == 'battle' and e.get('_player') == 0]) == 1
    before, rng = game.snapshot(), game.rt.rng.getstate()
    menu.host.clock.step(240)
    assert game.snapshot() == before and game.rt.rng.getstate() == rng


def test_menu_setup_and_turns_are_deterministic():
    def simulate():
        m = selected_menu()
        g = m.start_game()
        for _ in range(3):
            m.press('btn1'); m.press('btnAccept')
            m.press('btn4'); m.press('btnAccept')
            m.press('btn46')
        return g.snapshot(), g.rt.rng.getstate()
    assert simulate() == simulate()


def test_stage_click_start_keeps_audio_clock_and_selected_nation_in_same_application():
    menu = selected_menu()
    menu.press('colorBtn2')
    menu.press('buildingBtn1')
    expected_color = menu.rt.invoke(menu.menu_model, 'color_name_by_id', 1)
    expected_religion = menu.rt.invoke(menu.menu_model, 'building_num_to_religion_code', 1)
    menu.press('soundBtn')  # Music off must survive the runtime handoff.
    audio, theme = menu.audio, menu.audio.theme
    menu.host.clock.step(24)
    menu.host.clock.pause()
    menu.click((570, 565))  # Original Start button's stage position.
    assert menu.game is not None and menu.audio is audio and audio.theme is theme
    assert menu.audio.rt is menu.game.rt
    assert menu.host.clock.ticks == 24 and menu.host.clock.paused
    assert get(menu.game.human, 'playerColor') == expected_color
    assert get(menu.game.human, 'religion_code') == expected_religion
    assert not get(get(menu.model, 'option'), 'music') and not theme.playing
    menu.press('btn39')
    assert theme.playing and get(get(menu.model, 'option'), 'music')
    menu.audio.complete(theme)
    assert theme.playing  # Original loop callback now dispatches in the new runtime.
    menu.press('btn38')
    assert not get(get(menu.model, 'option'), 'sound')
    menu.audio.close()


def test_real_window_dispatches_menu_to_gameplay_actions_without_reopening_display(monkeypatch):
    import pygame
    from wd2.setup_menu import run_window
    monkeypatch.setenv('SDL_VIDEODRIVER', 'dummy')
    monkeypatch.setenv('SDL_AUDIODRIVER', 'dummy')
    pygame.quit()
    menu = SetupMenu(0)
    events = iter([(400, 500), (205, 373), (570, 565), (75, 150),
                   'btnAccept', 'btn4', 'btnAccept', 'btn46', 'quit'])
    displays = []
    set_mode = pygame.display.set_mode
    def open_display(*args, **kwargs):
        displays.append(args[0])
        return set_mode(*args, **kwargs)
    def next_events():
        item = next(events)
        if item == 'quit':
            return [pygame.event.Event(pygame.QUIT)]
        if isinstance(item, str):
            node = next(n for n in menu.gameplay.controls() if n.name == item)
            x0, y0, x1, y1 = menu.renderer.control_bounds(node)
            item = ((x0+x1)/2, (y0+y1)/2)
        return [pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=item)]
    monkeypatch.setattr(pygame.display, 'set_mode', open_display)
    monkeypatch.setattr(pygame.event, 'get', next_events)
    run_window(menu)
    assert displays == [(800, 600)]
    assert get(menu.game.model, 'turn') == 1
    assert not menu.audio.theme.playing


@pytest.mark.parametrize('seed,difficulty,expected', [
    (0, 1, 'e9124105eeb9a8dfcc2845a5da6aaf8dd6c2e38f293cb7d1910ed3bd64d0f518'),
    (9, 0, '857af99f9b6c20f8b188df9a30371140cc166993c36b8c190400c0a27f1b3cae'),
    (9, 2, 'c331f2c23f86aebaec02aa2b6948d276c0a7d73609676ff4271767dc37fcf7b0'),
])
def test_existing_headless_engine_matches_pre_change_baseline(seed, difficulty, expected):
    game = Game(seed, difficulty)
    sequence = [game.snapshot()]
    for _ in range(5):
        game.queue('resources'); game.queue('religion'); sequence.append(game.advance())
    payload = json.dumps(sequence, sort_keys=True, allow_nan=True, separators=(',', ':'))
    assert hashlib.sha256(payload.encode()).hexdigest() == expected
