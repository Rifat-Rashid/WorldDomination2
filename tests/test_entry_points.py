"""Both launchers use the original flow; the desktop remains an explicit fallback."""
import json
from pathlib import Path
import subprocess
import sys

from PIL import Image
import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize('script,options,size', [
    ('run_original_menu.py', ['--select-first'], (800, 600)),
    ('run_game.py', ['--legacy-ui', '--smoke'], (1160, 820)),
    ('run_game.py', ['--smoke'], (800, 600)),
])
def test_launcher_contracts(script, options, size, tmp_path):
    output = tmp_path / f'{script}.png'
    subprocess.run([sys.executable, str(ROOT / script), *options, '--screenshot', str(output)],
                   cwd=ROOT, check=True, capture_output=True, timeout=30)
    assert Image.open(output).size == size
    if script == 'run_original_menu.py':
        report = json.loads(output.with_suffix('.json').read_text())
        assert report['state']['selected_leaders'] == [0]
        assert report['audio'] == {'theme': 'WDTheme.wav', 'music_enabled': True, 'device_connected': False}
    elif '--legacy-ui' not in options:
        report = json.loads(output.with_suffix('.json').read_text())
        assert report['state']['scene'] == 'gameplay'
        assert report['state']['game']['turn'] == 1
