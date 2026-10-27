# Generated from __Packages/Sub_presenter.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Sub_presenter_Sub_presenter(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_presenter')
    return U

def Sub_presenter_turnResults(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc14_', '_loc15_', '_loc16_', '_loc17_', '_loc18_', '_loc19_', '_loc20_', '_loc21_', '_loc22_', '_loc23_', '_loc24_', '_loc25_', '_loc26_', '_loc27_', '_loc28_', '_loc29_', '_loc2_', '_loc30_', '_loc31_', '_loc32_', '_loc33_', '_loc34_', '_loc35_', '_loc36_', '_loc37_', '_loc38_', '_loc39_', '_loc3_', '_loc40_', '_loc41_', '_loc42_', '_loc43_', '_loc44_', '_loc45_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', 'i', 'j', 'k', 'k2', 'q'], closure, 'Sub_presenter')
    rt.call_ref(ref(ref(this, 'model').get(), 'reset_playerAB_position_arr'), [])
    assign(ref(ref(this, 'model').get(), 'attackingSubs_arr'), '=', lambda: arr([]))
    assign(ref(ref(this, 'model').get(), 'attackingSubs_arr_index'), '=', lambda: 0)
    assign(ref(ref(this, 'model').get(), 'turnResultsArr'), '=', lambda: arr([]))
    assign(ref(ref(this, 'model').get(), 'battleMC_units_active'), '=', lambda: False)
    for key_1 in keys(ref(ref(this, 'model').get(), 'activePlayerArr').get()):
        e.ref('i').set(key_1)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: True)
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'activePlayerArr').get(), e.get('i')).get())
            assign(ref(e.get('_loc3_'), 'shortMSG_arr'), '=', lambda: arr([]))
            assign(ref(e.get('_loc3_'), 'turnBattleCasualties'), '=', lambda: 0)
            assign(ref(e.get('_loc3_'), 'turnBattleKills'), '=', lambda: 0)
            assign(ref(e.get('_loc3_'), 'turnPropagandaCasualties'), '=', lambda: 0)
            assign(ref(e.get('_loc3_'), 'turnResourcesGained'), '=', lambda: 0)
            if truth(binop('<', ref(e.get('_loc3_'), 'spy_readiness').get(), 0)):
                assign(ref(e.get('_loc3_'), 'spy_readiness'), '=', lambda: 0)
            if truth(rt.call_ref(ref(e.get('_global'), 'isNaN'), [ref(e.get('_loc3_'), 'spy_readiness').get()])):
                assign(ref(e.get('_loc3_'), 'spy_readiness'), '=', lambda: 50)
            assign(ref(e.get('_loc3_'), 'spy_readiness'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'min'), [binop('+', ref(e.get('_loc3_'), 'spy_readiness').get(), 25), 100]))
            assign(e.ref('_loc4_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc4_'), ref(ref(e.get('_loc3_'), 'regardArr').get(), 'length').get())):
                rt.tick()
                try:
                    if truth(ref(ref(ref(e.get('_loc3_'), 'ceaseFireArr').get(), e.get('_loc4_')).get(), '_status').get()):
                        assign(ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')), '+=', lambda: 2)
                    if truth(binop('<', ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')).get(), 100)):
                        update(ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')), 1, False)
                        if truth(binop('==', ref(ref(this, 'model').get(), 'difficulty_level').get(), 0)):
                            update(ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')), 1, False)
                            update(ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')), 1, False)
                        if truth(binop('==', ref(ref(this, 'model').get(), 'difficulty_level').get(), 1)):
                            update(ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')), 1, False)
                    if truth(binop('<', ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')).get(), 50)):
                        update(ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')), 1, False)
                        if truth(binop('==', ref(ref(this, 'model').get(), 'difficulty_level').get(), 0)):
                            update(ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')), 1, False)
                    if truth(binop('<', ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')).get(), 30)):
                        update(ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')), 1, False)
                    if truth(binop('>', ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')).get(), 100)):
                        assign(ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')), '=', lambda: 100)
                    if truth(binop('==', ref(e.get('_loc3_'), 'playedBy').get(), 'AI')):
                        assign(e.ref('_loc5_'), '=', lambda: 1)
                        while truth(binop('<', e.get('_loc5_'), ref(ref(e.get('_loc3_'), 'regardArr').get(), 'length').get())):
                            rt.tick()
                            try:
                                assign(ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc5_')), '+=', lambda: ref(ref(this, 'model').get(), 'difficulty_level').get())
                                assign(e.ref('_loc5_'), '=', lambda: binop('+', e.get('_loc5_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                    assign(e.ref('_loc4_'), '=', lambda: binop('+', e.get('_loc4_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            if truth(unary('!', ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), 'primary_enemy').get()).get(), 'alive').get())):
                assign(ref(e.get('_loc3_'), 'primary_enemy'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'get_random_set_enemy'), [e.get('_loc3_'), ref(e.get('_loc3_'), 'secundary_enemy').get()]))
            if truth(unary('!', ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), 'secundary_enemy').get()).get(), 'alive').get())):
                assign(ref(e.get('_loc3_'), 'secundary_enemy'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'get_random_set_enemy'), [e.get('_loc3_'), ref(e.get('_loc3_'), 'primary_enemy').get()]))
            if truth(binop('>', ref(e.get('_loc3_'), 'religion').get(), 11)):
                assign(ref(e.get('_loc3_'), 'religion'), '-=', lambda: rt.call_ref(ref(ref(ref(this, 'model').get(), 'tools').get(), 'randRange'), [5, 10]))
            if truth(logical('&&', binop('<', ref(e.get('_loc3_'), 'money').get(), unary('-', 1)), lambda: binop('==', ref(e.get('_loc3_'), 'playedBy').get(), 'human'))):
                rt.call_ref(ref(ref(this, 'model').get(), 'error'), ['money', ref(e.get('_loc3_'), 'playerNum').get(), ref(e.get('_loc3_'), 'money').get()])
            if truth(binop('<', ref(e.get('_loc3_'), 'money').get(), 0)):
                assign(ref(e.get('_loc3_'), 'money'), '=', lambda: 1)
            if truth(ref(e.get('_loc3_'), 'special_person').get()):
                assign(ref(e.get('_loc3_'), 'money'), '+=', lambda: 3)
            if truth(logical('&&', binop('==', ref(e.get('_loc3_'), 'preAttackStatus').get(), 'ready'), lambda: logical('&&', binop('!=', ref(ref(e.get('_loc3_'), 'turnAction_1').get(), 'action').get(), 'preAttack'), lambda: binop('!=', ref(ref(e.get('_loc3_'), 'turnAction_2').get(), 'action').get(), 'preAttack')))):
                rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_plr': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'cancel_pre'})])
                assign(ref(e.get('_loc3_'), 'preAttackStatus'), '=', lambda: 'inactive')
            if truth(logical('&&', binop('!=', ref(ref(e.get('_loc3_'), 'turnAction_1').get(), 'action').get(), 'preAttack'), lambda: binop('!=', ref(ref(e.get('_loc3_'), 'turnAction_2').get(), 'action').get(), 'preAttack'))):
                assign(ref(e.get('_loc3_'), 'preLocation'), '=', lambda: e.get('undefined'))
            if truth(logical('&&', ref(e.get('_loc3_'), 'preLocation').get(), lambda: binop('!=', ref(e.get('_loc3_'), 'preAttackStatus').get(), 'ready'))):
                assign(ref(e.get('_loc3_'), 'preLocation'), '=', lambda: e.get('undefined'))
            for key_2 in keys(ref(e.get('_loc3_'), 'diplomacyAcceptedArr').get()):
                e.ref('j').set(key_2)
                rt.tick()
                try:
                    rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'diplomacyAccepted', '_arr': ref(ref(e.get('_loc3_'), 'diplomacyAcceptedArr').get(), e.get('j')).get()})])
                except ASContinue:
                    pass
                except ASBreak:
                    break
            for key_3 in keys(ref(e.get('_loc3_'), 'diplomacyRejectedArr').get()):
                e.ref('j').set(key_3)
                rt.tick()
                try:
                    rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'diplomacyRejected', '_arr': ref(ref(e.get('_loc3_'), 'diplomacyRejectedArr').get(), e.get('j')).get()})])
                except ASContinue:
                    pass
                except ASBreak:
                    break
            for key_4 in keys(ref(e.get('_loc3_'), 'cityArr').get()):
                e.ref('j').set(key_4)
                rt.tick()
                try:
                    assign(e.ref('_loc6_'), '=', lambda: ref(ref(e.get('_loc3_'), 'cityArr').get(), e.get('j')).get())
                    if truth(ref(e.get('_loc6_'), 'bioloaded').get()):
                        rt.call_ref(ref(e.get('_loc6_'), 'removeBioload'), [])
                except ASContinue:
                    pass
                except ASBreak:
                    break
            rt.call_ref(ref(ref(e.get('_loc3_'), 'weaponStock').get(), 'removeBioload'), [])
            assign(ref(e.get('_loc3_'), 'bioloadedActionsArr'), '=', lambda: arr([]))
            assign(ref(e.get('_loc3_'), 'bioloadedStockArr'), '=', lambda: arr([]))
            assign(ref(e.get('_loc3_'), 'bioloaded'), '=', lambda: False)
            assign(ref(e.get('_loc3_'), 'diplomacyAcceptedArr'), '=', lambda: arr([]))
            assign(ref(e.get('_loc3_'), 'diplomacyRejectedArr'), '=', lambda: arr([]))
            assign(ref(e.get('_loc3_'), 'preBuilding_this_turn'), '=', lambda: False)
            for key_5 in keys(ref(e.get('_loc3_'), 'diplomacy_offeredLastTurn').get()):
                e.ref('j').set(key_5)
                rt.tick()
                try:
                    assign(e.ref('_loc7_'), '=', lambda: ref(ref(e.get('_loc3_'), 'diplomacy_offeredLastTurn').get(), e.get('j')).get())
                    if truth(binop('>', e.get('_loc7_'), 0)):
                        update(ref(ref(e.get('_loc3_'), 'diplomacy_offeredLastTurn').get(), e.get('j')), -1, False)
                    else:
                        if truth(binop('<=', e.get('_loc7_'), 0)):
                            assign(ref(ref(e.get('_loc3_'), 'diplomacy_offeredLastTurn').get(), e.get('j')), '=', lambda: False)
                except ASContinue:
                    pass
                except ASBreak:
                    break
            for key_6 in keys(ref(ref(e.get('_loc3_'), 'weaponStock').get(), 'weaponArr').get()):
                e.ref('j').set(key_6)
                rt.tick()
                try:
                    assign(ref(ref(ref(ref(e.get('_loc3_'), 'weaponStock').get(), 'weaponArr').get(), e.get('j')).get(), 'inUse'), '=', lambda: 0)
                except ASContinue:
                    pass
                except ASBreak:
                    break
            assign(ref(ref(this, 'view').get(), 'AB_interval_start_index'), '=', lambda: 0)
            for key_7 in keys(ref(e.get('_loc3_'), 'turnActionArr').get()):
                e.ref('j').set(key_7)
                rt.tick()
                try:
                    assign(e.ref('_loc8_'), '=', lambda: ref(ref(e.get('_loc3_'), 'turnActionArr').get(), e.get('j')).get())
                    switch_8 = ref(e.get('_loc8_'), 'action').get()
                    case_9 = -1
                    if case_9 == -1 and strict_eq(switch_8, 'resources'):
                        case_9 = 0
                    if case_9 == -1 and strict_eq(switch_8, 'production'):
                        case_9 = 1
                    if case_9 == -1 and strict_eq(switch_8, 'produce'):
                        case_9 = 2
                    if case_9 == -1 and strict_eq(switch_8, 'research'):
                        case_9 = 3
                    if case_9 == -1 and strict_eq(switch_8, 'religion'):
                        case_9 = 4
                    if case_9 == -1 and strict_eq(switch_8, 'preAttack'):
                        case_9 = 5
                    if case_9 == -1 and strict_eq(switch_8, 'attack'):
                        case_9 = 6
                    if case_9 == -1 and strict_eq(switch_8, 'preCounter'):
                        case_9 = 7
                    if case_9 == -1 and strict_eq(switch_8, 'defense'):
                        case_9 = 8
                    if case_9 == -1 and strict_eq(switch_8, 'propaganda'):
                        case_9 = 9
                    if case_9 == -1 and strict_eq(switch_8, 'diplomacy'):
                        case_9 = 10
                    if case_9 == -1:
                        case_9 = -1
                    try:
                        if 0 <= case_9 <= 0:
                            rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'resources', '_value': '0', '_plusmin': 'plus'})])
                            raise ASBreak()
                        if 0 <= case_9 <= 1:
                            for key_10 in keys(ref(e.get('_loc8_'), 'productionInvestmentArr').get()):
                                e.ref('k').set(key_10)
                                rt.tick()
                                try:
                                    if truth(binop('>', ref(ref(ref(e.get('_loc8_'), 'productionInvestmentArr').get(), e.get('k')).get(), 1).get(), 0)):
                                        rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'produce2', '_value': ref(ref(ref(e.get('_loc8_'), 'productionInvestmentArr').get(), e.get('k')).get(), 0).get(), '_amount': ref(ref(ref(e.get('_loc8_'), 'productionInvestmentArr').get(), e.get('k')).get(), 1).get(), '_group': ref(ref(ref(e.get('_loc8_'), 'productionInvestmentArr').get(), e.get('k')).get(), 2).get(), '_money': ref(ref(ref(e.get('_loc8_'), 'productionInvestmentArr').get(), e.get('k')).get(), 3).get()})])
                                except ASContinue:
                                    pass
                                except ASBreak:
                                    break
                            rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'production_building'})])
                            raise ASBreak()
                        if 0 <= case_9 <= 2:
                            raise ASBreak()
                        if 0 <= case_9 <= 3:
                            for key_11 in keys(ref(e.get('_loc8_'), 'researchArr').get()):
                                e.ref('k').set(key_11)
                                rt.tick()
                                try:
                                    rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'research', '_value': ref(ref(ref(e.get('_loc8_'), 'researchArr').get(), e.get('k')).get(), 'techID').get(), 'amount': 1})])
                                except ASContinue:
                                    pass
                                except ASBreak:
                                    break
                            for key_12 in keys(ref(e.get('_loc8_'), 'inventArr').get()):
                                e.ref('k').set(key_12)
                                rt.tick()
                                try:
                                    rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'research', '_value': ref(ref(ref(e.get('_loc8_'), 'inventArr').get(), e.get('k')).get(), 'techID').get(), 'amount': 1})])
                                except ASContinue:
                                    pass
                                except ASBreak:
                                    break
                            rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'research_building'})])
                            raise ASBreak()
                        if 0 <= case_9 <= 4:
                            rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'religion', '_value': 0, '_plusmin': 'plus'})])
                            raise ASBreak()
                        if 0 <= case_9 <= 5:
                            if truth(logical('||', binop('==', ref(e.get('_loc3_'), 'preAttackStatus').get(), 'active'), lambda: binop('==', ref(e.get('_loc3_'), 'preAttackStatus').get(), 'inactive'))):
                                assign(e.ref('_loc2_'), '=', lambda: False)
                                assign(e.ref('_loc9_'), '=', lambda: ref(ref(e.get('_loc8_'), 'preAttackCarrier').get(), 'weaponID').get())
                                assign(e.ref('_loc10_'), '=', lambda: ref(ref(e.get('_loc8_'), 'preAttackPayload').get(), 'weaponID').get())
                                assign(e.ref('_loc11_'), '=', lambda: ref(ref(e.get('_loc8_'), 'targetCity').get(), 'cityID').get())
                                if truth(binop('==', ref(ref(e.get('_loc8_'), 'preAttackCarrier').get(), 'weaponType').get(), 'rocket')):
                                    assign(e.ref('_loc12_'), '=', lambda: 'silo')
                                else:
                                    if truth(binop('==', ref(ref(e.get('_loc8_'), 'preAttackCarrier').get(), 'weaponType').get(), 'plane')):
                                        assign(e.ref('_loc12_'), '=', lambda: 'airfield')
                                    else:
                                        if truth(binop('==', ref(ref(e.get('_loc8_'), 'preAttackCarrier').get(), 'weaponType').get(), 'sub')):
                                            assign(e.ref('_loc12_'), '=', lambda: 'sub')
                                            rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_item': 'battle', '_player': ref(e.get('_loc3_'), 'playerNum').get(), '_weapon': ref(ref(e.get('_loc8_'), 'preAttackCarrier').get(), 'weaponID').get(), '_action': 1, '_dontReduce': True})])
                                        else:
                                            if truth(binop('==', ref(ref(e.get('_loc8_'), 'preAttackCarrier').get(), 'weaponType').get(), 'ship')):
                                                assign(e.ref('_loc12_'), '=', lambda: 'ship')
                                                rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_item': 'battle', '_player': ref(e.get('_loc3_'), 'playerNum').get(), '_weapon': ref(ref(e.get('_loc8_'), 'preAttackCarrier').get(), 'weaponID').get(), '_action': 1, '_dontReduce': True, '_dontBeAnAss': True})])
                                            else:
                                                assign(e.ref('_loc12_'), '=', lambda: ref(ref(e.get('_loc8_'), 'preAttackCarrier').get(), 'weaponType').get())
                                rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'setPreAttack', '_value': 'ready', '_a': ref(e.get('_loc3_'), 'playerNum').get(), '_b': ref(ref(e.get('_loc8_'), 'targetPlayer').get(), 'playerNum').get(), '_weapon': ref(ref(e.get('_loc8_'), 'preAttackCarrier').get(), 'weaponID').get(), '_carrier': e.get('_loc9_'), '_payload': e.get('_loc10_'), '_city': ref(ref(e.get('_loc8_'), 'targetCity').get(), 'cityID').get(), '_frame': e.get('_loc12_'), '_blocked': False})])
                            else:
                                if truth(binop('==', ref(e.get('_loc3_'), 'preAttackStatus').get(), 'ready')):
                                    assign(ref(e.get('_loc3_'), 'preBuilding_this_turn'), '=', lambda: True)
                                    assign(e.ref('_loc13_'), '=', lambda: ref(ref(e.get('_loc8_'), 'preAttackCarrier').get(), 'weaponID').get())
                                    assign(e.ref('_loc14_'), '=', lambda: ref(ref(e.get('_loc8_'), 'preAttackPayload').get(), 'weaponID').get())
                                    assign(e.ref('_loc15_'), '=', lambda: ref(ref(e.get('_loc8_'), 'targetCity').get(), 'cityID').get())
                                    assign(e.ref('_loc17_'), '=', lambda: False)
                                    if truth(binop('==', ref(ref(e.get('_loc8_'), 'preAttackCarrier').get(), 'weaponType').get(), 'rocket')):
                                        assign(e.ref('_loc16_'), '=', lambda: 'silo')
                                    else:
                                        if truth(binop('==', ref(ref(e.get('_loc8_'), 'preAttackCarrier').get(), 'weaponType').get(), 'plane')):
                                            assign(e.ref('_loc16_'), '=', lambda: 'airfield')
                                        else:
                                            if truth(binop('==', ref(ref(e.get('_loc8_'), 'preAttackCarrier').get(), 'weaponType').get(), 'sub')):
                                                assign(e.ref('_loc20_'), '=', lambda: 2)
                                            else:
                                                if truth(binop('==', ref(ref(e.get('_loc8_'), 'preAttackCarrier').get(), 'weaponType').get(), 'ship')):
                                                    assign(e.ref('_loc17_'), '=', lambda: True)
                                                    assign(e.ref('_loc18_'), '=', lambda: rt.construct(e.get('Array'), []))
                                                    assign(e.ref('_loc19_'), '=', lambda: 2)
                                                else:
                                                    assign(e.ref('_loc16_'), '=', lambda: ref(ref(e.get('_loc8_'), 'preAttackCarrier').get(), 'weaponType').get())
                                    rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'battle', '_value': 'preAttack', '_a': ref(e.get('_loc3_'), 'playerNum').get(), '_b': ref(ref(e.get('_loc8_'), 'targetPlayer').get(), 'playerNum').get(), '_weapon': e.get('_loc13_'), '_carrier': e.get('_loc13_'), '_payload': e.get('_loc14_'), '_city': ref(ref(e.get('_loc8_'), 'targetCity').get(), 'cityID').get(), '_blocked': False, '_casualties': 0, '_frame': e.get('_loc16_'), '_result': True, '_isShip': e.get('_loc17_'), '_attack_arr': ref(e.get('_loc8_'), 'ship_attack_arr').get(), '_result_arr': e.get('_loc18_'), '_action': e.get('_loc20_')})])
                                    rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'setPreAttack', '_value': 'inactive'})])
                                    rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'regard', '_a': ref(e.get('_loc3_'), 'playerNum').get(), '_b': ref(ref(e.get('_loc8_'), 'targetPlayer').get(), 'playerNum').get()})])
                                    rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'regard', '_value': 'preAttack', '_a': ref(e.get('_loc3_'), 'playerNum').get(), '_b': ref(ref(e.get('_loc8_'), 'targetPlayer').get(), 'playerNum').get(), '_wpnLevel': ref(ref(e.get('_loc8_'), 'preAttackPayload').get(), 'weaponLevel').get()})])
                            raise ASBreak()
                        if 0 <= case_9 <= 6:
                            rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'battle', '_value': 'attack', '_a': ref(e.get('_loc3_'), 'playerNum').get(), '_b': ref(ref(e.get('_loc8_'), 'targetPlayer').get(), 'playerNum').get(), '_weapon': ref(ref(e.get('_loc8_'), 'attackWeapon').get(), 'weaponID').get(), '_city': ref(ref(e.get('_loc8_'), 'targetCity').get(), 'cityID').get(), '_casualties': 0, '_result': True, '_spyArr': e.get('undefined'), '_spyBuilding': ref(e.get('_loc8_'), 'spyBuilding').get()})])
                            rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'regard', '_value': 'attack', '_a': ref(e.get('_loc3_'), 'playerNum').get(), '_b': ref(ref(e.get('_loc8_'), 'targetPlayer').get(), 'playerNum').get(), '_wpnLevel': ref(ref(e.get('_loc8_'), 'attackWeapon').get(), 'weaponLevel').get()})])
                            if truth(binop('==', ref(ref(e.get('_loc8_'), 'attackWeapon').get(), 'weaponType').get(), 'spy')):
                                rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'reset_spy_readiness', '_value': 0})])
                            raise ASBreak()
                        if 0 <= case_9 <= 7:
                            rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'defense', '_value': ref(ref(e.get('_loc8_'), 'attackWeapon').get(), 'weaponID').get(), '_result': False, '_frame': ref(ref(e.get('_loc8_'), 'attackWeapon').get(), 'weaponName').get()})])
                            raise ASBreak()
                        if 0 <= case_9 <= 8:
                            rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'defense', '_value': ref(ref(e.get('_loc8_'), 'attackWeapon').get(), 'weaponID').get(), '_results': False, '_frame': ref(ref(e.get('_loc8_'), 'attackWeapon').get(), 'weaponName').get()})])
                            rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'regard', '_value': 'propaganda', '_a': ref(e.get('_loc3_'), 'playerNum').get(), '_b': ref(ref(e.get('_loc8_'), 'targetPlayer').get(), 'playerNum').get()})])
                            raise ASBreak()
                        if 0 <= case_9 <= 9:
                            rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'propaganda', '_a': ref(e.get('_loc3_'), 'playerNum').get(), '_b': ref(ref(e.get('_loc8_'), 'targetPlayer').get(), 'playerNum').get(), '_city': ref(ref(e.get('_loc8_'), 'targetCity').get(), 'cityID').get(), '_value': 0})])
                            raise ASBreak()
                        if 0 <= case_9 <= 10:
                            rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'diplomacy', '_value': 'call', '_leader': ref(e.get('_loc8_'), 'diplomacyLeader').get(), '_option': ref(e.get('_loc8_'), 'diplomacyOption').get()})])
                            rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_player': ref(e.get('_loc3_'), 'playerNum').get(), '_item': 'regard', '_value': 'diplomacy', '_a': ref(e.get('_loc3_'), 'playerNum').get(), '_b': ref(e.get('_loc8_'), 'diplomacyLeader').get(), '_diplomacy': True})])
                    except ASBreak:
                        pass
                except ASContinue:
                    pass
                except ASBreak:
                    break
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_13 in keys(ref(ref(this, 'model').get(), 'turnResultsArr').get()):
        e.ref('i').set(key_13)
        rt.tick()
        try:
            assign(e.ref('_loc21_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), e.get('i')).get())
            switch_14 = ref(e.get('_loc21_'), '_item').get()
            case_15 = -1
            if case_15 == -1 and strict_eq(switch_14, 'resources'):
                case_15 = 0
            if case_15 == -1 and strict_eq(switch_14, 'religion'):
                case_15 = 1
            if case_15 == -1 and strict_eq(switch_14, 'battle'):
                case_15 = 2
            if case_15 == -1 and strict_eq(switch_14, 'propaganda'):
                case_15 = 3
            if case_15 == -1 and strict_eq(switch_14, 'diplomacy'):
                case_15 = 4
            if case_15 == -1:
                case_15 = -1
            try:
                if 0 <= case_15 <= 0:
                    if truth(binop('==', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_player').get()).get(), 'playedBy').get(), 'human')):
                        assign(ref(e.get('_loc21_'), '_value'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [binop('/', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_player').get()).get(), 'population').get(), ref(ref(ref(ref(this, 'model').get(), 'difficulty_level_specific_vars').get(), 'player_resources_divider').get(), ref(ref(this, 'model').get(), 'difficulty_level').get()).get())]))
                    else:
                        assign(ref(e.get('_loc21_'), '_value'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [binop('/', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_player').get()).get(), 'population').get(), ref(ref(ref(ref(this, 'model').get(), 'difficulty_level_specific_vars').get(), 'enemy_resources_divider').get(), ref(ref(this, 'model').get(), 'difficulty_level').get()).get())]))
                    assign(ref(e.get('_loc21_'), '_plusmin'), '=', lambda: 'plus')
                    raise ASBreak()
                if 0 <= case_15 <= 1:
                    if truth(binop('==', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_player').get()).get(), 'playedBy').get(), 'human')):
                        assign(ref(e.get('_loc21_'), '_value'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'difficulty_level_specific_vars').get(), 'player_religion_addition').get(), ref(ref(this, 'model').get(), 'difficulty_level').get()).get())
                    else:
                        assign(ref(e.get('_loc21_'), '_value'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'difficulty_level_specific_vars').get(), 'enemy_religion_addition').get(), ref(ref(this, 'model').get(), 'difficulty_level').get()).get())
                    raise ASBreak()
                if 0 <= case_15 <= 2:
                    if truth(logical('&&', binop('==', ref(e.get('_loc21_'), '_value').get(), 'preAttack'), lambda: unary('!', ref(e.get('_loc21_'), '_isShip').get()))):
                        assign(e.ref('_loc22_'), '=', lambda: rt.call_ref(ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_player').get()).get(), 'weaponStock').get(), 'getWeaponByID'), [ref(e.get('_loc21_'), '_payload').get()]))
                        assign(e.ref('_loc23_'), '=', lambda: ref(e.get('_loc22_'), 'maxKills').get())
                        if truth(logical('&&', binop('==', ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_a').get()).get(), 'playedBy').get(), 'AI'), lambda: binop('==', ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_b').get()).get(), 'playedBy').get(), 'human'))):
                            assign(ref(e.get('_loc21_'), '_casualties'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [e.get('_loc23_'), binop('*', e.get('_loc23_'), 1.2)])]))
                        else:
                            assign(ref(e.get('_loc21_'), '_casualties'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [binop('/', e.get('_loc23_'), 1.5), e.get('_loc23_')])]))
                        if truth(logical('||', unary('!', ref(e.get('_loc21_'), '_casualties').get()), lambda: rt.call_ref(ref(e.get('_global'), 'isNaN'), [ref(e.get('_loc21_'), '_casualties').get()]))):
                            assign(ref(e.get('_loc21_'), '_casualties'), '=', lambda: 0)
                        for key_16 in keys(ref(ref(this, 'model').get(), 'turnResultsArr').get()):
                            e.ref('j').set(key_16)
                            rt.tick()
                            try:
                                if truth(binop('==', ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), e.get('j')).get(), '_item').get(), 'defense')):
                                    assign(e.ref('_loc24_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), e.get('j')).get())
                                    if truth(logical('&&', binop('==', ref(rt.call_ref(ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc24_'), '_player').get()).get(), 'weaponStock').get(), 'getWeaponByID'), [ref(e.get('_loc24_'), '_value').get()]), 'weaponName').get(), ref(rt.call_ref(ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_player').get()).get(), 'weaponStock').get(), 'getWeaponByID'), [ref(e.get('_loc21_'), '_carrier').get()]), 'counteredBy').get()), lambda: binop('==', ref(e.get('_loc21_'), '_b').get(), ref(e.get('_loc24_'), '_player').get()))):
                                        if truth(ref(e.get('_loc21_'), '_isShip').get()):
                                            assign(e.ref('_loc25_'), '=', lambda: 0)
                                            while truth(binop('<', e.get('_loc25_'), 3)):
                                                rt.tick()
                                                try:
                                                    if truth(binop('==', rt.call_ref(ref(ref(ref(this, 'model').get(), 'tools').get(), 'randRange'), [0, 3]), 3)):
                                                        rt.call_ref(ref(ref(e.get('_loc21_'), '_result_arr').get(), 'push'), [obj({'_num': e.get('_loc25_'), '_result': False, '_casualties': 0})])
                                                        assign(ref(e.get('_loc24_'), '_restult'), '=', lambda: True)
                                                    else:
                                                        rt.call_ref(ref(ref(e.get('_loc21_'), '_result_arr').get(), 'push'), [obj({'_num': e.get('_loc25_'), '_result': True, '_casualties': rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [binop('/', ref(e.get('_loc22_'), 'maxKills').get(), 2), ref(e.get('_loc22_'), 'maxKills').get()])})])
                                                    assign(e.ref('_loc25_'), '=', lambda: binop('+', e.get('_loc25_'), 1))
                                                except ASContinue:
                                                    pass
                                                except ASBreak:
                                                    break
                                            raise ASBreak()
                                        if truth(binop('!=', rt.call_ref(ref(ref(ref(this, 'model').get(), 'tools').get(), 'randRange'), [1, 9]), 5)):
                                            assign(ref(e.get('_loc21_'), '_casualties'), '=', lambda: 0)
                                            assign(ref(e.get('_loc21_'), '_result'), '=', lambda: False)
                                            assign(ref(e.get('_loc24_'), '_result'), '=', lambda: True)
                                            raise ASBreak()
                                        assign(ref(e.get('_loc21_'), '_result'), '=', lambda: True)
                                        assign(ref(e.get('_loc24_'), '_result'), '=', lambda: True)
                                        assign(ref(e.get('_loc21_'), '_pass_anti'), '=', lambda: True)
                                        raise ASBreak()
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        assign(e.ref('_loc26_'), '=', lambda: rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'weaponStock').get(), 'getWeaponByID'), [ref(e.get('_loc21_'), '_payload').get()]))
                        if truth(logical('&&', binop('==', rt.call_ref(ref(ref(e.get('_loc26_'), 'weaponName').get(), 'slice'), [0, unary('-', 1)]), 'bioload'), lambda: ref(e.get('_loc21_'), '_result').get())):
                            if truth(binop('==', ref(rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'weaponStock').get(), 'getWeaponByID'), [ref(e.get('_loc21_'), '_weapon').get()]), 'weaponName').get(), 'sub')):
                                for key_17 in keys(ref(ref(this, 'model').get(), 'turnResultsArr').get()):
                                    e.ref('q').set(key_17)
                                    rt.tick()
                                    try:
                                        assign(e.ref('_loc27_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), e.get('q')).get())
                                        if truth(logical('&&', binop('==', ref(e.get('_loc27_'), '_player').get(), ref(e.get('_loc21_'), '_player').get()), lambda: ref(e.get('_loc27_'), '_isSub').get())):
                                            assign(ref(e.get('_loc27_'), '_bioload'), '=', lambda: True)
                                    except ASContinue:
                                        pass
                                    except ASBreak:
                                        break
                            assign(ref(e.get('_loc21_'), '_bioload'), '=', lambda: True)
                            assign(e.ref('_loc28_'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'createBioHazardArr'), [e.call('Number', [rt.call_ref(ref(ref(e.get('_loc26_'), 'weaponName').get(), 'substr'), [binop('-', ref(ref(e.get('_loc26_'), 'weaponName').get(), 'length').get(), 1), 1])])]))
                            assign(ref(rt.call_ref(ref(ref(this, 'model').get(), 'getCityByID'), [ref(e.get('_loc21_'), '_city').get()]), 'bioload_in_battle'), '=', lambda: True)
                            rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_item': 'bioload', '_value': 'deactivate', '_plr': ref(e.get('_loc21_'), '_b').get(), '_arr': e.get('_loc28_')})])
                    else:
                        if truth(ref(e.get('_loc21_'), '_isShip').get()):
                            assign(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_player').get()).get(), 'shipFrame'), '=', lambda: 2)
                            assign(ref(e.get('_loc21_'), '_action'), '=', lambda: 2)
                            assign(e.ref('_loc29_'), '=', lambda: False)
                            for key_18 in keys(ref(ref(this, 'model').get(), 'turnResultsArr').get()):
                                e.ref('k2').set(key_18)
                                rt.tick()
                                try:
                                    if truth(logical('&&', binop('==', ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), e.get('k2')).get(), '_item').get(), 'defense'), lambda: binop('==', ref(e.get('_loc21_'), '_b').get(), ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), e.get('k2')).get(), '_player').get()))):
                                        assign(e.ref('_loc30_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), e.get('k2')).get())
                                        if truth(binop('==', ref(rt.call_ref(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_a').get()).get(), 'weaponStock').get(), 'getWeaponByID'), [ref(e.get('_loc30_'), '_value').get()]), 'weaponName').get(), 'antiAir')):
                                            assign(e.ref('_loc29_'), '=', lambda: True)
                                            assign(ref(e.get('_loc30_'), '_result'), '=', lambda: True)
                                except ASContinue:
                                    pass
                                except ASBreak:
                                    break
                            assign(e.ref('_loc31_'), '=', lambda: 0)
                            while truth(binop('<', e.get('_loc31_'), 3)):
                                rt.tick()
                                try:
                                    assign(e.ref('_loc32_'), '=', lambda: rt.call_ref(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_player').get()).get(), 'weaponStock').get(), 'getWeaponByID'), [ref(ref(ref(e.get('_loc21_'), '_attack_arr').get(), e.get('_loc31_')).get(), 'wpn').get()]))
                                    assign(e.ref('_loc33_'), '=', lambda: True)
                                    assign(e.ref('_loc34_'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [rt.call_ref(ref(ref(ref(this, 'model').get(), 'tools').get(), 'randRange'), [binop('/', ref(e.get('_loc32_'), 'maxKills').get(), 2), ref(e.get('_loc32_'), 'maxKills').get()])]))
                                    assign(e.ref('_loc35_'), '=', lambda: rt.call_ref(ref(ref(ref(this, 'model').get(), 'tools').get(), 'randRange'), [1, 3]))
                                    if truth(logical('&&', e.get('_loc29_'), lambda: binop('==', e.get('_loc35_'), 2))):
                                        assign(e.ref('_loc33_'), '=', lambda: False)
                                        assign(e.ref('_loc34_'), '=', lambda: 0)
                                    rt.call_ref(ref(ref(e.get('_loc21_'), '_result_arr').get(), 'push'), [obj({'_num': e.get('_loc31_'), '_result': e.get('_loc33_'), '_casualties': e.get('_loc34_')})])
                                    if truth(logical('&&', binop('==', rt.call_ref(ref(ref(e.get('_loc32_'), 'weaponName').get(), 'slice'), [0, unary('-', 1)]), 'bioload'), lambda: e.get('_loc33_'))):
                                        assign(ref(ref(ref(e.get('_loc21_'), '_attack_arr').get(), e.get('_loc31_')).get(), '_bioload'), '=', lambda: True)
                                        assign(e.ref('_loc36_'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'createBioHazardArr'), [e.call('Number', [rt.call_ref(ref(ref(e.get('_loc32_'), 'weaponName').get(), 'substr'), [binop('-', ref(ref(e.get('_loc32_'), 'weaponName').get(), 'length').get(), 1), 1])])]))
                                        assign(ref(rt.call_ref(ref(ref(this, 'model').get(), 'getCityByID'), [ref(ref(ref(e.get('_loc21_'), '_attack_arr').get(), e.get('_loc31_')).get(), 'city').get()]), 'bioload_in_battle'), '=', lambda: True)
                                        rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_item': 'bioload', '_value': 'deactivate', '_plr': ref(e.get('_loc21_'), '_b').get(), '_arr': e.get('_loc36_')})])
                                    assign(e.ref('_loc31_'), '=', lambda: binop('+', e.get('_loc31_'), 1))
                                except ASContinue:
                                    pass
                                except ASBreak:
                                    break
                        else:
                            if truth(binop('==', ref(e.get('_loc21_'), '_value').get(), 'attack')):
                                assign(e.ref('_loc37_'), '=', lambda: rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'weaponStock').get(), 'getWeaponByID'), [ref(e.get('_loc21_'), '_weapon').get()]))
                                if truth(binop('!=', ref(e.get('_loc37_'), 'weaponType').get(), 'spy')):
                                    assign(ref(e.get('_loc21_'), '_casualties'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [binop('/', ref(e.get('_loc37_'), 'maxKills').get(), 2), ref(e.get('_loc37_'), 'maxKills').get()])]))
                                else:
                                    assign(ref(e.get('_loc21_'), '_spyArr'), '=', lambda: rt.call_ref(ref(this, 'createSpyStealArray'), [ref(e.get('_loc21_'), '_a').get(), ref(e.get('_loc21_'), '_b').get(), ref(e.get('_loc37_'), 'weaponLevel').get()]))
                                    assign(ref(e.get('_loc21_'), '_casualties'), '=', lambda: 0)
                                    assign(ref(e.get('_loc21_'), '_frame'), '=', lambda: ref(e.get('_loc21_'), '_spyBuilding').get())
                    if truth(ref(e.get('_loc21_'), '_attack_arr').get()):
                        for key_19 in keys(ref(e.get('_loc21_'), '_attack_arr').get()):
                            e.ref('j').set(key_19)
                            rt.tick()
                            try:
                                assign(e.ref('_loc38_'), '=', lambda: rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'weaponStock').get(), 'getWeaponByID'), [ref(ref(ref(e.get('_loc21_'), '_attack_arr').get(), e.get('j')).get(), 'wpn').get()]))
                                if truth(binop('==', rt.call_ref(ref(ref(e.get('_loc38_'), 'weaponName').get(), 'slice'), [0, unary('-', 1)]), 'bioload')):
                                    assign(ref(ref(ref(e.get('_loc21_'), '_attack_arr').get(), e.get('j')).get(), '_bioload'), '=', lambda: True)
                                    assign(e.ref('_loc39_'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'createBioHazardArr'), [e.call('Number', [rt.call_ref(ref(ref(e.get('_loc38_'), 'weaponName').get(), 'substr'), [binop('-', ref(ref(e.get('_loc38_'), 'weaponName').get(), 'length').get(), 1), 1])])]))
                                    assign(ref(rt.call_ref(ref(ref(this, 'model').get(), 'getCityByID'), [ref(ref(ref(e.get('_loc21_'), '_attack_arr').get(), e.get('j')).get(), 'city').get()]), 'bioload_in_battle'), '=', lambda: True)
                                    rt.call_ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), 'push'), [obj({'_item': 'bioload', '_value': 'deactivate', '_plr': ref(e.get('_loc21_'), '_b').get(), '_arr': e.get('_loc39_')})])
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                    if truth(logical('&&', unary('!', rt.call_ref(ref(e.get('_global'), 'isNaN'), [ref(e.get('_loc21_'), '_casualties').get()])), lambda: ref(e.get('_loc21_'), '_casualties').get())):
                        assign(e.ref('_loc40_'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'getCityByID'), [ref(e.get('_loc21_'), '_city').get()]))
                        if truth(binop('>', ref(e.get('_loc21_'), '_casualties').get(), binop('-', ref(e.get('_loc40_'), 'population').get(), ref(e.get('_loc40_'), 'battle_loop_casualties').get()))):
                            assign(ref(e.get('_loc21_'), '_casualties'), '=', lambda: binop('-', ref(e.get('_loc40_'), 'population').get(), ref(e.get('_loc40_'), 'battle_loop_casualties').get()))
                            assign(ref(e.get('_loc40_'), 'propaganda_exclude'), '=', lambda: True)
                        assign(ref(e.get('_loc40_'), 'battle_loop_casualties'), '+=', lambda: ref(e.get('_loc21_'), '_casualties').get())
                        assign(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_b').get()).get(), 'turnBattleCasualties'), '+=', lambda: ref(e.get('_loc21_'), '_casualties').get())
                        assign(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_a').get()).get(), 'turnBattleKills'), '+=', lambda: ref(e.get('_loc21_'), '_casualties').get())
                        if truth(logical('||', unary('!', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_b').get()).get(), 'lastAttackedBy_casualties').get()), lambda: binop('<', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_b').get()).get(), 'lastAttackedBy_casualties').get(), ref(e.get('_loc21_'), '_casualties').get()))):
                            assign(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_b').get()).get(), 'lastAttackedBy_num'), '=', lambda: ref(e.get('_loc21_'), '_a').get())
                            assign(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_b').get()).get(), 'lastAttackedBy_casualties'), '=', lambda: ref(e.get('_loc21_'), '_casualties').get())
                        rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'addToHighscore'), [ref(e.get('_loc21_'), '_a').get(), 1, ref(e.get('_loc21_'), '_casualties').get()])
                    if truth(ref(e.get('_loc21_'), '_isShip').get()):
                        assign(e.ref('_loc41_'), '=', lambda: 0)
                        while truth(binop('<', e.get('_loc41_'), ref(ref(e.get('_loc21_'), '_result_arr').get(), 'length').get())):
                            rt.tick()
                            try:
                                if truth(logical('&&', unary('!', rt.call_ref(ref(e.get('_global'), 'isNaN'), [ref(ref(ref(e.get('_loc21_'), '_result_arr').get(), e.get('_loc41_')).get(), '_casualties').get()])), lambda: ref(ref(ref(e.get('_loc21_'), '_result_arr').get(), e.get('_loc41_')).get(), '_casualties').get())):
                                    assign(e.ref('_loc42_'), '=', lambda: rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(ref(e.get('_loc21_'), '_attack_arr').get(), e.get('_loc41_')).get(), 'city').get()]))
                                    if truth(binop('>', ref(ref(ref(e.get('_loc21_'), '_result_arr').get(), e.get('_loc41_')).get(), '_casualties').get(), binop('-', ref(e.get('_loc42_'), 'population').get(), ref(e.get('_loc42_'), 'battle_loop_casualties').get()))):
                                        assign(ref(ref(ref(e.get('_loc21_'), '_result_arr').get(), e.get('_loc41_')).get(), '_casualties'), '=', lambda: binop('-', ref(e.get('_loc42_'), 'population').get(), ref(e.get('_loc42_'), 'battle_loop_casualties').get()))
                                        assign(ref(e.get('_loc42_'), 'propaganda_exclude'), '=', lambda: True)
                                    assign(ref(e.get('_loc42_'), 'battle_loop_casualties'), '+=', lambda: ref(ref(ref(e.get('_loc21_'), '_result_arr').get(), e.get('_loc41_')).get(), '_casualties').get())
                                    assign(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_b').get()).get(), 'turnBattleCasualties'), '+=', lambda: ref(ref(ref(e.get('_loc21_'), '_result_arr').get(), e.get('_loc41_')).get(), '_casualties').get())
                                    assign(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_a').get()).get(), 'turnBattleKills'), '+=', lambda: ref(ref(ref(e.get('_loc21_'), '_result_arr').get(), e.get('_loc41_')).get(), '_casualties').get())
                                    if truth(logical('||', unary('!', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_b').get()).get(), 'lastAttackedBy_casualties').get()), lambda: binop('<', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_b').get()).get(), 'lastAttackedBy_casualties').get(), ref(ref(ref(e.get('_loc21_'), '_result_arr').get(), e.get('_loc41_')).get(), '_casualties').get()))):
                                        assign(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_b').get()).get(), 'lastAttackedBy_num'), '=', lambda: ref(e.get('_loc21_'), '_a').get())
                                        assign(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc21_'), '_b').get()).get(), 'lastAttackedBy_casualties'), '=', lambda: ref(ref(ref(e.get('_loc21_'), '_result_arr').get(), e.get('_loc41_')).get(), '_casualties').get())
                                    rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'addToHighscore'), [ref(e.get('_loc21_'), '_a').get(), 1, ref(ref(ref(e.get('_loc21_'), '_result_arr').get(), e.get('_loc41_')).get(), '_casualties').get()])
                                assign(e.ref('_loc41_'), '=', lambda: binop('+', e.get('_loc41_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                    raise ASBreak()
                if 0 <= case_15 <= 3:
                    raise ASBreak()
                if 0 <= case_15 <= 4:
                    pass
            except ASBreak:
                pass
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_20 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_20)
        rt.tick()
        try:
            assign(e.ref('_loc43_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get())
            assign(e.ref('_loc44_'), '=', lambda: True)
            assign(e.ref('_loc45_'), '=', lambda: True)
            if truth(logical('&&', binop('==', ref(e.get('_loc43_'), 'preAttackStatus').get(), 'ready'), lambda: ref(e.get('_loc43_'), 'alive').get())):
                if truth(binop('==', ref(ref(e.get('_loc43_'), 'turnAction_1').get(), 'action').get(), 'preAttack')):
                    assign(e.ref('_loc44_'), '=', lambda: False)
                if truth(binop('==', ref(ref(e.get('_loc43_'), 'turnAction_2').get(), 'action').get(), 'preAttack')):
                    assign(e.ref('_loc45_'), '=', lambda: False)
                if truth(e.get('_loc44_')):
                    rt.call_ref(ref(ref(e.get('_loc43_'), 'turnAction_1').get(), 'doReset'), [])
                else:
                    if truth(e.get('_loc45_')):
                        rt.call_ref(ref(ref(e.get('_loc43_'), 'turnAction_2').get(), 'doReset'), [])
                assign(ref(e.get('_loc43_'), 'preAttackStatus'), '=', lambda: 'inactive')
            if truth(binop('==', ref(e.get('_loc43_'), 'playerNum').get(), 0)):
                pass
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Sub_presenter_createSpyStealArray(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['plr_a_nr', 'plr_b_nr', 'spyLevel'], ['_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc14_', '_loc15_', '_loc16_', '_loc17_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', 'i', 'k', 'm', 'plr_a_nr', 'plr_b_nr', 'spyLevel'], closure, 'Sub_presenter')
    e.set('_loc5_', rt.construct(e.get('Array'), []))
    e.set('_loc6_', rt.construct(e.get('Array'), []))
    e.set('_loc7_', rt.construct(e.get('Array'), []))
    e.set('_loc8_', ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('plr_b_nr')).get())
    e.set('_loc10_', ref(ref(ref(this, 'model').get(), 'spy_stat_obj').get(), binop('+', 'spy', e.get('spyLevel'))).get())
    e.set('_loc11_', rt.call_ref(ref(ref(ref(this, 'model').get(), 'tools').get(), 'randRange'), [1, ref(e.get('_loc10_'), 'weaponStealMax').get()]))
    if truth(ref(e.get('_loc8_'), 'special_person').get()):
        assign(e.ref('_loc11_'), '=', lambda: 1)
    e.set('_loc12_', 0)
    e.set('_loc13_', 'resources')
    e.set('_loc15_', rt.call_ref(ref(e.get('Math'), 'round'), [binop('*', binop('/', ref(e.get('_loc8_'), 'money').get(), 100), rt.call_ref(ref(ref(ref(this, 'model').get(), 'tools').get(), 'randRange'), [binop('*', e.get('spyLevel'), 10), ref(e.get('_loc10_'), 'moneyStealPrcMax').get()]))]))
    if truth(binop('>', e.get('_loc15_'), ref(ref(ref(ref(e.get('_global'), 'model').get(), 'difficulty_level_specific_vars').get(), 'spy_steal_money_max').get(), ref(ref(e.get('_global'), 'model').get(), 'difficulty_level').get()).get())):
        assign(e.ref('_loc15_'), '=', lambda: ref(ref(ref(ref(e.get('_global'), 'model').get(), 'difficulty_level_specific_vars').get(), 'spy_steal_money_max').get(), ref(ref(e.get('_global'), 'model').get(), 'difficulty_level').get()).get())
    rt.call_ref(ref(e.get('_loc7_'), 'push'), [e.get('_loc15_')])
    if truth(logical('&&', ref(e.get('_loc8_'), 'special_person').get(), lambda: binop('>', e.get('_loc15_'), 20))):
        assign(e.ref('_loc15_'), '=', lambda: 20)
    for key_21 in keys(ref(ref(e.get('_loc8_'), 'weaponStock').get(), 'weaponArr').get()):
        e.ref('i').set(key_21)
        rt.tick()
        try:
            assign(e.ref('_loc9_'), '=', lambda: ref(ref(ref(e.get('_loc8_'), 'weaponStock').get(), 'weaponArr').get(), e.get('i')).get())
            if truth(unary('!', ref(e.get('_loc8_'), 'special_person').get())):
                if truth(logical('&&', binop('<=', ref(e.get('_loc9_'), 'weaponLevel').get(), e.get('spyLevel')), lambda: logical('&&', binop('>', ref(e.get('_loc9_'), 'inStock').get(), 0), lambda: binop('!=', ref(e.get('_loc9_'), 'weaponType').get(), 'spy')))):
                    rt.call_ref(ref(e.get('_loc5_'), 'push'), [ref(e.get('_loc9_'), 'weaponID').get()])
            else:
                if truth(logical('&&', binop('<=', ref(e.get('_loc9_'), 'weaponLevel').get(), 1), lambda: logical('&&', binop('>', ref(e.get('_loc9_'), 'inStock').get(), 0), lambda: binop('!=', ref(e.get('_loc9_'), 'weaponType').get(), 'spy')))):
                    rt.call_ref(ref(e.get('_loc5_'), 'push'), [ref(e.get('_loc9_'), 'weaponID').get()])
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_22 in keys(ref(ref(this, 'model').get(), 'turnResultsArr').get()):
        e.ref('k').set(key_22)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), e.get('k')).get(), '_player').get(), e.get('plr_a_nr'))):
                assign(e.ref('_loc16_'), '=', lambda: 0)
                while truth(binop('<', e.get('_loc16_'), ref(ref(ref(this, 'model').get(), 'spyActions_arr').get(), 'length').get())):
                    rt.tick()
                    try:
                        if truth(binop('==', ref(ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), e.get('k')).get(), '_item').get(), ref(ref(ref(this, 'model').get(), 'spyActions_arr').get(), e.get('_loc16_')).get())):
                            assign(e.ref('_loc14_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'spyActions_arr').get(), e.get('_loc16_')).get())
                            raise ASBreak()
                        assign(e.ref('_loc16_'), '=', lambda: binop('+', e.get('_loc16_'), 1))
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_23 in keys(ref(ref(this, 'model').get(), 'spyActions_arr').get()):
        e.ref('m').set(key_23)
        rt.tick()
        try:
            if truth(binop('!=', ref(ref(ref(this, 'model').get(), 'spyActions_arr').get(), e.get('m')).get(), e.get('_loc14_'))):
                rt.call_ref(ref(e.get('_loc6_'), 'push'), [ref(ref(ref(this, 'model').get(), 'spyActions_arr').get(), e.get('m')).get()])
        except ASContinue:
            pass
        except ASBreak:
            break
    rt.call_ref(ref(e.get('_loc7_'), 'push'), [ref(e.get('_loc6_'), rt.call_ref(ref(ref(ref(this, 'model').get(), 'tools').get(), 'randRange'), [0, binop('-', ref(e.get('_loc6_'), 'length').get(), 1)])).get()])
    if truth(binop('<', ref(e.get('_loc5_'), 'length').get(), e.get('_loc11_'))):
        assign(e.ref('_loc11_'), '=', lambda: ref(e.get('_loc5_'), 'length').get())
    e.set('_loc17_', 0)
    while truth(binop('<', e.get('_loc17_'), e.get('_loc11_'))):
        rt.tick()
        try:
            assign(e.ref('_loc12_'), '=', lambda: rt.call_ref(ref(ref(ref(this, 'model').get(), 'tools').get(), 'randRange'), [0, binop('-', ref(e.get('_loc5_'), 'length').get(), 1)]))
            rt.call_ref(ref(e.get('_loc7_'), 'push'), [ref(e.get('_loc5_'), e.get('_loc12_')).get()])
            rt.call_ref(ref(e.get('_loc5_'), 'splice'), [e.get('_loc12_'), 1])
            rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'addToHighscore'), [e.get('plr_a_nr'), 2, 1])
            assign(e.ref('_loc17_'), '=', lambda: binop('+', e.get('_loc17_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc7_')
    return U

def Sub_presenter_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_presenter')
    pass

def register(rt):
    rt.define('Sub_presenter', None, Sub_presenter_fields, {'Sub_presenter': ASFunction(Sub_presenter_Sub_presenter), 'turnResults': ASFunction(Sub_presenter_turnResults), 'createSpyStealArray': ASFunction(Sub_presenter_createSpyStealArray)}, {}, {})
