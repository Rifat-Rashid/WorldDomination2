# Generated from __Packages/Btn_tube.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Btn_tube_Btn_tube(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_btnMC', '_tubeMC'], ['_btnMC', '_tubeMC'], closure, 'Btn_tube')
    assign(ref(this, 'tubeMC'), '=', lambda: e.get('_tubeMC'))
    assign(ref(ref(ref(ref(this, 'tubeMC').get(), 'txtMC').get(), 'txt').get(), 'embedFonts'), '=', lambda: True)
    assign(ref(ref(ref(this, 'tubeMC').get(), 'txtMC').get(), '_alpha'), '=', lambda: 65)
    assign(ref(this, 'btnMC'), '=', lambda: e.get('_btnMC'))
    assign(ref(ref(this, 'tubeMC').get(), 'targetState'), '=', lambda: 1)
    return U

def f_3(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(binop('>', ref(this, '_currentframe').get(), ref(this, 'targetFrame').get())):
        rt.call_ref(ref(this, 'prevFrame'), [])
        if truth(binop('==', ref(this, '_currentframe').get(), 9)):
            rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_close_tube'])
    else:
        if truth(binop('<', ref(this, '_currentframe').get(), ref(this, 'targetFrame').get())):
            rt.call_ref(ref(this, 'nextFrame'), [])
            if truth(binop('==', ref(this, '_currentframe').get(), 2)):
                rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_open_tube'])
        else:
            rt.call_ref(ref(this, 'gotoAndStop'), [ref(this, 'targetFrame').get()])
            ref(this, 'onEnterFrame').delete()
    return U

def Btn_tube___set__state(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str'], closure, 'Btn_tube')
    if truth(binop('!=', ref(this, 'state').get(), e.get('_str'))):
        rt.call_ref(ref(this, 'setOverlayText'), [])
        switch_1 = e.get('_str')
        case_2 = -1
        if case_2 == -1 and strict_eq(switch_1, 'closed'):
            case_2 = 0
        if case_2 == -1 and strict_eq(switch_1, 'open'):
            case_2 = 1
        if case_2 == -1 and strict_eq(switch_1, 'set'):
            case_2 = 2
        if case_2 == -1:
            case_2 = -1
        try:
            if 0 <= case_2 <= 0:
                assign(ref(ref(this, 'tubeMC').get(), 'targetFrame'), '=', lambda: 1)
                raise ASBreak()
            if 0 <= case_2 <= 1:
                assign(ref(ref(this, 'tubeMC').get(), 'targetFrame'), '=', lambda: 10)
                raise ASBreak()
            if 0 <= case_2 <= 2:
                assign(ref(this, 'handCursor'), '=', lambda: True)
                assign(ref(ref(this, 'tubeMC').get(), 'targetFrame'), '=', lambda: 11)
        except ASBreak:
            pass
        assign(ref(this, '_state'), '=', lambda: e.get('_str'))
        assign(ref(ref(this, 'tubeMC').get(), 'onEnterFrame'), '=', lambda: ASFunction(f_3, e))
    return U

def Btn_tube___set__handCursor(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_bln'], ['_bln'], closure, 'Btn_tube')
    if truth(unary('!', e.get('_bln'))):
        rt.call_ref(ref(ref(this, 'btnMC').get(), 'gotoAndStop'), [2])
    else:
        rt.call_ref(ref(ref(this, 'btnMC').get(), 'gotoAndStop'), [1])
    return U

def Btn_tube_setOverlayText(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_tube')
    assign(ref(this, '_overlayText'), '=', lambda: '')
    if truth(ref(ref(this, 'associatedTA').get(), 'action').get()):
        assign(ref(this, '_overlayText'), '=', lambda: rt.call_ref(ref(ref(e.get('_global'), 'view_interface').get(), 'actionName2label'), [ref(ref(this, 'associatedTA').get(), 'action').get()]))
        if truth(logical('||', binop('==', ref(this, '_overlayText').get(), 'DIRECT ATTACK'), lambda: binop('==', ref(this, '_overlayText').get(), 'PREPARED ATTACK'))):
            rt.call_ref(ref(ref(ref(this, 'tubeMC').get(), 'txtMC').get(), 'gotoAndStop'), [2])
        else:
            rt.call_ref(ref(ref(ref(this, 'tubeMC').get(), 'txtMC').get(), 'gotoAndStop'), [1])
    else:
        if truth(ref(ref(e.get('_global'), 'model').get(), 'userSelectedActionBtn').get()):
            assign(ref(this, '_overlayText'), '=', lambda: rt.call_ref(ref(ref(e.get('_global'), 'view_interface').get(), 'actionName2label'), [ref(ref(e.get('_global'), 'model').get(), 'userSelectedActionBtn').get()]))
            if truth(logical('||', binop('==', ref(this, '_overlayText').get(), 'DIRECT ATTACK'), lambda: binop('==', ref(this, '_overlayText').get(), 'PREPARED ATTACK'))):
                rt.call_ref(ref(ref(ref(this, 'tubeMC').get(), 'txtMC').get(), 'gotoAndStop'), [2])
            else:
                rt.call_ref(ref(ref(ref(this, 'tubeMC').get(), 'txtMC').get(), 'gotoAndStop'), [1])
    if truth(ref(this, '_overlayText').get()):
        assign(ref(ref(ref(ref(this, 'tubeMC').get(), 'txtMC').get(), 'txt').get(), 'htmlText'), '=', lambda: ref(this, '_overlayText').get())
        rt.call_ref(ref(ref(ref(ref(this, 'tubeMC').get(), 'txtMC').get(), 'txt').get(), 'setTextFormat'), [ref(ref(ref(e.get('_global'), 'view').get(), 'textFormats').get(), 'interface_tubeText_1').get()])
        assign(ref(ref(ref(ref(this, 'tubeMC').get(), 'txtMC').get(), 'txt').get(), 'embedFonts'), '=', lambda: True)
    return U

def Btn_tube_getPverlayText(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_tube')
    return ref(this, '_overlayText').get()
    return U

def Btn_tube___get__state(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_tube')
    return ref(this, '_state').get()
    return U

def Btn_tube_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_tube')
    ref(this, 'type').set('tube')
    ref(this, '_state').set('closed')

def register(rt):
    rt.define('Btn_tube', None, Btn_tube_fields, {'Btn_tube': ASFunction(Btn_tube_Btn_tube), 'setOverlayText': ASFunction(Btn_tube_setOverlayText), 'getPverlayText': ASFunction(Btn_tube_getPverlayText)}, {'state': ASFunction(Btn_tube___get__state)}, {'state': ASFunction(Btn_tube___set__state), 'handCursor': ASFunction(Btn_tube___set__handCursor)})
