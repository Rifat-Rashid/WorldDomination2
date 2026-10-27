"""Runtime asset paths, with optional source-workspace locations for verification."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / 'assets/runtime'


def asset_directory(group):
    packaged = RUNTIME / group
    if packaged.is_dir():
        return packaged
    development = {'shapes': 'reverse/export/shapes', 'texts': 'reverse/svgtext',
                   'fonts': 'reverse/export/fonts', 'audio': 'reverse/export/sounds'}
    return ROOT / development[group]
