"""Original opening timelines and converted video/stream audio presentation."""
from .generated import register_all
from .menu_audio import MenuAudio
from .menu_renderer import MenuRenderer
from .movieclip_host import MovieClipHost
from .runtime import Runtime, U, get
from .resources import RUNTIME


class TimelineAudio:
    def __init__(self, audio, metadata):
        self.audio, self.events = audio, metadata['timeline_sounds']
        self.active = {}

    def enter(self, node):
        for event in self.events.get(str(node.character_id),{}).get(str(node.frame),[]):
            sid = event['sound_id']
            previous = self.active.get(sid)
            if event['stop']:
                if previous:
                    previous.stop()
                continue
            if event['no_multiple'] and previous and previous.playing:
                continue
            if event['sample_in'] or event['sample_out'] or len(event['envelope']) > 1:
                self.audio.events.append({'event':'unsupported_timeline_envelope','sound_id':sid})
                continue
            sound = self.audio.new_sound()
            sound.linkage = sid
            self.audio.asset(sid)
            if event['envelope']:
                _, left, right = event['envelope'][0]
                maximum = max(left,right)
                sound.set_volume(maximum/32768*100)
                sound.set_pan(100*(right-left)/maximum if maximum else 0)
            sound.start(0,event['loops'])
            self.active[sid] = sound


class Opening:
    def __init__(self, menu):
        from .setup_menu import reachable
        self.menu = menu
        self.tree = menu.document.root(2)
        self.rt = Runtime(menu.seed); register_all(self.rt)
        self.host = MovieClipHost(self.rt,self.tree,reachable(menu.document,(5808,5782))|{0})
        # Main is already initialized by SetupMenu. Root frame 10's second
        # action constructs Main; keep only the original first stop action here.
        self.host.scripts[(0,10)] = [entry for entry in self.host.scripts.get((0,10),[]) if entry[0] == 1]
        self.host.root.set('getBytesLoaded',lambda:menu.renderer.assets.opening['source_size'])
        self.host.root.set('getBytesTotal',lambda:menu.renderer.assets.opening['source_size'])
        self.renderer = MenuRenderer(menu.document,menu.renderer.assets,self.host)
        self.audio = MenuAudio(self.rt,menu.document)
        self.audio.backend = menu.audio.backend
        self.sounds = TimelineAudio(self.audio,menu.renderer.assets.opening)
        self.host.timeline_sound = self.sounds.enter
        self.host.enter(self.tree)
        self.done = False

    def step(self,ticks=1):
        for _ in range(ticks):
            if self.done or self.host.clock.paused:
                break
            self.rt.reset_budget()
            self.host.clock.step()
            if self.tree.frame == 10:
                self.done = True
                self.audio.close()
