# Generated from DefineSprite_4018/frame_1/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('gotoAndPlay', [rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [2, 110])])
    return U

def register(rt):
    rt.scripts['DefineSprite_4018/frame_1/DoAction.as'] = ASFunction(run)
