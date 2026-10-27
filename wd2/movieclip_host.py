"""ASObject adapter for the existing display tree; no headless host changes."""
from dataclasses import replace
import math
import re
import weakref
import html

from .display_list import Matrix, MovieClip, Operation, Symbol, Timeline
from .presentation_clock import PresentationClock
from .runtime import ASObject, ASFunction, U, get, number, string, truth


class ClipObject(ASObject):
    def __init__(self, host, node):
        super().__init__(rt=host.rt)
        self.host, self.node = host, node
        node._as2_object = self  # Lifetime follows the display instance, including its custom properties.
        self.x_sign = 1
        self.methods = {
            'gotoAndStop': lambda target: host.goto(node, target, False),
            'gotoAndPlay': lambda target: host.goto(node, target, True),
            'play': lambda: self._play(True), 'stop': lambda: self._play(False),
            'nextFrame': lambda: host.goto(node, min(node.frame+1, self.get('_totalframes')), False),
            'prevFrame': lambda: host.goto(node, max(1, node.frame-1), False),
            'getDepth': lambda: node.depth,
            'getNextHighestDepth': lambda: max(node.children, default=-1)+1,
            'attachMovie': self.attach,
            'createEmptyMovieClip': lambda name, depth: self.attach(host.empty_id, name, depth),
            'removeMovieClip': self.remove,
            'setTextFormat': lambda fmt: self.set('_textFormat', fmt),
        }

    def _play(self, playing):
        self.node.playing = playing
        return U

    def get(self, key):
        key = string(key)
        node, m = self.node, self.node.matrix
        values = {'_root': self.host.root, '_parent': self.host.wrap(node.parent),
            '_name': node.name, '_x': m.tx, '_y': m.ty,
            '_xscale': math.hypot(m.a, m.b)*100*self.x_sign,
            '_yscale': math.copysign(math.hypot(m.c, m.d)*100, (m.a*m.d-m.b*m.c)*self.x_sign),
            '_rotation': math.degrees(math.atan2(m.b*self.x_sign, m.a*self.x_sign)),
            '_visible': node.visible, '_alpha': node.color.mult[3]*100,
            '_currentframe': node.frame or 1,
            '_totalframes': len(node.symbol.timeline.frames) if node.symbol.timeline else 1}
        if key in values:
            return values[key]
        if key in self.props:
            return super().get(key)
        if key in self.methods:
            return self.methods[key]
        child = node.named(key)
        return self.host.wrap(child) if child else super().get(key)

    def has(self, key):
        key = string(key)
        return key in self.methods or key in ('_root', '_parent', '_name', '_x', '_y',
            '_xscale', '_yscale', '_rotation', '_visible', '_alpha', '_currentframe',
            '_totalframes') or self.node.named(key) is not None or super().has(key)

    def set(self, key, value):
        key = string(key)
        node, m = self.node, self.node.matrix
        if key in ('_x', '_y'):
            node.matrix = replace(m, **{'tx' if key == '_x' else 'ty': number(value)})
        elif key in ('_xscale', '_yscale'):
            current = self.get(key)
            factor = number(value)/current if current else number(value)/100
            if key == '_xscale':
                node.matrix = replace(m, a=m.a*factor if current else factor, b=m.b*factor)
                self.x_sign = -1 if number(value) < 0 else 1
            else:
                node.matrix = replace(m, c=m.c*factor, d=m.d*factor if current else factor)
        elif key == '_rotation':
            angle = math.radians(number(value)-self.get('_rotation'))
            c, s = math.cos(angle), math.sin(angle)
            node.matrix = Matrix(c*m.a-s*m.b, s*m.a+c*m.b, c*m.c-s*m.d, s*m.c+c*m.d, m.tx, m.ty)
        elif key == '_alpha':
            node.color = replace(node.color, mult=(*node.color.mult[:3], number(value)/100))
        elif key == '_visible':
            node.visible = truth(value)
        elif key == '_name':
            node.name = string(value)
        elif key in ('_currentframe', '_totalframes', '_parent', '_root'):
            return value  # Read-only Flash properties.
        else:
            super().set(key, value)
            if node.symbol.kind == 37 and key == 'text':
                self.props['htmlText'] = html.escape(string(value))
            if node.symbol.kind == 37 and key == 'htmlText':
                text = re.sub(r'<br\s*/?>', '\n', string(value), flags=re.I)
                self.props['text'] = html.unescape(re.sub('<[^>]*>', '', text))
            if node.symbol.kind == 37 and key in ('text', 'htmlText', 'textColor', '_textFormat'):
                node.as2_text = self.props
        return value

    def attach(self, linkage, name, depth, init=U):
        sid = linkage if isinstance(linkage, int) else self.host.linkages.get(string(linkage))
        if sid not in self.node.symbols:
            raise ValueError(f'Unknown linkage: {linkage}')
        self.node.apply(Operation(int(number(depth)), {'character_id': sid, 'name': string(name)}))
        child = self.host.wrap(self.node.children[int(number(depth))])
        if isinstance(init, ASObject):
            for key in init.keys():
                child.set(key, get(init, key))
        self.host.enter(child.node)
        return child

    def remove(self):
        node = self.node
        if node.parent and node.parent.children.get(node.depth) is node:
            node.parent.apply(Operation(node.depth, remove=True))
        return U


class MovieClipHost:
    def __init__(self, rt, root, script_symbols=()):
        self.rt, self.tree = rt, root
        self.objects = weakref.WeakValueDictionary()
        self.entered = weakref.WeakKeyDictionary()
        self.script_symbols = set(script_symbols)
        self.scripts = {}
        for path, fn in rt.scripts.items():
            match = re.fullmatch(r'DefineSprite_(\d+)[^/]*/frame_(\d+)/DoAction(?:_(\d+))?\.as', path)
            if match:
                self.scripts.setdefault((int(match[1]), int(match[2])), []).append((int(match[3] or 1), fn))
        self.linkages = {s.linkage: sid for sid, s in root.symbols.items() if s.linkage}
        self.empty_id = min(root.symbols)-1
        root.symbols[self.empty_id] = Symbol(self.empty_id, 39, timeline=Timeline())
        self.root = self.wrap(root)
        rt.root = self.root
        rt.globals.set('_root', self.root)
        rt.globals.set('_level0', self.root)
        self.clock = PresentationClock(self.frame)
        rt.globals.set('setInterval', self.interval)
        rt.globals.set('clearInterval', lambda timer_id: self.clock.clear_interval(timer_id))
        rt.globals.set('getTimer', lambda: int(self.clock.milliseconds))

    def wrap(self, node):
        if node is None:
            return U
        key = id(node)
        if key not in self.objects:
            self.objects[key] = ClipObject(self, node)
        return self.objects[key]

    def attached(self, node):
        while node.parent:
            node = node.parent
        return node is self.tree

    def enter(self, node):
        # Scope script execution to this vertical slice, never initialize Main or combat.
        for child in list(node.ordered()):
            self.enter(child)
        if self.entered.get(node) != node.frame:
            self.entered[node] = node.frame
            if node.character_id in self.script_symbols:
                for _, fn in sorted(self.scripts.get((node.character_id, node.frame), [])):
                    self.rt.call(fn, self.wrap(node), [])

    def goto(self, node, target, playing):
        timeline = node.symbol.timeline
        if timeline is None:
            return U
        if target is U or target is None:
            return U  # Source update_selected_leaders calls gotoAndStop(undefined).
        frame = timeline.labels.get(target) if isinstance(target, str) and target in timeline.labels else int(number(target))
        frame = max(1, min(len(timeline.frames), frame))
        old_frame, old_children = node.frame, dict(node.children)
        node.goto_frame(frame)
        if frame < old_frame:
            # Reconcile children surviving the seek. The inspector deliberately
            # rebuilds backward state; live AS2 references must keep their identity.
            recreated = {op.depth for ops in timeline.frames[frame:old_frame] for op in ops
                         if op.remove or 'character_id' in op.values}
            for depth, new in list(node.children.items()):
                old = old_children.get(depth)
                if old and depth not in recreated and old.character_id == new.character_id:
                    for key in ('matrix', 'color', 'name', 'clip_depth', 'ratio', 'placement_offset'):
                        setattr(old, key, getattr(new, key))
                    new.parent = None
                    old.parent = node
                    node.children[depth] = old
        node.playing = playing
        self.enter(node)
        return U

    def dispatch(self, node, event):
        target = self.wrap(node)
        fn = get(target, event)
        return self.rt.call(fn, target, []) if fn is not U else U

    def frame(self):
        existing = list(self.tree.walk())
        # Stable preorder callbacks, even for stopped timelines; detached nodes skip.
        for node in existing:
            if self.attached(node):
                self.dispatch(node, 'onEnterFrame')
        for node in existing:
            if self.attached(node) and node.playing and node.symbol.timeline:
                self.goto(node, node.frame % len(node.symbol.timeline.frames)+1, True)
        self.enter(self.tree)

    def interval(self, *args):
        if len(args) >= 3 and isinstance(args[1], str):
            target, method, milliseconds, *params = args
            callback = lambda: self.rt.invoke(target, method, *params)
        else:
            fn, milliseconds, *params = args
            callback = lambda: self.rt.call(fn, self.rt.globals, params)
        return self.clock.set_interval(callback, number(milliseconds))
