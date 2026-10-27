# Generated from DefineSprite_5649/frame_2/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('play', [])
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'launch_space_rocket_sound'), [])
    return U

def register(rt):
    rt.scripts['DefineSprite_5649/frame_2/DoAction.as'] = ASFunction(run)
