# Generated from DefineSprite_1808_explosion002/frame_51/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('stop', [])
    return U

def register(rt):
    rt.scripts['DefineSprite_1808_explosion002/frame_51/DoAction.as'] = ASFunction(run)
