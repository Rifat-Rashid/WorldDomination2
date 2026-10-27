# Generated from __Packages/DecisionPoints.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def DecisionPoints_DecisionPoints(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'DecisionPoints')
    return U

def DecisionPoints_DeciosionPoints(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'DecisionPoints')
    return U

def DecisionPoints_set_points_to_difficulty(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['a_nr'], closure, 'DecisionPoints')
    switch_1 = e.get('a_nr')
    case_2 = -1
    if case_2 == -1 and strict_eq(switch_1, 1):
        case_2 = 0
    if case_2 == -1 and strict_eq(switch_1, 2):
        case_2 = 1
    if case_2 == -1 and strict_eq(switch_1, 3):
        case_2 = 2
    if case_2 == -1:
        case_2 = 3
    try:
        if 0 <= case_2 <= 0:
            assign(ref(ref(this, 'attack').get(), 'base'), '=', lambda: 80)
            return U
        if 0 <= case_2 <= 1:
            assign(ref(ref(this, 'attack').get(), 'base'), '=', lambda: 86)
            return U
        if 0 <= case_2 <= 2:
            assign(ref(ref(this, 'attack').get(), 'base'), '=', lambda: 90)
            return U
        if 0 <= case_2 <= 3:
            assign(ref(ref(this, 'attack').get(), 'base'), '=', lambda: 86)
            return U
    except ASBreak:
        pass
    return U

def DecisionPoints_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'DecisionPoints')
    ref(this, 'attack').set(rt.construct(e.get('Object'), [obj({'base': 89, 'retalBonus': 20})]))
    ref(this, 'preCounter').set(rt.construct(e.get('Object'), [obj({'base': 86, 'lastAttackAB_bonus': 10, 'lastAttackBA_bonus': 10, 'minPopForBonus': 20, 'lowPopBonus': 10, 'otherTargetsBonus': 5})]))
    ref(this, 'religion').set(rt.construct(e.get('Object'), [obj({'base': 40})]))
    ref(this, 'propaganda').set(rt.construct(e.get('Object'), [obj({'base': 42, 'highReligionBonus': 10})]))
    ref(this, 'diplomacy').set(rt.construct(e.get('Object'), [obj({'base': 60})]))
    ref(this, 'resources').set(rt.construct(e.get('Object'), [obj({'base': 50, 'reserveBase': 25, 'maxFunds': 100})]))
    ref(this, 'production').set(rt.construct(e.get('Object'), [obj({'base': 55, 'enemy_stock_bonus': 15})]))
    ref(this, 'research').set(rt.construct(e.get('Object'), [obj({'base': 60, 'turnCap': 60, 'techTurnRatioMultiplier': 9})]))

def register(rt):
    rt.define('DecisionPoints', None, DecisionPoints_fields, {'DecisionPoints': ASFunction(DecisionPoints_DecisionPoints), 'DeciosionPoints': ASFunction(DecisionPoints_DeciosionPoints), 'set_points_to_difficulty': ASFunction(DecisionPoints_set_points_to_difficulty)}, {}, {})
