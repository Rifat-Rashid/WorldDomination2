# Generated from __Packages/Model.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Model_Model(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc3_', '_loc4_'], closure, 'Model')
    e.call('__super__', [])
    assign(ref(this, 'playing_ambient_sound_arr'), '=', lambda: rt.construct(e.get('Array'), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assign(ref(this, 'battle'), '=', lambda: rt.construct(e.get('Battle'), []))
    assign(ref(this, 'tools'), '=', lambda: rt.construct(e.get('Tools'), []))
    assign(ref(this, 'text_messages'), '=', lambda: rt.construct(e.get('WD2_messages'), []))
    assign(ref(this, 'turnResultsArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'wd_colors'), '=', lambda: rt.construct(e.get('WD_colors'), []))
    assign(ref(this, 'option'), '=', lambda: rt.construct(e.get('Option'), []))
    assign(ref(this, 'playedSounds_arr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'soundCount'), '=', lambda: 0)
    assign(ref(this, 'difficulty_level_specific_vars'), '=', lambda: rt.construct(e.get('Object'), []))
    e.set('_loc3_', ref(this, 'difficulty_level_specific_vars').get())
    assign(ref(e.get('_loc3_'), 'stock_cap_plr'), '=', lambda: rt.construct(e.get('Array'), [4, 4, 4]))
    assign(ref(e.get('_loc3_'), 'stock_cap_enm'), '=', lambda: rt.construct(e.get('Array'), [4, 4, 4]))
    assign(ref(e.get('_loc3_'), 'enemy_start_money'), '=', lambda: rt.construct(e.get('Array'), [50, 65, 60]))
    assign(ref(e.get('_loc3_'), 'player_start_money'), '=', lambda: rt.construct(e.get('Array'), [80, 65, 55]))
    assign(ref(e.get('_loc3_'), 'spy_alert_money'), '=', lambda: rt.construct(e.get('Array'), [180, 150, 100]))
    assign(ref(e.get('_loc3_'), 'enemy_start_religion'), '=', lambda: rt.construct(e.get('Array'), [30, 40, 60]))
    assign(ref(e.get('_loc3_'), 'player_start_relgion'), '=', lambda: rt.construct(e.get('Array'), [80, 60, 20]))
    assign(ref(e.get('_loc3_'), 'spy_steal_money_max'), '=', lambda: rt.construct(e.get('Array'), [90, 120, 150]))
    assign(ref(e.get('_loc3_'), 'start_regard_arr'), '=', lambda: rt.construct(e.get('Array'), [arr([80, 80, 80, 80, 80]), arr([65, 65, 65, 65, 65]), arr([50, 50, 50, 50, 50])]))
    if truth(unary('!', ref(this, 'zs66hj8s').get())):
        assign(ref(e.get('_loc3_'), 'player_start_population'), '=', lambda: rt.construct(e.get('Array'), [500, 450, 400]))
    else:
        assign(ref(e.get('_loc3_'), 'player_start_population'), '=', lambda: rt.construct(e.get('Array'), [250, 250, 200]))
    if truth(unary('!', ref(this, 'zs66hj8s').get())):
        assign(ref(e.get('_loc3_'), 'enemy_start_population'), '=', lambda: rt.construct(e.get('Array'), [450, 450, 450]))
    else:
        assign(ref(e.get('_loc3_'), 'enemy_start_population'), '=', lambda: rt.construct(e.get('Array'), [200, 250, 205]))
    assign(ref(e.get('_loc3_'), 'player_resources_divider'), '=', lambda: rt.construct(e.get('Array'), [9, 11, 13]))
    assign(ref(e.get('_loc3_'), 'enemy_resources_divider'), '=', lambda: rt.construct(e.get('Array'), [9, 10, 12]))
    assign(ref(e.get('_loc3_'), 'enemy_religion_addition'), '=', lambda: rt.construct(e.get('Array'), [45, 35, 25]))
    assign(ref(e.get('_loc3_'), 'player_religion_addition'), '=', lambda: rt.construct(e.get('Array'), [30, 30, 25]))
    assign(ref(this, 'active_ambient_sounds'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'spy_stat_obj'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(this, 'spy_stat_obj').get(), 'spy1'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(ref(this, 'spy_stat_obj').get(), 'spy1').get(), 'weaponStealMax'), '=', lambda: 5)
    assign(ref(ref(ref(this, 'spy_stat_obj').get(), 'spy1').get(), 'moneyStealPrcMax'), '=', lambda: 20)
    assign(ref(ref(this, 'spy_stat_obj').get(), 'spy2'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(ref(this, 'spy_stat_obj').get(), 'spy2').get(), 'weaponStealMax'), '=', lambda: 7)
    assign(ref(ref(ref(this, 'spy_stat_obj').get(), 'spy2').get(), 'moneyStealPrcMax'), '=', lambda: 40)
    assign(ref(ref(this, 'spy_stat_obj').get(), 'spy3'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(ref(this, 'spy_stat_obj').get(), 'spy3').get(), 'weaponStealMax'), '=', lambda: 9)
    assign(ref(ref(ref(this, 'spy_stat_obj').get(), 'spy3').get(), 'moneyStealPrcMax'), '=', lambda: 60)
    assign(ref(ref(this, 'spy_stat_obj').get(), 'spy4'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(ref(this, 'spy_stat_obj').get(), 'spy4').get(), 'weaponStealMax'), '=', lambda: 12)
    assign(ref(ref(ref(this, 'spy_stat_obj').get(), 'spy4').get(), 'moneyStealPrcMax'), '=', lambda: 80)
    assign(ref(this, 'regard_bonus_table_obj'), '=', lambda: rt.construct(e.get('Object'), []))
    e.set('_loc4_', ref(this, 'regard_bonus_table_obj').get())
    assign(ref(e.get('_loc4_'), 'preAttack'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(e.get('_loc4_'), 'preAttack').get(), 'attack'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(e.get('_loc4_'), 'preAttack').get(), 'defend'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(ref(e.get('_loc4_'), 'preAttack').get(), 'attack').get(), 'baseBonus'), '=', lambda: 8)
    assign(ref(ref(ref(e.get('_loc4_'), 'preAttack').get(), 'defend').get(), 'baseBonus'), '=', lambda: 8)
    assign(ref(ref(e.get('_loc4_'), 'preAttack').get(), 'bystander'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(ref(e.get('_loc4_'), 'preAttack').get(), 'bystander').get(), 'baseBonus'), '=', lambda: 6)
    assign(ref(ref(e.get('_loc4_'), 'preAttack').get(), 'wpnLevelDef'), '=', lambda: 4)
    assign(ref(e.get('_loc4_'), 'attack'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(e.get('_loc4_'), 'attack').get(), 'attack'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(ref(e.get('_loc4_'), 'attack').get(), 'attack').get(), 'baseBonus'), '=', lambda: 5)
    assign(ref(ref(e.get('_loc4_'), 'attack').get(), 'defend'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(ref(e.get('_loc4_'), 'attack').get(), 'defend').get(), 'baseBonus'), '=', lambda: 6)
    assign(ref(ref(e.get('_loc4_'), 'attack').get(), 'bystander'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(ref(e.get('_loc4_'), 'attack').get(), 'bystander').get(), 'baseBonus'), '=', lambda: 4)
    assign(ref(ref(e.get('_loc4_'), 'attack').get(), 'wpnLevelMultiplier'), '=', lambda: 4)
    assign(ref(e.get('_loc4_'), 'propaganda'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(e.get('_loc4_'), 'propaganda').get(), 'attack'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(e.get('_loc4_'), 'propaganda').get(), 'defend'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(e.get('_loc4_'), 'propaganda').get(), 'bystander'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(ref(e.get('_loc4_'), 'propaganda').get(), 'attack').get(), 'baseBonuss'), '=', lambda: 6)
    assign(ref(ref(ref(e.get('_loc4_'), 'propaganda').get(), 'defend').get(), 'baseBonus'), '=', lambda: 6)
    assign(ref(ref(ref(e.get('_loc4_'), 'propaganda').get(), 'bystander').get(), 'baseBonus'), '=', lambda: 4)
    assign(ref(e.get('_loc4_'), 'no_retal_bonus'), '=', lambda: 3)
    assign(ref(e.get('_loc4_'), 'sameReligion_bonus'), '=', lambda: 4)
    assign(ref(e.get('_loc4_'), 'standard_regard_bonus'), '=', lambda: 4)
    assign(ref(e.get('_loc4_'), 'diplomacyBonus'), '=', lambda: 3)
    rt.call_ref(ref(ref(e.get('System'), 'security').get(), 'allowDomain'), ['www.totallygame.com'])
    assign(ref(e.get('_root'), 'hs_list'), '=', lambda: False)
    assign(ref(e.get('_root'), 'hs_score'), '=', lambda: 0)
    assign(ref(e.get('_root'), 'is_time'), '=', lambda: False)
    assign(ref(e.get('_root'), 'hs_gameid'), '=', lambda: 39)
    assign(ref(e.get('_root'), 'hs_requesturl'), '=', lambda: 'www.totallygame.com')
    return U

def Model_get_cur_preAttack_arr(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_player'], ['_loc3_', '_loc4_', 'i', 'j', 'param_player'], closure, 'Model')
    e.set('_loc3_', arr([]))
    for key_1 in keys(ref(this, 'activePlayerArr').get()):
        e.ref('i').set(key_1)
        rt.tick()
        try:
            if truth(logical('&&', binop('==', ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'preAttackStatus').get(), 'ready'), lambda: logical('&&', binop('!=', ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'playerNum').get(), ref(e.get('param_player'), 'playerNum').get()), lambda: unary('!', ref(ref(ref(e.get('param_player'), 'ceaseFireArr').get(), ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'playerNum').get()).get(), '_status').get())))):
                for key_2 in keys(ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'turnActionArr').get()):
                    e.ref('j').set(key_2)
                    rt.tick()
                    try:
                        assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'strength').get())
                        rt.call_ref(ref(e.get('_loc3_'), 'push'), [obj({'player': ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'turnAction': ref(ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'turnActionArr').get(), e.get('j')).get(), 'weapon': ref(ref(ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'turnActionArr').get(), e.get('j')).get(), 'attackWeapon').get(), '_strength': e.get('_loc4_')})])
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

def Model_set_city_position_to_array(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_'], closure, 'Model')
    e.set('_loc2_', 0)
    while truth(binop('<', e.get('_loc2_'), ref(ref(this, 'playerArr').get(), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc3_'), ref(ref(this, 'cityPositions').get(), 'length').get())):
                rt.tick()
                try:
                    assign(ref(ref(ref(this, 'cityPositions').get(), e.get('_loc2_')).get(), e.get('_loc3_')), '=', lambda: arr([ref(ref(ref(ref(e.get('_global'), 'view').get(), 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'citypos', e.get('_loc2_')), '_'), e.get('_loc3_'))).get(), '_x').get(), ref(ref(ref(ref(e.get('_global'), 'view').get(), 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'citypos', e.get('_loc2_')), '_'), e.get('_loc3_'))).get(), '_y').get()]))
                    assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Model_get_random_set_enemy(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_plr', 'a_num'], ['_loc4_', '_loc5_', 'a_num', 'a_plr', 'i'], closure, 'Model')
    e.set('_loc4_', rt.construct(e.get('Array'), []))
    e.set('_loc5_', 0)
    for key_3 in keys(ref(this, 'playerArr').get()):
        e.ref('i').set(key_3)
        rt.tick()
        try:
            if truth(logical('&&', binop('!=', ref(ref(this, 'playerArr').get(), e.get('i')).get(), e.get('a_plr')), lambda: logical('&&', binop('!=', ref(ref(ref(this, 'playerArr').get(), e.get('i')).get(), 'playerNum').get(), e.get('a_num')), lambda: ref(ref(ref(this, 'playerArr').get(), e.get('i')).get(), 'alive').get()))):
                rt.call_ref(ref(e.get('_loc4_'), 'push'), [ref(ref(this, 'playerArr').get(), e.get('i')).get()])
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [0, binop('-', ref(e.get('_loc4_'), 'length').get(), 1)]))
    if truth(unary('!', e.get('_loc5_'))):
        assign(e.ref('_loc5_'), '=', lambda: 0)
    return e.get('_loc5_')
    return U

def Model_getPlayerData(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_action', 'param_player'], ['_loc10_', '_loc11_', '_loc12_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', 'i', 'j', 'param_action', 'param_player'], closure, 'Model')
    switch_4 = e.get('param_action')
    case_5 = -1
    if case_5 == -1 and strict_eq(switch_4, 'smallestCitySize'):
        case_5 = 0
    if case_5 == -1 and strict_eq(switch_4, 'largestCitySize'):
        case_5 = 1
    if case_5 == -1 and strict_eq(switch_4, 'largestCity'):
        case_5 = 2
    if case_5 == -1 and strict_eq(switch_4, 'largestCityOnTheMapSize'):
        case_5 = 3
    if case_5 == -1 and strict_eq(switch_4, 'playerStrength'):
        case_5 = 4
    if case_5 == -1 and strict_eq(switch_4, 'weaponStock'):
        case_5 = 5
    if case_5 == -1 and strict_eq(switch_4, 'largestNuclKill'):
        case_5 = 6
    if case_5 == -1 and strict_eq(switch_4, 'largestBioKill'):
        case_5 = 7
    if case_5 == -1 and strict_eq(switch_4, 'techCount'):
        case_5 = 8
    if case_5 == -1:
        case_5 = 9
    try:
        if 0 <= case_5 <= 0:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(e.get('param_player'), 'cityArr').get(), 0).get(), 'population').get())
            for key_6 in keys(ref(e.get('param_player'), 'cityArr').get()):
                e.ref('i').set(key_6)
                rt.tick()
                try:
                    if truth(binop('>', ref(ref(ref(e.get('param_player'), 'cityArr').get(), e.get('i')).get(), 'population').get(), 0)):
                        assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'min'), [e.get('_loc4_'), ref(ref(ref(e.get('param_player'), 'cityArr').get(), e.get('i')).get(), 'population').get()]))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            return e.get('_loc4_')
        if 0 <= case_5 <= 1:
            assign(e.ref('_loc5_'), '=', lambda: ref(ref(ref(e.get('param_player'), 'cityArr').get(), 0).get(), 'population').get())
            for key_7 in keys(ref(e.get('param_player'), 'cityArr').get()):
                e.ref('i').set(key_7)
                rt.tick()
                try:
                    assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'max'), [e.get('_loc5_'), ref(ref(ref(e.get('param_player'), 'cityArr').get(), e.get('i')).get(), 'population').get()]))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            return e.get('_loc5_')
        if 0 <= case_5 <= 2:
            assign(e.ref('_loc6_'), '=', lambda: ref(ref(e.get('param_player'), 'cityArr').get(), 0).get())
            for key_8 in keys(ref(e.get('param_player'), 'cityArr').get()):
                e.ref('i').set(key_8)
                rt.tick()
                try:
                    if truth(binop('<', ref(e.get('_loc6_'), 'population').get(), ref(ref(ref(e.get('param_player'), 'cityArr').get(), e.get('i')).get(), 'population').get())):
                        assign(e.ref('_loc6_'), '=', lambda: ref(ref(e.get('param_player'), 'cityArr').get(), e.get('i')).get())
                except ASContinue:
                    pass
                except ASBreak:
                    break
            return e.get('_loc6_')
        if 0 <= case_5 <= 3:
            assign(e.ref('_loc7_'), '=', lambda: 0)
            for key_9 in keys(ref(this, 'activePlayerArr').get()):
                e.ref('i').set(key_9)
                rt.tick()
                try:
                    for key_10 in keys(ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'cityArr').get()):
                        e.ref('j').set(key_10)
                        rt.tick()
                        try:
                            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'max'), [ref(ref(ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'cityArr').get(), e.get('j')).get(), 'population').get(), e.get('_loc7_')]))
                        except ASContinue:
                            pass
                        except ASBreak:
                            break
                except ASContinue:
                    pass
                except ASBreak:
                    break
            return e.get('_loc7_')
        if 0 <= case_5 <= 4:
            return ref(e.get('param_player'), 'techLevel').get()
        if 0 <= case_5 <= 5:
            return ref(e.get('param_player'), 'weaponStockLevel').get()
        if 0 <= case_5 <= 6:
            assign(e.ref('_loc8_'), '=', lambda: arr(['warhead1', 'warhead2', 'warhead3', 'warhead4']))
            assign(e.ref('_loc9_'), '=', lambda: ref(rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'getWeaponByName'), [ref(e.get('_loc8_'), 0).get()]), 'maxKills').get())
            for key_11 in keys(e.get('_loc8_')):
                e.ref('i').set(key_11)
                rt.tick()
                try:
                    if truth(ref(rt.call_ref(ref(ref(e.get('param_player'), 'techTree').get(), 'getTechByName'), [ref(e.get('_loc8_'), e.get('i')).get()]), 'invented').get()):
                        assign(e.ref('_loc9_'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'max'), [ref(rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'getWeaponByName'), [ref(e.get('_loc8_'), e.get('i')).get()]), 'maxKills').get(), e.get('_loc9_')]))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            return e.get('_loc9_')
        if 0 <= case_5 <= 7:
            assign(e.ref('_loc10_'), '=', lambda: arr(['bioload1', 'bioload2', 'bioload3', 'bioload4']))
            assign(e.ref('_loc11_'), '=', lambda: ref(rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'getWeaponByName'), [ref(e.get('_loc10_'), 0).get()]), 'maxKills').get())
            for key_12 in keys(e.get('_loc10_')):
                e.ref('i').set(key_12)
                rt.tick()
                try:
                    if truth(ref(rt.call_ref(ref(ref(e.get('param_player'), 'techTree').get(), 'getTechByName'), [ref(e.get('_loc10_'), e.get('i')).get()]), 'invented').get()):
                        assign(e.ref('_loc11_'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'max'), [ref(rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'getWeaponByName'), [ref(e.get('_loc10_'), e.get('i')).get()]), 'maxKills').get(), e.get('_loc11_')]))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            return e.get('_loc11_')
        if 0 <= case_5 <= 8:
            assign(e.ref('_loc12_'), '=', lambda: 0)
            for key_13 in keys(ref(ref(e.get('param_player'), 'techTree').get(), 'techArr').get()):
                e.ref('i').set(key_13)
                rt.tick()
                try:
                    if truth(ref(ref(ref(ref(e.get('param_player'), 'techTree').get(), 'techArr').get(), e.get('i')).get(), 'invented').get()):
                        assign(e.ref('_loc12_'), '=', lambda: binop('+', e.get('_loc12_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            return e.get('_loc12_')
        if 0 <= case_5 <= 9:
            return U
    except ASBreak:
        pass
    return U

def Model_calcPoints(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_player'], ['_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc14_', '_loc15_', '_loc16_', '_loc17_', '_loc18_', '_loc19_', '_loc20_', '_loc21_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', 'i', 'param_player'], closure, 'Model')
    e.set('_loc3_', 0)
    e.set('_loc4_', 0)
    e.set('_loc5_', 0)
    e.set('_loc6_', 0)
    e.set('_loc7_', 0)
    e.set('_loc8_', 0)
    assign(e.ref('_loc4_'), '=', lambda: binop('-', ref(ref(ref(this, 'decisionPoints').get(), 'attack').get(), 'base').get(), binop('/', ref(e.get('param_player'), 'lowestRegardNum').get(), 2)))
    if truth(binop('<', e.get('_loc4_'), 0)):
        assign(e.ref('_loc4_'), '=', lambda: 0)
    if truth(binop('==', ref(e.get('param_player'), 'preAttackStatus').get(), 'ready')):
        assign(e.ref('_loc4_'), '+=', lambda: 200)
    if truth(logical('&&', binop('!=', ref(e.get('param_player'), 'preAttackStatus').get(), 'ready'), lambda: logical('&&', binop('<=', ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'availableWeaponsArr').get(), 'length').get(), 0), lambda: unary('!', ref(ref(e.get('param_player'), 'weaponStock').get(), 'spyAvailable').get())))):
        assign(e.ref('_loc3_'), '+=', lambda: e.get('_loc4_'))
        assign(e.ref('_loc4_'), '=', lambda: unary('-', 999))
    else:
        if truth(logical('&&', binop('==', ref(e.get('param_player'), 'preAttackStatus').get(), 'ready'), lambda: unary('!', rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'payloadAvailable'), [ref(e.get('param_player'), 'preAttackWeapon').get()])))):
            assign(e.ref('_loc3_'), '+=', lambda: e.get('_loc4_'))
            assign(e.ref('_loc4_'), '=', lambda: unary('-', 999))
    if truth(ref(e.get('param_player'), 'special_person').get()):
        if truth(binop('<', ref(rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'getWeaponByName'), ['ship']), 'inStock').get(), 0)):
            assign(e.ref('_loc3_'), '+=', lambda: e.get('_loc4_'))
            assign(e.ref('_loc4_'), '=', lambda: unary('-', 999))
        else:
            if truth(binop('<', ref(rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'getWeaponByName'), ['warhead3']), 'inStock').get(), 3)):
                assign(e.ref('_loc3_'), '+=', lambda: e.get('_loc4_'))
                assign(e.ref('_loc4_'), '=', lambda: unary('-', 999))
    if truth(ref(e.get('param_player'), 'suicide_person').get()):
        if truth(binop('<', ref(rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'getWeaponByName'), ['soldier4']), 'inStock').get(), 2)):
            assign(e.ref('_loc3_'), '+=', lambda: e.get('_loc4_'))
            assign(e.ref('_loc4_'), '=', lambda: unary('-', 999))
    e.set('_loc9_', rt.call_ref(ref(this, 'get_cur_preAttack_arr'), [e.get('param_player')]))
    assign(ref(e.get('param_player'), 'preCounterEnemy'), '=', lambda: arr([]))
    for key_14 in keys(e.get('_loc9_')):
        e.ref('i').set(key_14)
        rt.tick()
        try:
            assign(e.ref('_loc10_'), '=', lambda: 0)
            assign(e.ref('_loc11_'), '=', lambda: ref(ref(e.get('_loc9_'), e.get('i')).get(), 'player').get())
            assign(e.ref('_loc10_'), '=', lambda: binop('-', ref(ref(ref(this, 'decisionPoints').get(), 'preCounter').get(), 'base').get(), ref(ref(e.get('param_player'), 'regardArr').get(), ref(e.get('_loc11_'), 'playerNum').get()).get()))
            if truth(binop('>', ref(ref(ref(this, 'decisionPoints').get(), 'preCounter').get(), 'minPopForBonus').get(), ref(e.get('param_player'), 'population').get())):
                assign(e.ref('_loc10_'), '+=', lambda: ref(ref(ref(this, 'decisionPoints').get(), 'preCounter').get(), 'lowPopBonus').get())
            if truth(binop('>', e.get('_loc10_'), e.get('_loc5_'))):
                assign(e.ref('_loc5_'), '=', lambda: e.get('_loc10_'))
                assign(ref(e.get('param_player'), 'preCounterEnemy'), '=', lambda: arr([ref(e.get('_loc9_'), e.get('i')).get()]))
            else:
                if truth(binop('==', e.get('_loc10_'), e.get('_loc5_'))):
                    rt.call_ref(ref(ref(e.get('param_player'), 'preCounterEnemy').get(), 'push'), [ref(e.get('_loc9_'), e.get('i')).get()])
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(e.ref('_loc6_'), '=', lambda: binop('-', ref(ref(ref(this, 'decisionPoints').get(), 'religion').get(), 'base').get(), ref(e.get('param_player'), 'religion').get()))
    e.set('_loc12_', 0)
    for key_15 in keys(ref(this, 'activePlayerArr').get()):
        e.ref('i').set(key_15)
        rt.tick()
        try:
            if truth(binop('>', ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'population').get(), e.get('_loc12_'))):
                assign(e.ref('_loc12_'), '=', lambda: ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'population').get())
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(e.ref('_loc6_'), '+=', lambda: binop('-', binop('-', rt.call_ref(ref(e.get('Math'), 'round'), [binop('*', binop('/', ref(e.get('param_player'), 'population').get(), e.get('_loc12_')), 100)]), ref(e.get('param_player'), 'religion').get()), 20))
    e.set('_loc13_', ref(ref(ref(this, 'decisionPoints').get(), 'propaganda').get(), 'base').get())
    if truth(binop('<', ref(e.get('param_player'), 'religion').get(), 30)):
        assign(e.ref('_loc6_'), '+=', lambda: e.get('_loc13_'))
    if truth(binop('>', ref(e.get('param_player'), 'religion').get(), 90)):
        assign(e.ref('_loc13_'), '+=', lambda: binop('*', ref(ref(ref(this, 'decisionPoints').get(), 'propaganda').get(), 'highReligionBonus').get(), 2))
    else:
        if truth(binop('>', ref(e.get('param_player'), 'religion').get(), 60)):
            assign(e.ref('_loc13_'), '+=', lambda: ref(ref(ref(this, 'decisionPoints').get(), 'propaganda').get(), 'highReligionBonus').get())
    assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [0, 90]))
    if truth(binop('==', rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [1, 3]), 2)):
        assign(e.ref('_loc7_'), '=', lambda: 0)
    if truth(binop('<', ref(e.get('param_player'), 'money').get(), 150)):
        assign(e.ref('_loc8_'), '=', lambda: binop('-', ref(ref(ref(this, 'decisionPoints').get(), 'resources').get(), 'base').get(), rt.call_ref(ref(e.get('Math'), 'round'), [ref(e.get('param_player'), 'weaponStockLevel').get()])))
        assign(e.ref('_loc8_'), '+=', lambda: binop('-', ref(ref(ref(this, 'decisionPoints').get(), 'resources').get(), 'reserveBase').get(), binop('/', binop('/', ref(e.get('param_player'), 'money').get(), ref(ref(ref(this, 'decisionPoints').get(), 'resources').get(), 'maxFunds').get()), 100)))
    if truth(ref(e.get('param_player'), 'special_person').get()):
        if truth(binop('<', ref(rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'getWeaponByName'), ['ship']), 'inStock').get(), 1)):
            assign(e.ref('_loc8_'), '+=', lambda: 250)
        if truth(binop('<', ref(rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'getWeaponByName'), ['warhead3']), 'inStock').get(), 3)):
            assign(e.ref('_loc8_'), '+=', lambda: 250)
    e.set('_loc14_', ref(e.get('param_player'), 'weaponStockLevel').get())
    assign(e.ref('_loc3_'), '+=', lambda: binop('-', ref(ref(ref(this, 'decisionPoints').get(), 'production').get(), 'base').get(), rt.call_ref(ref(e.get('Math'), 'round'), [e.get('_loc14_')])))
    e.set('_loc15_', 0)
    e.set('_loc16_', 0)
    for key_16 in keys(ref(this, 'activePlayerArr').get()):
        e.ref('i').set(key_16)
        rt.tick()
        try:
            if truth(binop('>', ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'weaponStockLevel').get(), e.get('_loc14_'))):
                assign(e.ref('_loc3_'), '+=', lambda: ref(ref(ref(this, 'decisionPoints').get(), 'production').get(), 'enemy_stock_bonus').get())
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(e.ref('_loc3_'), '+=', lambda: binop('/', e.get('_loc15_'), ref(ref(this, 'activePlayerArr').get(), 'length').get()))
    assign(e.ref('_loc3_'), '+=', lambda: ref(e.get('param_player'), 'money').get())
    if truth(binop('<=', ref(e.get('param_player'), 'money').get(), 20)):
        assign(e.ref('_loc8_'), '+=', lambda: e.get('_loc3_'))
        assign(e.ref('_loc3_'), '=', lambda: 0)
    e.set('_loc17_', 0)
    e.set('_loc18_', 0)
    if truth(logical('&&', ref(e.get('param_player'), 'special_person').get(), lambda: binop('>', e.get('_loc3_'), 0))):
        if truth(unary('!', ref(rt.call_ref(ref(ref(e.get('param_player'), 'techTree').get(), 'getTechByName'), ['ship']), 'invented').get())):
            assign(e.ref('_loc17_'), '+=', lambda: e.get('_loc3_'))
            assign(e.ref('_loc3_'), '=', lambda: unary('-', 10))
        else:
            if truth(unary('!', ref(rt.call_ref(ref(ref(e.get('param_player'), 'techTree').get(), 'getTechByName'), ['warhead3']), 'invented').get())):
                assign(e.ref('_loc17_'), '+=', lambda: e.get('_loc3_'))
                assign(e.ref('_loc3_'), '=', lambda: unary('-', 10))
    if truth(logical('&&', ref(e.get('param_player'), 'suicide_person').get(), lambda: binop('>', e.get('_loc3_'), 0))):
        if truth(unary('!', ref(rt.call_ref(ref(ref(e.get('param_player'), 'techTree').get(), 'getTechByName'), ['soldier4']), 'invented').get())):
            assign(e.ref('_loc18_'), '+=', lambda: e.get('_loc3_'))
    e.set('_loc19_', rt.call_ref(ref(e.get('Math'), 'min'), [ref(ref(ref(this, 'decisionPoints').get(), 'research').get(), 'turnCap').get(), ref(this, 'turn').get()]))
    e.set('_loc20_', binop('+', rt.call_ref(ref(this, 'getPlayerData'), ['largestNuclKill', e.get('param_player')]), rt.call_ref(ref(this, 'getPlayerData'), ['largestBioKill', e.get('param_player')])))
    e.set('_loc21_', rt.call_ref(ref(e.get('Math'), 'min'), [ref(ref(ref(this, 'decisionPoints').get(), 'research').get(), 'base').get(), binop('-', rt.call_ref(ref(this, 'getPlayerData'), ['largestCityOnTheMapSize', e.get('param_player')]), e.get('_loc20_'))]))
    assign(e.ref('_loc21_'), '+=', lambda: e.get('_loc17_'))
    assign(e.ref('_loc21_'), '+=', lambda: e.get('_loc18_'))
    assign(e.ref('_loc21_'), '+=', lambda: binop('*', binop('/', ref(this, 'turn').get(), rt.call_ref(ref(this, 'getPlayerData'), ['techCount', e.get('param_player')])), ref(ref(ref(this, 'decisionPoints').get(), 'research').get(), 'techTurnRatioMultiplier').get()))
    assign(e.ref('_loc21_'), '+=', lambda: ref(e.get('param_player'), 'money').get())
    if truth(binop('<=', ref(e.get('param_player'), 'money').get(), binop('*', rt.call_ref(ref(e.get('Math'), 'round'), [binop('/', ref(e.get('param_player'), 'population').get(), ref(ref(ref(this, 'difficulty_level_specific_vars').get(), 'enemy_resources_divider').get(), ref(this, 'difficulty_level').get()).get())]), 2))):
        assign(e.ref('_loc8_'), '+=', lambda: e.get('_loc21_'))
        assign(e.ref('_loc21_'), '=', lambda: 10)
    if truth(logical('&&', ref(e.get('param_player'), 'special_person').get(), lambda: logical('&&', ref(rt.call_ref(ref(ref(e.get('param_player'), 'techTree').get(), 'getTechByName'), ['ship']), 'invented').get(), lambda: logical('&&', ref(rt.call_ref(ref(ref(e.get('param_player'), 'techTree').get(), 'getTechByName'), ['warhead3']), 'invented').get(), lambda: binop('>', e.get('_loc21_'), 0))))):
        assign(e.ref('_loc3_'), '+=', lambda: e.get('_loc21_'))
        assign(e.ref('_loc21_'), '=', lambda: unary('-', 100))
    assign(ref(e.get('param_player'), 'actionArr'), '=', lambda: arr([obj({'id': '_attack', 'amount': e.get('_loc4_')}), obj({'id': 'preCounter', 'amount': e.get('_loc5_'), 'target': ref(e.get('param_player'), 'preCounterEnemy').get()}), obj({'id': 'propaganda', 'amount': e.get('_loc13_')}), obj({'id': 'diplomacy', 'amount': e.get('_loc7_')}), obj({'id': 'religion', 'amount': e.get('_loc6_')}), obj({'id': 'resources', 'amount': e.get('_loc8_')}), obj({'id': 'produce', 'amount': e.get('_loc3_')}), obj({'id': 'research', 'amount': e.get('_loc21_')})]))
    for key_17 in keys(ref(e.get('param_player'), 'actionArr').get()):
        e.ref('i').set(key_17)
        rt.tick()
        try:
            if truth(rt.call_ref(ref(e.get('param_player'), 'isBioloaded'), [ref(ref(ref(e.get('param_player'), 'actionArr').get(), e.get('i')).get(), 'id').get()])):
                rt.call_ref(ref(ref(ref(e.get('param_player'), 'actionArr').get(), e.get('i')).get(), 'splice'), [e.call('Number', [e.get('i')]), 1])
        except ASContinue:
            pass
        except ASBreak:
            break
    if truth(logical('&&', ref(e.get('param_player'), 'special_person').get(), lambda: logical('&&', binop('>', ref(rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'getWeaponByName'), ['ship']), 'inStock').get(), 0), lambda: binop('>', ref(rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'getWeaponByName'), ['warhead3']), 'inStock').get(), 1)))):
        assign(e.ref('_loc4_'), '+=', lambda: 50)
    rt.call_ref(ref(ref(e.get('param_player'), 'actionArr').get(), 'sortOn'), ['amount', binop('|', ref(e.get('Array'), 'NUMERIC').get(), ref(e.get('Array'), 'DESCENDING').get())])
    assign(ref(ref(e.get('param_player'), 'turnAction_1').get(), 'action'), '=', lambda: ref(ref(ref(e.get('param_player'), 'actionArr').get(), 0).get(), 'id').get())
    assign(ref(ref(e.get('param_player'), 'turnAction_2').get(), 'action'), '=', lambda: ref(ref(ref(e.get('param_player'), 'actionArr').get(), 1).get(), 'id').get())
    if truth(logical('&&', binop('>', binop('-', ref(ref(ref(e.get('param_player'), 'actionArr').get(), 0).get(), 'amount').get(), 50), ref(ref(ref(e.get('param_player'), 'actionArr').get(), 1).get(), 'amount').get()), lambda: binop('==', ref(ref(ref(e.get('param_player'), 'actionArr').get(), 0).get(), 'id').get(), '_attack'))):
        assign(ref(ref(e.get('param_player'), 'turnAction_2').get(), 'action'), '=', lambda: '_attack')
    return U

def Model_selectCounterWeapon(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_player', 'param_plr_TA', 'param_enemy', 'param_nmy_TA'], ['param_enemy', 'param_nmy_TA', 'param_player', 'param_plr_TA'], closure, 'Model')
    if truth(logical('&&', binop('==', ref(ref(e.get('param_nmy_TA'), 'attackWeapon').get(), 'weaponType').get(), 'rocketload'), lambda: binop('>', ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'antiRocket').get(), 'inStock').get(), 0))):
        assign(ref(e.get('param_plr_TA'), 'attackWeapon'), '=', lambda: ref(ref(e.get('param_player'), 'weaponStock').get(), 'antiRocket').get())
    else:
        if truth(unary('!', logical('&&', binop('==', ref(ref(e.get('param_nmy_TA'), 'attackWeapon').get(), 'weaponType').get(), 'plane'), lambda: binop('>', ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'antiAir').get(), 'inStock').get(), 0)))):
            return 'none'
        assign(ref(e.get('param_plr_TA'), 'attackWeapon'), '=', lambda: ref(ref(e.get('param_player'), 'weaponStock').get(), 'antiAir').get())
    return U

def Model_getTarget(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_player', 'param_TA'], ['_loc100_', '_loc101_', '_loc102_', '_loc103_', '_loc104_', '_loc105_', '_loc106_', '_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc14_', '_loc15_', '_loc16_', '_loc17_', '_loc18_', '_loc19_', '_loc20_', '_loc21_', '_loc22_', '_loc23_', '_loc24_', '_loc25_', '_loc26_', '_loc27_', '_loc28_', '_loc29_', '_loc30_', '_loc31_', '_loc32_', '_loc33_', '_loc34_', '_loc35_', '_loc36_', '_loc37_', '_loc38_', '_loc39_', '_loc40_', '_loc41_', '_loc42_', '_loc43_', '_loc44_', '_loc45_', '_loc46_', '_loc47_', '_loc48_', '_loc49_', '_loc4_', '_loc50_', '_loc51_', '_loc52_', '_loc53_', '_loc54_', '_loc55_', '_loc56_', '_loc57_', '_loc58_', '_loc59_', '_loc5_', '_loc60_', '_loc61_', '_loc62_', '_loc63_', '_loc64_', '_loc65_', '_loc66_', '_loc67_', '_loc68_', '_loc69_', '_loc6_', '_loc70_', '_loc71_', '_loc72_', '_loc73_', '_loc74_', '_loc75_', '_loc76_', '_loc77_', '_loc78_', '_loc79_', '_loc7_', '_loc80_', '_loc81_', '_loc82_', '_loc83_', '_loc84_', '_loc85_', '_loc86_', '_loc87_', '_loc88_', '_loc89_', '_loc8_', '_loc90_', '_loc91_', '_loc92_', '_loc93_', '_loc94_', '_loc95_', '_loc96_', '_loc97_', '_loc98_', '_loc99_', '_loc9_', 'i', 'j', 'param_TA', 'param_player'], closure, 'Model')
    switch_18 = ref(e.get('param_TA'), 'action').get()
    case_19 = -1
    if case_19 == -1 and strict_eq(switch_18, 'reset'):
        case_19 = 0
    if case_19 == -1 and strict_eq(switch_18, 'set_attack'):
        case_19 = 1
    if case_19 == -1 and strict_eq(switch_18, '_attack'):
        case_19 = 2
    if case_19 == -1 and strict_eq(switch_18, 'preCounter'):
        case_19 = 3
    if case_19 == -1 and strict_eq(switch_18, 'propaganda'):
        case_19 = 4
    if case_19 == -1 and strict_eq(switch_18, 'diplomacy'):
        case_19 = 5
    if case_19 == -1 and strict_eq(switch_18, 'religion'):
        case_19 = 6
    if case_19 == -1 and strict_eq(switch_18, 'resources'):
        case_19 = 7
    if case_19 == -1 and strict_eq(switch_18, 'produce'):
        case_19 = 8
    if case_19 == -1 and strict_eq(switch_18, 'research'):
        case_19 = 9
    if case_19 == -1:
        case_19 = 10
    try:
        if 0 <= case_19 <= 0:
            return False
        if 0 <= case_19 <= 1:
            assign(ref(e.get('param_TA'), 'action'), '=', lambda: 'attack')
            return True
        if 0 <= case_19 <= 2:
            assign(e.ref('_loc4_'), '=', lambda: True)
            assign(e.ref('_loc5_'), '=', lambda: True)
            assign(e.ref('_loc6_'), '=', lambda: True)
            assign(e.ref('_loc7_'), '=', lambda: False)
            assign(e.ref('_loc9_'), '=', lambda: ref(e.get('param_player'), 'preAttackWeapon').get())
            if truth(binop('==', ref(e.get('param_TA'), 'num').get(), 1)):
                assign(e.ref('_loc8_'), '=', lambda: ref(e.get('param_player'), 'turnAction_2').get())
                if truth(binop('==', ref(ref(e.get('param_player'), 'turnAction_2').get(), 'action').get(), 'attack')):
                    assign(e.ref('_loc4_'), '=', lambda: True)
                    assign(e.ref('_loc5_'), '=', lambda: False)
                else:
                    if truth(binop('==', ref(ref(e.get('param_player'), 'turnAction_2').get(), 'action').get(), 'preAttack')):
                        assign(e.ref('_loc4_'), '=', lambda: False)
                        assign(e.ref('_loc5_'), '=', lambda: True)
                    else:
                        if truth(binop('==', ref(ref(e.get('param_player'), 'turnAction_2').get(), 'action').get(), '_attack')):
                            assign(e.ref('_loc4_'), '=', lambda: True)
                            assign(e.ref('_loc5_'), '=', lambda: True)
                            assign(e.ref('_loc7_'), '=', lambda: True)
            else:
                if truth(binop('==', ref(e.get('param_TA'), 'num').get(), 2)):
                    assign(e.ref('_loc8_'), '=', lambda: ref(e.get('param_player'), 'turnAction_1').get())
                    if truth(binop('==', ref(ref(e.get('param_player'), 'turnAction_1').get(), 'action').get(), 'attack')):
                        assign(e.ref('_loc4_'), '=', lambda: True)
                        assign(e.ref('_loc5_'), '=', lambda: False)
                    else:
                        if truth(binop('==', ref(ref(e.get('param_player'), 'turnAction_1').get(), 'action').get(), 'preAttack')):
                            assign(e.ref('_loc4_'), '=', lambda: False)
                            assign(e.ref('_loc5_'), '=', lambda: True)
                        else:
                            if truth(binop('==', ref(ref(e.get('param_player'), 'turnAction_1').get(), 'action').get(), '_attack')):
                                assign(e.ref('_loc4_'), '=', lambda: True)
                                assign(e.ref('_loc5_'), '=', lambda: True)
                                assign(e.ref('_loc7_'), '=', lambda: True)
            assign(e.ref('_loc10_'), '=', lambda: 0)
            assign(e.ref('_loc11_'), '=', lambda: 0)
            for key_20 in keys(ref(this, 'activePlayerArr').get()):
                e.ref('i').set(key_20)
                rt.tick()
                try:
                    if truth(logical('&&', binop('!=', ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'playerNum').get(), ref(e.get('param_player'), 'playerNum').get()), lambda: unary('!', ref(ref(ref(e.get('param_player'), 'ceaseFireArr').get(), ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'playerNum').get()).get(), '_status').get()))):
                        assign(e.ref('_loc12_'), '=', lambda: binop('-', 100, ref(ref(e.get('param_player'), 'regardArr').get(), ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'playerNum').get()).get()))
                        if truth(binop('<', e.get('_loc12_'), 0)):
                            pass
                        if truth(binop('!=', ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'religion_code').get(), ref(e.get('param_player'), 'religion_code').get())):
                            pass
                        if truth(binop('==', ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'playerNum').get(), ref(e.get('param_player'), 'primary_enemy').get())):
                            assign(e.ref('_loc12_'), '+=', lambda: 1)
                        if truth(binop('==', ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'playerNum').get(), ref(e.get('param_player'), 'secundary_enemy').get())):
                            pass
                        if truth(binop('>', e.get('_loc12_'), e.get('_loc10_'))):
                            assign(e.ref('_loc10_'), '=', lambda: e.get('_loc12_'))
                            assign(ref(e.get('param_TA'), 'targetPlayer'), '=', lambda: ref(ref(this, 'activePlayerArr').get(), e.get('i')).get())
                except ASContinue:
                    pass
                except ASBreak:
                    break
            assign(e.ref('_loc13_'), '=', lambda: rt.construct(e.get('Array'), []))
            for key_21 in keys(ref(this, 'activePlayerArr').get()):
                e.ref('i').set(key_21)
                rt.tick()
                try:
                    if truth(logical('&&', binop('!=', ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), e.get('param_player')), lambda: unary('!', ref(ref(ref(e.get('param_player'), 'ceaseFireArr').get(), ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'playerNum').get()).get(), '_status').get()))):
                        rt.call_ref(ref(e.get('_loc13_'), 'push'), [ref(ref(this, 'activePlayerArr').get(), e.get('i')).get()])
                except ASContinue:
                    pass
                except ASBreak:
                    break
            if truth(unary('!', ref(e.get('param_TA'), 'targetPlayer').get())):
                assign(e.ref('_loc14_'), '=', lambda: 100)
                for key_22 in keys(e.get('_loc13_')):
                    e.ref('i').set(key_22)
                    rt.tick()
                    try:
                        if truth(logical('&&', binop('!=', ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), e.get('param_player')), lambda: logical('&&', binop('>', ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'population').get(), 0), lambda: logical('&&', binop('<=', ref(ref(e.get('param_player'), 'regardArr').get(), ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'playerNum').get()).get(), e.get('_loc14_')), lambda: unary('!', ref(ref(ref(e.get('param_player'), 'ceaseFireArr').get(), ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'playerNum').get()).get(), '_status').get()))))):
                            assign(e.ref('_loc14_'), '=', lambda: ref(ref(e.get('param_player'), 'regardArr').get(), ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'playerNum').get()).get())
                            assign(ref(e.get('param_TA'), 'targetPlayer'), '=', lambda: ref(ref(this, 'activePlayerArr').get(), e.get('i')).get())
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
            if truth(unary('!', ref(e.get('param_TA'), 'targetPlayer').get())):
                assign(ref(e.get('param_TA'), 'targetPlayer'), '=', lambda: ref(e.get('_loc13_'), rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [0, binop('-', ref(e.get('_loc13_'), 'length').get(), 1)])).get())
            if truth(unary('!', ref(e.get('param_TA'), 'targetPlayer').get())):
                return False
            if truth(logical('&&', e.get('_loc7_'), lambda: rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [0, 2]))):
                assign(e.ref('_loc7_'), '=', lambda: False)
                assign(ref(e.get('_loc8_'), 'action'), '=', lambda: 'reset')
            assign(e.ref('_loc15_'), '=', lambda: ref(ref(e.get('param_player'), 'weaponStock').get(), 'availableWeaponsArr').get())
            assign(ref(e.get('param_TA'), 'targetCity'), '=', lambda: e.get('undefined'))
            assign(ref(e.get('param_TA'), 'attackWeapon'), '=', lambda: e.get('undefined'))
            rt.call_ref(ref(e.get('_loc15_'), 'sortOn'), ['maxKills', binop('|', ref(e.get('Array'), 'NUMERIC').get(), ref(e.get('Array'), 'DESCENDING').get())])
            assign(e.ref('_loc16_'), '=', lambda: 0)
            assign(e.ref('_loc18_'), '=', lambda: False)
            assign(e.ref('_loc19_'), '=', lambda: 0)
            assign(e.ref('_loc21_'), '=', lambda: False)
            assign(e.ref('_loc22_'), '=', lambda: 0)
            assign(e.ref('_loc23_'), '=', lambda: False)
            if truth(logical('&&', e.get('_loc7_'), lambda: binop('==', ref(e.get('param_player'), 'preAttackStatus').get(), 'ready'))):
                for key_23 in keys(ref(ref(e.get('param_player'), 'weaponStock').get(), 'weaponArr').get()):
                    e.ref('i').set(key_23)
                    rt.tick()
                    try:
                        assign(e.ref('_loc24_'), '=', lambda: ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'weaponArr').get(), e.get('i')).get())
                        if truth(logical('&&', logical('||', binop('==', ref(e.get('_loc24_'), 'weaponCategory').get(), 'payload'), lambda: binop('==', ref(e.get('_loc24_'), 'weaponCategory').get(), 'specialLoad')), lambda: logical('&&', binop('>', ref(e.get('_loc24_'), 'inStock').get(), 0), lambda: logical('&&', binop('<=', ref(e.get('_loc24_'), 'weaponLevel').get(), ref(e.get('_loc9_'), 'weaponLevel').get()), lambda: ref(e.get('_loc24_'), 'active').get())))):
                            assign(e.ref('_loc18_'), '=', lambda: True)
                        if truth(logical('&&', binop('==', ref(e.get('_loc24_'), 'weaponCategory').get(), 'conventional'), lambda: logical('&&', binop('>', ref(e.get('_loc24_'), 'inStock').get(), 0), lambda: ref(e.get('_loc24_'), 'active').get()))):
                            assign(e.ref('_loc21_'), '=', lambda: True)
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
                if truth(logical('||', unary('!', e.get('_loc18_')), lambda: unary('!', e.get('_loc21_')))):
                    assign(e.ref('_loc7_'), '=', lambda: False)
                    assign(ref(e.get('_loc8_'), 'action'), '=', lambda: 'reset')
            if truth(logical('||', e.get('_loc7_'), lambda: binop('==', ref(ref(e.get('param_player'), 'preAttackWeapon').get(), 'weaponName').get(), 'ship'))):
                if truth(binop('==', ref(e.get('param_player'), 'preAttackStatus').get(), 'ready')):
                    if truth(logical('&&', binop('==', ref(ref(e.get('param_player'), 'preAttackWeapon').get(), 'weaponName').get(), 'ship'), lambda: unary('!', ref(e.get('_loc8_'), 'ship_attack_arr').get()))):
                        assign(e.ref('_loc25_'), '=', lambda: ref(ref(e.get('param_player'), 'weaponStock').get(), 'instock_active_payloads_perStock').get())
                        assign(e.ref('_loc26_'), '=', lambda: 0)
                        assign(e.ref('_loc27_'), '=', lambda: False)
                        assign(e.ref('_loc28_'), '=', lambda: rt.construct(e.get('Array'), []))
                        assign(e.ref('_loc29_'), '=', lambda: rt.construct(e.get('Array'), []))
                        assign(e.ref('_loc30_'), '=', lambda: rt.construct(e.get('Array'), []))
                        assign(e.ref('_loc31_'), '=', lambda: 0)
                        while truth(binop('<', e.get('_loc31_'), ref(e.get('_loc25_'), 'length').get())):
                            rt.tick()
                            try:
                                if truth(binop('>', ref(ref(e.get('_loc25_'), e.get('_loc31_')).get(), 'weaponLevel').get(), 3)):
                                    rt.call_ref(ref(e.get('_loc25_'), 'splice'), [e.get('_loc31_'), 1])
                                assign(e.ref('_loc31_'), '=', lambda: binop('+', e.get('_loc31_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        assign(ref(e.get('param_TA'), 'action'), '=', lambda: 'preAttack')
                        assign(ref(e.get('param_TA'), 'preAttackCarrier'), '=', lambda: ref(e.get('param_player'), 'preAttackWeapon').get())
                        if truth(binop('<', ref(e.get('_loc25_'), 'length').get(), 3)):
                            assign(e.ref('_loc26_'), '=', lambda: binop('-', 3, ref(e.get('_loc25_'), 'length').get()))
                            assign(e.ref('_loc27_'), '=', lambda: True)
                        assign(e.ref('_loc32_'), '=', lambda: 0)
                        while truth(binop('<', e.get('_loc32_'), 3)):
                            rt.tick()
                            try:
                                assign(e.ref('_loc33_'), '=', lambda: 0)
                                assign(e.ref('_loc36_'), '=', lambda: 0)
                                while truth(binop('<', e.get('_loc36_'), ref(e.get('_loc25_'), 'length').get())):
                                    rt.tick()
                                    try:
                                        assign(e.ref('_loc37_'), '=', lambda: ref(e.get('_loc25_'), e.get('_loc36_')).get())
                                        if truth(logical('&&', binop('>', ref(e.get('_loc37_'), 'maxKills').get(), e.get('_loc33_')), lambda: binop('<', ref(e.get('_loc37_'), 'weaponLevel').get(), 4))):
                                            assign(e.ref('_loc33_'), '=', lambda: ref(e.get('_loc37_'), 'maxKills').get())
                                            assign(e.ref('_loc34_'), '=', lambda: e.get('_loc37_'))
                                            assign(e.ref('_loc35_'), '=', lambda: e.get('_loc36_'))
                                        assign(e.ref('_loc36_'), '=', lambda: binop('+', e.get('_loc36_'), 1))
                                    except ASContinue:
                                        pass
                                    except ASBreak:
                                        break
                                rt.call_ref(ref(e.get('_loc28_'), 'push'), [e.get('_loc34_')])
                                rt.call_ref(ref(e.get('_loc25_'), 'splice'), [e.get('_loc35_'), 1])
                                assign(e.ref('_loc32_'), '=', lambda: binop('+', e.get('_loc32_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        for key_24 in keys(ref(ref(e.get('param_TA'), 'targetPlayer').get(), 'cityArr').get()):
                            e.ref('i').set(key_24)
                            rt.tick()
                            try:
                                assign(e.ref('_loc38_'), '=', lambda: ref(ref(ref(e.get('param_TA'), 'targetPlayer').get(), 'cityArr').get(), e.get('i')).get())
                                if truth(binop('>', ref(e.get('_loc38_'), 'population').get(), 0)):
                                    rt.call_ref(ref(e.get('_loc29_'), 'push'), [e.get('_loc38_')])
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        assign(ref(e.get('param_TA'), 'ship_attack_arr'), '=', lambda: rt.construct(e.get('Array'), []))
                        assign(e.ref('_loc39_'), '=', lambda: 0)
                        while truth(binop('<', e.get('_loc39_'), 3)):
                            rt.tick()
                            try:
                                assign(e.ref('_loc40_'), '=', lambda: rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [0, binop('-', ref(e.get('_loc29_'), 'length').get(), 1)]))
                                rt.call_ref(ref(ref(e.get('param_TA'), 'ship_attack_arr').get(), 'push'), [obj({'city': ref(ref(e.get('_loc29_'), e.get('_loc40_')).get(), 'cityID').get(), 'wpn': ref(ref(e.get('_loc28_'), e.get('_loc39_')).get(), 'weaponID').get()})])
                                assign(e.ref('_loc39_'), '=', lambda: binop('+', e.get('_loc39_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        for key_25 in keys(e.get('_loc15_')):
                            e.ref('i').set(key_25)
                            rt.tick()
                            try:
                                assign(e.ref('_loc41_'), '=', lambda: ref(e.get('_loc15_'), e.get('i')).get())
                                if truth(logical('&&', binop('==', ref(e.get('_loc41_'), 'weaponCategory').get(), 'conventional'), lambda: binop('>', ref(e.get('_loc41_'), 'maxKills').get(), e.get('_loc19_')))):
                                    assign(e.ref('_loc19_'), '=', lambda: ref(e.get('_loc41_'), 'maxKills').get())
                                    assign(e.ref('_loc20_'), '=', lambda: e.get('_loc41_'))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        for key_26 in keys(ref(ref(e.get('param_TA'), 'targetPlayer').get(), 'cityArr').get()):
                            e.ref('i').set(key_26)
                            rt.tick()
                            try:
                                assign(e.ref('_loc42_'), '=', lambda: ref(ref(ref(e.get('param_TA'), 'targetPlayer').get(), 'cityArr').get(), e.get('i')).get())
                                if truth(binop('>', ref(e.get('_loc42_'), 'population').get(), 0)):
                                    assign(ref(e.get('_loc8_'), 'action'), '=', lambda: 'attack')
                                    assign(ref(e.get('_loc8_'), 'targetCity'), '=', lambda: e.get('_loc42_'))
                                    assign(ref(e.get('_loc8_'), 'attackWeapon'), '=', lambda: e.get('_loc20_'))
                                    assign(ref(e.get('_loc8_'), 'targetPlayer'), '=', lambda: ref(e.get('param_TA'), 'targetPlayer').get())
                                    raise ASBreak()
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                    else:
                        assign(e.ref('_loc43_'), '=', lambda: ref(ref(e.get('param_player'), 'weaponStock').get(), 'instock_active_payloads').get())
                        for key_27 in keys(e.get('_loc15_')):
                            e.ref('i').set(key_27)
                            rt.tick()
                            try:
                                assign(e.ref('_loc44_'), '=', lambda: ref(e.get('_loc15_'), e.get('i')).get())
                                if truth(logical('&&', binop('==', ref(e.get('_loc44_'), 'weaponCategory').get(), 'conventional'), lambda: binop('>', ref(e.get('_loc44_'), 'maxKills').get(), e.get('_loc19_')))):
                                    assign(e.ref('_loc19_'), '=', lambda: ref(e.get('_loc44_'), 'maxKills').get())
                                    assign(e.ref('_loc20_'), '=', lambda: e.get('_loc44_'))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        assign(e.ref('_loc17_'), '=', lambda: rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'get_MaxKillPayload'), [e.get('_loc9_')]))
                        assign(e.ref('_loc16_'), '=', lambda: ref(e.get('_loc17_'), 'maxKills').get())
                        assign(e.ref('_loc22_'), '=', lambda: binop('+', e.get('_loc16_'), e.get('_loc19_')))
                        assign(e.ref('_loc45_'), '=', lambda: 0)
                        for key_28 in keys(ref(ref(e.get('param_TA'), 'targetPlayer').get(), 'cityArr').get()):
                            e.ref('i').set(key_28)
                            rt.tick()
                            try:
                                assign(e.ref('_loc46_'), '=', lambda: ref(ref(ref(e.get('param_TA'), 'targetPlayer').get(), 'cityArr').get(), e.get('i')).get())
                                if truth(logical('&&', binop('<', ref(e.get('_loc46_'), 'population').get(), e.get('_loc22_')), lambda: logical('&&', binop('>', ref(e.get('_loc46_'), 'population').get(), e.get('_loc45_')), lambda: binop('>', ref(e.get('_loc46_'), 'population').get(), 0)))):
                                    assign(e.ref('_loc45_'), '=', lambda: ref(e.get('_loc46_'), 'population').get())
                                    assign(e.ref('_loc23_'), '=', lambda: True)
                                    assign(ref(e.get('param_TA'), 'action'), '=', lambda: 'preAttack')
                                    assign(ref(e.get('param_TA'), 'targetCity'), '=', lambda: e.get('_loc46_'))
                                    assign(ref(e.get('param_TA'), 'attackWeapon'), '=', lambda: e.get('_loc17_'))
                                    assign(ref(e.get('param_TA'), 'preAttackPayload'), '=', lambda: e.get('_loc17_'))
                                    assign(ref(e.get('param_TA'), 'preAttackCarrier'), '=', lambda: ref(e.get('param_player'), 'preAttackWeapon').get())
                                    assign(ref(e.get('_loc8_'), 'action'), '=', lambda: 'set_attack')
                                    assign(ref(e.get('_loc8_'), 'targetCity'), '=', lambda: e.get('_loc46_'))
                                    assign(ref(e.get('_loc8_'), 'attackWeapon'), '=', lambda: e.get('_loc20_'))
                                    assign(ref(e.get('_loc8_'), 'targetPlayer'), '=', lambda: ref(e.get('param_TA'), 'targetPlayer').get())
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        if truth(unary('!', e.get('_loc23_'))):
                            assign(ref(e.get('param_TA'), 'action'), '=', lambda: 'preAttack')
                            assign(ref(e.get('param_TA'), 'targetCity'), '=', lambda: rt.call_ref(ref(this, 'select_random_city'), [ref(e.get('param_TA'), 'targetPlayer').get()]))
                            assign(ref(e.get('param_TA'), 'attackWeapon'), '=', lambda: e.get('_loc17_'))
                            assign(ref(e.get('param_TA'), 'preAttackPayload'), '=', lambda: e.get('_loc17_'))
                            assign(ref(e.get('param_TA'), 'preAttackCarrier'), '=', lambda: ref(e.get('param_player'), 'preAttackWeapon').get())
                            assign(ref(e.get('_loc8_'), 'action'), '=', lambda: 'attack')
                            assign(ref(e.get('_loc8_'), 'attackWeapon'), '=', lambda: e.get('_loc20_'))
                            assign(ref(e.get('_loc8_'), 'targetCity'), '=', lambda: rt.call_ref(ref(this, 'select_random_city'), [ref(e.get('param_TA'), 'targetPlayer').get()]))
                            assign(ref(e.get('_loc8_'), 'targetPlayer'), '=', lambda: ref(e.get('param_TA'), 'targetPlayer').get())
                else:
                    assign(e.ref('_loc47_'), '=', lambda: rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [1, 2]))
                    if truth(binop('==', e.get('_loc47_'), 1)):
                        assign(ref(e.get('param_TA'), 'action'), '=', lambda: 'preAttack')
                        assign(ref(e.get('_loc8_'), 'action'), '=', lambda: 'reset')
                        assign(ref(e.get('param_TA'), 'preAttackCarrier'), '=', lambda: ref(ref(e.get('param_player'), 'weaponStock').get(), 'randomAvailableCarrier').get())
                    if truth(binop('==', e.get('_loc47_'), 2)):
                        assign(ref(e.get('param_TA'), 'action'), '=', lambda: 'attack')
                        assign(ref(e.get('param_TA'), 'targetCity'), '=', lambda: rt.call_ref(ref(this, 'select_random_city'), [ref(e.get('param_TA'), 'targetPlayer').get()]))
                        assign(ref(e.get('_loc8_'), 'targetPlayer'), '=', lambda: ref(e.get('param_TA'), 'targetPlayer').get())
                        assign(ref(e.get('_loc8_'), 'action'), '=', lambda: 'reset')
                        assign(e.ref('_loc48_'), '=', lambda: arr([]))
                        for key_29 in keys(e.get('_loc15_')):
                            e.ref('i').set(key_29)
                            rt.tick()
                            try:
                                assign(e.ref('_loc49_'), '=', lambda: ref(e.get('_loc15_'), e.get('i')).get())
                                if truth(binop('==', ref(e.get('_loc49_'), 'weaponType').get(), 'soldier')):
                                    rt.call_ref(ref(e.get('_loc48_'), 'push'), [e.get('_loc49_')])
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        assign(ref(e.get('param_TA'), 'attackWeapon'), '=', lambda: ref(e.get('_loc48_'), rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [0, 3])).get())
            else:
                if truth(unary('!', e.get('_loc7_'))):
                    assign(e.ref('_loc50_'), '=', lambda: ref(ref(e.get('param_player'), 'weaponStock').get(), 'instock_active_payloads').get())
                    assign(e.ref('_loc16_'), '=', lambda: 0)
                    if truth(binop('==', ref(e.get('param_player'), 'preAttackStatus').get(), 'ready')):
                        for key_30 in keys(e.get('_loc50_')):
                            e.ref('i').set(key_30)
                            rt.tick()
                            try:
                                assign(e.ref('_loc51_'), '=', lambda: ref(e.get('_loc50_'), e.get('i')).get())
                                if truth(logical('&&', binop('==', ref(e.get('_loc51_'), 'weaponCategory').get(), 'payload'), lambda: logical('&&', binop('>', ref(e.get('_loc51_'), 'maxKills').get(), e.get('_loc16_')), lambda: binop('<=', ref(e.get('_loc51_'), 'weaponLevel').get(), ref(ref(e.get('param_player'), 'preAttackWeapon').get(), 'weaponLevel').get())))):
                                    assign(e.ref('_loc16_'), '=', lambda: ref(e.get('_loc51_'), 'maxKills').get())
                                    assign(e.ref('_loc17_'), '=', lambda: e.get('_loc51_'))
                                else:
                                    if truth(logical('&&', binop('==', ref(e.get('_loc51_'), 'weaponCategory').get(), 'specialLoad'), lambda: binop('==', ref(ref(e.get('param_player'), 'preAttackWeapon').get(), 'weaponName').get(), 'space'))):
                                        assign(e.ref('_loc16_'), '=', lambda: ref(e.get('_loc51_'), 'maxKills').get())
                                        assign(e.ref('_loc17_'), '=', lambda: e.get('_loc51_'))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        assign(ref(e.get('param_TA'), 'preAttackPayload'), '=', lambda: assign(ref(e.get('param_TA'), 'attackWeapon'), '=', lambda: e.get('_loc17_')))
                        assign(ref(e.get('param_TA'), 'preAttackCarrier'), '=', lambda: ref(e.get('param_player'), 'preAttackWeapon').get())
                        assign(ref(e.get('param_TA'), 'action'), '=', lambda: 'preAttack')
                        for key_31 in keys(ref(ref(e.get('param_TA'), 'targetPlayer').get(), 'cityArr').get()):
                            e.ref('i').set(key_31)
                            rt.tick()
                            try:
                                assign(e.ref('_loc52_'), '=', lambda: ref(ref(ref(e.get('param_TA'), 'targetPlayer').get(), 'cityArr').get(), e.get('i')).get())
                                if truth(logical('&&', binop('<=', ref(e.get('_loc52_'), 'population').get(), e.get('_loc16_')), lambda: binop('>', ref(e.get('_loc52_'), 'population').get(), 0))):
                                    assign(ref(e.get('param_TA'), 'targetCity'), '=', lambda: e.get('_loc52_'))
                                    assign(e.ref('_loc23_'), '=', lambda: True)
                                    assign(e.ref('_loc23_'), '=', lambda: True)
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        if truth(unary('!', e.get('_loc23_'))):
                            assign(ref(e.get('param_TA'), 'targetCity'), '=', lambda: rt.call_ref(ref(this, 'select_random_city'), [ref(e.get('param_TA'), 'targetPlayer').get()]))
                    else:
                        assign(e.ref('_loc54_'), '=', lambda: ref(ref(e.get('param_player'), 'weaponStock').get(), 'allowPre').get())
                        assign(e.ref('_loc55_'), '=', lambda: ref(ref(e.get('param_player'), 'weaponStock').get(), 'allowDir').get())
                        if truth(logical('&&', e.get('_loc55_'), lambda: e.get('_loc54_'))):
                            assign(e.ref('_loc53_'), '=', lambda: rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [1, 2]))
                        else:
                            if truth(logical('&&', unary('!', e.get('_loc55_')), lambda: e.get('_loc54_'))):
                                assign(e.ref('_loc53_'), '=', lambda: 1)
                            else:
                                if truth(logical('&&', e.get('_loc55_'), lambda: unary('!', e.get('_loc54_')))):
                                    assign(e.ref('_loc53_'), '=', lambda: 2)
                        if truth(binop('==', e.get('_loc53_'), 1)):
                            assign(ref(e.get('param_TA'), 'action'), '=', lambda: 'preAttack')
                            assign(ref(e.get('_loc8_'), 'action'), '=', lambda: 'reset')
                            assign(ref(e.get('param_TA'), 'preAttackCarrier'), '=', lambda: ref(ref(e.get('param_player'), 'weaponStock').get(), 'randomAvailableCarrier').get())
                        if truth(binop('==', e.get('_loc53_'), 2)):
                            assign(ref(e.get('param_TA'), 'action'), '=', lambda: 'attack')
                            assign(ref(e.get('param_TA'), 'targetCity'), '=', lambda: rt.call_ref(ref(this, 'select_random_city'), [ref(e.get('param_TA'), 'targetPlayer').get()]))
                            assign(ref(e.get('_loc8_'), 'action'), '=', lambda: 'reset')
                            assign(e.ref('_loc56_'), '=', lambda: arr([]))
                            for key_32 in keys(e.get('_loc15_')):
                                e.ref('i').set(key_32)
                                rt.tick()
                                try:
                                    assign(e.ref('_loc57_'), '=', lambda: ref(e.get('_loc15_'), e.get('i')).get())
                                    if truth(binop('==', ref(e.get('_loc57_'), 'weaponType').get(), 'soldier')):
                                        rt.call_ref(ref(e.get('_loc56_'), 'push'), [e.get('_loc57_')])
                                except ASContinue:
                                    pass
                                except ASBreak:
                                    break
                            assign(ref(e.get('param_TA'), 'attackWeapon'), '=', lambda: ref(e.get('_loc56_'), rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [0, 3])).get())
            assign(e.ref('_loc58_'), '=', lambda: ref(ref(e.get('param_player'), 'weaponStock').get(), 'availableSpies_obj').get())
            assign(e.ref('_loc59_'), '=', lambda: rt.construct(e.get('Object'), []))
            assign(ref(e.get('_loc59_'), '_level'), '=', lambda: 0)
            assign(ref(e.get('_loc59_'), '_amount'), '=', lambda: 0)
            assign(ref(e.get('_loc59_'), '_plr'), '=', lambda: e.get('undefined'))
            assign(e.ref('_loc61_'), '=', lambda: 0)
            assign(e.ref('_loc62_'), '=', lambda: False)
            if truth(ref(ref(e.get('param_player'), 'weaponStock').get(), 'spyAvailable').get()):
                for key_33 in keys(ref(this, 'activePlayerArr').get()):
                    e.ref('i').set(key_33)
                    rt.tick()
                    try:
                        assign(e.ref('_loc61_'), '=', lambda: 0)
                        assign(e.ref('_loc63_'), '=', lambda: ref(ref(this, 'activePlayerArr').get(), e.get('i')).get())
                        assign(e.ref('_loc60_'), '=', lambda: ref(ref(e.get('_loc63_'), 'weaponStock').get(), 'inStock_perLevel_obj').get())
                        assign(e.ref('_loc64_'), '=', lambda: 1)
                        while truth(binop('<', e.get('_loc64_'), 5)):
                            rt.tick()
                            try:
                                if truth(logical('&&', binop('>', ref(e.get('_loc60_'), binop('+', '_level', e.get('_loc64_'))).get(), ref(e.get('_loc59_'), '_amount').get()), lambda: logical('&&', binop('>', e.get('_loc64_'), ref(e.get('_loc59_'), '_level').get()), lambda: logical('&&', binop('!=', e.get('_loc63_'), e.get('param_player')), lambda: logical('&&', binop('>=', ref(e.get('_loc60_'), binop('+', '_level', e.get('_loc64_'))).get(), ref(ref(this, 'AI_spy_required_stock_obj').get(), binop('+', '_level', e.get('_loc64_'))).get()), lambda: logical('&&', binop('>', ref(e.get('_loc58_'), binop('+', '_level', e.get('_loc64_'))).get(), 0), lambda: binop('>=', binop('/', ref(e.get('param_player'), 'spy_readiness').get(), 25), e.get('_loc64_')))))))):
                                    assign(ref(e.get('_loc59_'), '_amount'), '=', lambda: ref(e.get('_loc60_'), binop('+', '_level', e.get('_loc64_'))).get())
                                    assign(ref(e.get('_loc59_'), '_level'), '=', lambda: e.get('_loc64_'))
                                    assign(ref(e.get('_loc59_'), '_plr'), '=', lambda: e.get('_loc63_'))
                                assign(e.ref('_loc64_'), '=', lambda: binop('+', e.get('_loc64_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
                if truth(binop('>', ref(ref(this, 'human').get(), 'money').get(), rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [ref(ref(ref(this, 'difficulty_level_specific_vars').get(), 'spy_alert_money').get(), ref(this, 'difficulty_level').get()).get(), 240]))):
                    assign(ref(e.get('_loc59_'), '_level'), '=', lambda: rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'get_highest_spy_level'), []))
                    assign(ref(e.get('_loc59_'), '_plr'), '=', lambda: ref(this, 'human').get())
                    assign(e.ref('_loc62_'), '=', lambda: True)
            if truth(logical('&&', unary('!', ref(e.get('param_TA'), 'attackWeapon').get()), lambda: logical('&&', unary('!', ref(e.get('param_TA'), 'preAttackCarrier').get()), lambda: ref(e.get('_loc59_'), '_plr').get()))):
                assign(e.ref('_loc62_'), '=', lambda: True)
            else:
                if truth(logical('&&', ref(e.get('param_TA'), 'attackWeapon').get(), lambda: logical('&&', unary('!', ref(e.get('param_TA'), 'preAttackCarrier').get()), lambda: ref(e.get('_loc59_'), '_plr').get()))):
                    assign(e.ref('_loc65_'), '=', lambda: rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [0, 6]))
                    if truth(binop('==', e.get('_loc65_'), 3)):
                        assign(e.ref('_loc62_'), '=', lambda: True)
            if truth(e.get('_loc62_')):
                if truth(logical('||', binop('==', ref(ref(e.get('param_player'), 'turnAction_1').get(), 'action').get(), 'attack'), lambda: binop('==', ref(ref(e.get('param_player'), 'turnAction_1').get(), 'action').get(), 'set_attack'))):
                    assign(e.ref('_loc66_'), '=', lambda: ref(e.get('param_player'), 'turnAction_1').get())
                else:
                    if truth(logical('||', binop('==', ref(ref(e.get('param_player'), 'turnAction_2').get(), 'action').get(), 'attack'), lambda: binop('==', ref(ref(e.get('param_player'), 'turnAction_2').get(), 'action').get(), 'set_attack'))):
                        assign(e.ref('_loc66_'), '=', lambda: ref(e.get('param_player'), 'turnAction_2').get())
                    else:
                        assign(e.ref('_loc66_'), '=', lambda: e.get('param_TA'))
                assign(ref(e.get('_loc66_'), 'action'), '=', lambda: 'attack')
                assign(ref(e.get('_loc66_'), 'attackWeapon'), '=', lambda: rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'select_spy_by_level'), [ref(e.get('_loc59_'), '_level').get()]))
                assign(ref(e.get('_loc66_'), 'targetCity'), '=', lambda: rt.call_ref(ref(this, 'select_random_city'), [ref(e.get('_loc59_'), '_plr').get()]))
                assign(ref(e.get('_loc66_'), 'spyBuilding'), '=', lambda: ref(ref(this, 'spyBuildingArr').get(), rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [1, binop('-', ref(ref(this, 'spyBuildingArr').get(), 'length').get(), 1)])).get())
                assign(ref(e.get('_loc66_'), 'targetPlayer'), '=', lambda: ref(e.get('_loc59_'), '_plr').get())
                assign(e.ref('param_TA'), '=', lambda: e.get('_loc66_'))
            if truth(logical('&&', unary('!', ref(e.get('param_TA'), 'attackWeapon').get()), lambda: unary('!', ref(e.get('param_TA'), 'preAttackCarrier').get()))):
                return False
            if truth(logical('&&', ref(e.get('param_TA'), 'preAttackCarrier').get(), lambda: logical('&&', binop('==', ref(e.get('param_player'), 'preAttackStatus').get(), 'ready'), lambda: logical('&&', unary('!', ref(e.get('param_TA'), 'preAttackPayload').get()), lambda: unary('!', ref(e.get('param_TA'), 'ship_attack_arr').get()))))):
                return False
            return True
            raise ASBreak()
        if 0 <= case_19 <= 3:
            rt.call_ref(ref(ref(e.get('param_player'), 'preCounterEnemy').get(), 'sortOn'), ['_strength', binop('|', ref(e.get('Array'), 'DESCENDING').get(), ref(e.get('Array'), 'NUMERIC').get())])
            assign(e.ref('_loc67_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc67_'), ref(ref(e.get('param_player'), 'preCounterEnemy').get(), 'length').get())):
                rt.tick()
                try:
                    if truth(ref(ref(ref(ref(e.get('param_player'), 'preCounterEnemy').get(), e.get('_loc67_')).get(), 'player').get(), 'preAttackWeapon').get()):
                        assign(e.ref('_loc68_'), '=', lambda: ref(ref(ref(e.get('param_player'), 'preCounterEnemy').get(), e.get('_loc67_')).get(), 'player').get())
                        assign(e.ref('_loc69_'), '=', lambda: ref(ref(ref(e.get('param_player'), 'preCounterEnemy').get(), e.get('_loc67_')).get(), 'turnAction').get())
                        assign(e.ref('_loc70_'), '=', lambda: rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'getWeaponByName'), [ref(ref(ref(ref(ref(e.get('param_player'), 'preCounterEnemy').get(), e.get('_loc67_')).get(), 'player').get(), 'preAttackWeapon').get(), 'counteredBy').get()]))
                        if truth(binop('>', ref(e.get('_loc70_'), 'inStock').get(), 0)):
                            assign(ref(e.get('param_TA'), 'attackWeapon'), '=', lambda: e.get('_loc70_'))
                            return True
                    assign(e.ref('_loc67_'), '=', lambda: binop('+', e.get('_loc67_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            return False
        if 0 <= case_19 <= 4:
            assign(e.ref('_loc71_'), '=', lambda: 0)
            assign(e.ref('_loc72_'), '=', lambda: 0)
            assign(e.ref('_loc73_'), '=', lambda: 0)
            assign(e.ref('_loc74_'), '=', lambda: 0)
            for key_34 in keys(ref(this, 'activePlayerArr').get()):
                e.ref('i').set(key_34)
                rt.tick()
                try:
                    assign(e.ref('_loc75_'), '=', lambda: ref(ref(this, 'activePlayerArr').get(), e.get('i')).get())
                    if truth(logical('&&', unary('!', ref(ref(ref(e.get('param_player'), 'ceaseFireArr').get(), ref(e.get('_loc75_'), 'playerNum').get()).get(), '_status').get()), lambda: binop('!=', e.get('_loc75_'), e.get('param_player')))):
                        assign(e.ref('_loc73_'), '=', lambda: binop('-', 100, ref(e.get('_loc75_'), 'religion').get()))
                        assign(e.ref('_loc73_'), '+=', lambda: ref(rt.call_ref(ref(e.get('_loc75_'), 'largest_city'), []), 'population').get())
                        assign(e.ref('_loc73_'), '-=', lambda: ref(ref(e.get('param_player'), 'regardArr').get(), ref(e.get('_loc75_'), 'playerNum').get()).get())
                        if truth(binop('>', e.get('_loc73_'), e.get('_loc71_'))):
                            assign(e.ref('_loc71_'), '=', lambda: e.get('_loc73_'))
                            assign(ref(e.get('param_TA'), 'targetPlayer'), '=', lambda: e.get('_loc75_'))
                            assign(ref(e.get('param_TA'), 'targetCity'), '=', lambda: rt.call_ref(ref(e.get('_loc75_'), 'largest_city'), []))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            if truth(logical('||', unary('!', ref(e.get('param_TA'), 'targetPlayer').get()), lambda: unary('!', ref(e.get('param_TA'), 'targetCity').get()))):
                return False
            return True
            raise ASBreak()
        if 0 <= case_19 <= 5:
            assign(e.ref('_loc80_'), '=', lambda: False)
            assign(e.ref('_loc82_'), '=', lambda: False)
            assign(e.ref('_loc83_'), '=', lambda: '')
            for key_35 in keys(ref(this, 'activePlayerArr').get()):
                e.ref('i').set(key_35)
                rt.tick()
                try:
                    assign(e.ref('_loc77_'), '=', lambda: ref(ref(this, 'activePlayerArr').get(), e.get('i')).get())
                    if truth(logical('&&', binop('!=', e.get('_loc77_'), e.get('param_player')), lambda: unary('!', ref(ref(ref(e.get('param_player'), 'ceaseFireArr').get(), ref(e.get('_loc77_'), 'playerNum').get()).get(), '_status').get()))):
                        if truth(unary('!', e.get('_loc78_'))):
                            assign(e.ref('_loc78_'), '=', lambda: ref(e.get('_loc77_'), 'population').get())
                            assign(e.ref('_loc76_'), '=', lambda: e.get('_loc77_'))
                        else:
                            if truth(binop('>', e.get('_loc78_'), ref(e.get('_loc77_'), 'population').get())):
                                assign(e.ref('_loc76_'), '=', lambda: e.get('_loc77_'))
                                assign(e.ref('_loc78_'), '=', lambda: ref(e.get('_loc77_'), 'population').get())
                except ASContinue:
                    pass
                except ASBreak:
                    break
            if truth(binop('>', ref(e.get('_loc76_'), 'money').get(), ref(e.get('param_player'), 'money').get())):
                assign(e.ref('_loc81_'), '=', lambda: e.get('_loc76_'))
                assign(e.ref('_loc82_'), '=', lambda: True)
            e.get('_loc78_')
            assign(e.ref('_loc84_'), '=', lambda: 0)
            for key_36 in keys(ref(this, 'activePlayerArr').get()):
                e.ref('i').set(key_36)
                rt.tick()
                try:
                    assign(e.ref('_loc77_'), '=', lambda: ref(ref(this, 'activePlayerArr').get(), e.get('i')).get())
                    if truth(logical('&&', binop('!=', e.get('_loc77_'), e.get('param_player')), lambda: logical('&&', unary('!', ref(ref(ref(e.get('param_player'), 'ceaseFireArr').get(), ref(e.get('_loc77_'), 'playerNum').get()).get(), '_status').get()), lambda: unary('!', ref(ref(e.get('param_player'), 'diplomacy_offeredLastTurn').get(), ref(e.get('_loc77_'), 'playerNum').get()).get())))):
                        assign(e.ref('_loc84_'), '=', lambda: rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [1, 5]))
                        if truth(logical('||', unary('!', e.get('_loc78_')), lambda: binop('>', e.get('_loc84_'), e.get('_loc78_')))):
                            assign(e.ref('_loc78_'), '=', lambda: e.get('_loc84_'))
                            assign(e.ref('_loc85_'), '=', lambda: e.get('_loc77_'))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            if truth(binop('>', ref(e.get('_loc85_'), 'population').get(), ref(e.get('param_player'), 'population').get())):
                assign(e.ref('_loc79_'), '=', lambda: e.get('_loc85_'))
                assign(e.ref('_loc80_'), '=', lambda: True)
            if truth(logical('&&', unary('!', ref(ref(ref(e.get('param_player'), 'ceaseFireArr').get(), 0).get(), '_status').get()), lambda: unary('!', ref(ref(e.get('param_player'), 'diplomacy_offeredLastTurn').get(), 0).get()))):
                if truth(logical('&&', binop('>', ref(ref(this, 'human').get(), 'money').get(), 50), lambda: binop('<', ref(ref(e.get('param_player'), 'regardArr').get(), 0).get(), 50))):
                    assign(e.ref('_loc81_'), '=', lambda: ref(this, 'human').get())
                    assign(e.ref('_loc82_'), '=', lambda: True)
                if truth(logical('&&', binop('>', ref(e.get('param_player'), 'money').get(), 50), lambda: binop('>', ref(ref(e.get('param_player'), 'regardArr').get(), 0).get(), 50))):
                    assign(e.ref('_loc79_'), '=', lambda: ref(this, 'human').get())
                    assign(e.ref('_loc80_'), '=', lambda: True)
            if truth(logical('&&', e.get('_loc80_'), lambda: e.get('_loc82_'))):
                if truth(binop('==', rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [0, 1]), 1)):
                    assign(e.ref('_loc83_'), '=', lambda: 'offer')
                else:
                    assign(e.ref('_loc83_'), '=', lambda: 'demand')
            else:
                if truth(e.get('_loc80_')):
                    assign(e.ref('_loc83_'), '=', lambda: 'offer')
                else:
                    if truth(e.get('_loc82_')):
                        assign(e.ref('_loc83_'), '=', lambda: 'demand')
            if truth(binop('==', e.get('_loc83_'), 'offer')):
                assign(e.ref('_loc86_'), '=', lambda: 0)
                while truth(binop('<', e.get('_loc86_'), ref(ref(this, 'diplomacy_options_arr').get(), 'length').get())):
                    rt.tick()
                    try:
                        if truth(logical('&&', binop('==', ref(ref(ref(this, 'diplomacy_options_arr').get(), e.get('_loc86_')).get(), 0).get(), 'offer'), lambda: binop('<', ref(ref(ref(this, 'diplomacy_options_arr').get(), e.get('_loc86_')).get(), 2).get(), ref(e.get('param_player'), 'turnMoney').get()))):
                            assign(ref(e.get('param_TA'), 'diplomacyLeader'), '=', lambda: ref(e.get('_loc79_'), 'playerNum').get())
                            assign(ref(e.get('param_TA'), 'diplomacyOption'), '=', lambda: e.call('Number', [e.get('_loc86_')]))
                        assign(e.ref('_loc86_'), '=', lambda: binop('+', e.get('_loc86_'), 1))
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
            else:
                assign(e.ref('_loc87_'), '=', lambda: 0)
                while truth(binop('<', e.get('_loc87_'), ref(ref(this, 'diplomacy_options_arr').get(), 'length').get())):
                    rt.tick()
                    try:
                        if truth(logical('&&', binop('==', ref(ref(ref(this, 'diplomacy_options_arr').get(), e.get('_loc87_')).get(), 0).get(), 'demand'), lambda: binop('<', ref(ref(ref(this, 'diplomacy_options_arr').get(), e.get('_loc87_')).get(), 2).get(), ref(e.get('_loc81_'), 'money').get()))):
                            assign(ref(e.get('param_TA'), 'diplomacyLeader'), '=', lambda: ref(e.get('_loc81_'), 'playerNum').get())
                            assign(ref(e.get('param_TA'), 'diplomacyOption'), '=', lambda: e.call('Number', [e.get('_loc87_')]))
                        assign(e.ref('_loc87_'), '=', lambda: binop('+', e.get('_loc87_'), 1))
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
            if truth(logical('||', ref(e.get('param_TA'), 'diplomacyLeader').get(), lambda: binop('==', ref(e.get('param_TA'), 'diplomacyLeader').get(), 0))):
                return True
            return False
            raise ASBreak()
        if 0 <= case_19 <= 6:
            return True
        if 0 <= case_19 <= 7:
            if truth(binop('<', ref(e.get('param_player'), 'money').get(), 150)):
                return True
            return False
            raise ASBreak()
        if 0 <= case_19 <= 8:
            assign(e.ref('_loc88_'), '=', lambda: rt.construct(e.get('Array'), []))
            assign(e.ref('_loc89_'), '=', lambda: 0)
            assign(e.ref('_loc90_'), '=', lambda: 0)
            assign(e.ref('_loc91_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc91_'), 8)):
                rt.tick()
                try:
                    assign(e.ref('_loc89_'), '=', lambda: 0)
                    for key_37 in keys(ref(ref(e.get('param_player'), 'weaponStock').get(), 'weaponArr').get()):
                        e.ref('j').set(key_37)
                        rt.tick()
                        try:
                            assign(e.ref('_loc92_'), '=', lambda: ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'weaponArr').get(), e.get('j')).get())
                            if truth(logical('&&', binop('>', ref(e.get('_loc92_'), 'desire').get(), ref(e.get('_loc92_'), 'inStock').get()), lambda: logical('&&', binop('==', e.get('_loc91_'), ref(e.get('_loc92_'), 'desireGroup').get()), lambda: rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'is_activeCategory'), [ref(e.get('_loc92_'), 'desireGroup').get()])))):
                                assign(e.ref('_loc89_'), '+=', lambda: binop('-', ref(e.get('_loc92_'), 'desire').get(), ref(e.get('_loc92_'), 'inStock').get()))
                        except ASContinue:
                            pass
                        except ASBreak:
                            break
                    rt.call_ref(ref(e.get('_loc88_'), 'push'), [obj({'_cat': e.get('_loc91_'), '_dif': e.get('_loc89_'), '_perc': 0})])
                    assign(e.ref('_loc91_'), '=', lambda: binop('+', e.get('_loc91_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            rt.call_ref(ref(e.get('_loc88_'), 'sortOn'), ['_dif', binop('|', ref(e.get('Array'), 'DESCENDING').get(), ref(e.get('Array'), 'NUMERIC').get())])
            assign(e.ref('_loc93_'), '=', lambda: rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [1, 4]))
            if truth(ref(e.get('param_player'), 'special_person').get()):
                assign(e.ref('_loc93_'), '=', lambda: 2)
            if truth(ref(e.get('param_player'), 'suicide_person').get()):
                assign(e.ref('_loc93_'), '=', lambda: 1)
            assign(e.ref('_loc94_'), '=', lambda: 0)
            if truth(logical('||', binop('<', ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'antiAir').get(), 'inStock').get(), 1), lambda: binop('<', ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'antiRocket').get(), 'inStock').get(), 1))):
                assign(e.ref('_loc94_'), '=', lambda: rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [20, 35]))
                assign(e.ref('_loc90_'), '=', lambda: e.get('_loc94_'))
            assign(e.ref('_loc95_'), '=', lambda: binop('*', rt.call_ref(ref(e.get('Math'), 'round'), [binop('/', rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [80, 100]), 10)]), 10))
            assign(e.ref('_loc96_'), '=', lambda: 0)
            assign(e.ref('_loc97_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc97_'), e.get('_loc93_'))):
                rt.tick()
                try:
                    if truth(rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'is_activeCategory'), [ref(ref(e.get('_loc88_'), e.get('_loc97_')).get(), '_cat').get()])):
                        if truth(binop('<', rt.call_ref(ref(ref(e.get('param_player'), 'weaponStock').get(), 'active_dCat_count'), []), 4)):
                            assign(e.ref('_loc96_'), '=', lambda: binop('*', rt.call_ref(ref(e.get('Math'), 'round'), [binop('/', rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [40, 60]), 10)]), 10))
                        else:
                            assign(e.ref('_loc96_'), '=', lambda: binop('*', rt.call_ref(ref(e.get('Math'), 'round'), [binop('/', rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [0, 60]), 10)]), 10))
                        if truth(ref(e.get('param_player'), 'special_person').get()):
                            assign(e.ref('_loc96_'), '=', lambda: 50)
                        if truth(binop('>', binop('+', e.get('_loc90_'), e.get('_loc96_')), e.get('_loc95_'))):
                            assign(e.ref('_loc96_'), '=', lambda: binop('-', e.get('_loc95_'), e.get('_loc90_')))
                            assign(e.ref('_loc90_'), '=', lambda: e.get('_loc95_'))
                        else:
                            assign(e.ref('_loc90_'), '+=', lambda: e.get('_loc96_'))
                        assign(ref(ref(e.get('_loc88_'), e.get('_loc97_')).get(), '_perc'), '=', lambda: e.get('_loc96_'))
                    assign(e.ref('_loc97_'), '=', lambda: binop('+', e.get('_loc97_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            rt.call_ref(ref(e.get('_loc88_'), 'sortOn'), ['_cat'])
            assign(e.ref('_loc98_'), '=', lambda: 0)
            assign(e.ref('_loc99_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc99_'), 9)):
                rt.tick()
                try:
                    if truth(binop('==', ref(ref(ref(e.get('param_TA'), 'productionInvestmentArr').get(), e.get('_loc99_')).get(), 0).get(), 'defense')):
                        assign(ref(ref(ref(e.get('param_TA'), 'productionInvestmentArr').get(), e.get('_loc99_')).get(), 1), '=', lambda: e.get('_loc94_'))
                        assign(ref(ref(ref(e.get('param_TA'), 'productionInvestmentArr').get(), e.get('_loc99_')).get(), 3), '=', lambda: rt.call_ref(ref(e.get('Math'), 'floor'), [binop('*', binop('/', ref(e.get('param_player'), 'turnMoney').get(), 100), e.get('_loc94_'))]))
                    else:
                        assign(e.ref('_loc100_'), '=', lambda: 0)
                        while truth(binop('<', e.get('_loc100_'), 9)):
                            rt.tick()
                            try:
                                if truth(binop('==', ref(ref(ref(e.get('param_TA'), 'productionInvestmentArr').get(), e.get('_loc100_')).get(), 2).get(), ref(ref(e.get('_loc88_'), e.get('_loc99_')).get(), '_cat').get())):
                                    assign(ref(ref(ref(e.get('param_TA'), 'productionInvestmentArr').get(), e.get('_loc100_')).get(), 1), '=', lambda: ref(ref(e.get('_loc88_'), e.get('_loc99_')).get(), '_perc').get())
                                    assign(ref(ref(ref(e.get('param_TA'), 'productionInvestmentArr').get(), e.get('_loc100_')).get(), 3), '=', lambda: rt.call_ref(ref(e.get('Math'), 'floor'), [binop('*', binop('/', ref(e.get('param_player'), 'turnMoney').get(), 100), ref(ref(e.get('_loc88_'), e.get('_loc99_')).get(), '_perc').get())]))
                                assign(e.ref('_loc100_'), '=', lambda: binop('+', e.get('_loc100_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                    assign(e.ref('_loc98_'), '+=', lambda: ref(ref(ref(e.get('param_TA'), 'productionInvestmentArr').get(), e.get('_loc99_')).get(), 3).get())
                    assign(e.ref('_loc99_'), '=', lambda: binop('+', e.get('_loc99_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            assign(ref(e.get('param_player'), 'turnMoney'), '-=', lambda: e.get('_loc98_'))
            assign(ref(e.get('param_TA'), 'action'), '=', lambda: 'production')
            return True
        if 0 <= case_19 <= 9:
            assign(e.ref('_loc101_'), '=', lambda: arr([]))
            assign(e.ref('_loc102_'), '=', lambda: rt.construct(e.get('Array'), []))
            assign(e.ref('_loc103_'), '=', lambda: 0)
            if truth(binop('==', ref(e.get('param_TA'), 'num').get(), 2)):
                assign(e.ref('_loc103_'), '=', lambda: ref(e.get('param_player'), 'turnMoney').get())
            else:
                assign(e.ref('_loc103_'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [binop('*', binop('/', ref(e.get('param_player'), 'turnMoney').get(), 100), rt.call_ref(ref(ref(this, 'tools').get(), 'randRange'), [20, 80]))]))
            if truth(ref(e.get('param_player'), 'special_person').get()):
                assign(e.ref('_loc103_'), '=', lambda: ref(e.get('param_player'), 'turnMoney').get())
            for key_38 in keys(ref(ref(e.get('param_player'), 'techTree').get(), 'techArr').get()):
                e.ref('i').set(key_38)
                rt.tick()
                try:
                    assign(e.ref('_loc104_'), '=', lambda: ref(ref(ref(e.get('param_player'), 'techTree').get(), 'techArr').get(), e.get('i')).get())
                    if truth(logical('&&', unary('!', ref(e.get('_loc104_'), 'invented').get()), lambda: logical('&&', binop('>', ref(e.get('param_player'), 'money').get(), ref(e.get('_loc104_'), 'cost').get()), lambda: logical('||', ref(ref(e.get('_loc104_'), 'requiredTech').get(), 'invented').get(), lambda: binop('==', ref(e.get('_loc104_'), 'techLevel').get(), 1))))):
                        if truth(binop('!=', ref(e.get('_loc104_'), 'desireGroup').get(), 7)):
                            rt.call_ref(ref(e.get('_loc101_'), 'push'), [e.get('_loc104_')])
                        else:
                            if truth(ref(ref(e.get('param_player'), 'techTree').get(), 'allow_special').get()):
                                rt.call_ref(ref(e.get('_loc101_'), 'push'), [e.get('_loc104_')])
                except ASContinue:
                    pass
                except ASBreak:
                    break
            rt.call_ref(ref(e.get('_loc101_'), 'sortOn'), ['desire', binop('|', ref(e.get('Array'), 'DESCENDING').get(), ref(e.get('Array'), 'NUMERIC').get())])
            assign(e.ref('_loc105_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc105_'), ref(e.get('_loc101_'), 'length').get())):
                rt.tick()
                try:
                    assign(e.ref('_loc106_'), '=', lambda: ref(e.get('_loc101_'), e.get('_loc105_')).get())
                    if truth(logical('&&', binop('>', e.get('_loc103_'), ref(e.get('_loc106_'), 'cost').get()), lambda: logical('||', binop('>', ref(ref(e.get('_loc101_'), e.get('_loc105_')).get(), 'desire').get(), 0), lambda: ref(e.get('param_player'), 'special_person').get()))):
                        rt.call_ref(ref(e.get('_loc102_'), 'push'), [obj({'techID': ref(e.get('_loc106_'), 'techID').get()})])
                        assign(e.ref('_loc103_'), '-=', lambda: ref(e.get('_loc106_'), 'cost').get())
                        assign(ref(e.get('param_player'), 'turnMoney'), '-=', lambda: ref(e.get('_loc106_'), 'cost').get())
                    assign(e.ref('_loc105_'), '=', lambda: binop('+', e.get('_loc105_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            assign(ref(e.get('param_TA'), 'researchArr'), '=', lambda: e.get('_loc102_'))
            if truth(unary('!', ref(ref(e.get('param_TA'), 'researchArr').get(), 0).get())):
                return False
            return True
            raise ASBreak()
        if 0 <= case_19 <= 10:
            return U
    except ASBreak:
        pass
    return U

def Model_populationPercentage(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_plr'], ['_loc3_', '_plr', 'i'], closure, 'Model')
    e.set('_loc3_', 0)
    for key_39 in keys(ref(this, 'activePlayerArr').get()):
        e.ref('i').set(key_39)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '+=', lambda: ref(ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), 'population').get())
        except ASContinue:
            pass
        except ASBreak:
            break
    return rt.call_ref(ref(e.get('Math'), 'round'), [binop('*', binop('/', ref(e.get('_plr'), 'population').get(), e.get('_loc3_')), 100)])
    return U

def Model_killPlayer(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_plr'], ['_loc3_', 'i', 'k', 'param_plr'], closure, 'Model')
    for key_40 in keys(ref(e.get('param_plr'), 'cityArr').get()):
        e.ref('i').set(key_40)
        rt.tick()
        try:
            assign(ref(ref(ref(e.get('param_plr'), 'cityArr').get(), e.get('i')).get(), 'population'), '=', lambda: 0)
            rt.call_ref(ref(ref(ref(e.get('param_plr'), 'cityArr').get(), e.get('i')).get(), 'removeBioload'), [])
            rt.call_ref(ref(ref(ref(ref(e.get('param_plr'), 'cityArr').get(), e.get('i')).get(), 'image').get(), 'gotoAndStop'), ['empty'])
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc3_', 0)
    while truth(binop('<', e.get('_loc3_'), ref(ref(this, 'activePlayerArr').get(), 'length').get())):
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'activePlayerArr').get(), e.get('_loc3_')).get(), 'playerNum').get(), ref(e.get('param_plr'), 'playerNum').get())):
                rt.call_ref(ref(ref(this, 'activePlayerArr').get(), 'splice'), [e.get('_loc3_'), 1])
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_41 in keys(ref(this, 'playerArr').get()):
        e.ref('k').set(key_41)
        rt.tick()
        try:
            if truth(logical('&&', unary('!', ref(ref(ref(this, 'playerArr').get(), e.get('k')).get(), 'alive').get()), lambda: binop('==', ref(ref(ref(this, 'playerArr').get(), e.get('k')).get(), 'lastAttackedBy_num').get(), ref(e.get('param_plr'), 'playerNum').get()))):
                assign(ref(ref(ref(this, 'playerArr').get(), e.get('k')).get(), 'lastattackedby_num'), '=', lambda: ref(e.get('param_plr'), 'lastAttackedBy_num').get())
        except ASContinue:
            pass
        except ASBreak:
            break
    rt.call_ref(ref(e.get('param_plr'), 'kill'), [])
    return U

def Model_calcBattle(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['plr', 'plr_TA'], ['_loc4_', 'plr', 'plr_TA'], closure, 'Model')
    e.set('_loc4_', ref(e.get('plr_TA'), 'targetPlayer').get())
    if truth(binop('==', ref(ref(e.get('_loc4_'), 'counterWeapon').get(), 'weaponName').get(), ref(ref(e.get('plr_TA'), 'preAttackCarrier').get(), 'counteredBy').get())):
        rt.call_ref(ref(ref(e.get('_loc4_'), 'weaponStock').get(), 'reduceWeaponByname'), [ref(ref(e.get('_loc4_'), 'counterWeapon').get(), 'weaponName').get()])
    else:
        assign(ref(ref(e.get('plr_TA'), 'targetCity').get(), 'population'), '-=', lambda: ref(ref(e.get('plr_TA'), 'attackWeapon').get(), 'maxKills').get())
        if truth(logical('&&', binop('==', ref(e.get('plr'), 'playedBy').get(), 'AI'), lambda: binop('>', ref(ref(e.get('plr'), 'regardArr').get(), ref(e.get('_loc4_'), 'playerNum').get()).get(), 0))):
            assign(ref(ref(e.get('plr'), 'regardArr').get(), ref(e.get('_loc4_'), 'playerNum').get()), '-=', lambda: 8)
        if truth(logical('&&', binop('==', ref(e.get('_loc4_'), 'playedBy').get(), 'AI'), lambda: binop('>', ref(ref(e.get('_loc4_'), 'regardArr').get(), ref(e.get('plr'), 'playerNum').get()).get(), 0))):
            assign(ref(ref(e.get('_loc4_'), 'regardArr').get(), ref(e.get('plr'), 'playerNum').get()), '-=', lambda: 8)
    rt.call_ref(ref(ref(e.get('plr'), 'weaponStock').get(), 'reduceWeaponByName'), [ref(ref(e.get('plr_TA'), 'attackWeapon').get(), 'weaponName').get(), 1])
    return U

def Model_AI_consider_diplomacyArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_plr', '_arr'], ['_arr', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', '_plr'], closure, 'Model')
    e.set('_loc4_', ref(ref(this, 'diplomacy_options_arr').get(), ref(e.get('_arr'), '_option').get()).get())
    e.set('_loc5_', ref(e.get('_loc4_'), 1).get())
    e.set('_loc6_', ref(e.get('_loc4_'), 2).get())
    e.set('_loc7_', ref(ref(this, 'playerArr').get(), ref(e.get('_arr'), '_leader').get()).get())
    e.set('_loc8_', 2)
    e.set('_loc9_', 0)
    if truth(binop('==', ref(e.get('_loc4_'), 0).get(), 'offer')):
        if truth(binop('>', ref(ref(e.get('_plr'), 'regardArr').get(), ref(e.get('_arr'), '_leader').get()).get(), 50)):
            assign(e.ref('_loc8_'), '=', lambda: binop('+', e.get('_loc8_'), 1))
        else:
            assign(e.ref('_loc9_'), '=', lambda: binop('+', e.get('_loc9_'), 1))
        assign(e.ref('_loc8_'), '+=', lambda: binop('*', ref(e.get('_arr'), '_option').get(), 4))
        if truth(binop('<', ref(e.get('_plr'), 'strength').get(), ref(e.get('_loc7_'), 'strength').get())):
            assign(e.ref('_loc8_'), '=', lambda: binop('+', e.get('_loc8_'), 1))
        else:
            assign(e.ref('_loc9_'), '=', lambda: binop('+', e.get('_loc9_'), 1))
        if truth(binop('>', ref(e.get('_loc7_'), 'population').get(), ref(e.get('_plr'), 'population').get())):
            assign(e.ref('_loc8_'), '=', lambda: binop('+', e.get('_loc8_'), 1))
        if truth(binop('<', ref(e.get('_plr'), 'money').get(), 30)):
            assign(e.ref('_loc8_'), '=', lambda: binop('+', e.get('_loc8_'), 1))
    else:
        if truth(binop('==', ref(e.get('_loc4_'), 0).get(), 'demand')):
            if truth(binop('>', ref(ref(e.get('_plr'), 'regardArr').get(), ref(e.get('_arr'), '_leader').get()).get(), 50)):
                assign(e.ref('_loc8_'), '=', lambda: binop('+', e.get('_loc8_'), 1))
            else:
                assign(e.ref('_loc9_'), '=', lambda: binop('+', e.get('_loc9_'), 1))
            assign(e.ref('_loc9_'), '+=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [binop('/', ref(e.get('_arr'), '_option').get(), 2)]))
            if truth(binop('<', ref(e.get('_plr'), 'strength').get(), ref(e.get('_loc7_'), 'strength').get())):
                assign(e.ref('_loc8_'), '=', lambda: binop('+', e.get('_loc8_'), 1))
            else:
                assign(e.ref('_loc9_'), '=', lambda: binop('+', e.get('_loc9_'), 1))
            if truth(binop('<', ref(e.get('_plr'), 'strength').get(), binop('/', ref(e.get('_loc7_'), 'strength').get(), 2))):
                assign(e.ref('_loc8_'), '+=', lambda: 2)
            else:
                assign(e.ref('_loc9_'), '=', lambda: binop('+', e.get('_loc9_'), 1))
            if truth(binop('>', ref(e.get('_loc7_'), 'population').get(), ref(e.get('_plr'), 'population').get())):
                assign(e.ref('_loc8_'), '=', lambda: binop('+', e.get('_loc8_'), 1))
            else:
                assign(e.ref('_loc9_'), '=', lambda: binop('+', e.get('_loc9_'), 1))
    if truth(binop('>', e.get('_loc8_'), e.get('_loc9_'))):
        if truth(binop('==', ref(e.get('_loc4_'), 0).get(), 'demand')):
            if truth(binop('>=', ref(e.get('_plr'), 'turnMoney').get(), ref(e.get('_loc4_'), 2).get())):
                rt.call_ref(ref(ref(e.get('_plr'), 'diplomacyAcceptedArr').get(), 'push'), [e.get('_arr')])
                assign(ref(e.get('_plr'), 'turnMoney'), '-=', lambda: ref(e.get('_loc4_'), 2).get())
            else:
                rt.call_ref(ref(ref(e.get('_plr'), 'diplomacyRejectedArr').get(), 'push'), [e.get('_arr')])
        else:
            if truth(binop('==', ref(e.get('_loc4_'), 0).get(), 'offer')):
                rt.call_ref(ref(ref(e.get('_plr'), 'diplomacyAcceptedArr').get(), 'push'), [e.get('_arr')])
    else:
        rt.call_ref(ref(ref(e.get('_plr'), 'diplomacyRejectedArr').get(), 'push'), [e.get('_arr')])
    return U

def Model_doTurn(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', 'i', 'j'], closure, 'Model')
    for key_42 in keys(ref(this, 'activePlayerArr').get()):
        e.ref('i').set(key_42)
        rt.tick()
        try:
            if truth(binop('!=', ref(ref(this, 'activePlayerArr').get(), e.get('i')).get(), ref(this, 'human').get())):
                assign(e.ref('_loc2_'), '=', lambda: ref(ref(this, 'activePlayerArr').get(), e.get('i')).get())
                assign(ref(e.get('_loc2_'), 'turnMoney'), '=', lambda: ref(e.get('_loc2_'), 'money').get())
                if truth(ref(ref(e.get('_loc2_'), 'diplomacyPendingArr').get(), 0).get()):
                    for key_43 in keys(ref(e.get('_loc2_'), 'diplomacyPendingArr').get()):
                        e.ref('j').set(key_43)
                        rt.tick()
                        try:
                            rt.call_ref(ref(this, 'AI_consider_diplomacyArr'), [e.get('_loc2_'), ref(ref(e.get('_loc2_'), 'diplomacyPendingArr').get(), e.get('j')).get()])
                            assign(ref(ref(e.get('_loc2_'), 'diplomacyPendingArr').get(), e.get('j')), '=', lambda: e.get('undefined'))
                        except ASContinue:
                            pass
                        except ASBreak:
                            break
                    assign(ref(e.get('_loc2_'), 'diplomacyPendingArr'), '=', lambda: arr([]))
                    assign(ref(e.get('_loc2_'), 'diplomacyPendingArr'), '=', lambda: rt.construct(e.get('Array'), []))
                rt.call_ref(ref(this, 'calcPoints'), [e.get('_loc2_')])
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc3_', 0)
    while truth(binop('<', e.get('_loc3_'), ref(ref(this, 'activePlayerArr').get(), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(this, 'activePlayerArr').get(), e.get('_loc3_')).get())
            if truth(binop('!=', e.get('_loc4_'), ref(this, 'human').get())):
                assign(e.ref('_loc5_'), '=', lambda: 0)
                for key_44 in keys(ref(e.get('_loc4_'), 'actionArr').get()):
                    e.ref('j').set(key_44)
                    rt.tick()
                    try:
                        if truth(rt.call_ref(ref(this, 'getTarget'), [e.get('_loc4_'), ref(e.get('_loc4_'), 'turnAction_1').get()])):
                            assign(e.ref('_loc5_'), '=', lambda: binop('+', e.get('_loc5_'), 1))
                            raise ASBreak()
                        assign(ref(ref(e.get('_loc4_'), 'turnAction_1').get(), 'action'), '=', lambda: ref(ref(ref(e.get('_loc4_'), 'actionArr').get(), e.get('_loc5_')).get(), 'id').get())
                        assign(ref(ref(e.get('_loc4_'), 'turnAction_2').get(), 'action'), '=', lambda: ref(ref(ref(e.get('_loc4_'), 'actionArr').get(), binop('+', e.get('_loc5_'), 1)).get(), 'id').get())
                        assign(e.ref('_loc5_'), '=', lambda: binop('+', e.get('_loc5_'), 1))
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
                for key_45 in keys(ref(e.get('_loc4_'), 'actionArr').get()):
                    e.ref('j').set(key_45)
                    rt.tick()
                    try:
                        if truth(rt.call_ref(ref(this, 'getTarget'), [e.get('_loc4_'), ref(e.get('_loc4_'), 'turnAction_2').get()])):
                            assign(e.ref('_loc5_'), '=', lambda: binop('+', e.get('_loc5_'), 1))
                            raise ASBreak()
                        assign(ref(ref(e.get('_loc4_'), 'turnAction_2').get(), 'action'), '=', lambda: ref(ref(ref(e.get('_loc4_'), 'actionArr').get(), e.get('_loc5_')).get(), 'id').get())
                        assign(e.ref('_loc5_'), '=', lambda: binop('+', e.get('_loc5_'), 1))
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_46 in keys(ref(this, 'playerArr').get()):
        e.ref('i').set(key_46)
        rt.tick()
        try:
            assign(e.ref('_loc6_'), '=', lambda: ref(ref(this, 'playerArr').get(), e.get('i')).get())
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(this, 'turn'), '=', lambda: binop('+', ref(this, 'turn').get(), 1))
    return U

def Model_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Model')
    pass

def register(rt):
    rt.define('Model', 'Sub_model', Model_fields, {'Model': ASFunction(Model_Model), 'get_cur_preAttack_arr': ASFunction(Model_get_cur_preAttack_arr), 'set_city_position_to_array': ASFunction(Model_set_city_position_to_array), 'get_random_set_enemy': ASFunction(Model_get_random_set_enemy), 'getPlayerData': ASFunction(Model_getPlayerData), 'calcPoints': ASFunction(Model_calcPoints), 'selectCounterWeapon': ASFunction(Model_selectCounterWeapon), 'getTarget': ASFunction(Model_getTarget), 'populationPercentage': ASFunction(Model_populationPercentage), 'killPlayer': ASFunction(Model_killPlayer), 'calcBattle': ASFunction(Model_calcBattle), 'AI_consider_diplomacyArr': ASFunction(Model_AI_consider_diplomacyArr), 'doTurn': ASFunction(Model_doTurn)}, {}, {})
