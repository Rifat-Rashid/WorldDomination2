# Generated from DefineSprite_5808/frame_99/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(e.get('_root'), 'gotoAndPlay'), [3])
    return U

def register(rt):
    rt.scripts['DefineSprite_5808/frame_99/DoAction.as'] = ASFunction(run)
