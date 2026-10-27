"""Source-backed city rendering checks; no Flash player or Java needed."""
import base64
import hashlib
import io
import json
from pathlib import Path
import xml.etree.ElementTree as ET

from PIL import Image
import pygame
import pytest

from wd2.city_layer import CityLayer
from wd2.game import Game
from wd2.runtime import get

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets/cities'


@pytest.mark.parametrize('frame,shape', [(1, 1339), (6, 1350), (10, 1352)])
def test_registered_art_matches_original_timeline_and_embedded_bitmap(frame, shape):
    # Independent reference: unmodified extraction, not another atlas fixture.
    inventory = json.loads((ROOT / 'reverse/swf_inventory.json').read_text())
    placements = [p for p in inventory['placements'] if p['parent_id'] == 1363]
    depth = 1 if frame <= 6 else 7
    art = [p for p in placements if p['depth'] == depth and p['frame'] <= frame
           and 'character_id' in p][-1]
    assert art['character_id'] == shape
    # Move-only records inherit the matrix from the first placement at this depth.
    assert next(p['matrix'] for p in placements if p['depth'] == depth and 'matrix' in p) == [1, 0, 0, 1, 0, 0]
    svg = ET.parse(ROOT / f'reverse/export/shapes/{shape}.svg').getroot()
    ns = '{http://www.w3.org/2000/svg}'
    embedded = svg.find(f'.//{ns}image').attrib['{http://www.w3.org/1999/xlink}href']
    source = Image.open(io.BytesIO(base64.b64decode(embedded.split(',')[1]))).convert('RGBA')
    bounds = source.getbbox()
    source = source.crop(bounds)
    entry = json.loads((ASSETS / 'manifest.json').read_text())['symbols']['christian_buildings']['frames'][str(frame)]
    actual = Image.open(ASSETS / entry['file']).convert('RGBA')
    assert actual.size == source.size
    for background in ('black', 'white'):
        # Hidden RGB in fully transparent pixels is immaterial to rendering.
        assert Image.alpha_composite(Image.new('RGBA', actual.size, background), actual).tobytes() == Image.alpha_composite(Image.new('RGBA', source.size, background), source).tobytes()
    matrix = svg.find(f'{ns}g').attrib['transform']
    tx, ty = map(float, matrix.removeprefix('matrix(').removesuffix(')').split(',')[-2:])
    assert entry['offset'] == [bounds[0] - tx, bounds[1] - ty]


def test_all_five_themes_have_complete_living_and_ruin_art():
    manifest = json.loads((ASSETS / 'manifest.json').read_text())
    assert manifest['swf_sha256'] == hashlib.sha256((ROOT / 'WorldDomination2.swf').read_bytes()).hexdigest()
    assert len(manifest['symbols']) == 5
    assert manifest['scale'] == .8  # View.spawnCity's 80%, not the old 52%.
    for symbol in manifest['symbols'].values():
        assert set(map(int, symbol['frames'])) == {*range(1, 7), *range(10, 16)}
        for entry in symbol['frames'].values():
            path = ASSETS / entry['file']
            assert hashlib.sha256(path.read_bytes()).hexdigest() == entry['sha256']
            assert Image.open(path).size == (entry['crop'][2] - entry['crop'][0], entry['crop'][3] - entry['crop'][1])


def test_model_drives_theme_depth_and_ruin_rendering_without_draw_side_effects():
    g = Game(0, 1)
    layer = CityLayer(pygame)
    assert [get(p, 'buildingSet_id') for p in g.players] == [
        'christian_buildings', 'muslim_buildings', 'budhist_buildings',
        'communist_buildings', 'jewish_buildings']
    ordered = layer.ordered_cities(g)
    depths = [get(c, 'image_depth') for _, _, c in ordered]
    assert depths == sorted(depths) and len(set(depths)) == 25
    # Establish a source size-1 city, then destroy it through the recovered battle
    # callback and advance path (rather than telling the renderer to draw ruins).
    city = get(g.players[1], 'cityArr')[0]
    city.set('population', 1); city.set('prevPopulation', 1)
    get(city, 'image').set('_currentframe', get(city, 'size_and_frame'))
    g.model.set('doTurn', lambda: g.model.set('turn', get(g.model, 'turn') + 1))
    g.queue('attack', weapon='soldier1', target=1, city=0); g.queue('resources'); g.advance()
    assert get(city, 'deathFrame') == 10
    assert get(get(city, 'image'), '_currentframe') == 10
    before = g.snapshot()
    state = [(dict(c.props), dict(get(c, 'image').props)) for _, _, c in ordered]
    rng_state = g.rt.rng.getstate()
    surface = pygame.Surface((1160, 820), pygame.SRCALPHA)
    for _ in range(2):
        surface.fill((0, 0, 0, 0))
        for _, _, c in ordered:
            layer.draw(surface, c, (20, 120))
    assert pygame.mask.from_surface(surface).count() > 0
    rect = layer.draw(surface, city, (20, 120))
    art, offset = layer.frames[get(city, 'citySet'), 10]
    assert rect.topleft == (round(20 + get(city, 'xPos') + offset[0] * .8), round(120 + get(city, 'yPos') + offset[1] * .8))
    assert rect.size == art.get_size()
    assert g.snapshot() == before and g.rt.rng.getstate() == rng_state
    assert [(dict(c.props), dict(get(c, 'image').props)) for _, _, c in ordered] == state
