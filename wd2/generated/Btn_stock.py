# Generated from __Packages/Btn_stock.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Btn_stock_Btn_stock(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_id', '_name', '_label', '_overlayMC', '_labelTF', '_scrn', '_scrnTF', '_btnSwitch', '_relatedWeapon', '_stockPanelNum', '_deactivate_in_demo'], ['_btnSwitch', '_deactivate_in_demo', '_id', '_label', '_labelTF', '_name', '_overlayMC', '_relatedWeapon', '_scrn', '_scrnTF', '_stockPanelNum'], closure, 'Btn_stock')
    assign(ref(this, 'id'), '=', lambda: e.get('_id'))
    assign(ref(this, 'name'), '=', lambda: e.get('_name'))
    assign(ref(this, 'label'), '=', lambda: e.get('_label'))
    assign(ref(this, 'overlayMC'), '=', lambda: e.get('_overlayMC'))
    assign(ref(this, 'labelTF'), '=', lambda: e.get('_labelTF'))
    assign(ref(this, 'scrn'), '=', lambda: e.get('_scrn'))
    assign(ref(this, 'scrnTF'), '=', lambda: e.get('_scrnTF'))
    assign(ref(this, 'btnSwitch'), '=', lambda: e.get('_btnSwitch'))
    assign(ref(this, 'relatedWeapon'), '=', lambda: e.get('_relatedWeapon'))
    assign(ref(ref(this, 'labelTF').get(), 'text'), '=', lambda: ref(this, 'label').get())
    rt.call_ref(ref(ref(this, 'labelTF').get(), 'setTextFormat'), [ref(ref(ref(e.get('_global'), 'view').get(), 'textFormats').get(), 'interface_stockText_1').get()])
    assign(ref(ref(this, 'labelTF').get(), 'embedFonts'), '=', lambda: True)
    rt.call_ref(ref(ref(this, 'scrnTF').get(), 'setTextFormat'), [ref(ref(ref(e.get('_global'), 'view').get(), 'textFormats').get(), 'interface_stockScrnText_1').get()])
    assign(ref(ref(this, 'scrnTF').get(), 'embedFonts'), '=', lambda: True)
    assign(ref(this, 'stockPanelNum'), '=', lambda: e.get('_stockPanelNum'))
    assign(ref(this, 'deactivate_in_demo'), '=', lambda: e.get('_deactivate_in_demo'))
    return U

def Btn_stock___set__stockAmount(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_nr'], ['_nr'], closure, 'Btn_stock')
    assign(ref(this, '_stockAmount'), '=', lambda: e.get('_nr'))
    assign(ref(ref(this, 'scrnTF').get(), 'text'), '=', lambda: binop('+', '', e.get('_nr')))
    if truth(binop('==', e.get('_nr'), unary('-', 1))):
        assign(ref(ref(this, 'scrnTF').get(), 'text'), '=', lambda: '-')
    return U

def Btn_stock_resetClips(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_stock')
    rt.call_ref(ref(ref(this, 'btnSwitch').get(), 'gotoAndStop'), [1])
    return U

def Btn_stock___set__state(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_nr'], ['_nr'], closure, 'Btn_stock')
    assign(ref(this, '_state'), '=', lambda: e.get('_nr'))
    switch_1 = e.get('_nr')
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
        case_2 = -1
    try:
        if 0 <= case_2 <= 0:
            rt.call_ref(ref(ref(this, 'btnSwitch').get(), 'gotoAndStop'), [1])
            raise ASBreak()
        if 0 <= case_2 <= 1:
            rt.call_ref(ref(ref(this, 'btnSwitch').get(), 'gotoAndStop'), [2])
            raise ASBreak()
        if 0 <= case_2 <= 2:
            rt.call_ref(ref(ref(this, 'btnSwitch').get(), 'gotoAndStop'), [3])
            raise ASBreak()
        if 0 <= case_2 <= 3:
            rt.call_ref(ref(ref(this, 'btnSwitch').get(), 'gotoAndStop'), [1])
            assign(ref(ref(this, 'labelTF').get(), 'textColor'), '=', lambda: 13421772)
    except ASBreak:
        pass
    return U

def Btn_stock___get__state(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_stock')
    return ref(this, '_state').get()
    return U

def Btn_stock___set__hover(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_bln'], ['_bln'], closure, 'Btn_stock')
    assign(ref(this, '_hover'), '=', lambda: e.get('_bln'))
    if truth(binop('==', ref(this, '_hover').get(), True)):
        assign(ref(ref(this, 'labelTF').get(), 'textColor'), '=', lambda: 16777215)
        assign(ref(ref(this, 'scrnTF').get(), 'textColor'), '=', lambda: 16777215)
        if truth(logical('&&', ref(this, 'deactivate_in_demo').get(), lambda: ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get())):
            assign(ref(ref(this, 'labelTF').get(), 'text'), '=', lambda: 'DEMO')
            assign(ref(ref(this, 'labelTF').get(), 'textColor'), '=', lambda: 16776960)
    else:
        if truth(ref(this, 'deactivate_in_demo').get()):
            assign(ref(ref(this, 'labelTF').get(), 'text'), '=', lambda: ref(this, 'label').get())
        assign(ref(ref(this, 'labelTF').get(), 'textColor'), '=', lambda: 13421772)
        assign(ref(ref(this, 'scrnTF').get(), 'textColor'), '=', lambda: 13421772)
    return U

def Btn_stock___get__hover(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_stock')
    return ref(this, '_hover').get()
    return U

def Btn_stock___set__bioloaded(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_bln'], ['_bln'], closure, 'Btn_stock')
    if truth(e.get('_bln')):
        rt.call_ref(ref(ref(ref(this, 'scrn').get(), 'bioMC').get(), 'gotoAndPlay'), [2])
    else:
        rt.call_ref(ref(ref(ref(this, 'scrn').get(), 'bioMC').get(), 'gotoAndStop'), [1])
    return U

def Btn_stock_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_stock')
    ref(this, 'type').set('stock')
    ref(this, 'hoverable').set(True)
    ref(this, '_hover').set(False)
    ref(this, '_state').set(0)
    ref(this, 'deactivate_in_demo').set(False)

def register(rt):
    rt.define('Btn_stock', None, Btn_stock_fields, {'Btn_stock': ASFunction(Btn_stock_Btn_stock), 'resetClips': ASFunction(Btn_stock_resetClips)}, {'state': ASFunction(Btn_stock___get__state), 'hover': ASFunction(Btn_stock___get__hover)}, {'stockAmount': ASFunction(Btn_stock___set__stockAmount), 'state': ASFunction(Btn_stock___set__state), 'hover': ASFunction(Btn_stock___set__hover), 'bioloaded': ASFunction(Btn_stock___set__bioloaded)})
