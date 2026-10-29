"""Menu-specific dynamic text using original EditText layout and extracted fonts."""
import base64
import io
import math
from functools import lru_cache
from collections import OrderedDict

from PIL import Image, ImageDraw, ImageFont

from .swf_bits import Bits, records
from .resources import asset_directory, read_asset
from .runtime import get, U
from .scene_renderer import SceneRenderer, element, XLINK
from .swf_scene import Reader


@lru_cache(maxsize=32)
def text_font(path, size):
    return ImageFont.truetype(io.BytesIO(read_asset(path)), size)


def font_families(document):
    """Read original DefineFont2/3 names, including glyphless device fonts."""
    if hasattr(document, 'font_families'):
        return document.font_families
    raw = document.raw
    bits = Bits(raw, 8)
    bits.read(4*bits.read(5))
    families = {}
    for _, kind, _, payload, size in records(raw, bits.align()+4, len(raw)):
        if kind not in (48, 75):
            continue
        r = Reader(raw[payload:payload+size])
        sid = r.u16()
        r.take(2)  # flags and language
        families[sid] = r.take(r.u8()).decode('utf-8', 'replace').rstrip('\0')
    return families


def edit_fields(document):
    if hasattr(document, 'text_fields'):
        return document.text_fields
    raw = document.raw
    bits = Bits(raw, 8)
    bits.read(4*bits.read(5))
    result = {}
    for _, kind, _, payload, size in records(raw, bits.align()+4, len(raw)):
        if kind != 37:
            continue
        r = Reader(raw[payload:payload+size])
        sid = r.u16()
        b = Bits(r.data, r.pos)
        n = b.read(5)
        bounds = tuple(b.read(n, True)/20 for _ in range(4))
        r.pos = b.align()
        f1, f2 = r.u8(), r.u8()
        font = r.u16() if f1 & 1 else None
        if f2 & 128:
            r.text()
        height = r.u16()/20 if f1 & 1 else 12
        color = tuple(r.take(4)) if f1 & 4 else (255, 255, 255, 255)
        max_length = r.u16() if f1 & 2 else 0
        align = 0
        if f2 & 32:
            align = r.u8()
            r.take(8)  # margins, indent, leading; selected fields have zero margins.
        variable = r.text()
        initial = r.text() if f1 & 128 else ''
        result[sid] = {'bounds': bounds, 'font': font, 'size': height, 'color': color, 'align': align,
                       'word_wrap': bool(f1 & 64), 'multiline': bool(f1 & 32),
                       'editable': not bool(f1 & 8), 'password': bool(f1 & 16),
                       'max_length': max_length, 'variable': variable, 'initial_text': initial}
    return result


class MenuRenderer(SceneRenderer):
    def __init__(self, document, assets, host=None):
        super().__init__(assets, flash_masks=True)
        self.host = host
        self.fields = edit_fields(document)
        self.font_families = font_families(document)
        self.font_paths = {int(p.name.split('_', 1)[0]): p
                           for p in sorted(asset_directory('fonts').glob('*.ttf*'))}
        self.text_cache = OrderedDict()
        self.text_cache_bytes = 0

    def cache_text(self, key, value):
        size = len(value[2]) + len(key[1].encode('utf-8'))
        old = self.text_cache.pop(key,None)
        if old is not None:
            self.text_cache_bytes -= len(old[2]) + len(key[1].encode('utf-8'))
        while self.text_cache and (len(self.text_cache)>=256 or self.text_cache_bytes+size>8*1024**2):
            old_key, old = self.text_cache.popitem(last=False)
            self.text_cache_bytes -= len(old[2]) + len(old_key[1].encode('utf-8'))
        if size<=8*1024**2:
            self.text_cache[key]=value
            self.text_cache_bytes+=size

    def city_overlays(self, node):
        # Registered atlas artwork stays intact. Runtime-only effects and the
        # authored initially-empty overlays still need their original timelines.
        return [c for c in node.ordered() if c.depth > 28 or
                (c.name in ('mc', 'bulletHoles', 'propagandaBeams', 'propagandaBeams2', 'citizensMovie') and c.frame > 1)]

    def text_metrics(self, node):
        field = self.fields[node.character_id]
        props = getattr(node, 'as2_text', {})
        fmt = props.get('_textFormat', U)
        size = get(fmt, 'size')
        size = field['size'] if size is U else size
        font = text_font(str(self.font_path(field['font'], get(fmt, 'font'))), round(size*4))
        text = str(props.get('text', field.get('initial_text', '')))
        width = math.ceil(field['bounds'][1]-field['bounds'][0])-4
        lines = []
        for paragraph in text.split('\n'):
            if not field.get('word_wrap'):
                lines.append(paragraph); continue
            line = ''
            for word in paragraph.split():
                candidate = (line+' '+word).strip()
                if line and font.getlength(candidate) > width*4:
                    lines.append(line); line = word
                else:
                    line = candidate
            lines.append(line)
        height = math.ceil(field['bounds'][3]-field['bounds'][2])
        visible_lines = max(1, math.floor((height-4)/(size+2)))
        return lines, visible_lines

    def font_path(self, font_id, family=U):
        if family is U and font_id in self.font_paths:
            return self.font_paths[font_id]
        requested = self.font_families.get(font_id) if family is U else family
        for sid in sorted(self.font_paths):
            if self.font_families.get(sid) == requested:
                return self.font_paths[sid]
        raise ValueError(f'No extracted font for SWF font {font_id}, family {requested!r}')

    def svg(self, root, size=(800, 600), background=(0, 0, 0)):
        markup = super().svg(root, size, background)
        self.report['mode'] = 'scoped_initialized_setup_menu'
        if self.host:
            executed = set()
            def visit(node, path):
                if node.character_id in self.host.script_symbols and self.host.entered.get(node) == node.frame:
                    executed.add(path)
                for child in node.ordered():
                    visit(child, path+'/'+(child.name or f'#{child.depth}'))
            visit(root, '_root')
            old = self.report['unexecuted_scripts']
            self.report['executed_visible_frame_instances'] = sum(e['path'] in executed for e in old)
            self.report['unexecuted_scripts'] = [e for e in old if e['path'] not in executed]
        return markup

    def _node(self, node, path):
        props = getattr(node, 'as2_text', {})
        if node.symbol.kind != 37 or 'text' not in props or not node.matrix.is_finite():
            return super()._node(node, path)
        group = element('g', {'transform': node.matrix.svg()})
        if not node.visible:
            return group
        field = self.fields[node.character_id]
        fmt = props.get('_textFormat', U)
        font_size = get(fmt, 'size')
        font_size = field['size'] if font_size is U else font_size
        color = props.get('textColor', get(fmt, 'color'))
        color = field['color'] if color is U else ((int(color)>>16)&255, (int(color)>>8)&255, int(color)&255, 255)
        text = str(props['text'])
        if not text and not props.get('_focused'):
            return group
        # A device-font declaration can have no exported glyph file. Resolve its
        # original family to an embedded/exported counterpart, not a system font.
        font_path = self.font_path(field['font'], get(fmt, 'font'))
        scroll = max(1, int(props.get('scroll', 1)))
        focused = props.get('_focused', False) and self.host and (self.host.clock.ticks//12) % 2 == 0
        key = (node.character_id, text, font_size, color, font_path.name, scroll, bool(focused), props.get('_caret', 0))
        cached = self.text_cache.get(key)
        if cached is None:
            x0, x1, y0, y1 = field['bounds']
            scale = 4
            width, height = math.ceil(x1-x0), math.ceil(y1-y0)
            image = Image.new('RGBA', (width*scale, height*scale))
            font = text_font(str(font_path), round(font_size*scale))
            draw = ImageDraw.Draw(image)
            if field['align'] == 2:
                xy, anchor = (width*scale/2, 4*scale), 'mt'
            else:
                xy, anchor = (2*scale, 4*scale), 'lt'
            lines, count = self.text_metrics(node)
            text = '\n'.join(lines[scroll-1:scroll-1+count])
            if '\n' in text:
                # Text fields in this slice are top-aligned; render each source line.
                for i, line in enumerate(text.split('\n')):
                    draw.text((xy[0], xy[1]+i*(font_size+2)*scale), line, font=font, fill=color, anchor=anchor)
            else:
                draw.text(xy, text, font=font, fill=color, anchor=anchor)
            if focused:
                prefix = str(props['text'])[:int(props.get('_caret', len(str(props['text']))))].split('\n')[-1]
                cx = 2*scale + font.getlength(prefix)
                draw.line((cx, 3*scale, cx, (font_size+5)*scale), fill=color, width=scale)
            stream = io.BytesIO()
            image.save(stream, format='PNG')
            cached = (width, height, 'data:image/png;base64,'+base64.b64encode(stream.getvalue()).decode('ascii'))
            self.cache_text(key,cached)
        else:
            self.text_cache.move_to_end(key)
        width, height, href = cached
        self.color_group(node,group).append(element('image', {'x': str(field['bounds'][0]), 'y': str(field['bounds'][2]),
            'width': str(width), 'height': str(height), f'{{{XLINK}}}href': href}))
        self.report['rendered_leaf_instances'] += 1
        return group

    def control_bounds(self, node):
        """Bounds of original geometry, including the existing city atlas."""
        points = []
        def visit(leaf):
            city = self.assets.cities.get(leaf.character_id)
            if city:
                frame = city['frames'].get(str(leaf.frame))
                if not frame:
                    return
                x, y = frame['offset']
                w, h = frame['crop'][2]-frame['crop'][0], frame['crop'][3]-frame['crop'][1]
            elif leaf.symbol.kind in (2, 22, 32, 83):
                x, y, w, h = self.assets.bounds(leaf.symbol)
            else:
                for child in leaf.ordered():
                    visit(child)
                return
            points.extend(leaf.world_matrix.point(px, py) for px, py in ((x,y),(x+w,y),(x,y+h),(x+w,y+h)))
        visit(node)
        if not points:
            return None
        return min(p[0] for p in points), min(p[1] for p in points), max(p[0] for p in points), max(p[1] for p in points)
