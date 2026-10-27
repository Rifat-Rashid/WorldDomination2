# Generated from __Packages/Tech.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Tech_Tech(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_name', 'param_id', 'param_cost', 'param_invented', 'param_weight', 'param_requiredTech', 'param_desireGroup', 'param_techLevel', 'param_pretty_name', 'p_allow_in_demo'], ['p_allow_in_demo', 'param_cost', 'param_desireGroup', 'param_id', 'param_invented', 'param_name', 'param_pretty_name', 'param_requiredTech', 'param_techLevel', 'param_weight'], closure, 'Tech')
    assign(ref(this, 'techName'), '=', lambda: e.get('param_name'))
    assign(ref(this, 'techID'), '=', lambda: e.get('param_id'))
    assign(ref(this, 'cost'), '=', lambda: e.get('param_cost'))
    assign(ref(this, '_invented'), '=', lambda: e.get('param_invented'))
    assign(ref(this, 'weight'), '=', lambda: e.get('param_weight'))
    assign(ref(this, 'requiredTech'), '=', lambda: e.get('param_requiredTech'))
    assign(ref(this, 'desireGroup'), '=', lambda: e.get('param_desireGroup'))
    assign(ref(this, 'techLevel'), '=', lambda: e.get('param_techLevel'))
    assign(ref(this, 'inventedInLastTurn'), '=', lambda: False)
    assign(ref(this, 'prettyName'), '=', lambda: e.get('param_pretty_name'))
    assign(ref(this, 'allow_in_demo'), '=', lambda: e.get('p_allow_in_demo'))
    return U

def Tech___set__invented(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_bln'], ['_bln'], closure, 'Tech')
    assign(ref(this, '_invented'), '=', lambda: e.get('_bln'))
    if truth(e.get('_bln')):
        assign(ref(this, 'inventedInLastTurn'), '=', lambda: True)
    return U

def Tech___get__invented(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Tech')
    return ref(this, '_invented').get()
    return U

def Tech_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Tech')
    ref(this, 'preOrder').set(False)

def register(rt):
    rt.define('Tech', None, Tech_fields, {'Tech': ASFunction(Tech_Tech)}, {'invented': ASFunction(Tech___get__invented)}, {'invented': ASFunction(Tech___set__invented)})
