"""Read SWF timeline control tags directly; never use flattened inventory placements.

Reference: Adobe SWF19, control tags; Ruffle swf/src/read.rs. Unhandled visual
effects retain their original bytes and are explicitly reported by the renderer.
"""
from collections import Counter
import hashlib
from pathlib import Path
import struct
import zlib

from .swf_bits import Bits, records
from .display_list import Matrix, ColorTransform, MovieClip, Operation, Symbol, Timeline

ROOT = Path(__file__).resolve().parents[1]


class Reader:
    def __init__(self, data, pos=0):
        self.data, self.pos = data, pos

    def take(self, count):
        result = self.data[self.pos:self.pos+count]
        if len(result) != count:
            raise ValueError('Truncated SWF control record')
        self.pos += count
        return result

    def u8(self):
        return self.take(1)[0]

    def u16(self):
        return struct.unpack('<H', self.take(2))[0]

    def text(self):
        end = self.data.index(0, self.pos)
        value = self.data[self.pos:end].decode('utf-8', 'replace')
        self.pos = end + 1
        return value

    def matrix(self):
        bits = Bits(self.data, self.pos)
        result = Matrix(*bits.matrix())
        self.pos = bits.align()
        return result

    def color(self, alpha=True):
        bits = Bits(self.data, self.pos)
        has_add, has_mult, n = bits.read(1), bits.read(1), bits.read(4)
        channels = 4 if alpha else 3
        mult = tuple(bits.read(n, True)/256 for _ in range(channels)) if has_mult else (1,)*channels
        add = tuple(bits.read(n, True) for _ in range(channels)) if has_add else (0,)*channels
        self.pos = bits.align()
        return ColorTransform(mult if alpha else mult+(1,), add if alpha else add+(0,))

    def filters(self):
        result = []
        for _ in range(self.u8()):
            kind = self.u8()
            start = self.pos
            fixed_sizes = {0: 23, 1: 9, 2: 15, 3: 27, 6: 80}
            if kind in fixed_sizes:
                self.take(fixed_sizes[kind])
            elif kind in (4, 7):
                self.take(self.u8()*5 + 19)
            elif kind == 5:
                cols, rows = self.u8(), self.u8()
                self.take(13 + cols*rows*4)
            else:
                raise ValueError(f'Unknown filter type {kind}')
            result.append({'id': kind, 'data_hex': self.data[start:self.pos].hex()})
        return tuple(result)


def parse_place(data, kind=26, offset=0):
    r = Reader(data)
    flags = r.u8()
    extra = r.u8() if kind == 70 else 0
    depth = r.u16()
    values = {}
    if extra & 8 or (extra & 16 and not flags & 2):
        values['class_name'] = r.text()
    if flags & 2:
        values['character_id'] = r.u16()
    if flags & 4:
        values['matrix'] = r.matrix()
    if flags & 8:
        values['color'] = r.color()
    if flags & 16:
        values['ratio'] = r.u16()
    if flags & 32:
        values['name'] = r.text()
    if flags & 64:
        values['clip_depth'] = r.u16()
    if extra & 1:
        values['filters'] = r.filters()
    if extra & 2:
        values['blend_mode'] = r.u8()
    if extra & 4:
        values['cache_as_bitmap'] = bool(r.u8())
    if extra & 32:
        values['visible'] = bool(r.u8())
    if extra & 64:
        values['background_rgba'] = list(r.take(4))
    if flags & 128:
        values['clip_actions_hex'] = r.take(len(data)-r.pos).hex()
    if r.pos != len(data):
        raise ValueError(f'Unparsed PlaceObject bytes at {offset}: {len(data)-r.pos}')
    return Operation(depth, values, bool(flags & 1), offset=offset, tag=kind)


class SWFDocument:
    def __init__(self, path=ROOT / 'WorldDomination2.swf'):
        original = Path(path).read_bytes()
        self.sha256 = hashlib.sha256(original).hexdigest()
        raw = original
        if raw[:3] == b'CWS':
            raw = b'FWS' + raw[3:8] + zlib.decompress(raw[8:])
        if raw[:3] != b'FWS':
            raise ValueError('Only FWS and CWS are supported')
        if len(raw) != struct.unpack_from('<I', raw, 4)[0]:
            raise ValueError('SWF byte length mismatch')
        self.raw = raw
        bits = Bits(raw, 8)
        n = bits.read(5)
        self.bounds = tuple(bits.read(n, True)/20 for _ in range(4))
        start = bits.align()
        fps, self.frame_count = struct.unpack_from('<HH', raw, start)
        self.fps = fps/256
        self.symbols = {}
        self.tag_counts = Counter()
        self.background = (0, 0, 0)
        root = self._timeline(start+4, len(raw), self.frame_count)
        self.symbols[0] = Symbol(0, 0, '_root', root)

    def _timeline(self, start, end, frame_count):
        timeline = Timeline([[] for _ in range(frame_count)])
        frame = 0
        # Definition tags with a leading character ID (not sound/stream records).
        definitions = {2, 6, 7, 10, 11, 14, 20, 21, 22, 32, 33, 34, 35,
                       36, 37, 39, 46, 48, 60, 75, 83, 84, 87, 90, 91}
        for _, kind, offset, payload, size in records(self.raw, start, end):
            self.tag_counts[kind] += 1
            data = self.raw[payload:payload+size]
            if kind == 1:
                frame += 1
            elif kind in (26, 70):
                timeline.frames[frame].append(parse_place(data, kind, offset))
            elif kind == 28:
                timeline.frames[frame].append(Operation(Reader(data).u16(), remove=True, offset=offset, tag=kind))
            elif kind == 43:
                timeline.labels[Reader(data).text()] = frame+1
            elif kind in (12, 59):
                timeline.actions.setdefault(frame+1, []).append(offset)
            elif kind == 56:
                r = Reader(data)
                for _ in range(r.u16()):
                    sid, linkage = r.u16(), r.text()
                    self.symbols[sid].linkage = linkage
            elif kind == 9:
                self.background = tuple(data)
            elif kind in definitions:
                sid = struct.unpack_from('<H', data)[0]
                symbol = Symbol(sid, kind)
                self.symbols[sid] = symbol
                if kind == 39:
                    count = struct.unpack_from('<H', data, 2)[0]
                    symbol.timeline = self._timeline(payload+4, payload+size, count)
                elif kind == 34:
                    symbol.timeline = self._button(data, offset)
        # Authoring tools emit empty one-frame sprites without a ShowFrame.
        if frame != frame_count and not (frame == 0 and frame_count == 1 and not timeline.frames[0]):
            raise ValueError(f'Expected {frame_count} ShowFrame tags, got {frame}')
        return timeline

    def _button(self, data, offset):
        # A deterministic button "up" display state; actions/hit testing deferred.
        r = Reader(data, 2)
        r.u8()
        action_offset = r.u16()
        ops = []
        while flags := r.u8():
            sid, depth = r.u16(), r.u16()
            values = {'character_id': sid, 'matrix': r.matrix(), 'color': r.color()}
            if flags & 16:
                values['filters'] = r.filters()
            if flags & 32:
                values['blend_mode'] = r.u8()
            if flags & 1:
                ops.append(Operation(depth, values, offset=offset, tag=34))
        return Timeline([ops], actions={1: [offset]} if action_offset else {})

    def root(self, frame=10):
        return MovieClip(self.symbols).goto_frame(frame)
