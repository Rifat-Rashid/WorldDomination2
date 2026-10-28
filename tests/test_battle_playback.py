import io
from pathlib import Path

import pytest
from PIL import Image, ImageStat

from wd2.setup_menu import SetupMenu
from wd2.battle_playback import PresentationSnapshot
from wd2.runtime import ASObject, arr, get, obj, truth, U
from wd2.movieclip_host import MovieClipHost
from wd2.display_list import MovieClip, Symbol, Timeline, Matrix


def started(seed=0):
    m = SetupMenu(seed)
    m.press('splashScreenMC'); m.press('BTN_allLeaders_screen1'); m.start_game()
    return m


def test_snapshot_preserves_aliases_prototype_data_and_has_no_native_closures():
    m = started()
    shared = obj({'callback': lambda: m.game.advance()})
    shared.set('cycle', shared)
    m.model.set('copy_fixture', arr([shared, shared]))
    before = m.game.snapshot(), m.rt.rng.getstate()
    copy = PresentationSnapshot(m.game)
    a, b = get(copy.model, 'copy_fixture')
    assert a is b and get(a, 'cycle') is a
    assert not truth(get(a, 'callback'))
    assert get(copy.model, 'human') is get(copy.model, 'playerArr')[0]
    get(copy.model, 'human').set('money', 99999)
    assert (m.game.snapshot(), m.rt.rng.getstate()) == before


@pytest.mark.parametrize('kind', ['resources', 'attack', 'rocket', 'propaganda'])
def test_recovered_battle_runs_once_on_copy_and_returns_to_same_session(kind):
    m = started()
    game = m.game
    if kind == 'rocket':
        game.queue('preAttack', weapon='rocket1'); game.queue('resources'); game.advance()
        m.gameplay.actions.after_turn(); m.gameplay.refresh()
    if kind == 'attack':
        game.queue('attack', weapon='soldier1', target=1, city=0)
    elif kind == 'rocket':
        game.queue('preAttack', payload='warhead1', target=1, city=0)
    elif kind == 'propaganda':
        game.queue('propaganda', target=1, city=0)
    else:
        game.queue('religion')
    game.queue('resources')
    m.play_battles = True
    m.press('btn46')
    playback = m.playback
    assert playback is not None
    before, rng, events = game.snapshot(), game.rt.rng.getstate(), list(game.events)
    assert playback.model is not game.model and playback.rt is not game.rt
    assert playback.rt.invoke(playback.battle, 'getDepth') == game.rt.invoke(m.gameplay.battle, 'getDepth')
    assert get(playback.battle, '_xscale') == 100
    assert len(get(get(playback.model, 'battle'), '_activeUnitsArr'))
    assert all(hasattr(get(c, 'image'), 'node') for p in get(playback.model, 'playerArr') for c in get(p, 'cityArr'))
    for index in (2,3,4):
        assert get(get(playback.battle, f'ab{index}_1'), '_currentframe') == 1
    m.host.clock.pause(); m.step(20)
    assert playback.host.clock.ticks == 0
    m.host.clock.resume()
    m.step(48)
    image = Image.open(io.BytesIO(m.png())).convert('RGB')
    assert image.size == (800, 600)
    assert min(ImageStat.Stat(image).mean) > 10
    assert m.host.clock.ticks == 48
    m.press('btn46')  # Input during playback cannot resolve another turn.
    m.step(1000)
    assert playback.done and m.playback is None
    assert m.game is game
    assert (game.snapshot(), game.rt.rng.getstate(), game.events) == (before, rng, events)
    assert 'attachMovie' not in playback.rt.missing_calls
    assert 'swapDepths' not in playback.rt.missing_calls or playback.rt.missing_calls['swapDepths'] <= 5  # Absent legacy interface children.


def test_depth_swaps_and_coordinate_conversion_preserve_clip_identity():
    from wd2.runtime import Runtime
    s = {0: Symbol(0, 0, timeline=Timeline()), 1: Symbol(1, 39, 'clip', Timeline())}
    h = MovieClipHost(Runtime(), MovieClip(s))
    a = h.rt.invoke(h.root, 'attachMovie', 'clip', 'a', 1)
    b = h.rt.invoke(h.root, 'attachMovie', 'clip', 'b', 2)
    a.node.matrix = Matrix(0, 2, -3, 0, 100, 200)
    point = obj({'x': 5, 'y': 7})
    h.rt.invoke(a, 'localToGlobal', point)
    assert (get(point, 'x'), get(point, 'y')) == (79, 210)
    h.rt.invoke(a, 'globalToLocal', point)
    assert (get(point, 'x'), get(point, 'y')) == (5, 7)
    h.rt.invoke(a, 'swapDepths', b)
    assert h.tree.children[2] is a.node and h.tree.children[1] is b.node
    h.rt.invoke(a, 'swapDepths', 100)
    assert h.tree.children[100] is a.node and get(h.root, 'a') is a
    assert get(a, '_parent') is h.root
    assert h.rt.invoke(h.root, 'attachMovie', 'absent_linkage', 'missing', 100) is U
    assert h.tree.children[100] is a.node
    assert h.missing_linkages == {'absent_linkage'}


def test_original_laser_drawing_invalidates_cached_surfaces(monkeypatch):
    import pygame
    from wd2.runtime import Runtime
    from wd2.scene_renderer import SceneRenderer
    from wd2.surface_renderer import SurfaceRenderer
    monkeypatch.setenv('SDL_VIDEODRIVER', 'dummy')
    monkeypatch.setenv('SDL_AUDIODRIVER', 'dummy')
    pygame.init(); pygame.display.set_mode((40, 40))
    try:
        s = {0: Symbol(0, 0, timeline=Timeline()), 1: Symbol(1, 39, 'clip', Timeline())}
        h = MovieClipHost(Runtime(), MovieClip(s))
        a = h.rt.invoke(h.root, 'attachMovie', 'clip', 'laser', 1)
        renderer = SurfaceRenderer(SceneRenderer(), pygame)
        h.rt.invoke(a, 'lineStyle', 2, 0xff0000, 100)
        h.rt.invoke(a, 'moveTo', 5, 20); h.rt.invoke(a, 'lineTo', 35, 20)
        first = renderer.frame(h.tree, (40, 40))
        assert first.get_at((20,20))[:3] == (255, 0, 0)
        assert renderer.frame(h.tree, (40,40)) is first
        h.rt.invoke(a, 'clear')
        assert renderer.frame(h.tree, (40,40)).get_at((20,20))[:3] == (0,0,0)
    finally:
        pygame.quit()


def test_source_city_bullet_overlay_renders_above_completed_atlas_without_model_writes():
    m = started()
    city = next(iter(m.gameplay.city_clips.values()))
    before = m.png()
    rng, state = m.rt.rng.getstate(), m.game.snapshot()
    m.rt.invoke(get(city, 'bulletHoles'), 'gotoAndStop', 8)
    assert m.png() != before
    assert (m.game.snapshot(), m.rt.rng.getstate()) == (state, rng)


def test_initialized_battle_ocean_matches_independent_ruffle_reference():
    from PIL import ImageChops
    reference = Path(__file__).resolve().parents[1]/'validation/ruffle_battle/battle_after_6s.png'
    if not reference.exists():
        pytest.skip('Optional original-player capture is not distributed')
    m = started(); m.play_battles = True
    m.game.queue('attack', weapon='soldier1'); m.game.queue('resources')
    m.press('btn46'); m.step(145)
    image = Image.open(io.BytesIO(m.png())).convert('RGB')
    original = Image.open(reference).convert('RGB')
    # Original players have independent random city/flag/animation states.
    # Unobstructed ocean checks the verified root mask, not those random states.
    for box in ((600,400,780,570), (20,450,180,570), (320,100,540,160)):
        assert max(ImageStat.Stat(ImageChops.difference(image.crop(box), original.crop(box))).mean) < .3


@pytest.mark.parametrize('carrier,payload', [('plane1','bioload1'), ('sub','warhead3'),
                                           ('space','specialLoad'), ('ship','warhead1')])
def test_original_prepared_controls_drive_special_battles_without_replaying_damage(carrier, payload):
    from wd2.action_entry import control_path
    m = started(3)
    stock = get(m.game.human, 'weaponStock')
    for name in (carrier, payload):
        w = m.rt.invoke(stock, 'getWeaponByName', name)
        w.set('active', True); w.set('inStock', 2)
    m.game.queue('preAttack', weapon=carrier); m.game.queue('resources'); m.game.advance()
    m.gameplay.actions.after_turn(); m.gameplay.refresh()
    while truth(get(m.game.human, 'diplomacyPendingArr')[0]):
        m.press('btnCancel')
    m.play_battles = True
    m.press('btn6')
    button = next(b for b in get(m.gameplay.hud, 'stockBtn_arr')
                  if truth(b) and get(b, 'relatedWeapon') == payload)
    m.press(control_path(get(button, 'overlayMC').node))
    target = get(m.game.players[1], 'cityArr')[0]
    m.press('city'+str(get(target, 'cityID')))
    m.press('btnAccept'); m.press('btn1'); m.press('btnAccept'); m.press('btn46')
    playback = m.playback
    assert playback is not None
    state, rng, events = m.game.snapshot(), m.rt.rng.getstate(), list(m.game.events)
    m.step(300)
    image = Image.open(io.BytesIO(m.png())).convert('RGB')
    assert min(ImageStat.Stat(image).mean) > 10
    m.step(800)
    assert playback.done and m.playback is None
    assert (m.game.snapshot(), m.rt.rng.getstate(), m.game.events) == (state, rng, events)


def test_recovered_clip_registration_initialization_and_particle_callbacks():
    from wd2.runtime import Runtime
    from wd2.generated import register_all
    from wd2.scene_data import load_scene
    rt = Runtime(8); register_all(rt)
    h = MovieClipHost(rt, load_scene().root(10))
    for node in h.tree.walk():
        node.playing = False
    rt.globals.set('model', obj({'tools': rt.new('Tools')}))
    for path in ('bioCloud.as','spaceRocket_smoke.as','spaceRocket_trail_element.as'):
        rt.call(rt.scripts[path], rt.globals, [])
    smoke = rt.invoke(h.root, 'attachMovie', 'spaceRocket_smoke', 'smoke', 9000, obj({'_x':50, '_y':100}))
    assert smoke.cls is rt.classes['SpaceRocket_smoke']
    assert get(smoke, 'groundY') == 100  # Source constructor sees initObject.
    h.clock.step(3)
    trail = get(smoke, 'trailArr')[0]
    assert trail.cls is rt.classes['SpaceRocket_trail_element']
    assert get(trail, '_parent') is h.root and get(trail, '_alpha') > 0
    h.clock.step(192)
    assert get(trail, '_parent') is U and not h.clock.timers
    bio = rt.invoke(h.root, 'attachMovie', 'bioCloud', 'bio', 9001)
    rt.invoke(bio, 'spawn'); before = get(bio, '_y')
    h.clock.step()
    assert get(bio, '_y') == before-2
    assert not rt.missing_calls
