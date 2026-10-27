# Generated from DefineSprite_4425_propaganda_beams/frame_2/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['loopCount'], closure, None)
    e.set('loopCount', 0)
    return U

def register(rt):
    rt.scripts['DefineSprite_4425_propaganda_beams/frame_2/DoAction.as'] = ASFunction(run)
