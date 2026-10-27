# Generated from __Packages/View_interface.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def f_1(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    return U

def f_2(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPress'), [ref(ref(this, '_btnObj').get(), 'index_in_arr').get()])
    return U

def f_3(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnRoll_on'), [ref(ref(this, '_btnObj').get(), 'index_in_arr').get()])
    return U

def f_4(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnRoll_on'), [unary('-', 1)])
    return U

def f_5(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPress'), [ref(ref(this, '_btnObj').get(), 'index_in_arr').get()])
    return U

def f_6(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnRoll_on'), [ref(ref(this, '_btnObj').get(), 'index_in_arr').get()])
    return U

def f_7(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnRoll_off'), [unary('-', 1)])
    return U

def f_8(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPressed_tube'), [ref(this, '_btnObj').get()])
    return U

def f_9(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPressed_tube'), [ref(this, '_btnObj').get()])
    return U

def f_10(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPressed_option'), [ref(ref(this, '_obj').get(), 'option').get()])
    return U

def f_11(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPressed_option'), [ref(ref(this, '_obj').get(), 'option').get()])
    return U

def f_12(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPressed_scroll_MSG'), ['up'])
    return U

def f_13(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPressed_scroll_MSG'), ['down'])
    return U

def f_14(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(binop('!=', ref(ref(e.get('_global'), 'model').get(), 'userSelectedActionBtn').get(), 'diplomacy')):
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPress'), [8])
    if truth(logical('&&', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), 1).get(), 'alive').get(), lambda: unary('!', ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'ceaseFireArr').get(), 1).get(), '_status').get()))):
        assign(ref(ref(e.get('_global'), 'model').get(), 'userSelectedDiplomacyLeader'), '=', lambda: 1)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'updateView'), [])
    return U

def f_15(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(binop('!=', ref(ref(e.get('_global'), 'model').get(), 'userSelectedActionBtn').get(), 'diplomacy')):
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPress'), [8])
    if truth(logical('&&', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), 2).get(), 'alive').get(), lambda: unary('!', ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'ceaseFireArr').get(), 2).get(), '_status').get()))):
        assign(ref(ref(e.get('_global'), 'model').get(), 'userSelectedDiplomacyLeader'), '=', lambda: 2)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'updateView'), [])
    return U

def f_16(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(binop('!=', ref(ref(e.get('_global'), 'model').get(), 'userSelectedActionBtn').get(), 'diplomacy')):
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPress'), [8])
    if truth(logical('&&', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), 3).get(), 'alive').get(), lambda: unary('!', ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'ceaseFireArr').get(), 3).get(), '_status').get()))):
        assign(ref(ref(e.get('_global'), 'model').get(), 'userSelectedDiplomacyLeader'), '=', lambda: 3)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'updateView'), [])
    return U

def f_17(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(binop('!=', ref(ref(e.get('_global'), 'model').get(), 'userSelectedActionBtn').get(), 'diplomacy')):
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPress'), [8])
    if truth(logical('&&', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), 4).get(), 'alive').get(), lambda: unary('!', ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'ceaseFireArr').get(), 4).get(), '_status').get()))):
        assign(ref(ref(e.get('_global'), 'model').get(), 'userSelectedDiplomacyLeader'), '=', lambda: 4)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'updateView'), [])
    return U

def f_18(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'roll_over_stat'), ['regard', ref(this, 'num').get()])
    rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'view_interface').get(), 'interfaceMC').get(), binop('+', binop('+', 'leaderStar_roll_', ref(this, 'num').get()), '1')).get(), 'play'), [])
    return U

def f_19(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(e.get('_global'), 'view_interface').get(), 'infoLine'), '=', lambda: 'null')
    return U

def f_20(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'roll_over_stat'), ['population'])
    rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'view_interface').get(), 'interfaceMC').get(), binop('+', binop('+', 'leaderStar_roll_', ref(this, 'num').get()), '2')).get(), 'play'), [])
    return U

def f_21(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(e.get('_global'), 'view_interface').get(), 'infoLine'), '=', lambda: 'null')
    return U

def f_22(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(e.get('_global'), 'model').get(), 'userSelectedActionBtn'), '=', lambda: 'help')
    assign(ref(ref(e.get('_global'), 'model').get(), 'userSelectedHelpTopic'), '=', lambda: 'help_index')
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'updateView'), [])
    return U

def f_23(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(ref(ref(e.get('_global'), 'model').get(), 'fullscreen').get()):
        assign(ref(ref(e.get('_global'), 'model').get(), 'fullscreen'), '=', lambda: False)
        e.call('fscommand', ['fullscreen', 'false'])
    else:
        assign(ref(ref(e.get('_global'), 'model').get(), 'fullscreen'), '=', lambda: True)
        e.call('fscommand', ['fullscreen', 'true'])
    return U

def View_interface_View_interface(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_interfaceMC'], ['_interfaceMC', '_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_'], closure, 'View_interface')
    assign(ref(ref(e.get('_interfaceMC'), 'btn1').get(), 'onPress'), '=', lambda: ASFunction(f_1, e))
    assign(ref(this, 'interfaceMC'), '=', lambda: e.get('_interfaceMC'))
    assign(ref(this, 'stockRequirements_list'), '=', lambda: rt.construct(e.get('StockRequirements_list'), []))
    assign(ref(this, 'stockBtn_data'), '=', lambda: rt.construct(e.get('StockBtn_data'), []))
    assign(ref(this, 'stockBtn_arr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'actionBtn_arr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'btn_arr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(ref(this, 'actionBtn_arr').get(), 0), '=', lambda: e.get('undefined'))
    assign(ref(ref(this, 'stockBtn_arr').get(), 0), '=', lambda: e.get('undefined'))
    assign(ref(this, 'shortMSG_textField'), '=', lambda: ref(ref(this, 'interfaceMC').get(), 'shortMSG_textField').get())
    e.set('_loc3_', 1)
    while truth(binop('<', e.get('_loc3_'), ref(ref(ref(this, 'stockBtn_data').get(), 'dataArr').get(), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(this, 'stockBtn_data').get(), 'dataArr').get(), e.get('_loc3_')).get())
            assign(e.ref('_loc5_'), '=', lambda: rt.construct(e.get('Btn_stock'), [ref(e.get('_loc4_'), 'id').get(), ref(e.get('_loc4_'), 'name').get(), ref(e.get('_loc4_'), 'label').get(), ref(ref(ref(this, 'interfaceMC').get(), binop('+', 'stockPanel', ref(e.get('_loc4_'), 'stockPanelNum').get())).get(), ref(e.get('_loc4_'), 'overlayMC_name').get()).get(), ref(ref(ref(this, 'interfaceMC').get(), binop('+', 'stockPanel', ref(e.get('_loc4_'), 'stockPanelNum').get())).get(), ref(e.get('_loc4_'), 'labelTF_name').get()).get(), ref(ref(ref(this, 'interfaceMC').get(), binop('+', 'stockPanel', ref(e.get('_loc4_'), 'stockPanelNum').get())).get(), ref(e.get('_loc4_'), 'scrnMC_name').get()).get(), ref(ref(ref(this, 'interfaceMC').get(), binop('+', 'stockPanel', ref(e.get('_loc4_'), 'stockPanelNum').get())).get(), ref(e.get('_loc4_'), 'scrnTF_name').get()).get(), ref(ref(ref(this, 'interfaceMC').get(), binop('+', 'stockPanel', ref(e.get('_loc4_'), 'stockPanelNum').get())).get(), ref(e.get('_loc4_'), 'btnSwitchMC_name').get()).get(), ref(e.get('_loc4_'), 'weaponName').get(), ref(e.get('_loc4_'), 'stockPanelNum').get(), ref(e.get('_loc4_'), 'deactivate_in_demo').get()]))
            assign(ref(ref(e.get('_loc5_'), 'overlayMC').get(), '_btnObj'), '=', lambda: e.get('_loc5_'))
            assign(ref(ref(e.get('_loc5_'), 'overlayMC').get(), 'onPress'), '=', lambda: ASFunction(f_2, e))
            assign(ref(ref(e.get('_loc5_'), 'overlayMC').get(), 'onRollOver'), '=', lambda: ASFunction(f_3, e))
            assign(ref(ref(e.get('_loc5_'), 'overlayMC').get(), 'onRollOut'), '=', lambda: ASFunction(f_4, e))
            rt.call_ref(ref(e.get('_loc5_'), 'resetClips'), [])
            rt.call_ref(ref(ref(this, 'stockBtn_arr').get(), 'push'), [e.get('_loc5_')])
            assign(ref(this, 'infoLine'), '=', lambda: 'welcome')
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc6_', 1)
    while truth(binop('<', e.get('_loc6_'), 10)):
        rt.tick()
        try:
            assign(ref(ref(this, 'actionBtn_arr').get(), e.get('_loc6_')), '=', lambda: rt.construct(e.get('Btn_action'), [ref(ref(this, 'actionNames_arr').get(), e.get('_loc6_')).get(), ref(ref(this, 'actionLabels_arr').get(), e.get('_loc6_')).get(), ref(ref(this, 'interfaceMC').get(), binop('+', 'btn', e.get('_loc6_'))).get(), ref(ref(this, 'interfaceMC').get(), binop('+', 'scrn', e.get('_loc6_'))).get(), ref(ref(this, 'interfaceMC').get(), binop('+', 'switch', e.get('_loc6_'))).get(), ref(ref(ref(this, 'interfaceMC').get(), binop('+', 'txtMC', e.get('_loc6_'))).get(), 'txt').get()]))
            assign(e.ref('_loc7_'), '=', lambda: ref(ref(this, 'actionBtn_arr').get(), e.get('_loc6_')).get())
            assign(ref(ref(e.get('_loc7_'), 'overlayMC').get(), '_btnObj'), '=', lambda: e.get('_loc7_'))
            assign(ref(ref(e.get('_loc7_'), 'overlayMC').get(), 'onPress'), '=', lambda: ASFunction(f_5, e))
            assign(ref(ref(e.get('_loc7_'), 'overlayMC').get(), 'onRollOver'), '=', lambda: ASFunction(f_6, e))
            assign(ref(ref(e.get('_loc7_'), 'overlayMC').get(), 'onRollOut'), '=', lambda: ASFunction(f_7, e))
            rt.call_ref(ref(e.get('_loc7_'), 'setLabelText'), [])
            rt.call_ref(ref(e.get('_loc7_'), 'updateBtn'), [])
            assign(e.ref('_loc6_'), '=', lambda: binop('+', e.get('_loc6_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(this, 'actionTube1'), '=', lambda: rt.construct(e.get('Btn_tube'), [ref(ref(this, 'interfaceMC').get(), 'btn44').get(), ref(ref(this, 'interfaceMC').get(), 'tubeMC1').get()]))
    assign(ref(ref(ref(this, 'actionTube1').get(), 'btnMC').get(), '_btnObj'), '=', lambda: ref(this, 'actionTube1').get())
    assign(ref(ref(this, 'actionTube1').get(), 'actionNum'), '=', lambda: 1)
    assign(ref(ref(this, 'actionTube1').get(), 'associatedTA'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'turnAction_1').get())
    assign(ref(ref(ref(this, 'actionTube1').get(), 'btnMC').get(), 'onPress'), '=', lambda: ASFunction(f_8, e))
    assign(ref(this, 'actionTube2'), '=', lambda: rt.construct(e.get('Btn_tube'), [ref(ref(this, 'interfaceMC').get(), 'btn45').get(), ref(ref(this, 'interfaceMC').get(), 'tubeMC2').get()]))
    assign(ref(ref(ref(this, 'actionTube2').get(), 'btnMC').get(), '_btnObj'), '=', lambda: ref(this, 'actionTube2').get())
    assign(ref(ref(this, 'actionTube2').get(), 'actionNum'), '=', lambda: 2)
    assign(ref(ref(this, 'actionTube2').get(), 'associatedTA'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'turnAction_2').get())
    assign(ref(ref(ref(this, 'actionTube2').get(), 'btnMC').get(), 'onPress'), '=', lambda: ASFunction(f_9, e))
    assign(ref(this, 'turnBtn'), '=', lambda: rt.construct(e.get('Btn_turn'), [ref(ref(this, 'interfaceMC').get(), 'btn46').get(), ref(ref(this, 'interfaceMC').get(), 'actionHatch3').get()]))
    e.set('_loc8_', 1)
    while truth(binop('<', e.get('_loc8_'), ref(ref(this, 'actionBtn_arr').get(), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc9_'), '=', lambda: ref(ref(this, 'actionBtn_arr').get(), e.get('_loc8_')).get())
            assign(ref(e.get('_loc9_'), 'index_in_arr'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'max'), [binop('-', rt.call_ref(ref(ref(this, 'btn_arr').get(), 'push'), [obj({'_btn': e.get('_loc9_')})]), 1), 0]))
            assign(e.ref('_loc8_'), '=', lambda: binop('+', e.get('_loc8_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc10_', 1)
    while truth(binop('<', e.get('_loc10_'), ref(ref(this, 'stockBtn_arr').get(), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc11_'), '=', lambda: ref(ref(this, 'stockBtn_arr').get(), e.get('_loc10_')).get())
            assign(ref(e.get('_loc11_'), 'index_in_arr'), '=', lambda: binop('-', rt.call_ref(ref(ref(this, 'btn_arr').get(), 'push'), [obj({'_btn': ref(ref(this, 'stockBtn_arr').get(), e.get('_loc10_')).get()})]), 1))
            assign(e.ref('_loc10_'), '=', lambda: binop('+', e.get('_loc10_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(this, 'btn_sound'), '=', lambda: rt.construct(e.get('Btn_musicSwitch'), [ref(ref(this, 'interfaceMC').get(), 'btn38').get(), ref(ref(this, 'interfaceMC').get(), 'switch38').get(), 'sound']))
    assign(ref(ref(ref(this, 'btn_sound').get(), 'overlayMC').get(), '_obj'), '=', lambda: ref(this, 'btn_sound').get())
    assign(ref(ref(ref(this, 'btn_sound').get(), 'overlayMC').get(), 'onPress'), '=', lambda: ASFunction(f_10, e))
    assign(ref(this, 'btn_music'), '=', lambda: rt.construct(e.get('Btn_musicSwitch'), [ref(ref(this, 'interfaceMC').get(), 'btn39').get(), ref(ref(this, 'interfaceMC').get(), 'switch39').get(), 'music']))
    assign(ref(ref(ref(this, 'btn_music').get(), 'overlayMC').get(), '_obj'), '=', lambda: ref(this, 'btn_music').get())
    assign(ref(ref(ref(this, 'btn_music').get(), 'overlayMC').get(), 'onPress'), '=', lambda: ASFunction(f_11, e))
    assign(ref(this, 'scrollBtn_msg_up'), '=', lambda: rt.construct(e.get('Btn_simple'), [ref(ref(this, 'interfaceMC').get(), 'btn_scroll_MSG_up_overlay').get(), ref(ref(this, 'interfaceMC').get(), 'btn_scroll_MSG_up').get()]))
    assign(ref(this, 'scrollBtn_msg_down'), '=', lambda: rt.construct(e.get('Btn_simple'), [ref(ref(this, 'interfaceMC').get(), 'btn_scroll_MSG_down_overlay').get(), ref(ref(this, 'interfaceMC').get(), 'btn_scroll_MSG_down').get()]))
    assign(ref(ref(ref(this, 'interfaceMC').get(), 'btn_scroll_MSG_up_overlay').get(), 'onPress'), '=', lambda: ASFunction(f_12, e))
    assign(ref(ref(ref(this, 'interfaceMC').get(), 'btn_scroll_MSG_down_overlay').get(), 'onPress'), '=', lambda: ASFunction(f_13, e))
    assign(ref(ref(ref(this, 'interfaceMC').get(), 'btn40').get(), 'onPress'), '=', lambda: ASFunction(f_14, e))
    assign(ref(ref(ref(this, 'interfaceMC').get(), 'btn41').get(), 'onPress'), '=', lambda: ASFunction(f_15, e))
    assign(ref(ref(ref(this, 'interfaceMC').get(), 'btn42').get(), 'onPress'), '=', lambda: ASFunction(f_16, e))
    assign(ref(ref(ref(this, 'interfaceMC').get(), 'btn43').get(), 'onPress'), '=', lambda: ASFunction(f_17, e))
    e.set('_loc12_', 1)
    while truth(binop('<', e.get('_loc12_'), 5)):
        rt.tick()
        try:
            assign(ref(ref(ref(this, 'interfaceMC').get(), binop('+', binop('+', 'stat', e.get('_loc12_')), '1')).get(), 'num'), '=', lambda: e.get('_loc12_'))
            assign(ref(ref(ref(this, 'interfaceMC').get(), binop('+', binop('+', 'stat', e.get('_loc12_')), '1')).get(), 'onRollOver'), '=', lambda: ASFunction(f_18, e))
            assign(ref(ref(ref(this, 'interfaceMC').get(), binop('+', binop('+', 'stat', e.get('_loc12_')), '1')).get(), 'onRollOut'), '=', lambda: ASFunction(f_19, e))
            assign(ref(ref(ref(this, 'interfaceMC').get(), binop('+', binop('+', 'stat', e.get('_loc12_')), '2')).get(), 'num'), '=', lambda: e.get('_loc12_'))
            assign(ref(ref(ref(this, 'interfaceMC').get(), binop('+', binop('+', 'stat', e.get('_loc12_')), '2')).get(), 'onRollOver'), '=', lambda: ASFunction(f_20, e))
            assign(ref(ref(ref(this, 'interfaceMC').get(), binop('+', binop('+', 'stat', e.get('_loc12_')), '2')).get(), 'onRollOut'), '=', lambda: ASFunction(f_21, e))
            assign(e.ref('_loc12_'), '=', lambda: binop('+', e.get('_loc12_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(ref(ref(ref(this, 'interfaceMC').get(), 'txtMC_help').get(), 'txt').get(), 'text'), '=', lambda: 'HELP')
    assign(ref(ref(ref(this, 'interfaceMC').get(), 'btn_help').get(), 'onPress'), '=', lambda: ASFunction(f_22, e))
    assign(ref(ref(ref(ref(this, 'interfaceMC').get(), 'txtMC_fullscreen').get(), 'txt').get(), 'text'), '=', lambda: 'FULL SCREEN')
    assign(ref(ref(ref(this, 'interfaceMC').get(), 'btn_fullscreen').get(), 'onPress'), '=', lambda: ASFunction(f_23, e))
    e.set('_loc13_', 1)
    while truth(binop('<', e.get('_loc13_'), 6)):
        rt.tick()
        try:
            rt.call_ref(ref(ref(ref(this, 'interfaceMC').get(), binop('+', 'map_overlay_btn', e.get('_loc13_'))).get(), 'gotoAndStop'), [2])
            assign(e.ref('_loc13_'), '=', lambda: binop('+', e.get('_loc13_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(this, 'infoLine'), '=', lambda: 'welcome')
    return U

def View_interface_update_stockPanelMask(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_num', '_frm'], ['_frm', '_num'], closure, 'View_interface')
    rt.call_ref(ref(ref(ref(ref(ref(this, 'interfaceMC').get(), 'stockPanel').get(), 'maskMC').get(), binop('+', 'mc', e.get('_num'))).get(), 'gotoAndStop'), [e.get('_frm')])
    return U

def View_interface_actionName2TubeLabel(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str', 'i'], closure, 'View_interface')
    for key_24 in keys(ref(this, 'actionNames_arr').get()):
        e.ref('i').set(key_24)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(this, 'actionNames_arr').get(), e.get('i')).get(), e.get('_str'))):
                return ref(ref(this, 'actionTubeLabels_arr').get(), e.get('i')).get()
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def View_interface_actionName2label(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str', 'i'], closure, 'View_interface')
    for key_25 in keys(ref(this, 'actionNames_arr').get()):
        e.ref('i').set(key_25)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(this, 'actionNames_arr').get(), e.get('i')).get(), e.get('_str'))):
                return ref(ref(this, 'actionLabels_arr').get(), e.get('i')).get()
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def f_26(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(binop('>', ref(this, '_alpha').get(), binop('+', ref(this, 'targetAlpha').get(), 5))):
        assign(ref(this, '_alpha'), '-=', lambda: 20)
    else:
        if truth(binop('<', ref(this, '_alpha').get(), binop('-', ref(this, 'targetAlpha').get(), 5))):
            assign(ref(this, '_alpha'), '+=', lambda: 20)
    if truth(binop('<', binop('-', rt.call_ref(ref(e.get('Math'), 'max'), [ref(this, '_alpha').get(), ref(this, 'targetAlpha').get()]), rt.call_ref(ref(e.get('Math'), 'min'), [ref(this, '_alpha').get(), ref(this, 'targetAlpha').get()])), 21)):
        assign(ref(this, '_alpha'), '=', lambda: ref(this, 'targetAlpha').get())
        ref(this, 'onEnterFrame').delete()
    return U

def View_interface_update_stockPanel_alpha(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_num', '__alpha'], ['__alpha', '_num'], closure, 'View_interface')
    assign(ref(ref(ref(this, 'interfaceMC').get(), binop('+', 'stockPanel', e.get('_num'))).get(), 'targetAlpha'), '=', lambda: e.get('__alpha'))
    assign(ref(ref(ref(this, 'interfaceMC').get(), binop('+', 'stockPanel', e.get('_num'))).get(), 'onEnterFrame'), '=', lambda: ASFunction(f_26, e))
    return U

def View_interface_infoLine_interfal_func(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'infoLine_interval_id').get()])
    assign(ref(this, 'infoLine_interval_id'), '=', lambda: e.get('undefined'))
    rt.call_ref(ref(ref(ref(this, 'interfaceMC').get(), 'infoLine').get(), 'gotoAndStop'), [1])
    return U

def View_interface___set__infoLine(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str'], closure, 'View_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'infoLine_interval_id').get()])
    assign(ref(this, 'infoLine_interval_id'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'infoLine_interfal_func', 4500]))
    rt.call_ref(ref(ref(ref(this, 'interfaceMC').get(), 'infoLine').get(), 'gotoAndStop'), [e.get('_str')])
    return U

def View_interface_update_statBar(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_num', '_val'], ['_num', '_val'], closure, 'View_interface')
    assign(ref(ref(ref(ref(this, 'interfaceMC').get(), binop('+', 'statBar', e.get('_num'))).get(), 'statMask').get(), '_xscale'), '=', lambda: e.get('_val'))
    return U

def View_interface_update_statMoney(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_val'], ['_val'], closure, 'View_interface')
    if truth(binop('<=', e.get('_val'), 0)):
        assign(ref(ref(ref(this, 'interfaceMC').get(), 'statTxt').get(), 'text'), '=', lambda: '$ out of funds')
    else:
        assign(ref(ref(ref(this, 'interfaceMC').get(), 'statTxt').get(), 'text'), '=', lambda: binop('+', binop('+', '$ ', rt.call_ref(ref(e.get('Math'), 'round'), [e.get('_val')])), '.000.000 '))
    return U

def View_interface_update_hover_states(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_index'], ['_index'], closure, 'View_interface')
    return U

def View_interface___set__shortMSG_text(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_arr'], ['_arr', '_loc3_', '_loc4_'], closure, 'View_interface')
    assign(ref(ref(this, 'shortMSG_textField').get(), 'text'), '=', lambda: '')
    e.set('_loc3_', 0)
    while truth(binop('<', e.get('_loc3_'), ref(e.get('_arr'), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(e.get('_arr'), e.get('_loc3_')).get())
            if truth(logical('&&', binop('!=', ref(e.get('_loc4_'), '_msg').get(), ''), lambda: ref(e.get('_loc4_'), '_msg').get())):
                assign(ref(ref(this, 'shortMSG_textField').get(), 'htmlText'), '+=', lambda: binop('+', ref(e.get('_loc4_'), '_msg').get(), '<br />'))
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    rt.call_ref(ref(this, 'scroll_msg_txt'), [])
    return U

def View_interface_set_color_dot(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_num', 'a_frame'], ['a_frame', 'a_num'], closure, 'View_interface')
    rt.call_ref(ref(ref(ref(this, 'interfaceMC').get(), binop('+', 'colorDotMC', e.get('a_num'))).get(), 'gotoAndStop'), [e.get('a_frame')])
    return U

def View_interface_update_leaderFace(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_playerNum', '_frame', '_alive', '_inactive', '_played_noise'], ['_alive', '_frame', '_inactive', '_loc7_', '_played_noise', '_playerNum'], closure, 'View_interface')
    e.set('_loc7_', ref(ref(this, 'interfaceMC').get(), binop('+', 'leaderMC', e.get('_playerNum'))).get())
    if truth(e.get('_inactive')):
        assign(ref(e.get('_loc7_'), '_visible'), '=', lambda: False)
        return e.get('undefined')
    assign(ref(e.get('_loc7_'), '_visible'), '=', lambda: True)
    if truth(e.get('_alive')):
        rt.call_ref(ref(e.get('_loc7_'), 'gotoAndStop'), ['leaderLife'])
        assign(ref(e.get('_loc7_'), '_visible'), '=', lambda: True)
        rt.call_ref(ref(ref(e.get('_loc7_'), 'aliveMC').get(), 'gotoAndStop'), [e.get('_frame')])
        rt.call_ref(ref(ref(e.get('_loc7_'), 'deadMC').get(), 'gotoAndStop'), [e.get('_frame')])
    else:
        assign(ref(ref(e.get('_loc7_'), 'aliveMC').get(), '_visible'), '=', lambda: False)
        rt.call_ref(ref(e.get('_loc7_'), 'gotoAndStop'), ['leaderDead'])
        if truth(e.get('_played_noise')):
            rt.call_ref(ref(ref(e.get('_loc7_'), 'aliveMC').get(), 'gotoAndStop'), [20])
            assign(ref(ref(e.get('_loc7_'), 'deadMC').get(), '_visible'), '=', lambda: True)
            rt.call_ref(ref(ref(e.get('_loc7_'), 'deadMC').get(), 'gotoAndStop'), [e.get('_frame')])
        else:
            assign(ref(e.get('_loc7_'), 'playDead'), '=', lambda: True)
            assign(ref(ref(e.get('_loc7_'), 'deadMC').get(), '_visible'), '=', lambda: True)
            rt.call_ref(ref(ref(e.get('_loc7_'), 'deadMC').get(), 'gotoAndStop'), [e.get('_frame')])
            rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_noise'])
            rt.call_ref(ref(e.get('_loc7_'), 'gotoAndPlay'), [24])
    return U

def View_interface_set_centerScreenFunc(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_type'], ['_type'], closure, 'View_interface')
    switch_27 = e.get('_type')
    case_28 = -1
    if case_28 == -1 and strict_eq(switch_27, 'default'):
        case_28 = 0
    if case_28 == -1 and strict_eq(switch_27, 'hide'):
        case_28 = 1
    if case_28 == -1:
        case_28 = 2
    try:
        if 0 <= case_28 <= 0:
            rt.call_ref(ref(this, 'set_centerScreen_btns_default'), [])
            raise ASBreak()
        if 0 <= case_28 <= 1:
            rt.call_ref(ref(this, 'set_centerScreen_btns_hide'), [])
        if 0 <= case_28 <= 2:
            return U
    except ASBreak:
        pass
    return U

def View_interface_set_centerScreen_btns_hide(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View_interface')
    rt.call_ref(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'btnAccept').get(), 'gotoAndStop'), ['empty'])
    rt.call_ref(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'btnCancel').get(), 'gotoAndStop'), ['empty'])
    return U

def f_29(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'gotoAndStop'), ['over'])
    return U

def f_30(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'gotoAndStop'), ['off'])
    return U

def f_31(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPressed_accept'), [])
    return U

def f_32(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_acceptAction_btn'])
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPressed_cancel'), [])
    return U

def f_33(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'gotoAndStop'), ['over'])
    return U

def f_34(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'gotoAndStop'), ['off'])
    return U

def View_interface_set_centerScreen_btns_default(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View_interface')
    rt.call_ref(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'btnAccept').get(), 'gotoAndStop'), ['off'])
    rt.call_ref(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'btnCancel').get(), 'gotoAndStop'), ['off'])
    assign(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'btnAccept').get(), 'onRollOver'), '=', lambda: ASFunction(f_29, e))
    assign(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'btnAccept').get(), 'onRollOut'), '=', lambda: ASFunction(f_30, e))
    assign(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'btnAccept').get(), 'onPress'), '=', lambda: ASFunction(f_31, e))
    assign(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'btnCancel').get(), 'onPress'), '=', lambda: ASFunction(f_32, e))
    assign(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'btnCancel').get(), 'onRollOver'), '=', lambda: ASFunction(f_33, e))
    assign(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'btnCancel').get(), 'onRollOut'), '=', lambda: ASFunction(f_34, e))
    return U

def View_interface_set_production_specialStats(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_arr'], ['_arr', '_loc3_'], closure, 'View_interface')
    e.set('_loc3_', 0)
    while truth(binop('<', e.get('_loc3_'), ref(e.get('_arr'), 'length').get())):
        rt.tick()
        try:
            assign(ref(ref(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'slide3').get(), binop('+', 'stat', e.get('_loc3_'))).get(), 'maskMC').get(), '_xscale'), '=', lambda: binop('*', binop('/', ref(ref(e.get('_arr'), e.get('_loc3_')).get(), 0).get(), ref(ref(e.get('_arr'), e.get('_loc3_')).get(), 1).get()), 100))
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def View_interface_set_productionText(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str1', '_str2', '_str3'], ['_str1', '_str2', '_str3'], closure, 'View_interface')
    assign(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'txt1').get(), 'htmlText'), '=', lambda: e.get('_str1'))
    assign(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'txt2').get(), 'htmlText'), '=', lambda: e.get('_str2'))
    rt.call_ref(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'txt2').get(), 'setTextFormat'), [ref(ref(ref(e.get('_global'), 'view').get(), 'textFormats').get(), 'interface_production_1').get()])
    assign(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'txt3').get(), 'htmlText'), '=', lambda: e.get('_str3'))
    return U

def View_interface_set_researchText(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str1', '_str2', '_str3'], ['_str1', '_str2', '_str3'], closure, 'View_interface')
    assign(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'txt1').get(), 'htmlText'), '=', lambda: e.get('_str1'))
    rt.call_ref(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'txt1').get(), 'setTextFormat'), [ref(ref(ref(e.get('_global'), 'view').get(), 'textFormats').get(), 'interface_production_2').get()])
    assign(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'txt2').get(), 'htmlText'), '=', lambda: e.get('_str2'))
    rt.call_ref(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'txt2').get(), 'setTextFormat'), [ref(ref(ref(e.get('_global'), 'view').get(), 'textFormats').get(), 'interface_production_1').get()])
    assign(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'txt3').get(), 'htmlText'), '=', lambda: e.get('_str3'))
    rt.call_ref(ref(ref(ref(ref(this, 'interfaceMC').get(), 'centerScreen').get(), 'txt3').get(), 'setTextFormat'), [ref(ref(ref(e.get('_global'), 'view').get(), 'textFormats').get(), 'interface_production_1').get()])
    return U

def View_interface_set_top_plrColor(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_num', '_clr'], ['_clr', '_num'], closure, 'View_interface')
    rt.call_ref(ref(ref(ref(this, 'interfaceMC').get(), binop('+', 'plrColor', e.get('_num'))).get(), 'gotoAndStop'), [e.get('_clr')])
    return e.get('undefined')
    return U

def f_35(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(e.get('_global'), 'model').get(), 'userSelectedHelpTopic'), '=', lambda: 'help_index')
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'updateView'), [])
    return U

def f_36(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(e.get('_global'), 'model').get(), 'userSelectedHelpTopic'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'help_data').get(), 'get_prev'), [ref(this, '_str').get()]))
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'updateView'), [])
    return U

def f_37(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(e.get('_global'), 'model').get(), 'userSelectedHelpTopic'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'help_data').get(), 'get_next'), [ref(this, '_str').get()]))
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'updateView'), [])
    return U

def f_39(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(e.get('_global'), 'model').get(), 'userSelectedHelpTopic'), '=', lambda: ref(this, 'goto').get())
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'updateView'), [])
    return U

def View_interface_set_centerScreenFunc_help(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_info'], ['_loc3_', '_loc4_', 'a_info', 'i'], closure, 'View_interface')
    e.set('_loc3_', ref(ref(this, 'interfaceMC').get(), 'centerScreen').get())
    rt.call_ref(ref(e.get('_loc3_'), 'gotoAndStop'), [ref(e.get('a_info'), 'pgName').get()])
    if truth(ref(e.get('a_info'), '_btnIndex').get()):
        assign(ref(ref(e.get('_loc3_'), 'btnIndex').get(), '_visible'), '=', lambda: True)
        assign(ref(ref(e.get('_loc3_'), 'btnIndex').get(), 'onPress'), '=', lambda: ASFunction(f_35, e))
    else:
        assign(ref(ref(e.get('_loc3_'), 'btnIndex').get(), '_visible'), '=', lambda: False)
    if truth(ref(e.get('a_info'), '_btnPrev').get()):
        assign(ref(ref(e.get('_loc3_'), 'btnPrev').get(), '_visible'), '=', lambda: True)
        assign(ref(ref(e.get('_loc3_'), 'btnPrev').get(), '_str'), '=', lambda: ref(e.get('a_info'), '_pgName').get())
        assign(ref(ref(e.get('_loc3_'), 'btnPrev').get(), 'onPress'), '=', lambda: ASFunction(f_36, e))
    else:
        assign(ref(ref(e.get('_loc3_'), 'btnPrev').get(), '_visible'), '=', lambda: False)
    if truth(ref(e.get('a_info'), '_btnNext').get()):
        assign(ref(ref(e.get('_loc3_'), 'btnNext').get(), '_visible'), '=', lambda: True)
        assign(ref(ref(e.get('_loc3_'), 'btnNext').get(), '_str'), '=', lambda: ref(e.get('a_info'), '_pgName').get())
        assign(ref(ref(e.get('_loc3_'), 'btnNext').get(), 'onPress'), '=', lambda: ASFunction(f_37, e))
    else:
        assign(ref(ref(e.get('_loc3_'), 'btnNext').get(), '_visible'), '=', lambda: False)
    for key_38 in keys(ref(e.get('a_info'), '_btnArr').get()):
        e.ref('i').set(key_38)
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(e.get('a_info'), '_btnArr').get(), e.get('i')).get())
            assign(ref(ref(e.get('_loc3_'), ref(e.get('_loc4_'), '_mcName').get()).get(), 'goto'), '=', lambda: ref(e.get('_loc4_'), '_trgtString').get())
            assign(ref(ref(e.get('_loc3_'), ref(e.get('_loc4_'), '_mcName').get()).get(), 'onPress'), '=', lambda: ASFunction(f_39, e))
        except ASContinue:
            pass
        except ASBreak:
            break
    rt.call_ref(ref(ref(e.get('_loc3_'), 'mc1').get(), 'stop'), [])
    return U

def View_interface_scroll_msg_txt(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_loc3_', '_str'], closure, 'View_interface')
    switch_40 = e.get('_str')
    case_41 = -1
    if case_41 == -1 and strict_eq(switch_40, 'up'):
        case_41 = 0
    if case_41 == -1 and strict_eq(switch_40, 'down'):
        case_41 = 1
    if case_41 == -1:
        case_41 = -1
    try:
        if 0 <= case_41 <= 0:
            update(ref(ref(ref(this, 'interfaceMC').get(), 'shortMSG_textField').get(), 'scroll'), -1, False)
            raise ASBreak()
        if 0 <= case_41 <= 1:
            update(ref(ref(ref(this, 'interfaceMC').get(), 'shortMSG_textField').get(), 'scroll'), 1, False)
    except ASBreak:
        pass
    e.set('_loc3_', ref(ref(ref(this, 'interfaceMC').get(), 'shortMSG_textField').get(), 'scroll').get())
    if truth(binop('==', e.get('_loc3_'), 1)):
        rt.call_ref(ref(ref(ref(this, 'scrollBtn_msg_up').get(), 'img').get(), 'gotoAndStop'), [2])
    else:
        rt.call_ref(ref(ref(ref(this, 'scrollBtn_msg_up').get(), 'img').get(), 'gotoAndStop'), [1])
    if truth(binop('==', e.get('_loc3_'), ref(ref(ref(this, 'interfaceMC').get(), 'shortMSG_textField').get(), 'maxscroll').get())):
        rt.call_ref(ref(ref(ref(this, 'scrollBtn_msg_down').get(), 'img').get(), 'gotoAndStop'), [2])
    else:
        rt.call_ref(ref(ref(ref(this, 'scrollBtn_msg_down').get(), 'img').get(), 'gotoAndStop'), [1])
    return U

def View_interface_play_leaderMC_sequence(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['num'], ['num'], closure, 'View_interface')
    return U

def View_interface_update_highScore(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_amnt'], ['a_amnt'], closure, 'View_interface')
    assign(ref(ref(ref(ref(this, 'interfaceMC').get(), 'txtMC_score').get(), 'txt').get(), 'text'), '=', lambda: e.get('a_amnt'))
    return U

def View_interface_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View_interface')
    ref(this, 'actionNames_arr').set(rt.construct(e.get('Array'), [e.get('undefined'), 'resources', 'production', 'research', 'religion', 'attack', 'preAttack', 'defense', 'propaganda', 'diplomacy', 'skip_action']))
    ref(this, 'actionLabels_arr').set(rt.construct(e.get('Array'), [e.get('undefined'), 'RESOURCES', 'PRODUCTION', 'TECHNOLOGY', 'MASS MEDIA', 'DIRECT ATTACK', 'PREPARED ATTACK', 'DEFENSE', 'PROPAGANDA', 'DIPLOMACY', 'SKIP']))
    ref(this, 'actionTubeLabels_arr').set(rt.construct(e.get('Array'), [e.get('undefined'), 'RESOURCES', 'PRODUCTION', 'TECHNOLOGY', 'MASS MEDIA', 'DIRECT <br />ATTACK', 'PREPARED <br /> ATTACK', 'DEFENSE', 'PROPAGANDA', 'DIPLOMACY']))
    ref(this, 'stockPanel_mask_states_arr').set(rt.construct(e.get('Array'), [arr([0]), arr([3]), arr([0]), arr([0]), arr([3]), arr([2, 2, 2, 2, 2, 2, 1, 1, 2]), arr([1, 1, 1, 1, 2, 2, 2, 2, 2]), arr([2, 2, 2, 2, 2, 2, 2, 2, 1]), arr([3]), arr([3])]))

def register(rt):
    rt.define('View_interface', None, View_interface_fields, {'View_interface': ASFunction(View_interface_View_interface), 'update_stockPanelMask': ASFunction(View_interface_update_stockPanelMask), 'actionName2TubeLabel': ASFunction(View_interface_actionName2TubeLabel), 'actionName2label': ASFunction(View_interface_actionName2label), 'update_stockPanel_alpha': ASFunction(View_interface_update_stockPanel_alpha), 'infoLine_interfal_func': ASFunction(View_interface_infoLine_interfal_func), 'update_statBar': ASFunction(View_interface_update_statBar), 'update_statMoney': ASFunction(View_interface_update_statMoney), 'update_hover_states': ASFunction(View_interface_update_hover_states), 'set_color_dot': ASFunction(View_interface_set_color_dot), 'update_leaderFace': ASFunction(View_interface_update_leaderFace), 'set_centerScreenFunc': ASFunction(View_interface_set_centerScreenFunc), 'set_centerScreen_btns_hide': ASFunction(View_interface_set_centerScreen_btns_hide), 'set_centerScreen_btns_default': ASFunction(View_interface_set_centerScreen_btns_default), 'set_production_specialStats': ASFunction(View_interface_set_production_specialStats), 'set_productionText': ASFunction(View_interface_set_productionText), 'set_researchText': ASFunction(View_interface_set_researchText), 'set_top_plrColor': ASFunction(View_interface_set_top_plrColor), 'set_centerScreenFunc_help': ASFunction(View_interface_set_centerScreenFunc_help), 'scroll_msg_txt': ASFunction(View_interface_scroll_msg_txt), 'play_leaderMC_sequence': ASFunction(View_interface_play_leaderMC_sequence), 'update_highScore': ASFunction(View_interface_update_highScore)}, {}, {'infoLine': ASFunction(View_interface___set__infoLine), 'shortMSG_text': ASFunction(View_interface___set__shortMSG_text)})
