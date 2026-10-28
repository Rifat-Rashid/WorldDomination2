"""Deterministic, partial SWF tree renderer using existing JPEXS leaf SVGs.

No runtime/model objects are imported here. SVG leaves are placed independently
through the binary timeline tree; no pre-rendered root-frame image is used.
"""
import argparse
import base64
import copy
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

from .display_list import ColorTransform
from .swf_scene import ROOT, SWFDocument
from .resources import asset_directory, asset_path, read_asset

SVG = 'http://www.w3.org/2000/svg'
XLINK = 'http://www.w3.org/1999/xlink'
ET.register_namespace('', SVG)
ET.register_namespace('xlink', XLINK)


def element(name, attrs=None):
    return ET.Element(f'{{{SVG}}}{name}', attrs or {})


class SVGAssets:
    """Normalize export registration back to the original local coordinate origin."""
    def __init__(self, root=ROOT):
        self.root = root
        self.bounds_cache = {}
        self.city_directory = root / 'assets/cities'
        manifest = self.city_directory / 'manifest.json'
        self.cities = {s['character_id']: s for s in json.loads(manifest.read_text())['symbols'].values()} if manifest.exists() else {}

    def city_frame(self, node):
        """Reuse the completed atlas; a placed city supplies its own 80% matrix.

        No additional city sizing, theme selection, or gameplay reads occur here.
        The original root frame 10 does not dynamically spawn gameplay cities.
        """
        if node.character_id not in self.cities:
            return None
        entry = self.cities[node.character_id]['frames'].get(str(node.frame))
        if entry is None:
            raise NotImplementedError(f'city transition frame {node.frame} is not in the completed atlas')
        data = (self.city_directory / entry['file']).read_bytes()
        return element('image', {'x': str(entry['offset'][0]), 'y': str(entry['offset'][1]),
            'width': str(entry['crop'][2]-entry['crop'][0]),
            'height': str(entry['crop'][3]-entry['crop'][1]),
            f'{{{XLINK}}}href': 'data:image/png;base64,'+base64.b64encode(data).decode('ascii')})

    def load(self, symbol):
        if symbol.kind in (2, 22, 32, 83):
            path = asset_directory('shapes') / f'{symbol.character_id}.svg'
        elif symbol.kind in (11, 33, 37):
            path = asset_directory('texts') / f'{symbol.character_id}.svg'
        else:
            raise NotImplementedError(f'leaf tag {symbol.kind}')
        path = asset_path(path)
        if not path.exists():
            raise NotImplementedError(f'missing SVG {path.relative_to(self.root)}')
        svg = ET.fromstring(read_asset(path))
        group = svg.find(f'{{{SVG}}}g')
        if group is None:
            raise ValueError(f'No export registration group: {path}')
        match = re.fullmatch(r'matrix\(([^)]+)\)', group.get('transform', ''))
        matrix = tuple(float(v) for v in match[1].split(',')) if match else ()
        if len(matrix) != 6 or matrix[:4] != (1, 0, 0, 1):
            raise ValueError(f'Unexpected export registration: {path}')
        self.bounds_cache[symbol.character_id] = (-matrix[4], -matrix[5],
            float(svg.get('width').removesuffix('px')), float(svg.get('height').removesuffix('px')))
        # Only the outer bounding-box translation belongs to the exporter.
        # Inner transforms (e.g. text glyph matrices) remain untouched.
        group.attrib.pop('transform')
        container = element('g', {'id': f'asset_{symbol.character_id}'})
        for child in svg:
            container.append(copy.deepcopy(child))
        ids = {e.attrib['id']: f'a{symbol.character_id}_{e.attrib["id"]}'
               for e in container.iter() if 'id' in e.attrib and e is not container}
        for e in container.iter():
            for key, value in list(e.attrib.items()):
                if key == 'id' and value in ids:
                    e.set(key, ids[value])
                else:
                    for old, new in ids.items():
                        value = value.replace(f'url(#{old})', f'url(#{new})')
                        if value == f'#{old}':
                            value = f'#{new}'
                    e.set(key, value)
        return container

    def bounds(self, symbol):
        if symbol.character_id not in self.bounds_cache:
            self.load(symbol)
        return self.bounds_cache[symbol.character_id]


class SceneRenderer:
    def __init__(self, assets=None, flash_masks=False):
        self.assets = assets or SVGAssets()
        self.flash_masks = flash_masks

    def city_overlays(self, node):
        return ()

    def svg(self, root, size=(800, 600), background=(0, 0, 0)):
        self._stencil = getattr(self, '_force_stencil', False)
        self.report = {'mode': 'uninitialized_timeline_state', 'unsupported': [],
                       'unexecuted_scripts': [], 'rendered_leaf_instances': 0,
                       'unique_leaf_assets': 0, 'masks': 0}
        self._issues = set()
        self._loaded = set()
        self._serial = 0
        svg = element('svg', {'width': str(size[0]), 'height': str(size[1]),
                              'viewBox': f'0 0 {size[0]} {size[1]}'})
        self.defs = ET.SubElement(svg, f'{{{SVG}}}defs')
        if background is not None:
            svg.append(element('rect', {'width': '100%', 'height': '100%',
                                       'fill': '#%02x%02x%02x' % tuple(background)}))
        svg.append(self._node(root, '_root'))
        self.report['unique_leaf_assets'] = len(self._loaded)
        return ET.tostring(svg, encoding='unicode')

    def mask_svg(self, root, size=(800, 600), background=None):
        self._force_stencil = self.flash_masks
        try:
            return self.svg(root, size, background)
        finally:
            self._force_stencil = False

    def leaf_asset(self, node):
        suffix = '_stencil' if self._stencil else ''
        asset_id = (self.assets.node_asset_id(node) if hasattr(self.assets, 'node_asset_id') else f'asset_{node.character_id}')+suffix
        key = asset_id
        if key not in self._loaded:
            asset = copy.deepcopy(self.assets.load_node(node) if hasattr(self.assets, 'load_node') else self.assets.load(node.symbol))
            if self._stencil:
                ids = {e.get('id'): e.get('id')+suffix for e in asset.iter() if e.get('id')}
                for e in asset.iter():
                    for attribute, value in list(e.attrib.items()):
                        if attribute == 'id':
                            e.set(attribute, ids[value])
                        else:
                            for old, new in ids.items():
                                value = value.replace(f'url(#{old})', f'url(#{new})')
                                if value == '#'+old:
                                    value = '#'+new
                            e.set(attribute, value)
                    if e.get('fill') != 'none':
                        e.set('fill', '#ffffff')
                    e.set('fill-opacity', '1'); e.set('opacity', '1')
                    e.set('stroke', 'none')
            self.defs.append(asset)
            self._loaded.add(key)
        return asset_id

    def _issue(self, node, path, feature):
        key = (node.character_id, feature)
        if key not in self._issues:
            self._issues.add(key)
            self.report['unsupported'].append({'character_id': node.character_id,
                'path': path, 'feature': feature})

    def color_group(self, node, group):
        if node.color == ColorTransform() or self._stencil:
            return group
        self._serial += 1
        fid = f'color_{self._serial}'
        filt = element('filter', {'id': fid, 'color-interpolation-filters': 'sRGB'})
        transfer = element('feComponentTransfer')
        for i, channel in enumerate('RGBA'):
            transfer.append(element('feFunc'+channel, {'type': 'linear',
                'slope': str(node.color.mult[i]), 'intercept': str(node.color.add[i]/255)}))
        filt.append(transfer)
        self.defs.append(filt)
        colored = element('g', {'filter': f'url(#{fid})'})
        group.append(colored)
        return colored

    def _node(self, node, path):
        group = element('g')
        if not node.visible:
            return group
        if not node.matrix.is_finite():
            self._issue(node, path, 'nonfinite_transform_not_rendered')
            return group
        group.set('transform', node.matrix.svg())
        for key in node.extras:
            self._issue(node, path, key)
        if node.filters:
            self._issue(node, path, 'bitmap_filters_not_rendered')
        if node.blend_mode not in (0, 1):
            self._issue(node, path, f'blend_mode_{node.blend_mode}_not_rendered')
        if node.symbol.timeline and node.symbol.timeline.actions.get(node.frame):
            self.report['unexecuted_scripts'].append({'path': path, 'character_id': node.character_id,
                'frame': node.frame, 'offsets': node.symbol.timeline.actions.get(node.frame, [])})
        colored = self.color_group(node,group)
        for start, end, style in getattr(node, 'graphics', ()):
            width, color, alpha = style
            colored.append(element('path', {'d': f'M {start[0]} {start[1]} L {end[0]} {end[1]}',
                'fill': 'none', 'stroke': f'#{color:06x}', 'stroke-width': str(width),
                'stroke-opacity': str(alpha), 'stroke-linecap': 'round', 'stroke-linejoin': 'round'}))
        try:
            city_art = self.assets.city_frame(node) if hasattr(self.assets, 'city_frame') else None
        except NotImplementedError as error:
            self._issue(node, path, str(error))
            return group
        if city_art is not None:
            colored.append(city_art)
            self.report['rendered_leaf_instances'] += 1
            for child in self.city_overlays(node):
                colored.append(self._node(child, path+'/'+(child.name or f'#{child.depth}')))
        elif node.symbol.timeline:
            masks = []
            for child in node.ordered():
                child_path = path + '/' + (child.name or f'#{child.depth}')
                stencil = self._stencil
                if self.flash_masks and child.clip_depth > child.depth:
                    self._stencil = True
                try:
                    content = self._node(child, child_path)
                finally:
                    self._stencil = stencil
                masks = [(end, mid) for end, mid in masks if end >= child.depth]
                if child.clip_depth > child.depth:
                    self._serial += 1
                    mid = f'mask_{self._serial}'
                    mask = element('mask', {'id': mid, 'maskUnits': 'userSpaceOnUse',
                        'x': '-10000', 'y': '-10000', 'width': '20000', 'height': '20000',
                        'style': 'mask-type:alpha'})
                    mask.append(content)
                    self.defs.append(mask)
                    masks.append((child.clip_depth, mid))
                    self.report['masks'] += 1
                else:
                    for _, mid in masks:
                        wrapper = element('g', {'mask': f'url(#{mid})'})
                        wrapper.append(content)
                        content = wrapper
                    colored.append(content)
        else:
            try:
                asset_id = self.leaf_asset(node)
                colored.append(element('use', {f'{{{XLINK}}}href': '#'+asset_id}))
                self.report['rendered_leaf_instances'] += 1
            except NotImplementedError as error:
                self._issue(node, path, str(error))
        return group

    def png(self, root, size=(800, 600), background=(0, 0, 0)):
        import resvg_py
        return resvg_py.svg_to_bytes(svg_string=self.svg(root, size, background), skip_system_fonts=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--swf', type=Path, default=ROOT / 'WorldDomination2.swf')
    parser.add_argument('--frame', type=int, default=10)
    parser.add_argument('--output', type=Path, default=ROOT / 'validation/root_frame_10')
    args = parser.parse_args()
    document = SWFDocument(args.swf)
    root = document.root(args.frame)
    renderer = SceneRenderer()
    bounds = document.bounds
    size = (round(bounds[1]-bounds[0]), round(bounds[3]-bounds[2]))
    svg = renderer.svg(root, size, document.background)
    import resvg_py
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.with_suffix('.svg').write_text(svg, encoding='utf-8')
    args.output.with_suffix('.png').write_bytes(resvg_py.svg_to_bytes(svg_string=svg, skip_system_fonts=True))
    report = {'source_sha256': document.sha256, 'stage_bounds_pixels': bounds,
              'fps': document.fps, 'root_frame': args.frame, 'scene': root.dump(),
              'rendering': renderer.report}
    args.output.with_suffix('.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps({k: v for k, v in renderer.report.items() if k not in ('unexecuted_scripts', 'unsupported')}))
    print(f'Unsupported features: {len(renderer.report["unsupported"])}; see {args.output.with_suffix(".json")}')


if __name__ == '__main__':
    main()
