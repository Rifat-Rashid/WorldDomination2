# Generated from spaceRocket_smoke.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(e.get('Object'), 'registerClass'), ['spaceRocket_smoke', e.get('SpaceRocket_smoke')])
    return U

def register(rt):
    rt.scripts['spaceRocket_smoke.as'] = ASFunction(run)
