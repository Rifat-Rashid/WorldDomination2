# Generated from __Packages/Presenter_gameMenu.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Presenter_gameMenu_Presenter_gameMenu(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_gameMenu')
    return U

def Presenter_gameMenu_init_main_interface(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc0_', '_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_'], closure, 'Presenter_gameMenu')
    e.set('_loc2_', rt.construct(e.get('Array'), [0, 1, 2, 3, 4]))
    assign(ref(ref(e.get('_global'), 'model').get(), 'playerArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(ref(e.get('_global'), 'model').get(), 'activePlayerArr'), '=', lambda: rt.construct(e.get('Array'), []))
    e.set('_loc3_', assign(ref(ref(e.get('_global'), 'model').get(), 'human'), '=', lambda: rt.construct(e.get('Player'), ['human', 0, arr([0, 0])])))
    assign(ref(e.get('_loc3_'), 'religion_code'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'building_num_to_religion_code'), [ref(ref(this, 'model').get(), 'selected_building').get()]))
    assign(ref(e.get('_loc3_'), 'playerColor'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'color_name_by_id'), [binop('-', ref(ref(this, 'model').get(), 'player_color').get(), 1)]))
    assign(ref(e.get('_loc3_'), 'playerColorTint1'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'wd_colors').get(), binop('+', 'color_', rt.call_ref(ref(ref(this, 'model').get(), 'color_code_by_id'), [binop('-', ref(ref(this, 'model').get(), 'player_color').get(), 1)]))).get())
    assign(ref(e.get('_loc3_'), 'hexColorTint'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'color_hex_by_id'), [binop('-', ref(ref(this, 'model').get(), 'player_color').get(), 1)]))
    assign(ref(e.get('_loc3_'), 'hexColorTint_str'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'color_hexStr_by_id'), [binop('-', ref(ref(this, 'model').get(), 'player_color').get(), 1)]))
    assign(ref(e.get('_loc3_'), 'buildingSet_id'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'get_religion_buildingSet_by_code'), [ref(e.get('_loc3_'), 'religion_code').get()]))
    assign(ref(e.get('_loc3_'), 'alive'), '=', lambda: True)
    assign(ref(e.get('_loc3_'), 'playerNum'), '=', lambda: 0)
    rt.call_ref(ref(ref(e.get('_loc3_'), 'shortMSG_arr').get(), 'push'), [obj({'_type': 'welcome', '_msg': 'Welcome commander. Please select 2 action from the left menu.'})])
    assign(ref(ref(e.get('_global'), 'model').get(), 'difficulty_level'), '=', lambda: ref(ref(this, 'model').get(), 'difficulty').get())
    rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), 'push'), [e.get('_loc3_')])
    rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'activePlayerArr').get(), 'push'), [e.get('_loc3_')])
    rt.call_ref(ref(this, 'remove_value_from_array'), [e.get('_loc2_'), binop('-', ref(ref(this, 'model').get(), 'player_color').get(), 1)])
    e.set('_loc4_', False)
    e.set('_loc5_', False)
    e.set('_loc6_', 0)
    while truth(binop('<', e.get('_loc6_'), ref(ref(ref(this, 'model').get(), 'selected_leader_arr').get(), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc7_'), '=', lambda: assign(ref(ref(e.get('_global'), 'model').get(), binop('+', 'comp', binop('+', e.get('_loc6_'), 1))), '=', lambda: rt.construct(e.get('Player'), ['AI', binop('+', e.get('_loc6_'), 1), arr([0, 0])])))
            assign(e.ref('_loc8_'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'get_leader_by_ID'), [ref(ref(ref(this, 'model').get(), 'selected_leader_arr').get(), e.get('_loc6_')).get()]))
            assign(ref(e.get('_loc7_'), 'religion_code'), '=', lambda: ref(e.get('_loc8_'), '_religion').get())
            assign(ref(e.get('_loc7_'), 'buildingSet_id'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'get_religion_buildingSet_by_code'), [ref(e.get('_loc8_'), '_religion').get()]))
            assign(e.ref('_loc9_'), '=', lambda: ref(e.get('_loc2_'), rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [0, binop('-', ref(e.get('_loc2_'), 'length').get(), 1)])).get())
            assign(ref(e.get('_loc7_'), 'playerColor'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'color_name_by_id'), [e.get('_loc9_')]))
            rt.call_ref(ref(this, 'remove_value_from_array'), [e.get('_loc2_'), e.get('_loc9_')])
            assign(ref(e.get('_loc7_'), 'playerColorTint1'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'wd_colors').get(), binop('+', 'color_', rt.call_ref(ref(ref(this, 'model').get(), 'color_code_by_id'), [e.get('_loc9_')]))).get())
            assign(ref(e.get('_loc7_'), 'hexColorTint'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'color_hex_by_id'), [e.get('_loc9_')]))
            assign(ref(e.get('_loc7_'), 'hexColorTint_str'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'color_hexStr_by_id'), [e.get('_loc9_')]))
            assign(ref(e.get('_loc7_'), 'faceFrame'), '=', lambda: ref(e.get('_loc8_'), '_frame').get())
            assign(ref(e.get('_loc7_'), 'alive'), '=', lambda: True)
            assign(ref(e.get('_loc7_'), 'playerNum'), '=', lambda: binop('+', e.get('_loc6_'), 1))
            rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), 'push'), [e.get('_loc7_')])
            rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'activePlayerArr').get(), 'push'), [e.get('_loc7_')])
            if truth(logical('&&', binop('==', rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [1, 3]), 2), lambda: unary('!', e.get('_loc4_')))):
                assign(ref(e.get('_loc7_'), 'special_person'), '=', lambda: True)
                assign(e.ref('_loc4_'), '=', lambda: True)
            else:
                if truth(logical('&&', binop('==', rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [1, 3]), 2), lambda: unary('!', e.get('_loc5_')))):
                    assign(ref(e.get('_loc7_'), 'suicide_person'), '=', lambda: True)
                    assign(e.ref('_loc5_'), '=', lambda: True)
            assign(e.ref('_loc6_'), '=', lambda: binop('+', e.get('_loc6_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'set_player_vars'), [])
    rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'spawn_cities'), [])
    rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'updateMiniMap'), [])
    rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'updateView'), [])
    rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'decisionPoints').get(), 'set_points_to_difficulty'), [ref(ref(e.get('_global'), 'model').get(), 'difficulty_level').get()])
    rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'updateView'), [])
    rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'setMapFrames'), [])
    rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'resetActionBuildings'), [])
    rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'updateCities'), [])
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'update_top_plrColor'), [])
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'update_color_dots'), [])
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'reset_leader_stat_bars'), [])
    assign(ref(ref(ref(e.get('_global'), 'view_interface').get(), 'actionTube1').get(), 'associatedTA'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'turnAction_1').get())
    assign(ref(ref(ref(e.get('_global'), 'view_interface').get(), 'actionTube2').get(), 'associatedTA'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'turnAction_2').get())
    rt.call_ref(ref(ref(this, 'view').get(), 'hide_gameMenu'), [])
    assign(ref(ref(ref(e.get('_global'), 'view_interface').get(), 'interfaceMC').get(), '_visible'), '=', lambda: True)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'updateView'), [])
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'debug_automate_func'), [])
    rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'updateCities'), [])
    rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'changeOver'), ['toInterface'])
    return U

def Presenter_gameMenu_remove_value_from_array(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['arr', 'a_value'], ['_loc4_', 'a_value', 'arr'], closure, 'Presenter_gameMenu')
    e.set('_loc4_', 0)
    while truth(binop('<', e.get('_loc4_'), ref(e.get('arr'), 'length').get())):
        rt.tick()
        try:
            if truth(binop('==', ref(e.get('arr'), e.get('_loc4_')).get(), e.get('a_value'))):
                rt.call_ref(ref(e.get('arr'), 'splice'), [e.get('_loc4_'), 1])
            assign(e.ref('_loc4_'), '=', lambda: binop('+', e.get('_loc4_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def f_1(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_gameMenu').get(), 'btn_pressed_difficulty'), [1])
    return U

def f_2(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_gameMenu').get(), 'btn_pressed_difficulty'), [2])
    return U

def f_3(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_gameMenu').get(), 'btn_pressed_difficulty'), [3])
    return U

def f_4(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_gameMenu').get(), 'btn_pressed_color'), [ref(this, 'num').get()])
    return U

def f_5(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_gameMenu').get(), 'btn_pressed_building'), [ref(this, 'num').get()])
    return U

def f_6(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_gameMenu').get(), 'btn_pressed_leader_from_list'), [ref(this, 'num').get()])
    return U

def f_7(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_gameMenu').get(), 'btn_rollOver_leader'), [ref(this, 'num').get()])
    return U

def f_8(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(ref(ref(e.get('_global'), 'view_gameMenu').get(), 'src_MC').get(), 'leaderText').get(), 'text'), '=', lambda: '')
    return U

def f_9(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_gameMenu').get(), 'btn_pressed_selected_leader'), [ref(this, 'num').get()])
    return U

def f_10(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_gameMenu').get(), 'btn_pressed_leader_arrow_left'), [])
    return U

def f_11(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_gameMenu').get(), 'btn_pressed_leader_arrow_right'), [])
    return U

def f_12(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_gameMenu').get(), 'btn_pressed_start'), [])
    return U

def f_13(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btn_pressed_full'), [])
    return U

def f_14(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btn_pressed_full'), [])
    return U

def f_15(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('getURL', ['http://www.arcadetown.com', '_blank'])
    return U

def f_16(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('getURL', ['http://www.agame.com', '_blank'])
    return U

def f_17(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('getURL', ['http://www.youdagames.com', '_blank'])
    return U

def f_18(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('getURL', ['http://www.youdagames.com/shop/', '_blank'])
    return U

def f_19(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPressed_option'), ['music', True])
    rt.call_ref(ref(ref(ref(e.get('_level0'), 'gameMenu').get(), 'switch39').get(), 'play'), [])
    return U

def Presenter_gameMenu_set_btn_func(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_'], closure, 'Presenter_gameMenu')
    assign(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'btn1').get(), 'onPress'), '=', lambda: ASFunction(f_1, e))
    assign(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'btn2').get(), 'onPress'), '=', lambda: ASFunction(f_2, e))
    assign(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'btn3').get(), 'onPress'), '=', lambda: ASFunction(f_3, e))
    e.set('_loc2_', 1)
    while truth(binop('<', e.get('_loc2_'), 6)):
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'colorBtn', e.get('_loc2_'))).get())
            assign(ref(e.get('_loc3_'), 'num'), '=', lambda: e.get('_loc2_'))
            assign(ref(e.get('_loc3_'), 'onPress'), '=', lambda: ASFunction(f_4, e))
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc4_', 1)
    while truth(binop('<', e.get('_loc4_'), 6)):
        rt.tick()
        try:
            assign(e.ref('_loc5_'), '=', lambda: ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'buildingBtn', e.get('_loc4_'))).get())
            assign(ref(e.get('_loc5_'), 'num'), '=', lambda: e.get('_loc4_'))
            assign(ref(e.get('_loc5_'), 'onPress'), '=', lambda: ASFunction(f_5, e))
            assign(e.ref('_loc4_'), '=', lambda: binop('+', e.get('_loc4_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc6_', 1)
    while truth(binop('<', e.get('_loc6_'), 7)):
        rt.tick()
        try:
            assign(e.ref('_loc7_'), '=', lambda: ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'BTN_allLeaders_screen', e.get('_loc6_'))).get())
            assign(ref(e.get('_loc7_'), 'num'), '=', lambda: e.get('_loc6_'))
            assign(ref(e.get('_loc7_'), 'onPress'), '=', lambda: ASFunction(f_6, e))
            assign(ref(e.get('_loc7_'), 'onRollOver'), '=', lambda: ASFunction(f_7, e))
            assign(ref(e.get('_loc7_'), 'onRollOut'), '=', lambda: ASFunction(f_8, e))
            assign(e.ref('_loc6_'), '=', lambda: binop('+', e.get('_loc6_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc8_', 1)
    while truth(binop('<', e.get('_loc8_'), 5)):
        rt.tick()
        try:
            assign(e.ref('_loc9_'), '=', lambda: ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'BTN_selectedLeader_screen', e.get('_loc8_'))).get())
            assign(ref(e.get('_loc9_'), 'num'), '=', lambda: e.get('_loc8_'))
            assign(ref(e.get('_loc9_'), 'onPress'), '=', lambda: ASFunction(f_9, e))
            assign(e.ref('_loc8_'), '=', lambda: binop('+', e.get('_loc8_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'btn_player_list_left').get(), 'onPress'), '=', lambda: ASFunction(f_10, e))
    assign(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'btn_player_list_right').get(), 'onPress'), '=', lambda: ASFunction(f_11, e))
    assign(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'btn_start').get(), 'onPress'), '=', lambda: ASFunction(f_12, e))
    if truth(unary('!', ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get())):
        assign(ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'demo_MC').get(), 'btn_full').get(), 'onPress'), '=', lambda: ASFunction(f_13, e))
    if truth(ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get()):
        assign(ref(ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'demo_MC').get(), 'txtMC_full').get(), 'txt').get(), 'text'), '=', lambda: 'FULL VERSION')
        assign(ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'demo_MC').get(), 'btn_full').get(), 'onPress'), '=', lambda: ASFunction(f_14, e))
        assign(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'arcade_town_logo').get(), 'onPress'), '=', lambda: ASFunction(f_15, e))
        assign(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'agame_logo').get(), 'onPress'), '=', lambda: ASFunction(f_16, e))
        if truth(logical('||', binop('==', rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'get_demo_version_name'), []), 'Totallygame'), lambda: logical('||', binop('==', rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'get_demo_version_name'), []), 'Affiliates'), lambda: binop('==', rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'get_demo_version_name'), []), 'NewGrounds')))):
            assign(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'youda_logo').get(), 'onPress'), '=', lambda: ASFunction(f_17, e))
            assign(ref(ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'demo_MC').get(), 'txtMC_more').get(), 'txt').get(), 'text'), '=', lambda: 'MORE GAMES')
            assign(ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'demo_MC').get(), 'btn_more').get(), 'onPress'), '=', lambda: ASFunction(f_18, e))
        else:
            assign(ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'demo_MC').get(), 'scrn_more').get(), '_visible'), '=', lambda: False)
            assign(ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'demo_MC').get(), 'btn_more').get(), '_visible'), '=', lambda: False)
    else:
        assign(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'demo_MC').get(), '_visible'), '=', lambda: False)
    assign(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'soundBtn').get(), 'onPress'), '=', lambda: ASFunction(f_19, e))
    return e.get('undefined')
    return U

def Presenter_gameMenu_initialize_gameMenu(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_gameMenu')
    rt.call_ref(ref(this, 'btn_pressed_difficulty'), [2])
    rt.call_ref(ref(this, 'btn_pressed_color'), [rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [1, 5])])
    if truth(unary('!', ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get())):
        rt.call_ref(ref(this, 'btn_pressed_building'), [rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [1, 5])])
    else:
        rt.call_ref(ref(this, 'btn_pressed_building'), [2])
    rt.call_ref(ref(this, 'set_btn_func'), [])
    rt.call_ref(ref(this, 'set_visble_leaders_list_arr'), [])
    rt.call_ref(ref(this, 'update_selected_leaders'), [True])
    rt.call_ref(ref(this, 'update_leader_list'), [True])
    rt.call_ref(ref(this, 'update_leader_list'), [])
    rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'setMapFrames'), [])
    return U

def Presenter_gameMenu_btn_pressed_building(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['a_nr'], closure, 'Presenter_gameMenu')
    if truth(logical('||', unary('!', ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get()), lambda: logical('||', binop('==', e.get('a_nr'), 1), lambda: binop('==', e.get('a_nr'), 2)))):
        rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_acceptAction_btn'])
        assign(ref(ref(this, 'model').get(), 'selected_building'), '=', lambda: e.get('a_nr'))
        assign(ref(ref(this, 'view').get(), 'active_building_btn'), '=', lambda: e.get('a_nr'))
        rt.call_ref(ref(this, 'active_start_btn'), [])
    else:
        rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_select_stock'])
    return e.get('undefined')
    return U

def Presenter_gameMenu_btn_pressed_difficulty(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['a_nr'], closure, 'Presenter_gameMenu')
    rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_actionBtn_on'])
    assign(ref(ref(this, 'model').get(), 'difficulty'), '=', lambda: binop('-', e.get('a_nr'), 1))
    assign(ref(ref(this, 'view').get(), 'active_difficulty_btn'), '=', lambda: e.get('a_nr'))
    rt.call_ref(ref(this, 'active_start_btn'), [])
    return e.get('undefined')
    return U

def Presenter_gameMenu_btn_pressed_color(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['a_nr'], closure, 'Presenter_gameMenu')
    rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_acceptAction_btn'])
    assign(ref(ref(this, 'model').get(), 'player_color'), '=', lambda: e.get('a_nr'))
    assign(ref(ref(this, 'view').get(), 'active_color_btn'), '=', lambda: e.get('a_nr'))
    rt.call_ref(ref(this, 'active_start_btn'), [])
    return e.get('undefined')
    return U

def Presenter_gameMenu_btn_pressed_leader_from_list(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['a_nr'], closure, 'Presenter_gameMenu')
    rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_acceptAction_btn'])
    rt.call_ref(ref(this, 'add_leader_to_selection'), [rt.call_ref(ref(this, 'btn_num_to_leader_num'), [e.get('a_nr')])])
    rt.call_ref(ref(this, 'active_start_btn'), [])
    return e.get('undefined')
    return U

def Presenter_gameMenu_btn_pressed_selected_leader(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['a_nr'], closure, 'Presenter_gameMenu')
    rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_select_stock'])
    rt.call_ref(ref(this, 'remove_selected_leader'), [binop('-', e.get('a_nr'), 1)])
    rt.call_ref(ref(this, 'active_start_btn'), [])
    return e.get('undefined')
    return U

def Presenter_gameMenu_btn_pressed_start(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_gameMenu')
    rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_open_tube'])
    if truth(logical('&&', ref(this, 'allow_game_start').get(), lambda: unary('!', ref(ref(e.get('_global'), 'model').get(), 'game_initiated').get()))):
        assign(ref(ref(e.get('_global'), 'model').get(), 'game_initiated'), '=', lambda: True)
        rt.call_ref(ref(this, 'init_main_interface'), [])
    return e.get('undefined')
    return U

def Presenter_gameMenu___get__allow_game_start(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_gameMenu')
    if truth(logical('&&', unary('!', ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get()), lambda: logical('&&', binop('>', ref(ref(ref(this, 'model').get(), 'selected_leader_arr').get(), 'length').get(), 0), lambda: logical('&&', ref(ref(this, 'model').get(), 'selected_building').get(), lambda: logical('&&', binop('!=', ref(ref(this, 'model').get(), 'difficulty').get(), e.get('undefined')), lambda: ref(ref(this, 'model').get(), 'player_color').get()))))):
        return True
    if truth(logical('&&', ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get(), lambda: logical('&&', binop('>', ref(ref(ref(this, 'model').get(), 'selected_leader_arr').get(), 'length').get(), 2), lambda: logical('&&', ref(ref(this, 'model').get(), 'selected_building').get(), lambda: logical('&&', binop('!=', ref(ref(this, 'model').get(), 'difficulty').get(), e.get('undefined')), lambda: ref(ref(this, 'model').get(), 'player_color').get()))))):
        return True
    return False
    return U

def Presenter_gameMenu_active_start_btn(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_gameMenu')
    if truth(ref(this, 'allow_game_start').get()):
        rt.call_ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'scrn_start').get(), 'gotoAndStop'), [2])
    else:
        rt.call_ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'scrn_start').get(), 'gotoAndStop'), [1])
    return U

def Presenter_gameMenu_remove_selected_leader(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_arr_index'], ['a_arr_index'], closure, 'Presenter_gameMenu')
    rt.call_ref(ref(ref(ref(this, 'model').get(), 'selected_leader_arr').get(), 'splice'), [e.get('a_arr_index'), 1])
    rt.call_ref(ref(this, 'update_leader_panel'), [])
    return U

def Presenter_gameMenu_add_leader_to_selection(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['a_nr'], closure, 'Presenter_gameMenu')
    if truth(logical('&&', unary('!', rt.call_ref(ref(this, 'allowed_demo_religion'), [e.get('a_nr')])), lambda: ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get())):
        return e.get('undefined')
    if truth(logical('&&', unary('!', rt.call_ref(ref(this, 'is_selected_leader'), [e.get('a_nr')])), lambda: binop('<', ref(ref(ref(this, 'model').get(), 'selected_leader_arr').get(), 'length').get(), 4))):
        rt.call_ref(ref(ref(ref(this, 'model').get(), 'selected_leader_arr').get(), 'push'), [e.get('a_nr')])
    rt.call_ref(ref(this, 'update_leader_panel'), [])
    return U

def Presenter_gameMenu_is_selected_leader(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['_loc3_', 'a_nr'], closure, 'Presenter_gameMenu')
    e.set('_loc3_', 0)
    while truth(binop('<', e.get('_loc3_'), ref(ref(ref(this, 'model').get(), 'selected_leader_arr').get(), 'length').get())):
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'model').get(), 'selected_leader_arr').get(), e.get('_loc3_')).get(), e.get('a_nr'))):
                return True
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return False
    return U

def Presenter_gameMenu_btn_num_to_leader_num(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['a_nr'], closure, 'Presenter_gameMenu')
    return ref(ref(ref(this, 'model').get(), 'visible_leader_list_arr').get(), binop('-', e.get('a_nr'), 1)).get()
    return U

def Presenter_gameMenu_update_leader_panel(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_gameMenu')
    rt.call_ref(ref(this, 'set_visble_leaders_list_arr'), [])
    rt.call_ref(ref(this, 'update_selected_leaders'), [])
    rt.call_ref(ref(this, 'update_leader_list'), [])
    return U

def Presenter_gameMenu_set_visble_leaders_list_arr(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Presenter_gameMenu')
    assign(ref(ref(this, 'model').get(), 'visible_leader_list_arr'), '=', lambda: arr([]))
    e.set('_loc2_', 0)
    while truth(binop('<', e.get('_loc2_'), 7)):
        rt.tick()
        try:
            if truth(binop('>', binop('+', ref(ref(this, 'model').get(), 'leader_list_start_num').get(), e.get('_loc2_')), 18)):
                rt.call_ref(ref(ref(ref(this, 'model').get(), 'visible_leader_list_arr').get(), 'push'), [binop('-', binop('-', e.get('_loc2_'), binop('-', 18, ref(ref(this, 'model').get(), 'leader_list_start_num').get())), 1)])
            else:
                rt.call_ref(ref(ref(ref(this, 'model').get(), 'visible_leader_list_arr').get(), 'push'), [binop('+', ref(ref(this, 'model').get(), 'leader_list_start_num').get(), e.get('_loc2_'))])
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Presenter_gameMenu_update_selected_leaders(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_init'], ['_loc3_', '_loc4_', 'a_init'], closure, 'Presenter_gameMenu')
    if truth(e.get('a_init')):
        assign(e.ref('_loc3_'), '=', lambda: 1)
        while truth(binop('<', e.get('_loc3_'), 5)):
            rt.tick()
            try:
                rt.call_ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'leaderScrn', e.get('_loc3_'))).get(), 'gotoAndStop'), ['leaderLife'])
                rt.call_ref(ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'leaderScrn', e.get('_loc3_'))).get(), 'aliveMC').get(), 'gotoAndStop'), [20])
                assign(ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'leaderScrn', e.get('_loc3_'))).get(), 'deadMC').get(), '_visible'), '=', lambda: False)
                assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
            except ASContinue:
                pass
            except ASBreak:
                break
        return e.get('undefined')
    e.set('_loc4_', 1)
    while truth(binop('<', e.get('_loc4_'), 5)):
        rt.tick()
        try:
            rt.call_ref(ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'leaderScrn', e.get('_loc4_'))).get(), 'aliveMC').get(), 'gotoAndStop'), [20])
            rt.call_ref(ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'leaderScrn', e.get('_loc4_'))).get(), 'aliveMC').get(), 'gotoAndStop'), [ref(rt.call_ref(ref(ref(this, 'model').get(), 'get_leader_by_ID'), [ref(ref(ref(this, 'model').get(), 'selected_leader_arr').get(), binop('-', e.get('_loc4_'), 1)).get()]), '_frame').get()])
            if truth(rt.call_ref(ref(ref(this, 'model').get(), 'get_leader_by_ID'), [ref(ref(ref(this, 'model').get(), 'selected_leader_arr').get(), binop('-', e.get('_loc4_'), 1)).get()])):
                rt.call_ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'btnCancel', e.get('_loc4_'))).get(), 'gotoAndStop'), [2])
            else:
                rt.call_ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'btnCancel', e.get('_loc4_'))).get(), 'gotoAndStop'), [1])
            assign(e.ref('_loc4_'), '=', lambda: binop('+', e.get('_loc4_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('undefined')
    return U

def Presenter_gameMenu_update_leader_list(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_init'], ['_loc3_', '_loc4_', 'a_init'], closure, 'Presenter_gameMenu')
    if truth(e.get('a_init')):
        assign(e.ref('_loc3_'), '=', lambda: 1)
        while truth(binop('<', e.get('_loc3_'), 7)):
            rt.tick()
            try:
                rt.call_ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'allLeaderScreen', e.get('_loc3_'))).get(), 'gotoAndStop'), ['leaderLife'])
                rt.call_ref(ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'allLeaderScreen', e.get('_loc3_'))).get(), 'aliveMC').get(), 'gotoAndStop'), [binop('+', ref(ref(ref(this, 'model').get(), 'visible_leader_list_arr').get(), binop('-', e.get('_loc3_'), 1)).get(), 1)])
                assign(ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'allLeaderScreen', e.get('_loc3_'))).get(), 'deadMC').get(), '_visible'), '=', lambda: False)
                assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
            except ASContinue:
                pass
            except ASBreak:
                break
        return e.get('undefined')
    e.set('_loc4_', 1)
    while truth(binop('<', e.get('_loc4_'), 7)):
        rt.tick()
        try:
            rt.call_ref(ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'allLeaderScreen', e.get('_loc4_'))).get(), 'aliveMC').get(), 'gotoAndStop'), [binop('+', ref(ref(ref(this, 'model').get(), 'visible_leader_list_arr').get(), binop('-', e.get('_loc4_'), 1)).get(), 1)])
            if truth(rt.call_ref(ref(this, 'is_selected_leader'), [ref(ref(ref(this, 'model').get(), 'visible_leader_list_arr').get(), binop('-', e.get('_loc4_'), 1)).get()])):
                assign(ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'allLeaderScreen', e.get('_loc4_'))).get(), 'aliveMC').get(), '_alpha'), '=', lambda: 20)
            else:
                assign(ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'allLeaderScreen', e.get('_loc4_'))).get(), 'aliveMC').get(), '_alpha'), '=', lambda: 100)
            if truth(ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get()):
                if truth(unary('!', rt.call_ref(ref(this, 'allowed_demo_religion'), [ref(ref(ref(this, 'model').get(), 'visible_leader_list_arr').get(), binop('-', e.get('_loc4_'), 1)).get()]))):
                    assign(ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'allLeaderScreen', e.get('_loc4_'))).get(), 'aliveMC').get(), '_alpha'), '=', lambda: 50)
                    rt.call_ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'full_version_leader_mc_', e.get('_loc4_'))).get(), 'gotoAndStop'), [2])
                else:
                    rt.call_ref(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), binop('+', 'full_version_leader_mc_', e.get('_loc4_'))).get(), 'gotoAndStop'), [1])
            assign(e.ref('_loc4_'), '=', lambda: binop('+', e.get('_loc4_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('undefined')
    return U

def Presenter_gameMenu_allowed_demo_religion(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_num'], ['_loc3_', 'a_num'], closure, 'Presenter_gameMenu')
    e.set('_loc3_', rt.call_ref(ref(ref(this, 'model').get(), 'get_leader_by_ID'), [e.get('a_num')]))
    if truth(logical('||', binop('==', ref(e.get('_loc3_'), '_religion').get(), 'chr'), lambda: binop('==', ref(e.get('_loc3_'), '_religion').get(), 'bhu'))):
        return True
    return False
    return U

def Presenter_gameMenu_btn_pressed_leader_arrow_right(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Presenter_gameMenu')
    e.set('_loc2_', ref(ref(this, 'model').get(), 'leader_list_start_num').get())
    if truth(binop('>', e.get('_loc2_'), 18)):
        assign(ref(ref(this, 'model').get(), 'leader_list_start_num'), '=', lambda: 0)
    else:
        update(ref(ref(this, 'model').get(), 'leader_list_start_num'), 1, False)
    rt.call_ref(ref(this, 'update_leader_panel'), [])
    return U

def Presenter_gameMenu_btn_pressed_leader_arrow_left(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Presenter_gameMenu')
    e.set('_loc2_', ref(ref(this, 'model').get(), 'leader_list_start_num').get())
    if truth(binop('<', e.get('_loc2_'), 1)):
        assign(ref(ref(this, 'model').get(), 'leader_list_start_num'), '=', lambda: 18)
    else:
        update(ref(ref(this, 'model').get(), 'leader_list_start_num'), -1, False)
    rt.call_ref(ref(this, 'update_leader_panel'), [])
    return U

def Presenter_gameMenu_btn_rollOver_leader(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['a_nr'], closure, 'Presenter_gameMenu')
    assign(ref(ref(ref(ref(this, 'view').get(), 'src_MC').get(), 'leaderText').get(), 'text'), '=', lambda: ref(rt.call_ref(ref(ref(this, 'model').get(), 'get_leader_by_ID'), [rt.call_ref(ref(this, 'btn_num_to_leader_num'), [e.get('a_nr')])]), '_name').get())
    return U

def Presenter_gameMenu_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_gameMenu')
    pass

def register(rt):
    rt.define('Presenter_gameMenu', None, Presenter_gameMenu_fields, {'Presenter_gameMenu': ASFunction(Presenter_gameMenu_Presenter_gameMenu), 'init_main_interface': ASFunction(Presenter_gameMenu_init_main_interface), 'remove_value_from_array': ASFunction(Presenter_gameMenu_remove_value_from_array), 'set_btn_func': ASFunction(Presenter_gameMenu_set_btn_func), 'initialize_gameMenu': ASFunction(Presenter_gameMenu_initialize_gameMenu), 'btn_pressed_building': ASFunction(Presenter_gameMenu_btn_pressed_building), 'btn_pressed_difficulty': ASFunction(Presenter_gameMenu_btn_pressed_difficulty), 'btn_pressed_color': ASFunction(Presenter_gameMenu_btn_pressed_color), 'btn_pressed_leader_from_list': ASFunction(Presenter_gameMenu_btn_pressed_leader_from_list), 'btn_pressed_selected_leader': ASFunction(Presenter_gameMenu_btn_pressed_selected_leader), 'btn_pressed_start': ASFunction(Presenter_gameMenu_btn_pressed_start), 'active_start_btn': ASFunction(Presenter_gameMenu_active_start_btn), 'remove_selected_leader': ASFunction(Presenter_gameMenu_remove_selected_leader), 'add_leader_to_selection': ASFunction(Presenter_gameMenu_add_leader_to_selection), 'is_selected_leader': ASFunction(Presenter_gameMenu_is_selected_leader), 'btn_num_to_leader_num': ASFunction(Presenter_gameMenu_btn_num_to_leader_num), 'update_leader_panel': ASFunction(Presenter_gameMenu_update_leader_panel), 'set_visble_leaders_list_arr': ASFunction(Presenter_gameMenu_set_visble_leaders_list_arr), 'update_selected_leaders': ASFunction(Presenter_gameMenu_update_selected_leaders), 'update_leader_list': ASFunction(Presenter_gameMenu_update_leader_list), 'allowed_demo_religion': ASFunction(Presenter_gameMenu_allowed_demo_religion), 'btn_pressed_leader_arrow_right': ASFunction(Presenter_gameMenu_btn_pressed_leader_arrow_right), 'btn_pressed_leader_arrow_left': ASFunction(Presenter_gameMenu_btn_pressed_leader_arrow_left), 'btn_rollOver_leader': ASFunction(Presenter_gameMenu_btn_rollOver_leader)}, {'allow_game_start': ASFunction(Presenter_gameMenu___get__allow_game_start)}, {})
