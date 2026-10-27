# Generated from DefineSprite_4425_propaganda_beams/frame_3/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    update(e.ref('loopCount'), 1, False)
    if truth(binop('>', e.get('loopCount'), 8)):
        e.call('gotoAndStop', [1])
    return U

def register(rt):
    rt.scripts['DefineSprite_4425_propaganda_beams/frame_3/DoAction.as'] = ASFunction(run)
