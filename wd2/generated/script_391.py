# Generated from frame_10/DoAction_2.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('stop', [])
    assign(ref(e.get('_global'), 'main'), '=', lambda: rt.construct(e.get('Main'), []))
    return U

def register(rt):
    rt.scripts['frame_10/DoAction_2.as'] = ASFunction(run)
