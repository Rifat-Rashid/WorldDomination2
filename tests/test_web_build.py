"""Exercise the reviewed browser bundle and its restricted local server."""
import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import sys
import threading
from urllib.error import HTTPError
from urllib.request import urlopen

import pytest

ROOT=Path(__file__).resolve().parents[1]
WEB=ROOT/'web-build'


@pytest.fixture(scope='module')
def built(tmp_path_factory):
    directory=tmp_path_factory.mktemp('web_bundle')
    env=dict(os.environ,WD2_WEB_BUILD_OUTPUT=str(directory))
    subprocess.run([sys.executable,str(WEB/'build.py')],cwd=ROOT,check=True,env=env)
    return directory,env


def test_packaged_assets_retain_exact_decoded_pixels(built):
    result=subprocess.run([sys.executable,str(WEB/'verify_assets.py')],cwd=ROOT,check=True,capture_output=True,text=True,env=built[1])
    assert 'all pixels and other bytes match' in result.stdout


def test_local_server_only_serves_the_intended_browser_files(built,tmp_path):
    spec=importlib.util.spec_from_file_location('browser_serve',WEB/'serve.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    module.ROOT=tmp_path
    (tmp_path/'dist').mkdir()
    shutil.copyfile(WEB/'index.html',tmp_path/'index.html')
    shutil.copyfile(built[0]/'game.zip',tmp_path/'dist/game.zip')
    server=module.ThreadingHTTPServer(('127.0.0.1',0),module.Handler)
    thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
    base=f'http://127.0.0.1:{server.server_port}'
    try:
        with urlopen(base+'/',timeout=5) as response:
            page=response.read().decode('utf-8')
            assert response.headers.get_content_type()=='text/html'
            assert 'apple-touch-icon' in page
        with urlopen(base+'/dist/game.zip',timeout=5) as response:
            assert response.headers.get_content_type()=='application/zip'
            assert response.read(4)==b'PK\x03\x04'
        for path in ('/AGENTS.md','/build.py','/analysis/PROGRESS.md','/wd2/runtime.py'):
            with pytest.raises(HTTPError) as error:urlopen(base+path,timeout=5)
            assert error.value.code==404
    finally:
        server.shutdown();server.server_close();thread.join()
