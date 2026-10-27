import io
from pathlib import Path

from PIL import Image, ImageChops, ImageStat
import pytest

from wd2.setup_menu import SetupMenu
from wd2.runtime import get

ROOT = Path(__file__).resolve().parents[1]


def test_original_splash_and_leader_callbacks_update_model_and_display_tree():
    menu = SetupMenu(0)
    assert menu.tree.named('splashScreenMC').visible
    assert not menu.tree.named('gameMenu').visible
    assert get(menu.menu_model, 'difficulty') == 1
    assert get(menu.menu_model, 'player_color') == 5
    assert get(menu.menu_model, 'selected_building') == 4
    # Actual source shape bounds, not hard-coded replacement UI rectangles.
    assert menu.bounds['BTN_allLeaders_screen1'][0] == pytest.approx(171.95)
    menu.click((400, 500))  # Exact translated Main.f_8 callback.
    assert not menu.tree.named('splashScreenMC').visible
    assert menu.tree.named('gameMenu').visible
    menu.click((205, 373))  # Bound ASFunction from Presenter_gameMenu.set_btn_func.
    assert list(get(menu.menu_model, 'selected_leader_arr')) == [0]
    source = get(menu.root, 'gameMenu')
    assert get(get(get(source, 'allLeaderScreen1'), 'aliveMC'), '_alpha') == 20
    assert get(get(get(source, 'leaderScrn1'), 'aliveMC'), '_currentframe') == 1
    assert get(get(source, 'btnCancel1'), '_currentframe') == 2
    assert get(get(source, 'scrn_start'), '_currentframe') == 2
    menu.click((205, 373))  # Duplicate selection rejected by original logic.
    assert list(get(menu.menu_model, 'selected_leader_arr')) == [0]
    menu.click((352, 260))  # Original selected-leader cancellation control.
    assert list(get(menu.menu_model, 'selected_leader_arr')) == []
    assert get(get(source, 'scrn_start'), '_currentframe') == 1


def test_menu_clock_and_rendering_do_not_consume_rng_or_progress_game_turns():
    menu = SetupMenu(0)
    menu.press('splashScreenMC')
    before, rng = menu.snapshot(), menu.rt.rng.getstate()
    # Rendering is pure with respect to both recovered menu state and RNG.
    initial = menu.png()
    assert menu.png() == initial
    assert menu.snapshot() == before and menu.rt.rng.getstate() == rng
    menu.host.clock.step(24)
    after = menu.snapshot()
    assert {k:v for k,v in after.items() if k != 'ticks'} == {k:v for k,v in before.items() if k != 'ticks'}
    assert after['ticks'] == 24 and menu.rt.rng.getstate() == rng
    # View.setMapFrames loops over absent source anchors: recorded AS2 no-ops,
    # also visible in the original SWF (not fabricated menu children).
    assert menu.rt.missing_calls == {'gotoAndStop': 4}
    assert get(menu.model, 'game_initiated') is not True


@pytest.mark.parametrize('selected', [False, True])
def test_initialized_menu_against_corresponding_original_ruffle_capture(selected):
    menu = SetupMenu(0)
    menu.press('splashScreenMC')
    if selected:
        menu.press('BTN_allLeaders_screen1')
    image = Image.open(io.BytesIO(menu.png())).convert('RGB')
    suffix = 'selected' if selected else 'initial'
    reference = Image.open(ROOT / f'validation/ruffle_menu/setup_menu_{suffix}.png').convert('RGB')
    assert image.size == reference.size == (800, 600)
    # A tolerance test, not a pixel-parity assertion. Ruffle's arrow animation
    # phase, text rasterization, and selected portrait effects differ.
    assert max(ImageStat.Stat(ImageChops.difference(image, reference)).mean) < 1.0


def test_leader_hover_selection_and_rollout_render_with_original_device_font():
    menu = SetupMenu(0)
    menu.press('splashScreenMC')
    baseline = Image.open(io.BytesIO(menu.png())).convert('RGB')
    # The original hover field references font 4465 (Arial, zero embedded
    # glyphs); JPEXS correctly exports no 4465 TTF. Exercise actual mouse motion.
    assert menu.renderer.fields[5824]['font'] == 4465
    assert menu.renderer.font_families[4465] == 'Arial'
    assert 4465 not in menu.renderer.font_paths
    assert menu.renderer.font_path(4465).name == '1_Arial_Arial.ttf'
    menu.motion((205, 373))
    text = get(get(menu.root, 'gameMenu'), 'leaderText')
    assert get(text, 'text') == 'The Bombki'
    hovered = Image.open(io.BytesIO(menu.png())).convert('RGB')
    assert ImageChops.difference(baseline, hovered).getbbox() is not None
    menu.motion((780, 590))
    assert get(text, 'text') == ''
    assert Image.open(io.BytesIO(menu.png())).convert('RGB').tobytes() == baseline.tobytes()
    menu.motion((205, 373))
    menu.click((205, 373))
    assert menu.snapshot()['selected_leaders'] == [0]
    assert Image.open(io.BytesIO(menu.png())).size == (800, 600)
