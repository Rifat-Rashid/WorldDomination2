"""Load converted runtime timeline data without needing the original movie file."""
import gzip
import json

from .display_list import ColorTransform, Matrix, MovieClip, Operation, Symbol, Timeline
from .resources import RUNTIME


class RuntimeScene:
    def __init__(self, path=RUNTIME / 'scene.json.gz'):
        with gzip.open(path, 'rt', encoding='utf-8') as stream:
            data = json.load(stream)
        if data['format'] != 1:
            raise ValueError('Unsupported runtime scene version')
        self.sha256 = data['source_sha256']
        self.bounds = tuple(data['bounds'])
        self.fps, self.frame_count = data['fps'], data['frame_count']
        self.background = tuple(data['background'])
        self.font_families = {int(k): v for k, v in data['font_families'].items()}
        self.text_fields = {int(k): v for k, v in data['text_fields'].items()}
        for field in self.text_fields.values():
            field['bounds'] = tuple(field['bounds'])
            field['color'] = tuple(field['color'])
        self.sound_metadata = {int(k): v for k, v in data['sound_metadata'].items()}
        self.symbols = {}
        for entry in data['symbols']:
            timeline = None
            if entry['timeline'] is not None:
                t = entry['timeline']
                frames = []
                for frame in t['frames']:
                    operations = []
                    for op in frame:
                        values = op['values']
                        if 'matrix' in values:
                            values['matrix'] = Matrix(**values['matrix'])
                        if 'color' in values:
                            c = values['color']
                            values['color'] = ColorTransform(tuple(c['mult']), tuple(c['add']))
                        operations.append(Operation(op['depth'], values, op['move'], op['remove'], tag=op['tag']))
                    frames.append(operations)
                timeline = Timeline(frames, t['labels'], {int(f): [0] for f in t['action_frames']})
            symbol = Symbol(entry['id'], entry['kind'], entry['linkage'], timeline)
            self.symbols[symbol.character_id] = symbol

    def root(self, frame=10):
        return MovieClip(self.symbols).goto_frame(frame)


def load_scene():
    if (RUNTIME / 'scene.json.gz').is_file():
        return RuntimeScene()
    # Optional development fallback. Public distributions always include scene data.
    from .swf_scene import SWFDocument
    return SWFDocument()
