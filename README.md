# World Domination II — Python reconstruction

An unofficial standalone Python reconstruction of the Flash strategy game.
The original splash screen, setup menu, map, city artwork and gameplay HUD run
without Flash, a browser or the original SWF.

This is a partial reconstruction. Original gameplay rules and AI run through
translated Python classes; interface restoration is still in progress.

<p>
  <img src="docs/screenshots/splash.png" alt="Reconstructed World Domination II splash screen" width="400" />
  <img src="docs/screenshots/resources.png" alt="Reconstructed gameplay interface with Resources selected" width="400" />
</p>

## Install and launch

Use Python 3.12 or newer on Windows or Linux:

```sh
python -m pip install -r requirements.txt
python run_game.py
```

Click the title screen, choose your difficulty, nation color, building theme and
one to four opponents, then click **Start Game**. The selected configuration
carries into the original gameplay interface within the same window.

Original action controls:

- Choose Resources, Production, Technology, Mass Media, Direct Attack,
  Prepared Attack, Defense, Propaganda or Diplomacy on the left.
- Use the original production sliders, technology boxes and stock buttons.
  Select a city on the map when prompted; spies also choose a target building.
- Prepared attacks require a carrier on one turn, then a compatible payload
  and target on the next. Ships can assign up to three payloads to cities of
  one opponent. Space rockets use satellites.
- **Accept** queues the action. **Cancel** abandons the draft; a prepared
  carrier has a separate cancellation confirmation.
- Click a filled action tube (or its action button) to cancel and refund it.
  Click an empty tube to skip that action. Each action type can be used once
  per turn, matching the original interface.
- Fill both slots, then click **Confirm** below the map to resolve the turn.
  Pending diplomacy offers must be accepted or rejected first.
- Music and Sound switches operate independently. **P** pauses presentation
  and audio; **Escape** closes the window.

The original Help pages, message scrolling and fullscreen switch are connected.
Win/loss screens retain the original delayed score sequence; **New Game** returns
to the title in the same window. Editable text fields accept keyboard input.
Combat resolves through the existing synchronous engine; timed battle animation
and battle audio synchronization remain unfinished.
Presentation uses a 24 Hz logical clock and cached native surfaces. New scene
states and unsupported effects can take longer to render on some systems.

For the broader playable desktop controls:

```sh
python run_game.py --legacy-ui
```

In that mode choose actions on the right, click a target city, queue two actions
and press **Resolve turn** or Enter. **Clear** cancels queued actions. Arrow
controls select equipment, technology, budgets and diplomacy options. Prepared
attacks use a carrier first and a payload on the following turn. The desktop
currently supports one target per carrier attack.

`python run_original_menu.py` is an alternate launcher for the original flow.
Use `--seed 42` with either mode for reproducible Python sessions; the legacy
mode also accepts `--difficulty 0`, `1` or `2`.

The original SVG renderer remains available with `--svg-renderer`. Screenshot
exports use that reference path; the live window uses the cached compositor.

## Rendering performance

In an off-screen Windows/Python 3.14 benchmark (12 frames per scene), median frame
work including timeline callbacks changed as follows:

| Scene | SVG path | Cached path |
| --- | ---: | ---: |
| Splash | 530 ms | 4.5 ms |
| Setup | 506 ms | 5.2 ms |
| Animated gameplay | 597 ms | 11.5 ms |

Dispatching a gameplay-panel input and producing the resulting frame fell from
about 605 ms to 14 ms after warm-up. These measurements exclude window pacing and
are not hardware input-latency measurements. A cold scene still takes about one
second to populate caches. Surface storage is bounded to 64 MiB, in addition to
the original asset definitions. Actual performance depends on hardware.

## Validation

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q
python run_game.py --smoke --screenshot smoke.png
python run_game.py --legacy-ui --smoke --screenshot legacy-smoke.png
python -m wd2.game --turns 10 --seed 42
```

The original smoke resolves Resources and Mass Media for one turn and exports an
800 x 600 screenshot plus JSON state. Screenshot mode needs no display or audio
device. Automated tests cover setup handoff, HUD/action bindings, real window
event dispatch, mixer playback, deterministic simulations and asset integrity.
Optional checks against source movies and external-player reference captures
explicitly skip in this distribution because those fixtures are not included.

The game loads converted timeline instructions, individual vector artwork,
registered city images, fonts and audio from `assets/`. It does not depend on
development exports. The original 800 x 600 hierarchy and 24 Hz logical clock
are preserved, but animation, shading and font rendering still differ from Flash.
Pixel-perfect fidelity is not claimed.

## Third-party materials

This project is unofficial and is not affiliated with the original game creators.
The repository's code license does not establish permission to redistribute
third-party game assets or translated game content. See
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for the distinction and unresolved
rights status.
