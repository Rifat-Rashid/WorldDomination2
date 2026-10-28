import io
import json
from pathlib import Path
import wave

from PIL import Image, ImageChops, ImageStat
import pytest

from wd2.runtime import get
from wd2.setup_menu import SetupMenu
from wd2.opening_assets import interpolate
from wd2.resources import RUNTIME


def test_recovered_logo_loading_video_and_theme_handoff_keep_menu_identity_rng():
    m = SetupMenu(0)
    model, rng = m.model, m.rt.rng.getstate()
    m.begin_opening()
    opening = m.opening
    m.step(48)
    assert opening.tree.frame == 2
    assert Image.open(io.BytesIO(m.png())).size == (800,600)
    assert not opening.renderer.report['unsupported']
    assert any(e.get('linkage') == 5786 for e in opening.audio.events)
    m.step(100)
    assert m.opening is None and m.tree.named('introMovie').visible
    first = m.png(); m.step(); assert m.png() != first
    assert not m.audio.theme.playing and m.intro_sound.playing
    m.step(200)
    assert not m.tree.named('introMovie').visible and m.tree.named('splashScreenMC').visible
    assert m.audio.theme.playing and m.intro_sound is None
    assert m.model is model and m.rt.rng.getstate() == rng and m.game is None
    m.click((400,500)); m.press('BTN_allLeaders_screen1'); m.press('btn_start')
    assert m.game is not None


def test_intro_skip_uses_original_callback_and_stops_stream():
    m = SetupMenu()
    m.begin_intro(); m.step(24)
    sound = m.intro_sound
    assert m.control_at((400,300)) == 'introMovie'
    m.click((400,300))
    assert not m.tree.named('introMovie').visible and not sound.playing
    assert m.audio.theme.playing


def test_opening_pause_and_video_frame_selection():
    m = SetupMenu(); m.begin_opening()
    m.host.clock.pause(); m.step(30)
    assert m.opening.host.clock.ticks == 0
    m.host.clock.resume(); m.step(120)
    video = next(n for n in m.tree.walk() if n.character_id == 5911)
    assert video.parent.frame > 1
    m.rt.invoke(m.host.wrap(video.parent),'gotoAndStop',100)
    assert m.renderer.assets.node_asset_id(video) == 'asset_5911_100'
    image = m.png(); m.step(5); assert m.png() == image


def test_morph_endpoints_and_interpolation_are_explicit():
    assert interpolate('M0 0 Q10 20 30 40','M10 20 Q20 40 50 80',.5) == 'M5.0 10.0 Q15.0 30.0 40.0 60.0'
    assert interpolate('#00ff00','#00ff02',.5) == '#00ff01'
    with pytest.raises(NotImplementedError):
        interpolate('M0 0','M0 0 L10 10',.5)


def test_converted_opening_matches_source_timeline_and_sample_metadata():
    meta = json.loads((RUNTIME/'opening/manifest.json').read_text())
    assert meta['video']['placements'] == [[i+1,5911,i] for i in range(202)]
    assert meta['stream']['blocks'] == 202 and meta['stream']['latency_seek'] == 1633
    with Image.open(RUNTIME/'opening/5911.webp') as video:
        assert video.n_frames == 202 and video.size == (320,240)
    from wd2.resources import read_asset
    with wave.open(io.BytesIO(read_asset(RUNTIME/'opening/intro.wav'))) as sound:
        assert sound.getframerate() == 22050 and sound.getnchannels() == 1
        assert 8 < sound.getnframes()/22050 < 8.5


def test_original_logo_and_video_surroundings_against_ruffle_reference():
    reference = Path(__file__).resolve().parents[1]/'validation/ruffle_battle/original_after_10s.png'
    if not reference.exists():
        pytest.skip('Optional original-player capture')
    m = SetupMenu(); m.begin_intro(); m.step(48)
    python = Image.open(io.BytesIO(m.png())).convert('RGB')
    original = Image.open(reference).convert('RGB')
    # Frame phases differ; compare the authored surround, excluding the video.
    for box in ((0,0,200,600),(570,0,800,600)):
        assert max(ImageStat.Stat(ImageChops.difference(python.crop(box),original.crop(box))).mean) < .3
    parent = next(n.parent for n in m.tree.walk() if n.character_id == 5911)
    m.rt.invoke(m.host.wrap(parent),'gotoAndStop',123)
    aligned = Image.open(io.BytesIO(m.png())).convert('RGB')
    assert max(ImageStat.Stat(ImageChops.difference(aligned,original)).mean) < .6


def test_native_video_surfaces_reuse_background_and_keep_svg_fallback(monkeypatch):
    import pygame
    from wd2.display_list import ColorTransform
    monkeypatch.setenv('SDL_VIDEODRIVER','dummy'); monkeypatch.setenv('SDL_AUDIODRIVER','dummy')
    pygame.init(); pygame.display.set_mode((800,600))
    try:
        m = SetupMenu(); m.begin_intro()
        for frame in (12,100,194):
            parent = next(n.parent for n in m.tree.walk() if n.character_id == 5911)
            m.rt.invoke(m.host.wrap(parent),'gotoAndStop',frame)
            surface = m.surface(pygame)
            actual = Image.frombytes('RGB',surface.get_size(),pygame.image.tobytes(surface,'RGB'))
            expected = Image.open(io.BytesIO(m.png())).convert('RGB')
            assert max(ImageStat.Stat(ImageChops.difference(actual,expected)).mean) < .3
        cache = m._surface_renderer
        assert cache.decoded_frames == 3
        count = cache.rasterizations
        m.rt.invoke(m.host.wrap(parent),'gotoAndStop',193); m.surface(pygame)
        assert cache.rasterizations == count
        video = next(n for n in m.tree.walk() if n.character_id == 5911)
        video.color = ColorTransform((1,1,1,.5))
        m.surface(pygame)
        assert cache.rasterizations > count  # Unsupported native color uses SVG.
    finally:
        pygame.quit()


@pytest.mark.parametrize('intro',[False,True])
def test_authored_opaque_opening_covers_stage_without_changing_live_hierarchy(intro):
    m = SetupMenu()
    if intro:
        m.begin_intro(); m.step(30)
    children = list(m.tree.ordered())
    full = m.renderer.png(m.tree)
    assert m.png() == full or Image.open(io.BytesIO(m.png())).tobytes() == Image.open(io.BytesIO(full)).tobytes()
    coverage = Image.open(io.BytesIO(m.renderer.png(m.render_tree,background=None))).convert('RGBA')
    assert coverage.getextrema()[3] == (255,255)
    assert list(m.tree.ordered()) == children


def test_original_intro_stream_decodes_and_hands_mixer_back_to_theme(monkeypatch):
    import pygame
    from wd2.menu_audio import PygameMenuAudio
    monkeypatch.setenv('SDL_AUDIODRIVER','dummy')
    pygame.mixer.quit(); pygame.mixer.init()
    try:
        m = SetupMenu()
        m.audio.connect(PygameMenuAudio(m.audio,pygame))
        m.begin_intro()
        stream = m.intro_sound
        assert stream.channel != 0 and pygame.mixer.Channel(stream.channel).get_busy()
        m.click((400,300))
        assert stream.channel is None
        assert m.audio.theme.channel == 0 and pygame.mixer.Channel(0).get_busy()
        m.audio.close()
    finally:
        pygame.mixer.quit()
