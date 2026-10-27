# Generated from __Packages/Model_interface.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Model_interface_Model_interface(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Model_interface')
    return U

def Model_interface___set__selected_action_name(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str'], closure, 'Model_interface')
    assign(ref(this, '_selected_action_name'), '=', lambda: e.get('_str'))
    return U

def Model_interface___get__selected_action_name(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Model_interface')
    return ref(ref(e.get('_global'), 'model').get(), 'userSelectedActionBtn').get()
    return U

def Model_interface___set__cur_pressed_action_btn(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_btn'], ['_btn'], closure, 'Model_interface')
    if truth(ref(this, 'cur_pressed_action_btn').get()):
        assign(ref(ref(this, 'cur_pressed_action_btn').get(), 'pressed'), '=', lambda: False)
    assign(ref(this, '_cur_pressed_action_btn'), '=', lambda: e.get('_btn'))
    return U

def Model_interface___get__cur_pressed_action_btn(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Model_interface')
    return ref(this, '_cur_pressed_action_btn').get()
    return U

def Model_interface_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Model_interface')
    pass

def register(rt):
    rt.define('Model_interface', None, Model_interface_fields, {'Model_interface': ASFunction(Model_interface_Model_interface)}, {'selected_action_name': ASFunction(Model_interface___get__selected_action_name), 'cur_pressed_action_btn': ASFunction(Model_interface___get__cur_pressed_action_btn)}, {'selected_action_name': ASFunction(Model_interface___set__selected_action_name), 'cur_pressed_action_btn': ASFunction(Model_interface___set__cur_pressed_action_btn)})
