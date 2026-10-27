# Generated from __Packages/WeaponStock.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def WeaponStock_WeaponStock(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'WeaponStock')
    e.set('_loc2_', 0)
    assign(ref(this, '_availableWeaponsArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, '_productionArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'roc1'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['rocket', 'carrier', 1, 'rocket1', update(e.ref('_loc2_'), 1, False), 5, 'rocket1', 'antiRocket', False, 0, 0, 100, 'lib_rocketMC', 0, 1, 'none', 'ROCKET (10 MEG)']))
    assign(ref(this, 'roc2'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['rocket', 'carrier', 2, 'rocket2', update(e.ref('_loc2_'), 1, False), 10, 'rocket2', 'antiRocket', False, 0, 0, 100, 'lib_rocketMC', 0, 1, 'none', 'ROCKET (25 MEG)']))
    assign(ref(this, 'roc3'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['rocket', 'carrier', 3, 'rocket3', update(e.ref('_loc2_'), 1, False), 15, 'rocket3', 'antiRocket', False, 0, 0, 100, 'lib_rocketMC', 0, 1, 'none', 'ROCKET (50 MEG)']))
    assign(ref(this, 'roc4'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['rocket', 'carrier', 4, 'rocket4', update(e.ref('_loc2_'), 1, False), 20, 'rocket4', 'antiRocket', False, 0, 0, 100, 'lib_rocketMC', 0, 1, 'none', 'ROCKET (95 MEG)']))
    assign(ref(this, 'war1'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['rocketload', 'payload', 1, 'warhead1', update(e.ref('_loc2_'), 1, False), 5, 'warhead1', 'none', False, 15, 0, 100, 'none', 0, 2, 'explosion_warhead_1', 'WARHEAD (10 MEG)']))
    assign(ref(this, 'war2'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['rocketload', 'payload', 2, 'warhead2', update(e.ref('_loc2_'), 1, False), 10, 'warhead2', 'none', False, 40, 0, 100, 'none', 0, 2, 'explosion_warhead_2', 'WARHEAD (25 MEG)']))
    assign(ref(this, 'war3'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['rocketload', 'payload', 3, 'warhead3', update(e.ref('_loc2_'), 1, False), 15, 'warhead3', 'none', False, 90, 0, 100, 'none', 0, 2, 'explosion_warhead_3', 'WARHEAD (50 MEG)']))
    assign(ref(this, 'war4'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['rocketload', 'payload', 4, 'warhead4', update(e.ref('_loc2_'), 1, False), 20, 'warhead4', 'none', False, 150, 0, 100, 'none', 0, 2, 'explosion_warhead_4', 'WARHEAD (95 MEG)']))
    assign(ref(this, 'bio1'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['rocketload', 'payload', 1, 'bioload1', update(e.ref('_loc2_'), 1, False), 5, 'bioload1', 'none', False, 10, 0, 100, 'none', 0, 3, 'explosion_bioload_1', 'BIOLOAD (10 MEG)']))
    assign(ref(this, 'bio2'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['rocketload', 'payload', 2, 'bioload2', update(e.ref('_loc2_'), 1, False), 10, 'bioload2', 'none', False, 35, 0, 100, 'none', 0, 3, 'explosion_bioload_2', 'BIOLOAD (25 MEG)']))
    assign(ref(this, 'bio3'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['rocketload', 'payload', 3, 'bioload3', update(e.ref('_loc2_'), 1, False), 15, 'bioload3', 'none', False, 60, 0, 100, 'none', 0, 3, 'explosion_bioload_3', 'BIOLOAD (50 MEG)']))
    assign(ref(this, 'bio4'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['rocketload', 'payload', 4, 'bioload4', update(e.ref('_loc2_'), 1, False), 20, 'bioload4', 'none', False, 80, 0, 100, 'none', 0, 3, 'explosion_bioload_4', 'BIOLOAD (95 MEG)']))
    assign(ref(this, 'sol1'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['soldier', 'conventional', 1, 'soldier1', update(e.ref('_loc2_'), 1, False), 5, 'soldier1', 'none', False, 4, 0, 100, 'lib_boat001', 0, 4, 'explosion_soldier_1', 'SOLDIER']))
    assign(ref(this, 'sol2'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['soldier', 'conventional', 2, 'soldier2', update(e.ref('_loc2_'), 1, False), 10, 'soldier2', 'none', False, 10, 0, 100, 'lib_soldier1MC', 0, 4, 'explosion_soldier_2', 'SEAL']))
    assign(ref(this, 'sol3'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['soldier', 'conventional', 3, 'soldier3', update(e.ref('_loc2_'), 1, False), 15, 'soldier3', 'none', False, 21, 0, 100, 'lib_soldier1MC', 0, 4, 'explosion_soldier_3', 'TANK']))
    assign(ref(this, 'sol4'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['soldier', 'conventional', 4, 'soldier4', update(e.ref('_loc2_'), 1, False), 20, 'soldier4', 'none', False, 35, 0, 100, 'lib_soldier1MC', 0, 4, 'explosion_soldier_4', 'SPECIAL UNIT']))
    assign(ref(this, 'spy1'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['spy', 'conventional', 1, 'spy1', update(e.ref('_loc2_'), 1, False), 5, 'spy1', 'none', False, 0, 1, 100, 'none', 0, 5, 'none', 'SPY (LEVEL 1)']))
    assign(ref(this, 'spy2'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['spy', 'conventional', 2, 'spy2', update(e.ref('_loc2_'), 1, False), 10, 'spy2', 'none', False, 0, 0, 100, 'none', 0, 5, 'none', 'SPY (LEVEL 2)']))
    assign(ref(this, 'spy3'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['spy', 'conventional', 3, 'spy3', update(e.ref('_loc2_'), 1, False), 15, 'spy3', 'none', False, 0, 0, 100, 'none', 0, 5, 'none', 'SPY (LEVEL 3)']))
    assign(ref(this, 'spy4'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['spy', 'conventional', 4, 'spy4', update(e.ref('_loc2_'), 1, False), 20, 'spy4', 'none', False, 0, 0, 100, 'none', 0, 5, 'none', 'SPY (LEVEL 4)']))
    assign(ref(this, 'plane1'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['plane', 'carrier', 2, 'plane1', update(e.ref('_loc2_'), 1, False), 5, 'plane1', 'antiAir', True, 0, 0, 100, 'lib_plane1MC', 0, 6, 'none', 'FIGHTER JET']))
    assign(ref(this, 'plane2'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['plane', 'carrier', 4, 'plane2', update(e.ref('_loc2_'), 1, False), 10, 'plane2', 'antiAir', False, 0, 0, 100, 'lib_plane2MC', 0, 6, 'none', 'BOMBER']))
    assign(ref(this, 'spe1'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['sub', 'specialCarrier', 3, 'sub', update(e.ref('_loc2_'), 1, False), 50, 'sub', 'none', False, 0, 0, 100, 'lib_carrierMC', 0, 7, 'none', 'SUBMARINE']))
    assign(ref(this, 'spe2'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['ship', 'specialCarrier', 3, 'ship', update(e.ref('_loc2_'), 1, False), 65, 'ship', 'antiAir', False, 0, 0, 100, 'lib_submarineMC', 0, 7, 'none', 'AIRCRAFT CARRIER']))
    assign(ref(this, 'spe3'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['space', 'specialCarrier', 3, 'space', update(e.ref('_loc2_'), 1, False), 70, 'space', 'none', False, 0, 0, 100, 'lib_spaceMC', 0, 7, 'none', 'SPACE ROCKET']))
    assign(ref(this, 'antiAir'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['anti', 'anti', 1, 'antiAir', update(e.ref('_loc2_'), 1, False), 15, 'antiAir', 'none', True, 1, 2, 100, 'none', 0, 8, 'none', 'ANTI AIR']))
    assign(ref(this, 'antiRocket'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['anti', 'anti', 1, 'antiRocket', update(e.ref('_loc2_'), 1, False), 15, 'antiRocket', 'none', True, 1, 2, 100, 'none', 0, 8, 'none', 'ANTI ROCKET']))
    assign(ref(this, 'specialLoad'), '=', lambda: rt.construct(e.get('WeaponSlot'), ['specialLoad', 'specialLoad', 4, 'specialLoad', update(e.ref('_loc2_'), 1, False), 80, 'specialLoad', 'none', False, 200000, 0, 100, 'lib_spaceMC', 0, 7, 'explosion_bioload_4', 'SATELLITE']))
    if truth(ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get()):
        assign(ref(this, 'roc3'), '=', lambda: e.get('undefined'))
        assign(ref(this, 'roc4'), '=', lambda: e.get('undefined'))
        assign(ref(this, 'war3'), '=', lambda: e.get('undefined'))
        assign(ref(this, 'war4'), '=', lambda: e.get('undefined'))
        assign(ref(this, 'sol3'), '=', lambda: e.get('undefined'))
        assign(ref(this, 'sol4'), '=', lambda: e.get('undefined'))
        assign(ref(this, 'bio3'), '=', lambda: e.get('undefined'))
        assign(ref(this, 'bio4'), '=', lambda: e.get('undefined'))
        assign(ref(this, 'spy3'), '=', lambda: e.get('undefined'))
        assign(ref(this, 'spy4'), '=', lambda: e.get('undefined'))
        assign(ref(this, 'plane2'), '=', lambda: e.get('undefined'))
        assign(ref(this, 'spe2'), '=', lambda: e.get('undefined'))
        assign(ref(this, 'spe3'), '=', lambda: e.get('undefined'))
        assign(ref(this, 'specialLoad'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'weaponArr'), '=', lambda: arr([ref(this, 'roc1').get(), ref(this, 'roc2').get(), ref(this, 'roc3').get(), ref(this, 'roc4').get(), ref(this, 'war1').get(), ref(this, 'war2').get(), ref(this, 'war3').get(), ref(this, 'war4').get(), ref(this, 'bio1').get(), ref(this, 'bio2').get(), ref(this, 'bio3').get(), ref(this, 'bio4').get(), ref(this, 'sol1').get(), ref(this, 'sol2').get(), ref(this, 'sol3').get(), ref(this, 'sol4').get(), ref(this, 'spy1').get(), ref(this, 'spy2').get(), ref(this, 'spy3').get(), ref(this, 'spy4').get(), ref(this, 'plane1').get(), ref(this, 'plane2').get(), ref(this, 'spe1').get(), ref(this, 'spe2').get(), ref(this, 'spe3').get(), ref(this, 'specialLoad').get()]))
    assign(ref(this, 'counterArr'), '=', lambda: arr([ref(this, 'antiAir').get(), ref(this, 'antiRocket').get()]))
    return U

def WeaponStock_getWeaponByID(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_id'], ['i', 'param_id'], closure, 'WeaponStock')
    for key_1 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_1)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponID').get(), e.get('param_id'))):
                return ref(ref(this, 'weaponArr').get(), e.get('i')).get()
        except ASContinue:
            pass
        except ASBreak:
            break
    if truth(binop('==', e.get('param_id'), ref(ref(this, 'antiAir').get(), 'weaponID').get())):
        return ref(this, 'antiAir').get()
    if truth(binop('==', e.get('param_id'), ref(ref(this, 'antiRocket').get(), 'weaponID').get())):
        return ref(this, 'antiRocket').get()
    return U

def WeaponStock_select_spy_by_level(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_lvl'], ['_lvl', 'i'], closure, 'WeaponStock')
    for key_2 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_2)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponName').get(), binop('+', 'spy', e.get('_lvl')))):
                return ref(ref(this, 'weaponArr').get(), e.get('i')).get()
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def WeaponStock_activeWeaponByTechName(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_name'], ['_loc3_', 'i', 'param_name'], closure, 'WeaponStock')
    for key_3 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_3)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(this, 'weaponArr').get(), e.get('i')).get())
            if truth(binop('==', ref(e.get('_loc3_'), 'relatedTechName').get(), e.get('param_name'))):
                assign(ref(e.get('_loc3_'), 'active'), '=', lambda: True)
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def WeaponStock_getWeaponByName(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_name'], ['i', 'param_name'], closure, 'WeaponStock')
    for key_4 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_4)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponName').get(), e.get('param_name'))):
                return ref(ref(this, 'weaponArr').get(), e.get('i')).get()
        except ASContinue:
            pass
        except ASBreak:
            break
    if truth(binop('==', e.get('param_name'), ref(ref(this, 'antiAir').get(), 'weaponName').get())):
        return ref(this, 'antiAir').get()
    if truth(binop('==', e.get('param_name'), ref(ref(this, 'antiRocket').get(), 'weaponName').get())):
        return ref(this, 'antiRocket').get()
    return U

def WeaponStock_produceWeaponByName(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_name', 'param_amount'], ['param_amount', 'param_name'], closure, 'WeaponStock')
    assign(ref(rt.call_ref(ref(this, 'getWeaponByName'), [e.get('param_name')]), 'inStock'), '=', lambda: binop('+', ref(rt.call_ref(ref(this, 'getWeaponByName'), [e.get('param_name')]), 'inStock').get(), e.get('param_amount')))
    return U

def WeaponStock_reduceWeaponByName(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_name', 'param_amount'], ['param_amount', 'param_name'], closure, 'WeaponStock')
    assign(ref(rt.call_ref(ref(this, 'getWeaponByName'), [e.get('param_name')]), 'inStock'), '=', lambda: binop('-', ref(rt.call_ref(ref(this, 'getWeaponByName'), [e.get('param_name')]), 'inStock').get(), e.get('param_amount')))
    return U

def WeaponStock_reduceWeaponByID(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_id', 'param_amount'], ['param_amount', 'param_id'], closure, 'WeaponStock')
    assign(ref(rt.call_ref(ref(this, 'getWeaponByID'), [e.get('param_id')]), 'inStock'), '=', lambda: binop('-', ref(rt.call_ref(ref(this, 'getWeaponByID'), [e.get('param_id')]), 'inStock').get(), e.get('param_amount')))
    return U

def WeaponStock_getAvailableCarrier(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['wp'], ['_loc3_', 'i', 'wp'], closure, 'WeaponStock')
    for key_5 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_5)
        rt.tick()
        try:
            if truth(logical('&&', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'active').get(), lambda: logical('&&', binop('>=', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponLevel').get(), ref(e.get('wp'), 'weaponLevel').get()), lambda: logical('&&', binop('>', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'inStock').get(), 0), lambda: binop('==', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponCategory').get(), 'carrier'))))):
                assign(e.ref('_loc3_'), '=', lambda: ref(ref(this, 'weaponArr').get(), e.get('i')).get())
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc3_')
    return U

def WeaponStock___get__allowPre(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'WeaponStock')
    for key_6 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_6)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(this, 'weaponArr').get(), e.get('i')).get())
            if truth(logical('&&', binop('>', ref(e.get('_loc2_'), 'inStock').get(), 0), lambda: logical('&&', ref(e.get('_loc2_'), 'active').get(), lambda: logical('||', binop('==', ref(e.get('_loc2_'), 'weaponCategory').get(), 'carrier'), lambda: binop('==', ref(e.get('_loc2_'), 'weaponCategory').get(), 'specialCarrier'))))):
                return True
        except ASContinue:
            pass
        except ASBreak:
            break
    return False
    return U

def WeaponStock___get__allowDir(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'WeaponStock')
    for key_7 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_7)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(this, 'weaponArr').get(), e.get('i')).get())
            if truth(logical('&&', binop('==', ref(e.get('_loc2_'), 'weaponCategory').get(), 'conventional'), lambda: logical('&&', binop('>', ref(e.get('_loc2_'), 'inStock').get(), 0), lambda: ref(e.get('_loc2_'), 'active').get()))):
                return True
        except ASContinue:
            pass
        except ASBreak:
            break
    return False
    return U

def WeaponStock___get__availableWeaponsArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'WeaponStock')
    assign(ref(this, '_availableWeaponsArr'), '=', lambda: arr([]))
    for key_8 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_8)
        rt.tick()
        try:
            if truth(logical('&&', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'active').get(), lambda: logical('&&', binop('>', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'inStock').get(), 0), lambda: logical('&&', binop('!=', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponType').get(), 'spy'), lambda: logical('&&', binop('!=', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponCategory').get(), 'carrier'), lambda: binop('!=', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponCategory').get(), 'specialCarrier')))))):
                if truth(binop('==', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponCategory').get(), 'payload')):
                    if truth(binop('>', ref(ref(this, binop('+', 'roc', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponLevel').get())).get(), 'inStock').get(), 0)):
                        rt.call_ref(ref(ref(this, '_availableWeaponsArr').get(), 'push'), [ref(ref(this, 'weaponArr').get(), e.get('i')).get()])
                    else:
                        if truth(logical('&&', binop('<=', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponLevel').get(), ref(ref(this, 'plane1').get(), 'weaponLevel').get()), lambda: binop('>', ref(ref(this, 'plane1').get(), 'inStock').get(), 0))):
                            rt.call_ref(ref(ref(this, '_availableWeaponsArr').get(), 'push'), [ref(ref(this, 'weaponArr').get(), e.get('i')).get()])
                        else:
                            if truth(logical('&&', binop('<=', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponLevel').get(), ref(ref(this, 'plane2').get(), 'weaponLevel').get()), lambda: binop('>', ref(ref(this, 'plane2').get(), 'inStock').get(), 0))):
                                rt.call_ref(ref(ref(this, '_availableWeaponsArr').get(), 'push'), [ref(ref(this, 'weaponArr').get(), e.get('i')).get()])
                            else:
                                if truth(logical('&&', binop('==', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponName').get(), 'ship'), lambda: logical('&&', binop('>', ref(ref(this, 'spe1').get(), 'inStock').get(), 0), lambda: ref(this, 'stocked_for_ship_attack').get()))):
                                    rt.call_ref(ref(ref(this, '_availableWeaponsArr').get(), 'push'), [ref(ref(this, 'weaponArr').get(), e.get('i')).get()])
                                else:
                                    if truth(logical('&&', binop('==', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponName').get(), 'sub'), lambda: logical('&&', binop('>', ref(ref(this, 'spe2').get(), 'inStock').get(), 0), lambda: ref(this, 'stocked_for_ship_attack').get()))):
                                        rt.call_ref(ref(ref(this, '_availableWeaponsArr').get(), 'push'), [ref(ref(this, 'weaponArr').get(), e.get('i')).get()])
                                    else:
                                        if truth(logical('&&', binop('<=', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponLevel').get(), ref(ref(this, 'spe2').get(), 'weaponLevel').get()), lambda: binop('>', ref(ref(this, 'spe2').get(), 'inStock').get(), 0))):
                                            rt.call_ref(ref(ref(this, '_availableWeaponsArr').get(), 'push'), [ref(ref(this, 'weaponArr').get(), e.get('i')).get()])
                                        else:
                                            if truth(logical('&&', binop('<=', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponLevel').get(), ref(ref(this, 'spe1').get(), 'weaponLevel').get()), lambda: binop('>', ref(ref(this, 'spe1').get(), 'inStock').get(), 0))):
                                                rt.call_ref(ref(ref(this, '_availableWeaponsArr').get(), 'push'), [ref(ref(this, 'weaponArr').get(), e.get('i')).get()])
                else:
                    if truth(logical('&&', binop('==', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponCategory').get(), 'specialLoad'), lambda: binop('>', ref(ref(this, 'spe3').get(), 'inStock').get(), 0))):
                        rt.call_ref(ref(ref(this, '_availableWeaponsArr').get(), 'push'), [ref(ref(this, 'weaponArr').get(), e.get('i')).get()])
                    else:
                        if truth(logical('&&', binop('!=', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponCategory').get(), 'specialLoad'), lambda: binop('!=', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponCategory').get(), 'payLoad'))):
                            rt.call_ref(ref(ref(this, '_availableWeaponsArr').get(), 'push'), [ref(ref(this, 'weaponArr').get(), e.get('i')).get()])
        except ASContinue:
            pass
        except ASBreak:
            break
    e.call('trace', [binop('+', ' available WeaponsArr : ', ref(this, '_availableWeaponsArr').get())])
    return ref(this, '_availableWeaponsArr').get()
    return U

def WeaponStock_payloadInStock(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_wpn'], ['_wpn'], closure, 'WeaponStock')
    if truth(logical('&&', binop('==', ref(e.get('_wpn'), 'weaponCategory').get(), 'payload'), lambda: binop('>', ref(e.get('_wpn'), 'inStock').get(), 0))):
        return True
    return False
    return U

def WeaponStock_get_MaxKillPayload(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['carrierWeapon'], ['_loc3_', '_loc4_', '_loc5_', '_loc6_', 'carrierWeapon', 'i'], closure, 'WeaponStock')
    e.set('_loc3_', 0)
    e.set('_loc4_', ref(this, 'instock_active_payloads').get())
    for key_9 in keys(e.get('_loc4_')):
        e.ref('i').set(key_9)
        rt.tick()
        try:
            assign(e.ref('_loc6_'), '=', lambda: ref(e.get('_loc4_'), e.get('i')).get())
            if truth(logical('&&', binop('>', ref(e.get('_loc6_'), 'maxKills').get(), e.get('_loc3_')), lambda: logical('&&', binop('<=', ref(e.get('_loc6_'), 'weaponLevel').get(), ref(e.get('carrierWeapon'), 'weaponLevel').get()), lambda: logical('&&', binop('!=', ref(e.get('carrierWeapon'), 'weaponName').get(), 'space'), lambda: logical('&&', binop('!=', ref(e.get('_loc6_'), 'weaponName').get(), 'specialLoad'), lambda: ref(e.get('_loc6_'), 'active').get()))))):
                assign(e.ref('_loc5_'), '=', lambda: e.get('_loc6_'))
                assign(e.ref('_loc3_'), '=', lambda: ref(e.get('_loc6_'), 'maxKills').get())
            else:
                if truth(logical('&&', binop('==', ref(e.get('carrierWeapon'), 'weaponName').get(), 'space'), lambda: logical('&&', binop('==', ref(e.get('_loc6_'), 'weaponName').get(), 'specialLoad'), lambda: logical('&&', binop('>', ref(e.get('_loc6_'), 'inStock').get(), 0), lambda: ref(e.get('_loc6_'), 'active').get())))):
                    assign(e.ref('_loc5_'), '=', lambda: e.get('_loc6_'))
                    assign(e.ref('_loc3_'), '=', lambda: binop('==', ref(e.get('_loc6_'), 'maxKills').get(), 2000))
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc5_')
    return U

def WeaponStock___get__stocked_for_ship_attack(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'WeaponStock')
    if truth(logical('||', binop('>', ref(ref(this, 'war1').get(), 'inStock').get(), 0), lambda: logical('||', binop('>', ref(ref(this, 'war2').get(), 'inStock').get(), 0), lambda: logical('||', binop('>', ref(ref(this, 'war3').get(), 'inStock').get(), 0), lambda: logical('||', binop('>', ref(ref(this, 'bio1').get(), 'inStock').get(), 0), lambda: logical('||', binop('>', ref(ref(this, 'bio2').get(), 'inStock').get(), 0), lambda: binop('>', ref(ref(this, 'bio3').get(), 'inStock').get(), 0))))))):
        return True
    return False
    return U

def WeaponStock_payloadAvailable(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_wpn'], ['_loc3_', '_loc4_', '_wpn', 'i'], closure, 'WeaponStock')
    e.set('_loc3_', False)
    for key_10 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_10)
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(this, 'weaponArr').get(), e.get('i')).get())
            if truth(logical('&&', binop('==', ref(e.get('_wpn'), 'weaponType').get(), 'rocket'), lambda: binop('>=', ref(e.get('_loc4_'), 'weaponLevel').get(), ref(e.get('_wpn'), 'weaponLevel').get()))):
                assign(e.ref('_loc3_'), '=', lambda: True)
            else:
                if truth(logical('&&', binop('==', ref(e.get('_wpn'), 'weaponType').get(), 'plane'), lambda: rt.call_ref(ref(this, 'payloadInStock'), [e.get('_loc4_')]))):
                    if truth(binop('>=', ref(e.get('_wpn'), 'weaponLevel').get(), ref(e.get('_loc4_'), 'weaponLevel').get())):
                        assign(e.ref('_loc3_'), '=', lambda: True)
                else:
                    if truth(logical('&&', binop('==', ref(e.get('_wpn'), 'weaponType').get(), 'sub'), lambda: rt.call_ref(ref(this, 'payloadInStock'), [e.get('_loc4_')]))):
                        assign(e.ref('_loc3_'), '=', lambda: True)
                    else:
                        if truth(logical('&&', binop('==', ref(e.get('_wpn'), 'weaponType').get(), 'ship'), lambda: rt.call_ref(ref(this, 'payloadInStock'), [e.get('_loc4_')]))):
                            assign(e.ref('_loc3_'), '=', lambda: True)
        except ASContinue:
            pass
        except ASBreak:
            break
    if truth(logical('&&', binop('==', ref(e.get('_wpn'), 'weaponType').get(), 'space'), lambda: binop('>', ref(ref(this, 'specialLoad').get(), 'inStock').get(), 0))):
        assign(e.ref('_loc3_'), '=', lambda: True)
    return e.get('_loc3_')
    return U

def WeaponStock___get__logicalCarrierArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'WeaponStock')
    assign(ref(this, '_logicalCarrierArr'), '=', lambda: arr([]))
    for key_11 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_11)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(this, 'weaponArr').get(), e.get('i')).get())
            if truth(logical('&&', rt.call_ref(ref(this, 'payloadAvailable'), [e.get('_loc2_')]), lambda: binop('>', ref(e.get('_loc2_'), 'inStock').get(), 0))):
                rt.call_ref(ref(ref(this, '_logicalCarrierArr').get(), 'push'), [e.get('_loc2_')])
        except ASContinue:
            pass
        except ASBreak:
            break
    return ref(this, '_logicalCarrierArr').get()
    return U

def WeaponStock___get__highWeaponCount(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', 'i'], closure, 'WeaponStock')
    e.set('_loc2_', 0)
    e.set('_loc3_', rt.construct(e.get('Array'), [e.get('undefined'), 0, 0, 0, 0]))
    e.set('_loc4_', 0)
    for key_12 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_12)
        rt.tick()
        try:
            assign(e.ref('_loc5_'), '=', lambda: ref(ref(this, 'weaponArr').get(), e.get('i')).get())
            if truth(binop('>', ref(e.get('_loc5_'), 'inStock').get(), 0)):
                update(ref(e.get('_loc3_'), ref(e.get('_loc5_'), 'weaponLevel').get()), 1, False)
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc6_', 0)
    while truth(binop('<', e.get('_loc6_'), 5)):
        rt.tick()
        try:
            if truth(binop('>=', ref(e.get('_loc3_'), e.get('_loc6_')).get(), e.get('_loc4_'))):
                assign(e.ref('_loc4_'), '=', lambda: ref(e.get('_loc3_'), e.get('_loc6_')).get())
                assign(e.ref('_loc2_'), '=', lambda: e.get('_loc6_'))
            assign(e.ref('_loc6_'), '=', lambda: binop('+', e.get('_loc6_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def WeaponStock___get__inStock_perLevel_obj(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'WeaponStock')
    e.set('_loc2_', rt.construct(e.get('Object'), []))
    assign(ref(e.get('_loc2_'), '_level1'), '=', lambda: 0)
    assign(ref(e.get('_loc2_'), '_level2'), '=', lambda: 0)
    assign(ref(e.get('_loc2_'), '_level3'), '=', lambda: 0)
    assign(ref(e.get('_loc2_'), '_level4'), '=', lambda: 0)
    for key_13 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_13)
        rt.tick()
        try:
            assign(ref(e.get('_loc2_'), binop('+', '_level', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponLevel').get())), '+=', lambda: ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'inStock').get())
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def WeaponStock___get__spyAvailable(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'WeaponStock')
    for key_14 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_14)
        rt.tick()
        try:
            if truth(logical('&&', binop('==', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponType').get(), 'spy'), lambda: logical('&&', binop('>', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'inStock').get(), 0), lambda: ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'active').get()))):
                return True
        except ASContinue:
            pass
        except ASBreak:
            break
    return False
    return U

def WeaponStock_activateAll(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_amount'], ['_amount', '_loc3_', '_loc4_', 'i'], closure, 'WeaponStock')
    e.set('_loc3_', logical('||', e.get('_amount'), lambda: 1))
    for key_15 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_15)
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(this, 'weaponArr').get(), e.get('i')).get())
            assign(ref(e.get('_loc4_'), 'active'), '=', lambda: True)
            assign(ref(e.get('_loc4_'), 'bioloaded'), '=', lambda: False)
            assign(ref(e.get('_loc4_'), 'inStock'), '=', lambda: e.get('_loc3_'))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def WeaponStock___get__availableSpies_obj(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', 'i'], closure, 'WeaponStock')
    e.set('_loc2_', rt.construct(e.get('Object'), []))
    assign(ref(e.get('_loc2_'), '_level1'), '=', lambda: 0)
    assign(ref(e.get('_loc2_'), '_level2'), '=', lambda: 0)
    assign(ref(e.get('_loc2_'), '_level3'), '=', lambda: 0)
    assign(ref(e.get('_loc2_'), '_level4'), '=', lambda: 0)
    for key_16 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_16)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(this, 'weaponArr').get(), e.get('i')).get())
            if truth(binop('==', ref(e.get('_loc3_'), 'weaponType').get(), 'spy')):
                assign(ref(e.get('_loc2_'), binop('+', '_level', ref(e.get('_loc3_'), 'weaponLevel').get())), '+=', lambda: ref(e.get('_loc3_'), 'inStock').get())
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def WeaponStock_get_highest_spy_level(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_'], closure, 'WeaponStock')
    e.set('_loc2_', 0)
    e.set('_loc3_', 0)
    while truth(binop('<', e.get('_loc3_'), ref(ref(this, 'weaponArr').get(), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(this, 'weaponArr').get(), e.get('_loc3_')).get())
            if truth(logical('&&', binop('==', ref(e.get('_loc4_'), 'weaponType').get(), 'spy'), lambda: logical('&&', binop('>', ref(e.get('_loc4_'), 'inStock').get(), 0), lambda: ref(e.get('_loc4_'), 'active').get()))):
                if truth(binop('>', ref(e.get('_loc4_'), 'weaponLevel').get(), e.get('_loc2_'))):
                    assign(e.ref('_loc2_'), '=', lambda: ref(e.get('_loc4_'), 'weaponLevel').get())
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def WeaponStock___get__instock_active_payloads(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', 'i'], closure, 'WeaponStock')
    e.set('_loc2_', rt.construct(e.get('Array'), []))
    for key_17 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_17)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(this, 'weaponArr').get(), e.get('i')).get())
            if truth(logical('&&', logical('||', binop('==', ref(e.get('_loc3_'), 'weaponCategory').get(), 'payload'), lambda: binop('==', ref(e.get('_loc3_'), 'weaponCategory').get(), 'specialLoad')), lambda: logical('&&', binop('>', ref(e.get('_loc3_'), 'inStock').get(), 0), lambda: ref(e.get('_loc3_'), 'active').get()))):
                rt.call_ref(ref(e.get('_loc2_'), 'push'), [e.get('_loc3_')])
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def WeaponStock___get__instock_active_payloads_perStock(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', 'i'], closure, 'WeaponStock')
    e.set('_loc2_', rt.construct(e.get('Array'), []))
    for key_18 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_18)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(this, 'weaponArr').get(), e.get('i')).get())
            if truth(logical('&&', logical('||', binop('==', ref(e.get('_loc3_'), 'weaponCategory').get(), 'payload'), lambda: binop('==', ref(e.get('_loc3_'), 'weaponCategory').get(), 'specialLoad')), lambda: logical('&&', binop('>', ref(e.get('_loc3_'), 'inStock').get(), 0), lambda: ref(e.get('_loc3_'), 'active').get()))):
                assign(e.ref('_loc4_'), '=', lambda: 0)
                while truth(binop('<', e.get('_loc4_'), ref(e.get('_loc3_'), 'inStock').get())):
                    rt.tick()
                    try:
                        rt.call_ref(ref(e.get('_loc2_'), 'push'), [e.get('_loc3_')])
                        assign(e.ref('_loc4_'), '=', lambda: binop('+', e.get('_loc4_'), 1))
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def WeaponStock___get__randomAvailableCarrier(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', 'i'], closure, 'WeaponStock')
    e.set('_loc2_', rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [1, 3]))
    e.set('_loc3_', rt.construct(e.get('Object'), []))
    assign(ref(e.get('_loc3_'), 'rocket'), '=', lambda: False)
    assign(ref(e.get('_loc3_'), 'plane'), '=', lambda: False)
    assign(ref(e.get('_loc3_'), 'sub'), '=', lambda: False)
    assign(ref(e.get('_loc3_'), 'ship'), '=', lambda: False)
    assign(ref(e.get('_loc3_'), 'space'), '=', lambda: False)
    e.set('_loc4_', rt.construct(e.get('Array'), []))
    e.set('_loc5_', '')
    for key_19 in keys(ref(this, 'logicalCarrierArr').get()):
        e.ref('i').set(key_19)
        rt.tick()
        try:
            assign(e.ref('_loc6_'), '=', lambda: ref(ref(this, 'logicalCarrierArr').get(), e.get('i')).get())
            switch_20 = ref(e.get('_loc6_'), 'weaponType').get()
            case_21 = -1
            if case_21 == -1 and strict_eq(switch_20, 'rocket'):
                case_21 = 0
            if case_21 == -1 and strict_eq(switch_20, 'plane'):
                case_21 = 1
            if case_21 == -1 and strict_eq(switch_20, 'sub'):
                case_21 = 2
            if case_21 == -1 and strict_eq(switch_20, 'ship'):
                case_21 = 3
            if case_21 == -1 and strict_eq(switch_20, 'space'):
                case_21 = 4
            if case_21 == -1:
                case_21 = -1
            try:
                if 0 <= case_21 <= 0:
                    assign(ref(e.get('_loc3_'), 'rocket'), '=', lambda: True)
                    raise ASBreak()
                if 0 <= case_21 <= 1:
                    assign(ref(e.get('_loc3_'), 'plane'), '=', lambda: True)
                    raise ASBreak()
                if 0 <= case_21 <= 2:
                    assign(ref(e.get('_loc3_'), 'sub'), '=', lambda: True)
                    raise ASBreak()
                if 0 <= case_21 <= 3:
                    assign(ref(e.get('_loc3_'), 'ship'), '=', lambda: True)
                    raise ASBreak()
                if 0 <= case_21 <= 4:
                    assign(ref(e.get('_loc3_'), 'space'), '=', lambda: True)
            except ASBreak:
                pass
        except ASContinue:
            pass
        except ASBreak:
            break
    if truth(binop('==', ref(e.get('_loc3_'), 'rocket').get(), True)):
        rt.call_ref(ref(e.get('_loc4_'), 'push'), ['rocket'])
    if truth(binop('==', ref(e.get('_loc3_'), 'plane').get(), True)):
        rt.call_ref(ref(e.get('_loc4_'), 'push'), ['plane'])
    if truth(binop('==', ref(e.get('_loc3_'), 'sub').get(), True)):
        rt.call_ref(ref(e.get('_loc4_'), 'push'), ['sub'])
    if truth(binop('==', ref(e.get('_loc3_'), 'ship').get(), True)):
        rt.call_ref(ref(e.get('_loc4_'), 'push'), ['ship'])
    if truth(binop('==', ref(e.get('_loc3_'), 'space').get(), True)):
        rt.call_ref(ref(e.get('_loc4_'), 'push'), ['space'])
    assign(e.ref('_loc5_'), '=', lambda: ref(e.get('_loc4_'), rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [0, binop('-', ref(e.get('_loc4_'), 'length').get(), 1)])).get())
    e.set('_loc7_', 0)
    for key_22 in keys(ref(this, 'logicalCarrierArr').get()):
        e.ref('i').set(key_22)
        rt.tick()
        try:
            assign(e.ref('_loc8_'), '=', lambda: ref(ref(this, 'logicalCarrierArr').get(), e.get('i')).get())
            if truth(logical('&&', binop('==', ref(e.get('_loc8_'), 'weaponType').get(), e.get('_loc5_')), lambda: binop('<', e.get('_loc7_'), ref(e.get('_loc8_'), 'weaponLevel').get()))):
                return e.get('_loc8_')
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def WeaponStock___get__weaponStocklevel(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'WeaponStock')
    return U

def WeaponStock___get__productionArray(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', 'i'], closure, 'WeaponStock')
    e.set('_loc2_', rt.construct(e.get('Array'), []))
    for key_23 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_23)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(this, 'weaponArr').get(), e.get('i')).get())
            if truth(binop('>', ref(e.get('_loc3_'), 'preOrder').get(), 0)):
                rt.call_ref(ref(e.get('_loc2_'), 'push'), [obj({'weapon': e.get('_loc3_'), 'amount': ref(e.get('_loc3_'), 'preOrder').get()})])
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_24 in keys(ref(this, 'counterArr').get()):
        e.ref('i').set(key_24)
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(this, 'counterArr').get(), e.get('i')).get())
            if truth(binop('>', ref(e.get('_loc4_'), 'preOrder').get(), 0)):
                rt.call_ref(ref(e.get('_loc2_'), 'push'), [obj({'weapon': e.get('_loc4_'), 'amount': ref(e.get('_loc4_'), 'preOrder').get()})])
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def WeaponStock___get__production_money_spent(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'WeaponStock')
    e.set('_loc2_', 0)
    for key_25 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_25)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '+=', lambda: binop('*', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'preOrder').get(), ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'cost').get()))
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(e.ref('_loc2_'), '+=', lambda: binop('*', ref(ref(this, 'antiAir').get(), 'preOrder').get(), ref(ref(this, 'antiAir').get(), 'cost').get()))
    assign(e.ref('_loc2_'), '+=', lambda: binop('*', ref(ref(this, 'antiRocket').get(), 'preOrder').get(), ref(ref(this, 'antiRocket').get(), 'cost').get()))
    return e.get('_loc2_')
    return U

def WeaponStock_resetPreOrder(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'WeaponStock')
    for key_26 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_26)
        rt.tick()
        try:
            assign(ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'preOrder'), '=', lambda: 0)
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(ref(this, 'antiAir').get(), 'preOrder'), '=', lambda: 0)
    assign(ref(ref(this, 'antiRocket').get(), 'preOrder'), '=', lambda: 0)
    return U

def WeaponStock_resetInUse(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'WeaponStock')
    for key_27 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_27)
        rt.tick()
        try:
            assign(ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'inUse'), '=', lambda: 0)
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(ref(this, 'antiAir').get(), 'inUse'), '=', lambda: 0)
    assign(ref(ref(this, 'antiRocket').get(), 'inUse'), '=', lambda: 0)
    return U

def WeaponStock___get__highestRocketLoad(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'WeaponStock')
    e.set('_loc2_', 0)
    for key_28 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_28)
        rt.tick()
        try:
            if truth(logical('&&', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'active').get(), lambda: binop('>', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'weaponLevel').get(), ref(e.get('_loc2_'), 'weaponLevel').get()))):
                assign(e.ref('_loc2_'), '=', lambda: ref(ref(this, 'weaponArr').get(), e.get('i')).get())
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def WeaponStock___set__boughtMSG(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str'], closure, 'WeaponStock')
    return U

def WeaponStock___get__boughtMSG(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', 'i'], closure, 'WeaponStock')
    e.set('_loc2_', binop('+', 'Weapons produced: ', ' <br />'))
    e.set('_loc3_', False)
    for key_29 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_29)
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(this, 'weaponArr').get(), e.get('i')).get())
            if truth(binop('>', ref(e.get('_loc4_'), 'boughtInLastTurn').get(), 0)):
                if truth(unary('!', e.get('_loc3_'))):
                    assign(e.ref('_loc3_'), '=', lambda: True)
                    assign(e.ref('_loc2_'), '+=', lambda: binop('+', binop('+', binop('+', binop('+', ' -- ', ref(e.get('_loc4_'), 'prettyName').get()), ' x'), ref(e.get('_loc4_'), 'boughtInLastTurn').get()), ' <br />'))
                else:
                    assign(e.ref('_loc2_'), '+=', lambda: binop('+', binop('+', binop('+', binop('+', ' -- ', ref(e.get('_loc4_'), 'prettyName').get()), ' x'), ref(e.get('_loc4_'), 'boughtInLastTurn').get()), ' <br />'))
        except ASContinue:
            pass
        except ASBreak:
            break
    if truth(binop('>', ref(ref(this, 'antiAir').get(), 'boughtInLastTurn').get(), 0)):
        if truth(unary('!', e.get('_loc3_'))):
            assign(e.ref('_loc3_'), '=', lambda: True)
            assign(e.ref('_loc2_'), '+=', lambda: binop('+', binop('+', binop('+', binop('+', ' -- ', 'Anti Aircraft'), ' x'), ref(ref(this, 'antiAir').get(), 'boughtInLastTurn').get()), ' <br />'))
        else:
            assign(e.ref('_loc2_'), '+=', lambda: binop('+', binop('+', binop('+', binop('+', ' -- ', 'Anti Aircraft'), ' x'), ref(ref(this, 'antiAir').get(), 'boughtInLastTurn').get()), ' <br />'))
    if truth(binop('>', ref(ref(this, 'antiRocket').get(), 'boughtInLastTurn').get(), 0)):
        if truth(unary('!', e.get('_loc3_'))):
            assign(e.ref('_loc3_'), '=', lambda: True)
            assign(e.ref('_loc2_'), '+=', lambda: binop('+', binop('+', binop('+', binop('+', ' -- ', 'Anti Rocket'), ' x'), ref(ref(this, 'antiRocket').get(), 'boughtInLastTurn').get()), ' <br />'))
        else:
            assign(e.ref('_loc2_'), '+=', lambda: binop('+', binop('+', binop('+', binop('+', ' -- ', 'Anti Rocket'), ' x'), ref(ref(this, 'antiRocket').get(), 'boughtInLastTurn').get()), ' <br />'))
    if truth(e.get('_loc3_')):
        return e.get('_loc2_')
    return ''
    return U

def WeaponStock_removeBioload(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'WeaponStock')
    for key_30 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_30)
        rt.tick()
        try:
            if truth(ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'bioloaded').get()):
                assign(ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'active'), '=', lambda: True)
                assign(ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'bioloaded'), '=', lambda: False)
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def WeaponStock_resetBought(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'WeaponStock')
    for key_31 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_31)
        rt.tick()
        try:
            assign(ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'boughtInLastTurn'), '=', lambda: 0)
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(ref(this, 'antiAir').get(), 'boughtInLastTurn'), '=', lambda: 0)
    assign(ref(ref(this, 'antiRocket').get(), 'boughtInLastTurn'), '=', lambda: 0)
    return U

def WeaponStock_is_activeCategory(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_num'], ['_num', 'i'], closure, 'WeaponStock')
    for key_32 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_32)
        rt.tick()
        try:
            if truth(logical('&&', binop('==', ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'desireGroup').get(), e.get('_num')), lambda: ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'active').get())):
                return True
        except ASContinue:
            pass
        except ASBreak:
            break
    return False
    return U

def WeaponStock_active_dCat_count(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_'], closure, 'WeaponStock')
    e.set('_loc2_', 0)
    e.set('_loc3_', 0)
    while truth(binop('<', e.get('_loc3_'), 8)):
        rt.tick()
        try:
            if truth(rt.call_ref(ref(this, 'is_activeCategory'), [e.get('_loc3_')])):
                assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def WeaponStock_set_wpn_stock_per_level(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_level', 'a_stock'], ['_loc4_', 'a_level', 'a_stock', 'i'], closure, 'WeaponStock')
    for key_33 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_33)
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(this, 'weaponArr').get(), e.get('i')).get())
            if truth(binop('==', ref(e.get('_loc4_'), 'weaponLevel').get(), e.get('a_level'))):
                assign(ref(e.get('_loc4_'), 'inStock'), '=', lambda: e.get('a_stock'))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def WeaponStock_set_easy_wpn_stock(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'WeaponStock')
    return U

def WeaponStock_max_stock(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'WeaponStock')
    for key_34 in keys(ref(this, 'weaponArr').get()):
        e.ref('i').set(key_34)
        rt.tick()
        try:
            if truth(ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'active').get()):
                assign(ref(ref(ref(this, 'weaponArr').get(), e.get('i')).get(), 'inStock'), '=', lambda: 4)
            assign(ref(ref(ref(this, 'counterArr').get(), 0).get(), 'inStock'), '=', lambda: 4)
            assign(ref(ref(ref(this, 'counterArr').get(), 1).get(), 'inStock'), '=', lambda: 4)
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def WeaponStock_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'WeaponStock')
    pass

def register(rt):
    rt.define('WeaponStock', None, WeaponStock_fields, {'WeaponStock': ASFunction(WeaponStock_WeaponStock), 'getWeaponByID': ASFunction(WeaponStock_getWeaponByID), 'select_spy_by_level': ASFunction(WeaponStock_select_spy_by_level), 'activeWeaponByTechName': ASFunction(WeaponStock_activeWeaponByTechName), 'getWeaponByName': ASFunction(WeaponStock_getWeaponByName), 'produceWeaponByName': ASFunction(WeaponStock_produceWeaponByName), 'reduceWeaponByName': ASFunction(WeaponStock_reduceWeaponByName), 'reduceWeaponByID': ASFunction(WeaponStock_reduceWeaponByID), 'getAvailableCarrier': ASFunction(WeaponStock_getAvailableCarrier), 'payloadInStock': ASFunction(WeaponStock_payloadInStock), 'get_MaxKillPayload': ASFunction(WeaponStock_get_MaxKillPayload), 'payloadAvailable': ASFunction(WeaponStock_payloadAvailable), 'activateAll': ASFunction(WeaponStock_activateAll), 'get_highest_spy_level': ASFunction(WeaponStock_get_highest_spy_level), 'resetPreOrder': ASFunction(WeaponStock_resetPreOrder), 'resetInUse': ASFunction(WeaponStock_resetInUse), 'removeBioload': ASFunction(WeaponStock_removeBioload), 'resetBought': ASFunction(WeaponStock_resetBought), 'is_activeCategory': ASFunction(WeaponStock_is_activeCategory), 'active_dCat_count': ASFunction(WeaponStock_active_dCat_count), 'set_wpn_stock_per_level': ASFunction(WeaponStock_set_wpn_stock_per_level), 'set_easy_wpn_stock': ASFunction(WeaponStock_set_easy_wpn_stock), 'max_stock': ASFunction(WeaponStock_max_stock)}, {'allowPre': ASFunction(WeaponStock___get__allowPre), 'allowDir': ASFunction(WeaponStock___get__allowDir), 'availableWeaponsArr': ASFunction(WeaponStock___get__availableWeaponsArr), 'stocked_for_ship_attack': ASFunction(WeaponStock___get__stocked_for_ship_attack), 'logicalCarrierArr': ASFunction(WeaponStock___get__logicalCarrierArr), 'highWeaponCount': ASFunction(WeaponStock___get__highWeaponCount), 'inStock_perLevel_obj': ASFunction(WeaponStock___get__inStock_perLevel_obj), 'spyAvailable': ASFunction(WeaponStock___get__spyAvailable), 'availableSpies_obj': ASFunction(WeaponStock___get__availableSpies_obj), 'instock_active_payloads': ASFunction(WeaponStock___get__instock_active_payloads), 'instock_active_payloads_perStock': ASFunction(WeaponStock___get__instock_active_payloads_perStock), 'randomAvailableCarrier': ASFunction(WeaponStock___get__randomAvailableCarrier), 'weaponStocklevel': ASFunction(WeaponStock___get__weaponStocklevel), 'productionArray': ASFunction(WeaponStock___get__productionArray), 'production_money_spent': ASFunction(WeaponStock___get__production_money_spent), 'highestRocketLoad': ASFunction(WeaponStock___get__highestRocketLoad), 'boughtMSG': ASFunction(WeaponStock___get__boughtMSG)}, {'boughtMSG': ASFunction(WeaponStock___set__boughtMSG)})
