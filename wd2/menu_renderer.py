"""Menu-specific dynamic text using original EditText layout and extracted fonts."""
import base64
import io
import math

from PIL import Image, ImageDraw, ImageFont

from .swf_bits import Bits, records
from .resources import asset_directory
from .runtime import get, U
from .scene_renderer import SceneRenderer, element, XLINK
from .swf_scene import Reader


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
        if f1 & 2:
            r.u16()
        align = 0
        if f2 & 32:
            align = r.u8()
            r.take(8)  # margins, indent, leading; selected fields have zero margins.
        result[sid] = {'bounds': bounds, 'font': font, 'size': height, 'color': color, 'align': align,
                       'word_wrap': bool(f1 & 64), 'multiline': bool(f1 & 32)}
    return result


class MenuRenderer(SceneRenderer):
    def __init__(self, document, assets, host=None):
        super().__init__(assets)
        self.host = host
        self.fields = edit_fields(document)
        self.font_families = font_families(document)
        self.font_paths = {int(p.name.split('_', 1)[0]): p
                           for p in sorted(asset_directory('fonts').glob('*.ttf'))}
        self.text_cache = {}

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
        if node.symbol.kind != 37 or 'text' not in props:
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
        if not text:
            return group
        # A device-font declaration can have no exported glyph file. Resolve its
        # original family to an embedded/exported counterpart, not a system font.
        font_path = self.font_path(field['font'], get(fmt, 'font'))
        key = (node.character_id, text, font_size, color, font_path.name)
        if key not in self.text_cache:
            x0, x1, y0, y1 = field['bounds']
            scale = 4
            width, height = math.ceil(x1-x0), math.ceil(y1-y0)
            image = Image.new('RGBA', (width*scale, height*scale))
            font = ImageFont.truetype(str(font_path), round(font_size*scale))
            draw = ImageDraw.Draw(image)
            if field['align'] == 2:
                xy, anchor = (width*scale/2, 4*scale), 'mt'
            else:
                xy, anchor = (2*scale, 4*scale), 'lt'
            if field.get('word_wrap'):
                lines = []
                for paragraph in text.split('\n'):
                    line = ''
                    for word in paragraph.split():
                        candidate = (line+' '+word).strip()
                        if line and draw.textlength(candidate, font=font) > (width-4)*scale:
                            lines.append(line)
                            line = word
                        else:
                            line = candidate
                    lines.append(line)
                text = '\n'.join(lines)
            if '\n' in text:
                # Text fields in this slice are top-aligned; render each source line.
                for i, line in enumerate(text.split('\n')):
                    draw.text((xy[0], xy[1]+i*(font_size+2)*scale), line, font=font, fill=color, anchor=anchor)
            else:
                draw.text(xy, text, font=font, fill=color, anchor=anchor)
            stream = io.BytesIO()
            image.save(stream, format='PNG')
            self.text_cache[key] = (width, height, 'data:image/png;base64,'+base64.b64encode(stream.getvalue()).decode('ascii'))
        width, height, href = self.text_cache[key]
        group.append(element('image', {'x': str(field['bounds'][0]), 'y': str(field['bounds'][2]),
            'width': str(width), 'height': str(height), f'{{{XLINK}}}href': href}))
        self.report['rendered_leaf_instances'] += 1
        return group

    def control_bounds(self, node):
        """Bounds of original leaf geometry, for the rectangular setup controls."""
        points = []
        for leaf in node.walk():
            if leaf.symbol.timeline:
                continue
            if leaf.symbol.kind not in (2, 22, 32, 83):
                continue
            x, y, w, h = self.assets.bounds(leaf.symbol)
            points.extend(leaf.world_matrix.point(px, py) for px, py in ((x,y),(x+w,y),(x,y+h),(x+w,y+h)))
        if not points:
            return None
        return min(p[0] for p in points), min(p[1] for p in points), max(p[0] for p in points), max(p[1] for p in points)
