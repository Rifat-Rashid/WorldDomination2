# Generated from __Packages/AI_specialization.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def AI_specialization_AI_specialization(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_randomize'], ['_loc3_', '_randomize'], closure, 'AI_specialization')
    if truth(e.get('_randomize')):
        assign(e.ref('_loc3_'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [1, 2]))
        if truth(binop('==', e.get('_loc3_'), 1)):
            assign(ref(this, 'p_carrier'), '=', lambda: 'rocket')
        else:
            assign(ref(this, 'p_carrier'), '=', lambda: 'plane')
        assign(e.ref('_loc3_'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [1, 2]))
        if truth(binop('==', e.get('_loc3_'), 1)):
            assign(ref(this, 'p_common_payload'), '=', lambda: 'warhead')
        else:
            assign(ref(this, 'p_common_payload'), '=', lambda: 'bioload')
        assign(e.ref('_loc3_'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randrange'), [1, 3]))
        if truth(binop('==', e.get('_loc3_'), 1)):
            assign(ref(this, 'p_special_unit'), '=', lambda: 'submarine')
        else:
            if truth(binop('==', e.get('_loc3_'), 2)):
                assign(ref(this, 'p_special_unit'), '=', lambda: 'carrier')
            else:
                assign(ref(this, 'p_special_unit'), '=', lambda: 'space')
    return U

def AI_specialization_create_desire_arr(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'AI_specialization')
    e.set('_loc2_', rt.construct(e.get('Array'), []))
    if truth(binop('==', ref(this, 'p_carrier').get(), 'rocket')):
        rt.call_ref(ref(e.get('_loc2_'), 'push'), [2, 2, 2, 5])
    else:
        rt.call_ref(ref(e.get('_loc2_'), 'push'), [0, 0, 0, 0])
    if truth(binop('==', ref(this, 'p_common_payload').get(), 'warhead')):
        rt.call_ref(ref(e.get('_loc2_'), 'push'), [2, 2, 2, 5, 0, 0, 0, 0])
    else:
        rt.call_ref(ref(e.get('_loc2_'), 'push'), [0, 0, 0, 0, 2, 2, 2, 5])
    if truth(binop('==', rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [1, 2]), 1)):
        rt.call_ref(ref(e.get('_loc2_'), 'push'), [1, 1, 1, 5])
    else:
        rt.call_ref(ref(e.get('_loc2_'), 'push'), [0, 0, 0, 0])
    rt.call_ref(ref(e.get('_loc2_'), 'push'), [1, 1, 1, 5])
    if truth(binop('==', ref(this, 'p_carrier').get(), 'plane')):
        rt.call_ref(ref(e.get('_loc2_'), 'push'), [2, 5])
    else:
        rt.call_ref(ref(e.get('_loc2_'), 'push'), [0, 0])
    if truth(binop('==', ref(this, 'p_special_unit').get(), 1)):
        rt.call_ref(ref(e.get('_loc2_'), 'push'), [5, 0, 0, 0])
    else:
        if truth(binop('==', ref(this, 'p_special_unit').get(), 2)):
            rt.call_ref(ref(e.get('_loc2_'), 'push'), [1, 5, 0, 0])
        else:
            rt.call_ref(ref(e.get('_loc2_'), 'push'), [1, 1, 5, 5])
    assign(ref(this, 'desireArr'), '=', lambda: e.get('_loc2_'))
    return U

def AI_specialization___set__carrier(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str'], closure, 'AI_specialization')
    assign(ref(this, 'p_carrier'), '=', lambda: e.get('_str'))
    return U

def AI_specialization___get__carrier(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'AI_specialization')
    return ref(this, 'p_carrier').get()
    return U

def AI_specialization___set__common_payload(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str'], closure, 'AI_specialization')
    assign(ref(this, 'p_common_payload'), '=', lambda: e.get('_str'))
    return U

def AI_specialization___get__common_payload(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'AI_specialization')
    return ref(this, 'p_common_payload').get()
    return U

def AI_specialization___set__special_unit(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str'], closure, 'AI_specialization')
    assign(ref(this, 'p_special_unit'), '=', lambda: e.get('_str'))
    return U

def AI_specialization___get__special_unit(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'AI_specialization')
    return ref(this, 'p_special_unit').get()
    return U

def AI_specialization_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'AI_specialization')
    pass

def register(rt):
    rt.define('AI_specialization', None, AI_specialization_fields, {'AI_specialization': ASFunction(AI_specialization_AI_specialization), 'create_desire_arr': ASFunction(AI_specialization_create_desire_arr)}, {'carrier': ASFunction(AI_specialization___get__carrier), 'common_payload': ASFunction(AI_specialization___get__common_payload), 'special_unit': ASFunction(AI_specialization___get__special_unit)}, {'carrier': ASFunction(AI_specialization___set__carrier), 'common_payload': ASFunction(AI_specialization___set__common_payload), 'special_unit': ASFunction(AI_specialization___set__special_unit)})
