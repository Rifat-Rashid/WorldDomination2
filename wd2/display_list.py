"""Small, model-independent SWF display tree. Coordinates are stage pixels.

This module deliberately does not execute AVM1 scripts or model callbacks.
Seeking constructs timeline state; it is not a simulation of initialized Flash.
"""
from dataclasses import dataclass, field, asdict
import math


@dataclass(frozen=True)
class Matrix:
    a: float = 1
    b: float = 0
    c: float = 0
    d: float = 1
    tx: float = 0
    ty: float = 0

    def is_finite(self):
        return all(math.isfinite(v) for v in (self.a, self.b, self.c, self.d, self.tx, self.ty))

    def __matmul__(self, other):
        return Matrix(self.a*other.a+self.c*other.b, self.b*other.a+self.d*other.b,
                      self.a*other.c+self.c*other.d, self.b*other.c+self.d*other.d,
                      self.a*other.tx+self.c*other.ty+self.tx,
                      self.b*other.tx+self.d*other.ty+self.ty)

    def point(self, x, y):
        return self.a*x+self.c*y+self.tx, self.b*x+self.d*y+self.ty

    def svg(self):
        return 'matrix(' + ' '.join(str(v) for v in asdict(self).values()) + ')'


@dataclass(frozen=True)
class ColorTransform:
    mult: tuple = (1, 1, 1, 1)
    add: tuple = (0, 0, 0, 0)


@dataclass
class Operation:
    depth: int
    values: dict = field(default_factory=dict)
    move: bool = False
    remove: bool = False
    offset: int = 0
    tag: int = 26


@dataclass
class Timeline:
    frames: list = field(default_factory=lambda: [[]])
    labels: dict = field(default_factory=dict)
    actions: dict = field(default_factory=dict)


@dataclass
class Symbol:
    character_id: int
    kind: int
    linkage: str = ''
    timeline: Timeline | None = None


class MovieClip:
    """One instance per placement, with local state and depth-indexed children."""
    def __init__(self, symbols, character_id=0, parent=None, depth=0):
        self.symbols = symbols
        self.symbol = symbols[character_id]
        self.parent, self.depth = parent, depth
        self.name = ''
        self.matrix = Matrix()
        self.color = ColorTransform()
        self.visible = True
        self.clip_depth = 0
        self.ratio = 0
        self.filters = ()
        self.blend_mode = 1
        self.cache_as_bitmap = False
        self.extras = {}
        self.children = {}
        self.frame = 0
        self.playing = True
        self.placement_offset = 0
        if self.symbol.timeline:
            self.goto_frame(1)

    @property
    def character_id(self):
        return self.symbol.character_id

    @property
    def world_matrix(self):
        return self.parent.world_matrix @ self.matrix if self.parent else self.matrix

    def named(self, name):
        return next((c for c in self.children.values() if c.name == name), None)

    def ordered(self):
        return [self.children[k] for k in sorted(self.children)]

    def apply(self, op):
        previous = self.children.get(op.depth)
        if op.remove:
            if previous:
                previous.parent = None
                del self.children[op.depth]
            return
        values = dict(op.values)
        character_id = values.pop('character_id', None)
        if character_id is None:
            if previous is None:
                raise ValueError(f'Move at empty depth {op.depth}, SWF offset {op.offset}')
            child = previous
        else:
            child = MovieClip(self.symbols, character_id, self, op.depth)
            if previous:
                if op.move:
                    for key in ('name', 'matrix', 'color', 'visible', 'clip_depth', 'ratio',
                                'filters', 'blend_mode', 'cache_as_bitmap'):
                        setattr(child, key, getattr(previous, key))
                    child.extras = dict(previous.extras)
                previous.parent = None
            self.children[op.depth] = child
        for key, value in values.items():
            if key in ('name', 'matrix', 'color', 'visible', 'clip_depth', 'ratio',
                       'filters', 'blend_mode', 'cache_as_bitmap'):
                setattr(child, key, value)
            else:
                child.extras[key] = value
        child.placement_offset = op.offset

    def goto_frame(self, target):
        timeline = self.symbol.timeline
        if timeline is None:
            raise ValueError('Leaf has no timeline')
        if isinstance(target, str):
            target = timeline.labels[target]
        if not 1 <= target <= len(timeline.frames):
            raise ValueError(f'Invalid frame {target} for {self.character_id}')
        if target < self.frame:
            for child in self.children.values():
                child.parent = None
            self.children.clear()
            self.frame = 0
        while self.frame < target:
            for op in timeline.frames[self.frame]:
                self.apply(op)
            self.frame += 1
        return self

    def goto_and_stop(self, target):
        self.goto_frame(target)
        self.playing = False

    def goto_and_play(self, target):
        self.goto_frame(target)
        self.playing = True

    def advance(self):
        # Children newly placed this tick start at frame 1, not frame 2.
        existing = list(self.children.values())
        if self.playing and self.symbol.timeline:
            self.goto_frame(self.frame % len(self.symbol.timeline.frames) + 1)
        for child in existing:
            if child.parent is self:
                child.advance()

    def walk(self):
        yield self
        for child in self.ordered():
            yield from child.walk()

    def dump(self):
        return {
            'character_id': self.character_id, 'linkage': self.symbol.linkage,
            'kind': self.symbol.kind, 'name': self.name, 'depth': self.depth,
            'frame': self.frame, 'playing': self.playing, 'visible': self.visible,
            'matrix': asdict(self.matrix), 'world_matrix': asdict(self.world_matrix),
            'color': asdict(self.color), 'clip_depth': self.clip_depth,
            'ratio': self.ratio, 'filters': list(self.filters),
            'blend_mode': self.blend_mode, 'placement_offset': self.placement_offset,
            'extras': self.extras,
            'labels': self.symbol.timeline.labels if self.symbol.timeline else {},
            'unexecuted_action_offsets': self.symbol.timeline.actions.get(self.frame, []) if self.symbol.timeline else [],
            'children': [c.dump() for c in self.ordered()],
        }
