import io

from PIL import Image, ImageChops, ImageStat
import pygame
import pytest

from wd2.display_list import MovieClip, Matrix, ColorTransform, Operation, Symbol, Timeline
from wd2.runtime import get
from wd2.scene_renderer import SceneRenderer, element
from wd2.setup_menu import SetupMenu
from wd2.surface_renderer import SurfaceRenderer


@pytest.fixture
def display(monkeypatch):
    monkeypatch.setenv('SDL_VIDEODRIVER', 'dummy')
    monkeypatch.setenv('SDL_AUDIODRIVER', 'dummy')
    pygame.display.init()
    pygame.display.set_mode((800, 600))
    yield pygame
    pygame.display.quit()


def compare(surface, png):
    actual = Image.frombytes('RGB', surface.get_size(), pygame.image.tobytes(surface, 'RGB'))
    reference = Image.open(io.BytesIO(png)).convert('RGB')
    delta = ImageStat.Stat(ImageChops.difference(actual, reference))
    # SDL and resvg differ in integer alpha-over rounding. Layout, masks and
    # registration must still agree; this is not a pixel-parity claim.
    assert max(delta.mean) < .15
    assert max(hi for lo, hi in delta.extrema) <= 8
    return actual


@pytest.mark.parametrize('scene', ['splash', 'setup', 'gameplay'])
def test_original_scene_surfaces_match_svg_and_reuse_without_rasterization(scene, display, monkeypatch):
    menu = SetupMenu(0)
    if scene != 'splash':
        menu.press('splashScreenMC')
    if scene == 'gameplay':
        menu.press('BTN_allLeaders_screen1'); menu.start_game()
    rng = menu.rt.rng.getstate()
    state = menu.game.snapshot() if menu.game else menu.snapshot()
    compare(menu.surface(display), menu.png())
    cached = menu.surface(display)
    def unexpected(*args, **kwargs):
        pytest.fail('An unchanged scene must reuse native surfaces without PNG/SVG work')
    monkeypatch.setattr(menu.renderer, 'png', unexpected)
    monkeypatch.setattr(menu.renderer, 'svg', unexpected)
    monkeypatch.setattr(menu.renderer.assets, 'load', unexpected)
    monkeypatch.setattr(pygame.image, 'load', unexpected)
    for _ in range(3):
        assert menu.surface(display) is cached
    assert (menu.game.snapshot() if menu.game else menu.snapshot()) == state
    assert menu.rt.rng.getstate() == rng
    assert menu._surface_renderer.stats()['frame_hits'] >= 4


def test_changed_selection_invalidates_only_affected_layers_and_keeps_source_callbacks(display):
    menu = SetupMenu(0); menu.press('splashScreenMC')
    before = compare(menu.surface(display), menu.png())
    cache = menu._surface_renderer
    rasterizations = cache.rasterizations
    menu.motion((205, 373))
    hovered = compare(menu.surface(display), menu.png())
    assert ImageChops.difference(before, hovered).getbbox()
    assert cache.rasterizations-rasterizations <= 3
    menu.click((205, 373))
    compare(menu.surface(display), menu.png())
    assert list(get(menu.menu_model, 'selected_leader_arr')) == [0]
    assert cache.layers.hits > 50


class RectAssets:
    def bounds(self, symbol):
        return 0, 0, 8, 6

    def load(self, symbol):
        group = element('g', {'id': f'asset_{symbol.character_id}'})
        group.append(element('rect', {'width': '8', 'height': '6', 'fill': '#ff0000'}))
        return group


def synthetic():
    symbols = {0: Symbol(0, 0, timeline=Timeline()), 1: Symbol(1, 2),
               2: Symbol(2, 39, timeline=Timeline([
                   [Operation(1, {'character_id': 1})],
                   [Operation(1, {'matrix': Matrix(tx=4)}, move=True)]]))}
    return MovieClip(symbols)


@pytest.mark.parametrize('invalid', [Matrix(tx=float('nan')), Matrix(a=float('nan')),
                                   Matrix(ty=float('inf'))])
def test_nonfinite_subtree_preserves_siblings_and_recovers_when_transform_is_valid(display, invalid):
    root = synthetic()
    root.apply(Operation(1, {'character_id': 2}))
    root.children[1].apply(Operation(1, {'character_id': 2}))
    group = root.children[1].children[1]
    group.children[1].matrix = invalid
    group.apply(Operation(2, {'character_id':1,'matrix':Matrix(tx=12,ty=3)}))
    root.apply(Operation(2, {'character_id': 1, 'matrix': Matrix(tx=24,ty=3)}))
    base = SceneRenderer(RectAssets()); cache = SurfaceRenderer(base, display)
    first = cache.frame(root, (32, 24))
    assert first.get_at((2,2))[:3] == (0,0,0)
    assert first.get_at((14,5))[:3] == (255,0,0)
    compare(first, base.png(root, (32,24)))
    assert base.report['unsupported'][0]['feature'] == 'nonfinite_transform_not_rendered'
    assert cache.stats()['invalid_transforms'] >= 1
    # Unsupported effects still use SVG, with identical invalid-subtree handling.
    root.children[2].filters = ({'kind':'unsupported'},)
    compare(cache.frame(root, (32,24)), base.png(root, (32,24)))
    assert cache.fallback_frames == 1
    group.children[1].matrix = Matrix(tx=2,ty=2)
    root.children[2].filters = ()
    assert cache.frame(root, (32,24)).get_at((3,3))[:3] == (255,0,0)
    assert cache.stats()['invalid_transforms'] == 0


def test_invalid_mask_is_empty_coverage_and_does_not_expose_masked_content(display):
    root = synthetic()
    root.apply(Operation(1, {'character_id':1,'clip_depth':2,'matrix':Matrix(tx=float('nan'))}))
    root.apply(Operation(2, {'character_id':1}))
    root.apply(Operation(3, {'character_id':1,'matrix':Matrix(tx=12)}))
    base = SceneRenderer(RectAssets(),flash_masks=True)
    cache = SurfaceRenderer(base,display)
    image = compare(cache.frame(root,(32,24)),base.png(root,(32,24)))
    assert image.getpixel((2,2)) == (0,0,0)
    assert image.getpixel((14,2)) == (255,0,0)


def test_original_city_nan_transform_does_not_crash_or_change_gameplay(display):
    menu = SetupMenu(0); menu.press('splashScreenMC')
    menu.press('BTN_allLeaders_screen1'); menu.start_game()
    clip = next(iter(menu.gameplay.city_clips.values()))
    city = clip.node
    original = city.matrix
    frame = menu.surface(display)
    from wd2.runtime import U
    for key in ('_x','_y','_xscale','_yscale','_rotation','_alpha'):
        clip.set(key,U)
    assert city.matrix == original and menu.surface(display) is frame
    city.matrix = Matrix(tx=float('nan'))
    state, rng = menu.game.snapshot(), menu.rt.rng.getstate()
    compare(menu.surface(display),menu.png())
    assert menu._surface_renderer.stats()['invalid_transforms'] >= 1
    city.matrix = original
    compare(menu.surface(display),menu.png())
    assert menu.game.snapshot() == state and menu.rt.rng.getstate() == rng


def test_original_dynamic_text_with_invalid_transform_is_reported_and_recovers(display):
    menu = SetupMenu(0); menu.press('splashScreenMC')
    field = get(get(menu.root,'gameMenu'),'leaderText')
    field.set('text','Visible leader')
    original = field.node.matrix
    field.node.matrix = Matrix(tx=float('nan'))
    compare(menu.surface(display),menu.png())
    assert any(e['feature'] == 'nonfinite_transform_not_rendered' for e in menu.renderer.report['unsupported'])
    field.node.matrix = original
    compare(menu.surface(display),menu.png())


def test_composed_transforms_masks_color_depth_removal_and_animation_invalidate_cache(display):
    root = synthetic()
    root.apply(Operation(1, {'character_id': 1, 'clip_depth': 3, 'matrix': Matrix(a=.5)}))
    root.apply(Operation(2, {'character_id': 2}))
    root.apply(Operation(3, {'character_id': 1, 'matrix': Matrix(tx=2),
                           'color': ColorTransform((0, 1, 1, .5), (20, 40, 60, 0))}))
    root.apply(Operation(4, {'character_id': 2, 'matrix': Matrix(0, 1, -1, 0, 15, 2)}))
    base = SceneRenderer(RectAssets()); cache = SurfaceRenderer(base, display)
    first = compare(cache.frame(root, (24, 16)), base.png(root, (24, 16)))
    root.children[2].goto_and_stop(2)
    second = compare(cache.frame(root, (24, 16)), base.png(root, (24, 16)))
    assert ImageChops.difference(first, second).getbbox()
    root.children[4].matrix = Matrix(1, .25, .4, 1, 10, 1)
    compare(cache.frame(root, (24, 16)), base.png(root, (24, 16)))
    root.children[4].visible = False
    root.apply(Operation(3, remove=True))
    compare(cache.frame(root, (24, 16)), base.png(root, (24, 16)))
    # A parent filter must apply after its children have composited.
    root.color = ColorTransform((1, 1, 1, .5))
    compare(cache.frame(root, (24, 16)), base.png(root, (24, 16)))


def test_surface_lru_bounds_transformed_states_and_unsupported_effect_fallback(display):
    root = synthetic(); root.apply(Operation(1, {'character_id': 1}))
    base = SceneRenderer(RectAssets())
    cache = SurfaceRenderer(base, display, layer_entries=2, layer_bytes=1024,
                            frame_entries=2, frame_bytes=8192)
    for x in range(12):
        root.children[1].matrix = Matrix(tx=x)
        compare(cache.frame(root, (24, 16)), base.png(root, (24, 16)))
    assert len(cache.layers.items) <= 2 and cache.layers.bytes <= 1024
    assert len(cache.frames.items) <= 2 and cache.frames.bytes <= 8192
    assert cache.layers.evictions > 0
    root.children[1].filters = ({'kind': 'unsupported'},)
    compare(cache.frame(root, (24, 16)), base.png(root, (24, 16)))
    assert cache.fallback_frames == 1
    assert base.report['unsupported'][0]['feature'] == 'bitmap_filters_not_rendered'


def test_missing_artwork_retains_existing_svg_diagnostic(display):
    class MissingAssets(RectAssets):
        def bounds(self, symbol):
            raise NotImplementedError('Missing leaf artwork')
        def load(self, symbol):
            raise NotImplementedError('Missing leaf artwork')
    root = synthetic(); root.apply(Operation(1, {'character_id': 1}))
    base = SceneRenderer(MissingAssets())
    cache = SurfaceRenderer(base, display)
    compare(cache.frame(root, (24, 16)), base.png(root, (24, 16)))
    assert base.report['unsupported'][0]['feature'] == 'Missing leaf artwork'


def test_transparent_layers_composite_once_before_opaque_stage(display):
    root = synthetic(); root.apply(Operation(1, {'character_id': 2}))
    parent = root.children[1]
    parent.children[1].color = ColorTransform((1, 1, 1, .5))
    parent.apply(Operation(2, {'character_id': 1, 'matrix': Matrix(tx=2),
                             'color': ColorTransform((0, 0, 0, .5), (0, 0, 255, 0))}))
    base = SceneRenderer(RectAssets()); cache = SurfaceRenderer(base, display)
    surface = cache.frame(root, (24, 16))
    # Half-blue over half-red over black: red=.25, blue=.5. Straight-alpha
    # intermediate blits incorrectly darken/reweight this overlap.
    assert surface.get_at((3, 2))[:3] == pytest.approx((64, 0, 128), abs=1)
    compare(surface, base.png(root, (24, 16)))


def test_numeric_zero_text_is_visible_in_cached_original_field(display):
    menu = SetupMenu(0); menu.press('splashScreenMC')
    before = Image.open(io.BytesIO(menu.png())).convert('RGB')
    field = get(get(menu.root, 'gameMenu'), 'leaderText')
    field.set('text', 0)
    reference = Image.open(io.BytesIO(menu.png())).convert('RGB')
    changed = ImageChops.difference(before, reference).getbbox()
    assert changed
    surface = menu.surface(display)
    actual = Image.frombytes('RGB', surface.get_size(), pygame.image.tobytes(surface, 'RGB'))
    delta = ImageStat.Stat(ImageChops.difference(actual.crop(changed), reference.crop(changed)))
    assert max(delta.mean) < 1


def test_cached_gameplay_keeps_24hz_callbacks_and_authored_animation(display):
    menu = SetupMenu(0); menu.press('splashScreenMC')
    menu.press('BTN_allLeaders_screen1'); game = menu.start_game()
    first = pygame.image.tobytes(menu.surface(display), 'RGB')
    state, rng = game.snapshot(), game.rt.rng.getstate()
    callbacks = []
    menu.root.set('onEnterFrame', lambda: callbacks.append(menu.host.clock.ticks))
    for _ in range(24):
        menu.host.clock.step()
        menu.surface(display)
    assert len(callbacks) == 24 and menu.host.clock.milliseconds == 1000
    assert pygame.image.tobytes(menu.surface(display), 'RGB') != first
    compare(menu.surface(display), menu.png())
    assert game.snapshot() == state and game.rt.rng.getstate() == rng


def test_integer_motion_reuses_registered_raster_and_preserves_fractional_edges(display, monkeypatch):
    root = synthetic()
    root.apply(Operation(1, {'character_id': 1, 'matrix': Matrix(tx=3.25, ty=5.5)}))
    base = SceneRenderer(RectAssets()); cache = SurfaceRenderer(base, display)
    compare(cache.frame(root, (64, 64)), base.png(root, (64, 64)))
    count = cache.rasterizations
    for x in (4.25, 18.25, -1.75, 25.25):
        root.children[1].matrix = Matrix(tx=x, ty=5.5)
        compare(cache.frame(root, (64, 64)), base.png(root, (64, 64)))
    assert cache.rasterizations == count


def test_flash_timeline_mask_ignores_alpha_and_color_but_inspector_retains_export_mode(display):
    root = synthetic()
    root.apply(Operation(1, {'character_id': 1, 'clip_depth': 2,
                             'color': ColorTransform((0,0,0,.2))}))
    root.apply(Operation(2, {'character_id': 1}))
    flash = SceneRenderer(RectAssets(), flash_masks=True)
    cache = SurfaceRenderer(flash, display)
    image = compare(cache.frame(root, (24,16)), flash.png(root, (24,16)))
    assert image.getpixel((3,3)) == (255,0,0)
    legacy = SceneRenderer(RectAssets())
    assert Image.open(io.BytesIO(legacy.png(root,(24,16)))).getpixel((3,3))[0] < 255
