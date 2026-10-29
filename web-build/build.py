"""Build a browser archive from the reviewed public checkout."""
from pathlib import Path
import hashlib
import json
import base64
import gzip
import io
import os
import re
import zipfile
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent / 'publication' / 'repo'
if not ROOT.is_dir():
    ROOT = HERE.parent
OUT = Path(os.environ.get('WD2_WEB_BUILD_OUTPUT', HERE / 'dist'))
WEBP = re.compile(rb'data:image/webp;base64,([A-Za-z0-9+/=]+)')

def svg_for_browser(data):
    """The browser resvg build needs PNG; preserve decoded texture pixels."""
    svg=gzip.decompress(data)
    def convert(match):
        image=Image.open(io.BytesIO(base64.b64decode(match.group(1)))).convert('RGBA')
        out=io.BytesIO();image.save(out,format='PNG')
        return b'data:image/png;base64,'+base64.b64encode(out.getvalue())
    updated,count=WEBP.subn(convert,svg)
    return (gzip.compress(updated,mtime=0),count) if count else (data,0)

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    files = []
    for directory in ('wd2', 'assets/runtime', 'assets/cities'):
        files.extend(p for p in (ROOT / directory).rglob('*') if p.is_file()
                     and '__pycache__' not in p.parts and p.suffix not in ('.pyc', '.pyo'))
    paths = {p.relative_to(ROOT).as_posix() for p in files}
    allowed = set(json.loads((ROOT / 'public-files.json').read_text(encoding='utf-8')))
    unexpected = paths - allowed
    if unexpected:
        raise RuntimeError(f'Unreviewed runtime files: {sorted(unexpected)[:10]}')
    archive = OUT / 'game.zip'
    converted=0
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as package:
        for path in sorted(files):
            relative=path.relative_to(ROOT).as_posix()
            if path.suffix=='.svgz':
                data,count=svg_for_browser(path.read_bytes());converted+=count
                package.writestr(relative,data)
            else:package.write(path,relative)
    print(json.dumps({'files':len(files), 'bytes':archive.stat().st_size,
                      'textures_converted':converted,
                      'sha256':hashlib.sha256(archive.read_bytes()).hexdigest()}))

if __name__ == '__main__':
    main()
