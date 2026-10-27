# Generated from DefineSprite_4998_antiAir_bhu/frame_1/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('stop', [])
    return U

def register(rt):
    rt.scripts['DefineSprite_4998_antiAir_bhu/frame_1/DoAction.as'] = ASFunction(run)
