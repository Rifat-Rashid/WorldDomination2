"""Original enemy relationship hover thresholds and live pointer routing."""
import pytest

from wd2.runtime import get
from wd2.setup_menu import SetupMenu


@pytest.fixture
def menu():
    m = SetupMenu(0)
    m.press('splashScreenMC')
    for i in range(1, 5):
        m.press(f'BTN_allLeaders_screen{i}')
    m.start_game()
    return m


@pytest.mark.parametrize('regard,label', [
    (0, 'regard1'), (25, 'regard1'), (26, 'regard2'), (45, 'regard2'),
    (46, 'regard3'), (55, 'regard3'), (56, 'regard4'), (75, 'regard4'),
    (76, 'regard5'), (100, 'regard5'),
])
def test_relationship_hover_matches_original_bytecode_thresholds(menu, regard, label):
    get(menu.game.players[1], 'regardArr').set(0, regard)
    state, rng = menu.game.snapshot(), menu.rt.rng.getstate()
    menu.motion((283, 50))
    info = get(menu.gameplay.interface, 'infoLine').node
    assert info.frame == info.symbol.timeline.labels[label]
    menu.step(12)
    assert info.frame == info.symbol.timeline.labels[label]
    menu.motion((780, 590))
    assert info.frame == info.symbol.timeline.labels['null']
    assert menu.game.snapshot() == state and menu.rt.rng.getstate() == rng


def test_each_enemy_uses_its_own_regard_toward_human(menu):
    info = get(menu.gameplay.interface, 'infoLine').node
    for i, (x, regard, label) in enumerate([
        (283, 10, 'regard1'), (377, 40, 'regard2'),
        (470, 65, 'regard4'), (563, 90, 'regard5'),
    ], 1):
        get(menu.game.players[i], 'regardArr').set(0, regard)
        menu.motion((x, 50))
        assert info.frame == info.symbol.timeline.labels[label]
    menu.motion((780, 590))
    get(menu.game.players[4], 'regardArr').set(0, 50)
    menu.motion((563, 50))
    assert info.frame == info.symbol.timeline.labels['regard3']


def test_portrait_exposes_original_meter_message_and_retains_diplomacy_click(menu):
    get(menu.game.players[1], 'regardArr').set(0, 90)
    menu.motion((240, 50))
    info = get(menu.gameplay.interface, 'infoLine').node
    assert info.frame == info.symbol.timeline.labels['regard5']
    menu.click((240, 50))
    assert get(menu.game.model, 'userSelectedActionBtn') == 'diplomacy'
    assert get(menu.game.model, 'userSelectedDiplomacyLeader') == 1
    menu.motion((780, 590))
    assert info.frame == info.symbol.timeline.labels['null']


def test_absent_and_defeated_portraits_do_not_show_relationship(menu):
    info = get(menu.gameplay.interface, 'infoLine').node
    menu.game.players[1].set('alive', False)
    menu.motion((240, 50))
    assert info.frame != info.symbol.timeline.labels['regard1']
    menu.motion((780, 590))
    menu.game.players.set('length', 1)
    menu.motion((333, 50))
    assert info.frame == info.symbol.timeline.labels['null']
