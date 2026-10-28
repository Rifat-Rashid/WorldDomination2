"""AS2 Sound bridge for recovered splash/menu logic and extracted sound assets.

Logical sound commands work without a device for deterministic tests/captures.
Only the interactive window connects a Pygame backend. No game RNG is involved.
"""
import io

from .runtime import ASObject, NativeClass, U, get, number, string
from .swf_scene import ROOT
from .resources import asset_directory, asset_path, read_asset


class MenuSound(ASObject):
    def __init__(self, host, owner=U):
        super().__init__(rt=host.rt)
        self.host, self.owner = host, owner
        self.linkage = None
        self.volume, self.pan = 100, 0
        self.playing = False
        self.loops = 1
        self.channel = None
        self.props.update({'attachSound': self.attach, 'start': self.start, 'stop': self.stop,
            'setVolume': self.set_volume, 'getVolume': lambda: self.volume,
            'setPan': self.set_pan, 'getPan': lambda: self.pan})

    def attach(self, linkage):
        linkage = string(linkage)
        if linkage not in self.host.linkages:
            self.host.events.append({'event': 'missing_linkage', 'linkage': linkage})
            return U  # The original space sequence requests an absent symbol.
        self.host.asset(linkage)  # Verify against original linkage ID and extraction.
        self.stop()
        self.linkage = linkage
        return U

    def start(self, offset=0, loops=1):
        if number(offset) != 0:
            raise ValueError('Nonzero Sound.start offsets are outside the menu audio slice')
        if self.linkage is None:
            return U
        self.loops = max(1, int(number(loops)))  # AS2 uses 0/1 for one play; SDL uses 0.
        self.playing = True
        self.host.events.append({'event': 'start', 'linkage': self.linkage,
                                 'loops': self.loops, 'volume': self.volume, 'pan': self.pan})
        if self.host.backend:
            self.host.backend.start(self)
        return U

    def stop(self):
        if self.host.backend:
            self.host.backend.stop(self)
        if self.playing:
            self.host.events.append({'event': 'stop', 'linkage': self.linkage})
        self.playing = False
        return U

    def set_volume(self, value):
        self.volume = min(100, max(0, number(value)))
        if self.host.backend:
            self.host.backend.volume(self)
        return U

    def set_pan(self, value):
        self.pan = min(100, max(-100, number(value)))
        if self.host.backend:
            self.host.backend.volume(self)
        return U


class MenuAudio:
    def __init__(self, rt, document):
        self.rt = rt
        self.linkages = {s.linkage: sid for sid, s in document.symbols.items() if s.kind == 14 and s.linkage}
        self.sounds = []
        self.events = []
        self.theme = None
        self.backend = None
        self.paused = False
        self.extra_assets = {}
        rt.globals.set('Sound', NativeClass(self.new_sound))

    def asset(self, linkage):
        if linkage in self.extra_assets:
            return asset_path(self.extra_assets[linkage])
        sid = linkage if isinstance(linkage, int) else self.linkages.get(linkage)
        if sid is None:
            raise ValueError(f'Unknown original sound linkage: {linkage}')
        path = next(asset_directory('audio').glob(f'{sid}_*'), None)
        if path is None:
            path = next(asset_directory('audio').glob(f'{sid}.*'), None)
        if path is None:
            raise FileNotFoundError(f'Missing extracted sound {sid}: {linkage}')
        return asset_path(path)

    def new_sound(self, owner=U):
        sound = MenuSound(self, owner)
        self.sounds.append(sound)
        return sound

    def connect(self, backend):
        if self.backend:
            raise RuntimeError('Menu audio already connected')
        self.backend = backend
        # Do not replay transient initialization effects when opening a device.
        for sound in self.sounds:
            if sound is not self.theme:
                sound.playing = False
        if self.theme and self.theme.playing:
            backend.start(self.theme)
        backend.pause(self.paused)

    def complete(self, sound):
        if not sound.playing:
            return
        sound.playing = False
        self.events.append({'event': 'complete', 'linkage': sound.linkage})
        callback = get(sound, 'onSoundComplete')
        if callback is not U:
            self.rt.call(callback, sound, [])

    def poll(self):
        if self.backend and not self.paused:
            self.backend.poll()

    def pause(self, paused):
        self.paused = bool(paused)
        if self.backend:
            self.backend.pause(self.paused)

    def close(self):
        for sound in self.sounds:
            sound.stop()


class PygameMenuAudio:
    """Mixer channels keep music independent from overlapping menu effects."""
    def __init__(self, host, pygame):
        self.host, self.pg = host, pygame
        if not pygame.mixer.get_init():
            pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        pygame.mixer.set_num_channels(max(16, pygame.mixer.get_num_channels()))
        self.samples = {}
        self.slots = {}
        self.paused = False

    def sample(self, linkage):
        if linkage not in self.samples:
            self.samples[linkage] = self.pg.mixer.Sound(file=io.BytesIO(read_asset(self.host.asset(linkage))))
        return self.samples[linkage]

    def start(self, sound):
        self.stop(sound)
        if sound is self.host.theme:
            slot = 0
        else:
            # Effects cannot steal the dedicated music channel, even when full.
            slot = next((i for i in range(1, self.pg.mixer.get_num_channels())
                         if not self.pg.mixer.Channel(i).get_busy()), 1)
        previous = self.slots.get(slot)
        if previous:
            previous.playing = False
            previous.channel = None
        channel = self.pg.mixer.Channel(slot)
        self.slots[slot] = sound
        sound.channel = slot
        channel.play(self.sample(sound.linkage), loops=sound.loops-1)
        self.volume(sound)
        if self.paused:
            channel.pause()

    def volume(self, sound):
        if sound.channel is not None and self.slots.get(sound.channel) is sound:
            v, pan = sound.volume/100, sound.pan/100
            self.pg.mixer.Channel(sound.channel).set_volume(v*(1-max(pan, 0)), v*(1+min(pan, 0)))

    def stop(self, sound):
        if sound.channel is not None and self.slots.get(sound.channel) is sound:
            self.pg.mixer.Channel(sound.channel).stop()
            del self.slots[sound.channel]
        sound.channel = None

    def poll(self):
        for slot, sound in list(self.slots.items()):
            if not self.pg.mixer.Channel(slot).get_busy() and self.slots.get(slot) is sound:
                del self.slots[slot]
                sound.channel = None
                sound.host.complete(sound)

    def pause(self, paused):
        self.paused = bool(paused)
        for slot in self.slots:
            channel = self.pg.mixer.Channel(slot)
            channel.pause() if self.paused else channel.unpause()
