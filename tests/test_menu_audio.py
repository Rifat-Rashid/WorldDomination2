import struct

import pygame
import pytest

from wd2.swf_bits import Bits, records
from wd2.menu_audio import PygameMenuAudio
from wd2.runtime import ASFunction, get
from wd2.setup_menu import SetupMenu


class RecordingBackend:
    def __init__(self):
        self.starts, self.stops, self.pauses = [], [], []

    def start(self, sound):
        self.starts.append((sound.linkage, sound.loops, sound.volume, sound.pan))

    def stop(self, sound):
        self.stops.append(sound.linkage)

    def pause(self, paused):
        self.pauses.append(paused)

    def volume(self, sound):
        pass

    def poll(self):
        pass


def test_legacy_music_toggle_plays_compressed_theme_stream(monkeypatch):
    from wd2.desktop import Desktop
    monkeypatch.setenv('SDL_AUDIODRIVER','dummy')
    pygame.mixer.quit(); pygame.mixer.init()
    desktop = Desktop.__new__(Desktop)
    desktop.pg, desktop.music = pygame, False
    try:
        desktop.toggle_music()
        assert desktop.music and pygame.mixer.music.get_busy()
        assert desktop._music_stream.getbuffer().nbytes > 0
        desktop.toggle_music()
        assert not desktop.music and not pygame.mixer.music.get_busy()
    finally:
        pygame.mixer.quit()


def test_splash_music_original_toggle_loop_callback_and_no_rng_change():
    menu = SetupMenu(0)
    audio, rt = menu.audio, menu.rt
    theme = audio.theme
    option = get(menu.model, 'option')
    assert menu.tree.named('splashScreenMC').visible
    assert get(option, 'music') is True and theme.playing
    assert audio.asset(theme.linkage).name.removesuffix('.gz') == '2_WDTheme.wav.mp3'
    assert isinstance(get(theme, 'onSoundComplete'), ASFunction)
    backend = RecordingBackend()
    audio.connect(backend)
    assert backend.starts == [('WDTheme.wav', 1, 100, 0)]
    rng = rt.rng.getstate()
    audio.complete(theme)  # Actual recovered onSoundComplete calls this.start(0,1).
    assert len(backend.starts) == 2 and theme.playing
    menu.press('splashScreenMC')
    assert len(backend.starts) == 2  # Splash-to-menu must not restart the track.
    menu.press('soundBtn')
    assert get(option, 'music') is False and not theme.playing
    audio.complete(theme)  # A stale completion after stopping must not unmute.
    assert len(backend.starts) == 2
    menu.host.clock.step()
    assert menu.tree.named('gameMenu').named('switch39').frame == 2
    menu.press('soundBtn')
    assert get(option, 'music') is True and theme.playing
    assert len(backend.starts) == 3
    audio.pause(True); audio.pause(False)
    assert backend.pauses == [False, True, False]
    assert rt.rng.getstate() == rng
    audio.close()
    assert not theme.playing and menu.rt.missing_calls == {'gotoAndStop': 4}


def test_original_action_sound_mapping_pan_and_effect_toggle_are_separate_from_music():
    menu = SetupMenu(0)
    audio = menu.audio
    backend = RecordingBackend()
    audio.connect(backend)
    menu.press('splashScreenMC')
    menu.press('soundBtn')  # Music off, effects still on.
    menu.press('BTN_allLeaders_screen1')
    assert backend.starts[-1] == ('interface_Accept action bleep.wav', 1, 100, 0)
    menu.press('btn1')
    assert backend.starts[-1] == ('interface_Switch Action selection.wav', 1, 100, -80)
    menu.press('BTN_selectedLeader_screen1')
    assert backend.starts[-1] == ('interface_Switch Sounds 1.wav', 1, 100, 80)
    count = len(backend.starts)
    menu.rt.invoke(get(menu.model, 'option'), 'setSound')
    menu.press('btn2')
    assert len(backend.starts) == count
    assert not audio.theme.playing


def test_extracted_samples_play_through_mixer_with_isolated_theme_channel(monkeypatch, tmp_path):
    # Real MP3 decoding and channel playback; silent driver keeps CI deterministic.
    monkeypatch.setenv('SDL_AUDIODRIVER', 'dummy')
    pygame.mixer.quit()
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
    menu = SetupMenu(0)
    audio = menu.audio
    backend = PygameMenuAudio(audio, pygame)
    try:
        audio.connect(backend)
        sample = backend.samples['WDTheme.wav']
        from wd2.resources import read_asset
        loose = tmp_path/'original-theme.mp3'
        loose.write_bytes(read_asset(audio.asset('WDTheme.wav')))
        reference = pygame.mixer.Sound(str(loose))
        assert sample.get_raw() == reference.get_raw()
        assert pygame.mixer.Channel(0).get_busy()
        assert any(sample.get_raw())  # Decoded PCM is not silence.
        from wd2.resources import ROOT
        source = ROOT / 'WorldDomination2.swf'
        if source.exists():
            raw = source.read_bytes()
            bits = Bits(raw, 8)
            bits.read(4*bits.read(5))
            tag = next((raw[p:p+s] for _, k, _, p, s in records(raw, bits.align()+4, len(raw))
                        if k == 14 and struct.unpack_from('<H', raw, p)[0] == 2))
            rate = (5512.5, 11025, 22050, 44100)[(tag[2] >> 2) & 3]
            original_duration = struct.unpack_from('<I', tag, 3)[0]/rate
        else:
            metadata = menu.document.sound_metadata[2]
            original_duration = metadata['sample_count']/metadata['rate']
        assert sample.get_length() == pytest.approx(original_duration, abs=.2)
        menu.press('splashScreenMC')
        menu.press('soundBtn')
        assert not pygame.mixer.Channel(0).get_busy()
        menu.press('BTN_allLeaders_screen1')
        effect = audio.sounds[-1]
        assert effect.channel > 0
        assert pygame.mixer.Channel(effect.channel).get_busy()
        menu.press('soundBtn')
        assert pygame.mixer.Channel(0).get_busy()
        # Simulate the native channel's completed state without waiting a track.
        starts = len([e for e in audio.events if e['event'] == 'start' and e['linkage'] == 'WDTheme.wav'])
        pygame.mixer.Channel(0).stop()
        audio.poll()
        assert pygame.mixer.Channel(0).get_busy()
        assert len([e for e in audio.events if e['event'] == 'start' and e['linkage'] == 'WDTheme.wav']) == starts+1
        audio.pause(True)
        audio.poll()
        audio.pause(False)
        assert audio.theme.playing
        audio.close()
        assert not pygame.mixer.Channel(0).get_busy()
    finally:
        audio.close()
        pygame.mixer.quit()
