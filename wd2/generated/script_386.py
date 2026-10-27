# Generated from DefineSprite_5953/frame_2/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def f_1(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    return U

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(e.get('bg'), 'onPress'), '=', lambda: ASFunction(f_1, e))
    assign(ref(e.get('bg'), 'useHandCursor'), '=', lambda: False)
    return U

def register(rt):
    rt.scripts['DefineSprite_5953/frame_2/DoAction.as'] = ASFunction(run)
