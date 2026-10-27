# Generated from DefineSprite_3205_leadersTopMC/frame_24/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('play', [])
    return U

def register(rt):
    rt.scripts['DefineSprite_3205_leadersTopMC/frame_24/DoAction.as'] = ASFunction(run)
