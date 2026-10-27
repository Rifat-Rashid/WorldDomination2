# Generated from __Packages/Sub_model.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Sub_model_Sub_model(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    assign(ref(this, 'MD5'), '=', lambda: rt.construct(e.get('MD5_class'), []))
    return U

def Sub_model_get_demo_version_name(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    return ref(ref(this, 'demo_version_arr').get(), ref(this, 'demo_version').get()).get()
    return U

def Sub_model_get_demo_version_url(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_'], closure, 'Sub_model')
    if truth(binop('==', ref(this, 'demo_version').get(), 0)):
        assign(e.ref('_loc2_'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'unescape'), [ref(e.get('_root'), '_url').get()]))
        assign(e.ref('_loc3_'), '=', lambda: rt.call_ref(ref(e.get('_loc2_'), 'lastIndexOf'), ['_']))
        assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(e.get('_loc2_'), 'lastIndexOf'), ['.swf']))
        assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(e.get('_loc2_'), 'slice'), [0, e.get('_loc4_')]))
        assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(e.get('_loc5_'), 'slice'), [binop('+', e.get('_loc3_'), 1)]))
        return binop('+', 'https://secure.bmtmicro.com/servlets/Orders.ShoppingCart?CLR=0&CID=2249&PRODUCTID=22490032&AID=', e.get('_loc6_'))
    return ref(ref(this, 'demo_version_url').get(), ref(this, 'demo_version').get()).get()
    return U

def Sub_model___get__full_version_url(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    switch_1 = rt.call_ref(ref(this, 'get_demo_version_name'), [])
    case_2 = -1
    if case_2 == -1 and strict_eq(switch_1, 'Affiliates'):
        case_2 = 0
    if case_2 == -1 and strict_eq(switch_1, 'Miniclip'):
        case_2 = 1
    if case_2 == -1 and strict_eq(switch_1, 'Arcadetown'):
        case_2 = 2
    if case_2 == -1 and strict_eq(switch_1, 'Agame'):
        case_2 = 3
    if case_2 == -1:
        case_2 = 4
    try:
        if 0 <= case_2 <= 0:
            return 'http://www.youdagames.com/World+Domination+2-game-info-107/'
        if 0 <= case_2 <= 1:
            return 'http://www.miniclip.com/buy_worlddominationii.htm'
        if 0 <= case_2 <= 2:
            return 'http://www.arcadetown.com/worlddomination2/ordergame.asp'
        if 0 <= case_2 <= 3:
            return 'http://moregames.agame.com'
        if 0 <= case_2 <= 4:
            return 'http://www.youdagames.com/World+Domination+2-game-info-107/'
    except ASBreak:
        pass
    return U

def Sub_model_submit_2dplay_score(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Sub_model')
    e.set('_loc2_', rt.call_ref(ref(ref(this, 'MD5').get(), 'hex_md5'), [binop('+', binop('+', binop('+', binop('+', 'gameid=', ref(e.get('_root'), 'gameid').get()), '&hiscore='), ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'score').get()), '2DPlay.com/')]))
    e.call('getURL', [e.call('String', [binop('+', binop('+', binop('+', ref(e.get('_root'), 'scoreslink').get(), ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'score').get()), '&hash='), e.get('_loc2_'))]), '_blank'])
    return U

def Sub_model_get_religion_name_by_code(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_str'], ['a_str', 'i'], closure, 'Sub_model')
    for key_3 in keys(ref(this, 'religion_arr').get()):
        e.ref('i').set(key_3)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'religion_arr').get(), e.get('i')).get(), 0).get(), e.get('a_str'))):
                return ref(ref(ref(this, 'religion_arr').get(), e.get('i')).get(), 1).get()
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Sub_model_getCityByID(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_nr'], ['_loc3_', '_nr', 'i', 'j'], closure, 'Sub_model')
    for key_4 in keys(ref(this, 'playerArr').get()):
        e.ref('i').set(key_4)
        rt.tick()
        try:
            for key_5 in keys(ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'cityArr').get()):
                e.ref('j').set(key_5)
                rt.tick()
                try:
                    if truth(binop('==', ref(ref(ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'cityArr').get(), e.get('j')).get(), 'cityID').get(), e.get('_nr'))):
                        assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'cityArr').get(), e.get('j')).get())
                except ASContinue:
                    pass
                except ASBreak:
                    break
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc3_')
    return U

def Sub_model_string_is_used_action(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str', 'i'], closure, 'Sub_model')
    for key_6 in keys(ref(this, 'playerAB_position_arr').get()):
        e.ref('i').set(key_6)
        rt.tick()
        try:
            if truth(binop('==', e.get('_str'), ref(ref(ref(this, 'playerAB_position_arr').get(), e.get('i')).get(), 'action_name').get())):
                return True
        except ASContinue:
            pass
        except ASBreak:
            break
    return False
    return U

def Sub_model_reset_playerAB_position_arr(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    assign(ref(this, 'playerAB_position_arr'), '=', lambda: arr([obj({'_num': 0, 'building_name': e.get('undefined'), 'building_MC': e.get('undefined'), 'action_name': e.get('undefined')}), obj({'_num': 0, 'building_name': e.get('undefined'), 'building_MC': e.get('undefined'), 'action_name': e.get('undefined')}), obj({'_num': 1, 'building_name': e.get('undefined'), 'building_MC': e.get('undefined'), 'action_name': e.get('undefined')}), obj({'_num': 1, 'building_name': e.get('undefined'), 'building_MC': e.get('undefined'), 'action_name': e.get('undefined')}), obj({'_num': 2, 'building_name': e.get('undefined'), 'building_MC': e.get('undefined'), 'action_name': e.get('undefined')}), obj({'_num': 2, 'building_name': e.get('undefined'), 'building_MC': e.get('undefined'), 'action_name': e.get('undefined')}), obj({'_num': 3, 'building_name': e.get('undefined'), 'building_MC': e.get('undefined'), 'action_name': e.get('undefined')}), obj({'_num': 3, 'building_name': e.get('undefined'), 'building_MC': e.get('undefined'), 'action_name': e.get('undefined')}), obj({'_num': 4, 'building_name': e.get('undefined'), 'building_MC': e.get('undefined'), 'action_name': e.get('undefined')}), obj({'_num': 4, 'building_name': e.get('undefined'), 'building_MC': e.get('undefined'), 'action_name': e.get('undefined')})]))
    return U

def Sub_model_get_plr_arr_of_action(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_loc3_', '_str', 'i'], closure, 'Sub_model')
    e.set('_loc3_', rt.construct(e.get('Array'), []))
    for key_7 in keys(ref(this, 'playerAB_position_arr').get()):
        e.ref('i').set(key_7)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'playerAB_position_arr').get(), e.get('i')).get(), 'building_name').get(), e.get('_str'))):
                rt.call_ref(ref(e.get('_loc3_'), 'push'), [ref(ref(ref(this, 'playerAB_position_arr').get(), e.get('i')).get(), '_num').get()])
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc3_')
    return U

def Sub_model_loop_playerAB_position_arr(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_for', '_num', '_BN', '_BMC', '_action'], ['_BMC', '_BN', '_action', '_for', '_loc7_', '_num', 'i'], closure, 'Sub_model')
    for key_8 in keys(ref(this, 'playerAB_position_arr').get()):
        e.ref('i').set(key_8)
        rt.tick()
        try:
            assign(e.ref('_loc7_'), '=', lambda: ref(ref(this, 'playerAB_position_arr').get(), e.get('i')).get())
            switch_9 = e.get('_for')
            case_10 = -1
            if case_10 == -1 and strict_eq(switch_9, 'num'):
                case_10 = 0
            if case_10 == -1 and strict_eq(switch_9, 'name'):
                case_10 = 1
            if case_10 == -1 and strict_eq(switch_9, 'MC'):
                case_10 = 2
            if case_10 == -1 and strict_eq(switch_9, 'preAttack_any'):
                case_10 = 3
            if case_10 == -1 and strict_eq(switch_9, 'isDouble'):
                case_10 = 4
            if case_10 == -1:
                case_10 = -1
            try:
                if 0 <= case_10 <= 0:
                    if truth(logical('&&', binop('==', ref(e.get('_loc7_'), 'building_name').get(), e.get('_BN')), lambda: binop('==', ref(e.get('_loc7_'), 'building_MC').get(), e.get('_BMC')))):
                        return ref(e.get('_loc7_'), '_num').get()
                    raise ASBreak()
                if 0 <= case_10 <= 1:
                    if truth(logical('&&', binop('==', ref(e.get('_loc7_'), '_num').get(), e.get('_num')), lambda: binop('==', ref(e.get('_loc7_'), 'building_MC').get(), e.get('_BMC')))):
                        return ref(e.get('_loc7_'), 'building_name').get()
                    raise ASBreak()
                if 0 <= case_10 <= 2:
                    if truth(logical('&&', binop('==', ref(e.get('_loc7_'), '_num').get(), e.get('_num')), lambda: binop('==', ref(e.get('_loc7_'), 'building_name').get(), e.get('_BN')))):
                        return ref(e.get('_loc7_'), 'building_MC').get()
                    if truth(logical('&&', binop('==', ref(e.get('_loc7_'), '_num').get(), e.get('_num')), lambda: binop('==', ref(e.get('_loc7_'), 'action_name').get(), e.get('_BN')))):
                        return ref(e.get('_loc7_'), 'building_MC').get()
                    raise ASBreak()
                if 0 <= case_10 <= 3:
                    if truth(logical('||', binop('==', ref(e.get('_loc7_'), 'building_name').get(), 'silo'), lambda: logical('||', binop('==', ref(e.get('_loc7_'), 'building_name').get(), 'airfield'), lambda: logical('||', binop('==', ref(e.get('_loc7_'), 'building_name').get(), 'sub'), lambda: binop('==', ref(e.get('_loc7_'), 'building_name').get(), 'space'))))):
                        return True
                    raise ASBreak()
                if 0 <= case_10 <= 4:
                    if truth(logical('&&', binop('==', ref(e.get('_loc7_'), '_num').get(), e.get('_num')), lambda: binop('==', ref(e.get('_loc7_'), 'building_name').get(), e.get('_BN')))):
                        return True
            except ASBreak:
                pass
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Sub_model_reset_preAttackFrame(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_plr'], ['_plr'], closure, 'Sub_model')
    return U

def Sub_model_get_playerAB_mc(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_plrNum', '_aname'], ['_aname', '_loc4_', '_plrNum'], closure, 'Sub_model')
    if truth(binop('==', e.get('_aname'), 'preAttack')):
        assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'loop_playerAB_position_arr'), ['MC', e.get('_plrNum'), 'silo']))
        if truth(unary('!', e.get('_loc4_'))):
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'loop_playerAB_position_arr'), ['MC', e.get('_plrNum'), 'airfield']))
        if truth(unary('!', e.get('_loc4_'))):
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'loop_playerAB_position_arr'), ['MC', e.get('_plrNum'), 'sub']))
        if truth(unary('!', e.get('_loc4_'))):
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'loop_playerAB_position_arr'), ['MC', e.get('_plrNum'), 'space']))
    else:
        assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'loop_playerAB_position_arr'), ['MC', e.get('_plrNum'), e.get('_aname')]))
    return e.get('_loc4_')
    return U

def Sub_model___set__broadcaster(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param'], ['param'], closure, 'Sub_model')
    assign(ref(this, '_broadcaster'), '=', lambda: e.get('param'))
    return U

def Sub_model_setHumanTurnAction(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_'], closure, 'Sub_model')
    if truth(rt.call_ref(ref(ref(this, 'human').get(), 'getNextTurnAction'), [])):
        assign(e.ref('_loc2_'), '=', lambda: rt.call_ref(ref(ref(this, 'human').get(), 'getNextTurnAction'), []))
    rt.call_ref(ref(e.get('_loc2_'), 'doReset'), [])
    assign(ref(e.get('_loc2_'), 'action'), '=', lambda: ref(this, 'userSelectedActionBtn').get())
    if truth(binop('==', ref(e.get('_loc2_'), 'action').get(), 'preAttack')):
        if truth(binop('!=', ref(ref(this, 'human').get(), 'preAttackStatus').get(), 'ready')):
            assign(ref(e.get('_loc2_'), 'preAttackCarrier'), '=', lambda: ref(this, 'userSelectedWeapon').get())
        else:
            assign(ref(e.get('_loc2_'), 'preAttackCarrier'), '=', lambda: ref(this, 'userSelectedCarrier').get())
            assign(ref(e.get('_loc2_'), 'preAttackPayload'), '=', lambda: ref(this, 'userSelectedWeapon').get())
    else:
        if truth(logical('||', binop('==', ref(e.get('_loc2_'), 'action').get(), 'attack'), lambda: binop('==', ref(e.get('_loc2_'), 'action').get(), 'defense'))):
            assign(ref(e.get('_loc2_'), 'attackWeapon'), '=', lambda: ref(this, 'userSelectedWeapon').get())
    assign(ref(e.get('_loc2_'), 'humanBuyArr'), '=', lambda: ref(ref(ref(this, 'human').get(), 'weaponStock').get(), 'productionArray').get())
    assign(ref(e.get('_loc2_'), 'targetCity'), '=', lambda: ref(this, 'userSelectedCity').get())
    assign(ref(e.get('_loc2_'), 'ship_attack_arr'), '=', lambda: ref(this, 'ship_attack_arr').get())
    assign(ref(e.get('_loc2_'), 'targetPlayer'), '=', lambda: ref(this, 'userSelectedPlayer').get())
    assign(ref(e.get('_loc2_'), 'spyBuilding'), '=', lambda: ref(this, 'userSelectedSpyBuilding').get())
    if truth(binop('==', ref(e.get('_loc2_'), 'action').get(), 'production')):
        assign(e.ref('_loc3_'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [binop('*', binop('/', ref(ref(this, 'human').get(), 'turnMoney').get(), 100), ref(this, 'userSelectedProductionInvestmentArr_total_amount').get())]))
        assign(ref(ref(this, 'human').get(), 'turnMoney'), '-=', lambda: e.get('_loc3_'))
    else:
        if truth(binop('==', ref(e.get('_loc2_'), 'action').get(), 'research')):
            assign(ref(ref(this, 'human').get(), 'turnMoney'), '-=', lambda: ref(this, 'researchMoneySpend').get())
            assign(ref(e.get('_loc2_'), 'researchMoneySpend'), '=', lambda: ref(this, 'researchMoneySpend').get())
            assign(ref(e.get('_loc2_'), 'researchArr'), '=', lambda: ref(this, 'userSelectedResearchArr').get())
    assign(ref(e.get('_loc2_'), 'productionInvestmentArr'), '=', lambda: ref(this, '_userSelectedProductionInvestmentArr').get())
    assign(ref(e.get('_loc2_'), 'diplomacyArr'), '=', lambda: ref(this, 'userSelectedDiplomacyArr').get())
    assign(ref(e.get('_loc2_'), 'diplomacyLeader'), '=', lambda: ref(this, 'userSelectedDiplomacyLeader').get())
    assign(ref(e.get('_loc2_'), 'diplomacyOption'), '=', lambda: ref(this, 'userSelectedDiplomacyOption').get())
    if truth(logical('&&', binop('==', ref(this, 'userSelectedActionBtn').get(), 'diplomacy'), lambda: binop('==', ref(ref(ref(this, 'diplomacy_options_arr').get(), ref(this, 'userSelectedDiplomacyOption').get()).get(), 0).get(), 'offer'))):
        assign(ref(ref(this, 'human').get(), 'turnMoney'), '-=', lambda: ref(ref(ref(this, 'diplomacy_options_arr').get(), ref(this, 'userSelectedDiplomacyOption').get()).get(), 2).get())
    rt.call_ref(ref(this, 'resetUserSelections'), [])
    return U

def Sub_model_loadTurnAction(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_ta'], ['_ta'], closure, 'Sub_model')
    rt.call_ref(ref(this, 'resetUserSelections'), [])
    assign(ref(this, 'userSelectedActionBtn'), '=', lambda: ref(e.get('_ta'), 'action').get())
    assign(ref(this, 'userSelectedCity'), '=', lambda: ref(e.get('_ta'), 'targetCity').get())
    assign(ref(this, 'userSelectedPlayer'), '=', lambda: ref(e.get('_ta'), 'targetPlayer').get())
    assign(ref(this, 'userSelectedWeapon'), '=', lambda: ref(e.get('_ta'), 'attackWeapon').get())
    if truth(binop('!=', ref(ref(this, 'human').get(), 'preAttackStatus').get(), 'ready')):
        assign(ref(this, 'userSelectedCarrier'), '=', lambda: ref(e.get('_ta'), 'preAttackCarrier').get())
    assign(ref(this, 'ship_attack_arr'), '=', lambda: ref(e.get('_ta'), 'ship_attack_arr').get())
    rt.call_ref(ref(e.get('_ta'), 'doReset'), [])
    return U

def Sub_model___get__display_turnMoney(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Sub_model')
    e.set('_loc2_', '$ ')
    if truth(binop('>', ref(ref(this, 'human').get(), 'turnMoney').get(), 0)):
        assign(e.ref('_loc2_'), '=', lambda: binop('+', ref(ref(this, 'human').get(), 'turnMoney').get(), '.000.000'))
    else:
        assign(e.ref('_loc2_'), '+=', lambda: '0')
    return e.get('_loc2_')
    return U

def Sub_model___get__display_population(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Sub_model')
    e.set('_loc2_', '')
    assign(e.ref('_loc2_'), '+=', lambda: binop('+', rt.call_ref(ref(e.get('Math'), 'round'), [ref(ref(this, 'human').get(), 'population').get()]), '.000.000'))
    return e.get('_loc2_')
    return U

def Sub_model_resetPlayersForNewturn(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'Sub_model')
    for key_11 in keys(ref(this, 'activePlayerArr').get()):
        e.ref('i').set(key_11)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(this, 'activePlayerArr').get(), e.get('i')).get())
            rt.call_ref(ref(e.get('_loc2_'), 'resetActions'), [])
            rt.call_ref(ref(ref(e.get('_loc2_'), 'weaponStock').get(), 'resetPreOrder'), [])
            rt.call_ref(ref(ref(e.get('_loc2_'), 'techTree').get(), 'resetPreOrder'), [])
            assign(ref(e.get('_loc2_'), 'turnMoney'), '=', lambda: ref(e.get('_loc2_'), 'money').get())
            assign(ref(this, 'userSelectedSpyBuilding'), '=', lambda: 'spyCenter')
        except ASContinue:
            pass
        except ASBreak:
            break
    rt.call_ref(ref(this, 'resetUserSelections'), [])
    return U

def Sub_model_error(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['errorType', 'var1', 'var2', 'var3'], ['errorType', 'var1', 'var2', 'var3'], closure, 'Sub_model')
    if truth(ref(this, 'errorHandling').get()):
        if truth(unary('!', e.get('errorType'))):
            rt.call_ref(ref(ref(this, '_broadcaster').get(), 'broadcastMessage'), ['error', "And undefiend error occured... whatcha gonna do 'bout it?"])
        else:
            if truth(binop('==', e.get('errorType'), 'getTargets')):
                rt.call_ref(ref(ref(this, '_broadcaster').get(), 'broadcastMessage'), ['error', binop('+', binop('+', binop('+', 'Player: ', e.get('var1')), ", General undefined error in 'getTargets' method @ "), e.get('var2'))])
            else:
                if truth(binop('==', e.get('errorType'), 'doubleAction')):
                    rt.call_ref(ref(ref(this, '_broadcaster').get(), 'broadcastMessage'), ['error', binop('+', binop('+', binop('+', binop('+', 'player ', e.get('var1')), ' chose '), e.get('var2')), ' for both their actions... OMG!! ')])
                else:
                    if truth(binop('==', e.get('errorType'), 'noPreCarrier')):
                        rt.call_ref(ref(ref(this, '_broadcaster').get(), 'broadcastMessage'), ['error', binop('+', binop('+', 'player ', e.get('var1')), ' prepaired a pre attack withoug choosing a carrier')])
                    else:
                        if truth(binop('==', e.get('errorType'), 'noWeaponSelected')):
                            rt.call_ref(ref(ref(this, '_broadcaster').get(), 'broadcastMessage'), ['error', binop('+', binop('+', 'player', e.get('var1')), " selected 'attack' as an action, but did not select a weapon")])
                        else:
                            if truth(binop('==', e.get('errorType'), 'money')):
                                rt.call_ref(ref(ref(this, '_broadcaster').get(), 'broadcastMessage'), ['error', binop('+', binop('+', binop('+', binop('+', 'player', e.get('var1')), ' has a negative amount of money. $ '), e.get('var2')), '.000.000 ')])
    return U

def Sub_model___set__userSelectedActionBtn(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'Sub_model')
    if truth(binop('==', e.get('_param'), e.get('undefined'))):
        rt.call_ref(ref(this, 'resetUserSelections'), [])
    assign(ref(this, '_userSelectedActionBtn'), '=', lambda: e.get('_param'))
    return U

def Sub_model___get__userSelectedActionBtn(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    return ref(this, '_userSelectedActionBtn').get()
    return U

def Sub_model___set__userSelectedStockBtn(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'Sub_model')
    assign(ref(this, '_userSelectedStockBtn'), '=', lambda: e.get('_param'))
    return U

def Sub_model___get__userSelectedStockBtn(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    return ref(this, '_userSelectedStockBtn').get()
    return U

def Sub_model___set__userSelectedCity(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'Sub_model')
    assign(ref(this, '_userSelectedCity'), '=', lambda: e.get('_param'))
    return U

def Sub_model___set__userSelectedShipCityWaitingForTurnAction(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'Sub_model')
    assign(ref(this, '_userSelectedShipCityWaitingForTurnAction'), '=', lambda: e.get('_param'))
    return U

def Sub_model___get__userSelectedShipCityWaitingForTurnAction(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    return ref(this, '_userSelectedShipCityWaitingForTurnAction').get()
    return U

def Sub_model___set__userSelectedShipCityArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'Sub_model')
    assign(ref(this, '_userSelectedShipCityArr'), '=', lambda: e.get('_param'))
    return U

def Sub_model___get__userSelectedShipCityPlrNum(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    return ref(this, '_userSelectedShipCityPlrNum').get()
    return U

def Sub_model___set__userSelectedShipCityPlrNum(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'Sub_model')
    assign(ref(this, '_userSelectedShipCityPlrNum'), '=', lambda: e.get('_param'))
    return U

def Sub_model___get__userSelectedShipCityArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    return ref(this, '_userSelectedShipCityArr').get()
    return U

def Sub_model___get__userSelectedCity(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    return ref(this, '_userSelectedCity').get()
    return U

def Sub_model___set__userSelectedPlayer(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'Sub_model')
    assign(ref(this, '_userSelectedPlayer'), '=', lambda: e.get('_param'))
    return U

def Sub_model___get__userSelectedPlayer(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    return ref(this, '_userSelectedPlayer').get()
    return U

def Sub_model___set__userSelectedCarrier(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'Sub_model')
    assign(ref(this, '_userSelectedCarrier'), '=', lambda: e.get('_param'))
    return U

def Sub_model___get__userSelectedCarrier(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    return ref(this, '_userSelectedCarrier').get()
    return U

def Sub_model___set__userSelectedWeapon(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'Sub_model')
    assign(ref(this, '_userSelectedWeapon'), '=', lambda: e.get('_param'))
    return U

def Sub_model___get__userSelectedWeapon(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    return ref(this, '_userSelectedWeapon').get()
    return U

def Sub_model___set__userSelectedPayload(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'Sub_model')
    assign(ref(this, '_userSelectedPayload'), '=', lambda: e.get('_param'))
    return U

def Sub_model___get__userSelectedPayload(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    return ref(this, '_userSelectedPayload').get()
    return U

def Sub_model___set__userResetPreAttack(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'Sub_model')
    assign(ref(this, '_userResetPreAttack'), '=', lambda: e.get('_param'))
    return U

def Sub_model___get__userResetPreAttack(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    return ref(this, '_userResetPreAttack').get()
    return U

def Sub_model___set__userSelectedProductionInvestmentArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_arr'], ['_arr'], closure, 'Sub_model')
    assign(ref(this, '_userSelectedProductionInvestmentArr'), '=', lambda: e.get('_arr'))
    return U

def Sub_model___set__userSelectedResearchArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_arr'], ['_arr'], closure, 'Sub_model')
    assign(ref(this, '_userSelectedResearchArr'), '=', lambda: e.get('_arr'))
    return U

def Sub_model___get__userSelectedResearchArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    return ref(this, '_userSelectedResearchArr').get()
    return U

def Sub_model_productionInvestementPercLeft(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_num'], ['_loc3_', '_loc4_', '_num'], closure, 'Sub_model')
    e.set('_loc3_', 0)
    e.set('_loc4_', 1)
    while truth(binop('<', e.get('_loc4_'), ref(ref(this, 'userSelectedProductionInvestmentArr').get(), 'length').get())):
        rt.tick()
        try:
            if truth(binop('!=', e.get('_loc4_'), e.get('_num'))):
                assign(e.ref('_loc3_'), '+=', lambda: ref(ref(ref(this, 'userSelectedProductionInvestmentArr').get(), e.get('_loc4_')).get(), 1).get())
            assign(e.ref('_loc4_'), '=', lambda: binop('+', e.get('_loc4_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return binop('-', 100, e.get('_loc3_'))
    return U

def Sub_model_researchInvestementPercLeft(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_num'], ['_loc3_', '_loc4_', '_num'], closure, 'Sub_model')
    e.set('_loc3_', 0)
    e.set('_loc4_', 1)
    while truth(binop('<', e.get('_loc4_'), ref(ref(this, 'userSelectedResearchInvestmentArr').get(), 'length').get())):
        rt.tick()
        try:
            if truth(binop('!=', e.get('_loc4_'), e.get('_num'))):
                assign(e.ref('_loc3_'), '+=', lambda: ref(ref(ref(this, 'userSelectedResearchInvestmentArr').get(), e.get('_loc4_')).get(), 1).get())
            assign(e.ref('_loc4_'), '=', lambda: binop('+', e.get('_loc4_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return binop('-', 100, e.get('_loc3_'))
    return U

def Sub_model___get__userSelectedProductionInvestmentArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    return ref(this, '_userSelectedProductionInvestmentArr').get()
    return U

def Sub_model___get__userSelectedProductionInvestmentArr_total_amount(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'Sub_model')
    e.set('_loc2_', 0)
    for key_12 in keys(ref(this, '_userSelectedProductionInvestmentArr').get()):
        e.ref('i').set(key_12)
        rt.tick()
        try:
            if truth(ref(ref(ref(this, '_userSelectedProductionInvestmentArr').get(), e.get('i')).get(), 1).get()):
                assign(e.ref('_loc2_'), '+=', lambda: ref(ref(ref(this, '_userSelectedProductionInvestmentArr').get(), e.get('i')).get(), 1).get())
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def Sub_model___set__userSelectedDiplomacyArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_arr'], ['_arr'], closure, 'Sub_model')
    assign(ref(this, '_userSelectedDiplomacyArr'), '=', lambda: e.get('_arr'))
    return U

def Sub_model___get__userSelectedDiplomacyArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    return ref(this, '_userSelectedDiplomacyArr').get()
    return U

def Sub_model___set__userSelectedResearchInvestmentArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_arr'], ['_arr'], closure, 'Sub_model')
    assign(ref(ref(this, '_userSelectedResearchInvestmentArr').get(), ref(e.get('_arr'), 0).get()), '=', lambda: ref(e.get('_arr'), 1).get())
    return U

def Sub_model___get__userSelectedResearchInvestmentArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    return ref(this, '_userSelectedResearchInvestmentArr').get()
    return U

def Sub_model___get__userSelectedResearchInvestmentArr_total_amount(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'Sub_model')
    e.set('_loc2_', 0)
    for key_13 in keys(ref(this, '_userSelectedResearchInvestmentArr').get()):
        e.ref('i').set(key_13)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '+=', lambda: ref(ref(this, '_userSelectedResearchInvestmentArr').get(), e.get('i')).get())
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def Sub_model_resetUserSelections(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'Sub_model')
    assign(ref(this, '_userSelectedActionBtn'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'userSelectedWeapon'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'userSelectedStockBtn'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'userSelectedCity'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'ship_attack_arr'), '=', lambda: arr([]))
    assign(ref(this, 'userSelectedPlayer'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'userSelectedShipCityPlrNum'), '=', lambda: e.get('undefined'))
    if truth(binop('!=', ref(ref(this, 'human').get(), 'preAttackStatus').get(), 'ready')):
        assign(ref(this, 'userSelectedCarrier'), '=', lambda: e.get('undefined'))
    assign(ref(this, '_userSelectedProductionInvestmentArr'), '=', lambda: arr([arr([]), arr(['rockets', 0, 1]), arr(['planes', 0, 6]), arr(['special', 0, 7]), arr(['warhead', 0, 2]), arr(['bioload', 0, 3]), arr(['soldier', 0, 4]), arr(['spy', 0, 5]), arr(['defense', 0, 8])]))
    for key_14 in keys(ref(this, 'userSelectedResearchArr').get()):
        e.ref('i').set(key_14)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(this, 'userSelectedResearchArr').get(), e.get('i')).get())
            assign(ref(e.get('_loc2_'), 'preOrder'), '=', lambda: False)
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(this, 'userSelectedDiplomacyLeader'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'userSelectedDiplomacyOption'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'researchMoneySpend'), '=', lambda: 0)
    assign(ref(this, 'userSelectedResearchArr'), '=', lambda: arr([]))
    assign(ref(this, 'userSelectedSpyBuilding'), '=', lambda: 'spyCenter')
    return U

def Sub_model_resetAfterCanceledTurnAction(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'Sub_model')
    assign(ref(ref(this, 'userSelectedCarrier').get(), 'inUse'), '=', lambda: 0)
    assign(ref(ref(this, 'userSelectedWeapon').get(), 'inUse'), '=', lambda: 0)
    switch_15 = ref(this, 'userSelectedActionBtn').get()
    case_16 = -1
    if case_16 == -1 and strict_eq(switch_15, 'preAttack'):
        case_16 = 0
    if case_16 == -1 and strict_eq(switch_15, 'attack'):
        case_16 = 1
    if case_16 == -1 and strict_eq(switch_15, 'propaganda'):
        case_16 = 2
    if case_16 == -1:
        case_16 = -1
    try:
        if 0 <= case_16 <= 0:
            if truth(binop('==', ref(ref(this, 'userSelectedCarrier').get(), 'weaponName').get(), 'ship')):
                for key_17 in keys(ref(this, 'ship_attack_arr').get()):
                    e.ref('i').set(key_17)
                    rt.tick()
                    try:
                        rt.call_ref(ref(rt.call_ref(ref(this, 'getCityByID'), [ref(ref(ref(this, 'ship_attack_arr').get(), e.get('i')).get(), 'city').get()]), 'deselectForShipAttack'), [])
                        assign(ref(rt.call_ref(ref(ref(ref(this, 'human').get(), 'weaponStock').get(), 'getWeaponByID'), [ref(ref(ref(this, 'ship_attack_arr').get(), e.get('i')).get(), 'wpn').get()]), 'inUse'), '=', lambda: binop('-', ref(rt.call_ref(ref(ref(ref(this, 'human').get(), 'weaponStock').get(), 'getWeaponByID'), [ref(ref(ref(this, 'ship_attack_arr').get(), e.get('i')).get(), 'wpn').get()]), 'inUse').get(), 1))
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
            else:
                if truth(binop('==', ref(ref(this, 'human').get(), 'preAttackStatus').get(), 'ready')):
                    update(ref(ref(this, 'userSelectedPayload').get(), 'inUse'), -1, False)
                    rt.call_ref(ref(this, 'deselectCities'), ['preAttack'])
            raise ASBreak()
        if 0 <= case_16 <= 1:
            pass
        if 0 <= case_16 <= 2:
            pass
    except ASBreak:
        pass
    rt.call_ref(ref(this, 'resetUserSelections'), [])
    return U

def Sub_model_setCeaseFire(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_plrA', '_plrB', '_turns'], ['_plrA', '_plrB', '_turns'], closure, 'Sub_model')
    assign(ref(ref(ref(ref(ref(this, 'playerArr').get(), e.get('_plrA')).get(), 'ceaseFireArr').get(), e.get('_plrB')).get(), '_turnsLeft'), '=', lambda: e.get('_turns'))
    assign(ref(ref(ref(ref(ref(this, 'playerArr').get(), e.get('_plrA')).get(), 'ceaseFireArr').get(), e.get('_plrB')).get(), '_status'), '=', lambda: True)
    assign(ref(ref(ref(ref(ref(this, 'playerArr').get(), e.get('_plrB')).get(), 'ceaseFireArr').get(), e.get('_plrA')).get(), '_turnsLeft'), '=', lambda: e.get('_turns'))
    assign(ref(ref(ref(ref(ref(this, 'playerArr').get(), e.get('_plrB')).get(), 'ceaseFireArr').get(), e.get('_plrA')).get(), '_status'), '=', lambda: True)
    return U

def Sub_model_select_random_city(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_plr'], ['_loc3_', '_loc4_', '_plr', 'i'], closure, 'Sub_model')
    e.set('_loc3_', rt.construct(e.get('Array'), []))
    for key_18 in keys(ref(e.get('_plr'), 'cityArr').get()):
        e.ref('i').set(key_18)
        rt.tick()
        try:
            if truth(binop('>', ref(ref(ref(e.get('_plr'), 'cityArr').get(), e.get('i')).get(), 'population').get(), 0)):
                rt.call_ref(ref(e.get('_loc3_'), 'push'), [ref(ref(e.get('_plr'), 'cityArr').get(), e.get('i')).get()])
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc4_', ref(e.get('_loc3_'), rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [0, binop('-', ref(e.get('_loc3_'), 'length').get(), 1)])).get())
    return e.get('_loc4_')
    return U

def Sub_model_deselectCities(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_action'], ['_action', 'i', 'j'], closure, 'Sub_model')
    for key_19 in keys(ref(this, 'playerArr').get()):
        e.ref('i').set(key_19)
        rt.tick()
        try:
            for key_20 in keys(ref(ref(ref(this, 'playerArr').get(), e.get('i')).get(), 'cityArr').get()):
                e.ref('j').set(key_20)
                rt.tick()
                try:
                    rt.call_ref(ref(ref(ref(ref(ref(this, 'playerArr').get(), e.get('i')).get(), 'cityArr').get(), e.get('j')).get(), 'removeSelection'), [e.get('_action')])
                except ASContinue:
                    pass
                except ASBreak:
                    break
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Sub_model_gameStatus(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_n'], ['_loc0_', '_loc3_', 'i', 'param_n'], closure, 'Sub_model')
    if truth(binop('===', assign(e.ref('_loc0_'), '=', lambda: e.get('param_n')), 'worldPopulation')):
        assign(e.ref('_loc3_'), '=', lambda: 0)
        for key_21 in keys(ref(this, 'activePlayerArr').get()):
            e.ref('i').set(key_21)
            rt.tick()
            try:
                assign(e.ref('_loc3_'), '+=', lambda: ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'population').get())
            except ASContinue:
                pass
            except ASBreak:
                break
        return e.get('_loc3_')
    return U

def Sub_model_createBioHazardArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['bioLevel'], ['_loc3_', '_loc4_', '_loc5_', '_loc6_', 'bioLevel'], closure, 'Sub_model')
    if truth(logical('||', unary('!', e.get('bioLevel')), lambda: rt.call_ref(ref(e.get('_global'), 'isNaN'), [e.get('bioLevel')]))):
        assign(e.ref('bioLevel'), '=', lambda: 1)
    e.set('_loc3_', 0)
    e.set('_loc4_', ref(ref(ref(this, 'bioHazardDeactivateArray').get(), e.get('bioLevel')).get(), 1).get())
    e.set('_loc5_', rt.construct(e.get('Array'), []))
    e.set('_loc6_', 0)
    while truth(binop('<', e.get('_loc3_'), e.get('bioLevel'))):
        rt.tick()
        try:
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [0, binop('-', ref(ref(this, 'bioActions_arr').get(), 'length').get(), 1)]))
            rt.call_ref(ref(e.get('_loc5_'), 'push'), [obj({'_action': ref(ref(this, 'bioActions_arr').get(), e.get('_loc6_')).get()})])
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(e.ref('_loc3_'), '=', lambda: 0)
    while truth(binop('<', e.get('_loc3_'), e.get('_loc4_'))):
        rt.tick()
        try:
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [0, binop('-', ref(ref(ref(ref(this, 'human').get(), 'weaponStock').get(), 'weaponArr').get(), 'length').get(), 1)]))
            if truth(ref(ref(ref(ref(ref(this, 'human').get(), 'weaponStock').get(), 'weaponArr').get(), e.get('_loc6_')).get(), 'active').get()):
                rt.call_ref(ref(e.get('_loc5_'), 'push'), [obj({'_stock': ref(ref(ref(ref(ref(this, 'human').get(), 'weaponStock').get(), 'weaponArr').get(), e.get('_loc6_')).get(), 'weaponID').get(), '_weaponName': ref(ref(ref(ref(ref(this, 'human').get(), 'weaponStock').get(), 'weaponArr').get(), e.get('_loc6_')).get(), 'weaponName').get()})])
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc5_')
    return U

def Sub_model_next_ambient_sound_index(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    if truth(binop('<', ref(this, 'ambient_sound_index').get(), 10)):
        assign(ref(this, 'ambient_sound_index'), '=', lambda: binop('+', ref(this, 'ambient_sound_index').get(), 1))
    else:
        assign(ref(this, 'ambient_sound_index'), '=', lambda: 1)
    return U

def Sub_model_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_model')
    ref(this, 'demo_version_arr').set(arr(['Affiliates', 'Miniclip', 'Totallygame', 'NewGrounds', 'Arcadetown', 'Agame', '2dplay', '2dplay_youdaHS', 'Craziness']))
    ref(this, 'demo_version_url').set(arr(['Affiliates', 'http://www.miniclip.com/buy_worlddominationii.htm', 'http://www.youdagames.com/World+Domination+2-game-info-107/', 'https://secure.bmtmicro.com/servlets/Orders.ShoppingCart?CLR=0&CID=2249&PRODUCTID=22490032&AID=1071719', 'http://www.arcadetown.com/worlddomination2/ordergame.asp', 'https://secure.bmtmicro.com/servlets/Orders.ShoppingCart?CLR=0&CID=2249&PRODUCTID=22490032&AID=1111152', 'https://secure.bmtmicro.com/servlets/Orders.ShoppingCart?CLR=0&CID=2249&PRODUCTID=22490032&AID=1298578', 'https://secure.bmtmicro.com/servlets/Orders.ShoppingCart?CLR=0&CID=2249&PRODUCTID=22490032&AID=1298578', 'https://secure.bmtmicro.com/servlets/Orders.ShoppingCart?CLR=0&CID=2249&PRODUCTID=22490032&AID=1298578']))
    ref(this, 'demo_version').set(2)
    ref(this, 'general_version_url').set('')
    ref(this, 'demo_mode').set(False)
    ref(this, 'zs66hj8s').set(False)
    ref(this, 'view_leader_MCs_played').set('false')
    ref(this, 'view_leader_MCs_played_count').set(0)
    ref(this, 'difficulty_level').set(1)
    ref(this, 'actionNames_arr').set(arr(['resources', 'production', 'research', 'religion', 'preAttack', 'attack', 'defense', 'propaganda', 'diplomacy']))
    ref(this, 'force_error_window').set(False)
    ref(this, 'force_error_window_text').set('')
    ref(this, 'satellite_sound_playing').set(False)
    ref(this, 'game_initiated').set(False)
    ref(this, 'ambient_sound_index').set(1)
    ref(this, 'fullscreen').set(False)
    ref(this, 'religion_arr').set(arr([arr(['chr', 'Christian']), arr(['bhu', 'Bhudist']), arr(['com', 'Communist']), arr(['mus', 'Muslim']), arr(['jew', 'Jewish'])]))
    ref(this, 'building_names_to_actions_arr').set(arr([obj({'building_name': 'resources', 'action_name': 'resources'}), obj({'building_name': 'factory', 'action_name': 'production'}), obj({'building_name': 'tech', 'action_name': 'research'}), obj({'building_name': 'technology', 'action_name': 'research'}), obj({'building_name': 'religion', 'action_name': 'religion'}), obj({'building_name': 'sub', 'action_name': 'preAttack'}), obj({'building_name': 'space', 'action_name': 'preAttack'}), obj({'building_name': 'ship', 'action_name': 'preAttack'}), obj({'building_name': 'base', 'action_name': 'attack'}), obj({'building_name': 'helipad', 'action_name': 'attack'}), obj({'building_name': '____', 'action_name': 'attack'}), obj({'building_name': 'hatch', 'action_name': 'attack'}), obj({'building_name': 'propaganda', 'action_name': 'propaganda'}), obj({'building_name': 'diplomacy', 'action_name': 'diplomacy'}), obj({'building_name': 'antiAir_still', 'action_name': 'defense'}), obj({'building_name': 'antiRocket_still', 'action_name': 'defense'}), obj({'building_name': 'silo', 'action_name': 'preAttack'}), obj({'building_name': 'airfield', 'action_name': 'preAttack'})]))
    ref(this, 'orderOfActions_arr').set(arr(['resources', 'production', 'produce', 'technology', 'research', 'religion', 'battle', 'preAttack', 'attack', 'propaganda', 'diplomacy']))
    ref(this, 'spyActions_arr').set(arr(['diplomacy', 'factory', 'tech', 'religion', 'resources']))
    ref(this, 'spyBuildings_arr').set(arr(['diplomacy', 'factory', 'tech', 'religion', 'resources']))
    ref(this, 'bioActions_arr').set(arr(['resources', 'production', 'technology', 'religion', 'propaganda', 'diplomacy']))
    ref(this, 'cityPositions').set(rt.construct(e.get('Array'), [arr([arr([377, 242]), arr([308, 307]), arr([418, 425]), arr([478, 251]), arr([546, 322])]), arr([arr([36, 96]), arr([229, 58]), arr([126, 220]), arr([28, 234]), arr([191, 151])]), arr([arr([546, 80]), arr([703, 200]), arr([620, 151]), arr([764, 95]), arr([770, 251])]), arr([arr([26, 426]), arr([136, 438]), arr([41, 572]), arr([308, 583]), arr([237, 478])]), arr([arr([758, 571]), arr([642, 496]), arr([697, 417]), arr([532, 560]), arr([764, 412])])]))
    ref(this, 'soldier_waypoints_arr').set(rt.construct(e.get('Array'), [arr([obj({'_wpArr': arr([0]), '_endPos': 'RT'}), obj({'_wpArr': arr([1, 2]), '_endPos': 'B'}), obj({'_wpArr': arr([1, 2, 3]), '_endPos': 'L'}), obj({'_wpArr': arr([1, 6]), '_endPos': 'B'}), obj({'_wpArr': arr([0]), '_endPos': 'L'})]), arr([obj({'_wpArr': arr([1]), '_endPos': 'T'}), obj({'_wpArr': arr([1]), '_endPos': 'LT'}), obj({'_wpArr': arr([2]), '_endPos': 'LT'}), obj({'_wpArr': arr([2, 3, 5]), '_endPos': 'LB'}), obj({'_wpArr': arr([4]), '_endPos': 'LB'})]), arr([obj({'_wpArr': arr([0]), '_endPos': 'B'}), obj({'_wpArr': arr([1]), '_endPos': 'RT'}), obj({'_wpArr': arr([1, 2]), '_endPos': 'RT'}), obj({'_wpArr': arr([1, 2, 3]), '_endPos': 'LT'}), obj({'_wpArr': arr([4]), '_endPos': 'T'})]), arr([obj({'_wpArr': arr([0]), '_endPos': 'L'}), obj({'_wpArr': arr([2]), '_endPos': 'L'}), obj({'_wpArr': arr([1, 2]), '_endPos': 'LB'}), obj({'_wpArr': arr([1, 2, 3, 5]), '_endPos': 'R'}), obj({'_wpArr': arr([4]), '_endPos': 'R'})]), arr([obj({'_wpArr': arr([0]), '_endPos': 'T'}), obj({'_wpArr': arr([1]), '_endPos': 'R'}), obj({'_wpArr': arr([2, 3]), '_endPos': 'B'}), obj({'_wpArr': arr([2, 3, 4]), '_endPos': 'B'}), obj({'_wpArr': arr([5]), '_endPos': 'L'})])]))
    ref(this, 'soldier_fire_positions').set(rt.construct(e.get('Array'), [obj({'_pos': 'LB', '_arr': arr([arr([unary('-', 55), unary('-', 5)]), arr([unary('-', 40), 40]), arr([unary('-', 10), 20])])}), obj({'_pos': 'LT', '_arr': arr([arr([unary('-', 55), unary('-', 5)]), arr([unary('-', 40), unary('-', 20)]), arr([unary('-', 20), unary('-', 40)])])}), obj({'_pos': 'RT', '_arr': arr([arr([35, unary('-', 5)]), arr([30, unary('-', 20)]), arr([unary('-', 20), unary('-', 40)])])}), obj({'_pos': 'R', '_arr': arr([arr([55, unary('-', 5)]), arr([40, 15]), arr([40, unary('-', 15)])])}), obj({'_pos': 'B', '_arr': arr([arr([unary('-', 55), unary('-', 5)]), arr([0, 25]), arr([35, unary('-', 5)])])}), obj({'_pos': 'L', '_arr': arr([arr([unary('-', 60), unary('-', 5)]), arr([unary('-', 55), 15]), arr([unary('-', 55), unary('-', 15)])])}), obj({'_pos': 'T', '_arr': arr([arr([unary('-', 55), unary('-', 20)]), arr([unary('-', 40), unary('-', 30)]), arr([25, unary('-', 20)])])})]))
    ref(this, 'tank_waypoints_arr').set(rt.construct(e.get('Array'), [arr([obj({'_wpArr': arr([0]), '_endPos': 'RT'}), obj({'_wpArr': arr([1, 2]), '_endPos': 'B'}), obj({'_wpArr': arr([1, 2, 3]), '_endPos': 'L'}), obj({'_wpArr': arr([1, 6]), '_endPos': 'B'}), obj({'_wpArr': arr([1]), '_endPos': 'LT'})]), arr([obj({'_wpArr': arr([1]), '_endPos': 'T'}), obj({'_wpArr': arr([1]), '_endPos': 'LT'}), obj({'_wpArr': arr([2]), '_endPos': 'LT'}), obj({'_wpArr': arr([2, 3, 5]), '_endPos': 'LB'}), obj({'_wpArr': arr([4]), '_endPos': 'LB'})]), arr([obj({'_wpArr': arr([0]), '_endPos': 'B'}), obj({'_wpArr': arr([1]), '_endPos': 'RT'}), obj({'_wpArr': arr([1, 2]), '_endPos': 'RT'}), obj({'_wpArr': arr([1, 2, 3]), '_endPos': 'LT'}), obj({'_wpArr': arr([4]), '_endPos': 'T'})]), arr([obj({'_wpArr': arr([0]), '_endPos': 'L'}), obj({'_wpArr': arr([0]), '_endPos': 'LB'}), obj({'_wpArr': arr([1, 2]), '_endPos': 'LB'}), obj({'_wpArr': arr([1, 2, 3]), '_endPos': 'R'}), obj({'_wpArr': arr([4]), '_endPos': 'R'})]), arr([obj({'_wpArr': arr([0]), '_endPos': 'T'}), obj({'_wpArr': arr([1]), '_endPos': 'L'}), obj({'_wpArr': arr([2, 3]), '_endPos': 'B'}), obj({'_wpArr': arr([2, 3, 4]), '_endPos': 'B'}), obj({'_wpArr': arr([5]), '_endPos': 'L'})])]))
    ref(this, 'tank_fire_positions').set(rt.construct(e.get('Array'), [obj({'_pos': 'LB', '_arr': arr([arr([unary('-', 55), 20])])}), obj({'_pos': 'LT', '_arr': arr([arr([unary('-', 55), unary('-', 25)])])}), obj({'_pos': 'RT', '_arr': arr([arr([55, unary('-', 25)])])}), obj({'_pos': 'R', '_arr': arr([arr([55, unary('-', 5)])])}), obj({'_pos': 'B', '_arr': arr([arr([0, 25])])}), obj({'_pos': 'L', '_arr': arr([arr([unary('-', 55), unary('-', 5)])])}), obj({'_pos': 'T', '_arr': arr([arr([0, unary('-', 20)])])})]))
    ref(this, 'boatWayPointPositions').set(rt.construct(e.get('Array'), [arr([380, 156]), arr([474, 192]), arr([578, 240]), arr([655, 307]), arr([582, 455]), arr([493, 498]), arr([400, 530]), arr([337, 504]), arr([254, 411]), arr([200, 360]), arr([217, 266]), arr([240, 250]), arr([295, 194])]))
    ref(this, 'boatStartingPosition').set(rt.construct(e.get('Array'), [arr([410, 474, 7]), arr([179, 252, 11]), arr([528, 145, 1]), arr([311, 525, 7]), arr([575, 510, 5])]))
    ref(this, 'landUnitsArr').set(rt.construct(e.get('Array'), [arr([420, 420]), arr([160, 201]), arr([563, 108]), arr([260, 500]), arr([562, 511])]))
    ref(this, 'marine_landUnitsArr').set(rt.construct(e.get('Array'), [arr([420, 420]), arr([160, 201]), arr([563, 108]), arr([260, 500]), arr([562, 511])]))
    ref(this, 'chinookStartPositions').set(rt.construct(e.get('Array'), [arr([420, 310]), arr([88, 109]), arr([708, 91]), arr([105, 510]), arr([730, 505])]))
    ref(this, 'marineFirePos').set(arr([arr([unary('-', 55), unary('-', 5)]), arr([0, 25]), arr([35, unary('-', 5)]), arr([0, unary('-', 30)])]))
    ref(this, 'bioHazardArr').set(arr([1, 8, 9, 14, 15, 17, 18, 32, 33, 34, 35, 36, 37]))
    ref(this, 'bioHazardDeactivateArray').set(arr([arr([]), arr([3, 6]), arr([7, 10]), arr([14, 17]), arr([17, 30])]))
    ref(this, 'suicide_spawn_array').set(arr([arr([420, 420]), arr([160, 201]), arr([563, 108]), arr([260, 500]), arr([562, 511])]))
    ref(this, 'submarine_surface_friendly_loc').set(arr([arr([370, 170]), arr([300, 150]), arr([425, 40]), arr([33, 357]), arr([400, 550])]))
    ref(this, 'submarine_surface_enemy_loc').set(arr([arr([450, 180]), arr([340, 65]), arr([490, 140]), arr([170, 390]), arr([437, 500])]))
    ref(this, 'satellite_height_arr').set(arr([158, 18, 18, 269, 169]))
    ref(this, 'satellite_pos_arr').set(arr([obj({'_x': 368, '_y': 75}), obj({'_x': 268, '_y': 104}), obj({'_x': 466, '_y': 111}), obj({'_x': 121, '_y': 321}), obj({'_x': 667, '_y': 291})]))
    ref(this, 'ship_plane_start_arr').set(rt.construct(e.get('Array'), [arr([28, unary('-', 26)]), arr([unary('-', 9), unary('-', 3)]), arr([unary('-', 38), 11])]))
    ref(this, 'spyBuildingArr').set(rt.construct(e.get('Array'), [1, 'spyCenter', 'tech', 'religion', 'resources', 'factory']))
    ref(this, 'diplomacy_options_arr').set(arr([arr(['offer', 3, 10]), arr(['offer', 6, 50]), arr(['offer', 10, 90]), arr(['demand', 3, 10]), arr(['demand', 6, 50]), arr(['demand', 10, 90])]))
    ref(this, 'liftOff_location').set(arr([arr([327, 246]), arr([230, 230]), arr([570, 220]), arr([200, 430]), arr([620, 450])]))
    ref(this, 'attackingSubs_arr').set(rt.construct(e.get('Array'), []))
    ref(this, '_broadcaster').set(rt.construct(e.get('Object'), []))
    ref(this, 'errorHandling').set(False)
    ref(this, 'curBattleMCAction').set('')
    ref(this, '_userSelectedActionBtn').set(e.get('undefined'))
    ref(this, '_userSelectedStockBtn').set(e.get('undefined'))
    ref(this, '_userSelectedCity').set(e.get('undefined'))
    ref(this, '_userSelectedPlayer').set(e.get('undefined'))
    ref(this, '_userSelectedCarrier').set(e.get('undefined'))
    ref(this, '_userSelectedWeapon').set(e.get('undefined'))
    ref(this, '_userSelectedPayload').set(e.get('undefined'))
    ref(this, '_userSelectedShipCityArr').set(rt.construct(e.get('Array'), []))
    ref(this, '_userSelectedShipCityWaitingForTurnAction').set(False)
    ref(this, '_userSelectedProductionInvestmentArr').set(rt.construct(e.get('Array'), [arr([]), arr(['rockets', 0, 1, 0]), arr(['planes', 0, 6, 0]), arr(['special', 0, 7, 0]), arr(['warhead', 0, 2, 0]), arr(['bioload', 0, 3, 0]), arr(['soldier', 0, 4, 0]), arr(['spy', 0, 5, 0]), arr(['defense', 0, 8, 0])]))
    ref(this, '_userSelectedResearchInvestmentArr').set(rt.construct(e.get('Array'), [arr([]), arr(['rockets', 0, 1]), arr(['planes', 0, 6]), arr(['special', 0, 7]), arr(['warhead', 0, 2]), arr(['bioload', 0, 3]), arr(['soldier', 0, 4]), arr(['spy', 0, 5]), arr(['defense', 0, 8])]))
    ref(this, 'ship_attack_arr').set(rt.construct(e.get('Array'), []))
    ref(this, 'm11').set('soldier_loop_9')
    ref(this, 'soldierSpawnArr1').set(rt.construct(e.get('Array'), ['soldier', 'soldier', 'soldier']))
    ref(this, 'soldierSpawnArr2').set(rt.construct(e.get('Array'), ['soldier', 'soldier']))
    ref(this, 'soldierSpawnArr3').set(rt.construct(e.get('Array'), ['soldier', 'soldier', 'soldier']))
    ref(this, 'soldierSpawnArr4').set(rt.construct(e.get('Array'), ['soldier', 'soldier', 'soldier', 'soldier']))
    ref(this, 'interface_spawned_bioMC_array').set(rt.construct(e.get('Array'), []))
    ref(this, 'battleCounter').set(0)
    ref(this, 'battleTimerIndex').set(0)
    ref(this, 'unitStartNum').set(0)
    ref(this, 'heliStart').set(arr([]))
    ref(this, 'cityDepthArr').set(rt.construct(e.get('Array'), []))
    ref(this, 'lastUnitWasBuilding').set(False)
    ref(this, 'maxCarrierCityAmount').set(3)
    ref(this, 'corrupt_highscore').set(False)
    ref(this, 'AI_spy_required_stock_obj').set(rt.construct(e.get('Object'), [obj({'_level1': 10, '_level2': 8, '_level3': 5, '_level4': 3})]))
    ref(this, 'ch_018').set(arr([obj({'id_str': 'orca', 'str': 'free willy', 'active': False}), obj({'id_str': 'easter', 'str': 'rapa nui', 'active': False}), obj({'id_str': 'nessy', 'str': 'nessy', 'active': False}), obj({'id_str': 'disco', 'str': 'saturdaynight', 'active': False}), obj({'id_str': 'kill_all', 'str': 'psycho killer', 'active': False}), obj({'id_str': 'bush', 'str': 'I am Bush', 'active': False}), obj({'id_str': 'cash', 'str': 'trump', 'active': False}), obj({'id_str': 'tech', 'str': 'dexter', 'active': False}), obj({'id_str': 'stock', 'str': 'gimmegimme', 'active': False})]))
    ref(this, 'soundCount').set(0)
    ref(this, 'action_to_sound_arr').set(rt.construct(e.get('Array'), [obj({'_actionName': 'interface_noise', '_soundName': 'TV noise.wav'}), obj({'_actionName': 'interface_startup', '_soundName': 'interface_startup.wav'}), obj({'_actionName': 'interface_actionBtn_on', '_soundName': 'interface_Switch Action selection.wav', '_pan': unary('-', 80)}), obj({'_actionName': 'interface_actionBtn_off', '_soundName': 'interface_Switch Action selection2.wav', '_pan': unary('-', 80)}), obj({'_actionName': 'interface_acceptAction_btn', '_soundName': 'interface_Accept action bleep.wav'}), obj({'_actionName': 'interface_open_tube', '_soundName': 'interface_openactiondevice.wav'}), obj({'_actionName': 'interface_close_tube', '_soundName': 'interface_closeactiondevice.wav'}), obj({'_actionName': 'interface_close_turnBtn', '_soundName': 'interface_Closeconfirmbutton.wav'}), obj({'_actionName': 'interface_open_turnBtn', '_soundName': 'interface_Openconfirmbutton.wav'}), obj({'_actionName': 'interface_select_stock', '_soundName': 'interface_Switch Sounds 1.wav', '_pan': 80}), obj({'_actionName': 'interface_slider_bleep', '_soundName': 'interface_select unit bleep.wav'}), obj({'_actionName': 'interface_select_city', '_soundName': 'interface_select unit bleep.wav'}), obj({'_actionName': 'interface_select_tech', '_soundName': 'interface_select unit bleep.wav'}), obj({'_actionName': 'interface_deselect_tech', '_soundName': 'interface_select unit bleep.wav'}), obj({'_actionName': 'interface_cant_select_tech', '_soundName': 'interface_select unit bleep.wav'}), obj({'_actionName': 'interface_select_diplo_leader', '_soundName': 'interface_select unit bleep.wav'}), obj({'_actionName': 'interface_select_diplo_option', '_soundName': 'interface_select unit bleep.wav'}), obj({'_actionName': 'interface_select_spy_building', '_soundName': 'interface_select unit bleep.wav'}), obj({'_actionName': '--', '_soundName': '--'})]))
    ref(this, 'ch_019').set(arr([obj({'id_str': '#2dawgz', 'str': '#2dawgz', 'active': False, 'msg': "## 2 dawgz / 2 pirates. No ninja's. ##"}), obj({'id_str': '#thenizz', 'str': '#thenizz', 'active': False, 'msg': '## dawgz 4 life, homez 4e4 ##'}), obj({'id_str': '#lollerskates', 'str': '#lollerskates', 'active': False, 'msg': '## 2 long, 2 much ##'}), obj({'id_str': '#fc1', 'str': '#fc1', 'active': False, 'msg': "## It is only after you've lost everything, that you are free to do anything... ## ~Chuck Palahniuk, Fight Club, Chapter 8 "}), obj({'id_str': '#sa1', 'str': '#sa1', 'active': False, 'msg': '## 4 teh goons, humor me with your witty sarcasm. As no one seems to get. ##'}), obj({'id_str': '#error', 'str': '#error', 'active': False, 'msg': '## get a life, you deserve it ##'})]))
    ref(this, 'building_to_sound_arr').set(rt.construct(e.get('Array'), [obj({'_buildingName': 'production', '_soundName': 'building_factory.wav'}), obj({'_buildingName': 'religion', '_varSoundName': 'religion'}), obj({'_buildingName': 'diplomacy', '_soundName': 'Diplomacy humans.wav'}), obj({'_buildingName': 'silo', '_soundName': 'building_silo.wav'}), obj({'_buildingName': 'airfield', '_soundName': 'building_airfield.wav'}), obj({'_buildingName': 'propaganda', '_soundName': 'building_Propaganda.wav'}), obj({'_buildingName': 'resources', '_soundName': 'building_Resource.wav'}), obj({'_buildingName': 'ambient_resources', '_soundName': 'Resources ambient loop.wav'}), obj({'_buildingName': 'space', '_soundName': 'building_space_launch_2.wav'}), obj({'_buildingName': 'research', '_soundName': 'building_tech.wav'}), obj({'_buildingName': 'helipad', '_soundName': 'building_helipad.wav'}), obj({'_buildingName': 'base', '_soundName': 'troops_marching_001.wav'}), obj({'_buildingName': 'sub', '_soundName': 'sub_ping.wav'}), obj({'_buildingName': 'base', '_soundName': 'building_base.wav'}), obj({'_buildingName': 'hatch', '_soundName': 'unit_Suicide Hatch.wav'}), obj({'_buildingName': '--', '_soundName': '--'})]))
    ref(this, 'event_to_sound_arr').set(rt.construct(e.get('Array'), [obj({'_eventName': 'sub_surface', '_soundName': 'unit_Submarine water splash.wav'}), obj({'_eventName': 'stop_anti_rocket', '_soundName': 'building_Anti rocket rotate stop.wav'}), obj({'_eventName': 'satellite_flight', '_soundName': 'Satelite_flight.wav'}), obj({'_eventName': 'space_launch', '_soundName': 'building_space_launch.wav'}), obj({'_eventName': '--', '_soundName': '--'})]))
    ref(this, 'explosion_MC_to_sound_arr').set(rt.construct(e.get('Array'), [obj({'_mcName': 'explosion_warhead_1', '_soundName': 'Explode small3.wav'}), obj({'_mcName': 'explosion_warhead_2', '_soundName': 'Explode medium 3.wav'}), obj({'_mcName': 'explosion_warhead_3', '_soundName': 'explode medium.wav'}), obj({'_mcName': 'explosion_warhead_4', '_soundName': 'Explode large2.wav'}), obj({'_mcName': 'explosion_bioload_1', '_soundName': 'Explode small3.wav'}), obj({'_mcName': 'explosion_bioload_2', '_soundName': 'Explode medium 3.wav'}), obj({'_mcName': 'explosion_bioload_3', '_soundName': 'explode medium.wav'}), obj({'_mcName': 'explosion_bioload_4', '_soundName': 'Explode large.wav'}), obj({'_mcName': 'explosion001', '_soundName': 'Explode small3.wav'}), obj({'_mcName': 'explosion002', '_soundName': 'Explode small3.wav'}), obj({'_mcName': 'explosion003', '_soundName': 'Explode small3.wav'}), obj({'_mcName': 'suicide', '_soundName': 'unit_Suicide explode.wav'}), obj({'_mcName': '', '_soundName': ''})]))
    ref(this, 'ambient_sound_arr').set(rt.construct(e.get('Array'), [obj({'_building': 'resources', '_soundName': 'Resources ambient loop.wav'}), obj({'_building': 'production', '_soundName': 'Production Ambient loop.wav'}), obj({'_building': 'diplomacy', '_soundName': 'Ambience Diplomacy.wav'}), obj({'_building': 'defense', '_soundName': 'Defence.wav'}), obj({'_building': 'religion', '_soundName': 'Massmedia ambient loop.wav'}), obj({'_building': 'research', '_soundName': 'Technology ambient loop.wav'}), obj({'_building': 'game', '_soundName': 'General ambient.wav'})]))

def register(rt):
    rt.define('Sub_model', None, Sub_model_fields, {'Sub_model': ASFunction(Sub_model_Sub_model), 'get_demo_version_name': ASFunction(Sub_model_get_demo_version_name), 'get_demo_version_url': ASFunction(Sub_model_get_demo_version_url), 'submit_2dplay_score': ASFunction(Sub_model_submit_2dplay_score), 'get_religion_name_by_code': ASFunction(Sub_model_get_religion_name_by_code), 'getCityByID': ASFunction(Sub_model_getCityByID), 'string_is_used_action': ASFunction(Sub_model_string_is_used_action), 'reset_playerAB_position_arr': ASFunction(Sub_model_reset_playerAB_position_arr), 'get_plr_arr_of_action': ASFunction(Sub_model_get_plr_arr_of_action), 'loop_playerAB_position_arr': ASFunction(Sub_model_loop_playerAB_position_arr), 'reset_preAttackFrame': ASFunction(Sub_model_reset_preAttackFrame), 'get_playerAB_mc': ASFunction(Sub_model_get_playerAB_mc), 'setHumanTurnAction': ASFunction(Sub_model_setHumanTurnAction), 'loadTurnAction': ASFunction(Sub_model_loadTurnAction), 'resetPlayersForNewturn': ASFunction(Sub_model_resetPlayersForNewturn), 'error': ASFunction(Sub_model_error), 'productionInvestementPercLeft': ASFunction(Sub_model_productionInvestementPercLeft), 'researchInvestementPercLeft': ASFunction(Sub_model_researchInvestementPercLeft), 'resetUserSelections': ASFunction(Sub_model_resetUserSelections), 'resetAfterCanceledTurnAction': ASFunction(Sub_model_resetAfterCanceledTurnAction), 'setCeaseFire': ASFunction(Sub_model_setCeaseFire), 'select_random_city': ASFunction(Sub_model_select_random_city), 'deselectCities': ASFunction(Sub_model_deselectCities), 'gameStatus': ASFunction(Sub_model_gameStatus), 'createBioHazardArr': ASFunction(Sub_model_createBioHazardArr), 'next_ambient_sound_index': ASFunction(Sub_model_next_ambient_sound_index)}, {'full_version_url': ASFunction(Sub_model___get__full_version_url), 'display_turnMoney': ASFunction(Sub_model___get__display_turnMoney), 'display_population': ASFunction(Sub_model___get__display_population), 'userSelectedActionBtn': ASFunction(Sub_model___get__userSelectedActionBtn), 'userSelectedStockBtn': ASFunction(Sub_model___get__userSelectedStockBtn), 'userSelectedShipCityWaitingForTurnAction': ASFunction(Sub_model___get__userSelectedShipCityWaitingForTurnAction), 'userSelectedShipCityPlrNum': ASFunction(Sub_model___get__userSelectedShipCityPlrNum), 'userSelectedShipCityArr': ASFunction(Sub_model___get__userSelectedShipCityArr), 'userSelectedCity': ASFunction(Sub_model___get__userSelectedCity), 'userSelectedPlayer': ASFunction(Sub_model___get__userSelectedPlayer), 'userSelectedCarrier': ASFunction(Sub_model___get__userSelectedCarrier), 'userSelectedWeapon': ASFunction(Sub_model___get__userSelectedWeapon), 'userSelectedPayload': ASFunction(Sub_model___get__userSelectedPayload), 'userResetPreAttack': ASFunction(Sub_model___get__userResetPreAttack), 'userSelectedResearchArr': ASFunction(Sub_model___get__userSelectedResearchArr), 'userSelectedProductionInvestmentArr': ASFunction(Sub_model___get__userSelectedProductionInvestmentArr), 'userSelectedProductionInvestmentArr_total_amount': ASFunction(Sub_model___get__userSelectedProductionInvestmentArr_total_amount), 'userSelectedDiplomacyArr': ASFunction(Sub_model___get__userSelectedDiplomacyArr), 'userSelectedResearchInvestmentArr': ASFunction(Sub_model___get__userSelectedResearchInvestmentArr), 'userSelectedResearchInvestmentArr_total_amount': ASFunction(Sub_model___get__userSelectedResearchInvestmentArr_total_amount)}, {'broadcaster': ASFunction(Sub_model___set__broadcaster), 'userSelectedActionBtn': ASFunction(Sub_model___set__userSelectedActionBtn), 'userSelectedStockBtn': ASFunction(Sub_model___set__userSelectedStockBtn), 'userSelectedCity': ASFunction(Sub_model___set__userSelectedCity), 'userSelectedShipCityWaitingForTurnAction': ASFunction(Sub_model___set__userSelectedShipCityWaitingForTurnAction), 'userSelectedShipCityArr': ASFunction(Sub_model___set__userSelectedShipCityArr), 'userSelectedShipCityPlrNum': ASFunction(Sub_model___set__userSelectedShipCityPlrNum), 'userSelectedPlayer': ASFunction(Sub_model___set__userSelectedPlayer), 'userSelectedCarrier': ASFunction(Sub_model___set__userSelectedCarrier), 'userSelectedWeapon': ASFunction(Sub_model___set__userSelectedWeapon), 'userSelectedPayload': ASFunction(Sub_model___set__userSelectedPayload), 'userResetPreAttack': ASFunction(Sub_model___set__userResetPreAttack), 'userSelectedProductionInvestmentArr': ASFunction(Sub_model___set__userSelectedProductionInvestmentArr), 'userSelectedResearchArr': ASFunction(Sub_model___set__userSelectedResearchArr), 'userSelectedDiplomacyArr': ASFunction(Sub_model___set__userSelectedDiplomacyArr), 'userSelectedResearchInvestmentArr': ASFunction(Sub_model___set__userSelectedResearchInvestmentArr)})
