# Generated from DefineSprite_3251_boat001_still/frame_6/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('stop', [])
    return U

def register(rt):
    rt.scripts['DefineSprite_3251_boat001_still/frame_6/DoAction.as'] = ASFunction(run)
