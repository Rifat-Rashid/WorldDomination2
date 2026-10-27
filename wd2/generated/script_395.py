# Generated from spaceRocket_trail_element.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(e.get('Object'), 'registerClass'), ['spaceRocket_trail_element', e.get('SpaceRocket_trail_element')])
    return U

def register(rt):
    rt.scripts['spaceRocket_trail_element.as'] = ASFunction(run)
