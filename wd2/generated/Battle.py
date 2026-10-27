# Generated from __Packages/Battle.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Battle_Battle(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Battle')
    assign(ref(this, 'model'), '=', lambda: ref(e.get('_global'), 'model').get())
    assign(ref(this, '_activeUnitsArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, '_toDeleteUnitsArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, '_toShowTimedABArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, '_toShowInBattleABArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, '_toShowInitABArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, '_toShowLastABArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, '_toDeleteExplosionMC_arr'), '=', lambda: rt.construct(e.get('Array'), []))
    return U

def Battle_createBattleScriptVars(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', 'i'], closure, 'Battle')
    rt.call_ref(ref(this, 'resetBattle'), [])
    rt.call_ref(ref(this, 'createToShowABArray'), [])
    assign(ref(ref(e.get('_global'), 'model').get(), 'battleTimerArr'), '=', lambda: arr([]))
    e.set('_loc2_', 0)
    while truth(binop('<', e.get('_loc2_'), 15)):
        rt.tick()
        try:
            rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'battleTimerArr').get(), 'push'), [rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [50, 60])])
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(this, 'tmpBattleArr'), '=', lambda: arr([]))
    assign(ref(this, 'randUnitOrderArr'), '=', lambda: arr([]))
    for key_1 in keys(ref(ref(e.get('_global'), 'model').get(), 'turnResultsArr').get()):
        e.ref('i').set(key_1)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'turnResultsArr').get(), e.get('i')).get())
            if truth(logical('||', binop('==', ref(e.get('_loc3_'), '_item').get(), 'battle'), lambda: logical('||', binop('==', ref(e.get('_loc3_'), '_item').get(), 'diplomacy'), lambda: logical('||', binop('==', ref(e.get('_loc3_'), '_item').get(), 'resources'), lambda: logical('||', binop('==', ref(e.get('_loc3_'), '_item').get(), 'propaganda'), lambda: binop('==', ref(e.get('_loc3_'), '_item').get(), 'religion')))))):
                rt.call_ref(ref(ref(this, 'tmpBattleArr').get(), 'push'), [e.get('_loc3_')])
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_2 in keys(ref(this, '_toShowInBattleABArr').get()):
        e.ref('i').set(key_2)
        rt.tick()
        try:
            pass
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc4_', 0)
    e.set('_loc5_', 0)
    while truth(binop('<=', e.get('_loc5_'), ref(ref(ref(e.get('_global'), 'model').get(), 'orderOfActions_arr').get(), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc6_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc6_'), ref(ref(this, 'tmpBattleArr').get(), 'length').get())):
                rt.tick()
                try:
                    if truth(binop('==', ref(ref(ref(this, 'tmpBattleArr').get(), e.get('_loc6_')).get(), '_item').get(), ref(ref(ref(e.get('_global'), 'model').get(), 'orderOfActions_arr').get(), e.get('_loc4_')).get())):
                        rt.call_ref(ref(ref(this, 'randUnitOrderArr').get(), 'push'), [ref(ref(this, 'tmpBattleArr').get(), e.get('_loc6_')).get()])
                    assign(e.ref('_loc6_'), '=', lambda: binop('+', e.get('_loc6_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            assign(e.ref('_loc4_'), '=', lambda: binop('+', e.get('_loc4_'), 1))
            assign(e.ref('_loc5_'), '=', lambda: binop('+', e.get('_loc5_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_3 in keys(ref(this, 'randUnitOrderArr').get()):
        e.ref('i').set(key_3)
        rt.tick()
        try:
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'doTR_from_battle'), [ref(ref(this, 'randUnitOrderArr').get(), e.get('i')).get()]))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Battle_createToSpawnUnitsArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc14_', '_loc15_', '_loc16_', '_loc17_', '_loc18_', '_loc19_', '_loc20_', '_loc21_', '_loc22_', '_loc23_', '_loc24_', '_loc25_', '_loc26_', '_loc27_', '_loc28_', '_loc29_', '_loc2_', '_loc30_', '_loc31_', '_loc32_', '_loc33_', '_loc34_', '_loc35_', '_loc36_', '_loc37_', '_loc38_', '_loc39_', '_loc3_', '_loc40_', '_loc41_', '_loc42_', '_loc43_', '_loc44_', '_loc45_', '_loc46_', '_loc47_', '_loc48_', '_loc49_', '_loc4_', '_loc50_', '_loc51_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', 'i', 'j', 'sh'], closure, 'Battle')
    rt.call_ref(ref(this, 'createBattleScriptVars'), [])
    for key_4 in keys(ref(this, 'randUnitOrderArr').get()):
        e.ref('i').set(key_4)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(this, 'randUnitOrderArr').get(), e.get('i')).get())
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), '_player').get()).get())
            assign(e.ref('_loc4_'), '=', lambda: ref(e.get('_loc2_'), '_weapon').get())
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'weaponStock').get(), 'getWeaponByID'), [e.get('_loc4_')]))
            assign(e.ref('_loc6_'), '=', lambda: ref(rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'weaponStock').get(), 'getWeaponByID'), [ref(e.get('_loc2_'), '_payload').get()]), 'explosion_mc_name').get())
            assign(e.ref('_loc7_'), '=', lambda: ref(ref(e.get('_loc3_'), 'startLocation').get(), 0).get())
            assign(e.ref('_loc8_'), '=', lambda: ref(ref(e.get('_loc3_'), 'startLocation').get(), 1).get())
            assign(e.ref('_loc9_'), '=', lambda: rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(e.get('_loc2_'), '_city').get()]))
            assign(e.ref('_loc10_'), '=', lambda: ref(e.get('_loc9_'), 'xPos').get())
            assign(e.ref('_loc11_'), '=', lambda: ref(e.get('_loc9_'), 'yPos').get())
            assign(e.ref('_loc12_'), '=', lambda: rt.construct(e.get('Array'), []))
            assign(e.ref('_loc13_'), '=', lambda: binop('+', 'unit', e.get('i')))
            assign(e.ref('_loc14_'), '=', lambda: binop('+', e.call('Number', [e.get('i')]), 1))
            assign(e.ref('_loc15_'), '=', lambda: rt.construct(e.get('Object'), []))
            if truth(binop('==', ref(e.get('_loc2_'), '_item').get(), 'battle')):
                switch_5 = ref(e.get('_loc5_'), 'weaponName').get()
                case_6 = -1
                if case_6 == -1 and strict_eq(switch_5, 'soldier1'):
                    case_6 = 0
                if case_6 == -1 and strict_eq(switch_5, 'soldier2'):
                    case_6 = 1
                if case_6 == -1 and strict_eq(switch_5, 'soldier3'):
                    case_6 = 2
                if case_6 == -1 and strict_eq(switch_5, 'soldier4'):
                    case_6 = 3
                if case_6 == -1:
                    case_6 = -1
                try:
                    if 0 <= case_6 <= 0:
                        assign(e.ref('_loc16_'), '=', lambda: ref(ref(ref(ref(e.get('_global'), 'model').get(), 'boatStartingPosition').get(), ref(ref(e.get('_loc9_'), 'plr').get(), 'playerNum').get()).get(), 2).get())
                        assign(e.ref('_loc17_'), '=', lambda: ref(ref(ref(ref(e.get('_global'), 'model').get(), 'boatStartingPosition').get(), ref(e.get('_loc2_'), '_player').get()).get(), 2).get())
                        assign(e.ref('_loc18_'), '=', lambda: e.get('_loc17_'))
                        while truth(binop('!=', e.get('_loc18_'), e.get('_loc16_'))):
                            rt.tick()
                            try:
                                rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'boatWayPointPositions').get(), e.get('_loc18_')).get(), 0).get(), '_y': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'boatWayPointPositions').get(), e.get('_loc18_')).get(), 1).get(), '_type': 'default'})])
                                assign(e.ref('_loc18_'), '=', lambda: binop('+', e.get('_loc18_'), 1))
                                if truth(binop('>', e.get('_loc18_'), binop('-', ref(ref(ref(e.get('_global'), 'model').get(), 'boatWayPointPositions').get(), 'length').get(), 1))):
                                    assign(e.ref('_loc18_'), '=', lambda: 0)
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'boatStartingPosition').get(), ref(ref(e.get('_loc9_'), 'plr').get(), 'playerNum').get()).get(), 0).get(), '_y': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'boatStartingPosition').get(), ref(ref(e.get('_loc9_'), 'plr').get(), 'playerNum').get()).get(), 1).get(), '_type': 'unload'})])
                        rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'unitID': e.get('_loc13_'), 'player': ref(e.get('_loc2_'), '_player').get(), 'weaponID': e.get('_loc4_'), 'startX': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'boatStartingPosition').get(), ref(e.get('_loc2_'), '_player').get()).get(), 0).get(), 'startY': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'boatStartingPosition').get(), ref(e.get('_loc2_'), '_player').get()).get(), 1).get(), 'trgtX': e.get('_loc10_'), 'trgtY': e.get('_loc11_'), 'wayPointArr': e.get('_loc12_'), 'result': ref(e.get('_loc2_'), '_result').get(), 'tail': e.get('undefined'), 'tailNum': e.get('undefined'), 'force_MC': 'boat', 'startNum': e.get('_loc14_'), 'tr': e.get('_loc2_'), 'explosion_name': e.get('_loc6_')})])
                        assign(e.ref('_loc19_'), '=', lambda: rt.construct(e.get('Array'), []))
                        assign(e.ref('_loc20_'), '=', lambda: 0)
                        assign(e.ref('_loc21_'), '=', lambda: rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'get_soldier_positions'), [e.get('_loc9_')]))
                        assign(e.ref('_loc11_'), '-=', lambda: 20)
                        for key_7 in keys(ref(ref(e.get('_global'), 'model').get(), 'soldierSpawnArr1').get()):
                            e.ref('j').set(key_7)
                            rt.tick()
                            try:
                                assign(e.ref('_loc19_'), '=', lambda: arr([]))
                                rt.call_ref(ref(e.get('_loc19_'), 'push'), [obj({'_x': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'landUnitsArr').get(), ref(ref(e.get('_loc9_'), 'plr').get(), 'playerNum').get()).get(), 0).get(), '_y': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'landUnitsArr').get(), ref(ref(e.get('_loc9_'), 'plr').get(), 'playerNum').get()).get(), 1).get(), '_type': 'spawn'})])
                                assign(e.ref('_loc22_'), '=', lambda: 0)
                                while truth(binop('<', e.get('_loc22_'), ref(ref(e.get('_loc21_'), '_wpArr').get(), 'length').get())):
                                    rt.tick()
                                    try:
                                        rt.call_ref(ref(e.get('_loc19_'), 'push'), [obj({'_x': ref(ref(ref(e.get('_loc21_'), '_wpArr').get(), e.get('_loc22_')).get(), '_x').get(), '_y': ref(ref(ref(e.get('_loc21_'), '_wpArr').get(), e.get('_loc22_')).get(), '_y').get(), '_type': 'default'})])
                                        assign(e.ref('_loc22_'), '=', lambda: binop('+', e.get('_loc22_'), 1))
                                    except ASContinue:
                                        pass
                                    except ASBreak:
                                        break
                                rt.call_ref(ref(e.get('_loc19_'), 'push'), [obj({'_x': binop('+', binop('+', e.get('_loc10_'), ref(ref(ref(e.get('_loc21_'), '_endPosArr').get(), e.get('_loc20_')).get(), 0).get()), rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [unary('-', 3), 3])), '_y': binop('+', binop('+', e.get('_loc11_'), ref(ref(ref(e.get('_loc21_'), '_endPosArr').get(), e.get('_loc20_')).get(), 1).get()), rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [unary('-', 3), 3])), '_type': 'soldier_reset_range'})])
                                rt.call_ref(ref(e.get('_loc19_'), 'push'), [obj({'_x': e.get('_loc10_'), '_y': e.get('_loc11_'), '_type': 'shoot'})])
                                rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'unitID': binop('+', binop('+', 'tail', e.get('_loc13_')), e.get('j')), 'player': ref(e.get('_loc2_'), '_player').get(), 'weaponID': e.get('_loc4_'), 'startX': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'landUnitsArr').get(), ref(ref(e.get('_loc2_'), 'city').get(), 'playerNum').get()).get(), 0).get(), 'startY': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'landUnitsArr').get(), ref(ref(e.get('_loc2_'), 'city').get(), 'playerNum').get()).get(), 1).get(), 'trgtX': e.get('_loc10_'), 'trgtY': e.get('_loc11_'), 'wayPointArr': e.get('_loc19_'), 'result': ref(e.get('_loc2_'), '_result').get(), 'tail': e.get('_loc13_'), 'tailNum': update(e.ref('_loc20_'), 1, False), 'force_MC': 'soldier', 'startNum': e.get('_loc14_'), 'tr': e.get('_loc2_'), 'explosion_name': e.get('_loc6_')})])
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        raise ASBreak()
                    if 0 <= case_6 <= 1:
                        rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': binop('+', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'marine_landUnitsArr').get(), ref(ref(e.get('_loc9_'), 'plr').get(), 'playerNum').get()).get(), 0).get(), 35), '_y': binop('-', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'marine_landUnitsArr').get(), ref(ref(e.get('_loc9_'), 'plr').get(), 'playerNum').get()).get(), 1).get(), 10), '_type': 'heli_unload'})])
                        rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'unitID': e.get('_loc13_'), 'player': ref(e.get('_loc2_'), '_player').get(), 'weaponID': e.get('_loc4_'), 'startX': 0, 'startY': 0, 'trgtX': e.get('_loc10_'), 'trgtY': e.get('_loc11_'), 'wayPointArr': e.get('_loc12_'), 'result': ref(e.get('_loc2_'), '_result').get(), 'tail': e.get('undefined'), 'tailNum': e.get('undefined'), 'force_MC': 'apache', 'startNum': e.get('_loc14_'), 'tr': e.get('_loc2_'), 'explosion_name': e.get('_loc6_')})])
                        assign(e.ref('_loc23_'), '=', lambda: rt.construct(e.get('Array'), []))
                        assign(e.ref('_loc24_'), '=', lambda: 0)
                        assign(e.ref('_loc25_'), '=', lambda: rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'get_soldier_positions'), [e.get('_loc9_')]))
                        for key_8 in keys(ref(ref(e.get('_global'), 'model').get(), 'soldierSpawnArr1').get()):
                            e.ref('j').set(key_8)
                            rt.tick()
                            try:
                                assign(e.ref('_loc23_'), '=', lambda: arr([]))
                                rt.call_ref(ref(e.get('_loc23_'), 'push'), [obj({'_x': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'marine_landUnitsArr').get(), ref(ref(e.get('_loc9_'), 'plr').get(), 'playerNum').get()).get(), 0).get(), '_y': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'marine_landUnitsArr').get(), ref(ref(e.get('_loc9_'), 'plr').get(), 'playerNum').get()).get(), 1).get(), '_type': 'spawn'})])
                                assign(e.ref('_loc26_'), '=', lambda: 0)
                                while truth(binop('<', e.get('_loc26_'), ref(ref(e.get('_loc25_'), '_wpArr').get(), 'length').get())):
                                    rt.tick()
                                    try:
                                        rt.call_ref(ref(e.get('_loc23_'), 'push'), [obj({'_x': ref(ref(ref(e.get('_loc25_'), '_wpArr').get(), e.get('_loc26_')).get(), '_x').get(), '_y': ref(ref(ref(e.get('_loc25_'), '_wpArr').get(), e.get('_loc26_')).get(), '_y').get(), '_type': 'default'})])
                                        assign(e.ref('_loc26_'), '=', lambda: binop('+', e.get('_loc26_'), 1))
                                    except ASContinue:
                                        pass
                                    except ASBreak:
                                        break
                                rt.call_ref(ref(e.get('_loc23_'), 'push'), [obj({'_x': binop('+', binop('+', e.get('_loc10_'), ref(ref(ref(e.get('_loc25_'), '_endPosArr').get(), e.get('_loc24_')).get(), 0).get()), rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [unary('-', 3), 3])), '_y': binop('+', binop('+', e.get('_loc11_'), ref(ref(ref(e.get('_loc25_'), '_endPosArr').get(), e.get('_loc24_')).get(), 1).get()), rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [unary('-', 3), 3])), '_type': 'soldier_reset_range'})])
                                rt.call_ref(ref(e.get('_loc23_'), 'push'), [obj({'_x': e.get('_loc10_'), '_y': e.get('_loc11_'), '_type': 'shoot'})])
                                rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'unitID': binop('+', 'tail', e.get('_loc13_')), 'player': ref(e.get('_loc2_'), '_player').get(), 'weaponID': e.get('_loc4_'), 'startX': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'landUnitsArr').get(), ref(ref(e.get('_loc2_'), 'city').get(), 'playerNum').get()).get(), 0).get(), 'startY': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'landUnitsArr').get(), ref(ref(e.get('_loc2_'), 'city').get(), 'playerNum').get()).get(), 1).get(), 'trgtX': e.get('_loc10_'), 'trgtY': e.get('_loc11_'), 'wayPointArr': e.get('_loc23_'), 'result': ref(e.get('_loc2_'), '_result').get(), 'tail': e.get('_loc13_'), 'tailNum': update(e.ref('_loc24_'), 1, False), 'force_MC': 'marine', 'startNum': e.get('_loc14_'), 'tr': e.get('_loc2_'), 'explosion_name': e.get('_loc6_')})])
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        raise ASBreak()
                    if 0 <= case_6 <= 2:
                        rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'landUnitsArr').get(), ref(ref(e.get('_loc9_'), 'plr').get(), 'playerNum').get()).get(), 0).get(), '_y': binop('-', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'landUnitsArr').get(), ref(ref(e.get('_loc9_'), 'plr').get(), 'playerNum').get()).get(), 1).get(), 40), '_type': 'drop'})])
                        rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'unitID': e.get('_loc13_'), 'player': ref(e.get('_loc2_'), '_player').get(), 'weaponID': e.get('_loc4_'), 'startX': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'chinookStartPositions').get(), ref(e.get('_loc2_'), '_player').get()).get(), 0).get(), 'startY': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'chinookStartPositions').get(), ref(e.get('_loc2_'), '_player').get()).get(), 1).get(), 'trgtX': e.get('_loc10_'), 'trgtY': e.get('_loc11_'), 'wayPointArr': e.get('_loc12_'), 'result': ref(e.get('_loc2_'), '_result').get(), 'tail': e.get('undefined'), 'tailNum': e.get('undefined'), 'force_MC': 'chinook', 'startNum': e.get('_loc14_'), 'tr': e.get('_loc2_'), 'explosion_name': e.get('_loc6_')})])
                        assign(e.ref('_loc27_'), '=', lambda: rt.construct(e.get('Array'), []))
                        assign(e.ref('_loc28_'), '=', lambda: rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'get_tank_positions'), [e.get('_loc9_')]))
                        assign(e.ref('_loc29_'), '=', lambda: 0)
                        while truth(binop('<', e.get('_loc29_'), ref(ref(e.get('_loc28_'), '_wpArr').get(), 'length').get())):
                            rt.tick()
                            try:
                                if truth(binop('!=', e.get('_loc29_'), binop('-', ref(ref(e.get('_loc28_'), '_wpArr').get(), 'length').get(), 1))):
                                    rt.call_ref(ref(e.get('_loc27_'), 'push'), [obj({'_x': ref(ref(ref(e.get('_loc28_'), '_wpArr').get(), e.get('_loc29_')).get(), '_x').get(), '_y': ref(ref(ref(e.get('_loc28_'), '_wpArr').get(), e.get('_loc29_')).get(), '_y').get(), '_type': 'default'})])
                                else:
                                    rt.call_ref(ref(e.get('_loc27_'), 'push'), [obj({'_x': ref(ref(ref(e.get('_loc28_'), '_wpArr').get(), e.get('_loc29_')).get(), '_x').get(), '_y': ref(ref(ref(e.get('_loc28_'), '_wpArr').get(), e.get('_loc29_')).get(), '_y').get(), '_type': 'tank_reset_range'})])
                                assign(e.ref('_loc29_'), '=', lambda: binop('+', e.get('_loc29_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        assign(e.ref('_loc30_'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [0, 2]))
                        rt.call_ref(ref(e.get('_loc27_'), 'push'), [obj({'_x': binop('+', e.get('_loc10_'), ref(ref(ref(e.get('_loc28_'), '_endPosArr').get(), 0).get(), 0).get()), '_y': binop('+', e.get('_loc11_'), ref(ref(ref(e.get('_loc28_'), '_endPosArr').get(), 0).get(), 1).get()), '_type': 'tank_shoot'})])
                        rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'unitID': binop('+', 'tail', e.get('_loc13_')), 'player': ref(e.get('_loc2_'), '_player').get(), 'weaponID': e.get('_loc4_'), 'startX': binop('-', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'chinookStartPositions').get(), ref(e.get('_loc2_'), '_player').get()).get(), 0).get(), 210), 'startY': binop('-', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'chinookStartPositions').get(), ref(e.get('_loc2_'), '_player').get()).get(), 1).get(), 210), 'trgtX': e.get('_loc10_'), 'trgtY': e.get('_loc11_'), 'wayPointArr': e.get('_loc27_'), 'result': ref(e.get('_loc2_'), '_result').get(), 'tail': e.get('_loc13_'), 'tailNum': 1, 'force_MC': 'tank_noShade', 'startNum': e.get('_loc14_'), 'tr': e.get('_loc2_'), 'explosion_name': e.get('_loc6_')})])
                        assign(e.ref('_loc31_'), '=', lambda: rt.construct(e.get('Array'), []))
                        rt.call_ref(ref(e.get('_loc31_'), 'push'), [obj({'_x': e.get('_loc10_'), '_y': e.get('_loc11_'), '_type': 'tank_shoot'})])
                        rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'unitID': binop('+', binop('+', 'tail', e.get('_loc13_')), 'tail'), 'player': ref(e.get('_loc2_'), '_player').get(), 'weaponID': e.get('_loc4_'), 'startX': binop('-', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'chinookStartPositions').get(), ref(e.get('_loc2_'), '_player').get()).get(), 0).get(), 40), 'startY': binop('-', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'chinookStartPositions').get(), ref(e.get('_loc2_'), '_player').get()).get(), 1).get(), 40), 'trgtX': binop('+', e.get('_loc10_'), ref(ref(ref(e.get('_loc28_'), '_endPosArr').get(), e.get('_loc30_')).get(), 0).get()), 'trgtY': binop('+', e.get('_loc11_'), ref(ref(ref(e.get('_loc28_'), '_endPosArr').get(), e.get('_loc30_')).get(), 1).get()), 'wayPointArr': e.get('_loc31_'), 'result': ref(e.get('_loc2_'), '_result').get(), 'tail': binop('+', 'tail', e.get('_loc13_')), 'tailNum': 2, 'force_MC': 'tankTop', 'startNum': e.get('_loc14_'), 'tr': e.get('_loc2_'), 'explosion_name': e.get('_loc6_')})])
                        raise ASBreak()
                    if 0 <= case_6 <= 3:
                        rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': 0, '_y': 0, '_type': 'suicide_dissapear'})])
                        rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': 0, '_y': 0, '_type': 'suicide_dissapear'})])
                        rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'suicide_spawn_array').get(), ref(e.get('_loc2_'), '_b').get()).get(), 0).get(), '_y': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'suicide_spawn_array').get(), ref(e.get('_loc2_'), '_b').get()).get(), 1).get(), '_type': 'suicide_appear'})])
                        assign(e.ref('_loc32_'), '=', lambda: rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'get_tank_positions'), [e.get('_loc9_')]))
                        assign(e.ref('_loc33_'), '=', lambda: 0)
                        while truth(binop('<', e.get('_loc33_'), ref(ref(e.get('_loc32_'), '_wpArr').get(), 'length').get())):
                            rt.tick()
                            try:
                                if truth(ref(ref(ref(e.get('_loc32_'), '_wpArr').get(), e.get('_loc33_')).get(), '_x').get()):
                                    rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': ref(ref(ref(e.get('_loc32_'), '_wpArr').get(), e.get('_loc33_')).get(), '_x').get(), '_y': ref(ref(ref(e.get('_loc32_'), '_wpArr').get(), e.get('_loc33_')).get(), '_y').get(), '_type': 'default'})])
                                assign(e.ref('_loc33_'), '=', lambda: binop('+', e.get('_loc33_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': e.get('_loc10_'), '_y': e.get('_loc11_'), '_type': 'suicide_explode'})])
                        rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'unitID': e.get('_loc13_'), 'player': ref(e.get('_loc2_'), '_player').get(), 'weaponID': e.get('_loc4_'), 'startX': 0, 'startY': 0, 'trgtX': e.get('_loc10_'), 'trgtY': e.get('_loc11_'), 'wayPointArr': e.get('_loc12_'), 'result': ref(e.get('_loc2_'), '_result').get(), 'tail': e.get('undefined'), 'tailNum': 1, 'force_MC': 'suicide_bomber', 'startNum': e.get('_loc14_'), 'tr': e.get('_loc2_'), 'explosion_name': e.get('_loc6_')})])
                except ASBreak:
                    pass
                switch_9 = ref(e.get('_loc5_'), 'weaponType').get()
                case_10 = -1
                if case_10 == -1 and strict_eq(switch_9, 'rocket'):
                    case_10 = 0
                if case_10 == -1 and strict_eq(switch_9, 'plane'):
                    case_10 = 1
                if case_10 == -1 and strict_eq(switch_9, 'sub'):
                    case_10 = 2
                if case_10 == -1 and strict_eq(switch_9, 'ship'):
                    case_10 = 3
                if case_10 == -1 and strict_eq(switch_9, 'space'):
                    case_10 = 4
                if case_10 == -1 and strict_eq(switch_9, 'spy'):
                    case_10 = 5
                if case_10 == -1:
                    case_10 = -1
                try:
                    if 0 <= case_10 <= 0:
                        assign(e.ref('_loc34_'), '=', lambda: 30)
                        assign(e.ref('_loc35_'), '=', lambda: 30)
                        assign(e.ref('_loc15_'), '=', lambda: rt.construct(e.get('Object'), []))
                        assign(e.ref('_loc36_'), '=', lambda: binop('+', ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), '_player').get()).get(), 'preStart').get(), 0).get(), 10))
                        assign(e.ref('_loc37_'), '=', lambda: binop('-', ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), '_player').get()).get(), 'preStart').get(), 1).get(), 42))
                        assign(ref(e.get('_loc15_'), 'ellipseWidth'), '=', lambda: binop('-', rt.call_ref(ref(e.get('Math'), 'max'), [e.get('_loc36_'), e.get('_loc10_')]), rt.call_ref(ref(e.get('Math'), 'min'), [e.get('_loc36_'), e.get('_loc10_')])))
                        assign(ref(e.get('_loc15_'), 'ellipseHeight'), '=', lambda: 340)
                        assign(ref(e.get('_loc15_'), 'ellipseCenterX'), '=', lambda: binop('+', rt.call_ref(ref(e.get('Math'), 'min'), [e.get('_loc36_'), e.get('_loc10_')]), binop('/', ref(e.get('_loc15_'), 'ellipseWidth').get(), 2)))
                        assign(ref(e.get('_loc15_'), 'ellipseCenterY'), '=', lambda: binop('-', rt.call_ref(ref(e.get('Math'), 'min'), [e.get('_loc11_'), e.get('_loc37_')]), 40))
                        if truth(binop('>', e.get('_loc36_'), e.get('_loc10_'))):
                            assign(ref(e.get('_loc15_'), 'directionMultiplier'), '=', lambda: 1)
                            assign(ref(e.get('_loc15_'), 'startAngle'), '=', lambda: 0)
                        else:
                            assign(ref(e.get('_loc15_'), 'directionMultiplier'), '=', lambda: unary('-', 1))
                            assign(ref(e.get('_loc15_'), 'startAngle'), '=', lambda: 180)
                        if truth(binop('<', e.get('_loc11_'), ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), '_player').get()).get(), 'preStart').get(), 1).get())):
                            assign(e.ref('_loc38_'), '=', lambda: binop('-', e.get('_loc11_'), e.get('_loc34_')))
                        else:
                            assign(e.ref('_loc38_'), '=', lambda: binop('-', ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), '_player').get()).get(), 'preStart').get(), 1).get(), e.get('_loc34_')))
                        if truth(ref(e.get('_loc2_'), '_result').get()):
                            rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': binop('+', ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), '_player').get()).get(), 'preStart').get(), 0).get(), 10), '_y': ref(e.get('_loc15_'), 'ellipseCenterY').get(), '_type': 'rocket_follow_ellipse'})])
                            rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': e.get('_loc10_'), '_y': e.get('_loc11_'), '_type': 'rocket_explode_city'})])
                            if truth(binop('==', ref(e.get('_loc15_'), 'startAngle').get(), 0)):
                                assign(ref(e.get('_loc15_'), 'targetAngle'), '=', lambda: unary('-', 180))
                            else:
                                assign(ref(e.get('_loc15_'), 'targetAngle'), '=', lambda: 360)
                            assign(ref(e.get('_loc15_'), 'finalAction'), '=', lambda: 'rocket_explode_city')
                        else:
                            rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': binop('+', ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), '_player').get()).get(), 'preStart').get(), 0).get(), 10), '_y': ref(e.get('_loc15_'), 'ellipseCenterY').get(), '_type': 'rocket_follow_ellipse_with_anti'})])
                            if truth(binop('==', ref(e.get('_loc15_'), 'startAngle').get(), 0)):
                                assign(ref(e.get('_loc15_'), 'targetAngle'), '=', lambda: unary('-', 180))
                            else:
                                assign(ref(e.get('_loc15_'), 'targetAngle'), '=', lambda: 360)
                            rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': e.get('_loc10_'), '_y': binop('-', e.get('_loc11_'), 100), '_type': 'rocket_explode_self'})])
                            assign(ref(e.get('_loc15_'), 'finalAction'), '=', lambda: 'rocket_explode_self')
                            assign(ref(e.get('_loc15_'), 'anti'), '=', lambda: True)
                            assign(ref(e.get('_loc15_'), 'antiNum'), '=', lambda: ref(e.get('_loc2_'), '_b').get())
                        if truth(ref(e.get('_loc2_'), '_bioload').get()):
                            assign(ref(e.get('_loc15_'), 'bioload'), '=', lambda: True)
                        if truth(ref(e.get('_loc2_'), '_pass_anti').get()):
                            assign(ref(e.get('_loc15_'), 'anti'), '=', lambda: True)
                            assign(ref(e.get('_loc15_'), 'antiNum'), '=', lambda: ref(e.get('_loc2_'), '_b').get())
                        rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'unitID': binop('+', 'unit', e.get('_loc13_')), 'player': ref(e.get('_loc2_'), '_player').get(), 'weaponID': e.get('_loc4_'), 'startX': binop('+', ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), '_player').get()).get(), 'preStart').get(), 0).get(), 10), 'startY': binop('-', ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), '_player').get()).get(), 'preStart').get(), 1).get(), 21), 'trgtX': e.get('_loc10_'), 'trgtY': e.get('_loc11_'), 'wayPointArr': e.get('_loc12_'), 'result': ref(e.get('_loc2_'), '_result').get(), 'tail': e.get('undefined'), 'tailNum': e.get('undefined'), 'force_MC': 'rocket', 'startNum': e.get('_loc14_'), 'targetPlayer': ref(e.get('_loc2_'), '_b').get(), 'tr': e.get('_loc2_'), 'wildCard': e.get('_loc15_'), 'explosion_name': e.get('_loc6_')})])
                        raise ASBreak()
                    if 0 <= case_10 <= 1:
                        assign(e.ref('_loc15_'), '=', lambda: rt.construct(e.get('Object'), []))
                        assign(e.ref('_loc40_'), '=', lambda: rt.construct(e.get('Array'), []))
                        if truth(binop('==', ref(e.get('_loc5_'), 'weaponName').get(), 'plane1')):
                            assign(e.ref('_loc39_'), '=', lambda: 'plane1')
                        else:
                            if truth(binop('==', ref(e.get('_loc5_'), 'weaponName').get(), 'plane2')):
                                assign(e.ref('_loc39_'), '=', lambda: 'plane2')
                        switch_11 = ref(e.get('_loc2_'), '_player').get()
                        case_12 = -1
                        if case_12 == -1 and strict_eq(switch_11, 0):
                            case_12 = 0
                        if case_12 == -1 and strict_eq(switch_11, 1):
                            case_12 = 1
                        if case_12 == -1 and strict_eq(switch_11, 2):
                            case_12 = 2
                        if case_12 == -1 and strict_eq(switch_11, 3):
                            case_12 = 3
                        if case_12 == -1 and strict_eq(switch_11, 4):
                            case_12 = 4
                        if case_12 == -1:
                            case_12 = -1
                        try:
                            if 0 <= case_12 <= 0:
                                assign(ref(e.get('_loc15_'), 'plane_angle_step'), '=', lambda: unary('-', 1))
                                assign(ref(e.get('_loc15_'), 'plane_angle_start'), '=', lambda: 180)
                                assign(ref(e.get('_loc15_'), 'plane_angle_center'), '=', lambda: arr([273, 298]))
                                assign(ref(e.get('_loc15_'), 'circular_modifier_flyTo'), '=', lambda: arr([unary('-', 100), 0]))
                                assign(ref(e.get('_loc15_'), 'circular_modifier_center'), '=', lambda: arr([100, 0]))
                                assign(ref(e.get('_loc15_'), 'circular_radius'), '=', lambda: 100)
                                assign(ref(e.get('_loc15_'), 'x_multiplier'), '=', lambda: 2)
                                assign(ref(e.get('_loc15_'), 'y_multiplier'), '=', lambda: 1)
                                raise ASBreak()
                            if 0 <= case_12 <= 1:
                                assign(ref(e.get('_loc15_'), 'plane_angle_step'), '=', lambda: unary('-', 1))
                                assign(ref(e.get('_loc15_'), 'plane_angle_start'), '=', lambda: 0)
                                assign(ref(e.get('_loc15_'), 'plane_angle_center'), '=', lambda: arr([175, 75]))
                                assign(ref(e.get('_loc15_'), 'circular_modifier_flyTo'), '=', lambda: arr([100, 0]))
                                assign(ref(e.get('_loc15_'), 'circular_modifier_center'), '=', lambda: arr([unary('-', 100), 0]))
                                assign(ref(e.get('_loc15_'), 'x_multiplier'), '=', lambda: 2)
                                assign(ref(e.get('_loc15_'), 'y_multiplier'), '=', lambda: 1)
                                assign(ref(e.get('_loc15_'), 'circular_radius'), '=', lambda: 100)
                                raise ASBreak()
                            if 0 <= case_12 <= 2:
                                assign(ref(e.get('_loc15_'), 'plane_angle_step'), '=', lambda: 1)
                                assign(ref(e.get('_loc15_'), 'plane_angle_start'), '=', lambda: 180)
                                assign(ref(e.get('_loc15_'), 'plane_angle_center'), '=', lambda: arr([619, 100]))
                                assign(ref(e.get('_loc15_'), 'circular_modifier_flyTo'), '=', lambda: arr([unary('-', 100), 0]))
                                assign(ref(e.get('_loc15_'), 'circular_modifier_center'), '=', lambda: arr([100, 0]))
                                assign(ref(e.get('_loc15_'), 'circular_radius'), '=', lambda: 100)
                                raise ASBreak()
                            if 0 <= case_12 <= 3:
                                assign(ref(e.get('_loc15_'), 'plane_angle_step'), '=', lambda: 1)
                                assign(ref(e.get('_loc15_'), 'plane_angle_start'), '=', lambda: 0)
                                assign(ref(e.get('_loc15_'), 'plane_angle_center'), '=', lambda: arr([230, 500]))
                                assign(ref(e.get('_loc15_'), 'circular_modifier_flyTo'), '=', lambda: arr([100, 0]))
                                assign(ref(e.get('_loc15_'), 'circular_modifier_center'), '=', lambda: arr([unary('-', 100), 0]))
                                assign(ref(e.get('_loc15_'), 'x_multiplier'), '=', lambda: 1)
                                assign(ref(e.get('_loc15_'), 'y_multiplier'), '=', lambda: 1)
                                assign(ref(e.get('_loc15_'), 'circular_radius'), '=', lambda: 100)
                                raise ASBreak()
                            if 0 <= case_12 <= 4:
                                assign(ref(e.get('_loc15_'), 'plane_angle_step'), '=', lambda: unary('-', 1))
                                assign(ref(e.get('_loc15_'), 'plane_angle_start'), '=', lambda: 180)
                                assign(ref(e.get('_loc15_'), 'plane_angle_center'), '=', lambda: arr([570, 500]))
                                assign(ref(e.get('_loc15_'), 'circular_modifier_flyTo'), '=', lambda: arr([unary('-', 100), 0]))
                                assign(ref(e.get('_loc15_'), 'circular_modifier_center'), '=', lambda: arr([100, 0]))
                                assign(ref(e.get('_loc15_'), 'circular_radius'), '=', lambda: 100)
                                assign(ref(e.get('_loc15_'), 'x_multiplier'), '=', lambda: 2)
                                assign(ref(e.get('_loc15_'), 'y_multiplier'), '=', lambda: 1)
                        except ASBreak:
                            pass
                        assign(ref(e.get('_loc15_'), 'city'), '=', lambda: ref(e.get('_loc2_'), '_city').get())
                        if truth(ref(e.get('_loc2_'), '_bioload').get()):
                            assign(ref(e.get('_loc15_'), 'bioload'), '=', lambda: True)
                        rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'liftOff_location').get(), ref(e.get('_loc2_'), '_player').get()).get(), 0).get(), '_y': ref(ref(ref(ref(e.get('_global'), 'model').get(), 'liftOff_location').get(), ref(e.get('_loc2_'), '_player').get()).get(), 1).get(), '_type': 'default'})])
                        rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': binop('+', ref(ref(e.get('_loc15_'), 'plane_angle_center').get(), 0).get(), ref(ref(e.get('_loc15_'), 'circular_modifier_flyTo').get(), 0).get()), '_y': binop('+', ref(ref(e.get('_loc15_'), 'plane_angle_center').get(), 1).get(), ref(ref(e.get('_loc15_'), 'circular_modifier_flyTo').get(), 1).get()), '_type': 'plane_circular_flight'})])
                        if truth(ref(e.get('_loc2_'), '_result').get()):
                            assign(e.ref('_loc11_'), '-=', lambda: 100)
                            rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': e.get('_loc10_'), '_y': e.get('_loc11_'), '_type': 'bomb'})])
                        else:
                            rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': e.get('_loc10_'), '_y': e.get('_loc11_'), '_type': 'speedup_die'})])
                            assign(ref(e.get('_loc15_'), 'anti'), '=', lambda: True)
                            assign(ref(e.get('_loc15_'), 'antiNum'), '=', lambda: ref(e.get('_loc2_'), '_b').get())
                        if truth(ref(e.get('_loc2_'), '_pass_anti').get()):
                            assign(ref(e.get('_loc15_'), 'anti'), '=', lambda: True)
                            assign(ref(e.get('_loc15_'), 'antiNum'), '=', lambda: ref(e.get('_loc2_'), '_b').get())
                        rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'unitID': binop('+', 'unit', e.get('_loc13_')), 'player': ref(e.get('_loc2_'), '_player').get(), 'weaponID': e.get('_loc4_'), 'startX': binop('+', ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), '_player').get()).get(), 'preStart').get(), 0).get(), 10), 'startY': binop('-', ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), '_player').get()).get(), 'preStart').get(), 1).get(), 25), 'trgtX': e.get('_loc10_'), 'trgtY': binop('+', e.get('_loc11_'), 100), 'wayPointArr': e.get('_loc12_'), 'result': ref(e.get('_loc2_'), '_result').get(), 'tail': e.get('undefined'), 'tailNum': e.get('undefined'), 'force_MC': e.get('_loc39_'), 'startNum': e.get('_loc14_'), 'targetPlayer': ref(e.get('_loc2_'), '_b').get(), 'tr': e.get('_loc2_'), 'wildCard': e.get('_loc15_'), 'explosion_name': e.get('_loc6_')})])
                        raise ASBreak()
                    if 0 <= case_10 <= 2:
                        if truth(binop('==', ref(e.get('_loc2_'), '_action').get(), 1)):
                            rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'_building': 'sub', '_startNum': e.get('_loc14_'), '_player': ref(e.get('_loc2_'), '_player').get(), '_locPlr': ref(e.get('_loc2_'), '_player').get(), '_locPos': 1, '_frame': 'sub', 'tr': e.get('_loc2_')})])
                        if truth(binop('==', ref(e.get('_loc2_'), '_action').get(), 2)):
                            rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'_building': 'sub', '_player': ref(e.get('_loc2_'), '_player').get(), '_startNum': e.get('_loc14_'), '_locPlr': ref(e.get('_loc2_'), '_b').get(), '_locPos': 2, '_frame': 'sub', '_trgtCity': ref(e.get('_loc2_'), '_city').get(), '_casualties': ref(e.get('_loc2_'), '_casualties').get(), 'tr': e.get('_loc2_'), '_addToSubArr': True})])
                            assign(e.ref('_loc41_'), '=', lambda: 30)
                            assign(e.ref('_loc42_'), '=', lambda: 30)
                            assign(e.ref('_loc15_'), '=', lambda: rt.construct(e.get('Object'), []))
                            assign(ref(e.get('_loc15_'), 'sub_launch_num'), '=', lambda: ref(e.get('_loc2_'), '_player').get())
                            assign(ref(e.get('_loc15_'), 'bioload'), '=', lambda: ref(e.get('_loc2_'), '_bioload').get())
                            assign(e.ref('_loc43_'), '=', lambda: binop('+', ref(ref(ref(ref(e.get('_global'), 'view').get(), 'battleSrcMC').get(), binop('+', binop('+', 'sub_', ref(e.get('_loc2_'), '_b').get()), '_2')).get(), '_x').get(), 21))
                            assign(e.ref('_loc44_'), '=', lambda: binop('+', ref(ref(ref(ref(e.get('_global'), 'view').get(), 'battleSrcMC').get(), binop('+', binop('+', 'sub_', ref(e.get('_loc2_'), '_b').get()), '_2')).get(), '_y').get(), 55))
                            assign(ref(e.get('_loc15_'), 'ellipseWidth'), '=', lambda: binop('-', rt.call_ref(ref(e.get('Math'), 'max'), [e.get('_loc43_'), e.get('_loc10_')]), rt.call_ref(ref(e.get('Math'), 'min'), [e.get('_loc43_'), e.get('_loc10_')])))
                            assign(ref(e.get('_loc15_'), 'ellipseHeight'), '=', lambda: 340)
                            assign(ref(e.get('_loc15_'), 'ellipseCenterX'), '=', lambda: binop('+', rt.call_ref(ref(e.get('Math'), 'min'), [e.get('_loc43_'), e.get('_loc10_')]), binop('/', ref(e.get('_loc15_'), 'ellipseWidth').get(), 2)))
                            assign(ref(e.get('_loc15_'), 'ellipseCenterY'), '=', lambda: binop('-', rt.call_ref(ref(e.get('Math'), 'min'), [e.get('_loc11_'), e.get('_loc44_')]), 40))
                            if truth(binop('>', e.get('_loc43_'), e.get('_loc10_'))):
                                assign(ref(e.get('_loc15_'), 'directionMultiplier'), '=', lambda: 1)
                                assign(ref(e.get('_loc15_'), 'startAngle'), '=', lambda: 0)
                            else:
                                assign(ref(e.get('_loc15_'), 'directionMultiplier'), '=', lambda: unary('-', 1))
                                assign(ref(e.get('_loc15_'), 'startAngle'), '=', lambda: 180)
                            if truth(binop('<', e.get('_loc11_'), e.get('_loc44_'))):
                                assign(e.ref('_loc45_'), '=', lambda: binop('-', e.get('_loc11_'), e.get('_loc41_')))
                            else:
                                assign(e.ref('_loc45_'), '=', lambda: binop('-', e.get('_loc44_'), e.get('_loc41_')))
                            rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': e.get('_loc43_'), '_y': ref(e.get('_loc15_'), 'ellipseCenterY').get(), '_type': 'rocket_follow_ellipse'})])
                            if truth(binop('==', ref(e.get('_loc15_'), 'startAngle').get(), 0)):
                                assign(ref(e.get('_loc15_'), 'targetAngle'), '=', lambda: unary('-', 180))
                            else:
                                assign(ref(e.get('_loc15_'), 'targetAngle'), '=', lambda: 360)
                            rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': e.get('_loc10_'), '_y': e.get('_loc11_'), '_type': 'rocket_explode_city_from_sub'})])
                            assign(ref(e.get('_loc15_'), 'finalAction'), '=', lambda: 'rocket_explode_city_from_sub')
                            rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'unitID': binop('+', 'unit', e.get('_loc13_')), 'player': ref(e.get('_loc2_'), '_player').get(), 'weaponID': e.get('_loc4_'), 'startX': e.get('_loc43_'), 'startY': e.get('_loc44_'), 'trgtX': e.get('_loc10_'), 'trgtY': e.get('_loc11_'), 'wayPointArr': e.get('_loc12_'), 'result': ref(e.get('_loc2_'), '_result').get(), 'tail': e.get('undefined'), 'tailNum': e.get('undefined'), 'force_MC': 'sub_rocket', 'startNum': e.get('_loc14_'), 'targetPlayer': ref(e.get('_loc2_'), '_b').get(), 'tr': e.get('_loc2_'), 'wildCard': e.get('_loc15_'), 'explosion_name': e.get('_loc6_'), '_casualties': ref(e.get('_loc2_'), '_casualties').get()})])
                        raise ASBreak()
                    if 0 <= case_10 <= 3:
                        if truth(binop('!=', ref(e.get('_loc2_'), '_action').get(), 1)):
                            if truth(binop('==', ref(e.get('_loc2_'), '_action').get(), 2)):
                                assign(e.ref('_loc46_'), '=', lambda: 0)
                                for key_13 in keys(ref(e.get('_loc2_'), '_attack_arr').get()):
                                    e.ref('sh').set(key_13)
                                    rt.tick()
                                    try:
                                        assign(e.ref('_loc12_'), '=', lambda: arr([]))
                                        assign(e.ref('_loc6_'), '=', lambda: ref(rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'weaponStock').get(), 'getWeaponByID'), [ref(ref(ref(e.get('_loc2_'), '_attack_arr').get(), e.get('sh')).get(), 'wpn').get()]), 'explosion_mc_name').get())
                                        assign(e.ref('_loc15_'), '=', lambda: rt.construct(e.get('Object'), []))
                                        assign(ref(e.get('_loc15_'), '_number'), '=', lambda: e.call('Number', [e.get('sh')]))
                                        assign(ref(e.get('_loc15_'), '_city'), '=', lambda: ref(ref(ref(e.get('_loc2_'), '_attack_arr').get(), e.get('sh')).get(), 'city').get())
                                        assign(ref(e.get('_loc15_'), '_casualties'), '=', lambda: ref(ref(ref(e.get('_loc2_'), '_result_arr').get(), e.get('sh')).get(), '_casualties').get())
                                        if truth(ref(ref(ref(e.get('_loc2_'), '_attack_arr').get(), e.get('sh')).get(), '_bioload').get()):
                                            assign(ref(e.get('_loc15_'), 'bioload'), '=', lambda: True)
                                            assign(ref(e.get('_loc15_'), 'city'), '=', lambda: ref(ref(ref(e.get('_loc2_'), '_attack_arr').get(), e.get('sh')).get(), 'city').get())
                                        rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': binop('-', ref(ref(ref(ref(e.get('_global'), 'view').get(), 'battleSrcMC').get(), binop('+', 'carrier', ref(e.get('_loc2_'), '_player').get())).get(), '_x').get(), 112), '_y': binop('+', ref(ref(ref(ref(e.get('_global'), 'view').get(), 'battleSrcMC').get(), binop('+', 'carrier', ref(e.get('_loc2_'), '_player').get())).get(), '_y').get(), 54), '_type': 'default'})])
                                        assign(e.ref('_loc47_'), '=', lambda: binop('+', ref(ref(ref(ref(e.get('_global'), 'view').get(), 'battleSrcMC').get(), binop('+', 'carrier', ref(e.get('_loc2_'), '_player').get())).get(), '_y').get(), 54))
                                        assign(e.ref('_loc48_'), '=', lambda: ref(rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(ref(e.get('_loc2_'), '_attack_arr').get(), e.get('sh')).get(), 'city').get()]), 'yPos').get())
                                        assign(e.ref('_loc49_'), '=', lambda: binop('-', ref(ref(ref(ref(e.get('_global'), 'view').get(), 'battleSrcMC').get(), binop('+', 'carrier', ref(e.get('_loc2_'), '_player').get())).get(), '_x').get(), 112))
                                        assign(e.ref('_loc50_'), '=', lambda: ref(rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(ref(e.get('_loc2_'), '_attack_arr').get(), e.get('sh')).get(), 'city').get()]), 'xPos').get())
                                        if truth(logical('&&', binop('<=', binop('-', rt.call_ref(ref(e.get('Math'), 'max'), [e.get('_loc47_'), e.get('_loc48_')]), rt.call_ref(ref(e.get('Math'), 'min'), [e.get('_loc47_'), e.get('_loc48_')])), 200), lambda: binop('>', e.get('_loc50_'), e.get('_loc49_')))):
                                            assign(e.ref('_loc51_'), '=', lambda: ref(rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(ref(e.get('_loc2_'), '_attack_arr').get(), e.get('sh')).get(), 'city').get()]), 'yPos').get())
                                            if truth(binop('<', e.get('_loc47_'), e.get('_loc48_'))):
                                                assign(e.ref('_loc51_'), '+=', lambda: 150)
                                            else:
                                                assign(e.ref('_loc51_'), '-=', lambda: 150)
                                            rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': binop('-', ref(ref(ref(ref(e.get('_global'), 'view').get(), 'battleSrcMC').get(), binop('+', 'carrier', ref(e.get('_loc2_'), '_player').get())).get(), '_x').get(), 112), '_y': e.get('_loc51_'), '_type': 'default'})])
                                        if truth(ref(ref(ref(e.get('_loc2_'), '_result_arr').get(), e.call('Number', [e.get('sh')])).get(), '_result').get()):
                                            rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': ref(rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(ref(e.get('_loc2_'), '_attack_arr').get(), e.get('sh')).get(), 'city').get()]), 'xPos').get(), '_y': binop('-', ref(rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(ref(e.get('_loc2_'), '_attack_arr').get(), e.get('sh')).get(), 'city').get()]), 'yPos').get(), 100), '_type': 'ship_plane_bomb'})])
                                        else:
                                            assign(ref(e.get('_loc15_'), 'anti'), '=', lambda: True)
                                            assign(ref(e.get('_loc15_'), 'antiNum'), '=', lambda: ref(e.get('_loc2_'), '_b').get())
                                            rt.call_ref(ref(e.get('_loc12_'), 'push'), [obj({'_x': ref(rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(ref(e.get('_loc2_'), '_attack_arr').get(), e.get('sh')).get(), 'city').get()]), 'xPos').get(), '_y': binop('-', ref(rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(ref(e.get('_loc2_'), '_attack_arr').get(), e.get('sh')).get(), 'city').get()]), 'yPos').get(), 100), '_type': 'explode'})])
                                        rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'unitID': binop('+', 'unit_ship', e.call('Number', [e.get('sh')])), 'player': ref(e.get('_loc2_'), '_player').get(), 'weaponID': e.get('_loc4_'), 'startX': binop('+', ref(ref(ref(ref(e.get('_global'), 'view').get(), 'battleSrcMC').get(), binop('+', 'carrier', ref(e.get('_loc2_'), '_player').get())).get(), '_x').get(), ref(ref(ref(ref(e.get('_global'), 'model').get(), 'ship_plane_start_arr').get(), e.get('_loc46_')).get(), 0).get()), 'startY': binop('+', ref(ref(ref(ref(e.get('_global'), 'view').get(), 'battleSrcMC').get(), binop('+', 'carrier', ref(e.get('_loc2_'), '_player').get())).get(), '_y').get(), ref(ref(ref(ref(e.get('_global'), 'model').get(), 'ship_plane_start_arr').get(), e.get('_loc46_')).get(), 1).get()), 'trgtX': ref(rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(ref(e.get('_loc2_'), '_attack_arr').get(), e.get('sh')).get(), 'city').get()]), 'xPos').get(), 'trgtY': ref(rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(ref(e.get('_loc2_'), '_attack_arr').get(), e.get('sh')).get(), 'city').get()]), 'yPos').get(), 'wayPointArr': e.get('_loc12_'), 'result': ref(e.get('_loc2_'), '_result').get(), 'tail': e.get('undefined'), 'tailNum': e.get('undefined'), 'force_MC': 'ship_plane', 'startNum': e.get('_loc14_'), 'targetPlayer': ref(e.get('_loc2_'), '_b').get(), 'tr': e.get('_loc2_'), 'wildCard': e.get('_loc15_'), 'explosion_name': e.get('_loc6_')})])
                                        assign(e.ref('_loc46_'), '=', lambda: binop('+', e.get('_loc46_'), 1))
                                    except ASContinue:
                                        pass
                                    except ASBreak:
                                        break
                        raise ASBreak()
                    if 0 <= case_10 <= 4:
                        assign(e.ref('_loc15_'), '=', lambda: rt.construct(e.get('Object'), []))
                        assign(ref(e.get('_loc15_'), 'targetX'), '=', lambda: ref(ref(ref(ref(e.get('_global'), 'model').get(), 'satellite_pos_arr').get(), ref(e.get('_loc2_'), '_player').get()).get(), '_x').get())
                        assign(ref(e.get('_loc15_'), 'targetY'), '=', lambda: ref(ref(ref(ref(e.get('_global'), 'model').get(), 'satellite_pos_arr').get(), ref(e.get('_loc2_'), '_player').get()).get(), '_y').get())
                        assign(ref(e.get('_loc15_'), 'satellite'), '=', lambda: True)
                        assign(ref(e.get('_loc15_'), 'cityX'), '=', lambda: e.get('_loc10_'))
                        assign(ref(e.get('_loc15_'), 'cityY'), '=', lambda: e.get('_loc11_'))
                        assign(ref(e.get('_loc15_'), 'satelliteFrame'), '=', lambda: ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), '_player').get()).get(), 'religion_code').get())
                        assign(ref(e.get('_loc15_'), 'laser_hex_color'), '=', lambda: ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), '_player').get()).get(), 'hexColorTint_str').get())
                        rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'unitID': binop('+', 'satellite', e.get('_loc13_')), 'player': ref(e.get('_loc2_'), '_player').get(), 'weaponID': e.get('_loc4_'), 'startX': unary('-', 120), 'startY': ref(ref(ref(e.get('_global'), 'model').get(), 'satellite_height_arr').get(), ref(e.get('_loc2_'), '_player').get()).get(), 'result': ref(e.get('_loc2_'), '_result').get(), 'tail': e.get('undefined'), 'tailNum': e.get('undefined'), 'startNum': e.get('_loc14_'), 'targetPlayer': ref(e.get('_loc2_'), '_b').get(), 'tr': e.get('_loc2_'), 'wildCard': e.get('_loc15_'), 'explosion_name': e.get('_loc6_')})])
                        raise ASBreak()
                    if 0 <= case_10 <= 5:
                        rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'_building': ref(e.get('_loc2_'), '_frame').get(), '_startNum': e.get('_loc14_'), '_player': ref(e.get('_loc2_'), '_player').get(), '_frame': ref(e.get('_loc2_'), '_frame').get(), 'tr': e.get('_loc2_')})])
                except ASBreak:
                    pass
            else:
                switch_14 = ref(e.get('_loc2_'), '_item').get()
                case_15 = -1
                if case_15 == -1 and strict_eq(switch_14, 'diplomacy'):
                    case_15 = 0
                if case_15 == -1 and strict_eq(switch_14, 'propaganda'):
                    case_15 = 1
                if case_15 == -1 and strict_eq(switch_14, 'resources'):
                    case_15 = 2
                if case_15 == -1 and strict_eq(switch_14, 'religion'):
                    case_15 = 3
                if case_15 == -1 and strict_eq(switch_14, 'produce'):
                    case_15 = 4
                if case_15 == -1:
                    case_15 = -1
                try:
                    if 0 <= case_15 <= 0:
                        rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'_building': 'diplomacy', '_startNum': e.get('_loc14_'), '_player': ref(e.get('_loc2_'), '_player').get(), '_frame': 'diplomacy', 'tr': e.get('_loc2_')})])
                        raise ASBreak()
                    if 0 <= case_15 <= 1:
                        rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'_building': 'propaganda_2', '_startNum': e.get('_loc14_'), '_player': ref(e.get('_loc2_'), '_player').get(), '_frame': 'propaganda_2', '_targetCity_id': ref(e.get('_loc2_'), '_city').get(), 'tr': e.get('_loc2_')})])
                        raise ASBreak()
                    if 0 <= case_15 <= 2:
                        rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'_building': 'resources', '_startNum': e.get('_loc14_'), '_player': ref(e.get('_loc2_'), '_player').get(), '_frame': 'resources', 'tr': e.get('_loc2_')})])
                        raise ASBreak()
                    if 0 <= case_15 <= 3:
                        rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'_building': 'religion', '_startNum': e.get('_loc14_'), '_player': ref(e.get('_loc2_'), '_player').get(), '_frame': 'religion', 'tr': e.get('_loc2_')})])
                        raise ASBreak()
                    if 0 <= case_15 <= 4:
                        rt.call_ref(ref(ref(this, '_toSpawnUnitsArr').get(), 'push'), [obj({'_building': 'produce', '_startNum': e.get('_loc14_'), '_player': ref(e.get('_loc2_'), '_player').get(), '_frame': 'produce', 'tr': e.get('_loc2_')})])
                except ASBreak:
                    pass
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Battle_createToShowABArray(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc14_', '_loc15_', '_loc16_', '_loc17_', '_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', 'k'], closure, 'Battle')
    e.set('_loc2_', 0)
    e.set('_loc3_', 0)
    while truth(binop('<=', e.get('_loc3_'), 1)):
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'turnResultsArr').get(), e.get('_loc2_')).get())
            assign(e.ref('_loc5_'), '=', lambda: '')
            assign(e.ref('_loc6_'), '=', lambda: ref(e.get('_loc4_'), '_weapon').get())
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'weaponStock').get(), 'getWeaponByID'), [e.get('_loc6_')]))
            assign(e.ref('_loc8_'), '=', lambda: '')
            assign(e.ref('_loc9_'), '=', lambda: False)
            assign(e.ref('_loc10_'), '=', lambda: False)
            assign(e.ref('_loc11_'), '=', lambda: False)
            assign(e.ref('_loc12_'), '=', lambda: False)
            assign(e.ref('_loc13_'), '=', lambda: arr([False]))
            if truth(logical('&&', binop('==', e.get('_loc3_'), 0), lambda: ref(e.get('_loc4_'), '_item').get())):
                assign(e.ref('_loc11_'), '=', lambda: True)
                switch_16 = ref(e.get('_loc4_'), '_item').get()
                case_17 = -1
                if case_17 == -1 and strict_eq(switch_16, 'battle'):
                    case_17 = 0
                if case_17 == -1 and strict_eq(switch_16, 'setPreAttack'):
                    case_17 = 1
                if case_17 == -1:
                    case_17 = 2
                try:
                    if 0 <= case_17 <= 0:
                        assign(e.ref('_loc8_'), '=', lambda: 'init')
                        switch_18 = ref(e.get('_loc7_'), 'weaponName').get()
                        case_19 = -1
                        if case_19 == -1 and strict_eq(switch_18, 'soldier1'):
                            case_19 = 0
                        if case_19 == -1 and strict_eq(switch_18, 'soldier2'):
                            case_19 = 1
                        if case_19 == -1 and strict_eq(switch_18, 'soldier3'):
                            case_19 = 2
                        if case_19 == -1 and strict_eq(switch_18, 'soldier4'):
                            case_19 = 3
                        if case_19 == -1:
                            case_19 = -1
                        try:
                            if 0 <= case_19 <= 0:
                                assign(e.ref('_loc5_'), '=', lambda: 'base')
                                raise ASBreak()
                            if 0 <= case_19 <= 1:
                                assign(e.ref('_loc5_'), '=', lambda: 'helipad')
                                assign(e.ref('_loc10_'), '=', lambda: True)
                                raise ASBreak()
                            if 0 <= case_19 <= 2:
                                assign(e.ref('_loc5_'), '=', lambda: 'helipad')
                                assign(e.ref('_loc10_'), '=', lambda: True)
                                raise ASBreak()
                            if 0 <= case_19 <= 3:
                                assign(e.ref('_loc5_'), '=', lambda: 'hatch')
                                assign(e.ref('_loc10_'), '=', lambda: True)
                        except ASBreak:
                            pass
                        switch_20 = ref(e.get('_loc7_'), 'weaponType').get()
                        case_21 = -1
                        if case_21 == -1 and strict_eq(switch_20, 'plane'):
                            case_21 = 0
                        if case_21 == -1 and strict_eq(switch_20, 'rocket'):
                            case_21 = 1
                        if case_21 == -1 and strict_eq(switch_20, 'ship'):
                            case_21 = 2
                        if case_21 == -1 and strict_eq(switch_20, 'sub'):
                            case_21 = 3
                        if case_21 == -1 and strict_eq(switch_20, 'space'):
                            case_21 = 4
                        if case_21 == -1:
                            case_21 = -1
                        try:
                            if 0 <= case_21 <= 0:
                                assign(e.ref('_loc9_'), '=', lambda: True)
                                assign(e.ref('_loc5_'), '=', lambda: 'airfield')
                                assign(e.ref('_loc12_'), '=', lambda: True)
                                raise ASBreak()
                            if 0 <= case_21 <= 1:
                                assign(e.ref('_loc9_'), '=', lambda: True)
                                assign(e.ref('_loc5_'), '=', lambda: 'silo')
                                assign(e.ref('_loc12_'), '=', lambda: True)
                                raise ASBreak()
                            if 0 <= case_21 <= 2:
                                if truth(unary('!', ref(e.get('_loc4_'), '_dontBeAnAss').get())):
                                    assign(e.ref('_loc5_'), '=', lambda: 'ship')
                                    assign(e.ref('_loc9_'), '=', lambda: True)
                                    assign(e.ref('_loc12_'), '=', lambda: True)
                                else:
                                    e.get('_loc8_')
                                raise ASBreak()
                            if 0 <= case_21 <= 3:
                                assign(e.ref('_loc5_'), '=', lambda: 'sub')
                                assign(e.ref('_loc12_'), '=', lambda: False)
                                raise ASBreak()
                            if 0 <= case_21 <= 4:
                                assign(e.ref('_loc5_'), '=', lambda: 'space')
                                assign(e.ref('_loc12_'), '=', lambda: True)
                        except ASBreak:
                            pass
                        raise ASBreak()
                    if 0 <= case_17 <= 1:
                        if truth(binop('==', ref(e.get('_loc4_'), '_value').get(), 'ready')):
                            assign(e.ref('_loc9_'), '=', lambda: True)
                            assign(e.ref('_loc8_'), '=', lambda: 'last')
                            assign(e.ref('_loc5_'), '=', lambda: ref(e.get('_loc4_'), '_frame').get())
                        else:
                            e.get('_loc5_')
                            e.get('_loc8_')
                        raise ASBreak()
                    if 0 <= case_17 <= 2:
                        assign(e.ref('_loc11_'), '=', lambda: False)
                except ASBreak:
                    pass
            else:
                if truth(logical('&&', binop('==', e.get('_loc3_'), 1), lambda: ref(e.get('_loc4_'), '_item').get())):
                    assign(e.ref('_loc11_'), '=', lambda: True)
                    switch_22 = ref(e.get('_loc4_'), '_item').get()
                    case_23 = -1
                    if case_23 == -1 and strict_eq(switch_22, 'production_building'):
                        case_23 = 0
                    if case_23 == -1 and strict_eq(switch_22, 'research_building'):
                        case_23 = 1
                    if case_23 == -1 and strict_eq(switch_22, 'defense'):
                        case_23 = 2
                    if case_23 == -1 and strict_eq(switch_22, 'diplomacy'):
                        case_23 = 3
                    if case_23 == -1 and strict_eq(switch_22, 'propaganda'):
                        case_23 = 4
                    if case_23 == -1 and strict_eq(switch_22, 'regard'):
                        case_23 = 5
                    if case_23 == -1 and strict_eq(switch_22, 'bioload'):
                        case_23 = 6
                    if case_23 == -1:
                        case_23 = 7
                    try:
                        if 0 <= case_23 <= 0:
                            assign(e.ref('_loc8_'), '=', lambda: 'last')
                            assign(e.ref('_loc5_'), '=', lambda: 'factory')
                            raise ASBreak()
                        if 0 <= case_23 <= 1:
                            assign(e.ref('_loc8_'), '=', lambda: 'last')
                            assign(e.ref('_loc5_'), '=', lambda: 'tech')
                            raise ASBreak()
                        if 0 <= case_23 <= 2:
                            assign(e.ref('_loc8_'), '=', lambda: 'last')
                            if truth(ref(e.get('_loc4_'), '_result').get()):
                                if truth(binop('==', ref(rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'weaponStock').get(), 'getWeaponByID'), [ref(e.get('_loc4_'), '_value').get()]), 'weaponName').get(), 'antiAir')):
                                    assign(e.ref('_loc13_'), '=', lambda: arr([True, 'air']))
                                    assign(e.ref('_loc5_'), '=', lambda: 'antiAir_fire')
                                else:
                                    assign(e.ref('_loc13_'), '=', lambda: arr([True, 'rocket']))
                                    assign(e.ref('_loc5_'), '=', lambda: 'antiRocket_fire')
                            else:
                                assign(e.ref('_loc8_'), '=', lambda: 'last')
                                assign(e.ref('_loc5_'), '=', lambda: binop('+', ref(e.get('_loc4_'), '_frame').get(), '_still'))
                            raise ASBreak()
                        if 0 <= case_23 <= 3:
                            assign(e.ref('_loc8_'), '=', lambda: 'inBattle')
                            assign(e.ref('_loc5_'), '=', lambda: 'diplomacy')
                            raise ASBreak()
                        if 0 <= case_23 <= 4:
                            assign(e.ref('_loc8_'), '=', lambda: 'inBattle')
                            assign(e.ref('_loc5_'), '=', lambda: 'propaganda')
                            assign(e.ref('_loc14_'), '=', lambda: ref(e.get('_loc4_'), '_city').get())
                            assign(e.ref('_loc15_'), '=', lambda: ref(e.get('_loc4_'), '_player').get())
                            raise ASBreak()
                        if 0 <= case_23 <= 5:
                            e.get('_loc8_')
                            raise ASBreak()
                        if 0 <= case_23 <= 6:
                            e.get('_loc8_')
                            raise ASBreak()
                        if 0 <= case_23 <= 7:
                            assign(e.ref('_loc11_'), '=', lambda: False)
                    except ASBreak:
                        pass
            if truth(logical('&&', e.get('_loc11_'), lambda: unary('!', ref(e.get('_loc4_'), '_spyArr').get()))):
                switch_24 = e.get('_loc8_')
                case_25 = -1
                if case_25 == -1 and strict_eq(switch_24, 'timed'):
                    case_25 = 0
                if case_25 == -1 and strict_eq(switch_24, 'init'):
                    case_25 = 1
                if case_25 == -1 and strict_eq(switch_24, 'inBattle'):
                    case_25 = 2
                if case_25 == -1 and strict_eq(switch_24, 'last'):
                    case_25 = 3
                if case_25 == -1:
                    case_25 = -1
                try:
                    if 0 <= case_25 <= 0:
                        rt.call_ref(ref(ref(this, '_toShowTimedABArr').get(), 'push'), [obj({'_player': ref(e.get('_loc4_'), '_player').get(), '_frame': e.get('_loc5_'), '_setPreStart': e.get('_loc9_'), '_setHeliStart': e.get('_loc10_'), '_anti_arr': e.get('_loc13_'), '_value1': e.get('_loc14_'), '_value2': e.get('_loc15_'), '_building': True})])
                        raise ASBreak()
                    if 0 <= case_25 <= 1:
                        assign(e.ref('_loc16_'), '=', lambda: True)
                        for key_26 in keys(ref(this, '_toShowInitABArr').get()):
                            e.ref('k').set(key_26)
                            rt.tick()
                            try:
                                if truth(logical('&&', binop('==', e.get('_loc5_'), ref(ref(ref(this, '_toShowInitABArr').get(), e.get('k')).get(), '_frame').get()), lambda: binop('==', ref(e.get('_loc4_'), '_player').get(), ref(ref(ref(this, '_toShowInitABArr').get(), e.get('k')).get(), '_player').get()))):
                                    assign(e.ref('_loc16_'), '=', lambda: False)
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        if truth(e.get('_loc16_')):
                            rt.call_ref(ref(ref(this, '_toShowInitABArr').get(), 'push'), [obj({'_player': ref(e.get('_loc4_'), '_player').get(), '_frame': e.get('_loc5_'), '_setPreStart': e.get('_loc9_'), '_fixedLoc': e.get('_loc12_'), '_setHeliStart': e.get('_loc10_'), '_anti_arr': e.get('_loc13_'), '_value1': e.get('_loc14_'), '_value2': e.get('_loc15_'), '_building': True})])
                        raise ASBreak()
                    if 0 <= case_25 <= 2:
                        rt.call_ref(ref(ref(this, '_toShowInBattleABArr').get(), 'push'), [obj({'_player': ref(e.get('_loc4_'), '_player').get(), '_frame': e.get('_loc5_'), '_setPreStart': e.get('_loc9_'), '_setHeliStart': e.get('_loc10_'), '_anti_arr': e.get('_loc13_'), '_value1': e.get('_loc14_'), '_value2': e.get('_loc15_'), '_building': True})])
                        raise ASBreak()
                    if 0 <= case_25 <= 3:
                        assign(e.ref('_loc17_'), '=', lambda: True)
                        for key_27 in keys(ref(this, '_toShowLastABArr').get()):
                            e.ref('k').set(key_27)
                            rt.tick()
                            try:
                                if truth(logical('&&', binop('==', e.get('_loc5_'), ref(ref(ref(this, '_toShowLastABArr').get(), e.get('k')).get(), '_frame').get()), lambda: binop('==', ref(e.get('_loc4_'), '_player').get(), ref(ref(ref(this, '_toShowLastABArr').get(), e.get('k')).get(), '_player').get()))):
                                    assign(e.ref('_loc17_'), '=', lambda: False)
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        if truth(e.get('_loc17_')):
                            rt.call_ref(ref(ref(this, '_toShowLastABArr').get(), 'push'), [obj({'_player': ref(e.get('_loc4_'), '_player').get(), '_frame': e.get('_loc5_'), '_setPreStart': e.get('_loc9_'), '_setHeliStart': e.get('_loc10_'), '_anti_arr': e.get('_loc13_'), '_value1': e.get('_loc14_'), '_value2': e.get('_loc15_'), '_building': True})])
                except ASBreak:
                    pass
            if truth(binop('<', e.get('_loc2_'), binop('-', ref(ref(ref(e.get('_global'), 'model').get(), 'turnResultsArr').get(), 'length').get(), 1))):
                assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
            else:
                assign(e.ref('_loc2_'), '=', lambda: 0)
                assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Battle___get__all_turn_buildings_arr(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i', 'j', 'k', 'l', 'm', 'n'], closure, 'Battle')
    e.set('_loc2_', rt.construct(e.get('Array'), []))
    for key_28 in keys(ref(this, '_toShowInitABArr').get()):
        e.ref('k').set(key_28)
        rt.tick()
        try:
            rt.call_ref(ref(e.get('_loc2_'), 'push'), [ref(ref(this, '_toShowInitABArr').get(), e.get('k')).get()])
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_29 in keys(ref(this, '_toShowLastABArr').get()):
        e.ref('i').set(key_29)
        rt.tick()
        try:
            rt.call_ref(ref(e.get('_loc2_'), 'push'), [ref(ref(this, '_toShowLastABArr').get(), e.get('i')).get()])
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_30 in keys(ref(this, '_toShowTimedABArr').get()):
        e.ref('j').set(key_30)
        rt.tick()
        try:
            rt.call_ref(ref(e.get('_loc2_'), 'push'), [ref(ref(this, '_toShowTimedABArr').get(), e.get('j')).get()])
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_31 in keys(ref(this, '_toShowInBattleABArr').get()):
        e.ref('l').set(key_31)
        rt.tick()
        try:
            rt.call_ref(ref(e.get('_loc2_'), 'push'), [ref(ref(this, '_toShowInBattleABArr').get(), e.get('l')).get()])
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_32 in keys(ref(this, '_toSpawnUnitsArr').get()):
        e.ref('m').set(key_32)
        rt.tick()
        try:
            if truth(ref(ref(ref(this, '_toSpawnUnitsArr').get(), e.get('m')).get(), '_building').get()):
                rt.call_ref(ref(e.get('_loc2_'), 'push'), [ref(ref(this, '_toSpawnUnitsArr').get(), e.get('m')).get()])
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_33 in keys(e.get('_loc2_')):
        e.ref('n').set(key_33)
        rt.tick()
        try:
            pass
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc2_')
    return U

def Battle___get__curLastAB(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Battle')
    if truth(binop('!=', ref(ref(this, '_toShowLastABArr').get(), 'length').get(), 0)):
        return rt.call_ref(ref(ref(this, '_toShowLastABArr').get(), 'shift'), [])
    return obj({'_empty': True})
    return U

def Battle___get__toShowTimedABArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Battle')
    if truth(binop('!=', ref(ref(this, '_toShowTimedABArr').get(), 'length').get(), 0)):
        return rt.call_ref(ref(ref(this, '_toShowTimedABArr').get(), 'shift'), [])
    return obj({'_empty': True})
    return U

def Battle___get__toShowInitABArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Battle')
    if truth(binop('!=', ref(ref(this, '_toShowInitABArr').get(), 'length').get(), 0)):
        return rt.call_ref(ref(ref(this, '_toShowInitABArr').get(), 'shift'), [])
    return obj({'_empty': True})
    return U

def Battle___get__toShowInBattleABArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Battle')
    if truth(binop('!=', ref(ref(this, '_toShowInBattleABArr').get(), 'length').get(), 0)):
        return rt.call_ref(ref(ref(this, '_toShowInBattleABArr').get(), 'shift'), [])
    return obj({'_empty': True})
    return U

def Battle___get__toShowLastABArr(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Battle')
    if truth(binop('!=', ref(ref(this, '_toShowLastABArr').get(), 'length').get(), 0)):
        return rt.call_ref(ref(ref(this, '_toShowLastABArr').get(), 'shift'), [])
    return obj({'_empty': True})
    return U

def Battle___set__curAB(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'Battle')
    return U

def Battle_getLiftOffPos(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['startPos', 'weaponType', 'playerNum'], ['_loc5_', 'playerNum', 'startPos', 'weaponType'], closure, 'Battle')
    assign(ref(this, '_toShowLastABArr'), '=', lambda: arr([]))
    e.set('_loc5_', rt.construct(e.get('Array'), []))
    switch_34 = e.get('playerNum')
    case_35 = -1
    if case_35 == -1 and strict_eq(switch_34, 0):
        case_35 = 0
    if case_35 == -1 and strict_eq(switch_34, 1):
        case_35 = 1
    if case_35 == -1 and strict_eq(switch_34, 2):
        case_35 = 2
    if case_35 == -1 and strict_eq(switch_34, 3):
        case_35 = 3
    if case_35 == -1 and strict_eq(switch_34, 4):
        case_35 = 4
    if case_35 == -1:
        case_35 = -1
    try:
        if 0 <= case_35 <= 0:
            if truth(binop('==', e.get('weaponType'), 'plane')):
                assign(e.ref('_loc5_'), '=', lambda: arr([580, 195]))
            if truth(binop('==', e.get('weaponType'), 'soldier')):
                assign(e.ref('_loc5_'), '=', lambda: arr([580, 195]))
            raise ASBreak()
        if 0 <= case_35 <= 1:
            if truth(binop('==', e.get('weaponType'), 'plane')):
                assign(e.ref('_loc5_'), '=', lambda: arr([260, 160]))
            if truth(binop('==', e.get('weaponType'), 'soldier')):
                assign(e.ref('_loc5_'), '=', lambda: arr([260, 160]))
            raise ASBreak()
        if 0 <= case_35 <= 2:
            if truth(binop('==', e.get('weaponType'), 'plane')):
                assign(e.ref('_loc5_'), '=', lambda: arr([580, 195]))
            if truth(binop('==', e.get('weaponType'), 'soldier')):
                assign(e.ref('_loc5_'), '=', lambda: arr([580, 195]))
            raise ASBreak()
        if 0 <= case_35 <= 3:
            if truth(binop('==', e.get('weaponType'), 'plane')):
                assign(e.ref('_loc5_'), '=', lambda: arr([280, 415]))
            if truth(binop('==', e.get('weaponType'), 'soldier')):
                assign(e.ref('_loc5_'), '=', lambda: arr([280, 415]))
            raise ASBreak()
        if 0 <= case_35 <= 4:
            if truth(binop('==', e.get('weaponType'), 'plane')):
                assign(e.ref('_loc5_'), '=', lambda: arr([580, 415]))
            if truth(binop('==', e.get('weaponType'), 'soldier')):
                assign(e.ref('_loc5_'), '=', lambda: arr([580, 415]))
    except ASBreak:
        pass
    return e.get('_loc5_')
    return U

def Battle_resetBattle(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Battle')
    assign(ref(this, 'unitCount'), '=', lambda: 0)
    assign(ref(this, '_toShowTimedABArr'), '=', lambda: arr([]))
    assign(ref(this, '_toShowInitABArr'), '=', lambda: arr([]))
    assign(ref(this, '_toShowInBattleABArr'), '=', lambda: arr([]))
    assign(ref(this, '_toShowLastABArr'), '=', lambda: arr([]))
    assign(ref(this, '_toSpawnUnitsArr'), '=', lambda: arr([]))
    return U

def Battle_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Battle')
    ref(this, '_toSpawnUnitsArr').set(rt.construct(e.get('Array'), []))
    ref(this, 'unitCount').set(0)

def register(rt):
    rt.define('Battle', None, Battle_fields, {'Battle': ASFunction(Battle_Battle), 'createBattleScriptVars': ASFunction(Battle_createBattleScriptVars), 'createToSpawnUnitsArr': ASFunction(Battle_createToSpawnUnitsArr), 'createToShowABArray': ASFunction(Battle_createToShowABArray), 'getLiftOffPos': ASFunction(Battle_getLiftOffPos), 'resetBattle': ASFunction(Battle_resetBattle)}, {'all_turn_buildings_arr': ASFunction(Battle___get__all_turn_buildings_arr), 'curLastAB': ASFunction(Battle___get__curLastAB), 'toShowTimedABArr': ASFunction(Battle___get__toShowTimedABArr), 'toShowInitABArr': ASFunction(Battle___get__toShowInitABArr), 'toShowInBattleABArr': ASFunction(Battle___get__toShowInBattleABArr), 'toShowLastABArr': ASFunction(Battle___get__toShowLastABArr)}, {'curAB': ASFunction(Battle___set__curAB)})
