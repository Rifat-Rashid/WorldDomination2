"""Runtime asset paths, with optional source-workspace locations for verification."""
from pathlib import Path
import gzip

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / 'assets/runtime'


def asset_path(path):
    """Prefer a losslessly compressed asset, retaining loose-export fallback."""
    path = Path(path)
    if path.suffix in ('.svgz', '.gz'):
        return path
    compressed = path.with_suffix('.svgz') if path.suffix == '.svg' else Path(str(path)+'.gz')
    return compressed if compressed.is_file() else path


def read_asset(path):
    path = asset_path(path)
    data = path.read_bytes()
    return gzip.decompress(data) if path.suffix in ('.svgz', '.gz') else data


def asset_directory(group):
    packaged = RUNTIME / group
    if packaged.is_dir():
        return packaged
    development = {'shapes': 'reverse/export/shapes', 'texts': 'reverse/svgtext',
                   'fonts': 'reverse/export/fonts', 'audio': 'reverse/export/sounds'}
    return ROOT / development[group]
