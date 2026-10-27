# Generated from DefineSprite_5953/frame_7/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'full_version_mc_sound_start'), [])
    return U

def register(rt):
    rt.scripts['DefineSprite_5953/frame_7/DoAction.as'] = ASFunction(run)
