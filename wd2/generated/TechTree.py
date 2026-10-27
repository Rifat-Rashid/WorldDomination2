# Generated from __Packages/TechTree.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def TechTree_TechTree(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc14_', '_loc15_', '_loc16_', '_loc17_', '_loc18_', '_loc19_', '_loc20_', '_loc21_', '_loc22_', '_loc23_', '_loc24_', '_loc25_', '_loc26_', '_loc27_', '_loc28_', '_loc29_', '_loc2_', '_loc30_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_'], closure, 'TechTree')
    e.set('_loc2_', 1)
    e.set('_loc3_', rt.construct(e.get('Tech'), ['rocket1', e.get('_loc2_'), 5, False, 0, e.get('undefined'), 1, 1, 'ROCKET (10 MEG)', True]))
    e.set('_loc4_', rt.construct(e.get('Tech'), ['rocket2', update(e.ref('_loc2_'), 1, False), 10, False, 3, e.get('_loc3_'), 1, 2, 'ROCKET (25 MEG)', True]))
    e.set('_loc5_', rt.construct(e.get('Tech'), ['rocket3', update(e.ref('_loc2_'), 1, False), 15, False, 5, e.get('_loc4_'), 1, 3, 'ROCKET (50 MEG)', False]))
    e.set('_loc6_', rt.construct(e.get('Tech'), ['rocket4', update(e.ref('_loc2_'), 1, False), 20, False, 8, e.get('_loc5_'), 1, 4, 'ROCKET (95 MEG)', False]))
    e.set('_loc7_', rt.construct(e.get('Tech'), ['warhead1', update(e.ref('_loc2_'), 1, False), 5, False, 0, e.get('undefined'), 2, 1, 'WARHEAD (10 MEG)', True]))
    e.set('_loc8_', rt.construct(e.get('Tech'), ['warhead2', update(e.ref('_loc2_'), 1, False), 10, False, 3, e.get('_loc7_'), 2, 2, 'WARHEAD (25 MEG)', True]))
    e.set('_loc9_', rt.construct(e.get('Tech'), ['warhead3', update(e.ref('_loc2_'), 1, False), 15, False, 5, e.get('_loc8_'), 2, 3, 'WARHEAD (50 MEG)', False]))
    e.set('_loc10_', rt.construct(e.get('Tech'), ['warhead4', update(e.ref('_loc2_'), 1, False), 20, False, 8, e.get('_loc9_'), 2, 4, 'WARHEAD (95 MEG)', False]))
    e.set('_loc11_', rt.construct(e.get('Tech'), ['bioload1', update(e.ref('_loc2_'), 1, False), 5, False, 0, e.get('undefined'), 3, 1, 'BIOLOAD (10 MEG)', True]))
    e.set('_loc12_', rt.construct(e.get('Tech'), ['bioload2', update(e.ref('_loc2_'), 1, False), 10, False, 3, e.get('_loc11_'), 3, 2, 'BIOLOAD (25 MEG)', True]))
    e.set('_loc13_', rt.construct(e.get('Tech'), ['bioload3', update(e.ref('_loc2_'), 1, False), 15, False, 5, e.get('_loc12_'), 3, 3, 'BIOLOAD (50 MEG)', False]))
    e.set('_loc14_', rt.construct(e.get('Tech'), ['bioload4', update(e.ref('_loc2_'), 1, False), 20, False, 8, e.get('_loc13_'), 3, 4, 'BIOLOAD (95 MEG)', False]))
    e.set('_loc15_', rt.construct(e.get('Tech'), ['soldier1', update(e.ref('_loc2_'), 1, False), 5, False, 0, e.get('undefined'), 4, 1, 'SOLDIER', True]))
    e.set('_loc16_', rt.construct(e.get('Tech'), ['soldier2', update(e.ref('_loc2_'), 1, False), 10, False, 3, e.get('_loc15_'), 4, 2, 'SEALS', True]))
    e.set('_loc17_', rt.construct(e.get('Tech'), ['soldier3', update(e.ref('_loc2_'), 1, False), 15, False, 5, e.get('_loc16_'), 4, 3, 'TANK', False]))
    e.set('_loc18_', rt.construct(e.get('Tech'), ['soldier4', update(e.ref('_loc2_'), 1, False), 20, False, 8, e.get('_loc17_'), 4, 4, 'SPECIAL', False]))
    e.set('_loc19_', rt.construct(e.get('Tech'), ['spy1', update(e.ref('_loc2_'), 1, False), 5, False, 0, e.get('undefined'), 5, 1, 'SPY (LEVEL 1)', True]))
    e.set('_loc20_', rt.construct(e.get('Tech'), ['spy2', update(e.ref('_loc2_'), 1, False), 10, False, 3, e.get('_loc19_'), 5, 2, 'SPY (LEVEL 2)', True]))
    e.set('_loc21_', rt.construct(e.get('Tech'), ['spy3', update(e.ref('_loc2_'), 1, False), 15, False, 5, e.get('_loc20_'), 5, 3, 'SPY (LEVEL 3)', False]))
    e.set('_loc22_', rt.construct(e.get('Tech'), ['spy4', update(e.ref('_loc2_'), 1, False), 20, False, 8, e.get('_loc21_'), 5, 4, 'SPY (LEVEL 4)', False]))
    e.set('_loc23_', rt.construct(e.get('Tech'), ['plane1', update(e.ref('_loc2_'), 1, False), 5, False, 0, e.get('undefined'), 6, 1, 'FIGHTER', True]))
    e.set('_loc24_', rt.construct(e.get('Tech'), ['plane2', update(e.ref('_loc2_'), 1, False), 10, False, 4, e.get('_loc23_'), 6, 2, 'BOMBER', False]))
    e.set('_loc25_', rt.construct(e.get('Tech'), ['sub', update(e.ref('_loc2_'), 1, False), 20, False, 3, e.get('undefined'), 7, 1, 'SUBMARINE', True]))
    e.set('_loc26_', rt.construct(e.get('Tech'), ['ship', update(e.ref('_loc2_'), 1, False), 40, False, 5, e.get('_loc25_'), 7, 2, 'AIRCRAFT CARRIER', False]))
    e.set('_loc27_', rt.construct(e.get('Tech'), ['space', update(e.ref('_loc2_'), 1, False), 50, False, 8, e.get('_loc26_'), 7, 3, 'SPACE ROCKET', False]))
    e.set('_loc28_', rt.construct(e.get('Tech'), ['antiAir', update(e.ref('_loc2_'), 1, False), 20, True, 8, e.get('undefined'), 8, 1, 'ANTI AIR', True]))
    e.set('_loc29_', rt.construct(e.get('Tech'), ['antiRocket', update(e.ref('_loc2_'), 1, False), 20, True, 8, e.get('undefined'), 8, 1, 'ANTI ROCKET', True]))
    e.set('_loc30_', rt.construct(e.get('Tech'), ['specialLoad', update(e.ref('_loc2_'), 1, False), 50, False, 8, e.get('_loc27_'), 7, 4, 'SATELLITE', False]))
    if truth(ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get()):
        e.get('_loc5_')
        e.get('_loc6_')
        e.get('_loc9_')
        e.get('_loc10_')
        e.get('_loc17_')
        e.get('_loc18_')
        e.get('_loc13_')
        e.get('_loc14_')
        e.get('_loc21_')
        e.get('_loc22_')
        e.get('_loc24_')
        e.get('_loc26_')
        e.get('_loc27_')
        e.get('_loc30_')
    assign(ref(this, 'techArr'), '=', lambda: arr([e.get('_loc3_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), e.get('_loc8_'), e.get('_loc9_'), e.get('_loc10_'), e.get('_loc11_'), e.get('_loc12_'), e.get('_loc13_'), e.get('_loc14_'), e.get('_loc15_'), e.get('_loc16_'), e.get('_loc17_'), e.get('_loc18_'), e.get('_loc19_'), e.get('_loc20_'), e.get('_loc21_'), e.get('_loc22_'), e.get('_loc23_'), e.get('_loc24_'), e.get('_loc25_'), e.get('_loc26_'), e.get('_loc27_'), e.get('_loc28_'), e.get('_loc29_'), e.get('_loc30_')]))
    return U

def TechTree_inventAll(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'TechTree')
    for key_1 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_1)
        rt.tick()
        try:
            assign(ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'invented'), '=', lambda: True)
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def TechTree_inventTechByID(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_id'], ['i', 'param_id'], closure, 'TechTree')
    for key_2 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_2)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'techID').get(), e.get('param_id'))):
                if truth(binop('==', ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'invented').get(), False)):
                    assign(ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'invented'), '=', lambda: True)
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def TechTree_inventTechByName(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_name'], ['i', 'param_name'], closure, 'TechTree')
    for key_3 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_3)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'techName').get(), e.get('param_name'))):
                if truth(binop('==', ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'invented').get(), False)):
                    assign(ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'invented'), '=', lambda: True)
                    return 'success'
                return 'tech already invented...'
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def TechTree_unInventTechByName(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_name'], ['i', 'param_name'], closure, 'TechTree')
    for key_4 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_4)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'techName').get(), e.get('param_name'))):
                if truth(binop('==', ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'invented').get(), True)):
                    assign(ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'invented'), '=', lambda: False)
                    return 'success'
                return 'tech already unInvented...'
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def TechTree_unInventTechByID(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_id'], ['i', 'param_id'], closure, 'TechTree')
    for key_5 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_5)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'techID').get(), e.get('param_id'))):
                if truth(binop('==', ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'invented').get(), False)):
                    assign(ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'invented'), '=', lambda: True)
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def TechTree___get__turnTechArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', 'i'], closure, 'TechTree')
    e.set('_loc2_', rt.construct(e.get('Array'), []))
    for key_6 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_6)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(this, 'techArr').get(), e.get('i')).get())
            if truth(ref(e.get('_loc3_'), 'preOrder').get()):
                rt.call_ref(ref(e.get('_loc2_'), 'push'), [e.get('_loc3_')])
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def TechTree___get__researchMoneySpent(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'TechTree')
    e.set('_loc2_', 0)
    for key_7 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_7)
        rt.tick()
        try:
            if truth(ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'preOrder').get()):
                assign(e.ref('_loc2_'), '+=', lambda: ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'cost').get())
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def TechTree___set__researchMoneySpent(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'TechTree')
    return U

def TechTree_resetPreOrder(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'TechTree')
    for key_8 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_8)
        rt.tick()
        try:
            assign(ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'preOrder'), '=', lambda: False)
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def TechTree_getTechByID(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_nr'], ['i', 'param_nr'], closure, 'TechTree')
    for key_9 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_9)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'techID').get(), e.get('param_nr'))):
                return ref(ref(this, 'techArr').get(), e.get('i')).get()
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def TechTree_getTechByName(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_name'], ['i', 'param_name'], closure, 'TechTree')
    for key_10 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_10)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'techName').get(), e.get('param_name'))):
                return ref(ref(this, 'techArr').get(), e.get('i')).get()
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def TechTree___get__allInvented(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'TechTree')
    e.set('_loc2_', True)
    for key_11 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_11)
        rt.tick()
        try:
            if truth(unary('!', ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'invented').get())):
                assign(e.ref('_loc2_'), '=', lambda: False)
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def TechTree___get__cheapestUninventedTech(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', 'i'], closure, 'TechTree')
    e.set('_loc3_', 9000)
    for key_12 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_12)
        rt.tick()
        try:
            if truth(binop('<', ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'cost').get(), e.get('_loc3_'))):
                assign(e.ref('_loc2_'), '=', lambda: ref(ref(this, 'techArr').get(), e.get('i')).get())
                assign(e.ref('_loc3_'), '=', lambda: ref(e.get('_loc2_'), 'cost').get())
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def TechTree___get__techLevel(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'TechTree')
    e.set('_loc2_', 0)
    for key_13 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_13)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'invented').get(), True)):
                assign(e.ref('_loc2_'), '+=', lambda: ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'weight').get())
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def TechTree___get__shortMSG(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', 'i'], closure, 'TechTree')
    e.set('_loc2_', 'Technologies invented: ')
    for key_14 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_14)
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(this, 'techArr').get(), e.get('i')).get())
            if truth(ref(e.get('_loc4_'), 'inventedInLastTurn').get()):
                if truth(unary('!', e.get('_loc3_'))):
                    assign(e.ref('_loc3_'), '=', lambda: True)
                    assign(e.ref('_loc2_'), '+=', lambda: ref(e.get('_loc4_'), 'prettyName').get())
                else:
                    assign(e.ref('_loc2_'), '+=', lambda: binop('+', ', ', ref(e.get('_loc4_'), 'prettyName').get()))
        except ASContinue:
            pass
        except ASBreak:
            break
    if truth(e.get('_loc3_')):
        return e.get('_loc2_')
    return ''
    return U

def TechTree_resetInventedLastTurn(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'TechTree')
    for key_15 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_15)
        rt.tick()
        try:
            assign(ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'inventedInLastTurn'), '=', lambda: False)
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def TechTree___get__maxTexLevel(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'TechTree')
    e.set('_loc2_', 0)
    for key_16 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_16)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '+=', lambda: ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'weight').get())
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def TechTree___get__allow_special(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', 'i'], closure, 'TechTree')
    e.set('_loc2_', 0)
    e.set('_loc3_', False)
    for key_17 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_17)
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(this, 'techArr').get(), e.get('i')).get())
            if truth(logical('&&', binop('==', ref(e.get('_loc4_'), 'techLevel').get(), 4), lambda: ref(e.get('_loc4_'), 'invented').get())):
                assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
            if truth(logical('&&', ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get(), lambda: logical('&&', binop('==', ref(e.get('_loc4_'), 'techLevel').get(), 2), lambda: ref(e.get('_loc4_'), 'invented').get()))):
                assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
            if truth(logical('&&', ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get(), lambda: logical('&&', binop('==', ref(e.get('_loc4_'), 'techName').get(), 'plane1'), lambda: ref(e.get('_loc4_'), 'invented').get()))):
                assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    if truth(ref(rt.call_ref(ref(this, 'getTechByName'), ['plane2']), 'invented').get()):
        assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
    if truth(binop('>=', e.get('_loc2_'), 4)):
        assign(e.ref('_loc3_'), '=', lambda: True)
    return e.get('_loc3_')
    return U

def TechTree_allow_production_by_group(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['_loc3_', '_loc4_', 'a_nr', 'i'], closure, 'TechTree')
    e.set('_loc4_', False)
    if truth(binop('==', e.get('a_nr'), 8)):
        return True
    for key_18 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_18)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(this, 'techArr').get(), e.get('i')).get())
            if truth(logical('&&', ref(e.get('_loc3_'), 'invented').get(), lambda: binop('==', ref(e.get('_loc3_'), 'desireGroup').get(), e.get('a_nr')))):
                return True
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc4_')
    return U

def TechTree_force_invent_tech_ch(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'TechTree')
    for key_19 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_19)
        rt.tick()
        try:
            assign(ref(ref(ref(this, 'techArr').get(), e.get('i')).get(), 'invented'), '=', lambda: True)
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def TechTree_invent_below_tech_level(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_techLevel'], ['_loc3_', 'a_techLevel', 'i'], closure, 'TechTree')
    for key_20 in keys(ref(this, 'techArr').get()):
        e.ref('i').set(key_20)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(this, 'techArr').get(), e.get('i')).get())
            if truth(logical('&&', binop('<=', ref(e.get('_loc3_'), 'techLevel').get(), e.get('a_techLevel')), lambda: logical('&&', binop('!=', ref(e.get('_loc3_'), 'desireGroup').get(), 7), lambda: logical('||', unary('!', ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get()), lambda: ref(e.get('_loc3_'), 'allow_in_demo').get())))):
                assign(ref(e.get('_loc3_'), 'invented'), '=', lambda: True)
                assign(ref(e.get('_loc3_'), 'inventedInLastTurn'), '=', lambda: False)
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def TechTree___get__roc_invented(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'TechTree')
    if truth(ref(ref(ref(this, 'techArr').get(), 3).get(), 'invented').get()):
        return True
    return False
    return U

def TechTree_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'TechTree')
    pass

def register(rt):
    rt.define('TechTree', None, TechTree_fields, {'TechTree': ASFunction(TechTree_TechTree), 'inventAll': ASFunction(TechTree_inventAll), 'inventTechByID': ASFunction(TechTree_inventTechByID), 'inventTechByName': ASFunction(TechTree_inventTechByName), 'unInventTechByName': ASFunction(TechTree_unInventTechByName), 'unInventTechByID': ASFunction(TechTree_unInventTechByID), 'resetPreOrder': ASFunction(TechTree_resetPreOrder), 'getTechByID': ASFunction(TechTree_getTechByID), 'getTechByName': ASFunction(TechTree_getTechByName), 'resetInventedLastTurn': ASFunction(TechTree_resetInventedLastTurn), 'allow_production_by_group': ASFunction(TechTree_allow_production_by_group), 'force_invent_tech_ch': ASFunction(TechTree_force_invent_tech_ch), 'invent_below_tech_level': ASFunction(TechTree_invent_below_tech_level)}, {'turnTechArr': ASFunction(TechTree___get__turnTechArr), 'researchMoneySpent': ASFunction(TechTree___get__researchMoneySpent), 'allInvented': ASFunction(TechTree___get__allInvented), 'cheapestUninventedTech': ASFunction(TechTree___get__cheapestUninventedTech), 'techLevel': ASFunction(TechTree___get__techLevel), 'shortMSG': ASFunction(TechTree___get__shortMSG), 'maxTexLevel': ASFunction(TechTree___get__maxTexLevel), 'allow_special': ASFunction(TechTree___get__allow_special), 'roc_invented': ASFunction(TechTree___get__roc_invented)}, {'researchMoneySpent': ASFunction(TechTree___set__researchMoneySpent)})
