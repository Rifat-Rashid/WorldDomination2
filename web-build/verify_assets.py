"""Independently compare packaged textures and other assets with the source."""
import base64,gzip,io,re,zipfile
from pathlib import Path
from PIL import Image
from build import ROOT,OUT

webp=re.compile(rb'data:image/webp;base64,([A-Za-z0-9+/=]+)')
png=re.compile(rb'data:image/png;base64,([A-Za-z0-9+/=]+)')
count=files=0
with zipfile.ZipFile(OUT/'game.zip') as package:
    for name in package.namelist():
        files+=1;source=(ROOT/name).read_bytes();built=package.read(name)
        if not name.endswith('.svgz'):
            assert source==built,name
            continue
        original=gzip.decompress(source);converted=gzip.decompress(built)
        left=webp.findall(original)
        if not left:
            assert original==converted,name
            continue
        right=png.findall(converted)
        assert len(left)==len(right),name
        assert webp.sub(b'TEXTURE',original)==png.sub(b'TEXTURE',converted),name
        for a,b in zip(left,right):
            old=Image.open(io.BytesIO(base64.b64decode(a))).convert('RGBA')
            new=Image.open(io.BytesIO(base64.b64decode(b))).convert('RGBA')
            assert old.size==new.size and old.tobytes()==new.tobytes(),name
            count+=1
print(f'Compared {files} files and {count} decoded textures; all pixels and other bytes match.')
