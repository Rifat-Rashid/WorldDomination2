import io

import pytest
from PIL import Image

from wd2.runtime import get, arr, truth
from wd2.setup_menu import SetupMenu


@pytest.fixture
def menu():
    m = SetupMenu(0)
    m.press('splashScreenMC'); m.press('BTN_allLeaders_screen1'); m.start_game()
    return m


def test_original_help_topics_next_previous_index_and_close_preserve_actions(menu):
    state, rng = menu.game.snapshot(), menu.rt.rng.getstate()
    menu.press('btn_help')
    assert get(menu.model, 'userSelectedHelpTopic') == 'help_index'
    menu.press('btn_overview')
    assert get(menu.model, 'userSelectedHelpTopic') == 'help_overview'
    menu.press('btnNext')
    assert get(menu.model, 'userSelectedHelpTopic') == 'help_interface'
    menu.press('btnPrev'); menu.press('btnIndex')
    assert get(menu.model, 'userSelectedHelpTopic') == 'help_index'
    menu.press('btn1'); menu.press('btn1')
    assert not truth(get(menu.model, 'userSelectedActionBtn'))
    after = menu.game.snapshot()
    after.pop('missing_calls'); state.pop('missing_calls')
    assert after == state and menu.rt.rng.getstate() == rng


def test_all_original_help_pages_render(menu):
    for page in get(get(menu.gameplay.presenter, 'help_data'), 'page_arr'):
        menu.model.set('userSelectedActionBtn', 'help')
        menu.model.set('userSelectedHelpTopic', get(page, '_pgName'))
        menu.gameplay.actions.update()
        assert Image.open(io.BytesIO(menu.png())).size == (800, 600)
        assert not menu.renderer.report['unsupported']


def test_original_fullscreen_command_toggles_without_changing_gameplay(menu):
    before, rng = menu.game.snapshot(), menu.rt.rng.getstate()
    menu.press('btn_fullscreen')
    assert menu.fullscreen_requested and truth(get(menu.model, 'fullscreen'))
    menu.press('btn_fullscreen')
    assert not menu.fullscreen_requested and not truth(get(menu.model, 'fullscreen'))
    assert menu.game.snapshot() == before and menu.rt.rng.getstate() == rng


@pytest.mark.parametrize('status', ['win', 'lost'])
def test_source_endgame_delays_score_animation_and_restart_are_isolated(menu, status):
    game = menu.game
    game.human.set('score', 10000)
    if status == 'lost':
        game.human.set('alive', False)
    else:
        game.model.set('activePlayerArr', arr([game.human]))
    before, rng = game.snapshot(), game.rt.rng.getstate()
    menu.lifecycle.check()
    end = get(menu.root, 'endGameMC')
    assert not truth(get(end, '_visible'))
    menu.host.clock.step(71)
    assert not truth(get(end, '_visible'))
    menu.host.clock.step()
    assert truth(get(end, '_visible'))
    assert get(end, '_currentframe') == end.node.symbol.timeline.labels[status]
    menu.host.clock.step(48)
    assert get(end, '_currentframe') == end.node.symbol.timeline.labels[status+'2']
    assert Image.open(io.BytesIO(menu.png())).size == (800, 600)
    menu.host.clock.step(600)
    assert int(str(get(get(end, 'txt2'), 'text')).replace('.', '')) >= 10000
    assert game.snapshot() == before and game.rt.rng.getstate() == rng
    old_rt = menu.rt
    menu.press('btn_new')
    assert menu.game is None and menu.rt is not old_rt
    assert menu.tree.named('splashScreenMC').visible
    assert game.snapshot() == before and game.rt.rng.getstate() == rng
    # Restart's native host commands must target the surviving app object.
    menu.fscommand('fullscreen', 'true')
    assert menu.fullscreen_requested


def test_cheated_score_label_does_not_overwrite_resolved_model(menu):
    menu.game.human.set('alive', False)
    menu.game.human.set('score', 500)
    menu.model.set('corrupt_highscore', True)
    menu.lifecycle.check(); menu.host.clock.step(120)
    assert get(get(get(menu.root, 'endGameMC'), 'txt2'), 'text') == '!!CHEATED!!'
    assert get(menu.game.human, 'score') == 500


def test_source_help_input_accepts_keyboard_and_reaches_recovered_handler(menu):
    import pygame
    menu.press('btn_help')
    for _ in range(9):
        menu.press('btnIndex_c')
    menu.host.clock.step()
    field = next(n for n in menu.tree.walk() if n.name == 'chTXT')
    x0, x1, y0, y1 = menu.renderer.fields[field.character_id]['bounds']
    menu.click(field.world_matrix.point((x0+x1)/2, (y0+y1)/2))
    assert menu.text_entry.node is field
    menu.text_entry.key(pygame.K_a, pygame.KMOD_CTRL)
    menu.text_entry.insert('youdx')
    menu.text_entry.key(pygame.K_BACKSPACE)
    menu.text_entry.insert('a')
    assert get(menu.host.wrap(field), 'text') == 'youda'
    menu.press('btnIndex_c')
    assert get(menu.model, 'm11') == 'xx1231'
    assert get(menu.model, 'userSelectedActionBtn') == 'cheat'


def test_original_message_scroll_controls_change_visible_lines(menu):
    target = get(menu.gameplay.interface, 'shortMSG_textField')
    target.set('text', '\n'.join('Message '+str(i) for i in range(20)))
    assert get(target, 'maxscroll') > 1
    before = menu.png()
    menu.press('btn_scroll_MSG_down_overlay')
    assert get(target, 'scroll') == 2
    assert menu.png() != before
    target.set('scroll', 999)
    assert get(target, 'scroll') == get(target, 'maxscroll')
    target.set('scroll', -10)
    assert get(target, 'scroll') == 1
