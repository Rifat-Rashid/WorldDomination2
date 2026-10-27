# Generated from __Packages/Btn_musicSwitch.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Btn_musicSwitch_Btn_musicSwitch(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_overlayMC', '_imgMC', '_option'], ['_imgMC', '_option', '_overlayMC'], closure, 'Btn_musicSwitch')
    assign(ref(this, 'overlayMC'), '=', lambda: e.get('_overlayMC'))
    assign(ref(this, 'imgMC'), '=', lambda: e.get('_imgMC'))
    assign(ref(this, '_state'), '=', lambda: False)
    assign(ref(this, 'option'), '=', lambda: e.get('_option'))
    return U

def Btn_musicSwitch___set__state(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_bln'], ['_bln'], closure, 'Btn_musicSwitch')
    if truth(binop('!=', e.get('_bln'), ref(this, '_state').get())):
        assign(ref(this, '_state'), '=', lambda: e.get('_bln'))
        if truth(unary('!', e.get('_bln'))):
            rt.call_ref(ref(ref(this, 'imgMC').get(), 'gotoAndStop'), [2])
        else:
            rt.call_ref(ref(ref(this, 'imgMC').get(), 'gotoAndStop'), [1])
    return U

def Btn_musicSwitch___get__state(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_musicSwitch')
    return ref(this, '_state').get()
    return U

def Btn_musicSwitch___set__handCursor(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_bln'], ['_bln'], closure, 'Btn_musicSwitch')
    if truth(unary('!', e.get('_bln'))):
        rt.call_ref(ref(ref(this, 'overlayMC').get(), 'gotoAndStop'), [2])
    else:
        rt.call_ref(ref(ref(this, 'overlayMC').get(), 'gotoAndStop'), [1])
    return U

def Btn_musicSwitch_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_musicSwitch')
    pass

def register(rt):
    rt.define('Btn_musicSwitch', None, Btn_musicSwitch_fields, {'Btn_musicSwitch': ASFunction(Btn_musicSwitch_Btn_musicSwitch)}, {'state': ASFunction(Btn_musicSwitch___get__state)}, {'state': ASFunction(Btn_musicSwitch___set__state), 'handCursor': ASFunction(Btn_musicSwitch___set__handCursor)})
