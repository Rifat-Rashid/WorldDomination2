# Generated from __Packages/Btn_simple.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Btn_simple_Btn_simple(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_srcMC', '_img'], ['_img', '_srcMC'], closure, 'Btn_simple')
    assign(ref(this, 'srcMC'), '=', lambda: e.get('_srcMC'))
    assign(ref(this, 'img'), '=', lambda: e.get('_img'))
    return U

def Btn_simple_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Btn_simple')
    pass

def register(rt):
    rt.define('Btn_simple', None, Btn_simple_fields, {'Btn_simple': ASFunction(Btn_simple_Btn_simple)}, {}, {})
