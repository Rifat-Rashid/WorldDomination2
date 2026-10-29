# Browser-local prototype

This prototype runs the existing Python game, AI, rendering and audio in the
browser. Its build uses the reviewed runtime files in the parent checkout.

```sh
python -m pip install -r requirements.txt
python web-build/build.py
python web-build/verify_assets.py
python web-build/serve.py
```

Open `http://127.0.0.1:8768` in a browser. The title screen appears as soon as
loading finishes. Phones use the landscape layout; a mouse-oriented device
uses the original desktop layout. Add `?mode=mobile` or `?mode=desktop` to
override detection. Sound is enabled by the first touch, click or key press.

The first load needs the generated game archive (approximately 45 MB) plus the
Python and SVG WebAssembly runtimes from jsDelivr. Once the title screen appears,
the current session can continue offline. Reloading the page requires a network
connection. The game archive is generated in `web-build/dist/` and is not
committed.

The prototype starts at the title screen; the original opening video is not
yet connected to this browser entry point.

The build converts embedded WebP textures to PNG inside SVGZ files for the browser
renderer. `verify_assets.py` independently checks every decoded texture against
the source and verifies all other packaged bytes. Original runtime assets are not
modified. The working source assets occupy approximately 37 MB; the generated
compressed game archive is approximately 45 MB, excluding browser runtimes.

Pygbag's pygame-ce browser runtime was tested first. This prototype uses Pyodide
with a browser WebAssembly SVG renderer because the project's native `resvg_py`
binding is not available in Pygbag's published package index. Pyodide describes
its SDL support as experimental. Browser input, audio, file loading, and the game
loop use a separate adapter; the desktop launcher and generated rules are intact.

The offline turn has been exercised in desktop Chromium and phone-sized Chromium.
A desktop WebKit test exercises the same flow with simulated audio; physical
iPhone Safari and actual device audio still require verification. This is a
prototype and has not been established as a public production deployment.
