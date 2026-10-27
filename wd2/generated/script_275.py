# Generated from DefineSprite_4444/frame_134/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('gotoAndStop', [1])
    return U

def register(rt):
    rt.scripts['DefineSprite_4444/frame_134/DoAction.as'] = ASFunction(run)
