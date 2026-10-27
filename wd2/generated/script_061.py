# Generated from DefineSprite_1309/frame_1/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('stop', [])
    assign(e.ref('loopCount'), '=', lambda: 0)
    return U

def register(rt):
    rt.scripts['DefineSprite_1309/frame_1/DoAction.as'] = ASFunction(run)
