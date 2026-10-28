"""Independent pixel, payload and decoder checks for compact runtime storage."""
import base64
import gzip
import hashlib
import io
import json
from pathlib import Path
import re
import zipfile

from PIL import Image
import pytest
import resvg_py

from wd2.resources import RUNTIME, ROOT, asset_path, read_asset

IMAGE = re.compile(rb'data:image/\w+;base64,([A-Za-z0-9+/=\s]+)',re.I)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def pixel_identity(data):
    with Image.open(io.BytesIO(data)) as source:
        rgba = source.convert('RGBA')
        return [rgba.width,rgba.height,digest(rgba.tobytes())]


def test_reader_prefers_compressed_payload_and_preserves_loose_fallback(tmp_path):
    path = tmp_path/'effect.mp3'
    data = b'original encoded audio'*100
    path.write_bytes(b'outdated loose export')
    compressed = tmp_path/'effect.mp3.gz'
    compressed.write_bytes(gzip.compress(data,mtime=0))
    assert asset_path(path) == compressed and read_asset(path) == data
    compressed.unlink()
    assert read_asset(path) == b'outdated loose export'
    graphic = tmp_path/'shape.svgz'
    graphic.write_bytes(gzip.compress(b'<svg/>',mtime=0))
    assert read_asset(tmp_path/'shape.svg') == b'<svg/>'


def test_all_compressed_payloads_preserve_recorded_bytes_markup_and_bitmap_pixels():
    metadata = json.loads(read_asset(RUNTIME/'compression.json'))
    seen = {}
    for name,expected in metadata['decoded_sha256'].items():
        data = read_asset(RUNTIME/name)
        assert digest(data) == expected,name
        if name in metadata['svg_markup_sha256']:
            assert digest(IMAGE.sub(b'BITMAP',data)) == metadata['svg_markup_sha256'][name],name
            for match in IMAGE.finditer(data):
                bitmap = base64.b64decode(match[1]); key = digest(bitmap)
                if key not in seen:
                    seen[key] = pixel_identity(bitmap)
                assert seen[key] == metadata['bitmap_pixels'][key],name
    assert set(seen) == set(metadata['bitmap_pixels'])


def test_lossless_webp_embedded_in_svg_matches_original_png_decoder():
    image = Image.new('RGBA',(2,2))
    image.putdata([(255,0,0,255),(0,0,255,127),(0,255,0,0),(255,255,255,255)])
    pixels = []
    for fmt in ('PNG','WEBP'):
        stream = io.BytesIO()
        image.save(stream,format=fmt,lossless=True,exact=True)
        svg = '<svg xmlns="http://www.w3.org/2000/svg" width="2" height="2"><image width="2" height="2" href="data:image/'+fmt.lower()+';base64,'+base64.b64encode(stream.getvalue()).decode()+'"/></svg>'
        png = resvg_py.svg_to_bytes(svg_string=svg)
        pixels.append(Image.open(io.BytesIO(png)).convert('RGBA').tobytes())
    assert pixels[0] == pixels[1]


def test_packed_assets_against_preserved_original_export_bytes_and_pixels():
    backup = ROOT/'analysis/assets_before_compression.zip'
    if not backup.exists():
        pytest.skip('Optional private original-export reference')
    identities = {}
    def identity(data):
        key = digest(data)
        if key not in identities:
            identities[key] = pixel_identity(data)
        return identities[key]
    with zipfile.ZipFile(backup) as archive:
        for name in archive.namelist():
            if name == 'manifest.json':
                continue
            before = archive.read(name); after = read_asset(RUNTIME/name)
            if name.endswith('.gz'):
                assert (RUNTIME/name).read_bytes() == before,name
                assert after == gzip.decompress(before),name
                continue
            if name.endswith('.svg'):
                assert IMAGE.sub(b'BITMAP',before) == IMAGE.sub(b'BITMAP',after),name
                a = [identity(base64.b64decode(m[1])) for m in IMAGE.finditer(before)]
                b = [identity(base64.b64decode(m[1])) for m in IMAGE.finditer(after)]
                assert a == b,name
            else:
                assert after == before,name
