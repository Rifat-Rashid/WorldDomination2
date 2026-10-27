# Generated from __Packages/Player.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Player_Player(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_playedBy', 'param_num', 'param_startLocation'], ['param_num', 'param_playedBy', 'param_startLocation'], closure, 'Player')
    assign(ref(this, 'buildingSet_id'), '=', lambda: '__')
    assign(ref(this, 'alive'), '=', lambda: True)
    assign(ref(this, 'playerNum'), '=', lambda: e.get('param_num'))
    assign(ref(this, 'playedBy'), '=', lambda: e.get('param_playedBy'))
    assign(ref(this, 'turnAction_1'), '=', lambda: rt.construct(e.get('TurnAction'), [1]))
    assign(ref(this, 'turnAction_2'), '=', lambda: rt.construct(e.get('TurnAction'), [2]))
    assign(ref(this, 'turnActionArr'), '=', lambda: arr([ref(this, 'turnAction_1').get(), ref(this, 'turnAction_2').get()]))
    assign(ref(this, 'techTree'), '=', lambda: rt.construct(e.get('TechTree'), []))
    assign(ref(this, 'weaponStock'), '=', lambda: rt.construct(e.get('WeaponStock'), []))
    assign(ref(this, 'dualAttack'), '=', lambda: False)
    assign(ref(this, 'cityArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'regardArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'decisionPointsArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'preCounterEnemy'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'startLocation'), '=', lambda: e.get('param_startLocation'))
    assign(ref(this, 'bioloadedActionsArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'bioloadedStockArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'turnMoney'), '=', lambda: 0)
    assign(ref(this, 'bioloaded'), '=', lambda: False)
    assign(ref(this, 'ceaseFireArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'diplomacyPendingArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'diplomacyAcceptedArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'diplomacyRejectedArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'shortMSG_arr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'turnBattleCasualties'), '=', lambda: 0)
    assign(ref(this, 'turnPropagandaCasualties'), '=', lambda: 0)
    assign(ref(this, 'turnBattleKills'), '=', lambda: 0)
    assign(ref(this, 'turnResourcesGained'), '=', lambda: 0)
    assign(ref(this, 'diplomacy_offeredLastTurn'), '=', lambda: arr([False, False, False, False, False]))
    assign(ref(this, 'specialization'), '=', lambda: rt.construct(e.get('AI_specialization'), []))
    assign(ref(this, 'score'), '=', lambda: 0)
    return U

def Player___get__turnSpendings(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Player')
    e.set('_loc2_', binop('+', ref(ref(this, 'weaponStock').get(), 'production_money_spent').get(), ref(ref(this, 'techTree').get(), 'researchMoneySpent').get()))
    return e.call('Number', [e.get('_loc2_')])
    return U

def Player___get__nextActionBuilding(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Player')
    e.set('_loc2_', 1)
    if truth(ref(this, 'building1Shown').get()):
        assign(e.ref('_loc2_'), '=', lambda: 2)
    else:
        assign(ref(this, 'building1Shown'), '=', lambda: True)
    if truth(binop('==', ref(this, 'playerNum').get(), 0)):
        pass
    return e.get('_loc2_')
    return U

def Player___get__preLocation(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Player')
    return ref(this, '_preLocation').get()
    return U

def Player___set__preLocation(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_num'], ['_num'], closure, 'Player')
    assign(ref(this, '_preLocation'), '=', lambda: e.get('_num'))
    return U

def Player_resetBuildingsShown(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Player')
    assign(ref(this, 'building1Shown'), '=', lambda: False)
    assign(ref(this, 'building2Shown'), '=', lambda: False)
    return U

def Player_isBioloaded(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param'], ['_loc3_', 'i', 'param'], closure, 'Player')
    e.set('_loc3_', False)
    for key_1 in keys(ref(this, 'bioloadedActionsArr').get()):
        e.ref('i').set(key_1)
        rt.tick()
        try:
            if truth(logical('||', binop('==', e.get('param'), ref(ref(this, 'bioloadedActionsArr').get(), e.get('i')).get()), lambda: logical('||', logical('&&', binop('==', e.get('param'), 'produce'), lambda: binop('==', ref(ref(this, 'bioloadedActionsArr').get(), e.get('i')).get(), 'production')), lambda: logical('&&', binop('==', e.get('param'), 'research'), lambda: binop('==', ref(ref(this, 'bioloadedActionsArr').get(), e.get('i')).get(), 'technology'))))):
                assign(e.ref('_loc3_'), '=', lambda: True)
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc3_')
    return U

def Player_approveAction(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Player')
    return U

def Player_resetActions(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Player')
    if truth(binop('==', ref(this, 'preAttackStatus').get(), 'inactive')):
        rt.call_ref(ref(ref(this, 'turnAction_1').get(), 'doReset'), [])
        rt.call_ref(ref(ref(this, 'turnAction_2').get(), 'doReset'), [])
    if truth(unary('!', ref(ref(this, 'turnAction_1').get(), 'preAttackPayload').get())):
        rt.call_ref(ref(ref(this, 'turnAction_1').get(), 'doReset'), [])
    if truth(unary('!', ref(ref(this, 'turnAction_2').get(), 'preAttackPayload').get())):
        rt.call_ref(ref(ref(this, 'turnAction_2').get(), 'doReset'), [])
    else:
        assign(ref(this, 'turnAction_1'), '=', lambda: ref(this, 'turnAction_2').get())
        rt.call_ref(ref(ref(this, 'turnAction_2').get(), 'doReset'), [])
    return U

def Player_setNextTurnAction(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Player')
    if truth(unary('!', ref(ref(this, 'turnAction_1').get(), 'action').get())):
        assign(e.ref('_loc2_'), '=', lambda: ref(this, 'turnAction_1').get())
    else:
        if truth(unary('!', ref(ref(this, 'turnAction_2').get(), 'action').get())):
            assign(e.ref('_loc2_'), '=', lambda: ref(this, 'turnAction_2').get())
    return U

def Player_getNextTurnAction(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Player')
    if truth(unary('!', ref(ref(this, 'turnAction_1').get(), 'action').get())):
        return ref(this, 'turnAction_1').get()
    if truth(unary('!', ref(ref(this, 'turnAction_2').get(), 'action').get())):
        return ref(this, 'turnAction_2').get()
    return False
    return U

def Player___resolve(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param'], ['param'], closure, 'Player')
    if truth(logical('&&', binop('!=', e.get('param'), 'debug'), lambda: binop('!=', e.get('param'), '_visible'))):
        pass
    return U

def Player___get__lowestRegardNum(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'Player')
    e.set('_loc2_', 100)
    for key_2 in keys(ref(this, 'regardArr').get()):
        e.ref('i').set(key_2)
        rt.tick()
        try:
            if truth(binop('<', ref(ref(this, 'regardArr').get(), e.get('i')).get(), e.get('_loc2_'))):
                assign(e.ref('_loc2_'), '=', lambda: ref(ref(this, 'regardArr').get(), e.get('i')).get())
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def Player___get__population(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'Player')
    e.set('_loc2_', 0)
    for key_3 in keys(ref(this, 'cityArr').get()):
        e.ref('i').set(key_3)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '+=', lambda: ref(ref(ref(this, 'cityArr').get(), e.get('i')).get(), 'population').get())
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def Player_largest_city(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', 'i'], closure, 'Player')
    e.set('_loc2_', 0)
    for key_4 in keys(ref(this, 'cityArr').get()):
        e.ref('i').set(key_4)
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(this, 'cityArr').get(), e.get('i')).get())
            if truth(binop('<', e.get('_loc2_'), ref(e.get('_loc4_'), 'population').get())):
                assign(e.ref('_loc2_'), '=', lambda: ref(e.get('_loc4_'), 'population').get())
                assign(e.ref('_loc3_'), '=', lambda: e.get('_loc4_'))
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc3_')
    return U

def Player___get__religion(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Player')
    return ref(this, 'religionLevel').get()
    return U

def Player___set__religion(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['n'], ['n'], closure, 'Player')
    assign(ref(this, 'religionLevel'), '=', lambda: e.get('n'))
    return U

def Player___get__techLevel(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Player')
    return ref(ref(this, 'techTree').get(), 'techLevel').get()
    return U

def Player___get__weaponStockStrength(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', 'i'], closure, 'Player')
    e.set('_loc2_', 0)
    for key_5 in keys(ref(ref(this, 'weaponStock').get(), 'weaponArr').get()):
        e.ref('i').set(key_5)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(this, 'weaponStock').get(), 'weaponArr').get(), e.get('i')).get())
            assign(e.ref('_loc2_'), '+=', lambda: binop('*', ref(e.get('_loc3_'), 'inStock').get(), ref(e.get('_loc3_'), 'weaponLevel').get()))
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def Player___get__weaponStockLevel(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', 'i'], closure, 'Player')
    e.set('_loc2_', 0)
    e.set('_loc3_', 0)
    for key_6 in keys(ref(ref(this, 'weaponStock').get(), 'weaponArr').get()):
        e.ref('i').set(key_6)
        rt.tick()
        try:
            if truth(ref(rt.call_ref(ref(ref(this, 'techTree').get(), 'getTechByName'), [ref(ref(ref(ref(this, 'weaponStock').get(), 'weaponArr').get(), e.get('i')).get(), 'relatedTechName').get()]), 'invented').get()):
                assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
                if truth(binop('>=', ref(ref(ref(ref(this, 'weaponStock').get(), 'weaponArr').get(), e.get('i')).get(), 'inStock').get(), ref(ref(ref(ref(this, 'weaponStock').get(), 'weaponArr').get(), e.get('i')).get(), 'desire').get())):
                    assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return binop('*', binop('/', e.get('_loc3_'), e.get('_loc2_')), 100)
    return U

def Player___get__strength(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Player')
    return binop('+', binop('+', ref(this, 'techLevel').get(), ref(this, 'weaponStockStrength').get()), ref(this, 'money').get())
    return U

def Player_setChars(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'Player')
    if truth(binop('==', ref(ref(this, 'desireArr').get(), 'length').get(), ref(ref(ref(this, 'weaponStock').get(), 'weaponArr').get(), 'length').get())):
        for key_7 in keys(ref(this, 'desireArr').get()):
            e.ref('i').set(key_7)
            rt.tick()
            try:
                assign(ref(ref(ref(ref(this, 'weaponStock').get(), 'weaponArr').get(), e.get('i')).get(), 'desire'), '=', lambda: ref(ref(this, 'desireArr').get(), e.get('i')).get())
                assign(ref(rt.call_ref(ref(ref(this, 'techTree').get(), 'getTechByName'), [ref(ref(ref(ref(this, 'weaponStock').get(), 'weaponArr').get(), e.get('i')).get(), 'relatedTechName').get()]), 'desire'), '=', lambda: ref(ref(this, 'desireArr').get(), e.get('i')).get())
            except ASContinue:
                pass
            except ASBreak:
                break
    return U

def Player___get__counterWeapon(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'Player')
    for key_8 in keys(ref(this, 'turnActionArr').get()):
        e.ref('i').set(key_8)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'turnActionArr').get(), e.get('i')).get(), 'action').get(), 'counterPre')):
                return ref(ref(ref(this, 'turnActionArr').get(), e.get('i')).get(), 'attackWeapon').get()
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Player___get__allActionsSet(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Player')
    e.set('_loc2_', 0)
    if truth(binop('!=', ref(ref(this, 'turnAction_1').get(), 'action').get(), e.get('undefined'))):
        assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
    if truth(binop('!=', ref(ref(this, 'turnAction_2').get(), 'action').get(), e.get('undefined'))):
        assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
    if truth(binop('==', e.get('_loc2_'), 2)):
        return True
    return False
    return U

def Player_kill(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Player')
    assign(ref(this, 'shortMSG_arr'), '=', lambda: arr([]))
    assign(ref(this, 'alive'), '=', lambda: False)
    return U

def Player_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Player')
    ref(this, 'religionLevel').set(0)
    ref(this, 'preAttackStatus').set('inactive')
    ref(this, 'alive').set(False)
    ref(this, 'building1Shown').set(False)
    ref(this, 'building2Shown').set(False)
    ref(this, '_preLocation').set(e.get('undefined'))
    ref(this, '_propagandaMC').set(e.get('undefined'))
    ref(this, 'shipFrame').set(1)
    ref(this, 'diplomacy_offeredLastTurn').set(arr([False, False, False, False, False]))
    ref(this, 'special_person').set(False)
    ref(this, 'suicide_person').set(False)
    ref(this, 'dead_avatar_played').set(False)
    ref(this, 'production_money_returned').set(0)
    ref(this, '_technology_money_spent').set(0)
    ref(this, '_anti_spy_money_spent').set(0)
    ref(this, 'satellites_used').set(0)

def register(rt):
    rt.define('Player', None, Player_fields, {'Player': ASFunction(Player_Player), 'resetBuildingsShown': ASFunction(Player_resetBuildingsShown), 'isBioloaded': ASFunction(Player_isBioloaded), 'approveAction': ASFunction(Player_approveAction), 'resetActions': ASFunction(Player_resetActions), 'setNextTurnAction': ASFunction(Player_setNextTurnAction), 'getNextTurnAction': ASFunction(Player_getNextTurnAction), '__resolve': ASFunction(Player___resolve), 'largest_city': ASFunction(Player_largest_city), 'setChars': ASFunction(Player_setChars), 'kill': ASFunction(Player_kill)}, {'turnSpendings': ASFunction(Player___get__turnSpendings), 'nextActionBuilding': ASFunction(Player___get__nextActionBuilding), 'preLocation': ASFunction(Player___get__preLocation), 'lowestRegardNum': ASFunction(Player___get__lowestRegardNum), 'population': ASFunction(Player___get__population), 'religion': ASFunction(Player___get__religion), 'techLevel': ASFunction(Player___get__techLevel), 'weaponStockStrength': ASFunction(Player___get__weaponStockStrength), 'weaponStockLevel': ASFunction(Player___get__weaponStockLevel), 'strength': ASFunction(Player___get__strength), 'counterWeapon': ASFunction(Player___get__counterWeapon), 'allActionsSet': ASFunction(Player___get__allActionsSet)}, {'preLocation': ASFunction(Player___set__preLocation), 'religion': ASFunction(Player___set__religion)})
