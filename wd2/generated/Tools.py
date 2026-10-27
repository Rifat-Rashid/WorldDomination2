# Generated from __Packages/Tools.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Tools_Tools(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Tools')
    return U

def Tools_randRange(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['min', 'max'], ['_loc4_', 'max', 'min'], closure, 'Tools')
    e.set('_loc4_', binop('+', rt.call_ref(ref(e.get('Math'), 'floor'), [binop('*', rt.call_ref(ref(e.get('Math'), 'random'), []), binop('+', binop('-', e.get('max'), e.get('min')), 1))]), e.get('min')))
    return e.get('_loc4_')
    return U

def Tools_reverse_string(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_str'], ['_loc3_', '_loc4_', '_loc5_', '_loc6_', 'a_str'], closure, 'Tools')
    e.set('_loc3_', rt.construct(e.get('Array'), []))
    e.set('_loc4_', '')
    e.set('_loc5_', ref(e.get('a_str'), 'length').get())
    while truth(binop('>=', e.get('_loc5_'), 0)):
        rt.tick()
        try:
            rt.call_ref(ref(e.get('_loc3_'), 'push'), [rt.call_ref(ref(e.get('a_str'), 'charAt'), [e.get('_loc5_')])])
            assign(e.ref('_loc5_'), '=', lambda: binop('-', e.get('_loc5_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc6_', 0)
    while truth(binop('<', e.get('_loc6_'), ref(e.get('_loc3_'), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '+=', lambda: ref(e.get('_loc3_'), e.get('_loc6_')).get())
            assign(e.ref('_loc6_'), '=', lambda: binop('+', e.get('_loc6_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc4_')
    return U

def Tools_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Tools')
    pass

def register(rt):
    rt.define('Tools', None, Tools_fields, {'Tools': ASFunction(Tools_Tools), 'randRange': ASFunction(Tools_randRange), 'reverse_string': ASFunction(Tools_reverse_string)}, {}, {})
