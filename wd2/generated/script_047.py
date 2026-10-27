# Generated from bioCloud.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(e.get('Object'), 'registerClass'), ['bioCloud', e.get('BioCloud')])
    return U

def register(rt):
    rt.scripts['bioCloud.as'] = ASFunction(run)
