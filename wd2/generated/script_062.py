# Generated from DefineSprite_1309/frame_18/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    update(e.ref('loopCount'), 1, False)
    if truth(unary('!', e.get('loopCount'))):
        assign(e.ref('loopCount'), '=', lambda: 1)
    if truth(binop('>', e.get('loopCount'), 10)):
        e.call('gotoAndStop', [1])
    else:
        e.call('gotoAndPlay', [2])
    return U

def register(rt):
    rt.scripts['DefineSprite_1309/frame_18/DoAction.as'] = ASFunction(run)
