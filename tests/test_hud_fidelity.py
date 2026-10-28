from copy import copy
import io

from PIL import Image
import pytest

from wd2.setup_menu import SetupMenu
from wd2.runtime import get, U
from wd2.display_list import Matrix, ColorTransform


def started():
    m = SetupMenu(0); m.press('splashScreenMC'); m.press('BTN_allLeaders_screen1'); m.start_game()
    return m


def test_recovered_religion_flames_initialize_and_animate_on_visual_rng_only():
    m = started(); state, rng = m.game.snapshot(), m.rt.rng.getstate()
    from wd2.action_entry import control_path
    button = next(b for b in get(m.gameplay.hud,'stockBtn_arr') if b is not U and get(b,'relatedWeapon') == 'spy1')
    m.press(control_path(get(button,'overlayMC').node))
    target = get(m.game.players[1],'cityArr')[0]
    m.press('city'+str(get(target,'cityID')))
    nodes = [n for n in m.tree.walk() if n.character_id in (4010,4015,4018,4023,4028)]
    assert nodes
    assert all(2 <= n.frame <= 110 for n in nodes)
    state = m.game.snapshot()
    frames = [n.frame for n in nodes]
    m.step(120)
    assert [n.frame for n in nodes] != frames
    assert m.rt.rng.getstate() == rng
    assert m.game.snapshot() == state
    m.png()
    assert m.rt.rng.getstate() == rng


def test_original_welcome_has_no_added_header_and_panel_fades_settle():
    m = started()
    assert get(get(m.gameplay.interface,'shortMSG_textField'),'text') == 'Welcome commander. Please select 2 action from the left menu.\n'
    m.press('btn5'); m.step(12)
    assert [get(get(m.gameplay.interface,f'stockPanel{i}'),'_alpha') for i in range(1,9)] == [0,0,0,0,0,100,100,0]


def test_dynamic_field_uses_same_movieclip_color_transform_as_original_leaves():
    m = SetupMenu(); m.press('splashScreenMC')
    field = get(get(m.root,'gameMenu'),'leaderText')
    field.set('text','MMMMMMMM')
    field.node.color = ColorTransform((0,0,0,.5),(255,0,0,0))
    view = copy(field.node); view.matrix = Matrix(tx=20,ty=20)
    image = Image.open(io.BytesIO(m.renderer.png(view,(200,60),None))).convert('RGBA')
    alpha = image.getchannel('A')
    assert 126 <= alpha.getextrema()[1] <= 128
    point = max(((x,y) for y in range(image.height) for x in range(image.width)),key=lambda p:image.getpixel(p)[3])
    assert image.getpixel(point)[:3] == (255,0,0)


def test_all_19_original_leaders_are_selectable_and_initialize_source_identity():
    for leader in range(19):
        m = SetupMenu(2); m.press('splashScreenMC')
        for _ in range(leader):
            m.press('btn_player_list_right')
        assert get(m.menu_model,'visible_leader_list_arr')[0] == leader
        source = m.rt.invoke(m.menu_model,'get_leader_by_ID',leader)
        m.press('BTN_allLeaders_screen1')
        assert list(get(m.menu_model,'selected_leader_arr')) == [leader]
        game = m.start_game()
        assert game is not None and len(game.players) == 2
        assert get(game.players[1],'faceFrame') == get(source,'_frame')
        assert get(game.players[1],'religion_code') == get(source,'_religion')


def test_original_setup_option_controls_and_four_opponent_limit():
    m = SetupMenu(1); m.press('splashScreenMC')
    for value in range(1,6):
        m.press(f'colorBtn{value}'); m.press(f'buildingBtn{value}')
        assert get(m.menu_model,'player_color') == value
        assert get(m.menu_model,'selected_building') == value
    for value in (1,2,3):
        m.press(f'btn{value}')
        assert get(m.menu_model,'difficulty') == value-1
    for value in range(1,7):
        m.press(f'BTN_allLeaders_screen{value}')
    assert list(get(m.menu_model,'selected_leader_arr')) == [0,1,2,3]
    m.press('BTN_selectedLeader_screen2')
    assert list(get(m.menu_model,'selected_leader_arr')) == [0,2,3]
    m.press('BTN_allLeaders_screen6')
    assert list(get(m.menu_model,'selected_leader_arr')) == [0,2,3,5]


def test_live_initial_hud_uses_source_timed_stages_and_leader_noise_without_game_rng():
    m = SetupMenu(); m.play_battles = True
    m.press('splashScreenMC'); m.press('BTN_allLeaders_screen1'); m.start_game()
    state, rng = m.game.snapshot(), m.rt.rng.getstate()
    original_view = get(m.rt.globals,'view')
    sequence = m.interface_sequence
    m.step(8)
    assert sequence is not None and not sequence.done
    assert get(m.model,'view_leader_MCs_played') == 'false'
    m.step(120)
    assert sequence.done and m.interface_sequence is None
    assert get(m.model,'view_leader_MCs_played') == 'done'
    assert get(m.rt.globals,'view') is original_view
    # Absent legacy UI fields remain diagnostics; gameplay values stay intact.
    after = m.game.snapshot()
    after.pop('missing_calls'); state.pop('missing_calls')
    assert after == state and m.rt.rng.getstate() == rng


def test_return_hud_stages_do_not_call_city_battle_callbacks_or_mutate_gameplay():
    m = started(); m.game.queue('resources'); m.game.queue('religion'); m.game.advance()
    m.gameplay.actions.after_turn(); m.gameplay.refresh()
    state, rng = m.game.snapshot(), m.rt.rng.getstate()
    def unexpected(*args):
        pytest.fail('HUD phases must not resolve casualties')
    for player in m.game.players:
        for city in get(player,'cityArr'):
            city.set('size_and_frame_in_battle',unexpected)
    m.begin_interface_sequence(); sequence = m.interface_sequence
    m.step(5)
    assert not sequence.done
    m.step(100)
    assert sequence.done and m.interface_sequence is None
    after = m.game.snapshot()
    after.pop('missing_calls'); state.pop('missing_calls')
    assert after == state and m.rt.rng.getstate() == rng


def test_idle_city_overlays_obey_original_stops_and_reuse_registered_artwork():
    m = started()
    clips = list(m.gameplay.city_clips.values())
    before = [(c.node.frame,get(get(c,'mc'),'_currentframe')) for c in clips]
    m.step(30)
    assert [(c.node.frame,get(get(c,'mc'),'_currentframe')) for c in clips] == before
    for clip in clips:
        for name in ('bulletHoles','propagandaBeams','propagandaBeams2','citizensMovie'):
            overlay = get(clip,name)
            assert get(overlay,'_currentframe') == 1 and not overlay.node.playing


def test_original_human_city_hover_shows_population_without_gameplay_mutation():
    m = started()
    city = get(m.game.human,'cityArr')[0]
    clip = m.gameplay.city_clips[get(city,'cityID')]
    popup = get(clip,'citizensMovie')
    state,rng = m.game.snapshot(),m.rt.rng.getstate()
    b = m.renderer.control_bounds(clip.node)
    m.motion(((b[0]+b[2])/2,(b[1]+b[3])/2))
    assert get(popup,'_currentframe') == 2
    assert get(get(popup,'txt1'),'text') == get(city,'population')
    m.motion((795,595))
    assert get(popup,'_currentframe') == 1
    assert m.game.snapshot() == state and m.rt.rng.getstate() == rng
