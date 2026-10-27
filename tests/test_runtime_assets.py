import hashlib
import json
from pathlib import Path

from wd2.scene_data import RuntimeScene

ROOT = Path(__file__).resolve().parents[1]


def test_reviewed_runtime_assets_are_complete_and_match_manifest():
    for name, digest in json.loads((ROOT / 'assets/runtime/manifest.json').read_text()).items():
        assert hashlib.sha256((ROOT / 'assets' / name).read_bytes()).hexdigest() == digest
    atlas = json.loads((ROOT / 'assets/cities/manifest.json').read_text())
    assert len(atlas['symbols']) == 5
    for symbol in atlas['symbols'].values():
        assert set(map(int, symbol['frames'])) == {*range(1, 7), *range(10, 16)}
        for frame in symbol['frames'].values():
            assert hashlib.sha256((ROOT / 'assets/cities' / frame['file']).read_bytes()).hexdigest() == frame['sha256']


def test_converted_scene_preserves_required_original_hierarchy_and_metadata():
    scene = RuntimeScene()
    root = scene.root()
    assert scene.bounds == (0, 800, 0, 600) and scene.fps == 24
    for name, sid, xy in [('battleMC', 5766, (3, 0)), ('interfaceMC', 4658, (398, 355)),
                          ('gameMenu', 5882, (-112, -29))]:
        node = root.named(name)
        assert node.character_id == sid and node.matrix.point(0, 0) == xy
    assert scene.font_families[4465] == 'Arial'
    assert scene.text_fields[5824]['font'] == 4465
    assert scene.sound_metadata[2]['sample_count'] > 0
