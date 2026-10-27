# Generated from __Packages/Btn_turn.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Btn_turn_Btn_turn(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_btnMC', '_imgMC'], ['_btnMC', '_imgMC'], closure, 'Btn_turn')
    assign(ref(this, 'btnMC'), '=', lambda: e.get('_btnMC'))
    assign(ref(this, 'imgMC'), '=', lambda: e.get('_imgMC'))
    return U

def f_3(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(binop('<', ref(this, '_currentframe').get(), ref(this, 'targetFrame').get())):
        rt.call_ref(ref(this, 'nextFrame'), [])
    else:
        if truth(binop('>', ref(this, '_currentframe').get(), ref(this, 'targetFrame').get())):
            rt.call_ref(ref(this, 'prevFrame'), [])
        else:
            rt.call_ref(ref(this, 'gotoAndStop'), [ref(this, 'targetFrame').get()])
            ref(this, 'onEnterFrame').delete()
    return U

def Btn_turn___set__state(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str'], closure, 'Btn_turn')
    if truth(binop('!=', ref(this, '_state').get(), e.get('_str'))):
        switch_1 = e.get('_str')
        case_2 = -1
        if case_2 == -1 and strict_eq(switch_1, 'closed'):
            case_2 = 0
        if case_2 == -1 and strict_eq(switch_1, 'open'):
            case_2 = 1
        if case_2 == -1 and strict_eq(switch_1, 'green'):
            case_2 = 2
        if case_2 == -1:
            case_2 = -1
        try:
            if 0 <= case_2 <= 0:
                rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_open_turnBtn'])
                assign(ref(ref(this, 'imgMC').get(), 'targetFrame'), '=', lambda: 1)
                assign(ref(this, 'handCursor'), '=', lambda: False)
                raise ASBreak()
            if 0 <= case_2 <= 1:
                rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_close_turnBtn'])
                assign(ref(ref(this, 'imgMC').get(), 'targetFrame'), '=', lambda: 11)
                assign(ref(this, 'handCursor'), '=', lambda: False)
                raise ASBreak()
            if 0 <= case_2 <= 2:
                assign(ref(ref(this, 'imgMC').get(), 'targetFrame'), '=', lambda: 12)
                assign(ref(this, 'handCursor'), '=', lambda: False)
        except ASBreak:
            pass
        assign(ref(this, '_state'), '=', lambda: e.get('_str'))
        assign(ref(ref(this, 'imgMC').get(), 'onEnterFrame'), '=', lambda: ASFunction(f_3, e))
    return U

def Btn_turn___set__handCursor(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_bln'], ['_bln'], closure, 'Btn_turn')
    return U

def Btn_turn___get__state(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_turn')
    return ref(this, '_state').get()
    return U

def Btn_turn_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_turn')
    ref(this, 'pressed').set(False)
    ref(this, '_state').set('closed')

def register(rt):
    rt.define('Btn_turn', None, Btn_turn_fields, {'Btn_turn': ASFunction(Btn_turn_Btn_turn)}, {'state': ASFunction(Btn_turn___get__state)}, {'state': ASFunction(Btn_turn___set__state), 'handCursor': ASFunction(Btn_turn___set__handCursor)})
