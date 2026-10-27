# World Domination II — Python reconstruction

An unofficial, work-in-progress Python reconstruction of World Domination II.

This initial checkpoint establishes the public repository workflow and automated
publication checks. The runnable application and reviewed runtime assets are being
prepared on `feat/original-gameplay-integration`; this checkpoint does not yet
contain an installable game.

The reconstruction preserves the existing game rules while restoring the original
splash, setup menu and gameplay interface. Full animation and visual parity are
not claimed.

## Development checks

```sh
python tools/check_public_tree.py
python -m unittest discover -s tests -p "test_public_tree.py"
```

## Rights and attribution

This project is unofficial and is not endorsed by the original game's creators.
The existing repository license does not grant rights to third-party game artwork,
music, fonts or translated game content. Any packaged third-party content will be
identified separately; its age or noncommercial use does not imply public-domain
status or redistribution permission.
