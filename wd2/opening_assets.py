"""Deterministic leaf artwork for the original logo morphs and decoded video."""
import base64
from collections import OrderedDict
import copy
import io
import json
import re
import xml.etree.ElementTree as ET

from PIL import Image

from .resources import RUNTIME, read_asset
from .scene_renderer import SVGAssets, SVG, XLINK, element


NUMBER = re.compile(r'[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?')


def interpolate(a, b, ratio):
    if a.startswith('#') and b.startswith('#'):
        values = [round(int(a[i:i+2],16)*(1-ratio)+int(b[i:i+2],16)*ratio) for i in (1,3,5)]
        return '#%02x%02x%02x' % tuple(values)
    av, bv = list(NUMBER.finditer(a)), list(NUMBER.finditer(b))
    if len(av) != len(bv) or re.findall('[A-DF-Za-df-z]',a) != re.findall('[A-DF-Za-df-z]',b):
        raise NotImplementedError('Incompatible authored morph endpoints')
    replacements = iter(str(float(x[0])*(1-ratio)+float(y[0])*ratio) for x,y in zip(av,bv))
    return NUMBER.sub(lambda _:next(replacements),a)


class OpeningAssets(SVGAssets):
    def __init__(self):
        super().__init__()
        self.cache, self.dynamic_cache = {}, OrderedDict()
        self.video = None
        path = RUNTIME/'opening/manifest.json'
        self.opening = json.loads(path.read_text()) if path.exists() else None

    def supports(self, kind):
        return bool(self.opening) and kind in (46,60)

    def node_asset_id(self, node):
        state = node.ratio if node.symbol.kind == 46 else node.parent.frame if node.symbol.kind == 60 else None
        return f'asset_{node.character_id}'+('' if state is None else f'_{state}')

    def load(self, symbol):
        if symbol.character_id not in self.cache:
            self.cache[symbol.character_id] = super().load(symbol)
        return self.cache[symbol.character_id]

    def load_node(self, node):
        if node.symbol.kind not in (46,60):
            return self.load(node.symbol)
        key = self.node_asset_id(node)
        if key in self.dynamic_cache:
            self.dynamic_cache.move_to_end(key)
            return self.dynamic_cache[key]
        if node.symbol.kind == 46:
            source = ET.fromstring(read_asset(RUNTIME/f'morphs/{node.character_id}.svg'))
            group = source.find(f'{{{SVG}}}g')
            matrix = [float(x) for x in group.attrib.pop('transform')[7:-1].split(',')]
            self.bounds_cache[node.character_id] = (-matrix[4],-matrix[5],float(source.get('width')[:-2]),float(source.get('height')[:-2]))
            asset = element('g', {'id':key})
            for child in source:
                asset.append(copy.deepcopy(child))
            for parent in asset.iter():
                for animation in list(parent):
                    if animation.tag == f'{{{SVG}}}animate':
                        a,b = animation.get('values').split(';')
                        parent.set(animation.get('attributeName'), interpolate(a,b,node.ratio/65535))
                        parent.remove(animation)
        else:
            data = io.BytesIO(); self.video_frame(node).save(data, format='PNG')
            asset = element('g', {'id':key})
            asset.append(element('image', {'width':'320', 'height':'240',
                f'{{{XLINK}}}href':'data:image/png;base64,'+base64.b64encode(data.getvalue()).decode('ascii')}))
        self.dynamic_cache[key] = asset
        while len(self.dynamic_cache) > 32:
            self.dynamic_cache.popitem(last=False)
        return asset

    def video_frame(self, node):
        if self.video is None:
            self.video = Image.open(RUNTIME/'opening/5911.webp')
        self.video.seek(max(0,min(self.video.n_frames-1,node.parent.frame-1)))
        return self.video.convert('RGBA')

    def bounds(self, symbol):
        if symbol.kind == 60:
            return 0,0,320,240
        if symbol.kind == 46 and symbol.character_id not in self.bounds_cache:
            from .display_list import MovieClip
            self.load_node(MovieClip({symbol.character_id:symbol},symbol.character_id))
        return super().bounds(symbol)
