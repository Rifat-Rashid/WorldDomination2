"""Cached native surfaces composed from the existing SVG renderer.

Rasterize authored subtrees at their exact composed transforms. Keep group color
effects in SVG and apply alpha masks to already composited children. Depth-ordered
Pygame blits then reuse the cropped surfaces. This is a
presentation cache over the existing tree, not another timeline implementation.
"""
from collections import OrderedDict
from copy import copy
import io
import math
import xml.etree.ElementTree as ET

from .display_list import ColorTransform, Matrix
from .runtime import U, get
from .scene_renderer import element


class SurfaceLRU:
    def __init__(self, entries, byte_limit):
        self.limit, self.byte_limit = entries, byte_limit
        self.items = OrderedDict()
        self.bytes = self.hits = self.misses = self.evictions = 0

    def get(self, key):
        if key not in self.items:
            self.misses += 1
            return None
        self.hits += 1
        value, size = self.items.pop(key)
        self.items[key] = value, size
        return value

    def put(self, key, value):
        surface = value[0]
        size = surface.get_pitch()*surface.get_height()
        if size > self.byte_limit or self.limit < 1:
            return
        while self.items and (len(self.items) >= self.limit or self.bytes+size > self.byte_limit):
            _, (_, old_size) = self.items.popitem(last=False)
            self.bytes -= old_size
            self.evictions += 1
        self.items[key] = value, size
        self.bytes += size


def freeze(value):
    if isinstance(value, dict):
        return tuple((k, freeze(v)) for k, v in sorted(value.items()))
    if isinstance(value, (list, tuple)):
        return tuple(map(freeze, value))
    return value


class SurfaceRenderer:
    def __init__(self, renderer, pygame, layer_entries=512, layer_bytes=48*1024**2,
                 frame_entries=8, frame_bytes=16*1024**2):
        self.renderer, self.pg = renderer, pygame
        self.layers = SurfaceLRU(layer_entries, layer_bytes)
        self.frames = SurfaceLRU(frame_entries, frame_bytes)
        self.rasterizations = self.fallback_frames = 0
        self.city_ids = set(getattr(renderer.assets, 'cities', {}))
        self._signatures = {}
        opening = getattr(renderer.assets, 'opening', None)
        self.video_parents = {opening['video']['parent_id']} if opening else set()
        self.decoded_frames = 0
        self.invalid_transforms = set()

    def valid_transform(self, node, matrix):
        if matrix.is_finite():
            return True
        self.invalid_transforms.add((node.character_id, node.name, node.depth))
        return False

    def signature(self, node):
        if id(node) in self._signatures:
            return self._signatures[id(node)]
        if not node.visible:
            return ('hidden',)
        if not self.valid_transform(node, node.matrix):
            return ('invalid_transform', node.character_id, node.clip_depth)
        text = getattr(node, 'as2_text', {})
        fmt = text.get('_textFormat', U)
        text_key = ('text' in text, str(text.get('text', '')), text.get('textColor', U),
                    *(get(fmt, p) for p in ('font', 'size', 'color')),
                    text.get('scroll', 1), text.get('_caret', 0),
                    bool(text.get('_focused')) and self.renderer.host.clock.ticks//12 % 2 == 0)
        # A timeline frame matters through its current children. Atlas cities
        # override that tree, so their selected registered frame is explicit.
        result = (node.character_id, node.matrix, node.color, node.clip_depth,
                node.ratio, freeze(node.filters), node.blend_mode, freeze(node.extras), freeze(getattr(node, 'graphics', ())),
                node.frame if node.character_id in self.city_ids else None, text_key,
                node.parent.frame if node.symbol.kind == 60 and node.parent else None,
                tuple((c.depth, self.signature(c)) for c in node.ordered())
                if node.character_id not in self.city_ids else tuple((c.depth, self.signature(c)) for c in self.renderer.city_overlays(node)))
        self._signatures[id(node)] = result
        return result

    def unsupported(self, node):
        if not node.visible or not node.matrix.is_finite():
            return False
        if node.filters or node.extras or node.blend_mode not in (0, 1):
            return True
        if node.symbol.timeline and node.character_id not in self.city_ids:
            return any(self.unsupported(c) for c in node.ordered())
        return (node.symbol.kind not in (2, 22, 32, 83, 11, 33, 37)
                and not (hasattr(self.renderer.assets, 'supports') and self.renderer.assets.supports(node.symbol.kind))
                and node.character_id not in self.city_ids)

    @staticmethod
    def partial(node, children):
        view = copy(node)
        view.children = {c.depth: c for c in children}
        return view

    def empty(self):
        return self.pg.Surface((0, 0), self.pg.SRCALPHA, 32), (0, 0)

    def bounds(self, node, ancestors, size):
        """Conservative stage-pixel bounds; unknown geometry uses the full SVG."""
        points = []
        def visit(n, parent_matrix):
            if not n.visible:
                return True
            matrix = parent_matrix @ n.matrix
            if not self.valid_transform(n, matrix):
                return True
            if n.color.add[3]:
                return False  # Alpha addition can reveal a filter's padding.
            for start, end, style in getattr(n, 'graphics', ()):
                padding = style[0]/2
                for x, y in (start, end):
                    points.extend(matrix.point(x+dx, y+dy) for dx, dy in ((-padding,-padding),(padding,padding)))
            if n.character_id in self.city_ids:
                state = self.renderer.assets.cities[n.character_id]['frames'].get(str(n.frame))
                if state is None:
                    return False
                x, y = state['offset']
                w, h = state['crop'][2]-state['crop'][0], state['crop'][3]-state['crop'][1]
                if not all(visit(c, matrix) for c in self.renderer.city_overlays(n)):
                    return False
            elif n.symbol.timeline:
                return all(visit(c, matrix) for c in n.ordered())
            elif n.symbol.kind == 37 and hasattr(self.renderer, 'fields') and 'text' in getattr(n, 'as2_text', {}):
                if str(n.as2_text['text']) == '' and not n.as2_text.get('_focused'):
                    return True
                x, x1, y, y1 = self.renderer.fields[n.character_id]['bounds']
                w, h = math.ceil(x1-x), math.ceil(y1-y)
            elif hasattr(self.renderer.assets, 'bounds'):
                try:
                    x, y, w, h = self.renderer.assets.bounds(n.symbol)
                except NotImplementedError:
                    return False  # Keep the original SVG diagnostic/fallback.
            else:
                return False
            points.extend(matrix.point(px, py) for px, py in ((x,y), (x+w,y), (x,y+h), (x+w,y+h)))
            return True
        parent_matrix = Matrix()
        for ancestor in ancestors:
            parent_matrix = parent_matrix @ ancestor.matrix
        if not visit(node, parent_matrix):
            return self.pg.Rect((0, 0), size)
        if not points:
            return self.pg.Rect(0, 0, 0, 0)
        x0, y0 = math.floor(min(x for x,y in points))-2, math.floor(min(y for x,y in points))-2
        x1, y1 = math.ceil(max(x for x,y in points))+2, math.ceil(max(y for x,y in points))+2
        return self.pg.Rect(x0, y0, x1-x0, y1-y0).clip(self.pg.Rect((0, 0), size))

    def raster(self, node, ancestors, size, as_mask=False):
        viewport = self.bounds(node, ancestors, size)
        if not viewport:
            return self.empty()
        partial = node
        for ancestor in reversed(ancestors):
            partial = self.partial(ancestor, [partial])
        self.rasterizations += 1
        # Preserve original stage coordinates while encoding only the pixels
        # this sprite can occupy, rather than an 800x600 mostly-empty PNG.
        source = self.renderer.mask_svg if as_mask else self.renderer.svg
        svg = ET.fromstring(source(partial, size, None))
        if as_mask:
            # Ask the reference SVG path for the effective mask coverage,
            # including its antialiasing and mask-type interpretation.
            defs, content = list(svg)
            svg.remove(content)
            mask = element('mask', {'id': 'surface_coverage', 'maskUnits': 'userSpaceOnUse',
                'x': '-10000', 'y': '-10000', 'width': '20000', 'height': '20000',
                'style': 'mask-type:alpha'})
            mask.append(content); defs.append(mask)
            svg.append(element('rect', {'width': str(size[0]), 'height': str(size[1]),
                'fill': '#ffffff', 'mask': 'url(#surface_coverage)'}))
        svg.set('width', str(viewport.width)); svg.set('height', str(viewport.height))
        svg.set('viewBox', f'{viewport.x} {viewport.y} {viewport.width} {viewport.height}')
        import resvg_py
        png = resvg_py.svg_to_bytes(svg_string=ET.tostring(svg, encoding='unicode'), skip_system_fonts=True)
        surface = self.pg.image.load(io.BytesIO(png)).convert_alpha().premul_alpha()
        bounds = surface.get_bounding_rect(min_alpha=1)
        return surface.subsurface(bounds).copy(), (viewport.x+bounds.x, viewport.y+bounds.y)

    def mask(self, node, ancestors, size):
        key = ('mask', size, self.signature(node), tuple(a.matrix for a in ancestors))
        cached = self.layers.get(key)
        if cached is None:
            paint = copy(node)
            paint.clip_depth = 0  # Paint mask geometry, rather than mask an empty list.
            surface, position = self.raster(paint, ancestors, size, as_mask=True)
            # White mask coverage is now premultiplied: RGB and A both hold
            # coverage, so clipping scales premultiplied color and alpha alike.
            cached = surface, position
            self.layers.put(key, cached)
        return cached

    def translated_sprite(self, node, ancestors, size):
        """Reuse exact raster pixels when only integer stage translation changes.

        Keep fractional registration, scale/rotation, text, color and children in
        the key. Large/edge-clipped geometry stays on the existing SVG path.
        """
        matrix = Matrix()
        for parent in ancestors:
            matrix = matrix @ parent.matrix
        matrix = matrix @ node.matrix
        if not self.valid_transform(node, matrix):
            return self.empty()
        x, y = math.floor(matrix.tx), math.floor(matrix.ty)
        origin = size[0]//2, size[1]//2
        view = copy(node)
        view.matrix = Matrix(matrix.a, matrix.b, matrix.c, matrix.d,
                             origin[0]+round(matrix.tx-x, 10), origin[1]+round(matrix.ty-y, 10))
        # This temporary view shares descendants but never changes the live tree.
        self._signatures.pop(id(view), None)
        key = ('registered_sprite', size, self.signature(view))
        self._signatures.pop(id(view), None)
        cached = self.layers.get(key)
        if cached is None:
            bounds = self.bounds(view, (), size)
            if not bounds or bounds.left <= 0 or bounds.top <= 0 or bounds.right >= size[0] or bounds.bottom >= size[1]:
                return self.raster(node, ancestors, size)
            cached = self.raster(view, (), size)
            self.layers.put(key, cached)
        surface, position = cached
        return surface, (position[0]+x-origin[0], position[1]+y-origin[1])

    def video_paint(self, node, ancestors):
        matrix = Matrix()
        for parent in ancestors:
            matrix = matrix @ parent.matrix
        matrix = matrix @ node.matrix
        if not self.valid_transform(node, matrix):
            return self.empty()
        if ((matrix.a,matrix.b,matrix.c,matrix.d) != (1,0,0,1)
                or node.color != ColorTransform() or not hasattr(self.renderer.assets,'video_frame')):
            return None
        x,y = math.floor(matrix.tx),math.floor(matrix.ty)
        fx,fy = round(matrix.tx-x,10),round(matrix.ty-y,10)
        key = ('video',node.character_id,node.parent.frame,fx,fy)
        cached = self.layers.get(key)
        if cached is None:
            from PIL import Image
            source = self.renderer.assets.video_frame(node)
            image = Image.new('RGBA',(source.width+2,source.height+2))
            image.paste(source,(1,1))
            image = image.transform(image.size,Image.Transform.AFFINE,(1,0,-fx,0,1,-fy),Image.Resampling.BILINEAR)
            surface = self.pg.image.frombytes(image.tobytes(),image.size,'RGBA').convert_alpha().premul_alpha()
            cached = surface, (0,0)
            self.layers.put(key,cached)
            self.decoded_frames += 1
        return cached[0],(x-1,y-1)

    def clipped(self, paint, mask):
        surface, position = paint
        alpha, mask_position = mask
        bounds = surface.get_rect(topleft=position).clip(alpha.get_rect(topleft=mask_position))
        if not bounds:
            return self.empty()
        result = surface.subsurface(bounds.move(-position[0], -position[1])).copy()
        result.blit(alpha, (0, 0), bounds.move(-mask_position[0], -mask_position[1]),
                    special_flags=self.pg.BLEND_RGBA_MULT)
        return result, bounds.topleft

    def merge(self, paints):
        paints = [(surface, position) for surface, position in paints if surface.get_width() and surface.get_height()]
        if not paints:
            return self.empty()
        bounds = paints[0][0].get_rect(topleft=paints[0][1])
        for surface, position in paints[1:]:
            bounds.union_ip(surface.get_rect(topleft=position))
        result = self.pg.Surface(bounds.size, self.pg.SRCALPHA, 32)
        for surface, position in paints:
            result.blit(surface, (position[0]-bounds.x, position[1]-bounds.y),
                        special_flags=self.pg.BLEND_PREMULTIPLIED)
        return result, bounds.topleft

    def paint(self, node, ancestors, level, size):
        if not node.visible or not self.valid_transform(node, node.matrix):
            return self.empty()
        key = ('paint', size, self.signature(node), tuple(a.matrix for a in ancestors))
        cached = self.layers.get(key) if level else None
        if cached is not None:
            return cached
        if node.symbol.kind == 60:
            cached = self.video_paint(node,ancestors)
            if cached is not None:
                self.layers.put(key,cached)
                return cached
        if ((level >= 2 and node.character_id not in self.video_parents) or not node.symbol.timeline or node.character_id in self.city_ids
                or node.color != ColorTransform() or getattr(node, 'graphics', ())):
            # SVG retains precise affine rasterization and group color effects.
            cached = self.translated_sprite(node, ancestors, size)
        else:
            paints, masks = [], []
            for child in node.ordered():
                masks = [(end, mask) for end, mask in masks if end >= child.depth]
                if child.clip_depth > child.depth:
                    masks.append((child.clip_depth, child))
                    continue
                entry = self.paint(child, ancestors+(node,), level+1, size)
                # Clip each already-composited child once, exactly as the
                # reference SVG renderer does. Animated flags no longer force
                # the original map vectors to be rasterized again.
                for _, mask in masks:
                    entry = self.clipped(entry, self.mask(mask, ancestors+(node,), size))
                paints.append(entry)
            cached = self.merge(paints)
        if level:
            self.layers.put(key, cached)
        return cached

    def frame(self, root, size=(800, 600), background=(0, 0, 0)):
        self._signatures = {}
        self.invalid_transforms = set()
        key = (size, background, self.signature(root))
        cached = self.frames.get(key)
        if cached is not None:
            return cached[0]
        if self.unsupported(root):
            self.fallback_frames += 1
            surface = self.pg.image.load(io.BytesIO(self.renderer.png(root, size, background))).convert_alpha()
        else:
            surface = self.pg.Surface(size, self.pg.SRCALPHA, 32)
            surface.fill((*background, 255))
            sprite, position = self.paint(root, (), 0, size)
            surface.blit(sprite, position, special_flags=self.pg.BLEND_PREMULTIPLIED)
        self.frames.put(key, (surface, (0, 0)))
        return surface  # Owned by the cache; callers must only read/blit it.

    def stats(self):
        return {'rasterizations': self.rasterizations, 'fallback_frames': self.fallback_frames,
                'invalid_transforms': len(self.invalid_transforms),
                'decoded_video_frames': self.decoded_frames,
                'layer_hits': self.layers.hits, 'frame_hits': self.frames.hits,
                'layer_entries': len(self.layers.items), 'frame_entries': len(self.frames.items),
                'layer_bytes': self.layers.bytes, 'frame_bytes': self.frames.bytes,
                'evictions': self.layers.evictions+self.frames.evictions}
