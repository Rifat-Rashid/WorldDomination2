import io
import json
from pathlib import Path
import xml.parsers.expat

from PIL import Image, ImageChops, ImageStat, ImageDraw
import pytest

from wd2.display_list import Matrix, ColorTransform, MovieClip, Operation, Symbol, Timeline
from wd2.swf_scene import SWFDocument
from wd2.scene_renderer import SceneRenderer, element
from wd2.game import Game

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope='module')
def document():
    return SWFDocument()


def small_tree():
    return {0: Symbol(0, 0, timeline=Timeline()),
            1: Symbol(1, 2), 2: Symbol(2, 2)}


def test_placement_replacement_removal_and_inherited_properties():
    root = MovieClip(small_tree())
    root.apply(Operation(3, {'character_id': 1, 'name': 'first',
        'matrix': Matrix(2, 0, 0, 3, 40, 50), 'color': ColorTransform((.5, 1, 1, 1)), 'clip_depth': 8}))
    old = root.children[3]
    assert old.parent is root and old.depth == 3 and root.named('first') is old
    root.apply(Operation(3, {'ratio': 10}, move=True))
    assert root.children[3] is old and old.matrix.tx == 40
    root.apply(Operation(3, {'character_id': 2}, move=True))
    new = root.children[3]
    assert new is not old and old.parent is None
    assert new.matrix == Matrix(2, 0, 0, 3, 40, 50)
    assert new.name == 'first' and new.color.mult[0] == .5 and new.clip_depth == 8
    root.apply(Operation(3, {'character_id': 1}))
    assert root.children[3].matrix == Matrix()  # Fresh placement resets properties.
    root.apply(Operation(3, remove=True))
    assert not root.children
    with pytest.raises(ValueError, match='empty depth'):
        root.apply(Operation(3, {'ratio': 5}, move=True))


def test_parent_child_rotation_scale_composition():
    symbols = small_tree()
    symbols[1].timeline = Timeline()
    root = MovieClip(symbols)
    root.apply(Operation(2, {'character_id': 1, 'matrix': Matrix(0, 2, -3, 0, 100, 200)}))
    parent = root.children[2]
    parent.apply(Operation(7, {'character_id': 2, 'matrix': Matrix(4, 0, 0, 5, 10, 20)}))
    child = parent.children[7]
    assert child.world_matrix == Matrix(0, 8, -15, 0, 40, 220)
    assert child.world_matrix.point(1, 2) == (10, 228)


def test_frames_labels_seek_loop_and_child_lifetimes():
    symbols = small_tree()
    symbols[0].timeline = Timeline([
        [Operation(1, {'character_id': 1, 'matrix': Matrix(tx=3)})],
        [Operation(1, {'name': 'second'}, move=True)],
        [Operation(1, remove=True)]], {'start': 1, 'middle': 2})
    symbols[1].timeline = Timeline([[], [], []])
    root = MovieClip(symbols)
    child = root.children[1]
    root.advance()
    assert root.frame == 2 and child.frame == 2 and root.named('second') is child
    root.goto_and_stop('start')
    assert root.frame == 1 and child.parent is None and root.children[1].frame == 1
    root.advance()  # A stopped parent does not stop its children's timelines.
    assert root.frame == 1 and root.children[1].frame == 2
    root.goto_and_play('middle')
    root.advance()
    assert root.frame == 3 and not root.children
    root.advance()
    assert root.frame == 1 and root.children[1].frame == 1


def test_binary_counts_labels_and_real_move_inheritance(document):
    assert document.bounds == (0, 800, 0, 600) and document.fps == 24
    assert {k: document.tag_counts[k] for k in (26, 28, 39, 43, 70)} == {
        26: 8552, 28: 1100, 39: 426, 43: 382, 70: 6}
    city = MovieClip(document.symbols, 1363)
    matrix = city.children[1].matrix
    city.goto_frame(2)
    assert city.children[1].character_id == 1342 and city.children[1].matrix == matrix
    assert document.symbols[4658].linkage == 'interface_2'
    labels = document.symbols[4658].timeline.labels
    assert labels['get_full_version_top'] == 1
    labeled = next(s for s in document.symbols.values() if s.timeline and len(set(s.timeline.labels.values())) > 1)
    name, frame = next((k, v) for k, v in labeled.timeline.labels.items() if v > 1)
    clip = MovieClip(document.symbols, labeled.character_id)
    clip.goto_and_stop(name)
    assert clip.frame == frame and not clip.playing


def test_actual_placeobject3_filters_are_preserved_and_preloader_is_removed(document):
    loader = MovieClip(document.symbols, 5782)
    loader.goto_frame(10)  # Original preloader timeline's first nine frames are empty.
    assert loader.children[1].character_id == 5768
    assert [f['id'] for f in loader.children[1].filters] == [0, 1]
    assert loader.children[4].blend_mode == 13
    assert loader.named('percentloaded_bar_mc').depth == 6
    before = document.root(4)
    assert before.named('youdapreloader').character_id == 5782
    before.goto_frame(10)
    assert before.named('youdapreloader') is None and before.children[2].character_id == 5809


def test_root_frame10_against_independent_jpexs_xml(document):
    # Stream the original 265 MB XML, retaining only root placements/matrices.
    # This does not consult swf_inventory.json or any Python-generated scene dump.
    stack, placements = [], {}
    current, frame = None, 1
    def start(name, attrs):
        nonlocal current, frame
        if len(stack) == 2 and name == 'item':
            if attrs.get('type') == 'ShowFrameTag':
                frame += 1
            elif frame == 10 and attrs.get('type') == 'PlaceObject2Tag':
                current = dict(attrs)
                placements[int(attrs['depth'])] = current
        elif len(stack) == 3 and name == 'matrix' and current is not None:
            current['matrix'] = dict(attrs)
        stack.append(name)
    def end(name):
        nonlocal current
        stack.pop()
        if len(stack) == 2:
            current = None
    parser = xml.parsers.expat.ParserCreate()
    parser.StartElementHandler, parser.EndElementHandler = start, end
    with (ROOT / 'reverse/movie.xml').open('rb') as source:
        parser.ParseFile(source)
    root = document.root(10)
    assert set(root.children) == set(placements)
    for depth, name, sid, xy in [(14, 'battleMC', 5766, (3, 0)),
                                (335, 'interfaceMC', 4658, (398, 355)),
                                (1413, 'gameMenu', 5882, (-112, -29))]:
        original = placements[depth]
        node = root.children[depth]
        assert original['name'] == node.name == name
        assert int(original['characterId']) == node.character_id == sid
        assert (int(original['matrix']['translateX'])/20, int(original['matrix']['translateY'])/20) == xy
        assert node.world_matrix.point(0, 0) == xy
        assert node.parent is root and node.children
    assert root.children[1].clip_depth == int(placements[1]['clipDepth']) == 11
    assert root.children[12].clip_depth == int(placements[12]['clipDepth']) == 333


class RectAssets:
    def load(self, symbol):
        g = element('g', {'id': f'asset_{symbol.character_id}'})
        g.append(element('rect', {'width': '8', 'height': '4',
            'fill': '#ff0000' if symbol.character_id == 1 else '#00ff00'}))
        return g


def test_renderer_inclusive_depth_mask_visibility_and_color():
    root = MovieClip(small_tree())
    root.apply(Operation(1, {'character_id': 1, 'matrix': Matrix(a=.25), 'clip_depth': 3}))
    root.apply(Operation(2, {'character_id': 1}))
    root.apply(Operation(3, {'character_id': 2, 'matrix': Matrix(tx=1)}))
    root.apply(Operation(4, {'character_id': 2, 'matrix': Matrix(a=.125, d=.25, tx=4),
        'color': ColorTransform((0, 0, 0, .5), (20, 40, 60, 0))}))
    root.apply(Operation(5, {'character_id': 2, 'visible': False}))
    renderer = SceneRenderer(RectAssets())
    image = Image.open(io.BytesIO(renderer.png(root, (8, 4)))).convert('RGB')
    assert image.getpixel((0, 2)) == (255, 0, 0)
    assert image.getpixel((1, 2)) == (0, 255, 0)
    assert image.getpixel((2, 2)) == (0, 0, 0)  # Mask clips depths 2 AND 3.
    assert image.getpixel((4, 0)) == (10, 20, 30)  # Depth 4 is outside mask; RGBA cxform applies.
    assert renderer.report['masks'] == 1
    assert renderer.report['unsupported'] == []


def test_real_scene_render_is_deterministic_and_does_not_mutate_game(document):
    game = Game(42, 1)
    snapshot, rng = game.snapshot(), game.rt.rng.getstate()
    root = document.root(10)
    tree = json.dumps(root.dump(), sort_keys=True)
    renderer = SceneRenderer()
    first = renderer.png(root)
    assert renderer.png(root) == first
    assert Image.open(io.BytesIO(first)).size == (800, 600)
    # Existing independent JPEXS frame export includes a diagnostic placeholder
    # for unsupported video. Outside that rectangle, enforce source composition.
    actual = Image.open(io.BytesIO(first)).convert('RGB')
    reference = Image.open(ROOT / 'reverse/frames/10.png').convert('RGB')
    for image in (actual, reference):
        ImageDraw.Draw(image).rectangle((230, 150, 542, 389), fill=0)
    assert max(ImageStat.Stat(ImageChops.difference(actual, reference)).mean) < .01
    assert json.dumps(root.dump(), sort_keys=True) == tree
    assert game.snapshot() == snapshot and game.rt.rng.getstate() == rng
    assert renderer.report['unsupported'] == [{'character_id': 5911,
        'path': '_root/introMovie/#3/#2', 'feature': 'leaf tag 60'}]


def test_city_instances_reuse_completed_atlas_instead_of_another_city_renderer(document):
    import base64
    import xml.etree.ElementTree as ET
    city = MovieClip(document.symbols, 1363)
    city.goto_and_stop(6)
    city.matrix = Matrix(.8, 0, 0, .8, 50, 100)
    renderer = SceneRenderer()
    svg = ET.fromstring(renderer.svg(city, (150, 150)))
    image = svg.find('.//{http://www.w3.org/2000/svg}image')
    entry = json.loads((ROOT / 'assets/cities/manifest.json').read_text())['symbols']['christian_buildings']['frames']['6']
    assert [float(image.get(k)) for k in ('x', 'y')] == entry['offset']
    href = image.get('{http://www.w3.org/1999/xlink}href')
    assert base64.b64decode(href.split(',')[1]) == (ROOT / 'assets/cities' / entry['file']).read_bytes()
    assert renderer.report['rendered_leaf_instances'] == 1
    assert renderer.report['unsupported'] == []
