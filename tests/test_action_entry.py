"""Exercise original control callbacks and stage input, using existing model rules."""
import io
import pytest
from PIL import Image
from wd2.runtime import U, get, truth, number, arr, obj
from wd2.setup_menu import SetupMenu
from wd2.action_entry import control_path


@pytest.fixture
def menu():
    m = SetupMenu(3)
    m.press('splashScreenMC')
    m.press('BTN_allLeaders_screen1')
    m.press('BTN_allLeaders_screen2')
    m.start_game()
    return m


def weapon(m, name):
    return m.rt.invoke(get(m.game.human, 'weaponStock'), 'getWeaponByName', name)


def stock(m, name, count=None):
    w = weapon(m, name)
    if count is not None:
        w.set('inStock', count)
        w.set('active', True)
    button = next(b for b in get(m.gameplay.hud, 'stockBtn_arr')
                  if b is not U and get(b, 'relatedWeapon') == name)
    m.press(control_path(get(button, 'overlayMC').node))
    return w


def click(m, path):
    node = m.gameplay.actions.find(path)
    assert node is not None, path
    bounds = m.renderer.control_bounds(node)
    assert bounds is not None, path
    x0, y0, x1, y1 = bounds
    m.click(((x0+x1)/2, (y0+y1)/2))


def city(m, player=1, index=0):
    c = get(m.game.players[player], 'cityArr')[index]
    click(m, 'city'+str(get(c, 'cityID')))
    return c


def actions(m):
    return [get(t, 'action') for t in get(m.game.human, 'turnActionArr')]


def slider(m, index, percent):
    slide = get(get(m.gameplay.interface, 'centerScreen'), f'slide{index}')
    # Actual pointer movement in the slider's original coordinate system.
    width = get(get(slide, 'maxW'), '_width')
    point = slide.node.world_matrix.point(percent*100/width + 1, 0)
    bg = get(slide, 'sliderBG').node
    m.host.pointer = point
    m.press(control_path(bg))
    m.motion(point)
    m.release(point)


def test_all_action_panels_render_and_nested_buttons_have_distinct_identity(menu):
    for index, action in enumerate(('resources','production','research','religion',
                                    'attack','preAttack','defense','propaganda','diplomacy'), 1):
        menu.press(f'interfaceMC/btn{index}')
        assert menu.gameplay.selected_action == action
        assert Image.open(io.BytesIO(menu.png())).size == (800, 600)
    menu.press('interfaceMC/centerScreen/btn1')
    assert get(menu.model, 'userSelectedDiplomacyOption') == 0
    assert menu.gameplay.selected_action == 'diplomacy'
    assert len({control_path(n) for n in menu.gameplay.controls()}) == len(menu.gameplay.controls())


def test_tubes_skip_cancel_toggle_and_confirm_once(menu):
    menu.press('btn44'); menu.press('btnAccept')
    assert actions(menu)[0] == 'skip_action'
    menu.press('btn1'); menu.press('btnAccept')
    assert actions(menu)[1] == 'resources'
    menu.press('btn1')  # Selecting an already queued action cancels that slot.
    assert actions(menu) == ['skip_action', U]
    menu.press('btn4'); menu.press('btnAccept')
    menu.press('btn46'); menu.press('btn46')
    assert get(menu.model, 'turn') == 1
    assert actions(menu) == [U, U]
    menu.press('btn1'); menu.press('btn1')
    assert menu.gameplay.selected_action is None


def test_production_sliders_limit_total_cancel_refunds_exact_reserved_cost(menu):
    original = get(menu.game.human, 'turnMoney')
    menu.press('btn2')
    slider(menu, 6, 30)
    slider(menu, 8, 100)
    rows = get(menu.model, 'userSelectedProductionInvestmentArr')
    assert rows[6][1] == 30 and rows[8][1] == 70
    assert get(menu.model, 'userSelectedProductionInvestmentArr_total_amount') == 100
    assert not menu.host.mouse_listeners
    menu.press('btnAccept')
    assert get(menu.game.human, 'turnMoney') == 0
    menu.press('btn44')
    assert get(menu.game.human, 'turnMoney') == original
    menu.press('btn2'); slider(menu, 6, 10); menu.press('btnAccept')
    assert get(menu.game.human, 'turnMoney') == original - int(original*.1+.5)
    menu.press('btn44')
    assert get(menu.game.human, 'turnMoney') == original


def test_production_locked_group_and_error_dismissal(menu):
    menu.press('btn2'); slider(menu, 3, 40)
    assert truth(get(menu.model, 'interface_production_error'))
    menu.press('btnOK')
    assert not truth(get(menu.model, 'interface_production_error'))
    assert get(menu.model, 'userSelectedProductionInvestmentArr_total_amount') == 0


def test_slider_drag_clamps_at_stage_edges_and_release_stops_updates(menu):
    menu.press('btn2')
    slide = get(get(menu.gameplay.interface, 'centerScreen'), 'slide6')
    menu.click(slide.node.world_matrix.point(35, 12))
    assert menu.host.mouse_listeners
    menu.motion((-100, 264))
    assert get(menu.model, 'userSelectedProductionInvestmentArr')[6][1] == 0
    menu.motion((1000, 264))
    assert get(menu.model, 'userSelectedProductionInvestmentArr')[6][1] == 100
    menu.release((1000, 264))
    menu.motion((-100, 264))
    assert get(menu.model, 'userSelectedProductionInvestmentArr')[6][1] == 100
    assert not menu.host.mouse_listeners


def test_research_multiple_choices_cancel_refund_and_complete_group(menu):
    initial = get(menu.game.human, 'turnMoney')
    menu.press('btn3'); click(menu, 'tech1'); click(menu, 'tech2')
    chosen = list(get(menu.model, 'userSelectedResearchArr'))
    assert len(chosen) == 2
    cost = get(menu.model, 'researchMoneySpend')
    menu.press('btnAccept')
    assert get(menu.game.human, 'turnMoney') == initial-cost
    menu.press('btn44')
    assert get(menu.game.human, 'turnMoney') == initial
    assert not any(truth(get(t, 'preOrder')) for t in get(get(menu.game.human, 'techTree'), 'techArr'))
    for t in get(get(menu.game.human, 'techTree'), 'techArr'):
        if get(t, 'desireGroup') == get(menu.model, '_userSelectedResearchInvestmentArr')[2][2]:
            t.set('invented', True)
    menu.press('btn3')
    box = get(get(menu.gameplay.interface, 'centerScreen'), 'tech2')
    assert get(get(box, '_obj'), '_tech') is U
    menu.press('tech2')
    assert not len(get(menu.model, 'userSelectedResearchArr'))


def test_research_funds_and_special_gate(menu):
    menu.game.human.set('turnMoney', 0)
    menu.press('btn3'); menu.press('tech1')
    assert truth(get(menu.model, 'interface_research_error'))
    menu.press('btnOK')
    assert not len(get(menu.model, 'userSelectedResearchArr'))
    menu.game.human.set('turnMoney', 1000)
    menu.press('tech3')
    assert truth(get(menu.model, 'interface_research_error'))
    assert not len(get(menu.model, 'userSelectedResearchArr'))


def test_attack_stock_shortcut_target_rejection_and_cancellation(menu):
    w = stock(menu, 'soldier1')
    assert menu.gameplay.selected_action == 'attack'
    city(menu, 0)
    assert get(menu.model, 'userSelectedCity') is U
    ceasefire = get(menu.game.human, 'ceaseFireArr')[1]
    ceasefire.set('_status', True)
    city(menu)
    assert get(menu.model, 'userSelectedCity') is U
    ceasefire.set('_status', False)
    target = city(menu)
    assert get(menu.model, 'userSelectedCity') is target
    assert menu.gameplay.actions.markers[get(target, 'cityID')][0] == ('soldier',)
    menu.press('btnAccept')
    ta = get(menu.game.human, 'turnAction_1')
    assert get(ta, 'targetCity') is target and get(ta, 'attackWeapon') is w
    menu.press('btn44')
    assert get(w, 'inUse') == 0 and actions(menu) == [U, U]
    assert get(target, 'cityID') not in menu.gameplay.actions.markers


def test_spy_readiness_building_and_ceasefire_exception(menu):
    menu.game.human.set('spy_readiness', 0)
    stock(menu, 'spy1', 2)
    assert get(menu.model, 'userSelectedWeapon') is U
    assert truth(get(menu.model, 'interface_spy_error'))
    menu.press('btnOK')
    menu.game.human.set('spy_readiness', 100)
    stock(menu, 'spy1')
    get(menu.game.human, 'ceaseFireArr')[1].set('_status', True)
    target = city(menu)
    menu.press('interfaceMC/centerScreen/btn3')
    building = get(menu.model, 'userSelectedSpyBuilding')
    assert building != 'spyCenter'
    menu.press('btnAccept')
    ta = get(menu.game.human, 'turnAction_1')
    assert get(ta, 'targetCity') is target and get(ta, 'spyBuilding') == building


def test_defense_and_propaganda_preserve_other_slot(menu):
    w = stock(menu, 'antiAir')
    menu.press('btnAccept')
    menu.press('btn8'); city(menu); menu.press('btnAccept')
    menu.press('btn45')
    assert actions(menu) == ['defense', U] and get(w, 'inUse') == 1
    menu.press('btn8'); city(menu); menu.press('btnAccept'); menu.press('btn46')
    assert get(menu.model, 'turn') == 1 and get(w, 'inStock') == 1


@pytest.mark.parametrize('carrier,payload', [('rocket1','warhead1'),('plane1','bioload1'),
                                           ('sub','warhead3'),('space','specialLoad')])
def test_prepared_carrier_then_payload_complete_two_turns(menu, carrier, payload):
    stock(menu, carrier, 1); menu.press('btnAccept')
    menu.press('btn1'); menu.press('btnAccept'); menu.press('btn46')
    assert get(menu.game.human, 'preAttackStatus') == 'ready'
    assert get(weapon(menu, carrier), 'inStock') == 0
    menu.press('btn6'); stock(menu, payload, 2); city(menu); menu.press('btnAccept')
    ta = get(menu.game.human, 'turnAction_1')
    assert get(ta, 'preAttackPayload') is weapon(menu, payload)
    menu.press('btn1'); menu.press('btnAccept'); menu.press('btn46')
    assert get(menu.model, 'turn') == 2
    assert get(weapon(menu, payload), 'inStock') == 1
    assert get(menu.game.human, 'preAttackStatus') == 'inactive'


def ready_carrier(menu, name):
    w = weapon(menu, name)
    w.set('active', True)
    menu.game.human.set('preAttackStatus', 'ready')
    menu.game.human.set('preAttackWeapon', w)
    menu.model.set('userSelectedCarrier', w)
    menu.press('btn6')


def test_payload_capacity_and_preparation_cancellation_confirmation(menu):
    ready_carrier(menu, 'rocket1')
    stock(menu, 'warhead4', 1)
    assert get(menu.model, 'userSelectedWeapon') is U
    stock(menu, 'warhead1', 1)
    city(menu)
    menu.press('btnCancel')
    assert menu.gameplay.selected_action == 'cancelPreAttack'
    menu.press('btnCancel')
    assert get(menu.game.human, 'preAttackStatus') == 'ready'
    menu.press('btn6'); menu.press('btnCancel'); menu.press('btnAccept')
    assert get(menu.game.human, 'preAttackStatus') == 'inactive'
    assert get(weapon(menu, 'warhead1'), 'inUse') == 0


def test_ship_three_payloads_one_enemy_cancel_and_launch(menu):
    ready_carrier(menu, 'ship')
    city(menu)
    assert len(get(menu.model, 'ship_attack_arr')) == 0
    w = stock(menu, 'warhead1', 4)
    city(menu, 1, 0)
    stock(menu, 'warhead1'); city(menu, 2, 0)
    assert len(get(menu.model, 'ship_attack_arr')) == 1
    city(menu, 1, 1)
    stock(menu, 'warhead1'); city(menu, 1, 2)
    assert len(get(menu.model, 'ship_attack_arr')) == 3
    stock(menu, 'warhead1'); city(menu, 1, 3)
    assert len(get(menu.model, 'ship_attack_arr')) == 3
    menu.press('btnAccept')
    assert len(get(get(menu.game.human, 'turnAction_1'), 'ship_attack_arr')) == 3
    menu.press('btn44')
    assert get(w, 'inUse') == 0
    menu.press('btn6')
    for i in range(3):
        stock(menu, 'warhead1'); city(menu, 1, i)
    menu.press('btnAccept'); menu.press('btn1'); menu.press('btnAccept'); menu.press('btn46')
    assert get(w, 'inStock') == 1
    assert get(menu.model, 'turn') == 1


def test_diplomacy_cost_cancel_and_pending_responses(menu):
    initial = get(menu.game.human, 'turnMoney')
    menu.press('btn9'); menu.press('interfaceMC/centerScreen/leaderMC1')
    menu.press('interfaceMC/centerScreen/btn1'); menu.press('btnAccept')
    option = get(menu.model, 'diplomacy_options_arr')[0]
    assert get(menu.game.human, 'turnMoney') == initial-option[2]
    menu.press('btn44')
    assert get(menu.game.human, 'turnMoney') == initial
    pending = obj({'_leader': 1, '_option': 0})
    menu.game.human.set('diplomacyPendingArr', arr([pending]))
    menu.gameplay.actions.update()
    menu.press('btn1'); menu.press('btn44'); stock(menu, 'soldier1')
    assert menu.gameplay.selected_action == 'diplomacyPending'
    menu.press('btnAccept')
    assert get(menu.game.human, 'diplomacyAcceptedArr')[0] is pending
    menu.game.human.set('diplomacyPendingArr', arr([obj({'_leader': 1, '_option': 3})]))
    menu.game.human.set('turnMoney', 0)
    menu.gameplay.actions.update(); menu.press('btnAccept')
    assert len(get(menu.game.human, 'diplomacyPendingArr')) == 1
    menu.press('btnOK'); menu.press('btnCancel')
    assert len(get(menu.game.human, 'diplomacyRejectedArr')) == 1


def test_original_tube_hover_audio_clock_and_render_purity(menu):
    before, rng = menu.game.snapshot(), menu.rt.rng.getstate()
    click(menu, 'interfaceMC/btn1')
    tube = get(get(menu.gameplay.hud, 'actionTube1'), 'tubeMC')
    assert get(tube, '_currentframe') == 1
    menu.host.clock.step(12)
    assert get(tube, '_currentframe') == 10
    node = menu.gameplay.actions.find('btnAccept')
    b = menu.renderer.control_bounds(node)
    menu.motion(((b[0]+b[2])/2, (b[1]+b[3])/2))
    assert node.frame == node.symbol.timeline.labels['over']
    menu.press('btnAccept')
    menu.host.clock.step(12)
    assert get(tube, '_currentframe') == 11
    assert menu.rt.rng.getstate() == rng
    snapshot, rng = menu.game.snapshot(), menu.rt.rng.getstate()
    menu.png(); menu.png(); menu.host.clock.step(24)
    assert menu.game.snapshot() == snapshot and menu.rt.rng.getstate() == rng
    assert any(s.linkage.endswith('openactiondevice.wav') for s in menu.audio.sounds)


def test_research_resolves_original_technology_and_resources(menu):
    menu.press('btn3'); menu.press('tech1'); menu.press('tech2')
    chosen = [get(x, 'techID') for x in get(menu.model, 'userSelectedResearchArr')]
    menu.press('btnAccept'); menu.press('btn1'); menu.press('btnAccept'); menu.press('btn46')
    assert get(menu.model, 'turn') == 1
    tree = get(menu.game.human, 'techTree')
    assert all(truth(get(menu.rt.invoke(tree, 'getTechByID', tid), 'invented')) for tid in chosen)
    assert number(get(menu.game.human, 'money')) >= 0


def test_production_spend_and_inventory_resolve_through_original_engine(menu):
    initial = get(weapon(menu, 'soldier1'), 'inStock')
    funds = get(menu.game.human, 'money')
    menu.press('btn2'); slider(menu, 6, 100); menu.press('btnAccept')
    menu.press('btn4'); menu.press('btnAccept'); menu.press('btn46')
    assert get(weapon(menu, 'soldier1'), 'inStock') > initial
    bought = get(weapon(menu, 'soldier1'), 'inStock') - initial
    assert get(menu.game.human, 'money') == funds - bought*get(weapon(menu, 'soldier1'), 'cost')


def test_original_ui_same_turn_defeat_is_not_replayed(menu):
    enemy = menu.game.players[1]
    for i, target in enumerate(get(enemy, 'cityArr')):
        target.set('population', 1 if i == 0 else 0)
        target.set('prevPopulation', 1 if i == 0 else 0)
    menu.model.set('doTurn', lambda: menu.model.set('turn', get(menu.model, 'turn')+1))
    stock(menu, 'soldier1'); city(menu); menu.press('btnAccept')
    menu.press('btn1'); menu.press('btnAccept'); menu.press('btn46')
    assert not truth(get(enemy, 'alive'))
    before, rng = menu.game.snapshot(), menu.rt.rng.getstate()
    menu.host.clock.step(240)
    assert menu.game.snapshot() == before and menu.rt.rng.getstate() == rng


def test_original_native_window_slider_release_stock_and_confirm(menu, monkeypatch):
    import pygame
    from wd2.setup_menu import run_window
    monkeypatch.setenv('SDL_VIDEODRIVER', 'dummy')
    monkeypatch.setenv('SDL_AUDIODRIVER', 'dummy')
    pygame.quit()
    inputs = iter(['btn2', 'slide', 'release', 'btnAccept', 'btn36', 'btnAccept', 'btn46', 'quit'])
    last = (0, 0)
    def events():
        nonlocal last
        item = next(inputs)
        if item == 'quit':
            return [pygame.event.Event(pygame.QUIT)]
        if item == 'release':
            return [pygame.event.Event(pygame.MOUSEMOTION, pos=last),
                    pygame.event.Event(pygame.MOUSEBUTTONUP, button=1, pos=last)]
        if item == 'slide':
            slide = get(get(menu.gameplay.interface, 'centerScreen'), 'slide6')
            last = slide.node.world_matrix.point(99, 15)
        else:
            b = menu.renderer.control_bounds(menu.gameplay.actions.find(item))
            last = ((b[0]+b[2])/2, (b[1]+b[3])/2)
        return [pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=last)]
    monkeypatch.setattr(pygame.event, 'get', events)
    run_window(menu)
    assert get(menu.model, 'turn') == 1
    assert not menu.host.mouse_listeners
    assert get(weapon(menu, 'soldier1'), 'inStock') > 1
    assert get(weapon(menu, 'antiAir'), 'inStock') == 1


def test_target_panel_blocks_click_through_and_all_marker_art_is_packaged(menu):
    stock(menu, 'soldier1'); target = city(menu)
    assert get(menu.model, 'userSelectedCity') is target
    city(menu, 1, 1)  # The confirmation panel covers the map.
    assert get(menu.model, 'userSelectedCity') is target
    menu.png()
    assert not menu.renderer.report['unsupported']
    for name in ('rocket1', 'plane1', 'sub', 'space'):
        selection = get(target, 'selectionObj')
        selection.set('preAttack', True); selection.set('preAttackWeapon', name)
        menu.gameplay.actions.sync_cities(); menu.png()
        assert not menu.renderer.report['unsupported']
