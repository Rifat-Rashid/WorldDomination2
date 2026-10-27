# Generated from __Packages/Btn_action.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Btn_action_Btn_action(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str1', '_str2', '_overlayMC', '_mc1', '_mc2', '_tf'], ['_mc1', '_mc2', '_overlayMC', '_str1', '_str2', '_tf'], closure, 'Btn_action')
    assign(ref(this, 'overlayMC'), '=', lambda: e.get('_overlayMC'))
    assign(ref(this, 'actionName'), '=', lambda: e.get('_str1'))
    assign(ref(this, 'label'), '=', lambda: e.get('_str2'))
    assign(ref(this, 'scrnMC'), '=', lambda: e.get('_mc1'))
    assign(ref(this, 'btnSwitch'), '=', lambda: e.get('_mc2'))
    assign(ref(this, 'tf'), '=', lambda: e.get('_tf'))
    assign(ref(this, 'p_bioloaded'), '=', lambda: False)
    return U

def Btn_action___set__pressed(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_bln'], ['_bln'], closure, 'Btn_action')
    assign(ref(this, '_pressed'), '=', lambda: e.get('_bln'))
    if truth(ref(this, 'isSetAction').get()):
        assign(ref(this, 'state'), '=', lambda: 3)
    else:
        if truth(e.get('_bln')):
            assign(ref(this, 'state'), '=', lambda: 2)
        else:
            assign(ref(this, 'state'), '=', lambda: 1)
    return U

def Btn_action___get__pressed(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_action')
    return ref(this, '_pressed').get()
    return U

def Btn_action___set__btnStatus(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str'], closure, 'Btn_action')
    assign(ref(this, '_btnStatus'), '=', lambda: e.get('_str'))
    return U

def Btn_action___get__btnStatus(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_action')
    return ref(this, '_btnStatus').get()
    return U

def Btn_action_setLabelText(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_action')
    assign(ref(ref(this, 'tf').get(), 'text'), '=', lambda: ref(this, 'label').get())
    rt.call_ref(ref(ref(this, 'tf').get(), 'setTextFormat'), [ref(ref(ref(e.get('_global'), 'view').get(), 'textFormats').get(), 'interface_actionText_1').get()])
    assign(ref(ref(this, 'tf').get(), 'embedFonts'), '=', lambda: True)
    return U

def Btn_action___set__btnState(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_nr'], ['_nr'], closure, 'Btn_action')
    assign(ref(this, '_btnState'), '=', lambda: e.get('_nr'))
    return U

def Btn_action___get__btnState(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_action')
    return ref(this, '_btnState').get()
    return U

def Btn_action___set__hover(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_bln'], ['_bln'], closure, 'Btn_action')
    assign(ref(this, '_hover'), '=', lambda: e.get('_bln'))
    rt.call_ref(ref(this, 'updateBtn'), [])
    return U

def Btn_action___get__hover(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_action')
    return ref(this, '_hover').get()
    return U

def Btn_action___set__state(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_nr'], ['_nr'], closure, 'Btn_action')
    assign(ref(this, '_state'), '=', lambda: e.get('_nr'))
    rt.call_ref(ref(this, 'updateBtn'), [])
    return U

def Btn_action_updateBtn(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_action')
    switch_1 = ref(this, '_state').get()
    case_2 = -1
    if case_2 == -1 and strict_eq(switch_1, 1):
        case_2 = 0
    if case_2 == -1 and strict_eq(switch_1, 2):
        case_2 = 1
    if case_2 == -1 and strict_eq(switch_1, 3):
        case_2 = 2
    if case_2 == -1 and strict_eq(switch_1, 4):
        case_2 = 3
    if case_2 == -1:
        case_2 = 4
    try:
        if 0 <= case_2 <= 0:
            if truth(ref(this, 'hover').get()):
                assign(ref(ref(this, 'tf').get(), 'textColor'), '=', lambda: 16777215)
                rt.call_ref(ref(ref(this, 'scrnMC').get(), 'gotoAndStop'), [4])
            else:
                assign(ref(ref(this, 'tf').get(), 'textColor'), '=', lambda: 11184810)
                rt.call_ref(ref(ref(this, 'scrnMC').get(), 'gotoAndStop'), [1])
            rt.call_ref(ref(ref(this, 'btnSwitch').get(), 'gotoAndStop'), [1])
            raise ASBreak()
        if 0 <= case_2 <= 1:
            if truth(ref(this, 'hover').get()):
                assign(ref(ref(this, 'tf').get(), 'textColor'), '=', lambda: 16777215)
            else:
                assign(ref(ref(this, 'tf').get(), 'textColor'), '=', lambda: 0)
            rt.call_ref(ref(ref(this, 'scrnMC').get(), 'gotoAndStop'), [2])
            rt.call_ref(ref(ref(this, 'btnSwitch').get(), 'gotoAndStop'), [2])
            raise ASBreak()
        if 0 <= case_2 <= 2:
            if truth(ref(this, 'hover').get()):
                assign(ref(ref(this, 'tf').get(), 'textColor'), '=', lambda: 16777215)
            else:
                assign(ref(ref(this, 'tf').get(), 'textColor'), '=', lambda: 0)
            rt.call_ref(ref(ref(this, 'scrnMC').get(), 'gotoAndStop'), [3])
            rt.call_ref(ref(ref(this, 'btnSwitch').get(), 'gotoAndStop'), [3])
            raise ASBreak()
        if 0 <= case_2 <= 3:
            assign(ref(ref(this, 'tf').get(), 'textColor'), '=', lambda: 16777215)
            rt.call_ref(ref(ref(this, 'scrnMC').get(), 'gotoAndStop'), [4])
            rt.call_ref(ref(ref(this, 'btnSwitch').get(), 'gotoAndStop'), [1])
        if 0 <= case_2 <= 4:
            return U
    except ASBreak:
        pass
    return U

def Btn_action___get__state(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_action')
    return ref(this, '_state').get()
    return U

def Btn_action___set__handCursor(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_bln'], ['_bln'], closure, 'Btn_action')
    if truth(e.get('_bln')):
        rt.call_ref(ref(ref(this, 'overlayMC').get(), 'gotoAndStop'), [1])
    else:
        rt.call_ref(ref(ref(this, 'overlayMC').get(), 'gotoAndStop'), [2])
    return U

def Btn_action___set__bioloaded(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_bln'], ['_bln'], closure, 'Btn_action')
    assign(ref(this, 'p_bioloaded'), '=', lambda: e.get('_bln'))
    if truth(e.get('_bln')):
        rt.call_ref(ref(ref(ref(this, 'scrnMC').get(), 'bioMC1').get(), 'gotoAndPlay'), [2])
        rt.call_ref(ref(ref(ref(this, 'scrnMC').get(), 'bioMC2').get(), 'gotoAndPlay'), [2])
    else:
        rt.call_ref(ref(ref(ref(this, 'scrnMC').get(), 'bioMC1').get(), 'gotoAndStop'), [1])
        rt.call_ref(ref(ref(ref(this, 'scrnMC').get(), 'bioMC2').get(), 'gotoAndStop'), [1])
    return U

def Btn_action___get__bioloaded(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_action')
    return ref(this, 'p_bioloaded').get()
    return U

def Btn_action_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_action')
    ref(this, 'type').set('action')
    ref(this, 'hoverable').set(True)
    ref(this, '_hover').set(False)
    ref(this, '_btnState').set(0)
    ref(this, '_pressed').set(False)
    ref(this, '_state').set(1)

def register(rt):
    rt.define('Btn_action', None, Btn_action_fields, {'Btn_action': ASFunction(Btn_action_Btn_action), 'setLabelText': ASFunction(Btn_action_setLabelText), 'updateBtn': ASFunction(Btn_action_updateBtn)}, {'pressed': ASFunction(Btn_action___get__pressed), 'btnStatus': ASFunction(Btn_action___get__btnStatus), 'btnState': ASFunction(Btn_action___get__btnState), 'hover': ASFunction(Btn_action___get__hover), 'state': ASFunction(Btn_action___get__state), 'bioloaded': ASFunction(Btn_action___get__bioloaded)}, {'pressed': ASFunction(Btn_action___set__pressed), 'btnStatus': ASFunction(Btn_action___set__btnStatus), 'btnState': ASFunction(Btn_action___set__btnState), 'hover': ASFunction(Btn_action___set__hover), 'state': ASFunction(Btn_action___set__state), 'handCursor': ASFunction(Btn_action___set__handCursor), 'bioloaded': ASFunction(Btn_action___set__bioloaded)})
