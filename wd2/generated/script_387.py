# Generated from DefineSprite_5953/frame_290/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('stop', [])
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'load_full_version_btns'), [this])
    return U

def register(rt):
    rt.scripts['DefineSprite_5953/frame_290/DoAction.as'] = ASFunction(run)
