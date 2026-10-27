# Generated from __Packages/TurnAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def TurnAction_TurnAction(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_num'], ['param_num'], closure, 'TurnAction')
    assign(ref(this, 'turnMoney'), '=', lambda: 0)
    assign(ref(this, 'num'), '=', lambda: e.get('param_num'))
    assign(ref(this, 'productionInvestmentArr'), '=', lambda: rt.construct(e.get('Array'), [arr([]), arr(['rockets', 0, 1, 0, 1]), arr(['planes', 0, 6, 0, 2]), arr(['special', 0, 7, 0, 3]), arr(['warhead', 0, 2, 0, 4]), arr(['bioload', 0, 3, 0, 5]), arr(['soldier', 0, 4, 0, 6]), arr(['spy', 0, 5, 0, 7]), arr(['defense', 0, 8, 0, 8])]))
    return U

def TurnAction_doReset(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'TurnAction')
    assign(ref(ref(this, 'attackWeapon').get(), 'inUse'), '=', lambda: 0)
    assign(ref(ref(this, 'preAttackCarrier').get(), 'inUse'), '=', lambda: 0)
    assign(ref(ref(this, 'preAttackPayload').get(), 'inUse'), '=', lambda: 0)
    assign(ref(this, 'action'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'targetPlayer'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'targetCity'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'preAttackCarrier'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'preAttackPayload'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'attackWeapon'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'inventTech'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'buyArr'), '=', lambda: arr([]))
    assign(ref(this, 'humanBuyArr'), '=', lambda: arr([]))
    assign(ref(this, 'humanResearchArr'), '=', lambda: arr([]))
    assign(ref(this, 'inventArr'), '=', lambda: arr([]))
    assign(ref(this, 'forceCity'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'ship_attack_arr'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'productionInvestmentArr'), '=', lambda: rt.construct(e.get('Array'), [arr([]), arr(['rockets', 0, 1, 0, 1]), arr(['planes', 0, 6, 0, 2]), arr(['special', 0, 7, 0, 3]), arr(['warhead', 0, 2, 0, 4]), arr(['bioload', 0, 3, 0, 5]), arr(['soldier', 0, 4, 0, 6]), arr(['spy', 0, 5, 0, 7]), arr(['defense', 0, 8, 0, 8])]))
    assign(ref(this, 'researchArr'), '=', lambda: arr([]))
    assign(ref(this, 'diplomacyArr'), '=', lambda: arr([]))
    assign(ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'turnMoney'), '+=', lambda: ref(this, 'turnMoney').get())
    assign(ref(this, 'researchMoneySpend'), '=', lambda: 0)
    assign(ref(this, 'turnMoney'), '=', lambda: 0)
    assign(ref(this, 'diplomacyLeader'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'diplomacyOption'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'spyBuilding'), '=', lambda: 'spyCenter')
    return U

def TurnAction___set__action(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str'], closure, 'TurnAction')
    if truth(binop('==', e.get('_str'), 'reset')):
        if truth(logical('||', binop('==', ref(this, 'action').get(), '_attack'), lambda: logical('||', binop('==', ref(this, '_action').get(), 'preAttack'), lambda: binop('==', ref(this, '_action').get(), 'attack')))):
            assign(ref(this, '_action'), '=', lambda: 'reset')
    else:
        assign(ref(this, '_action'), '=', lambda: e.get('_str'))
    return U

def TurnAction___get__action(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'TurnAction')
    return ref(this, '_action').get()
    return U

def TurnAction___get__actionNames(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'TurnAction')
    e.set('_loc2_', '')
    if truth(ref(this, 'action').get()):
        assign(e.ref('_loc2_'), '+=', lambda: binop('+', binop('+', '<b> ', ref(this, 'action').get()), ' </b><br/>'))
    if truth(ref(this, 'targetPlayer').get()):
        assign(e.ref('_loc2_'), '+=', lambda: binop('+', binop('+', ' targetPlayer: ', ref(ref(this, 'targetPlayer').get(), 'playerNum').get()), '<br/>'))
    if truth(ref(this, 'targetCity').get()):
        assign(e.ref('_loc2_'), '+=', lambda: binop('+', binop('+', ' targetCity: ', ref(ref(this, 'targetCity').get(), 'cityID').get()), '<br/>'))
    if truth(ref(this, 'preAttackCarrier').get()):
        assign(e.ref('_loc2_'), '+=', lambda: binop('+', binop('+', ' carrier: ', ref(ref(this, 'preAttackCarrier').get(), 'weaponName').get()), '<br/>'))
    if truth(ref(this, 'preAttackPayload').get()):
        assign(e.ref('_loc2_'), '+=', lambda: binop('+', binop('+', ' payload: ', ref(ref(this, 'preAttackPayload').get(), 'weaponName').get()), '<br/>'))
    if truth(ref(this, 'attackWeapon').get()):
        assign(e.ref('_loc2_'), '+=', lambda: binop('+', binop('+', ' attackWeapon: ', ref(ref(this, 'attackWeapon').get(), 'weaponName').get()), '<br/>'))
    if truth(ref(this, 'inventTech').get()):
        assign(e.ref('_loc2_'), '+=', lambda: binop('+', binop('+', ' inventTech: ', ref(ref(this, 'inventTech').get(), 'techName').get()), '<br/>'))
    if truth(binop('>', ref(ref(this, 'buyArr').get(), 'length').get(), 0)):
        assign(e.ref('_loc2_'), '+=', lambda: ' buyArr: ')
        for key_1 in keys(ref(this, 'buyArr').get()):
            e.ref('i').set(key_1)
            rt.tick()
            try:
                assign(e.ref('_loc2_'), '+=', lambda: binop('+', ref(ref(ref(ref(this, 'buyArr').get(), e.get('i')).get(), 'weapon').get(), 'weaponName').get(), ' - '))
            except ASContinue:
                pass
            except ASBreak:
                break
        assign(e.ref('_loc2_'), '+=', lambda: ' <br/> ')
    return e.get('_loc2_')
    return U

def TurnAction___get__productionMoneySpend(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'TurnAction')
    e.set('_loc2_', 0)
    for key_2 in keys(ref(this, 'productionInvestmentArr').get()):
        e.ref('i').set(key_2)
        rt.tick()
        try:
            if truth(binop('>', ref(ref(ref(this, 'productionInvestmentArr').get(), e.get('i')).get(), 3).get(), 0)):
                assign(e.ref('_loc2_'), '+=', lambda: ref(ref(ref(this, 'productionInvestmentArr').get(), e.get('i')).get(), 3).get())
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def TurnAction_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'TurnAction')
    ref(this, 'reset').set(False)

def register(rt):
    rt.define('TurnAction', None, TurnAction_fields, {'TurnAction': ASFunction(TurnAction_TurnAction), 'doReset': ASFunction(TurnAction_doReset)}, {'action': ASFunction(TurnAction___get__action), 'actionNames': ASFunction(TurnAction___get__actionNames), 'productionMoneySpend': ASFunction(TurnAction___get__productionMoneySpend)}, {'action': ASFunction(TurnAction___set__action)})
