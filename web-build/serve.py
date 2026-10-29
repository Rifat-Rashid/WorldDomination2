"""Serve the browser build on localhost with an explicit file allowlist."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit
import argparse

ROOT=Path(__file__).resolve().parent
FILES={
    '/':('index.html','text/html; charset=utf-8'),
    '/index.html':('index.html','text/html; charset=utf-8'),
    '/app.js':('app.js','text/javascript; charset=utf-8'),
    '/browser_game.py':('browser_game.py','text/plain; charset=utf-8'),
    '/icon.png':('icon.png','image/png'),
    '/dist/game.zip':('dist/game.zip','application/zip'),
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        item=FILES.get(urlsplit(self.path).path)
        if not item:return self.send_error(404)
        path=ROOT/item[0]
        if not path.is_file():return self.send_error(404)
        self.send_response(200);self.send_header('Content-Type',item[1]);self.send_header('Content-Length',str(path.stat().st_size))
        self.send_header('X-Content-Type-Options','nosniff');self.end_headers()
        try:
            with path.open('rb') as data:
                while chunk:=data.read(1024*1024):self.wfile.write(chunk)
        except (BrokenPipeError,ConnectionResetError,ConnectionAbortedError):
            pass

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--port',type=int,default=8768)
    args=parser.parse_args()
    ThreadingHTTPServer(('127.0.0.1',args.port),Handler).serve_forever()
