# Generated from __Packages/Presenter.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Presenter_Presenter(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_model'], ['param_model'], closure, 'Presenter')
    e.call('__super__', [])
    assign(ref(this, 'model'), '=', lambda: e.get('param_model'))
    return U

def Presenter___set__model(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'Presenter')
    assign(ref(this, '_model'), '=', lambda: e.get('_param'))
    return U

def Presenter___get__model(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter')
    return ref(this, '_model').get()
    return U

def Presenter___set__view(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'Presenter')
    assign(ref(this, '_view'), '=', lambda: e.get('_param'))
    return U

def Presenter___get__view(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter')
    return ref(this, '_view').get()
    return U

def Presenter_updateMiniMap(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter')
    rt.call_ref(ref(ref(this, 'view').get(), 'updateCities'), [])
    return U

def Presenter_setOutlineColor(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'Presenter')
    for key_1 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_1)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get())
            rt.call_ref(ref(ref(ref(ref(this, 'view').get(), 'mapOutlineColorObj').get(), binop('+', 'outlineTrans', ref(e.get('_loc2_'), 'playerNum').get())).get(), 'setTransform'), [ref(e.get('_loc2_'), 'playerColorTint1').get()])
            rt.call_ref(ref(ref(ref(ref(this, 'view').get(), 'faceOutlineColorObj').get(), binop('+', 'outlineTrans', ref(e.get('_loc2_'), 'playerNum').get())).get(), 'setTransform'), [ref(e.get('_loc2_'), 'playerColorTint1').get()])
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Presenter_btn_pressed_new_game(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter')
    rt.call_ref(ref(e.get('_global'), 'stopAllSounds'), [])
    rt.call_ref(ref(e.get('_level0'), 'stopAllSounds'), [])
    rt.call_ref(ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'sound').get(), 'stop'), [])
    rt.call_ref(ref(ref(ref(this, 'model').get(), 'theme_sound').get(), 'stop'), [])
    ref(ref(e.get('_level0'), 'endGameMC').get(), 'onEnterFrame').delete()
    ref(e.get('_global'), 'model').delete()
    ref(e.get('_global'), 'model_interface').delete()
    ref(e.get('_global'), 'model_gameMenu').delete()
    rt.call_ref(ref(e.get('_root'), 'gotoAndPlay'), [2])
    return U

def Presenter_initBattle(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc14_', '_loc15_', '_loc16_', '_loc17_', '_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', 'i', 'j', 'k'], closure, 'Presenter')
    rt.call_ref(ref(ref(ref(this, 'model').get(), 'battle').get(), 'resetBattle'), [])
    rt.call_ref(ref(ref(ref(this, 'model').get(), 'battle').get(), 'createToSpawnUnitsArr'), [])
    e.set('_loc2_', 0)
    e.set('_loc3_', rt.construct(e.get('Array'), []))
    e.set('_loc4_', 0)
    for key_2 in keys(ref(ref(ref(this, 'model').get(), 'battle').get(), '_toSpawnUnitsArr').get()):
        e.ref('i').set(key_2)
        rt.tick()
        try:
            if truth(unary('!', ref(ref(ref(ref(ref(this, 'model').get(), 'battle').get(), '_toSpawnUnitsArr').get(), e.get('i')).get(), '_building').get())):
                assign(e.ref('_loc5_'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'battle').get(), '_toSpawnUnitsArr').get(), e.get('i')).get())
                assign(e.ref('_loc6_'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc5_'), 'player').get()).get(), 'playerColorTint1').get())
                assign(e.ref('_loc7_'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc5_'), 'player').get()).get(), 'playerColor').get())
                assign(e.ref('_loc4_'), '+=', lambda: 5)
                rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'battle').get(), '_activeUnitsArr').get(), 'push'), [rt.construct(e.get('Unit'), [ref(e.get('_loc5_'), 'unitID').get(), ref(ref(this, 'view').get(), 'battleSrcMC').get(), ref(rt.call_ref(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc5_'), 'player').get()).get(), 'weaponStock').get(), 'getWeaponByID'), [ref(e.get('_loc5_'), 'weaponID').get()]), 'weaponType').get(), binop('+', 'unit', assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))), ref(e.get('_loc5_'), 'startX').get(), ref(e.get('_loc5_'), 'startY').get(), ref(e.get('_loc5_'), 'wayPointArr').get(), ref(e.get('_loc5_'), 'result').get(), ref(e.get('_loc5_'), 'tail').get(), ref(e.get('_loc5_'), 'tailNum').get(), ref(e.get('_loc5_'), 'force_MC').get(), e.get('_loc6_'), ref(e.get('_loc5_'), 'startNum').get(), e.get('_loc4_'), ref(e.get('_loc5_'), 'targetPlayer').get(), ref(e.get('_loc5_'), 'tr').get(), ref(e.get('_loc5_'), 'player').get(), e.get('_loc7_'), ref(e.get('_loc5_'), 'wildCard').get(), ref(e.get('_loc5_'), 'explosion_name').get()])])
                if truth(ref(e.get('_loc5_'), 'tail').get()):
                    rt.call_ref(ref(e.get('_loc3_'), 'push'), [ref(e.get('_loc5_'), 'unitID').get()])
            else:
                assign(e.ref('_loc8_'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'battle').get(), '_toSpawnUnitsArr').get(), e.get('i')).get())
                rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'battle').get(), '_activeUnitsArr').get(), 'push'), [obj({'_building': True, 'obj': e.get('_loc8_')})])
            if truth(ref(ref(ref(ref(ref(this, 'model').get(), 'battle').get(), '_toSpawnUnitsArr').get(), e.get('i')).get(), '_addToSubArr').get()):
                rt.call_ref(ref(ref(ref(this, 'model').get(), 'attackingSubs_arr').get(), 'push'), [ref(ref(ref(ref(this, 'model').get(), 'battle').get(), '_toSpawnUnitsArr').get(), e.get('i')).get()])
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_3 in keys(e.get('_loc3_')):
        e.ref('i').set(key_3)
        rt.tick()
        try:
            assign(e.ref('_loc9_'), '=', lambda: ref(e.get('_loc3_'), e.get('i')).get())
            for key_4 in keys(ref(ref(ref(this, 'model').get(), 'battle').get(), '_activeUnitsArr').get()):
                e.ref('j').set(key_4)
                rt.tick()
                try:
                    assign(e.ref('_loc10_'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'battle').get(), '_activeUnitsArr').get(), e.get('j')).get())
                    if truth(binop('==', ref(e.get('_loc10_'), 'unitID').get(), e.get('_loc9_'))):
                        for key_5 in keys(ref(ref(ref(this, 'model').get(), 'battle').get(), '_activeUnitsArr').get()):
                            e.ref('k').set(key_5)
                            rt.tick()
                            try:
                                assign(e.ref('_loc11_'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'battle').get(), '_activeUnitsArr').get(), e.get('k')).get())
                                if truth(binop('==', ref(e.get('_loc10_'), 'tail').get(), ref(e.get('_loc11_'), 'unitID').get())):
                                    assign(ref(e.get('_loc10_'), 'tail'), '=', lambda: e.get('_loc11_'))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                except ASContinue:
                    pass
                except ASBreak:
                    break
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc12_', 0)
    e.set('_loc13_', arr([]))
    e.set('_loc14_', ref(ref(ref(e.get('_global'), 'model').get(), 'battle').get(), 'all_turn_buildings_arr').get())
    e.set('_loc15_', 0)
    while truth(binop('<', e.get('_loc15_'), ref(e.get('_loc14_'), 'length').get())):
        rt.tick()
        try:
            if truth(ref(ref(ref(e.get('_loc14_'), e.get('_loc15_')).get(), 'tr').get(), '_spyBuilding').get()):
                for key_6 in keys(e.get('_loc14_')):
                    e.ref('k').set(key_6)
                    rt.tick()
                    try:
                        if truth(logical('&&', binop('==', ref(ref(e.get('_loc14_'), e.get('k')).get(), '_frame').get(), ref(ref(e.get('_loc14_'), e.get('_loc15_')).get(), '_frame').get()), lambda: logical('&&', binop('!=', ref(e.get('_loc14_'), e.get('_loc15_')).get(), ref(e.get('_loc14_'), e.get('k')).get()), lambda: binop('==', ref(ref(e.get('_loc14_'), e.get('k')).get(), '_player').get(), ref(ref(e.get('_loc14_'), e.get('_loc15_')).get(), '_player').get())))):
                            assign(ref(ref(e.get('_loc14_'), e.get('_loc15_')).get(), '_frame'), '=', lambda: 'spyCenter')
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
            if truth(unary('!', rt.call_ref(ref(ref(this, 'model').get(), 'loop_playerAB_position_arr'), ['isDouble', ref(ref(e.get('_loc14_'), e.get('_loc15_')).get(), '_player').get(), ref(ref(e.get('_loc14_'), e.get('_loc15_')).get(), '_frame').get()]))):
                if truth(binop('!=', ref(ref(e.get('_loc14_'), e.get('_loc15_')).get(), '_frame').get(), 'propaganda_2')):
                    assign(e.ref('_loc16_'), '=', lambda: rt.call_ref(ref(ref(this, 'view').get(), 'showActionBuildingFromObj'), [ref(e.get('_loc14_'), e.get('_loc15_')).get()]))
                    rt.call_ref(ref(this, 'add_to_playerAB_position_arr'), [ref(ref(e.get('_loc14_'), e.get('_loc15_')).get(), '_player').get(), ref(ref(e.get('_loc14_'), e.get('_loc15_')).get(), '_frame').get(), e.get('_loc16_')])
                else:
                    if truth(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(ref(e.get('_loc14_'), e.get('_loc15_')).get(), '_player').get()).get(), 'preLocation').get()):
                        assign(e.ref('_loc17_'), '=', lambda: rt.call_ref(ref(this, 'get_preAB_mc'), [ref(ref(e.get('_loc14_'), e.get('_loc15_')).get(), '_player').get()]))
                        rt.call_ref(ref(this, 'add_to_playerAB_position_arr'), [ref(ref(e.get('_loc14_'), e.get('_loc15_')).get(), '_player').get(), ref(ref(e.get('_loc14_'), e.get('_loc15_')).get(), '_frame').get(), e.get('_loc17_')])
            assign(e.ref('_loc15_'), '=', lambda: binop('+', e.get('_loc15_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    rt.call_ref(ref(this, 'set_playerAB_position_arr_action_names'), [])
    assign(ref(ref(this, 'view').get(), 'AB_interval_ID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [ref(this, 'view').get(), 'interval_func', 1600]))
    if truth(ref(ref(e.get('_global'), 'debug').get(), 'skip_battle_animation').get()):
        assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [ref(e.get('_global'), 'presenter').get(), 'allUnitsDone', 100]))
    else:
        rt.call_ref(ref(ref(this, 'view').get(), 'createUnitTicker'), [])
    return U

def Presenter_add_to_playerAB_position_arr(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_plrNum', '_aname', '_mc'], ['_aname', '_loc5_', '_mc', '_plrNum', 'i'], closure, 'Presenter')
    for key_7 in keys(ref(ref(this, 'model').get(), 'playerAB_position_arr').get()):
        e.ref('i').set(key_7)
        rt.tick()
        try:
            assign(e.ref('_loc5_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerAB_position_arr').get(), e.get('i')).get())
            if truth(logical('&&', binop('==', ref(e.get('_loc5_'), '_num').get(), e.get('_plrNum')), lambda: logical('||', unary('!', ref(e.get('_loc5_'), 'building_name').get()), lambda: binop('==', ref(e.get('_loc5_'), 'building_name').get(), '')))):
                assign(ref(ref(ref(ref(this, 'model').get(), 'playerAB_position_arr').get(), e.get('i')).get(), 'building_name'), '=', lambda: e.get('_aname'))
                assign(ref(ref(ref(ref(this, 'model').get(), 'playerAB_position_arr').get(), e.get('i')).get(), 'building_MC'), '=', lambda: e.get('_mc'))
                raise ASBreak()
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Presenter_set_playerAB_position_arr_action_names(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i', 'j'], closure, 'Presenter')
    for key_8 in keys(ref(ref(this, 'model').get(), 'playerAB_position_arr').get()):
        e.ref('i').set(key_8)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerAB_position_arr').get(), e.get('i')).get())
            for key_9 in keys(ref(ref(this, 'model').get(), 'building_names_to_actions_arr').get()):
                e.ref('j').set(key_9)
                rt.tick()
                try:
                    if truth(binop('==', ref(ref(ref(ref(this, 'model').get(), 'building_names_to_actions_arr').get(), e.get('j')).get(), 'building_name').get(), ref(e.get('_loc2_'), 'building_name').get())):
                        assign(ref(e.get('_loc2_'), 'action_name'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'building_names_to_actions_arr').get(), e.get('j')).get(), 'action_name').get())
                except ASContinue:
                    pass
                except ASBreak:
                    break
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Presenter_get_preAB_mc(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_plrNum'], ['_loc3_', '_plrNum'], closure, 'Presenter')
    e.set('_loc3_', ref(ref(ref(this, 'view').get(), 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'ab', e.get('_plrNum')), '_'), ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), e.get('_plrNum')).get(), 'preLocation').get())).get())
    return e.get('_loc3_')
    return U

def Presenter_allUnitsDone(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', 'i'], closure, 'Presenter')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'allUnitsDone_intervalID').get()])
    e.set('_loc2_', 0)
    for key_10 in keys(ref(ref(ref(this, 'model').get(), 'battle').get(), '_toDeleteUnitsArr').get()):
        e.ref('i').set(key_10)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'battle').get(), '_toDeleteUnitsArr').get(), e.get('i')).get())
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
            rt.call_ref(ref(ref(e.get('_loc3_'), 'explosionMC').get(), 'removeMovieClip'), [])
            rt.call_ref(ref(ref(e.get('_loc3_'), 'MC').get(), 'removeMovieClip'), [])
            rt.call_ref(ref(ref(e.get('_loc3_'), 'tintMC').get(), 'removeMovieClip'), [])
            rt.call_ref(ref(ref(e.get('_loc3_'), 'shadowMC').get(), 'removeMovieClip'), [])
            if truth(binop('>', e.get('_loc2_'), 20)):
                raise ASBreak()
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc4_', 0)
    while truth(binop('<', e.get('_loc4_'), ref(ref(ref(ref(this, 'model').get(), 'battle').get(), '_toDeleteExplosionMC_arr').get(), 'length').get())):
        rt.tick()
        try:
            rt.call_ref(ref(ref(ref(ref(ref(this, 'model').get(), 'battle').get(), '_toDeleteExplosionMC_arr').get(), e.get('_loc4_')).get(), 'removeMovieClip'), [])
            rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'battle').get(), '_toDeleteExplosionMC_arr').get(), 'splice'), [e.get('_loc4_'), 1])
            if truth(binop('>', e.get('_loc4_'), 20)):
                raise ASBreak()
            assign(e.ref('_loc4_'), '=', lambda: binop('+', e.get('_loc4_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [ref(e.get('_global'), 'presenter').get(), 'endBattle', 25]))
    return U

def Presenter_showLastActionBuildings(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter')
    assign(ref(ref(this, 'model').get(), 'actionBuildingInterval'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [ref(this, 'view').get(), 'getIntervalBuildingsArray', 2000]))
    return U

def Presenter_endBattle(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'Presenter')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'allUnitsDone_intervalID').get()])
    assign(ref(ref(e.get('_global'), 'model').get(), 'battleTimerArr'), '=', lambda: arr([]))
    assign(ref(ref(e.get('_global'), 'model').get(), 'battleCounter'), '=', lambda: 20)
    assign(ref(ref(e.get('_global'), 'model').get(), 'battleTimerIndex'), '=', lambda: 0)
    assign(ref(ref(e.get('_global'), 'model').get(), 'unitStartNum'), '=', lambda: 0)
    for key_11 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_11)
        rt.tick()
        try:
            rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get(), 'resetBuildingsShown'), [])
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [ref(e.get('_global'), 'presenter').get(), 'initInterface_1', 25]))
    return U

def Presenter_doTR_from_battle(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['tr'], ['_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc14_', '_loc15_', '_loc16_', '_loc17_', '_loc19_', '_loc20_', '_loc21_', '_loc22_', '_loc23_', '_loc24_', '_loc25_', '_loc26_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', 'i', 'j', 'tr'], closure, 'Presenter')
    e.set('_loc5_', ' ok ')
    switch_12 = ref(e.get('tr'), '_item').get()
    case_13 = -1
    if case_13 == -1 and strict_eq(switch_12, 'battle'):
        case_13 = 0
    if case_13 == -1 and strict_eq(switch_12, 'resources'):
        case_13 = 1
    if case_13 == -1 and strict_eq(switch_12, 'religion'):
        case_13 = 2
    if case_13 == -1 and strict_eq(switch_12, 'propaganda'):
        case_13 = 3
    if case_13 == -1:
        case_13 = 4
    try:
        if 0 <= case_13 <= 0:
            if truth(unary('!', ref(e.get('tr'), '_spyArr').get())):
                for key_14 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
                    e.ref('i').set(key_14)
                    rt.tick()
                    try:
                        for key_15 in keys(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get(), 'cityArr').get()):
                            e.ref('j').set(key_15)
                            rt.tick()
                            try:
                                assign(e.ref('_loc6_'), '=', lambda: ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get(), 'cityArr').get(), e.get('j')).get())
                                if truth(logical('&&', binop('==', ref(e.get('_loc6_'), 'cityID').get(), ref(e.get('tr'), '_city').get()), lambda: logical('&&', unary('!', rt.call_ref(ref(e.get('_global'), 'isNaN'), [ref(e.get('tr'), '_casualties').get()])), lambda: ref(e.get('tr'), '_casualties').get()))):
                                    assign(ref(e.get('_loc6_'), 'total_battle_casualties'), '+=', lambda: ref(e.get('tr'), '_casualties').get())
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
                if truth(ref(e.get('tr'), '_isShip').get()):
                    assign(e.ref('_loc7_'), '=', lambda: 0)
                    while truth(binop('<', e.get('_loc7_'), ref(ref(e.get('tr'), '_attack_arr').get(), 'length').get())):
                        rt.tick()
                        try:
                            assign(e.ref('_loc8_'), '=', lambda: ref(ref(e.get('tr'), '_attack_arr').get(), e.get('_loc7_')).get())
                            assign(e.ref('_loc9_'), '=', lambda: ref(ref(e.get('tr'), '_result_arr').get(), e.get('_loc7_')).get())
                            assign(ref(rt.call_ref(ref(ref(this, 'model').get(), 'getCityByID'), [ref(e.get('_loc8_'), 'city').get()]), 'total_battle_casualties'), '=', lambda: binop('+', ref(rt.call_ref(ref(ref(this, 'model').get(), 'getCityByID'), [ref(e.get('_loc8_'), 'city').get()]), 'total_battle_casualties').get(), ref(e.get('_loc9_'), '_casualties').get()))
                            assign(e.ref('_loc7_'), '=', lambda: binop('+', e.get('_loc7_'), 1))
                        except ASContinue:
                            pass
                        except ASBreak:
                            break
            else:
                assign(e.ref('_loc10_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('tr'), '_a').get()).get())
                assign(e.ref('_loc11_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('tr'), '_b').get()).get())
                assign(e.ref('_loc12_'), '=', lambda: '')
                assign(e.ref('_loc13_'), '=', lambda: '')
                if truth(binop('>=', ref(e.get('_loc11_'), 'money').get(), ref(ref(e.get('tr'), '_spyArr').get(), 0).get())):
                    assign(ref(e.get('_loc10_'), 'money'), '+=', lambda: ref(ref(e.get('tr'), '_spyArr').get(), 0).get())
                    assign(ref(e.get('_loc11_'), 'money'), '-=', lambda: ref(ref(e.get('tr'), '_spyArr').get(), 0).get())
                else:
                    assign(ref(ref(e.get('tr'), '_spyArr').get(), 0), '=', lambda: ref(e.get('_loc11_'), 'money').get())
                    assign(ref(e.get('_loc11_'), 'money'), '=', lambda: 0)
                    assign(ref(e.get('_loc10_'), 'money'), '+=', lambda: ref(ref(e.get('tr'), '_spyArr').get(), 0).get())
                assign(e.ref('_loc14_'), '=', lambda: 2)
                while truth(binop('<', e.get('_loc14_'), ref(ref(e.get('tr'), '_spyArr').get(), 'length').get())):
                    rt.tick()
                    try:
                        assign(e.ref('_loc4_'), '=', lambda: ref(ref(e.get('tr'), '_spyArr').get(), e.get('_loc14_')).get())
                        if truth(ref(rt.call_ref(ref(ref(e.get('_loc10_'), 'weaponStock').get(), 'getWeaponByID'), [e.get('_loc4_')]), 'active').get()):
                            assign(e.ref('_loc12_'), '+=', lambda: binop('+', binop('+', 'WEAPON: ', ref(rt.call_ref(ref(ref(e.get('_loc10_'), 'weaponStock').get(), 'getWeaponByID'), [e.get('_loc4_')]), 'prettyName').get()), ' <br/> '))
                            assign(e.ref('_loc13_'), '+=', lambda: binop('+', binop('+', 'STOLEN: ', ref(rt.call_ref(ref(ref(e.get('_loc10_'), 'weaponStock').get(), 'getWeaponByID'), [e.get('_loc4_')]), 'prettyName').get()), ' <br/> '))
                            assign(ref(rt.call_ref(ref(ref(e.get('_loc10_'), 'weaponStock').get(), 'getWeaponByID'), [e.get('_loc4_')]), 'inStock'), '=', lambda: binop('+', ref(rt.call_ref(ref(ref(e.get('_loc10_'), 'weaponStock').get(), 'getWeaponByID'), [e.get('_loc4_')]), 'inStock').get(), 1))
                            if truth(ref(rt.call_ref(ref(ref(e.get('_loc11_'), 'weaponStock').get(), 'getWeaponByID'), [e.get('_loc4_')]), 'inStock').get()):
                                assign(ref(rt.call_ref(ref(ref(e.get('_loc11_'), 'weaponStock').get(), 'getWeaponByID'), [e.get('_loc4_')]), 'inStock'), '=', lambda: binop('-', ref(rt.call_ref(ref(ref(e.get('_loc11_'), 'weaponStock').get(), 'getWeaponByID'), [e.get('_loc4_')]), 'inStock').get(), 1))
                        else:
                            assign(e.ref('_loc12_'), '+=', lambda: binop('+', binop('+', ' TECHNOLOGY: ', ref(rt.call_ref(ref(ref(e.get('_loc10_'), 'weaponStock').get(), 'getWeaponByID'), [e.get('_loc4_')]), 'prettyName').get()), ' <br/> '))
                            assign(ref(rt.call_ref(ref(ref(e.get('_loc10_'), 'weaponStock').get(), 'getWeaponByID'), [e.get('_loc4_')]), 'active'), '=', lambda: True)
                            rt.call_ref(ref(ref(e.get('_loc10_'), 'techTree').get(), 'inventTechByName'), [ref(rt.call_ref(ref(ref(e.get('_loc10_'), 'weaponStock').get(), 'getWeaponByID'), [e.get('_loc4_')]), 'relatedTechName').get()])
                        assign(e.ref('_loc14_'), '=', lambda: binop('+', e.get('_loc14_'), 1))
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
                if truth(binop('>', ref(ref(e.get('tr'), '_spyArr').get(), 0).get(), 0)):
                    rt.call_ref(ref(ref(e.get('_loc10_'), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'spy', '_msg': binop('+', binop('+', binop('+', 'YOUR SPY STOLE <br/> $', ref(ref(e.get('tr'), '_spyArr').get(), 0).get()), '.000.000,<br/> '), e.get('_loc12_'))})])
                    rt.call_ref(ref(ref(e.get('_loc11_'), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'spy', '_msg': binop('+', binop('+', binop('+', 'AN ENEMY SPY STOLE <br/> $', ref(ref(e.get('tr'), '_spyArr').get(), 0).get()), '.000.000,<br/> '), e.get('_loc13_'))})])
                else:
                    if truth(ref(ref(e.get('tr'), '_spyArr').get(), 1).get()):
                        rt.call_ref(ref(ref(e.get('_loc10_'), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'spy', '_msg': binop('+', 'YOUR SPY STOLE <br/>', e.get('_loc12_'))})])
                        rt.call_ref(ref(ref(e.get('_loc11_'), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'spy', '_msg': binop('+', 'A ENEMY SPY STOLE <br/>', e.get('_loc13_'))})])
                    else:
                        if truth(binop('<', ref(ref(e.get('tr'), '_spyArr').get(), 'length').get(), 1)):
                            rt.call_ref(ref(ref(e.get('_loc10_'), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'spy', '_msg': 'YOUR SPY DID NOT STEAL ANYTHING'})])
                            rt.call_ref(ref(ref(e.get('_loc11_'), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'spy', '_msg': 'AN ENEMY SPY WAS STOPPED'})])
            raise ASBreak()
        if 0 <= case_13 <= 1:
            if truth(binop('==', ref(e.get('tr'), '_plusmin').get(), 'plus')):
                assign(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('tr'), '_player').get()).get(), 'money'), '+=', lambda: ref(e.get('tr'), '_value').get())
                assign(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('tr'), '_player').get()).get(), 'turnResourcesGained'), '+=', lambda: ref(e.get('tr'), '_value').get())
                rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'addToHighscore'), [ref(e.get('tr'), '_player').get(), 5, ref(e.get('tr'), '_value').get()])
            else:
                assign(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('tr'), '_player').get()).get(), 'money'), '-=', lambda: ref(e.get('tr'), '_value').get())
            raise ASBreak()
        if 0 <= case_13 <= 2:
            assign(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('tr'), '_player').get()).get(), 'religion'), '+=', lambda: ref(e.get('tr'), '_value').get())
            rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'addToHighscore'), [ref(e.get('tr'), '_player').get(), 6, ref(e.get('tr'), '_value').get()])
            raise ASBreak()
        if 0 <= case_13 <= 3:
            assign(e.ref('_loc15_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('tr'), '_a').get()).get())
            assign(e.ref('_loc16_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('tr'), '_b').get()).get())
            assign(e.ref('_loc17_'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'getCityByID'), [ref(e.get('tr'), '_city').get()]))
            assign(e.ref('_loc20_'), '=', lambda: binop('-', ref(e.get('_loc15_'), 'religion').get(), ref(e.get('_loc16_'), 'religion').get()))
            if truth(binop('<', e.get('_loc20_'), 0)):
                assign(e.ref('_loc20_'), '=', lambda: 0)
            assign(e.ref('_loc21_'), '=', lambda: 0)
            if truth(binop('>', binop('-', ref(e.get('_loc15_'), 'population').get(), ref(e.get('_loc16_'), 'population').get()), 20)):
                assign(e.ref('_loc21_'), '=', lambda: unary('-', 1))
            if truth(binop('>', binop('-', ref(e.get('_loc15_'), 'population').get(), ref(e.get('_loc16_'), 'population').get()), 40)):
                assign(e.ref('_loc21_'), '=', lambda: unary('-', 2))
            if truth(binop('>', binop('-', ref(e.get('_loc15_'), 'population').get(), ref(e.get('_loc16_'), 'population').get()), 80)):
                assign(e.ref('_loc21_'), '=', lambda: unary('-', 4))
            if truth(binop('>', binop('-', ref(e.get('_loc16_'), 'population').get(), ref(e.get('_loc15_'), 'population').get()), 20)):
                assign(e.ref('_loc21_'), '=', lambda: 1)
            if truth(binop('>', binop('-', ref(e.get('_loc16_'), 'population').get(), ref(e.get('_loc15_'), 'population').get()), 40)):
                assign(e.ref('_loc21_'), '=', lambda: 2)
            if truth(binop('>', binop('-', ref(e.get('_loc16_'), 'population').get(), ref(e.get('_loc15_'), 'population').get()), 80)):
                assign(e.ref('_loc21_'), '=', lambda: 4)
            if truth(binop('>', ref(e.get('_loc15_'), 'religion').get(), ref(e.get('_loc16_'), 'religion').get())):
                assign(e.ref('_loc19_'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [e.get('_loc20_')]))
            else:
                assign(e.ref('_loc19_'), '=', lambda: 0)
            if truth(binop('==', ref(e.get('_loc15_'), 'playedBy').get(), 'AI')):
                if truth(binop('>', e.get('_loc19_'), 25)):
                    assign(e.ref('_loc19_'), '=', lambda: 25)
            else:
                if truth(binop('>', e.get('_loc19_'), 15)):
                    assign(e.ref('_loc19_'), '=', lambda: 15)
            assign(e.ref('_loc19_'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'max'), [0, binop('+', e.get('_loc19_'), e.get('_loc21_'))]))
            if truth(binop('==', ref(e.get('_loc16_'), 'religion').get(), 100)):
                assign(e.ref('_loc19_'), '=', lambda: 0)
            assign(e.ref('_loc22_'), '=', lambda: 0)
            assign(e.ref('_loc22_'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'min'), [rt.call_ref(ref(e.get('Math'), 'round'), [binop('*', binop('/', binop('-', ref(e.get('_loc17_'), 'population').get(), ref(e.get('_loc17_'), 'total_battle_casualties').get()), 100), binop('+', e.get('_loc19_'), 5))]), 40]))
            assign(e.ref('_loc22_'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [binop('/', e.get('_loc22_'), 2)]))
            rt.call_ref(ref(ref(e.get('_loc17_'), 'propagandaMin').get(), 'push'), [e.get('_loc22_')])
            if truth(binop('>', e.get('_loc22_'), 0)):
                rt.call_ref(ref(ref(e.get('_loc15_'), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'propagandaGained', '_msg': binop('+', binop('+', 'You gained ', e.get('_loc22_')), '.000.000 citizens from propaganda')})])
                rt.call_ref(ref(ref(e.get('_loc16_'), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'propagandaLost', '_msg': binop('+', binop('+', 'You lost ', e.get('_loc22_')), '.000.000 citizens from propaganda')})])
            assign(ref(e.get('_loc16_'), 'turnPropagandaCasualties'), '+=', lambda: e.get('_loc22_'))
            rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'addToHighscore'), [e.get('_loc15_'), 7, e.get('_loc22_')])
            assign(e.ref('_loc23_'), '=', lambda: rt.construct(e.get('Array'), []))
            for key_16 in keys(ref(e.get('_loc15_'), 'cityArr').get()):
                e.ref('j').set(key_16)
                rt.tick()
                try:
                    assign(e.ref('_loc24_'), '=', lambda: ref(ref(e.get('_loc15_'), 'cityArr').get(), e.get('j')).get())
                    if truth(logical('&&', binop('>=', ref(e.get('_loc24_'), 'population').get(), 1), lambda: unary('!', ref(e.get('_loc24_'), 'propaganda_exclude').get()))):
                        rt.call_ref(ref(e.get('_loc23_'), 'push'), [e.get('_loc24_')])
                except ASContinue:
                    pass
                except ASBreak:
                    break
            assign(e.ref('_loc25_'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [binop('/', e.get('_loc22_'), ref(e.get('_loc23_'), 'length').get())]))
            for key_17 in keys(e.get('_loc23_')):
                e.ref('j').set(key_17)
                rt.tick()
                try:
                    assign(e.ref('_loc26_'), '=', lambda: ref(e.get('_loc23_'), e.get('j')).get())
                    assign(ref(e.get('_loc26_'), 'propagandaPlus'), '+=', lambda: e.get('_loc25_'))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            raise ASBreak()
        if 0 <= case_13 <= 4:
            assign(e.ref('_loc5_'), '=', lambda: binop('+', ' error with string: ', ref(e.get('tr'), '_value').get()))
    except ASBreak:
        pass
    return e.get('_loc5_')
    return U

def Presenter_killPlayer(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_plr'], ['_plr'], closure, 'Presenter')
    rt.call_ref(ref(ref(this, 'model').get(), 'killPlayer'), [e.get('_plr')])
    if truth(binop('==', ref(e.get('_plr'), 'playedBy').get(), 'human')):
        rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'allUnitsDone_intervalID').get()])
        rt.call_ref(ref(ref(this, 'view').get(), 'changeOver'), ['toPlayerLost'])
    rt.call_ref(ref(ref(ref(ref(this, 'view').get(), 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'ab', ref(e.get('_plr'), 'playerNum').get()), '_'), 1)).get(), 'gotoAndStop'), [1])
    rt.call_ref(ref(ref(ref(ref(this, 'view').get(), 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'ab', ref(e.get('_plr'), 'playerNum').get()), '_'), 2)).get(), 'gotoAndStop'), [1])
    assign(ref(e.get('_plr'), 'alive'), '=', lambda: False)
    if truth(logical('&&', binop('==', ref(ref(ref(this, 'model').get(), 'activePlayerArr').get(), 'length').get(), 1), lambda: ref(ref(ref(this, 'model').get(), 'human').get(), 'alive').get())):
        rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'allUnitsDone_intervalID').get()])
        rt.call_ref(ref(ref(this, 'view').get(), 'changeOver'), ['toPlayerWin'])
    return U

def Presenter_updatePlayerVars_1(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', 'i', 'j'], closure, 'Presenter')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'allUnitsDone_intervalID').get()])
    for key_18 in keys(ref(ref(this, 'model').get(), 'activePlayerArr').get()):
        e.ref('i').set(key_18)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'activePlayerArr').get(), e.get('i')).get())
            assign(ref(e.get('_loc2_'), 'heliStart'), '=', lambda: arr([]))
            rt.call_ref(ref(ref(e.get('_loc2_'), 'weaponStock').get(), 'resetInUse'), [])
            assign(ref(e.get('_loc2_'), 'anti_active'), '=', lambda: e.get('undefined'))
            assign(ref(e.get('_loc2_'), 'anti_type'), '=', lambda: e.get('undefined'))
            assign(ref(e.get('_loc2_'), 'anti_pos_arr'), '=', lambda: arr([]))
            assign(ref(e.get('_loc2_'), 'anti_loc'), '=', lambda: e.get('undefined'))
            assign(ref(e.get('_loc2_'), 'anti_inBattle_target'), '=', lambda: e.get('undefined'))
            assign(ref(e.get('_loc2_'), 'shipFrame'), '=', lambda: 1)
            assign(ref(e.get('_loc2_'), 'production_money_returned'), '=', lambda: 0)
            if truth(binop('>', ref(e.get('_loc2_'), 'religion').get(), 100)):
                assign(ref(e.get('_loc2_'), 'religion'), '=', lambda: 100)
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_19 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_19)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get())
            for key_20 in keys(ref(e.get('_loc3_'), 'cityArr').get()):
                e.ref('j').set(key_20)
                rt.tick()
                try:
                    if truth(rt.call_ref(ref(e.get('_global'), 'isNaN'), [ref(ref(ref(e.get('_loc3_'), 'cityArr').get(), e.get('j')).get(), 'population').get()])):
                        assign(ref(ref(ref(e.get('_loc3_'), 'cityArr').get(), e.get('j')).get(), 'population'), '=', lambda: 0)
                except ASContinue:
                    pass
                except ASBreak:
                    break
            if truth(binop('<=', ref(e.get('_loc3_'), 'population').get(), 0)):
                rt.call_ref(ref(this, 'killPlayer'), [e.get('_loc3_')])
        except ASContinue:
            pass
        except ASBreak:
            break
    if truth(ref(ref(ref(this, 'model').get(), 'human').get(), 'alive').get()):
        rt.call_ref(ref(this, 'updatePlayerVars_2'), [])
    return U

def Presenter_updatePlayerVars_2(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc14_', '_loc15_', '_loc16_', '_loc17_', '_loc18_', '_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', 'i', 'j', 'k', 'sp_i'], closure, 'Presenter')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'allUnitsDone_intervalID').get()])
    e.set('_loc2_', 0)
    for key_21 in keys(ref(ref(this, 'model').get(), 'turnResultsArr').get()):
        e.ref('i').set(key_21)
        rt.tick()
        try:
            if truth(binop('>=', e.get('_loc2_'), 50)):
                raise ASBreak()
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), e.get('i')).get())
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_player').get()).get())
            switch_22 = ref(e.get('_loc3_'), '_item').get()
            case_23 = -1
            if case_23 == -1 and strict_eq(switch_22, 'battle'):
                case_23 = 0
            if case_23 == -1 and strict_eq(switch_22, 'produce'):
                case_23 = 1
            if case_23 == -1 and strict_eq(switch_22, 'propaganda'):
                case_23 = 2
            if case_23 == -1 and strict_eq(switch_22, 'research'):
                case_23 = 3
            if case_23 == -1 and strict_eq(switch_22, 'setPreAttack'):
                case_23 = 4
            if case_23 == -1 and strict_eq(switch_22, 'attack'):
                case_23 = 5
            if case_23 == -1 and strict_eq(switch_22, 'defense'):
                case_23 = 6
            if case_23 == -1 and strict_eq(switch_22, 'diplomacy'):
                case_23 = 7
            if case_23 == -1 and strict_eq(switch_22, 'diplomacyAccepted'):
                case_23 = 8
            if case_23 == -1 and strict_eq(switch_22, 'diplomacyRejected'):
                case_23 = 9
            if case_23 == -1 and strict_eq(switch_22, 'bioload'):
                case_23 = 10
            if case_23 == -1 and strict_eq(switch_22, 'reset_spy_readiness'):
                case_23 = 11
            if case_23 == -1:
                case_23 = -1
            try:
                if 0 <= case_23 <= 0:
                    if truth(binop('==', ref(rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'weaponStock').get(), 'getWeaponByID'), [ref(e.get('_loc3_'), '_weapon').get()]), 'weaponName').get(), 'space')):
                        update(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_a').get()).get(), 'satellites_used'), 1, False)
                    if truth(logical('&&', unary('!', ref(ref(e.get('_loc3_'), '_attack_arr').get(), 0).get()), lambda: unary('!', ref(e.get('_loc3_'), '_dontReduce').get()))):
                        if truth(ref(e.get('_loc3_'), '_payload').get()):
                            rt.call_ref(ref(ref(e.get('_loc4_'), 'weaponStock').get(), 'reduceWeaponByID'), [ref(e.get('_loc3_'), '_payload').get(), 1])
                        else:
                            rt.call_ref(ref(ref(e.get('_loc4_'), 'weaponStock').get(), 'reduceWeaponByID'), [ref(e.get('_loc3_'), '_weapon').get(), 1])
                    else:
                        for key_24 in keys(ref(e.get('_loc3_'), '_attack_arr').get()):
                            e.ref('j').set(key_24)
                            rt.tick()
                            try:
                                rt.call_ref(ref(ref(e.get('_loc4_'), 'weaponStock').get(), 'reduceWeaponByID'), [ref(ref(ref(e.get('_loc3_'), '_attack_arr').get(), e.get('j')).get(), 'wpn').get(), 1])
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                    assign(e.ref('_loc5_'), '=', lambda: ref(e.get('_loc3_'), '_casualties').get())
                    if truth(ref(e.get('_loc3_'), '_attack_arr').get()):
                        assign(e.ref('_loc5_'), '=', lambda: binop('+', binop('+', ref(ref(ref(e.get('_loc3_'), '_attack_arr').get(), 0).get(), '_casualties').get(), ref(ref(ref(e.get('_loc3_'), '_attack_arr').get(), 1).get(), '_casualties').get()), ref(ref(ref(e.get('_loc3_'), '_attack_arr').get(), 2).get(), '_casualties').get()))
                    if truth(logical('&&', logical('||', unary('!', e.get('_loc5_')), lambda: rt.call_ref(ref(e.get('_global'), 'isNaN'), [e.get('_loc5_')])), lambda: binop('!=', e.get('_loc5_'), 0))):
                        assign(e.ref('_loc5_'), '=', lambda: 40)
                    if truth(ref(e.get('_loc3_'), '_dontReduce').get()):
                        raise ASBreak()
                    assign(e.ref('_loc6_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_a').get()).get())
                    assign(e.ref('_loc7_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_b').get()).get())
                    assign(ref(ref(e.get('_loc6_'), 'regardArr').get(), ref(e.get('_loc3_'), '_b').get()), '-=', lambda: e.get('_loc5_'))
                    assign(ref(ref(e.get('_loc7_'), 'regardArr').get(), ref(e.get('_loc3_'), '_a').get()), '-=', lambda: e.get('_loc5_'))
                    if truth(logical('&&', ref(e.get('_loc7_'), 'special_person').get(), lambda: binop('==', ref(e.get('_loc6_'), 'playedBy').get(), 'AI'))):
                        for key_25 in keys(ref(ref(this, 'model').get(), 'activePlayerArr').get()):
                            e.ref('sp_i').set(key_25)
                            rt.tick()
                            try:
                                assign(ref(ref(ref(ref(ref(this, 'model').get(), 'activePlayerArr').get(), e.get('sp_i')).get(), 'regardArr').get(), ref(e.get('_loc6_'), 'playerNum').get()), '-=', lambda: 7)
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                    for key_26 in keys(ref(ref(this, 'model').get(), 'activePlayerArr').get()):
                        e.ref('k').set(key_26)
                        rt.tick()
                        try:
                            assign(e.ref('_loc8_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'activePlayerArr').get(), e.get('k')).get())
                            if truth(logical('&&', binop('!=', e.get('_loc8_'), e.get('_loc6_')), lambda: logical('&&', binop('!=', e.get('_loc8_'), e.get('_loc7_')), lambda: ref(ref(ref(e.get('_loc8_'), 'ceaseFireArr').get(), ref(e.get('_loc3_'), '_a').get()).get(), '_status').get()))):
                                if truth(binop('>', ref(ref(e.get('_loc8_'), 'regardArr').get(), ref(e.get('_loc3_'), '_b').get()).get(), ref(ref(e.get('_loc8_'), 'regardArr').get(), ref(e.get('_loc3_'), '_a').get()).get())):
                                    assign(ref(ref(e.get('_loc8_'), 'regardArr').get(), ref(e.get('_loc3_'), '_a').get()), '-=', lambda: binop('/', e.get('_loc5_'), 20))
                                else:
                                    assign(ref(ref(e.get('_loc8_'), 'regardArr').get(), ref(e.get('_loc3_'), '_a').get()), '+=', lambda: binop('/', e.get('_loc5_'), 20))
                        except ASContinue:
                            pass
                        except ASBreak:
                            break
                    raise ASBreak()
                if 0 <= case_23 <= 1:
                    assign(e.ref('_loc9_'), '=', lambda: rt.call_ref(ref(ref(e.get('_loc4_'), 'weaponStock').get(), 'getWeaponByID'), [ref(e.get('_loc3_'), '_value').get()]))
                    rt.call_ref(ref(ref(e.get('_loc4_'), 'weaponStock').get(), 'produceWeaponByName'), [ref(e.get('_loc9_'), 'weaponName').get(), ref(e.get('_loc3_'), '_amount').get()])
                    assign(ref(e.get('_loc4_'), 'money'), '-=', lambda: binop('*', e.call('Number', [ref(e.get('_loc9_'), 'cost').get()]), e.call('Number', [ref(e.get('_loc3_'), '_amount').get()])))
                    raise ASBreak()
                if 0 <= case_23 <= 2:
                    assign(e.ref('_loc10_'), '=', lambda: rt.call_ref(ref(ref(ref(this, 'model').get(), 'tools').get(), 'randRange'), [5, 10]))
                    assign(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_a').get()).get(), 'regardArr').get(), ref(e.get('_loc3_'), '_b').get()), '-=', lambda: e.get('_loc10_'))
                    assign(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_b').get()).get(), 'regardArr').get(), ref(e.get('_loc3_'), '_a').get()), '-=', lambda: e.get('_loc10_'))
                    for key_27 in keys(ref(ref(this, 'model').get(), 'activePlayerArr').get()):
                        e.ref('k').set(key_27)
                        rt.tick()
                        try:
                            assign(e.ref('_loc11_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'activePlayerArr').get(), e.get('k')).get())
                            if truth(logical('&&', binop('!=', ref(e.get('_loc11_'), 'playerNum').get(), ref(e.get('_loc3_'), '_a').get()), lambda: binop('!=', ref(e.get('_loc11_'), 'playerNum').get(), ref(e.get('_loc3_'), '_b').get()))):
                                if truth(binop('>', ref(ref(e.get('_loc11_'), 'regardArr').get(), ref(e.get('_loc3_'), '_a').get()).get(), ref(ref(e.get('_loc11_'), 'regardArr').get(), ref(e.get('_loc3_'), '_b').get()).get())):
                                    assign(ref(ref(e.get('_loc11_'), 'regardArr').get(), ref(e.get('_loc3_'), '_a').get()), '+=', lambda: binop('/', e.get('_loc10_'), 5))
                                else:
                                    assign(ref(ref(e.get('_loc11_'), 'regardArr').get(), ref(e.get('_loc3_'), '_a').get()), '-=', lambda: binop('/', e.get('_loc10_'), 5))
                        except ASContinue:
                            pass
                        except ASBreak:
                            break
                    raise ASBreak()
                if 0 <= case_23 <= 3:
                    assign(e.ref('_loc12_'), '=', lambda: rt.call_ref(ref(ref(e.get('_loc4_'), 'techTree').get(), 'getTechByID'), [ref(e.get('_loc3_'), '_value').get()]))
                    rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'addToHighscore'), [ref(e.get('_loc4_'), 'playerNum').get(), 4, ref(e.get('_loc12_'), 'techLevel').get()])
                    if truth(logical('&&', binop('>=', ref(e.get('_loc4_'), 'money').get(), ref(e.get('_loc12_'), 'cost').get()), lambda: logical('||', unary('!', ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get()), lambda: ref(e.get('_loc12_'), 'allow_in_demo').get()))):
                        rt.call_ref(ref(ref(e.get('_loc4_'), 'techTree').get(), 'inventTechByID'), [ref(e.get('_loc3_'), '_value').get()])
                        rt.call_ref(ref(ref(e.get('_loc4_'), 'weaponStock').get(), 'activeWeaponByTechName'), [ref(e.get('_loc12_'), 'techName').get()])
                        assign(ref(e.get('_loc4_'), 'money'), '-=', lambda: e.call('Number', [ref(e.get('_loc12_'), 'cost').get()]))
                    raise ASBreak()
                if 0 <= case_23 <= 4:
                    rt.call_ref(ref(ref(e.get('_loc4_'), 'weaponStock').get(), 'reduceWeaponByID'), [ref(e.get('_loc3_'), '_weapon').get(), 1])
                    assign(ref(e.get('_loc4_'), 'preAttackStatus'), '=', lambda: ref(e.get('_loc3_'), '_value').get())
                    assign(ref(e.get('_loc4_'), 'preAttackWeapon'), '=', lambda: rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'weaponStock').get(), 'getWeaponByID'), [ref(e.get('_loc3_'), '_weapon').get()]))
                    if truth(binop('==', ref(ref(e.get('_loc4_'), 'preAttackWeapon').get(), 'weaponName').get(), 'ship')):
                        assign(ref(e.get('_loc4_'), 'shipFrame'), '=', lambda: 2)
                    if truth(binop('==', e.get('_loc4_'), ref(ref(this, 'model').get(), 'human').get())):
                        assign(ref(ref(this, 'model').get(), 'userSelectedCarrier'), '=', lambda: rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'weaponStock').get(), 'getWeaponByID'), [ref(e.get('_loc3_'), '_weapon').get()]))
                    raise ASBreak()
                if 0 <= case_23 <= 5:
                    raise ASBreak()
                if 0 <= case_23 <= 6:
                    assign(e.ref('_loc13_'), '=', lambda: rt.call_ref(ref(ref(e.get('_loc4_'), 'weaponStock').get(), 'getWeaponByID'), [ref(e.get('_loc3_'), '_value').get()]))
                    rt.call_ref(ref(ref(e.get('_loc4_'), 'weaponStock').get(), 'reduceWeaponByID'), [ref(e.get('_loc3_'), '_value').get(), 1])
                    raise ASBreak()
                if 0 <= case_23 <= 7:
                    rt.call_ref(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_leader').get()).get(), 'diplomacyPendingArr').get(), 'push'), [obj({'_leader': ref(e.get('_loc4_'), 'playerNum').get(), '_option': ref(e.get('_loc3_'), '_option').get()})])
                    assign(ref(ref(e.get('_loc4_'), 'diplomacy_offeredLastTurn').get(), ref(e.get('_loc3_'), '_leader').get()), '=', lambda: 2)
                    assign(e.ref('_loc14_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'diplomacy_options_arr').get(), ref(e.get('_loc3_'), '_option').get()).get())
                    if truth(binop('==', ref(e.get('_loc14_'), 0).get(), 'offer')):
                        assign(ref(e.get('_loc4_'), 'money'), '-=', lambda: ref(ref(ref(ref(this, 'model').get(), 'diplomacy_options_arr').get(), ref(e.get('_loc3_'), '_option').get()).get(), 2).get())
                    if truth(binop('<', ref(e.get('_loc3_'), '_option').get(), 3)):
                        assign(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_leader').get()).get(), 'regardArr').get(), ref(e.get('_loc4_'), 'playerNum').get()), '+=', lambda: binop('*', ref(e.get('_loc3_'), '_option').get(), 5))
                        assign(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc4_'), 'playerNum').get()).get(), 'regardArr').get(), ref(e.get('_loc3_'), '_leader').get()), '+=', lambda: binop('*', ref(e.get('_loc3_'), '_option').get(), 5))
                    else:
                        assign(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_leader').get()).get(), 'regardArr').get(), ref(e.get('_loc4_'), 'playerNum').get()), '-=', lambda: ref(e.get('_loc3_'), '_option').get())
                        assign(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc4_'), 'playerNum').get()).get(), 'regardArr').get(), ref(e.get('_loc3_'), '_leader').get()), '-=', lambda: ref(e.get('_loc3_'), '_option').get())
                    raise ASBreak()
                if 0 <= case_23 <= 8:
                    assign(e.ref('_loc15_'), '=', lambda: ref(e.get('_loc3_'), '_arr').get())
                    assign(e.ref('_loc16_'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'diplomacy_options_arr').get(), ref(e.get('_loc15_'), '_option').get()).get(), 1).get())
                    assign(e.ref('_loc17_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'diplomacy_options_arr').get(), ref(e.get('_loc15_'), '_option').get()).get())
                    assign(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_player').get()).get(), 'regardArr').get(), ref(ref(e.get('_loc3_'), '_arr').get(), '_leader').get()), '+=', lambda: ref(ref(ref(this, 'model').get(), 'regard_bonus_table_obj').get(), 'diplomacyBonus').get())
                    assign(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(ref(e.get('_loc3_'), '_arr').get(), '_leader').get()).get(), 'regardArr').get(), ref(e.get('_loc3_'), '_player').get()), '+=', lambda: ref(ref(ref(this, 'model').get(), 'regard_bonus_table_obj').get(), 'diplomacyBonus').get())
                    if truth(binop('==', ref(e.get('_loc17_'), 0).get(), 'offer')):
                        assign(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_player').get()).get(), 'money'), '+=', lambda: ref(e.get('_loc17_'), 2).get())
                        rt.call_ref(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(ref(e.get('_loc3_'), '_arr').get(), '_leader').get()).get(), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'diplomacy', '_msg': 'Diplomacy was accepted.'})])
                    else:
                        if truth(binop('==', ref(e.get('_loc17_'), 0).get(), 'demand')):
                            assign(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(ref(e.get('_loc3_'), '_arr').get(), '_leader').get()).get(), 'money'), '+=', lambda: ref(e.get('_loc17_'), 2).get())
                            assign(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_player').get()).get(), 'money'), '-=', lambda: ref(e.get('_loc17_'), 2).get())
                            rt.call_ref(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(ref(e.get('_loc3_'), '_arr').get(), '_leader').get()).get(), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'diplomacy', '_msg': binop('+', binop('+', 'Diplomacy was accepted. $ ', ref(e.get('_loc17_'), 2).get()), '.000.000 was added to you bank account.')})])
                    rt.call_ref(ref(ref(this, 'model').get(), 'setCeaseFire'), [ref(e.get('_loc3_'), '_player').get(), ref(e.get('_loc15_'), '_leader').get(), e.get('_loc16_')])
                    raise ASBreak()
                if 0 <= case_23 <= 9:
                    assign(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_player').get()).get(), 'regardArr').get(), ref(ref(e.get('_loc3_'), '_arr').get(), '_leader').get()), '-=', lambda: ref(ref(ref(this, 'model').get(), 'regard_bonus_table_obj').get(), 'diplomacyBonus').get())
                    assign(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(ref(e.get('_loc3_'), '_arr').get(), '_leader').get()).get(), 'regardArr').get(), ref(e.get('_loc3_'), '_player').get()), '-=', lambda: ref(ref(ref(this, 'model').get(), 'regard_bonus_table_obj').get(), 'diplomacyBonus').get())
                    rt.call_ref(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(ref(e.get('_loc3_'), '_arr').get(), '_leader').get()).get(), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'diplomacy', '_msg': 'Diplomacy was rejected.'})])
                    assign(e.ref('_loc18_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'diplomacy_options_arr').get(), ref(ref(e.get('_loc3_'), '_arr').get(), '_option').get()).get())
                    if truth(binop('==', ref(e.get('_loc18_'), 0).get(), 'offer')):
                        assign(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(ref(e.get('_loc3_'), '_arr').get(), '_leader').get()).get(), 'money'), '+=', lambda: ref(ref(ref(ref(this, 'model').get(), 'diplomacy_options_arr').get(), ref(ref(e.get('_loc3_'), '_arr').get(), '_option').get()).get(), 2).get())
                    raise ASBreak()
                if 0 <= case_23 <= 10:
                    rt.call_ref(ref(this, 'deactivateAfterBio'), [ref(e.get('_loc3_'), '_plr').get(), ref(e.get('_loc3_'), '_arr').get()])
                    raise ASBreak()
                if 0 <= case_23 <= 11:
                    assign(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_player').get()).get(), 'spy_readiness'), '=', lambda: 0)
            except ASBreak:
                pass
        except ASContinue:
            pass
        except ASBreak:
            break
    rt.call_ref(ref(this, 'updatePlayerVars_3'), [])
    return U

def Presenter_updatePlayerVars_3(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc0_', '_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc14_', '_loc15_', '_loc16_', '_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', 'i'], closure, 'Presenter')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'allUnitsDone_intervalID').get()])
    e.set('_loc2_', 0)
    for key_28 in keys(ref(ref(this, 'model').get(), 'turnResultsArr').get()):
        e.ref('i').set(key_28)
        rt.tick()
        try:
            if truth(binop('>=', e.get('_loc2_'), 50)):
                raise ASBreak()
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'turnResultsArr').get(), e.get('i')).get())
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_player').get()).get())
            if truth(binop('===', assign(e.ref('_loc0_'), '=', lambda: ref(e.get('_loc3_'), '_item').get()), 'produce2')):
                assign(e.ref('_loc5_'), '=', lambda: rt.construct(e.get('Array'), []))
                assign(e.ref('_loc6_'), '=', lambda: ref(e.get('_loc3_'), '_money').get())
                if truth(binop('==', ref(e.get('_loc3_'), '_group').get(), 8)):
                    rt.call_ref(ref(e.get('_loc5_'), 'push'), [ref(ref(e.get('_loc4_'), 'weaponStock').get(), 'antiAir').get()])
                    rt.call_ref(ref(e.get('_loc5_'), 'push'), [ref(ref(e.get('_loc4_'), 'weaponStock').get(), 'antiRocket').get()])
                else:
                    assign(e.ref('_loc8_'), '=', lambda: 0)
                    while truth(binop('<', e.get('_loc8_'), ref(ref(ref(e.get('_loc4_'), 'weaponStock').get(), 'weaponArr').get(), 'length').get())):
                        rt.tick()
                        try:
                            assign(e.ref('_loc7_'), '=', lambda: ref(ref(ref(e.get('_loc4_'), 'weaponStock').get(), 'weaponArr').get(), e.get('_loc8_')).get())
                            if truth(logical('&&', binop('==', ref(e.get('_loc7_'), 'desireGroup').get(), ref(e.get('_loc3_'), '_group').get()), lambda: logical('&&', ref(e.get('_loc7_'), 'active').get(), lambda: binop('<', ref(e.get('_loc7_'), 'cost').get(), e.get('_loc6_'))))):
                                rt.call_ref(ref(e.get('_loc5_'), 'push'), [e.get('_loc7_')])
                            else:
                                if truth(logical('&&', binop('==', ref(e.get('_loc7_'), 'desireGroup').get(), 7), lambda: logical('&&', binop('==', ref(e.get('_loc3_'), '_group').get(), 7), lambda: ref(e.get('_loc7_'), 'active').get()))):
                                    rt.call_ref(ref(e.get('_loc5_'), 'push'), [e.get('_loc7_')])
                            if truth(binop('>', e.get('_loc8_'), 40)):
                                raise ASBreak()
                            assign(e.ref('_loc8_'), '=', lambda: binop('+', e.get('_loc8_'), 1))
                        except ASContinue:
                            pass
                        except ASBreak:
                            break
                assign(e.ref('_loc9_'), '=', lambda: ref(ref(e.get('_loc5_'), 0).get(), 'cost').get())
                assign(e.ref('_loc10_'), '=', lambda: 0)
                while truth(binop('<', e.get('_loc10_'), ref(e.get('_loc5_'), 'lengthl').get())):
                    rt.tick()
                    try:
                        assign(e.ref('_loc9_'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'min'), [e.get('_loc9_'), ref(ref(e.get('_loc5_'), e.get('_loc10_')).get(), 'cost').get()]))
                        if truth(binop('>', e.get('_loc10_'), 30)):
                            raise ASBreak()
                        assign(e.ref('_loc10_'), '=', lambda: binop('+', e.get('_loc10_'), 1))
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
                assign(e.ref('_loc11_'), '=', lambda: 0)
                assign(e.ref('_loc12_'), '=', lambda: False)
                assign(e.ref('_loc13_'), '=', lambda: 0)
                while truth(binop('<', e.get('_loc13_'), ref(e.get('_loc5_'), 'length').get())):
                    rt.tick()
                    try:
                        if truth(logical('||', logical('&&', binop('>=', ref(ref(e.get('_loc5_'), e.get('_loc13_')).get(), 'inStock').get(), ref(ref(ref(ref(this, 'model').get(), 'difficulty_level_specific_vars').get(), 'stock_cap_enm').get(), ref(ref(this, 'model').get(), 'difficulty_level').get()).get()), lambda: binop('==', ref(e.get('_loc4_'), 'playedBy').get(), 'AI')), lambda: logical('&&', binop('>=', ref(ref(e.get('_loc5_'), e.get('_loc13_')).get(), 'inStock').get(), ref(ref(ref(ref(this, 'model').get(), 'difficulty_level_specific_vars').get(), 'stock_cap_plr').get(), ref(ref(this, 'model').get(), 'difficulty_level').get()).get()), lambda: binop('==', ref(e.get('_loc4_'), 'playedBy').get(), 'human')))):
                            rt.call_ref(ref(e.get('_loc5_'), 'splice'), [e.get('_loc13_'), 1])
                        if truth(binop('>=', e.get('_loc13_'), 30)):
                            raise ASBreak()
                        assign(e.ref('_loc13_'), '=', lambda: binop('+', e.get('_loc13_'), 1))
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
                while truth(unary('!', e.get('_loc12_'))):
                    rt.tick()
                    try:
                        assign(e.ref('_loc14_'), '=', lambda: rt.call_ref(ref(ref(ref(this, 'model').get(), 'tools').get(), 'randRange'), [0, binop('-', ref(e.get('_loc5_'), 'length').get(), 1)]))
                        assign(e.ref('_loc7_'), '=', lambda: ref(e.get('_loc5_'), e.get('_loc14_')).get())
                        if truth(unary('!', e.get('_loc7_'))):
                            assign(e.ref('_loc6_'), '=', lambda: 0)
                            raise ASBreak()
                        if truth(binop('==', ref(e.get('_loc5_'), 'length').get(), 0)):
                            assign(e.ref('_loc6_'), '=', lambda: 0)
                            raise ASBreak()
                        if truth(logical('||', logical('&&', binop('<=', ref(e.get('_loc7_'), 'inStock').get(), ref(ref(ref(ref(this, 'model').get(), 'difficulty_level_specific_vars').get(), 'stock_cap_enm').get(), ref(ref(this, 'model').get(), 'difficulty_level').get()).get()), lambda: binop('==', ref(e.get('_loc4_'), 'playedBy').get(), 'AI')), lambda: logical('&&', binop('<=', ref(e.get('_loc7_'), 'inStock').get(), ref(ref(ref(ref(this, 'model').get(), 'difficulty_level_specific_vars').get(), 'stock_cap_plr').get(), ref(ref(this, 'model').get(), 'difficulty_level').get()).get()), lambda: binop('==', ref(e.get('_loc4_'), 'playedBy').get(), 'human')))):
                            if truth(logical('&&', binop('<=', ref(e.get('_loc7_'), 'cost').get(), e.get('_loc6_')), lambda: binop('!=', ref(e.get('_loc7_'), 'desireGroup').get(), 7))):
                                if truth(logical('||', binop('==', ref(e.get('_loc4_'), 'playedBy').get(), 'human'), lambda: logical('||', binop('!=', ref(ref(this, 'model').get(), 'difficulty_level').get(), 0), lambda: logical('&&', binop('!=', ref(e.get('_loc7_'), 'weaponName').get(), 'spy3'), lambda: binop('!=', ref(e.get('_loc7_'), 'weaponName').get(), 'spy4'))))):
                                    assign(e.ref('_loc6_'), '-=', lambda: ref(e.get('_loc7_'), 'cost').get())
                                    assign(ref(e.get('_loc4_'), 'money'), '-=', lambda: ref(e.get('_loc7_'), 'cost').get())
                                    rt.call_ref(ref(e.get('_loc7_'), 'buy'), [])
                                rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'addToHighscore'), [ref(e.get('_loc4_'), 'playerNum').get(), 3, ref(e.get('_loc7_'), 'weaponLevel').get()])
                            else:
                                if truth(binop('==', ref(e.get('_loc7_'), 'desireGroup').get(), 7)):
                                    assign(e.ref('_loc15_'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [binop('/', e.get('_loc6_'), rt.call_ref(ref(ref(ref(this, 'model').get(), 'tools').get(), 'randRange'), [2, 25]))]))
                                    assign(ref(e.get('_loc7_'), 'investment'), '+=', lambda: e.get('_loc15_'))
                                    assign(e.ref('_loc16_'), '=', lambda: 0)
                                    while truth(binop('>=', ref(e.get('_loc7_'), 'investment').get(), ref(e.get('_loc7_'), 'cost').get())):
                                        rt.tick()
                                        try:
                                            assign(e.ref('_loc16_'), '=', lambda: binop('+', e.get('_loc16_'), 1))
                                            rt.call_ref(ref(e.get('_loc7_'), 'buy'), [])
                                            assign(ref(e.get('_loc7_'), 'investment'), '-=', lambda: ref(e.get('_loc7_'), 'cost').get())
                                            if truth(binop('>=', e.get('_loc16_'), 15)):
                                                raise ASBreak()
                                        except ASContinue:
                                            pass
                                        except ASBreak:
                                            break
                                    assign(e.ref('_loc6_'), '-=', lambda: e.get('_loc15_'))
                                    assign(ref(e.get('_loc4_'), 'money'), '-=', lambda: e.get('_loc15_'))
                        if truth(logical('||', logical('&&', binop('!=', ref(e.get('_loc3_'), '_group').get(), 7), lambda: logical('||', binop('<', e.get('_loc6_'), e.get('_loc9_')), lambda: binop('>', e.get('_loc11_'), 30))), lambda: logical('&&', binop('==', ref(e.get('_loc3_'), '_group').get(), 7), lambda: logical('||', binop('>', e.get('_loc11_'), 30), lambda: binop('<=', e.get('_loc6_'), 0))))):
                            assign(ref(e.get('_loc4_'), 'production_money_returned'), '+=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [e.get('_loc6_')]))
                            assign(e.ref('_loc6_'), '=', lambda: 0)
                            assign(e.ref('_loc12_'), '=', lambda: True)
                        if truth(binop('>', e.get('_loc11_'), 30)):
                            assign(ref(e.get('_loc4_'), 'production_money_returned'), '+=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [e.get('_loc6_')]))
                            assign(e.ref('_loc6_'), '=', lambda: 0)
                            assign(e.ref('_loc12_'), '=', lambda: True)
                            raise ASBreak()
                        assign(e.ref('_loc11_'), '=', lambda: binop('+', e.get('_loc11_'), 1))
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
        except ASContinue:
            pass
        except ASBreak:
            break
    rt.call_ref(ref(this, 'updatePlayerVars_4'), [])
    return U

def Presenter_updatePlayerVars_4(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', 'i', 'j', 'k'], closure, 'Presenter')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'allUnitsDone_intervalID').get()])
    for key_29 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_29)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get())
            rt.call_ref(ref(ref(e.get('_loc2_'), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'production', '_msg': ref(ref(e.get('_loc2_'), 'weaponStock').get(), 'boughtMSG').get()})])
            if truth(ref(e.get('_loc2_'), 'production_money_returned').get()):
                rt.call_ref(ref(ref(e.get('_loc2_'), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'production', '_msg': binop('+', binop('+', 'Money returned from production: ', ref(e.get('_loc2_'), 'production_money_returned').get()), '.000.000')})])
            rt.call_ref(ref(ref(e.get('_loc2_'), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'research', '_msg': ref(ref(e.get('_loc2_'), 'techTree').get(), 'shortMSG').get()})])
            if truth(binop('>', ref(e.get('_loc2_'), 'turnBattleCasualties').get(), 0)):
                rt.call_ref(ref(ref(e.get('_loc2_'), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'battle_casualties', '_msg': binop('+', binop('+', 'You LOST ', ref(e.get('_loc2_'), 'turnBattleCasualties').get()), '.000.000 citizens in battle.')})])
            if truth(binop('>', ref(e.get('_loc2_'), 'turnBattleKills').get(), 0)):
                rt.call_ref(ref(ref(e.get('_loc2_'), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'battle_kills', '_msg': binop('+', binop('+', 'You KILLED ', ref(e.get('_loc2_'), 'turnBattleKills').get()), '.000.000 citizens in battle.')})])
            if truth(binop('>', ref(e.get('_loc2_'), 'turnResourcesGained').get(), 0)):
                rt.call_ref(ref(ref(e.get('_loc2_'), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'resourcesGained', '_msg': binop('+', binop('+', 'You GAINED $ ', ref(e.get('_loc2_'), 'turnResourcesGained').get()), '.000.000 from resources')})])
            rt.call_ref(ref(ref(e.get('_loc2_'), 'weaponStock').get(), 'resetBought'), [])
            rt.call_ref(ref(ref(e.get('_loc2_'), 'techTree').get(), 'resetInventedLastTurn'), [])
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_30 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_30)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get())
            for key_31 in keys(ref(e.get('_loc3_'), 'ceaseFireArr').get()):
                e.ref('j').set(key_31)
                rt.tick()
                try:
                    if truth(binop('<=', ref(ref(ref(e.get('_loc3_'), 'ceaseFireArr').get(), e.get('j')).get(), '_turnsLeft').get(), 0)):
                        assign(ref(ref(ref(e.get('_loc3_'), 'ceaseFireArr').get(), e.get('j')).get(), '_turnsLeft'), '=', lambda: 0)
                        assign(ref(ref(ref(e.get('_loc3_'), 'ceaseFireArr').get(), e.get('j')).get(), '_status'), '=', lambda: False)
                    if truth(binop('>', ref(ref(ref(e.get('_loc3_'), 'ceaseFireArr').get(), e.get('j')).get(), '_turnsLeft').get(), 0)):
                        update(ref(ref(ref(e.get('_loc3_'), 'ceaseFireArr').get(), e.get('j')).get(), '_turnsLeft'), -1, False)
                except ASContinue:
                    pass
                except ASBreak:
                    break
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_32 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_32)
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get())
            for key_33 in keys(ref(e.get('_loc4_'), 'cityArr').get()):
                e.ref('j').set(key_33)
                rt.tick()
                try:
                    assign(e.ref('_loc5_'), '=', lambda: ref(ref(e.get('_loc4_'), 'cityArr').get(), e.get('j')).get())
                    assign(ref(e.get('_loc5_'), 'population'), '-=', lambda: ref(e.get('_loc5_'), 'total_battle_casualties').get())
                    for key_34 in keys(ref(e.get('_loc5_'), 'propagandaMin').get()):
                        e.ref('k').set(key_34)
                        rt.tick()
                        try:
                            if truth(binop('<=', ref(e.get('_loc5_'), 'population').get(), 0)):
                                raise ASBreak()
                            assign(ref(e.get('_loc5_'), 'population'), '-=', lambda: ref(ref(e.get('_loc5_'), 'propagandaMin').get(), e.get('k')).get())
                        except ASContinue:
                            pass
                        except ASBreak:
                            break
                    assign(ref(e.get('_loc5_'), 'population'), '+=', lambda: ref(e.get('_loc5_'), 'propagandaPlus').get())
                    assign(ref(e.get('_loc5_'), 'total_battle_casualties'), '=', lambda: 0)
                    assign(ref(e.get('_loc5_'), 'propagandaMinIndex'), '=', lambda: 0)
                    assign(ref(e.get('_loc5_'), 'propagandaMin'), '=', lambda: arr([]))
                    assign(ref(e.get('_loc5_'), 'propagandaPlus'), '=', lambda: 0)
                    rt.call_ref(ref(ref(ref(e.get('_loc5_'), 'image').get(), 'propagandaBeams').get(), 'gotoAndStop'), [1])
                    rt.call_ref(ref(ref(ref(e.get('_loc5_'), 'image').get(), 'propagandaBeams2').get(), 'gotoAndStop'), [1])
                    assign(ref(e.get('_loc5_'), 'battle_loop_casualties'), '=', lambda: 0)
                    assign(ref(e.get('_loc5_'), 'propaganda_exclude'), '=', lambda: False)
                except ASContinue:
                    pass
                except ASBreak:
                    break
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_35 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_35)
        rt.tick()
        try:
            assign(e.ref('_loc6_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get())
            if truth(binop('>', ref(e.get('_loc6_'), 'religion').get(), 100)):
                assign(ref(e.get('_loc6_'), 'religion'), '=', lambda: 100)
            if truth(rt.call_ref(ref(e.get('_global'), 'isNaN'), [ref(e.get('_loc6_'), 'money').get()])):
                assign(ref(e.get('_loc6_'), 'money'), '=', lambda: 10)
            if truth(rt.call_ref(ref(e.get('_global'), 'isNaN'), [ref(e.get('_loc6_'), 'religion').get()])):
                assign(ref(e.get('_loc6_'), 'religion'), '=', lambda: 40)
            assign(ref(e.get('_loc6_'), 'lastAttackedBy_casualties'), '=', lambda: 0)
        except ASContinue:
            pass
        except ASBreak:
            break
    rt.call_ref(ref(this, 'initInterface_2'), [])
    return U

def Presenter_initInterface_1(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'allUnitsDone_intervalID').get()])
    rt.call_ref(ref(this, 'updatePlayerVars_1'), [])
    return U

def Presenter_initInterface_2(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'allUnitsDone_intervalID').get()])
    rt.call_ref(ref(ref(this, 'model').get(), 'resetPlayersForNewturn'), [])
    rt.call_ref(ref(ref(this, 'view').get(), 'changeOver'), ['toInterface'])
    assign(ref(ref(this, 'model').get(), 'cur_sub_launch_num'), '=', lambda: e.get('undefined'))
    return U

def Presenter_check_ch_active(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_str'], ['_loc3_', 'a_str', 'i'], closure, 'Presenter')
    e.set('_loc3_', False)
    for key_36 in keys(ref(ref(this, 'model').get(), 'ch_018').get()):
        e.ref('i').set(key_36)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(ref(this, 'model').get(), 'ch_018').get(), e.get('i')).get(), 'id_str').get(), e.get('a_str'))):
                if truth(ref(ref(ref(ref(this, 'model').get(), 'ch_018').get(), e.get('i')).get(), 'active').get()):
                    assign(e.ref('_loc3_'), '=', lambda: True)
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_37 in keys(ref(ref(this, 'model').get(), 'ch_019').get()):
        e.ref('i').set(key_37)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(ref(this, 'model').get(), 'ch_019').get(), e.get('i')).get(), 'id_str').get(), e.get('a_str'))):
                if truth(ref(ref(ref(ref(this, 'model').get(), 'ch_019').get(), e.get('i')).get(), 'active').get()):
                    assign(e.ref('_loc3_'), '=', lambda: True)
        except ASContinue:
            pass
        except ASBreak:
            break
    if truth(e.get('_loc3_')):
        assign(ref(ref(e.get('_global'), 'model').get(), 'corrupt_higscore'), '=', lambda: True)
        return True
    return U

def Presenter_deactivate_ch(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_str'], ['a_str', 'i'], closure, 'Presenter')
    for key_38 in keys(ref(ref(this, 'model').get(), 'ch_018').get()):
        e.ref('i').set(key_38)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(ref(this, 'model').get(), 'ch_018').get(), e.get('i')).get(), 'id_str').get(), e.get('a_str'))):
                assign(ref(ref(ref(ref(this, 'model').get(), 'ch_018').get(), e.get('i')).get(), 'active'), '=', lambda: False)
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_39 in keys(ref(ref(this, 'model').get(), 'ch_019').get()):
        e.ref('i').set(key_39)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(ref(this, 'model').get(), 'ch_019').get(), e.get('i')).get(), 'id_str').get(), e.get('a_str'))):
                assign(ref(ref(ref(ref(this, 'model').get(), 'ch_019').get(), e.get('i')).get(), 'active'), '=', lambda: False)
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Presenter_explode_all(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i', 'j'], closure, 'Presenter')
    assign(ref(ref(this, 'model').get(), 'explode_all_arr'), '=', lambda: rt.construct(e.get('Array'), []))
    for key_40 in keys(ref(ref(this, 'model').get(), 'activePlayerArr').get()):
        e.ref('i').set(key_40)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'model').get(), 'activePlayerArr').get(), e.get('i')).get(), ref(ref(this, 'model').get(), 'human').get())):
                raise ASBreak()
            for key_41 in keys(ref(ref(ref(ref(this, 'model').get(), 'activePlayerArr').get(), e.get('i')).get(), 'cityArr').get()):
                e.ref('j').set(key_41)
                rt.tick()
                try:
                    assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(ref(ref(this, 'model').get(), 'activePlayerArr').get(), e.get('i')).get(), 'cityArr').get(), e.get('j')).get())
                    if truth(binop('>', ref(e.get('_loc2_'), 'population').get(), 0)):
                        rt.call_ref(ref(ref(ref(this, 'model').get(), 'explode_all_arr').get(), 'push'), [e.get('_loc2_')])
                except ASContinue:
                    pass
                except ASBreak:
                    break
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(ref(this, 'model').get(), 'explode_all_interval_id'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'explode_all_iteration', 1500, True]))
    return U

def Presenter_explode_self(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i', 'j'], closure, 'Presenter')
    assign(ref(ref(this, 'model').get(), 'explode_all_arr'), '=', lambda: rt.construct(e.get('Array'), []))
    for key_42 in keys(ref(ref(this, 'model').get(), 'activePlayerArr').get()):
        e.ref('i').set(key_42)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'model').get(), 'activePlayerArr').get(), e.get('i')).get(), ref(ref(this, 'model').get(), 'human').get())):
                for key_43 in keys(ref(ref(ref(ref(this, 'model').get(), 'activePlayerArr').get(), e.get('i')).get(), 'cityArr').get()):
                    e.ref('j').set(key_43)
                    rt.tick()
                    try:
                        assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(ref(ref(this, 'model').get(), 'activePlayerArr').get(), e.get('i')).get(), 'cityArr').get(), e.get('j')).get())
                        if truth(binop('>', ref(e.get('_loc2_'), 'population').get(), 0)):
                            rt.call_ref(ref(ref(ref(this, 'model').get(), 'explode_all_arr').get(), 'push'), [e.get('_loc2_')])
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(ref(this, 'model').get(), 'explode_all_interval_id'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'explode_all_iteration', 1500, False]))
    return U

def Presenter_explode_all_iteration(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_allDone'], ['_loc3_', 'a_allDone'], closure, 'Presenter')
    if truth(logical('&&', binop('==', ref(ref(ref(this, 'model').get(), 'explode_all_arr').get(), 'length').get(), 0), lambda: e.get('a_allDone'))):
        rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(this, 'model').get(), 'explode_all_interval_id').get()])
        ref(ref(ref(e.get('_global'), 'view').get(), 'battleSrcMC').get(), 'onEnterFrame').delete()
        assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [ref(e.get('_global'), 'presenter').get(), 'allUnitsDone', 2500]))
    else:
        assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'explode_all_arr').get(), 0).get())
        rt.call_ref(ref(ref(e.get('_loc3_'), 'image').get(), 'attachMovie'), ['explosion_warhead_4', 'boom', rt.call_ref(ref(ref(e.get('_loc3_'), 'image').get(), 'getNextHighestDepth'), [])])
        rt.call_ref(ref(e.get('_loc3_'), 'size_and_frame_in_battle'), [ref(e.get('_loc3_'), 'population').get(), True])
        assign(ref(e.get('_loc3_'), 'population'), '=', lambda: 0)
        rt.call_ref(ref(ref(ref(this, 'model').get(), 'explode_all_arr').get(), 'splice'), [0, 1])
    return U

def Presenter_deactivateAfterBio(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['plr_num', 'arr'], ['_loc4_', 'arr', 'i', 'plr_num'], closure, 'Presenter')
    e.set('_loc4_', ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('plr_num')).get())
    assign(ref(e.get('_loc4_'), 'bioloaded'), '=', lambda: True)
    for key_44 in keys(e.get('arr')):
        e.ref('i').set(key_44)
        rt.tick()
        try:
            if truth(ref(ref(e.get('arr'), e.get('i')).get(), '_action').get()):
                rt.call_ref(ref(ref(e.get('_loc4_'), 'bioloadedActionsArr').get(), 'push'), [ref(ref(e.get('arr'), e.get('i')).get(), '_action').get()])
            else:
                if truth(ref(ref(e.get('arr'), e.get('i')).get(), '_stock').get()):
                    rt.call_ref(ref(ref(e.get('_loc4_'), 'bioloadedStockArr').get(), 'push'), [ref(ref(e.get('arr'), e.get('i')).get(), '_weaponName').get()])
                    assign(ref(rt.call_ref(ref(ref(e.get('_loc4_'), 'weaponStock').get(), 'getWeaponByID'), [ref(ref(e.get('arr'), e.get('i')).get(), '_stock').get()]), 'bioloaded'), '=', lambda: True)
                    assign(ref(rt.call_ref(ref(ref(e.get('_loc4_'), 'weaponStock').get(), 'getWeaponByID'), [ref(ref(e.get('arr'), e.get('i')).get(), '_stock').get()]), 'active'), '=', lambda: False)
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Presenter_update_propaganda_plus(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_plr'], ['_loc3_', '_loc4_', '_plr', 'i'], closure, 'Presenter')
    e.set('_loc3_', ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('_plr')).get())
    for key_45 in keys(ref(e.get('_loc3_'), 'cityArr').get()):
        e.ref('i').set(key_45)
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(e.get('_loc3_'), 'cityArr').get(), e.get('i')).get())
            if truth(logical('&&', binop('>', ref(e.get('_loc4_'), 'population').get(), 0), lambda: unary('!', ref(e.get('_loc4_'), 'propaganda_exclude').get()))):
                rt.call_ref(ref(e.get('_loc4_'), 'propagandaPlus_func'), [])
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Presenter_updateSingleCity_byID(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_ID', 'casualties', 'propagandaMin', 'attacker_ID'], ['_ID', '_loc6_', '_loc7_', '_loc8_', 'attacker_ID', 'casualties', 'propagandaMin'], closure, 'Presenter')
    e.set('_loc6_', rt.call_ref(ref(ref(this, 'model').get(), 'getCityByID'), [e.get('_ID')]))
    rt.call_ref(ref(ref(this, 'view').get(), 'updateSingleCity'), [e.get('_loc6_'), e.get('casualties')])
    if truth(e.get('propagandaMin')):
        rt.call_ref(ref(e.get('_loc6_'), 'propagandaMin_func'), [])
        if truth(binop('==', ref(e.get('_loc6_'), 'propagandaMinIndex').get(), 1)):
            assign(e.ref('_loc7_'), '=', lambda: ref(ref(e.get('_loc6_'), 'image').get(), 'propagandaBeams').get())
        else:
            assign(e.ref('_loc7_'), '=', lambda: ref(ref(e.get('_loc6_'), 'image').get(), 'propagandaBeams2').get())
        assign(e.ref('_loc8_'), '=', lambda: rt.construct(e.get('Color'), [e.get('_loc7_')]))
        rt.call_ref(ref(e.get('_loc8_'), 'setTransform'), [ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), e.get('attacker_ID')).get(), 'playerColorTint1').get()])
        rt.call_ref(ref(e.get('_loc7_'), 'gotoAndPlay'), [1])
        if truth(binop('!=', ref(e.get('_loc6_'), 'propagandaMinIndex').get(), 0)):
            rt.call_ref(ref(e.get('_loc7_'), 'gotoAndPlay'), [3])
        rt.call_ref(ref(e.get('_loc6_'), 'updateIMG'), [])
    return U

def Presenter_allow_curAction_approve(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Presenter')
    e.set('_loc2_', False)
    switch_46 = ref(ref(this, 'model').get(), 'userSelectedActionBtn').get()
    case_47 = -1
    if case_47 == -1 and strict_eq(switch_46, 'resources'):
        case_47 = 0
    if case_47 == -1 and strict_eq(switch_46, 'production'):
        case_47 = 1
    if case_47 == -1 and strict_eq(switch_46, 'research'):
        case_47 = 2
    if case_47 == -1 and strict_eq(switch_46, 'religion'):
        case_47 = 3
    if case_47 == -1 and strict_eq(switch_46, 'preAttack'):
        case_47 = 4
    if case_47 == -1 and strict_eq(switch_46, 'attack'):
        case_47 = 5
    if case_47 == -1 and strict_eq(switch_46, 'defense'):
        case_47 = 6
    if case_47 == -1 and strict_eq(switch_46, 'propaganda'):
        case_47 = 7
    if case_47 == -1 and strict_eq(switch_46, 'diplomacy'):
        case_47 = 8
    if case_47 == -1:
        case_47 = -1
    try:
        if 0 <= case_47 <= 0:
            assign(e.ref('_loc2_'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_47 <= 1:
            if truth(binop('>', ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'weaponStock').get(), 'production_money_spent').get(), 0)):
                assign(e.ref('_loc2_'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_47 <= 2:
            if truth(binop('>', ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'techTree').get(), 'researchMoneySpent').get(), 0)):
                assign(e.ref('_loc2_'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_47 <= 3:
            assign(e.ref('_loc2_'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_47 <= 4:
            if truth(logical('&&', binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponName').get(), 'ship'), lambda: binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready'))):
                if truth(binop('==', ref(ref(ref(this, 'model').get(), 'ship_attack_arr').get(), 'length').get(), 3)):
                    assign(e.ref('_loc2_'), '=', lambda: True)
            else:
                if truth(logical('&&', binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready'), lambda: logical('&&', ref(ref(this, 'model').get(), 'userSelectedPayload').get(), lambda: ref(ref(this, 'model').get(), 'userSelectedCity').get()))):
                    assign(e.ref('_loc2_'), '=', lambda: True)
                else:
                    if truth(logical('&&', binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'inactive'), lambda: ref(ref(this, 'model').get(), 'userSelectedCarrier').get())):
                        assign(e.ref('_loc2_'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_47 <= 5:
            if truth(logical('&&', ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), lambda: logical('&&', ref(ref(this, 'model').get(), 'userSelectedCity').get(), lambda: binop('!=', ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'weaponType').get(), 'spy')))):
                assign(e.ref('_loc2_'), '=', lambda: True)
            if truth(logical('&&', ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), lambda: logical('&&', ref(ref(this, 'model').get(), 'userSelectedPlayer').get(), lambda: binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'weaponType').get(), 'spy')))):
                assign(e.ref('_loc2_'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_47 <= 6:
            if truth(ref(ref(this, 'model').get(), 'userSelectedWeapon').get()):
                assign(e.ref('_loc2_'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_47 <= 7:
            if truth(ref(ref(this, 'model').get(), 'userSelectedCity').get()):
                assign(e.ref('_loc2_'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_47 <= 8:
            if truth(ref(ref(this, 'model').get(), 'userSelectedPlayer').get()):
                assign(e.ref('_loc2_'), '=', lambda: True)
    except ASBreak:
        pass
    return e.get('_loc2_')
    return U

def Presenter_doPropaganda(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', 'i'], closure, 'Presenter')
    for key_48 in keys(ref(ref(ref(e.get('_global'), 'model').get(), 'battle').get(), '_activeUnitsArr').get()):
        e.ref('i').set(key_48)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(ref(e.get('_global'), 'model').get(), 'battle').get(), '_activeUnitsArr').get(), e.get('i')).get())
            if truth(binop('==', ref(ref(e.get('_loc2_'), 'obj').get(), '_frame').get(), 'propaganda_2')):
                assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'battle').get(), '_activeUnitsArr').get(), e.get('i')).get(), 'obj').get())
                assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_player').get()).get())
                assign(e.ref('_loc5_'), '=', lambda: ref(ref(rt.call_ref(ref(ref(this, 'model').get(), 'get_playerAB_mc'), [ref(e.get('_loc3_'), '_player').get(), 'propaganda']), 'mc').get(), 'beamMC').get())
                assign(e.ref('_loc6_'), '=', lambda: rt.construct(e.get('Color'), [e.get('_loc5_')]))
                rt.call_ref(ref(e.get('_loc6_'), 'setTransform'), [ref(e.get('_loc4_'), 'playerColorTint1').get()])
                rt.call_ref(ref(this, 'updateSingleCity_byID'), [ref(e.get('_loc3_'), '_targetCity_id').get(), 0, True, ref(e.get('_loc3_'), '_player').get()])
                rt.call_ref(ref(this, 'update_propaganda_plus'), [ref(e.get('_loc3_'), '_player').get()])
                rt.call_ref(ref(e.get('_loc5_'), 'play'), [])
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Presenter_approveAction(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Presenter')
    e.set('_loc2_', rt.call_ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'getNextTurnAction'), []))
    if truth(logical('&&', binop('!=', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), 'production'), lambda: binop('!=', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), 'research'))):
        rt.call_ref(ref(ref(this, 'model').get(), 'setHumanTurnAction'), [])
        assign(ref(ref(this, 'model').get(), 'userSelectedActionBtn'), '=', lambda: e.get('undefined'))
        assign(ref(ref(this, 'model').get(), 'userSelectedStockBtn'), '=', lambda: e.get('undefined'))
    return U

def Presenter_fireDefense(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_plr', 'frm'], ['_loc4_', '_plr', 'frm'], closure, 'Presenter')
    e.set('_loc4_', ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), e.get('_plr')).get())
    rt.call_ref(ref(ref(ref(ref(this, 'view').get(), 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'ab', e.get('_plr')), '_'), ref(e.get('_loc4_'), 'anti_loc').get())).get(), 'gotoAndStop'), [e.get('frm')])
    rt.call_ref(ref(ref(ref(ref(ref(this, 'view').get(), 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'ab', e.get('_plr')), '_'), ref(e.get('_loc4_'), 'anti_loc').get())).get(), 'mc').get(), 'gotoAndStop'), [ref(e.get('_loc4_'), 'religion_code').get()])
    return U

def Presenter_spawn_cities(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc14_', '_loc15_', '_loc16_', '_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', 'i', 'j'], closure, 'Presenter')
    rt.call_ref(ref(ref(this, 'model').get(), 'set_city_position_to_array'), [])
    e.set('_loc2_', 0)
    e.set('_loc3_', 0)
    while truth(binop('<', e.get('_loc3_'), ref(ref(ref(this, 'model').get(), 'playerArr').get(), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('_loc3_')).get())
            assign(e.ref('_loc5_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc5_'), 5)):
                rt.tick()
                try:
                    assign(ref(ref(e.get('_loc4_'), 'cityArr').get(), e.get('_loc5_')), '=', lambda: rt.construct(e.get('City'), [update(e.ref('_loc2_'), 1, False), 100, e.get('_loc4_')]))
                    assign(ref(ref(ref(e.get('_loc4_'), 'cityArr').get(), e.get('_loc5_')).get(), 'soldierWP_obj'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'soldier_waypoints_arr').get(), e.get('_loc3_')).get(), e.get('_loc5_')).get())
                    assign(ref(ref(ref(e.get('_loc4_'), 'cityArr').get(), e.get('_loc5_')).get(), 'tankWP_obj'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'tank_waypoints_arr').get(), e.get('_loc3_')).get(), e.get('_loc5_')).get())
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
    assign(ref(ref(this, 'model').get(), 'soldier_wayPointMC_pos_arr'), '=', lambda: rt.construct(e.get('Array'), []))
    e.set('_loc6_', 0)
    while truth(binop('<', e.get('_loc6_'), 7)):
        rt.tick()
        try:
            assign(ref(ref(ref(this, 'model').get(), 'soldier_wayPointMC_pos_arr').get(), e.get('_loc6_')), '=', lambda: rt.construct(e.get('Array'), []))
            assign(e.ref('_loc7_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc7_'), 7)):
                rt.tick()
                try:
                    assign(ref(ref(ref(ref(this, 'model').get(), 'soldier_wayPointMC_pos_arr').get(), e.get('_loc6_')).get(), e.get('_loc7_')), '=', lambda: obj({'_x': ref(ref(ref(ref(this, 'view').get(), 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'swp', e.get('_loc6_')), '_'), e.get('_loc7_'))).get(), '_x').get(), '_y': ref(ref(ref(ref(this, 'view').get(), 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'swp', e.get('_loc6_')), '_'), e.get('_loc7_'))).get(), '_y').get()}))
                    assign(e.ref('_loc7_'), '=', lambda: binop('+', e.get('_loc7_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            assign(e.ref('_loc6_'), '=', lambda: binop('+', e.get('_loc6_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(ref(this, 'model').get(), 'tank_wayPointMC_pos_arr'), '=', lambda: rt.construct(e.get('Array'), []))
    e.set('_loc8_', 0)
    while truth(binop('<', e.get('_loc8_'), 7)):
        rt.tick()
        try:
            assign(ref(ref(ref(this, 'model').get(), 'tank_wayPointMC_pos_arr').get(), e.get('_loc8_')), '=', lambda: rt.construct(e.get('Array'), []))
            assign(e.ref('_loc9_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc9_'), 7)):
                rt.tick()
                try:
                    assign(ref(ref(ref(ref(this, 'model').get(), 'tank_wayPointMC_pos_arr').get(), e.get('_loc8_')).get(), e.get('_loc9_')), '=', lambda: obj({'_x': ref(ref(ref(ref(this, 'view').get(), 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'twp', e.get('_loc8_')), '_'), e.get('_loc9_'))).get(), '_x').get(), '_y': ref(ref(ref(ref(this, 'view').get(), 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'twp', e.get('_loc8_')), '_'), e.get('_loc9_'))).get(), '_y').get()}))
                    assign(e.ref('_loc9_'), '=', lambda: binop('+', e.get('_loc9_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            assign(e.ref('_loc8_'), '=', lambda: binop('+', e.get('_loc8_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc10_', 0)
    for key_49 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_49)
        rt.tick()
        try:
            assign(e.ref('_loc11_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get())
            assign(e.ref('_loc12_'), '=', lambda: 0)
            if truth(binop('==', ref(e.get('_loc11_'), 'playedBy').get(), 'AI')):
                assign(e.ref('_loc12_'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'difficulty_level_specific_vars').get(), 'enemy_start_population').get(), ref(ref(this, 'model').get(), 'difficulty_level').get()).get())
            else:
                assign(e.ref('_loc12_'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'difficulty_level_specific_vars').get(), 'player_start_population').get(), ref(ref(this, 'model').get(), 'difficulty_level').get()).get())
            assign(e.ref('_loc13_'), '=', lambda: e.get('_loc12_'))
            assign(e.ref('_loc14_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc14_'), ref(ref(e.get('_loc11_'), 'cityArr').get(), 'length').get())):
                rt.tick()
                try:
                    assign(e.ref('_loc15_'), '=', lambda: ref(ref(e.get('_loc11_'), 'cityArr').get(), e.get('_loc14_')).get())
                    assign(e.ref('_loc10_'), '=', lambda: rt.call_ref(ref(ref(ref(this, 'model').get(), 'tools').get(), 'randRange'), [rt.call_ref(ref(e.get('Math'), 'min'), [40, e.get('_loc13_')]), rt.call_ref(ref(e.get('Math'), 'min'), [binop('/', e.get('_loc12_'), 4), e.get('_loc13_')])]))
                    if truth(binop('<', e.get('_loc14_'), binop('-', ref(ref(e.get('_loc11_'), 'cityArr').get(), 'length').get(), 1))):
                        assign(ref(e.get('_loc15_'), 'population'), '=', lambda: e.get('_loc10_'))
                        assign(e.ref('_loc13_'), '-=', lambda: e.get('_loc10_'))
                    else:
                        assign(ref(e.get('_loc15_'), 'population'), '=', lambda: e.get('_loc13_'))
                    assign(e.ref('_loc14_'), '=', lambda: binop('+', e.get('_loc14_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            for key_50 in keys(ref(ref(e.get('_loc11_'), 'weaponStock').get(), 'weaponArr').get()):
                e.ref('j').set(key_50)
                rt.tick()
                try:
                    assign(e.ref('_loc16_'), '=', lambda: ref(ref(ref(e.get('_loc11_'), 'weaponStock').get(), 'weaponArr').get(), e.get('j')).get())
                    if truth(ref(rt.call_ref(ref(ref(e.get('_loc11_'), 'techTree').get(), 'getTechByName'), [ref(e.get('_loc16_'), 'relatedTechName').get()]), 'invented').get()):
                        assign(ref(e.get('_loc16_'), 'active'), '=', lambda: True)
                    else:
                        assign(ref(e.get('_loc16_'), 'active'), '=', lambda: False)
                except ASContinue:
                    pass
                except ASBreak:
                    break
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Presenter_set_player_vars(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', 'i', 'j'], closure, 'Presenter')
    e.set('_loc2_', 0)
    while truth(binop('<', e.get('_loc2_'), ref(ref(ref(this, 'model').get(), 'playerArr').get(), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('_loc2_')).get())
            assign(e.ref('_loc4_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc4_'), 5)):
                rt.tick()
                try:
                    assign(ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')), '=', lambda: ref(ref(ref(ref(ref(this, 'model').get(), 'difficulty_level_specific_vars').get(), 'start_regard_arr').get(), ref(ref(this, 'model').get(), 'difficulty_level').get()).get(), e.get('_loc4_')).get())
                    assign(e.ref('_loc4_'), '=', lambda: binop('+', e.get('_loc4_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            if truth(binop('==', ref(e.get('_loc3_'), 'playedBy').get(), 'AI')):
                assign(ref(e.get('_loc3_'), 'turnMoney'), '=', lambda: assign(ref(e.get('_loc3_'), 'money'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'difficulty_level_specific_vars').get(), 'enemy_start_money').get(), ref(ref(this, 'model').get(), 'difficulty_level').get()).get()))
                assign(ref(e.get('_loc3_'), 'religion'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'difficulty_level_specific_vars').get(), 'enemy_start_religion').get(), ref(ref(this, 'model').get(), 'difficulty_level').get()).get())
                assign(ref(e.get('_loc3_'), 'spy_readiness'), '=', lambda: binop('*', 25, ref(ref(this, 'model').get(), 'difficulty_level').get()))
                assign(ref(e.get('_loc3_'), 'specialization'), '=', lambda: rt.construct(e.get('AI_specialization'), [True]))
                rt.call_ref(ref(ref(e.get('_loc3_'), 'specialization').get(), 'create_desire_arr'), [])
                assign(ref(e.get('_loc3_'), 'desireArr'), '=', lambda: ref(ref(e.get('_loc3_'), 'specialization').get(), 'desireArr').get())
                assign(ref(e.get('_loc3_'), 'primary_enemy'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'get_random_set_enemy'), [e.get('_loc3_')]))
                assign(ref(e.get('_loc3_'), 'secundary_enemy'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'get_random_set_enemy'), [e.get('_loc3_'), ref(e.get('_loc3_'), 'primary_enemy').get()]))
                assign(ref(ref(e.get('_loc3_'), 'regardArr').get(), ref(e.get('_loc3_'), 'primary_enemy').get()), '=', lambda: 45)
                assign(ref(ref(e.get('_loc3_'), 'regardArr').get(), ref(e.get('_loc3_'), 'secundary_enemy').get()), '=', lambda: 50)
                if truth(ref(e.get('_loc3_'), 'special_person').get()):
                    assign(ref(e.get('_loc3_'), 'desireArr'), '=', lambda: arr([0, 0, 0, 0, 1, 1, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 15, 0, 0]))
                if truth(ref(e.get('_loc3_'), 'suicide_person').get()):
                    assign(ref(e.get('_loc3_'), 'desireArr'), '=', lambda: arr([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
            else:
                assign(ref(e.get('_loc3_'), 'turnMoney'), '=', lambda: assign(ref(e.get('_loc3_'), 'money'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'difficulty_level_specific_vars').get(), 'player_start_money').get(), ref(ref(this, 'model').get(), 'difficulty_level').get()).get()))
                assign(ref(e.get('_loc3_'), 'religion'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'difficulty_level_specific_vars').get(), 'player_start_money').get(), ref(ref(this, 'model').get(), 'difficulty_level').get()).get())
                assign(ref(e.get('_loc3_'), 'spy_readiness'), '=', lambda: binop('-', 100, binop('*', 25, ref(ref(this, 'model').get(), 'difficulty_level').get())))
                assign(ref(e.get('_loc3_'), 'desireArr'), '=', lambda: arr([3, 2, 2, 15, 2, 3, 2, 15, 2, 3, 2, 15, 2, 3, 2, 15, 1, 2, 2, 2, 1, 15, 0, 2, 15, 15]))
            rt.call_ref(ref(e.get('_loc3_'), 'setChars'), [])
            assign(ref(e.get('_loc3_'), 'ceaseFireArr'), '=', lambda: arr([obj({'_status': False, '_turnsLeft': 0}), obj({'_status': False, '_turnsLeft': 0}), obj({'_status': False, '_turnsLeft': 0}), obj({'_status': False, '_turnsLeft': 0}), obj({'_status': False, '_turnsLeft': 0})]))
            assign(ref(e.get('_loc3_'), 'spy_readiness'), '=', lambda: 25)
            assign(ref(e.get('_loc3_'), 'mapSide'), '=', lambda: e.get('_loc2_'))
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    if truth(binop('==', ref(ref(this, 'model').get(), 'difficulty_level').get(), 2)):
        for key_51 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
            e.ref('i').set(key_51)
            rt.tick()
            try:
                assign(e.ref('_loc5_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get())
                if truth(binop('!=', e.get('_loc5_'), ref(ref(this, 'model').get(), 'human').get())):
                    assign(ref(e.get('_loc5_'), 'primary_enemy'), '=', lambda: 0)
                    assign(ref(e.get('_loc5_'), 'secundary_enemy'), '=', lambda: 0)
                    assign(ref(ref(e.get('_loc5_'), 'regardArr').get(), 0), '=', lambda: rt.call_ref(ref(ref(ref(this, 'model').get(), 'tools').get(), 'randRange'), [15, 60]))
                    rt.call_ref(ref(ref(e.get('_loc5_'), 'techTree').get(), 'invent_below_tech_level'), [2])
                    rt.call_ref(ref(ref(e.get('_loc5_'), 'weaponStock').get(), 'set_wpn_stock_per_level'), [1, 2])
                    rt.call_ref(ref(ref(e.get('_loc5_'), 'weaponStock').get(), 'set_wpn_stock_per_level'), [2, 1])
                else:
                    rt.call_ref(ref(ref(e.get('_loc5_'), 'techTree').get(), 'invent_below_tech_level'), [1])
            except ASContinue:
                pass
            except ASBreak:
                break
    if truth(binop('==', ref(ref(this, 'model').get(), 'difficulty_level').get(), 1)):
        for key_52 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
            e.ref('i').set(key_52)
            rt.tick()
            try:
                assign(e.ref('_loc6_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get())
                if truth(binop('!=', e.get('_loc6_'), ref(ref(this, 'model').get(), 'human').get())):
                    rt.call_ref(ref(ref(e.get('_loc6_'), 'techTree').get(), 'invent_below_tech_level'), [1])
                    rt.call_ref(ref(ref(e.get('_loc6_'), 'weaponStock').get(), 'set_wpn_stock_per_level'), [1, 1])
                else:
                    rt.call_ref(ref(ref(e.get('_loc6_'), 'techTree').get(), 'invent_below_tech_level'), [1])
                    rt.call_ref(ref(ref(e.get('_loc6_'), 'weaponStock').get(), 'set_wpn_stock_per_level'), [1, 1])
            except ASContinue:
                pass
            except ASBreak:
                break
    if truth(binop('==', ref(ref(this, 'model').get(), 'difficulty_level').get(), 0)):
        for key_53 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
            e.ref('i').set(key_53)
            rt.tick()
            try:
                assign(e.ref('_loc7_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get())
                if truth(binop('==', e.get('_loc7_'), ref(ref(this, 'model').get(), 'human').get())):
                    rt.call_ref(ref(ref(e.get('_loc7_'), 'techTree').get(), 'invent_below_tech_level'), [2])
                    rt.call_ref(ref(ref(e.get('_loc7_'), 'weaponStock').get(), 'set_easy_wpn_stock'), [])
                else:
                    rt.call_ref(ref(ref(e.get('_loc7_'), 'techTree').get(), 'invent_below_tech_level'), [1])
            except ASContinue:
                pass
            except ASBreak:
                break
    for key_54 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_54)
        rt.tick()
        try:
            assign(e.ref('_loc8_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get())
            if truth(ref(e.get('_loc8_'), 'special_person').get()):
                assign(ref(e.get('_loc8_'), 'regardArr'), '=', lambda: arr([70, 70, 70, 70, 70]))
                for key_55 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
                    e.ref('j').set(key_55)
                    rt.tick()
                    try:
                        assign(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('j')).get(), 'regardArr').get(), ref(e.get('_loc8_'), 'playerNum').get()), '=', lambda: 70)
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Presenter_citySelect(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['city'], ['city'], closure, 'Presenter')
    rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_select_city'])
    if truth(logical('&&', binop('>', ref(e.get('city'), 'population').get(), 0), lambda: logical('&&', binop('!=', ref(e.get('city'), 'plr').get(), ref(ref(this, 'model').get(), 'human').get()), lambda: logical('||', unary('!', ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'ceaseFireArr').get(), ref(ref(e.get('city'), 'plr').get(), 'playerNum').get()).get(), '_status').get()), lambda: binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'weaponType').get(), 'spy'))))):
        if truth(logical('&&', binop('==', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), 'attack'), lambda: ref(ref(this, 'model').get(), 'userSelectedStockBtn').get())):
            rt.call_ref(ref(ref(this, 'model').get(), 'deselectCities'), [ref(ref(this, 'model').get(), 'userSelectedActionBtn').get()])
            assign(ref(ref(this, 'model').get(), 'userSelectedCity'), '=', lambda: e.get('city'))
            assign(ref(ref(this, 'model').get(), 'userSelectedPlayer'), '=', lambda: ref(e.get('city'), 'plr').get())
            assign(ref(ref(e.get('city'), 'selectionObj').get(), 'attack'), '=', lambda: True)
        if truth(logical('&&', binop('==', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), 'preAttack'), lambda: binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready'))):
            if truth(logical('&&', binop('!=', ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponName').get(), 'ship'), lambda: ref(ref(this, 'model').get(), 'userSelectedStockBtn').get())):
                rt.call_ref(ref(ref(this, 'model').get(), 'deselectCities'), [ref(ref(this, 'model').get(), 'userSelectedActionBtn').get()])
                assign(ref(ref(this, 'model').get(), 'userSelectedCity'), '=', lambda: e.get('city'))
                assign(ref(ref(this, 'model').get(), 'userSelectedPlayer'), '=', lambda: ref(e.get('city'), 'plr').get())
                assign(ref(ref(e.get('city'), 'selectionObj').get(), 'preAttack'), '=', lambda: True)
                assign(ref(ref(e.get('city'), 'selectionObj').get(), 'preAttackWeapon'), '=', lambda: ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponName').get())
            else:
                if truth(binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponName').get(), 'ship')):
                    rt.call_ref(ref(this, 'addToShipSelection'), [e.get('city')])
        if truth(binop('==', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), 'propaganda')):
            rt.call_ref(ref(ref(this, 'model').get(), 'deselectCities'), [ref(ref(this, 'model').get(), 'userSelectedActionBtn').get()])
            assign(ref(ref(this, 'model').get(), 'userSelectedCity'), '=', lambda: e.get('city'))
            assign(ref(ref(this, 'model').get(), 'userSelectedPlayer'), '=', lambda: ref(e.get('city'), 'plr').get())
            assign(ref(ref(e.get('city'), 'selectionObj').get(), 'propaganda'), '=', lambda: True)
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'updateView'), [])
    if truth(ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'ceaseFireArr').get(), ref(ref(e.get('city'), 'plr').get(), 'playerNum').get()).get(), '_status').get()):
        assign(ref(ref(e.get('_global'), 'view_interface').get(), 'infoLine'), '=', lambda: 'ceaseFire')
    if truth(binop('==', ref(e.get('city'), 'plr').get(), ref(ref(this, 'model').get(), 'human').get())):
        assign(ref(ref(e.get('_global'), 'view_interface').get(), 'infoLine'), '=', lambda: 'citySelf')
    return U

def Presenter_addToShipSelection(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['city'], ['_loc3_', 'city'], closure, 'Presenter')
    e.set('_loc3_', False)
    if truth(logical('&&', ref(ref(this, 'model').get(), 'userSelectedShipCityPlrNum').get(), lambda: binop('==', ref(ref(e.get('city'), 'plr').get(), 'playerNum').get(), ref(ref(this, 'model').get(), 'userSelectedShipCityPlrNum').get()))):
        assign(e.ref('_loc3_'), '=', lambda: True)
    else:
        if truth(binop('==', ref(ref(ref(this, 'model').get(), 'ship_attack_arr').get(), 'length').get(), 0)):
            assign(e.ref('_loc3_'), '=', lambda: True)
            assign(ref(ref(this, 'model').get(), 'userSelectedShipCityPlrNum'), '=', lambda: ref(ref(e.get('city'), 'plr').get(), 'playerNum').get())
    if truth(logical('||', binop('==', ref(e.get('city'), 'plr').get(), ref(ref(this, 'model').get(), 'human').get()), lambda: ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'ceaseFireArr').get(), ref(ref(e.get('city'), 'plr').get(), 'playerNum').get()).get(), '_status').get())):
        assign(e.ref('_loc3_'), '=', lambda: False)
    if truth(e.get('_loc3_')):
        if truth(binop('>=', ref(ref(ref(this, 'model').get(), 'ship_attack_arr').get(), 'length').get(), 3)):
            rt.call_ref(ref(ref(ref(ref(ref(this, 'model').get(), 'ship_attack_arr').get(), 0).get(), 'city').get(), 'deSelectForShipAttack'), [])
            update(ref(ref(ref(ref(ref(this, 'model').get(), 'ship_attack_arr').get(), 0).get(), 'wpn').get(), 'inUse'), -1, False)
            rt.call_ref(ref(ref(ref(this, 'model').get(), 'ship_attack_arr').get(), 'splice'), [0, 1])
        rt.call_ref(ref(ref(ref(this, 'model').get(), 'ship_attack_arr').get(), 'push'), [obj({'city': ref(e.get('city'), 'cityID').get(), 'wpn': ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'weaponID').get()})])
        update(ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'inUse'), 1, False)
        rt.call_ref(ref(e.get('city'), 'selectForShipAttack'), [])
        assign(ref(ref(this, 'model').get(), 'userSelectedStockBtn'), '=', lambda: e.get('undefined'))
        assign(ref(ref(this, 'model').get(), 'userSelectedPlayer'), '=', lambda: ref(e.get('city'), 'plr').get())
        assign(ref(ref(this, 'model').get(), 'userSelectedWeapon'), '=', lambda: e.get('undefined'))
        assign(ref(ref(this, 'model').get(), 'userSelectedPayload'), '=', lambda: e.get('undefined'))
    return U

def Presenter_removeShipSelection(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_ta'], ['_loc3_', '_loc4_', '_ta', 'i'], closure, 'Presenter')
    e.set('_loc3_', logical('||', ref(e.get('_ta'), 'ship_attack_arr').get(), lambda: ref(ref(this, 'model').get(), 'ship_attack_arr').get()))
    for key_56 in keys(e.get('_loc3_')):
        e.ref('i').set(key_56)
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(e.get('_loc3_'), e.get('i')).get())
            rt.call_ref(ref(rt.call_ref(ref(ref(this, 'model').get(), 'getCityByID'), [ref(e.get('_loc4_'), 'city').get()]), 'removeSelection'), ['ship'])
            assign(ref(rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'weaponStock').get(), 'getWeaponByID'), [ref(e.get('_loc4_'), 'wpn').get()]), 'inUse'), '=', lambda: binop('-', ref(rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'weaponStock').get(), 'getWeaponByID'), [ref(e.get('_loc4_'), 'wpn').get()]), 'inUse').get(), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Presenter_remove_played_sound_objects(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Presenter')
    e.set('_loc2_', 0)
    while truth(binop('<', e.get('_loc2_'), ref(ref(ref(this, 'model').get(), 'playedSounds_arr').get(), 'length').get())):
        rt.tick()
        try:
            ref(ref(ref(ref(this, 'model').get(), 'playedSounds_arr').get(), e.get('_loc2_')).get(), 'soundObj').delete()
            rt.call_ref(ref(ref(ref(ref(ref(this, 'model').get(), 'playedSounds_arr').get(), e.get('_loc2_')).get(), 'mc').get(), 'removeMovieClip'), [])
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(ref(this, 'model').get(), 'playedSounds_arr'), '=', lambda: rt.construct(e.get('Array'), []))
    return U

def Presenter_stop_continues_sound_objects(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Presenter')
    e.set('_loc2_', 1)
    while truth(binop('<', e.get('_loc2_'), 20)):
        rt.tick()
        try:
            rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'playing_ambient_sound_arr').get(), e.get('_loc2_')).get(), 'stop'), [])
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Presenter_get_soldier_positions(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['city'], ['_loc3_', '_loc4_', '_loc5_', '_loc6_', 'city', 'i'], closure, 'Presenter')
    e.set('_loc3_', rt.construct(e.get('Object'), []))
    e.set('_loc4_', ref(e.get('city'), 'soldierWP_obj').get())
    if truth(binop('!=', ref(ref(e.get('_loc4_'), '_wpArr').get(), 0).get(), 0)):
        assign(ref(e.get('_loc3_'), '_wpArr'), '=', lambda: rt.construct(e.get('Array'), []))
        assign(e.ref('_loc5_'), '=', lambda: 0)
        while truth(binop('<', e.get('_loc5_'), ref(ref(e.get('_loc4_'), '_wpArr').get(), 'length').get())):
            rt.tick()
            try:
                rt.call_ref(ref(ref(e.get('_loc3_'), '_wpArr').get(), 'push'), [ref(ref(ref(ref(this, 'model').get(), 'soldier_wayPointMC_pos_arr').get(), ref(ref(e.get('city'), 'plr').get(), 'playerNum').get()).get(), ref(ref(e.get('_loc4_'), '_wpArr').get(), e.get('_loc5_')).get()).get()])
                assign(e.ref('_loc5_'), '=', lambda: binop('+', e.get('_loc5_'), 1))
            except ASContinue:
                pass
            except ASBreak:
                break
    for key_57 in keys(ref(ref(this, 'model').get(), 'soldier_fire_positions').get()):
        e.ref('i').set(key_57)
        rt.tick()
        try:
            assign(e.ref('_loc6_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'soldier_fire_positions').get(), e.get('i')).get())
            if truth(binop('==', ref(e.get('_loc6_'), '_pos').get(), ref(e.get('_loc4_'), '_endPos').get())):
                assign(ref(e.get('_loc3_'), '_endPosArr'), '=', lambda: ref(e.get('_loc6_'), '_arr').get())
                raise ASBreak()
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc3_')
    return U

def Presenter_get_tank_positions(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['city'], ['_loc3_', '_loc4_', '_loc5_', '_loc6_', 'city', 'i'], closure, 'Presenter')
    e.set('_loc3_', rt.construct(e.get('Object'), []))
    e.set('_loc4_', ref(e.get('city'), 'tankWP_obj').get())
    if truth(binop('!=', ref(ref(e.get('_loc4_'), '_wpArr').get(), 0).get(), 0)):
        assign(ref(e.get('_loc3_'), '_wpArr'), '=', lambda: rt.construct(e.get('Array'), []))
        assign(e.ref('_loc5_'), '=', lambda: 0)
        while truth(binop('<', e.get('_loc5_'), ref(ref(e.get('_loc4_'), '_wpArr').get(), 'length').get())):
            rt.tick()
            try:
                rt.call_ref(ref(ref(e.get('_loc3_'), '_wpArr').get(), 'push'), [ref(ref(ref(ref(this, 'model').get(), 'tank_wayPointMC_pos_arr').get(), ref(ref(e.get('city'), 'plr').get(), 'playerNum').get()).get(), ref(ref(e.get('_loc4_'), '_wpArr').get(), e.get('_loc5_')).get()).get()])
                assign(e.ref('_loc5_'), '=', lambda: binop('+', e.get('_loc5_'), 1))
            except ASContinue:
                pass
            except ASBreak:
                break
    for key_58 in keys(ref(ref(this, 'model').get(), 'tank_fire_positions').get()):
        e.ref('i').set(key_58)
        rt.tick()
        try:
            assign(e.ref('_loc6_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'tank_fire_positions').get(), e.get('i')).get())
            if truth(binop('==', ref(e.get('_loc6_'), '_pos').get(), ref(e.get('_loc4_'), '_endPos').get())):
                assign(ref(e.get('_loc3_'), '_endPosArr'), '=', lambda: ref(e.get('_loc6_'), '_arr').get())
                raise ASBreak()
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc3_')
    return U

def Presenter_btnIsSetAction(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_nm'], ['_nm'], closure, 'Presenter')
    if truth(logical('||', binop('==', e.get('_nm'), ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnAction_1').get(), 'action').get()), lambda: binop('==', e.get('_nm'), ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnAction_2').get(), 'action').get()))):
        return True
    return False
    return U

def Presenter_addToHighscore(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_plr', 'a_index', 'a_multiplier'], ['_loc5_', '_loc6_', 'a_index', 'a_multiplier', 'a_plr'], closure, 'Presenter')
    if truth(logical('||', unary('!', e.get('a_multiplier')), lambda: rt.call_ref(ref(e.get('_global'), 'isNaN'), [e.get('a_multiplier')]))):
        assign(e.ref('a_multiplier'), '=', lambda: 1)
    e.set('_loc5_', arr([151, 1213, 1001, 2001, 3002, 200, 101, 910]))
    e.set('_loc6_', binop('*', rt.call_ref(ref(e.get('Math'), 'round'), [binop('+', ref(e.get('_loc5_'), e.get('a_index')).get(), rt.call_ref(ref(ref(ref(this, 'model').get(), 'tools').get(), 'randRange'), [0, 50]))]), e.get('a_multiplier')))
    assign(e.ref('_loc6_'), '*=', lambda: ref(ref(e.get('_global'), 'model').get(), 'difficulty_level').get())
    if truth(logical('&&', unary('!', rt.call_ref(ref(e.get('_global'), 'isNaN'), [e.get('_loc6_')])), lambda: e.get('_loc6_'))):
        assign(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('a_plr')).get(), 'score'), '+=', lambda: e.get('_loc6_'))
    return U

def Presenter_brighter_hex_by_steps(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_curHex', 'a_steps'], ['_loc4_', '_loc5_', 'a_curHex', 'a_steps'], closure, 'Presenter')
    e.set('_loc4_', e.get('a_curHex'))
    e.set('_loc5_', 0)
    while truth(binop('<', e.get('_loc5_'), e.get('a_steps'))):
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'brighter_hex'), [e.get('_loc4_')]))
            assign(e.ref('_loc5_'), '=', lambda: binop('+', e.get('_loc5_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc4_')
    return U

def Presenter_brighter_hex(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_curHex'], ['_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', 'a_curHex'], closure, 'Presenter')
    e.set('_loc3_', arr(['9', 'A', 'B', 'C', 'D', 'E', 'F']))
    e.set('_loc4_', '0x')
    e.set('_loc5_', 2)
    while truth(binop('<', e.get('_loc5_'), 9)):
        rt.tick()
        try:
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(e.get('a_curHex'), 'charAt'), [e.get('_loc5_')]))
            if truth(logical('&&', unary('!', rt.call_ref(ref(e.get('_global'), 'isNaN'), [e.call('Number', [e.get('_loc6_')])])), lambda: binop('<', e.call('Number', [e.get('_loc6_')]), 9))):
                assign(e.ref('_loc6_'), '=', lambda: binop('+', e.get('_loc6_'), 1))
            else:
                if truth(binop('!=', e.get('_loc6_'), 'F')):
                    assign(e.ref('_loc7_'), '=', lambda: 0)
                    while truth(binop('<', e.get('_loc7_'), ref(e.get('_loc3_'), 'length').get())):
                        rt.tick()
                        try:
                            if truth(binop('==', ref(e.get('_loc3_'), e.get('_loc7_')).get(), e.get('_loc6_'))):
                                assign(e.ref('_loc6_'), '=', lambda: ref(e.get('_loc3_'), binop('+', e.get('_loc7_'), 1)).get())
                                raise ASBreak()
                            assign(e.ref('_loc7_'), '=', lambda: binop('+', e.get('_loc7_'), 1))
                        except ASContinue:
                            pass
                        except ASBreak:
                            break
            assign(e.ref('_loc4_'), '+=', lambda: e.get('_loc6_'))
            assign(e.ref('_loc5_'), '=', lambda: binop('+', e.get('_loc5_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc4_')
    return U

def Presenter_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter')
    pass

def register(rt):
    rt.define('Presenter', 'Sub_presenter', Presenter_fields, {'Presenter': ASFunction(Presenter_Presenter), 'updateMiniMap': ASFunction(Presenter_updateMiniMap), 'setOutlineColor': ASFunction(Presenter_setOutlineColor), 'btn_pressed_new_game': ASFunction(Presenter_btn_pressed_new_game), 'initBattle': ASFunction(Presenter_initBattle), 'add_to_playerAB_position_arr': ASFunction(Presenter_add_to_playerAB_position_arr), 'set_playerAB_position_arr_action_names': ASFunction(Presenter_set_playerAB_position_arr_action_names), 'get_preAB_mc': ASFunction(Presenter_get_preAB_mc), 'allUnitsDone': ASFunction(Presenter_allUnitsDone), 'showLastActionBuildings': ASFunction(Presenter_showLastActionBuildings), 'endBattle': ASFunction(Presenter_endBattle), 'doTR_from_battle': ASFunction(Presenter_doTR_from_battle), 'killPlayer': ASFunction(Presenter_killPlayer), 'updatePlayerVars_1': ASFunction(Presenter_updatePlayerVars_1), 'updatePlayerVars_2': ASFunction(Presenter_updatePlayerVars_2), 'updatePlayerVars_3': ASFunction(Presenter_updatePlayerVars_3), 'updatePlayerVars_4': ASFunction(Presenter_updatePlayerVars_4), 'initInterface_1': ASFunction(Presenter_initInterface_1), 'initInterface_2': ASFunction(Presenter_initInterface_2), 'check_ch_active': ASFunction(Presenter_check_ch_active), 'deactivate_ch': ASFunction(Presenter_deactivate_ch), 'explode_all': ASFunction(Presenter_explode_all), 'explode_self': ASFunction(Presenter_explode_self), 'explode_all_iteration': ASFunction(Presenter_explode_all_iteration), 'deactivateAfterBio': ASFunction(Presenter_deactivateAfterBio), 'update_propaganda_plus': ASFunction(Presenter_update_propaganda_plus), 'updateSingleCity_byID': ASFunction(Presenter_updateSingleCity_byID), 'allow_curAction_approve': ASFunction(Presenter_allow_curAction_approve), 'doPropaganda': ASFunction(Presenter_doPropaganda), 'approveAction': ASFunction(Presenter_approveAction), 'fireDefense': ASFunction(Presenter_fireDefense), 'spawn_cities': ASFunction(Presenter_spawn_cities), 'set_player_vars': ASFunction(Presenter_set_player_vars), 'citySelect': ASFunction(Presenter_citySelect), 'addToShipSelection': ASFunction(Presenter_addToShipSelection), 'removeShipSelection': ASFunction(Presenter_removeShipSelection), 'remove_played_sound_objects': ASFunction(Presenter_remove_played_sound_objects), 'stop_continues_sound_objects': ASFunction(Presenter_stop_continues_sound_objects), 'get_soldier_positions': ASFunction(Presenter_get_soldier_positions), 'get_tank_positions': ASFunction(Presenter_get_tank_positions), 'btnIsSetAction': ASFunction(Presenter_btnIsSetAction), 'addToHighscore': ASFunction(Presenter_addToHighscore), 'brighter_hex_by_steps': ASFunction(Presenter_brighter_hex_by_steps), 'brighter_hex': ASFunction(Presenter_brighter_hex)}, {'model': ASFunction(Presenter___get__model), 'view': ASFunction(Presenter___get__view)}, {'model': ASFunction(Presenter___set__model), 'view': ASFunction(Presenter___set__view)})
