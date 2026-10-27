# Generated from __Packages/WeaponSlot.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def WeaponSlot_WeaponSlot(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_type', 'param_category', 'param_level', 'param_name', 'param_ID', 'param_cost', 'param_techName', 'param_counteredBy', 'param_active', 'param_maxKills', 'param_initStock', 'param_maxStock', 'param_mcLinkage', 'param_inUse', 'param_desireGroup', 'param_explosion_mc_name', 'param_prettyName'], ['param_ID', 'param_active', 'param_category', 'param_cost', 'param_counteredBy', 'param_desireGroup', 'param_explosion_mc_name', 'param_inUse', 'param_initStock', 'param_level', 'param_maxKills', 'param_maxStock', 'param_mcLinkage', 'param_name', 'param_prettyName', 'param_techName', 'param_type'], closure, 'WeaponSlot')
    assign(ref(this, 'investment'), '=', lambda: 0)
    assign(ref(this, 'weaponType'), '=', lambda: e.get('param_type'))
    assign(ref(this, 'weaponCategory'), '=', lambda: e.get('param_category'))
    assign(ref(this, 'weaponLevel'), '=', lambda: e.get('param_level'))
    assign(ref(this, 'weaponName'), '=', lambda: e.get('param_name'))
    assign(ref(this, 'weaponID'), '=', lambda: e.get('param_ID'))
    assign(ref(this, 'cost'), '=', lambda: e.get('param_cost'))
    assign(ref(this, 'relatedTechName'), '=', lambda: e.get('param_techName'))
    assign(ref(this, 'counteredBy'), '=', lambda: e.get('param_counteredBy'))
    assign(ref(this, 'active'), '=', lambda: e.get('param_active'))
    assign(ref(this, 'maxKills'), '=', lambda: e.get('param_maxKills'))
    assign(ref(this, '_inStock'), '=', lambda: e.get('param_initStock'))
    assign(ref(this, 'maxStock'), '=', lambda: e.get('param_maxStock'))
    assign(ref(this, 'mcLinkage'), '=', lambda: e.get('param_mcLinkage'))
    assign(ref(this, 'inUse'), '=', lambda: e.get('param_inUse'))
    assign(ref(this, 'desireGroup'), '=', lambda: e.get('param_desireGroup'))
    assign(ref(this, 'prettyName'), '=', lambda: e.get('param_prettyName'))
    assign(ref(this, 'boughtInLastTurn'), '=', lambda: 0)
    assign(ref(this, 'bioloaded'), '=', lambda: False)
    assign(ref(this, 'explosion_mc_name'), '=', lambda: e.get('param_explosion_mc_name'))
    return U

def WeaponSlot_buy(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'WeaponSlot')
    assign(ref(this, 'inStock'), '=', lambda: binop('+', ref(this, 'inStock').get(), 1))
    assign(ref(this, 'boughtInLastTurn'), '=', lambda: binop('+', ref(this, 'boughtInLastTurn').get(), 1))
    return U

def WeaponSlot___set__inStock(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_nr'], ['_nr'], closure, 'WeaponSlot')
    assign(ref(this, '_inStock'), '=', lambda: e.get('_nr'))
    return U

def WeaponSlot___get__inStock(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'WeaponSlot')
    return ref(this, '_inStock').get()
    return U

def WeaponSlot_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'WeaponSlot')
    ref(this, 'preOrder').set(0)
    ref(this, 'inUse').set(0)

def register(rt):
    rt.define('WeaponSlot', None, WeaponSlot_fields, {'WeaponSlot': ASFunction(WeaponSlot_WeaponSlot), 'buy': ASFunction(WeaponSlot_buy)}, {'inStock': ASFunction(WeaponSlot___get__inStock)}, {'inStock': ASFunction(WeaponSlot___set__inStock)})
