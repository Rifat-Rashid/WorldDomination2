# Generated from DefineSprite_4486/frame_45/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('gotoAndPlay', [2])
    return U

def register(rt):
    rt.scripts['DefineSprite_4486/frame_45/DoAction.as'] = ASFunction(run)
