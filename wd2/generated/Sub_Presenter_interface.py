# Generated from __Packages/Sub_Presenter_interface.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Sub_Presenter_interface_Sub_Presenter_interface(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_Presenter_interface')
    e.call('__super__', [])
    return U

def Sub_Presenter_interface_resetBtns(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'Sub_Presenter_interface')
    for key_1 in keys(ref(ref(this, 'view_interface').get(), 'actionBtn_arr').get()):
        e.ref('i').set(key_1)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(this, 'view_interface').get(), 'actionBtn_arr').get(), e.get('i')).get())
            if truth(logical('&&', binop('!=', ref(e.get('_loc2_'), 'actionName').get(), ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnAction_1').get(), 'action').get()), lambda: binop('!=', ref(e.get('_loc2_'), 'actionName').get(), ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnAction_2').get(), 'action').get()))):
                assign(ref(e.get('_loc2_'), 'isSetAction'), '=', lambda: False)
            else:
                if truth(unary('!', ref(e.get('_loc2_'), 'isSetAction').get())):
                    assign(ref(e.get('_loc2_'), 'state'), '=', lambda: 1)
                    rt.call_ref(ref(e.get('_loc2_'), 'updateBtn'), [])
            assign(ref(ref(ref(ref(this, 'view_interface').get(), 'btn_arr').get(), e.get('i')).get(), 'pressed'), '=', lambda: False)
        except ASContinue:
            pass
        except ASBreak:
            break
    rt.call_ref(ref(ref(this, 'model').get(), 'deselectCities'), [ref(ref(this, 'model').get(), 'userSelectedActionBtn').get()])
    assign(ref(ref(this, 'model').get(), 'userSelectedStockBtn'), '=', lambda: e.get('undefined'))
    assign(ref(ref(this, 'model').get(), 'userSelectedActionBtn'), '=', lambda: e.get('undefined'))
    rt.call_ref(ref(ref(this, 'model').get(), 'resetUserSelections'), [])
    assign(ref(ref(this, 'model_interface').get(), 'cur_pressed_action_btn'), '=', lambda: e.get('undefined'))
    rt.call_ref(ref(this, 'updateView'), [])
    return U

def Sub_Presenter_interface_do_turn_backup(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_Presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'doTurn_backup_intervalID').get()])
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'doTurn_intervalID').get()])
    assign(ref(ref(ref(this, 'view_interface').get(), 'turnBtn').get(), 'state'), '=', lambda: 'closed')
    assign(ref(this, 'block_start_btn'), '=', lambda: False)
    assign(ref(this, 'blockAllBtns'), '=', lambda: False)
    return U

def Sub_Presenter_interface_turnInterval_step1(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_Presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'doTurn_intervalID').get()])
    assign(ref(this, 'doTurn_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'turnInterval_step2', 200]))
    assign(ref(ref(ref(this, 'view_interface').get(), 'actionTube2').get(), 'state'), '=', lambda: 'closed')
    return U

def Sub_Presenter_interface_turnInterval_step2(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_Presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'doTurn_intervalID').get()])
    assign(ref(this, 'doTurn_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'turnInterval_step3', 200]))
    rt.call_ref(ref(ref(ref(ref(this, 'view_interface').get(), 'turnBtn').get(), 'btnMC').get(), 'gotoAndStop'), [3])
    return U

def Sub_Presenter_interface_turnInterval_step3(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_Presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'doTurn_intervalID').get()])
    assign(ref(this, 'doTurn_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'turnInterval_go', 200]))
    return U

def Sub_Presenter_interface_turnInterval_go(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_Presenter_interface')
    if truth(logical('&&', ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnAction_1').get(), 'action').get(), lambda: ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnAction_2').get(), 'action').get())):
        assign(ref(this, 'block_start_btn'), '=', lambda: False)
        rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'doTurn_intervalID').get()])
        rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'doTurn_backup_intervalID').get()])
        rt.call_ref(ref(ref(this, 'view').get(), 'changeOver'), ['toBattle'])
        rt.call_ref(ref(ref(this, 'model').get(), 'doTurn'), [])
        rt.call_ref(ref(ref(this, 'presenter').get(), 'turnResults'), [])
        rt.call_ref(ref(ref(this, 'view').get(), 'updateCities'), [])
        rt.call_ref(ref(ref(this, 'presenter').get(), 'initBattle'), [])
        assign(ref(ref(this, 'model').get(), 'interface_diplomacy_error'), '=', lambda: e.get('undefined'))
        assign(ref(ref(this, 'model').get(), 'interface_spy_error'), '=', lambda: e.get('undefined'))
    return U

def f_2(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('getURL', [rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'get_demo_version_url'), []), '_blank'])
    return U

def f_3(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'ch_018').get(), 4).get(), 'active'), '=', lambda: True)
    return U

def f_8(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(e.get('_global'), 'presenter_interface').get(), 'blockAllBtns'), '=', lambda: True)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPressed_turn'), [])
    return U

def Sub_Presenter_interface_updateView(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc14_', '_loc15_', '_loc16_', '_loc17_', '_loc18_', '_loc19_', '_loc20_', '_loc21_', '_loc22_', '_loc23_', '_loc24_', '_loc25_', '_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', 'i', 'j'], closure, 'Sub_Presenter_interface')
    rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'remove_city_popups'), [])
    if truth(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'diplomacyPendingArr').get(), 0).get()):
        assign(ref(ref(this, 'model').get(), 'userSelectedActionBtn'), '=', lambda: 'diplomacyPending')
    if truth(ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get()):
        assign(ref(ref(ref(ref(e.get('_global'), 'view').get(), 'srcMC').get(), 'get_full_version_btn').get(), 'onPress'), '=', lambda: ASFunction(f_2, e))
        assign(ref(ref(ref(ref(e.get('_global'), 'view').get(), 'srcMC').get(), 'testBtn').get(), 'onPress'), '=', lambda: ASFunction(f_3, e))
    else:
        assign(ref(ref(ref(ref(e.get('_global'), 'view').get(), 'srcMC').get(), 'get_full_version_btn').get(), '_visible'), '=', lambda: False)
        assign(ref(ref(ref(ref(e.get('_global'), 'view').get(), 'srcMC').get(), 'get_full_version_text').get(), '_visible'), '=', lambda: False)
        rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'view').get(), 'srcMC').get(), 'demo_stock_overlay').get(), 'gotoAndStop'), [1])
        assign(ref(ref(ref(ref(e.get('_global'), 'view').get(), 'srcMC').get(), 'demo_stock_overlay').get(), '_visible'), '=', lambda: False)
    assign(ref(ref(this, 'view_interface').get(), 'shortMSG_text'), '=', lambda: ref(ref(ref(this, 'model').get(), 'human').get(), 'shortMSG_arr').get())
    for key_4 in keys(ref(ref(this, 'view_interface').get(), 'stockBtn_arr').get()):
        e.ref('i').set(key_4)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(this, 'view_interface').get(), 'stockBtn_arr').get(), e.get('i')).get())
            assign(e.ref('_loc3_'), '=', lambda: rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'weaponStock').get(), 'getWeaponByName'), [ref(e.get('_loc2_'), 'relatedWeapon').get()]))
            assign(e.ref('_loc4_'), '=', lambda: True)
            assign(e.ref('_loc5_'), '=', lambda: True)
            assign(e.ref('_loc6_'), '=', lambda: True)
            if truth(ref(e.get('_loc3_'), 'active').get()):
                assign(ref(e.get('_loc2_'), 'stockAmount'), '=', lambda: binop('-', ref(e.get('_loc3_'), 'inStock').get(), ref(e.get('_loc3_'), 'inUse').get()))
            else:
                assign(ref(e.get('_loc2_'), 'stockAmount'), '=', lambda: unary('-', 1))
            for key_5 in keys(ref(ref(ref(ref(this, 'view_interface').get(), 'stockRequirements_list').get(), ref(ref(this, 'model_interface').get(), 'selected_action_name').get()).get(), 'state2_arr').get()):
                e.ref('j').set(key_5)
                rt.tick()
                try:
                    if truth(unary('!', rt.call_ref(ref(this, 'stock_req_check_single'), [ref(ref(ref(ref(ref(this, 'view_interface').get(), 'stockRequirements_list').get(), ref(ref(this, 'model_interface').get(), 'selected_action_name').get()).get(), 'state2_arr').get(), e.get('j')).get(), e.get('_loc2_')]))):
                        assign(e.ref('_loc4_'), '=', lambda: False)
                        raise ASBreak()
                except ASContinue:
                    pass
                except ASBreak:
                    break
            for key_6 in keys(ref(ref(ref(ref(this, 'view_interface').get(), 'stockRequirements_list').get(), ref(ref(this, 'model_interface').get(), 'selected_action_name').get()).get(), 'state4_arr').get()):
                e.ref('j').set(key_6)
                rt.tick()
                try:
                    if truth(unary('!', rt.call_ref(ref(this, 'stock_req_check_single'), [ref(ref(ref(ref(ref(this, 'view_interface').get(), 'stockRequirements_list').get(), ref(ref(this, 'model_interface').get(), 'selected_action_name').get()).get(), 'state4_arr').get(), e.get('j')).get(), e.get('_loc2_')]))):
                        assign(e.ref('_loc6_'), '=', lambda: False)
                        raise ASBreak()
                except ASContinue:
                    pass
                except ASBreak:
                    break
            if truth(e.get('_loc6_')):
                assign(ref(e.get('_loc2_'), 'state'), '=', lambda: 4)
            else:
                if truth(e.get('_loc4_')):
                    assign(ref(e.get('_loc2_'), 'state'), '=', lambda: 2)
                else:
                    assign(ref(e.get('_loc2_'), 'state'), '=', lambda: 1)
            if truth(binop('==', ref(e.get('_loc2_'), 'relatedWeapon').get(), ref(ref(this, 'model').get(), 'userSelectedStockBtn').get())):
                assign(ref(e.get('_loc2_'), 'state'), '=', lambda: 3)
            if truth(logical('&&', binop('==', ref(e.get('_loc3_'), 'weaponName').get(), 'specialLoad'), lambda: binop('!=', ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'space'))):
                assign(ref(e.get('_loc2_'), 'state'), '=', lambda: 1)
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_7 in keys(ref(ref(this, 'view_interface').get(), 'actionBtn_arr').get()):
        e.ref('i').set(key_7)
        rt.tick()
        try:
            assign(e.ref('_loc7_'), '=', lambda: ref(ref(ref(this, 'view_interface').get(), 'actionBtn_arr').get(), e.get('i')).get())
            if truth(unary('!', rt.call_ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'getNextTurnAction'), []))):
                if truth(logical('&&', binop('!=', ref(e.get('_loc7_'), 'actionName').get(), ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnAction_1').get(), 'action').get()), lambda: binop('!=', ref(e.get('_loc7_'), 'actionName').get(), ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnAction_2').get(), 'action').get()))):
                    assign(ref(e.get('_loc7_'), 'handCursor'), '=', lambda: False)
            else:
                assign(ref(e.get('_loc7_'), 'handCursor'), '=', lambda: True)
            if truth(ref(e.get('_loc7_'), 'isSetAction').get()):
                assign(ref(e.get('_loc7_'), 'state'), '=', lambda: 3)
            else:
                if truth(ref(e.get('_loc7_'), 'pressed').get()):
                    assign(ref(e.get('_loc7_'), 'state'), '=', lambda: 2)
                else:
                    if truth(logical('&&', binop('==', ref(e.get('_loc7_'), 'actionName').get(), 'preAttack'), lambda: binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready'))):
                        assign(ref(e.get('_loc7_'), 'state'), '=', lambda: 4)
                    else:
                        assign(ref(e.get('_loc7_'), 'state'), '=', lambda: 1)
        except ASContinue:
            pass
        except ASBreak:
            break
    if truth(binop('==', ref(rt.call_ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'getNextTurnAction'), []), 'num').get(), 1)):
        if truth(ref(ref(this, 'model').get(), 'userSelectedActionBtn').get()):
            assign(ref(ref(ref(this, 'view_interface').get(), 'actionTube1').get(), 'state'), '=', lambda: 'open')
        else:
            assign(ref(ref(ref(this, 'view_interface').get(), 'actionTube1').get(), 'state'), '=', lambda: 'closed')
        if truth(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnAction_2').get(), 'action').get()):
            assign(ref(ref(ref(this, 'view_interface').get(), 'actionTube2').get(), 'state'), '=', lambda: 'set')
        else:
            assign(ref(ref(ref(this, 'view_interface').get(), 'actionTube2').get(), 'state'), '=', lambda: 'closed')
    else:
        if truth(binop('==', ref(rt.call_ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'getNextTurnAction'), []), 'num').get(), 2)):
            if truth(ref(ref(this, 'model').get(), 'userSelectedActionBtn').get()):
                assign(ref(ref(ref(this, 'view_interface').get(), 'actionTube2').get(), 'state'), '=', lambda: 'open')
            else:
                assign(ref(ref(ref(this, 'view_interface').get(), 'actionTube2').get(), 'state'), '=', lambda: 'closed')
            if truth(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnAction_1').get(), 'action').get()):
                assign(ref(ref(ref(this, 'view_interface').get(), 'actionTube1').get(), 'state'), '=', lambda: 'set')
            else:
                assign(ref(ref(ref(this, 'view_interface').get(), 'actionTube1').get(), 'state'), '=', lambda: 'closed')
        else:
            if truth(logical('&&', unary('!', rt.call_ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'getNextTurnAction'), [])), lambda: unary('!', ref(this, 'blockAllBtns').get()))):
                assign(ref(ref(ref(this, 'view_interface').get(), 'actionTube1').get(), 'state'), '=', lambda: 'set')
                assign(ref(ref(ref(this, 'view_interface').get(), 'actionTube2').get(), 'state'), '=', lambda: 'set')
                assign(ref(ref(ref(this, 'view_interface').get(), 'turnBtn').get(), 'state'), '=', lambda: 'open')
                rt.call_ref(ref(ref(ref(ref(this, 'view_interface').get(), 'turnBtn').get(), 'btnMC').get(), 'gotoAndStop'), [1])
                assign(ref(ref(ref(ref(this, 'view_interface').get(), 'turnBtn').get(), 'btnMC').get(), 'onPress'), '=', lambda: ASFunction(f_8, e))
    if truth(rt.call_ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'getNextTurnAction'), [])):
        assign(ref(ref(ref(this, 'view_interface').get(), 'turnBtn').get(), 'state'), '=', lambda: 'closed')
    e.set('_loc8_', 0)
    while truth(binop('<', e.get('_loc8_'), ref(ref(ref(this, 'view_interface').get(), 'actionNames_arr').get(), 'length').get())):
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'view_interface').get(), 'actionNames_arr').get(), e.get('_loc8_')).get(), ref(ref(this, 'model').get(), 'userSelectedActionBtn').get())):
                switch_9 = ref(ref(ref(ref(this, 'view_interface').get(), 'stockPanel_mask_states_arr').get(), e.get('_loc8_')).get(), 0).get()
                case_10 = -1
                if case_10 == -1 and strict_eq(switch_9, 0):
                    case_10 = 0
                if case_10 == -1 and strict_eq(switch_9, 1):
                    case_10 = 1
                if case_10 == -1 and strict_eq(switch_9, 2):
                    case_10 = 2
                if case_10 == -1 and strict_eq(switch_9, 3):
                    case_10 = 3
                if case_10 == -1:
                    case_10 = -1
                try:
                    if 0 <= case_10 <= 0:
                        assign(e.ref('_loc10_'), '=', lambda: 1)
                        while truth(binop('<', e.get('_loc10_'), 9)):
                            rt.tick()
                            try:
                                assign(e.ref('_loc11_'), '=', lambda: e.call('Number', [e.get('_loc10_')]))
                                rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_stockPanel_alpha'), [e.get('_loc11_'), 100])
                                assign(e.ref('_loc10_'), '=', lambda: binop('+', e.get('_loc10_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        raise ASBreak()
                    if 0 <= case_10 <= 1:
                        assign(e.ref('_loc12_'), '=', lambda: 1)
                        while truth(binop('<', e.get('_loc12_'), 9)):
                            rt.tick()
                            try:
                                assign(e.ref('_loc13_'), '=', lambda: e.call('Number', [e.get('_loc12_')]))
                                if truth(binop('==', ref(ref(ref(ref(this, 'view_interface').get(), 'stockPanel_mask_states_arr').get(), e.get('_loc8_')).get(), e.get('_loc13_')).get(), 1)):
                                    assign(e.ref('_loc9_'), '=', lambda: 100)
                                else:
                                    assign(e.ref('_loc9_'), '=', lambda: 0)
                                rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_stockPanel_alpha'), [e.get('_loc13_'), e.get('_loc9_')])
                                assign(e.ref('_loc12_'), '=', lambda: binop('+', e.get('_loc12_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        raise ASBreak()
                    if 0 <= case_10 <= 2:
                        assign(e.ref('_loc14_'), '=', lambda: 1)
                        while truth(binop('<', e.get('_loc14_'), 9)):
                            rt.tick()
                            try:
                                assign(e.ref('_loc15_'), '=', lambda: e.call('Number', [e.get('_loc14_')]))
                                if truth(binop('==', ref(ref(ref(ref(this, 'view_interface').get(), 'stockPanel_mask_states_arr').get(), e.get('_loc8_')).get(), e.get('_loc15_')).get(), 1)):
                                    assign(e.ref('_loc9_'), '=', lambda: 100)
                                else:
                                    assign(e.ref('_loc9_'), '=', lambda: 0)
                                rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_stockPanel_alpha'), [e.get('_loc15_'), e.get('_loc9_')])
                                assign(e.ref('_loc14_'), '=', lambda: binop('+', e.get('_loc14_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        raise ASBreak()
                    if 0 <= case_10 <= 3:
                        assign(e.ref('_loc16_'), '=', lambda: 1)
                        while truth(binop('<', e.get('_loc16_'), 9)):
                            rt.tick()
                            try:
                                assign(e.ref('_loc17_'), '=', lambda: e.call('Number', [e.get('_loc16_')]))
                                rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_stockPanel_alpha'), [e.get('_loc17_'), 0])
                                assign(e.ref('_loc16_'), '=', lambda: binop('+', e.get('_loc16_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                except ASBreak:
                    pass
            assign(e.ref('_loc8_'), '=', lambda: binop('+', e.get('_loc8_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    if truth(binop('==', ref(ref(e.get('_global'), 'model').get(), 'view_leader_MCs_played').get(), 'done')):
        assign(e.ref('_loc18_'), '=', lambda: 1)
        while truth(binop('<', e.get('_loc18_'), ref(ref(ref(this, 'model').get(), 'playerArr').get(), 'length').get())):
            rt.tick()
            try:
                assign(e.ref('_loc19_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('_loc18_')).get())
                assign(e.ref('_loc20_'), '=', lambda: ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), binop('+', 'leaderMC', e.get('_loc18_'))).get())
                assign(ref(e.get('_loc20_'), 'num'), '=', lambda: e.get('_loc18_'))
                assign(e.ref('_loc22_'), '=', lambda: 0)
                rt.call_ref(ref(ref(e.get('_loc20_'), 'cfIcon1').get(), 'gotoAndStop'), [1])
                rt.call_ref(ref(ref(e.get('_loc20_'), 'cfIcon2').get(), 'gotoAndStop'), [1])
                rt.call_ref(ref(ref(e.get('_loc20_'), 'cfIcon3').get(), 'gotoAndStop'), [1])
                assign(e.ref('_loc23_'), '=', lambda: 1)
                while truth(binop('<', e.get('_loc23_'), ref(ref(e.get('_loc19_'), 'ceaseFireArr').get(), 'length').get())):
                    rt.tick()
                    try:
                        if truth(ref(ref(ref(e.get('_loc19_'), 'ceaseFireArr').get(), e.get('_loc23_')).get(), '_status').get()):
                            assign(e.ref('_loc22_'), '=', lambda: binop('+', e.get('_loc22_'), 1))
                            rt.call_ref(ref(ref(e.get('_loc20_'), binop('+', 'cfIcon', e.get('_loc22_'))).get(), 'gotoAndStop'), [2])
                            assign(e.ref('_loc24_'), '=', lambda: rt.construct(e.get('Color'), [ref(e.get('_loc20_'), binop('+', 'cfIcon', e.get('_loc22_'))).get()]))
                            rt.call_ref(ref(e.get('_loc24_'), 'setTransform'), [ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('_loc23_')).get(), 'playerColorTint1').get()])
                        assign(e.ref('_loc23_'), '=', lambda: binop('+', e.get('_loc23_'), 1))
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
                if truth(ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'ceaseFireArr').get(), e.get('_loc18_')).get(), '_status').get()):
                    assign(e.ref('_loc25_'), '=', lambda: rt.construct(e.get('Color'), [ref(e.get('_loc20_'), 'iconCeaseFire').get()]))
                    rt.call_ref(ref(e.get('_loc25_'), 'setTransform'), [ref(ref(ref(this, 'model').get(), 'human').get(), 'playerColorTint1').get()])
                    rt.call_ref(ref(ref(e.get('_loc20_'), 'iconCeaseFire').get(), 'gotoAndStop'), [2])
                    assign(ref(ref(ref(e.get('_loc20_'), 'iconCeaseFire').get(), 'txt').get(), 'text'), '=', lambda: ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'ceaseFireArr').get(), e.get('_loc18_')).get(), '_turnsLeft').get())
                else:
                    rt.call_ref(ref(ref(e.get('_loc20_'), 'iconCeaseFire').get(), 'gotoAndStop'), [1])
                if truth(ref(e.get('_loc19_'), 'bioloaded').get()):
                    rt.call_ref(ref(ref(e.get('_loc20_'), 'iconBio').get(), 'gotoAndStop'), [2])
                else:
                    rt.call_ref(ref(ref(e.get('_loc20_'), 'iconBio').get(), 'gotoAndStop'), [1])
                assign(e.ref('_loc21_'), '=', lambda: ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), binop('+', binop('+', binop('+', 'leaderStat', e.get('_loc18_')), '_'), 1)).get(), 'maskMC').get())
                assign(ref(e.get('_loc21_'), '_yscale'), '=', lambda: ref(ref(e.get('_loc19_'), 'regardArr').get(), 0).get())
                assign(e.ref('_loc21_'), '=', lambda: ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), binop('+', binop('+', binop('+', 'leaderStat', e.get('_loc18_')), '_'), 2)).get(), 'maskMC').get())
                assign(ref(e.get('_loc21_'), '_yscale'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'populationPercentage'), [e.get('_loc19_')]))
                assign(e.ref('_loc18_'), '=', lambda: binop('+', e.get('_loc18_'), 1))
            except ASContinue:
                pass
            except ASBreak:
                break
    else:
        if truth(binop('==', ref(ref(e.get('_global'), 'model').get(), 'view_leader_MCs_played').get(), 'false')):
            rt.call_ref(ref(this, 'set_leader_face_MC_sequence'), [])
    if truth(binop('==', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), 'preAttack')):
        if truth(binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready')):
            rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_stockPanel_alpha'), [0, 0])
            rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_stockPanel_alpha'), [1, 0])
            rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_stockPanel_alpha'), [2, 0])
            rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_stockPanel_alpha'), [3, 0])
            rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_stockPanel_alpha'), [4, 100])
            rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_stockPanel_alpha'), [5, 100])
    if truth(binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponName').get(), 'space')):
        rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_stockPanel_alpha'), [3, 100])
        rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_stockPanel_alpha'), [4, 0])
        rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_stockPanel_alpha'), [5, 0])
    if truth(logical('&&', logical('||', binop('==', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), 'attack'), lambda: logical('||', binop('==', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), 'preAttack'), lambda: binop('==', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), 'propaganda'))), lambda: binop('!=', ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'weaponType').get(), 'spy'))):
        rt.call_ref(ref(this, 'colorCities'), ['attackable'])
    else:
        if truth(binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'weaponType').get(), 'spy')):
            rt.call_ref(ref(this, 'colorCities'), ['allEnemy'])
        else:
            rt.call_ref(ref(this, 'colorCities'), ['default'])
    if truth(binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready')):
        pass
    if truth(binop('==', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), 'attack')):
        if truth(binop('>=', ref(ref(ref(this, 'model').get(), 'human').get(), 'spy_readiness').get(), 25)):
            pass
    assign(ref(ref(ref(this, 'view_interface').get(), 'btn_sound').get(), 'state'), '=', lambda: ref(ref(ref(this, 'model').get(), 'option').get(), 'sound').get())
    assign(ref(ref(ref(this, 'view_interface').get(), 'btn_music').get(), 'state'), '=', lambda: ref(ref(ref(this, 'model').get(), 'option').get(), 'music').get())
    rt.call_ref(ref(ref(this, 'view').get(), 'updateCities'), [])
    rt.call_ref(ref(this, 'update_statistics'), [])
    rt.call_ref(ref(this, 'update_centerScreenContent'), [])
    rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_highScore'), [ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'score').get()])
    return U

def Sub_Presenter_interface_do_leader_face_MC_sequence_itteration(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Sub_Presenter_interface')
    if truth(binop('<', ref(ref(this, 'model').get(), 'view_leader_MCs_played_count').get(), ref(ref(this, 'model').get(), 'view_leader_MCs_played_max').get())):
        assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(ref(this, 'model').get(), 'view_leader_MCs_played_count').get()).get())
        rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_leaderFace'), [ref(e.get('_loc2_'), 'playerNum').get(), ref(e.get('_loc2_'), 'faceFrame').get(), ref(e.get('_loc2_'), 'alive').get(), False])
        rt.call_ref(ref(this, 'play_sound_by_action'), ['interface_noise'])
    else:
        rt.call_ref(ref(this, 'play_sound_by_action'), ['interface_startup'])
        rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(this, 'model').get(), 'view_leader_MCs_sequence_interval_id').get()])
        assign(ref(ref(e.get('_global'), 'model').get(), 'view_leader_MCs_played'), '=', lambda: 'done')
        rt.call_ref(ref(this, 'update_leaderFaces'), [])
        rt.call_ref(ref(this, 'updateView'), [])
    update(ref(ref(this, 'model').get(), 'view_leader_MCs_played_count'), 1, False)
    return U

def Sub_Presenter_interface_update_top_plrColor(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_'], closure, 'Sub_Presenter_interface')
    e.set('_loc2_', 0)
    while truth(binop('<', e.get('_loc2_'), 5)):
        rt.tick()
        try:
            rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_top_plrColor'), [e.get('_loc2_'), 'empty'])
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc3_', 0)
    while truth(binop('<', e.get('_loc3_'), ref(ref(ref(this, 'model').get(), 'playerArr').get(), 'length').get())):
        rt.tick()
        try:
            rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_top_plrColor'), [e.get('_loc3_'), ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('_loc3_')).get(), 'playerColor').get()])
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Sub_Presenter_interface_update_color_dots(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_Presenter_interface')
    rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_color_dot'), [1, ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'playerColor').get()])
    rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_color_dot'), [2, ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'playerColor').get()])
    return U

def Sub_Presenter_interface_update_statistics(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', 'i'], closure, 'Sub_Presenter_interface')
    e.set('_loc2_', 0)
    assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'techTree').get(), 'techLevel').get())
    rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_statBar'), [1, e.get('_loc2_')])
    assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'human').get(), 'religion').get())
    rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_statBar'), [2, e.get('_loc2_')])
    e.set('_loc3_', 0)
    for key_11 in keys(ref(ref(this, 'model').get(), 'activePlayerArr').get()):
        e.ref('i').set(key_11)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '+=', lambda: ref(ref(ref(ref(this, 'model').get(), 'activePlayerArr').get(), e.get('i')).get(), 'population').get())
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(e.ref('_loc2_'), '=', lambda: binop('*', binop('/', ref(ref(ref(this, 'model').get(), 'human').get(), 'population').get(), e.get('_loc3_')), 100))
    rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_statBar'), [3, e.get('_loc2_')])
    assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'human').get(), 'spy_readiness').get())
    rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_statBar'), [4, e.get('_loc2_')])
    rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_statMoney'), [ref(ref(ref(this, 'model').get(), 'human').get(), 'turnMoney').get()])
    return U

def Sub_Presenter_interface___get__display_textFunds(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_Presenter_interface')
    return binop('+', 'Budget: ', ref(ref(this, 'model').get(), 'display_turnMoney').get())
    return U

def Sub_Presenter_interface___get__display_population(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_Presenter_interface')
    return binop('+', rt.call_ref(ref(e.get('Math'), 'round'), [binop('*', ref(ref(ref(this, 'model').get(), 'human').get(), 'population').get(), 0.1)]), '.000.000')
    return U

def f_14(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(e.get('_global'), 'model').get(), 'force_error_window'), '=', lambda: False)
    assign(ref(ref(e.get('_global'), 'model').get(), 'force_error_window_text'), '=', lambda: '')
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'update_centerScreenContent'), [])
    return U

def f_15(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPressed_spyBuilding'), [ref(this, 'num').get()])
    return U

def f_16(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(e.get('_global'), 'model').get(), 'interface_spy_error'), '=', lambda: e.get('undefined'))
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'update_centerScreenContent'), [])
    return U

def f_17(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'gotoAndStop'), [2])
    return U

def f_18(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'gotoAndStop'), [1])
    return U

def f_19(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPressed_diplomacy'), ['leader', ref(this, 'num').get()])
    return U

def f_20(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPressed_diplomacy'), ['option', ref(this, 'option').get()])
    return U

def f_21(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(e.get('_global'), 'model').get(), 'interface_diplomacy_error'), '=', lambda: e.get('undefined'))
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'update_centerScreenContent'), [])
    return U

def f_22(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'gotoAndStop'), [2])
    return U

def f_23(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'gotoAndStop'), [1])
    return U

def f_24(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(e.get('_global'), 'model').get(), 'interface_diplomacy_error'), '=', lambda: e.get('undefined'))
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'update_centerScreenContent'), [])
    return U

def f_25(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'gotoAndStop'), [2])
    return U

def f_26(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'gotoAndStop'), [1])
    return U

def f_27(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPressed_index_c'), [this])
    return U

def f_28(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(unary('!', rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'do_ch_func'), [ref(ref(e.get('sc'), 'chTXT').get(), 'text').get()]))):
        assign(ref(ref(e.get('_global'), 'model').get(), 'userSelectedActionBtn'), '=', lambda: e.get('undefined'))
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'updateView'), [])
    else:
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'update_centerScreenContent'), [])
    return U

def Sub_Presenter_interface_update_centerScreenContent(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc14_', '_loc15_', '_loc16_', '_loc17_', '_loc18_', '_loc19_', '_loc20_', '_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', 'sc'], closure, 'Sub_Presenter_interface')
    if truth(ref(ref(this, 'model').get(), 'userSelectedActionBtn').get()):
        rt.call_ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), 'gotoAndStop'), [ref(ref(this, 'model').get(), 'userSelectedActionBtn').get()])
    else:
        rt.call_ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), 'gotoAndStop'), [1])
    e.set('sc', ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get())
    e.set('_loc2_', False)
    e.set('_loc3_', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get())
    if truth(ref(ref(e.get('_global'), 'model').get(), 'force_error_window').get()):
        assign(e.ref('_loc3_'), '=', lambda: 'force_error')
    switch_12 = e.get('_loc3_')
    case_13 = -1
    if case_13 == -1 and strict_eq(switch_12, 'force_error'):
        case_13 = 0
    if case_13 == -1 and strict_eq(switch_12, 'skip_action'):
        case_13 = 1
    if case_13 == -1 and strict_eq(switch_12, 'cancelPreAttack'):
        case_13 = 2
    if case_13 == -1 and strict_eq(switch_12, 'resources'):
        case_13 = 3
    if case_13 == -1 and strict_eq(switch_12, 'production'):
        case_13 = 4
    if case_13 == -1 and strict_eq(switch_12, 'research'):
        case_13 = 5
    if case_13 == -1 and strict_eq(switch_12, 'religion'):
        case_13 = 6
    if case_13 == -1 and strict_eq(switch_12, 'attack'):
        case_13 = 7
    if case_13 == -1 and strict_eq(switch_12, 'preAttack'):
        case_13 = 8
    if case_13 == -1 and strict_eq(switch_12, 'defense'):
        case_13 = 9
    if case_13 == -1 and strict_eq(switch_12, 'propaganda'):
        case_13 = 10
    if case_13 == -1 and strict_eq(switch_12, 'diplomacy'):
        case_13 = 11
    if case_13 == -1 and strict_eq(switch_12, 'diplomacyPending'):
        case_13 = 12
    if case_13 == -1 and strict_eq(switch_12, 'help'):
        case_13 = 13
    if case_13 == -1 and strict_eq(switch_12, 'cheat'):
        case_13 = 14
    if case_13 == -1:
        case_13 = -1
    try:
        if 0 <= case_13 <= 0:
            rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['production_error'])
            assign(ref(ref(ref(e.get('sc'), 'error_window').get(), 'text1').get(), 'text'), '=', lambda: ref(ref(e.get('_global'), 'model').get(), 'force_error_window_text').get())
            assign(ref(ref(ref(e.get('sc'), 'error_window').get(), 'btnOK').get(), 'onPress'), '=', lambda: ASFunction(f_14, e))
            assign(ref(ref(e.get('sc'), 'btnAccept').get(), '_visible'), '=', lambda: False)
            assign(ref(ref(e.get('sc'), 'btnCancel').get(), '_visible'), '=', lambda: False)
            raise ASBreak()
        if 0 <= case_13 <= 1:
            rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
            raise ASBreak()
        if 0 <= case_13 <= 2:
            rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['preCancel'])
            rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
            raise ASBreak()
        if 0 <= case_13 <= 3:
            rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
            assign(ref(ref(e.get('sc'), 'text1').get(), 'text'), '=', lambda: ref(ref(this, 'model').get(), 'display_population').get())
            assign(ref(ref(e.get('sc'), 'text2').get(), 'text'), '=', lambda: binop('+', rt.call_ref(ref(e.get('Math'), 'round'), [binop('/', ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'population').get(), ref(ref(ref(ref(e.get('_global'), 'model').get(), 'difficulty_level_specific_vars').get(), 'player_resources_divider').get(), ref(ref(e.get('_global'), 'model').get(), 'difficulty_level').get()).get())]), '.000.000'))
            assign(ref(ref(e.get('sc'), 'textFunds').get(), 'text'), '=', lambda: ref(this, 'display_textFunds').get())
            raise ASBreak()
        if 0 <= case_13 <= 4:
            if truth(unary('!', ref(ref(this, 'model').get(), 'interface_production_error').get())):
                if truth(binop('==', ref(ref(this, 'model').get(), 'userSelectedProductionInvestmentArr_total_amount').get(), 0)):
                    rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['hide'])
                else:
                    rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
                rt.call_ref(ref(this, 'loadProductionFunc'), [])
            else:
                rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['production_error'])
                rt.call_ref(ref(this, 'loadProductionFunc'), [ref(ref(this, 'model').get(), 'interface_production_error').get()])
            raise ASBreak()
        if 0 <= case_13 <= 5:
            if truth(unary('!', ref(ref(this, 'model').get(), 'interface_research_error').get())):
                if truth(unary('!', ref(ref(ref(this, 'model').get(), 'userSelectedResearchArr').get(), 0).get())):
                    rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['hide'])
                else:
                    rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
                rt.call_ref(ref(this, 'loadResearchFunc'), [])
            else:
                rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['research_error'])
                rt.call_ref(ref(this, 'loadResearchFunc'), [ref(ref(this, 'model').get(), 'interface_research_error').get()])
            rt.call_ref(ref(ref(e.get('sc'), 'MC1').get(), 'gotoAndStop'), [ref(ref(ref(this, 'model').get(), 'human').get(), 'religion_code').get()])
            raise ASBreak()
        if 0 <= case_13 <= 6:
            rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'human').get(), 'religion').get())
            assign(e.ref('_loc5_'), '=', lambda: binop('-', ref(ref(ref(ref(this, 'model').get(), 'difficulty_level_specific_vars').get(), 'player_religion_addition').get(), ref(ref(this, 'model').get(), 'difficulty_level').get()).get(), 10))
            if truth(binop('>', binop('+', e.get('_loc4_'), e.get('_loc5_')), 100)):
                assign(e.ref('_loc5_'), '=', lambda: binop('-', 100, e.get('_loc4_')))
            if truth(binop('<', e.get('_loc5_'), 0)):
                assign(e.ref('_loc5_'), '=', lambda: 0)
            assign(ref(ref(e.get('sc'), 'text1').get(), 'text'), '=', lambda: ref(this, 'display_population').get())
            assign(ref(ref(e.get('sc'), 'text2').get(), 'text'), '=', lambda: binop('+', ref(ref(ref(this, 'model').get(), 'human').get(), 'religion').get(), '%'))
            rt.call_ref(ref(ref(e.get('sc'), 'MC1').get(), 'gotoAndStop'), [ref(ref(ref(this, 'model').get(), 'human').get(), 'religion_code').get()])
            assign(ref(ref(e.get('sc'), 'text3').get(), 'text'), '=', lambda: binop('+', binop('+', '+', e.get('_loc5_')), ' %'))
            assign(ref(ref(ref(e.get('sc'), 'stat1').get(), 'maskMC').get(), '_xscale'), '=', lambda: ref(ref(ref(this, 'model').get(), 'human').get(), 'religion').get())
            raise ASBreak()
        if 0 <= case_13 <= 7:
            rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['attack1'])
            if truth(ref(ref(this, 'model').get(), 'userSelectedWeapon').get()):
                if truth(unary('!', ref(ref(this, 'model').get(), 'userSelectedCity').get())):
                    assign(e.ref('_loc2_'), '=', lambda: True)
                    assign(ref(ref(this, 'view_interface').get(), 'infoLine'), '=', lambda: 'selectWeapon')
                    rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['hide'])
                    rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['attack1'])
                else:
                    if truth(binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'weaponType').get(), 'spy')):
                        rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['attack_spy'])
                        rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
                        rt.call_ref(ref(ref(e.get('sc'), 'buildingsMC').get(), 'gotoAndStop'), [logical('||', ref(ref(this, 'model').get(), 'userSelectedSpyBuilding').get(), lambda: 'spyCenter')])
                        assign(e.ref('_loc6_'), '=', lambda: 1)
                        while truth(binop('<', e.get('_loc6_'), 6)):
                            rt.tick()
                            try:
                                assign(ref(ref(e.get('sc'), binop('+', 'btn', e.get('_loc6_'))).get(), 'num'), '=', lambda: e.get('_loc6_'))
                                assign(ref(ref(e.get('sc'), binop('+', 'btn', e.get('_loc6_'))).get(), 'onPress'), '=', lambda: ASFunction(f_15, e))
                                assign(e.ref('_loc6_'), '=', lambda: binop('+', e.get('_loc6_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        assign(e.ref('_loc7_'), '=', lambda: 1)
                        while truth(binop('<', e.get('_loc7_'), 6)):
                            rt.tick()
                            try:
                                rt.call_ref(ref(ref(ref(e.get('sc'), 'buildingsMC').get(), binop('+', 'mc', e.get('_loc7_'))).get(), 'gotoAndStop'), [ref(ref(ref(this, 'model').get(), 'human').get(), 'religion_code').get()])
                                assign(e.ref('_loc7_'), '=', lambda: binop('+', e.get('_loc7_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                    else:
                        rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['attack2'])
                        rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
                        if truth(binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'weaponType').get(), 'soldier')):
                            rt.call_ref(ref(ref(e.get('sc'), 'MC1').get(), 'gotoAndStop'), [ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'weaponName').get()])
                        else:
                            rt.call_ref(ref(ref(e.get('sc'), 'MC1').get(), 'gotoAndStop'), ['spy'])
                            assign(ref(ref(ref(ref(e.get('sc'), 'MC1').get(), 'statBar').get(), 'statMask').get(), '_xscale'), '=', lambda: ref(ref(ref(this, 'model').get(), 'human').get(), 'spy_readiness').get())
                        assign(e.ref('_loc8_'), '=', lambda: binop('+', ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'weaponLevel').get(), 1))
                        if truth(binop('==', e.get('_loc8_'), 5)):
                            assign(e.ref('_loc8_'), '=', lambda: 1)
                        rt.call_ref(ref(ref(e.get('sc'), 'MC2').get(), 'gotoAndStop'), [e.get('_loc8_')])
            else:
                rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['attackSelect'])
                rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['hide'])
            if truth(ref(ref(this, 'model').get(), 'interface_spy_error').get()):
                rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['spy_error'])
                assign(ref(ref(ref(e.get('sc'), 'error_window').get(), 'text1').get(), 'text'), '=', lambda: ref(ref(e.get('_global'), 'model').get(), 'interface_spy_error').get())
                assign(ref(ref(ref(e.get('sc'), 'statBar').get(), 'statMask').get(), '_xscale'), '=', lambda: ref(ref(ref(this, 'model').get(), 'human').get(), 'spy_readiness').get())
                assign(ref(ref(ref(e.get('sc'), 'error_window').get(), 'btnOK').get(), 'onPress'), '=', lambda: ASFunction(f_16, e))
                assign(ref(ref(ref(e.get('sc'), 'error_window').get(), 'btnOK').get(), 'onRollOver'), '=', lambda: ASFunction(f_17, e))
                assign(ref(ref(ref(e.get('sc'), 'error_window').get(), 'btnOK').get(), 'onRollOut'), '=', lambda: ASFunction(f_18, e))
            raise ASBreak()
        if 0 <= case_13 <= 8:
            if truth(binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready')):
                if truth(ref(ref(this, 'model').get(), 'userSelectedWeapon').get()):
                    if truth(logical('&&', unary('!', ref(ref(this, 'model').get(), 'userSelectedCity').get()), lambda: binop('!=', ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponName').get(), 'ship'))):
                        assign(e.ref('_loc2_'), '=', lambda: True)
                        assign(ref(ref(this, 'view_interface').get(), 'infoLine'), '=', lambda: 'selectWeapon')
                        rt.call_ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), 'gotoAndStop'), ['preAttack4'])
                        rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['hide'])
                    else:
                        if truth(binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponName').get(), 'ship')):
                            if truth(binop('<', ref(ref(ref(this, 'model').get(), 'ship_attack_arr').get(), 'length').get(), 3)):
                                assign(e.ref('_loc2_'), '=', lambda: True)
                                assign(ref(ref(this, 'view_interface').get(), 'infoLine'), '=', lambda: 'selectWeapon')
                                rt.call_ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), 'gotoAndStop'), ['preAttack4'])
                                rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
                            else:
                                rt.call_ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), 'gotoAndStop'), ['ship2'])
                                rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
                        else:
                            if truth(ref(ref(this, 'model').get(), 'userSelectedCity').get()):
                                rt.call_ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), 'gotoAndStop'), ['preAttack3'])
                                rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
                                assign(ref(ref(e.get('sc'), 'text1').get(), 'text'), '=', lambda: ref(ref(this, 'megaton_by_level_arr').get(), ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'weaponLevel').get()).get())
                                if truth(binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'desireGroup').get(), 2)):
                                    rt.call_ref(ref(ref(e.get('sc'), 'MC1').get(), 'gotoAndStop'), [1])
                                    rt.call_ref(ref(ref(e.get('sc'), 'MC2').get(), 'gotoAndStop'), [2])
                                else:
                                    rt.call_ref(ref(ref(e.get('sc'), 'MC1').get(), 'gotoAndStop'), [2])
                                    rt.call_ref(ref(ref(e.get('sc'), 'MC2').get(), 'gotoAndStop'), [1])
                                if truth(binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'weaponName').get(), 'specialLoad')):
                                    rt.call_ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), 'gotoAndStop'), ['preAttack_space'])
                                    rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
                else:
                    if truth(binop('!=', ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponName').get(), 'ship')):
                        assign(ref(ref(this, 'view_interface').get(), 'infoLine'), '=', lambda: 'selectCity')
                        rt.call_ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), 'gotoAndStop'), ['preAttack2'])
                        rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
                    else:
                        assign(ref(ref(this, 'view_interface').get(), 'infoLine'), '=', lambda: 'selectCity')
                        rt.call_ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), 'gotoAndStop'), ['ship1'])
                        rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
                        rt.call_ref(ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), 'planeCount').get(), 'gotoAndStop'), [binop('+', ref(ref(ref(this, 'model').get(), 'ship_attack_arr').get(), 'length').get(), 1)])
                        if truth(binop('==', ref(ref(ref(this, 'model').get(), 'ship_attack_arr').get(), 'length').get(), 3)):
                            rt.call_ref(ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), 'mc_select').get(), 'gotoAndStop'), [2])
            else:
                if truth(ref(ref(this, 'model').get(), 'userSelectedWeapon').get()):
                    rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['preAttack1'])
                    rt.call_ref(ref(ref(e.get('sc'), 'MC1').get(), 'gotoAndStop'), [ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'weaponName').get()])
                    rt.call_ref(ref(ref(e.get('sc'), 'MC2').get(), 'gotoAndStop'), [ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'weaponName').get()])
                    rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
                    if truth(binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'weaponName').get(), 'space')):
                        rt.call_ref(ref(ref(ref(e.get('sc'), 'MC2').get(), 'satIMG').get(), 'gotoAndStop'), [ref(ref(ref(this, 'model').get(), 'human').get(), 'religion').get()])
                else:
                    assign(ref(ref(this, 'view_interface').get(), 'infoLine'), '=', lambda: 'selectWeapon')
                    rt.call_ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), 'gotoAndStop'), ['preAttackSelect'])
                    rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['hide'])
            raise ASBreak()
        if 0 <= case_13 <= 9:
            if truth(ref(ref(this, 'model').get(), 'userSelectedWeapon').get()):
                rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
                rt.call_ref(ref(ref(e.get('sc'), 'mc1').get(), 'gotoAndStop'), [ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'weaponName').get()])
                if truth(binop('==', ref(ref(e.get('sc'), 'mc1').get(), '_currentframe').get(), 2)):
                    rt.call_ref(ref(ref(e.get('sc'), 'mc2').get(), 'gotoAndStop'), [1])
                else:
                    rt.call_ref(ref(ref(e.get('sc'), 'mc2').get(), 'gotoAndStop'), [2])
            else:
                assign(ref(ref(this, 'view_interface').get(), 'infoLine'), '=', lambda: 'selectWeapon')
                rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['defenseSelect'])
                rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['hide'])
            raise ASBreak()
        if 0 <= case_13 <= 10:
            if truth(ref(ref(this, 'model').get(), 'userSelectedCity').get()):
                rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
                rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['propaganda2'])
                assign(ref(ref(e.get('sc'), 'text1').get(), 'text'), '=', lambda: binop('+', binop('+', 'Propaganda strength: ', ref(ref(ref(this, 'model').get(), 'human').get(), 'religion').get()), ' %'))
            else:
                assign(e.ref('_loc2_'), '=', lambda: True)
                assign(ref(ref(this, 'view_interface').get(), 'infoLine'), '=', lambda: 'selectCity')
                rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['propaganda1'])
                rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['hide'])
            raise ASBreak()
        if 0 <= case_13 <= 11:
            if truth(unary('!', ref(ref(e.get('_global'), 'model').get(), 'interface_diplomacy_error').get())):
                assign(e.ref('_loc9_'), '=', lambda: 1)
                assign(e.ref('_loc10_'), '=', lambda: 0)
                while truth(binop('<', e.get('_loc10_'), 5)):
                    rt.tick()
                    try:
                        rt.call_ref(ref(ref(e.get('sc'), binop('+', 'leaderMC', e.get('_loc10_'))).get(), 'gotoAndStop'), ['black'])
                        assign(e.ref('_loc10_'), '=', lambda: binop('+', e.get('_loc10_'), 1))
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
                assign(e.ref('_loc11_'), '=', lambda: 0)
                while truth(binop('<', e.get('_loc11_'), ref(ref(ref(this, 'model').get(), 'playerArr').get(), 'length').get())):
                    rt.tick()
                    try:
                        assign(e.ref('_loc12_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('_loc11_')).get())
                        if truth(binop('!=', e.get('_loc12_'), ref(ref(this, 'model').get(), 'human').get())):
                            assign(e.ref('_loc13_'), '=', lambda: ref(e.get('sc'), binop('+', 'leaderMC', e.get('_loc9_'))).get())
                            if truth(logical('&&', unary('!', ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'ceaseFireArr').get(), ref(e.get('_loc12_'), 'playerNum').get()).get(), '_status').get()), lambda: ref(e.get('_loc12_'), 'alive').get())):
                                rt.call_ref(ref(e.get('_loc13_'), 'gotoAndStop'), [ref(e.get('_loc12_'), 'faceFrame').get()])
                                assign(ref(e.get('_loc13_'), 'num'), '=', lambda: e.get('_loc11_'))
                                assign(ref(e.get('_loc13_'), 'onPress'), '=', lambda: ASFunction(f_19, e))
                            else:
                                rt.call_ref(ref(e.get('_loc13_'), 'gotoAndStop'), ['black'])
                            if truth(binop('==', e.get('_loc11_'), ref(ref(this, 'model').get(), 'userSelectedDiplomacyLeader').get())):
                                rt.call_ref(ref(ref(e.get('sc'), binop('+', 'leaderSelected', e.get('_loc9_'))).get(), 'gotoAndStop'), [2])
                            else:
                                rt.call_ref(ref(ref(e.get('sc'), binop('+', 'leaderSelected', e.get('_loc9_'))).get(), 'gotoAndStop'), [1])
                            assign(e.ref('_loc9_'), '=', lambda: binop('+', e.get('_loc9_'), 1))
                        assign(e.ref('_loc11_'), '=', lambda: binop('+', e.get('_loc11_'), 1))
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
                assign(e.ref('_loc14_'), '=', lambda: 0)
                while truth(binop('<', e.get('_loc14_'), ref(ref(ref(this, 'model').get(), 'diplomacy_options_arr').get(), 'length').get())):
                    rt.tick()
                    try:
                        assign(e.ref('_loc15_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'diplomacy_options_arr').get(), e.get('_loc14_')).get())
                        assign(e.ref('_loc16_'), '=', lambda: ref(e.get('sc'), binop('+', 'btn', binop('+', e.get('_loc14_'), 1))).get())
                        if truth(binop('==', ref(e.get('_loc15_'), 0).get(), 'offer')):
                            assign(ref(ref(e.get('sc'), binop('+', 'text', binop('+', e.get('_loc14_'), 1))).get(), 'text'), '=', lambda: binop('+', binop('+', 'turns no attack, I pay $ ', ref(e.get('_loc15_'), 2).get()), ' mln'))
                        if truth(binop('==', ref(e.get('_loc15_'), 0).get(), 'demand')):
                            assign(ref(ref(e.get('sc'), binop('+', 'text', binop('+', e.get('_loc14_'), 1))).get(), 'text'), '=', lambda: binop('+', binop('+', 'turns no attack pay me $ ', ref(e.get('_loc15_'), 2).get()), ' mln'))
                        if truth(binop('==', e.get('_loc14_'), ref(ref(this, 'model').get(), 'userSelectedDiplomacyOption').get())):
                            rt.call_ref(ref(e.get('_loc16_'), 'gotoAndStop'), [2])
                            assign(ref(ref(e.get('sc'), binop('+', 'text', binop('+', e.get('_loc14_'), 1))).get(), 'textColor'), '=', lambda: 65280)
                        else:
                            rt.call_ref(ref(e.get('_loc16_'), 'gotoAndStop'), [1])
                            assign(ref(ref(e.get('sc'), binop('+', 'text', binop('+', e.get('_loc14_'), 1))).get(), 'textColor'), '=', lambda: 16777215)
                        rt.call_ref(ref(e.get('_loc16_'), 'gotoAndStop'), [1])
                        assign(ref(ref(e.get('_loc16_'), 'text1').get(), 'text'), '=', lambda: ref(e.get('_loc15_'), 1).get())
                        assign(ref(e.get('_loc16_'), 'option'), '=', lambda: e.get('_loc14_'))
                        assign(ref(e.get('_loc16_'), 'onPress'), '=', lambda: ASFunction(f_20, e))
                        assign(e.ref('_loc14_'), '=', lambda: binop('+', e.get('_loc14_'), 1))
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
                if truth(logical('||', unary('!', ref(ref(this, 'model').get(), 'userSelectedDiplomacyLeader').get()), lambda: binop('==', ref(ref(this, 'model').get(), 'userSelectedDiplomacyOption').get(), e.get('undefined')))):
                    rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['hide'])
                else:
                    rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
                assign(ref(ref(e.get('sc'), 'textFunds').get(), 'text'), '=', lambda: ref(this, 'display_textFunds').get())
            else:
                rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['diplomacy_error'])
                assign(ref(ref(ref(e.get('sc'), 'error_window').get(), 'text1').get(), 'text'), '=', lambda: ref(ref(e.get('_global'), 'model').get(), 'interface_diplomacy_error').get())
                assign(ref(ref(ref(e.get('sc'), 'error_window').get(), 'btnOK').get(), 'onPress'), '=', lambda: ASFunction(f_21, e))
                assign(ref(ref(ref(e.get('sc'), 'error_window').get(), 'btnOK').get(), 'onRollOver'), '=', lambda: ASFunction(f_22, e))
                assign(ref(ref(ref(e.get('sc'), 'error_window').get(), 'btnOK').get(), 'onRollOut'), '=', lambda: ASFunction(f_23, e))
            raise ASBreak()
        if 0 <= case_13 <= 12:
            if truth(unary('!', ref(ref(e.get('_global'), 'model').get(), 'interface_diplomacy_error').get())):
                assign(ref(this, 'curDiplomacyObj'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'diplomacyPendingArr').get(), 0).get())
                assign(ref(this, 'curDiplomacyOptionArr'), '=', lambda: ref(ref(ref(this, 'model').get(), 'diplomacy_options_arr').get(), ref(ref(this, 'curDiplomacyObj').get(), '_option').get()).get())
                if truth(binop('==', ref(ref(this, 'curDiplomacyOptionArr').get(), 0).get(), 'offer')):
                    rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['diplomacyOffer'])
                else:
                    if truth(binop('==', ref(ref(this, 'curDiplomacyOptionArr').get(), 0).get(), 'demand')):
                        rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['diplomacyDemand'])
                rt.call_ref(ref(ref(e.get('sc'), 'leaderMC1').get(), 'gotoAndStop'), [ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(ref(this, 'curDiplomacyObj').get(), '_leader').get()).get(), 'faceFrame').get()])
                assign(ref(ref(ref(e.get('sc'), 'btn1').get(), 'text1').get(), 'text'), '=', lambda: ref(ref(this, 'curDiplomacyOptionArr').get(), 1).get())
                rt.call_ref(ref(ref(e.get('sc'), 'btn1').get(), 'gotoAndStop'), [1])
                assign(ref(ref(e.get('sc'), 'text1').get(), 'text'), '=', lambda: binop('+', binop('+', ' $ ', ref(ref(this, 'curDiplomacyOptionArr').get(), 2).get()), '.000.000'))
                rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
                assign(e.ref('_loc18_'), '=', lambda: obj({'ra': 0, 'rb': 0, 'ga': 0, 'gb': 0, 'ba': 0, 'bb': 0, 'aa': 0, 'ab': 0}))
                assign(e.ref('_loc19_'), '=', lambda: 0)
                while truth(binop('<', e.get('_loc19_'), 5)):
                    rt.tick()
                    try:
                        assign(e.ref('_loc17_'), '=', lambda: rt.construct(e.get('Color'), [ref(ref(ref(e.get('sc'), 'mcapMC').get(), 'schemeMC').get(), binop('+', 'mc', e.get('_loc19_'))).get()]))
                        rt.call_ref(ref(e.get('_loc17_'), 'setTransform'), [obj({'ra': 100, 'rb': 0, 'ga': 100, 'gb': 0, 'ba': 100, 'bb': 0, 'aa': 100, 'ab': 0})])
                        assign(e.ref('_loc19_'), '=', lambda: binop('+', e.get('_loc19_'), 1))
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
                assign(e.ref('_loc20_'), '=', lambda: rt.construct(e.get('Color'), [ref(ref(ref(e.get('sc'), 'mapMC').get(), 'schemeMC').get(), binop('+', 'mc', ref(ref(this, 'curDiplomacyObj').get(), '_leader').get())).get()]))
                rt.call_ref(ref(e.get('_loc20_'), 'setTransform'), [ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(ref(this, 'curDiplomacyObj').get(), '_leader').get()).get(), 'playerColorTint1').get()])
                assign(ref(ref(e.get('sc'), 'textFunds').get(), 'text'), '=', lambda: ref(this, 'display_textFunds').get())
            else:
                rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), ['diplomacy_error'])
                assign(ref(ref(ref(e.get('sc'), 'error_window').get(), 'text1').get(), 'text'), '=', lambda: ref(ref(e.get('_global'), 'model').get(), 'interface_diplomacy_error').get())
                assign(ref(ref(ref(e.get('sc'), 'error_window').get(), 'btnOK').get(), 'onPress'), '=', lambda: ASFunction(f_24, e))
                assign(ref(ref(ref(e.get('sc'), 'error_window').get(), 'btnOK').get(), 'onRollOver'), '=', lambda: ASFunction(f_25, e))
                assign(ref(ref(ref(e.get('sc'), 'error_window').get(), 'btnOK').get(), 'onRollOut'), '=', lambda: ASFunction(f_26, e))
            raise ASBreak()
        if 0 <= case_13 <= 13:
            if truth(unary('!', ref(ref(this, 'model').get(), 'userSelectedHelpTopic').get())):
                assign(ref(ref(this, 'model').get(), 'userSelectedHelpTopic'), '=', lambda: 'help_index')
            else:
                rt.call_ref(ref(e.get('sc'), 'gotoAndStop'), [ref(ref(this, 'model').get(), 'userSelectedHelpTopic').get()])
                rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_centerScreenFunc_help'), [rt.call_ref(ref(ref(this, 'help_data').get(), 'get_data'), [ref(ref(this, 'model').get(), 'userSelectedHelpTopic').get()])])
            assign(ref(ref(e.get('sc'), 'btnIndex_c').get(), 'onPress'), '=', lambda: ASFunction(f_27, e))
            raise ASBreak()
        if 0 <= case_13 <= 14:
            assign(ref(ref(e.get('sc'), 'btnIndex_c').get(), 'onPress'), '=', lambda: ASFunction(f_28, e))
    except ASBreak:
        pass
    assign(ref(this, 'citiesSelectable'), '=', lambda: e.get('_loc2_'))
    return U

def Sub_Presenter_interface_do_ch_func(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_str'], ['a_str', 'i'], closure, 'Sub_Presenter_interface')
    assign(ref(ref(e.get('_global'), 'model').get(), 'corrupt_highscore'), '=', lambda: True)
    for key_29 in keys(ref(ref(this, 'model').get(), 'ch_018').get()):
        e.ref('i').set(key_29)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(ref(this, 'model').get(), 'ch_018').get(), e.get('i')).get(), 'str').get(), e.get('a_str'))):
                if truth(ref(ref(ref(ref(this, 'model').get(), 'ch_018').get(), e.get('i')).get(), 'active').get()):
                    assign(ref(ref(ref(ref(this, 'model').get(), 'ch_018').get(), e.get('i')).get(), 'active'), '=', lambda: False)
                else:
                    assign(ref(ref(ref(ref(this, 'model').get(), 'ch_018').get(), e.get('i')).get(), 'active'), '=', lambda: True)
                rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_select_tech'])
                return False
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_30 in keys(ref(ref(this, 'model').get(), 'ch_019').get()):
        e.ref('i').set(key_30)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(ref(this, 'model').get(), 'ch_019').get(), e.get('i')).get(), 'str').get(), e.get('a_str'))):
                assign(ref(ref(e.get('_global'), 'model').get(), 'force_error_window'), '=', lambda: True)
                assign(ref(ref(e.get('_global'), 'model').get(), 'force_error_window_text'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'ch_019').get(), e.get('i')).get(), 'msg').get())
                rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_select_tech'])
                return True
        except ASContinue:
            pass
        except ASBreak:
            break
    return False
    return U

def Sub_Presenter_interface_colorCities(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_loc3_', '_loc4_', '_loc5_', '_str', 'j'], closure, 'Sub_Presenter_interface')
    e.set('_loc3_', 0)
    while truth(binop('<', e.get('_loc3_'), ref(ref(ref(this, 'model').get(), 'playerArr').get(), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('_loc3_')).get())
            for key_31 in keys(ref(e.get('_loc4_'), 'cityArr').get()):
                e.ref('j').set(key_31)
                rt.tick()
                try:
                    assign(e.ref('_loc5_'), '=', lambda: ref(ref(e.get('_loc4_'), 'cityArr').get(), e.get('j')).get())
                    assign(ref(e.get('_loc5_'), 'hideForSelection'), '=', lambda: False)
                    assign(ref(e.get('_loc5_'), 'showForSelection'), '=', lambda: False)
                    switch_32 = e.get('_str')
                    case_33 = -1
                    if case_33 == -1 and strict_eq(switch_32, 'default'):
                        case_33 = 0
                    if case_33 == -1 and strict_eq(switch_32, 'attackable'):
                        case_33 = 1
                    if case_33 == -1 and strict_eq(switch_32, 'allEnemy'):
                        case_33 = 2
                    if case_33 == -1:
                        case_33 = -1
                    try:
                        if 0 <= case_33 <= 0:
                            assign(ref(e.get('_loc5_'), 'hideForSelection'), '=', lambda: False)
                            assign(ref(e.get('_loc5_'), 'showForSelection'), '=', lambda: False)
                            raise ASBreak()
                        if 0 <= case_33 <= 1:
                            if truth(logical('||', ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'ceaseFireArr').get(), ref(e.get('_loc4_'), 'playerNum').get()).get(), '_status').get(), lambda: binop('==', e.get('_loc4_'), ref(ref(this, 'model').get(), 'human').get()))):
                                assign(ref(e.get('_loc5_'), 'hideForSelection'), '=', lambda: True)
                            else:
                                assign(ref(e.get('_loc5_'), 'showForSelection'), '=', lambda: True)
                            if truth(logical('&&', binop('==', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), 'preAttack'), lambda: logical('&&', ref(ref(this, 'model').get(), 'userSelectedShipCityPlrNum').get(), lambda: binop('!=', ref(ref(this, 'model').get(), 'userSelectedShipCityPlrNum').get(), ref(ref(e.get('_loc5_'), 'plr').get(), 'playerNum').get())))):
                                assign(ref(e.get('_loc5_'), 'hideForSelection'), '=', lambda: True)
                            raise ASBreak()
                        if 0 <= case_33 <= 2:
                            if truth(binop('!=', e.get('_loc4_'), ref(ref(this, 'model').get(), 'human').get())):
                                assign(ref(e.get('_loc5_'), 'showForSelection'), '=', lambda: True)
                            else:
                                assign(ref(e.get('_loc5_'), 'hideForSelection'), '=', lambda: True)
                    except ASBreak:
                        pass
                except ASContinue:
                    pass
                except ASBreak:
                    break
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Sub_Presenter_interface___set__citiesSelectable(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_bln'], ['_bln', 'i', 'j'], closure, 'Sub_Presenter_interface')
    for key_34 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_34)
        rt.tick()
        try:
            for key_35 in keys(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get(), 'cityArr').get()):
                e.ref('j').set(key_35)
                rt.tick()
                try:
                    if truth(e.get('_bln')):
                        rt.call_ref(ref(ref(ref(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get(), 'cityArr').get(), e.get('j')).get(), 'image').get(), 'mc').get(), 'gotoAndStop'), [2])
                    else:
                        rt.call_ref(ref(ref(ref(ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get(), 'cityArr').get(), e.get('j')).get(), 'image').get(), 'mc').get(), 'gotoAndStop'), [1])
                except ASContinue:
                    pass
                except ASBreak:
                    break
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Sub_Presenter_interface___get__citiesSelectable(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_Presenter_interface')
    return True
    return U

def Sub_Presenter_interface_setSliderValue(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc0_', '_loc2_', '_loc3_', '_loc4_', '_loc5_'], closure, 'Sub_Presenter_interface')
    e.set('_loc2_', '')
    e.set('_loc3_', '')
    e.set('_loc4_', '')
    if truth(binop('===', assign(e.ref('_loc0_'), '=', lambda: ref(ref(this, 'model').get(), 'userSelectedActionBtn').get()), 'production')):
        assign(ref(ref(ref(ref(this, 'model').get(), '_userSelectedProductionInvestmentArr').get(), ref(ref(this, 'pressedSliderObj').get(), 'num').get()).get(), 1), '=', lambda: ref(ref(this, 'pressedSliderObj').get(), 'curVal').get())
        assign(ref(ref(ref(ref(this, 'model').get(), '_userSelectedProductionInvestmentArr').get(), ref(ref(this, 'pressedSliderObj').get(), 'num').get()).get(), 3), '=', lambda: binop('*', binop('/', ref(ref(ref(this, 'model').get(), 'human').get(), 'turnMoney').get(), 100), ref(ref(this, 'pressedSliderObj').get(), 'curVal').get()))
        assign(e.ref('_loc5_'), '=', lambda: 0)
        while truth(binop('<', e.get('_loc5_'), ref(ref(ref(this, 'model').get(), '_userSelectedProductionInvestmentArr').get(), 'length').get())):
            rt.tick()
            try:
                if truth(binop('>', ref(ref(ref(ref(this, 'model').get(), '_userSelectedProductionInvestmentArr').get(), e.get('_loc5_')).get(), 1).get(), 0)):
                    assign(e.ref('_loc2_'), '+=', lambda: binop('+', ref(ref(ref(ref(this, 'model').get(), '_userSelectedProductionInvestmentArr').get(), e.get('_loc5_')).get(), 0).get(), '<br />'))
                    assign(e.ref('_loc3_'), '+=', lambda: binop('+', binop('+', binop('+', binop('+', ref(ref(ref(ref(this, 'model').get(), '_userSelectedProductionInvestmentArr').get(), e.get('_loc5_')).get(), 1).get(), ' % ( $ '), rt.call_ref(ref(this, 'format_for_production'), [binop('*', binop('/', ref(ref(ref(this, 'model').get(), 'human').get(), 'turnMoney').get(), 100), ref(ref(ref(ref(this, 'model').get(), '_userSelectedProductionInvestmentArr').get(), e.get('_loc5_')).get(), 1).get())])), ' )'), '<br />'))
                assign(e.ref('_loc5_'), '=', lambda: binop('+', e.get('_loc5_'), 1))
            except ASContinue:
                pass
            except ASBreak:
                break
        assign(e.ref('_loc4_'), '=', lambda: binop('+', 'total estimated amount: ', rt.call_ref(ref(this, 'format_for_production'), [rt.call_ref(ref(e.get('Math'), 'round'), [binop('*', binop('/', ref(ref(ref(this, 'model').get(), 'human').get(), 'turnMoney').get(), 100), ref(ref(this, 'model').get(), 'userSelectedProductionInvestmentArr_total_amount').get())])])))
        rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_productionText'), [e.get('_loc2_'), e.get('_loc3_'), e.get('_loc4_')])
    return U

def Sub_Presenter_interface_format_for_production(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['_loc3_', '_loc4_', '_loc5_', 'a_nr'], closure, 'Sub_Presenter_interface')
    e.set('_loc3_', binop('+', binop('*', e.get('a_nr'), 1000000), ''))
    assign(e.ref('_loc3_'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'reverse_string'), [e.get('_loc3_')]))
    e.set('_loc4_', '')
    e.set('_loc5_', 0)
    while truth(binop('<', e.get('_loc5_'), ref(e.get('_loc3_'), 'length').get())):
        rt.tick()
        try:
            if truth(logical('||', binop('==', e.get('_loc5_'), 3), lambda: logical('||', binop('==', e.get('_loc5_'), 6), lambda: binop('==', e.get('_loc5_'), 9)))):
                assign(e.ref('_loc4_'), '+=', lambda: '.')
            assign(e.ref('_loc4_'), '+=', lambda: rt.call_ref(ref(e.get('_loc3_'), 'charAt'), [e.get('_loc5_')]))
            assign(e.ref('_loc5_'), '=', lambda: binop('+', e.get('_loc5_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'reverse_string'), [e.get('_loc4_')]))
    return e.get('_loc4_')
    return U

def Sub_Presenter_interface_set_sliders_after_error(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_'], closure, 'Sub_Presenter_interface')
    rt.call_ref(ref(this, 'setSliderValue'), [])
    e.set('_loc3_', 0)
    while truth(binop('<', e.get('_loc3_'), 11)):
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), binop('+', 'slide', e.get('_loc3_'))).get(), 'sliderBtn').get())
            assign(ref(e.get('_loc2_'), '_x'), '=', lambda: binop('*', binop('/', ref(ref(ref(e.get('_loc2_'), '_parent').get(), 'maxW').get(), '_width').get(), 100), ref(ref(ref(ref(this, 'model').get(), '_userSelectedProductionInvestmentArr').get(), e.get('_loc3_')).get(), 1).get()))
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Sub_Presenter_interface_set_research_after_error(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_'], closure, 'Sub_Presenter_interface')
    assign(ref(ref(this, 'model').get(), 'userSelectedResearchArr'), '=', lambda: arr([]))
    e.set('_loc3_', ' ')
    e.set('_loc4_', ' ')
    e.set('_loc5_', '')
    e.set('_loc6_', 0)
    e.set('_loc7_', 0)
    while truth(binop('<', e.get('_loc7_'), ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'techTree').get(), 'techArr').get(), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'techTree').get(), 'techArr').get(), e.get('_loc7_')).get())
            if truth(ref(e.get('_loc2_'), 'preOrder').get()):
                assign(e.ref('_loc3_'), '+=', lambda: binop('+', ref(e.get('_loc2_'), 'techName').get(), ' <br /> '))
                assign(e.ref('_loc4_'), '+=', lambda: binop('+', ref(e.get('_loc2_'), 'cost').get(), '.000.000 <br /> '))
                assign(e.ref('_loc6_'), '+=', lambda: ref(e.get('_loc2_'), 'cost').get())
                rt.call_ref(ref(ref(ref(this, 'model').get(), 'userSelectedResearchArr').get(), 'push'), [obj({'techID': ref(e.get('_loc2_'), 'techID').get()})])
            assign(e.ref('_loc7_'), '=', lambda: binop('+', e.get('_loc7_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(ref(this, 'model').get(), 'researchMoneySpend'), '=', lambda: e.get('_loc6_'))
    assign(e.ref('_loc5_'), '=', lambda: binop('+', binop('+', 'estimated total: ', e.get('_loc6_')), '.000.000'))
    rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_researchText'), [e.get('_loc3_'), e.get('_loc4_'), e.get('_loc5_')])
    rt.call_ref(ref(this, 'loadResearchFunc'), [])
    return U

def f_36(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_'], closure, None)
    e.set('_loc2_', ref(ref(e.get('_global'), 'presenter_interface').get(), 'pressedSliderObj').get())
    e.set('_loc3_', binop('-', ref(ref(ref(e.get('_loc2_'), '_mc').get(), '_parent').get(), '_xmouse').get(), ref(e.get('_loc2_'), 'regPoint').get()))
    e.set('_loc4_', ref(ref(ref(ref(e.get('_loc2_'), '_mc').get(), '_parent').get(), 'maxW').get(), '_width').get())
    e.set('_loc5_', ref(ref(ref(ref(e.get('_loc2_'), '_mc').get(), '_parent').get(), 'maxW').get(), '_x').get())
    e.set('_loc6_', 0)
    if truth(binop('>', e.get('_loc3_'), binop('/', e.get('_loc4_'), 2))):
        assign(e.ref('_loc6_'), '=', lambda: binop('*', rt.call_ref(ref(e.get('Math'), 'round'), [binop('/', binop('*', binop('/', e.get('_loc4_'), 100), e.get('_loc3_')), 10)]), 10))
    else:
        assign(e.ref('_loc6_'), '=', lambda: binop('*', rt.call_ref(ref(e.get('Math'), 'floor'), [binop('/', binop('*', binop('/', e.get('_loc4_'), 100), e.get('_loc3_')), 10)]), 10))
    if truth(binop('<', e.get('_loc6_'), 0)):
        assign(e.ref('_loc6_'), '=', lambda: 0)
    if truth(binop('>', e.get('_loc6_'), 100)):
        assign(e.ref('_loc6_'), '=', lambda: 100)
    if truth(binop('>', e.get('_loc6_'), rt.call_ref(ref(ref(e.get('_global'), 'model').get(), binop('+', ref(ref(e.get('_global'), 'model').get(), 'userSelectedActionBtn').get(), 'InvestementPercLeft')), [ref(e.get('_loc2_'), 'num').get()]))):
        assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(ref(e.get('_global'), 'model').get(), binop('+', ref(ref(e.get('_global'), 'model').get(), 'userSelectedActionBtn').get(), 'InvestementPercLeft')), [ref(e.get('_loc2_'), 'num').get()]))
    assign(ref(ref(e.get('_loc2_'), '_mc').get(), '_x'), '=', lambda: binop('*', binop('/', e.get('_loc4_'), 100), e.get('_loc6_')))
    if truth(binop('!=', ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'pressedSliderObj').get(), 'curVal').get(), e.get('_loc6_'))):
        rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_slider_bleep'])
    assign(ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'pressedSliderObj').get(), 'curVal'), '=', lambda: e.get('_loc6_'))
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'setSliderValue'), [])
    if truth(binop('!=', rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'productionInvestementPercLeft'), [99]), 100)):
        rt.call_ref(ref(ref(e.get('_global'), 'view_interface').get(), 'set_centerScreenFunc'), ['default'])
    else:
        rt.call_ref(ref(ref(e.get('_global'), 'view_interface').get(), 'set_centerScreenFunc'), ['hide'])
    return U

def f_37(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'setSliderValue'), [])
    assign(ref(ref(e.get('_global'), 'presenter_interface').get(), 'pressedSliderObj'), '=', lambda: e.get('undefined'))
    rt.call_ref(ref(e.get('Mouse'), 'removeListener'), [ref(ref(e.get('_global'), 'presenter_interface').get(), 'sliderListener').get()])
    return U

def Sub_Presenter_interface_slider_action(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['__obj'], ['__obj'], closure, 'Sub_Presenter_interface')
    assign(ref(this, 'pressedSliderObj'), '=', lambda: e.get('__obj'))
    if truth(unary('!', ref(e.get('__obj'), '_bg').get())):
        assign(ref(ref(this, 'pressedSliderObj').get(), 'regPoint'), '=', lambda: ref(ref(e.get('__obj'), '_mc').get(), '_xmouse').get())
    else:
        assign(ref(ref(this, 'pressedSliderObj').get(), 'regPoint'), '=', lambda: 0)
    assign(ref(ref(this, 'pressedSliderObj').get(), 'curVal'), '=', lambda: 0)
    assign(ref(ref(this, 'pressedSliderObj').get(), 'type'), '=', lambda: ref(e.get('__obj'), 'type').get())
    assign(ref(ref(this, 'pressedSliderObj').get(), 'num'), '=', lambda: ref(e.get('__obj'), 'num').get())
    assign(ref(ref(this, 'sliderListener').get(), 'onMouseMove'), '=', lambda: ASFunction(f_36, e))
    assign(ref(ref(this, 'sliderListener').get(), 'onMouseUp'), '=', lambda: ASFunction(f_37, e))
    rt.call_ref(ref(e.get('Mouse'), 'addListener'), [ref(this, 'sliderListener').get()])
    if truth(ref(e.get('__obj'), '_bg').get()):
        rt.call_ref(ref(ref(this, 'sliderListener').get(), 'onMouseMove'), [])
    return U

def f_38(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(e.get('_global'), 'model').get(), 'interface_production_error'), '=', lambda: e.get('undefined'))
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'update_centerScreenContent'), [])
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'set_sliders_after_error'), [])
    return U

def f_39(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'gotoAndStop'), [2])
    return U

def f_40(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'gotoAndStop'), [1])
    return U

def f_41(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(unary('!', rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'techTree').get(), 'allow_production_by_group'), [ref(ref(ref(ref(e.get('_global'), 'model').get(), '_userSelectedProductionInvestmentArr').get(), ref(ref(this, '_obj').get(), 'num').get()).get(), 2).get()]))):
        assign(ref(ref(e.get('_global'), 'model').get(), 'interface_production_error'), '=', lambda: 'You have not yet invented this Technology')
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'updateView'), [])
    else:
        assign(ref(ref(this, '_obj').get(), '_mc'), '=', lambda: this)
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'slider_action'), [ref(this, '_obj').get()])
    return U

def f_42(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(unary('!', rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'techTree').get(), 'allow_production_by_group'), [ref(ref(ref(ref(e.get('_global'), 'model').get(), '_userSelectedProductionInvestmentArr').get(), ref(ref(this, '_obj').get(), 'num').get()).get(), 2).get()]))):
        assign(ref(ref(e.get('_global'), 'model').get(), 'interface_production_error'), '=', lambda: 'You have not yet invented this Technology')
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'updateView'), [])
    else:
        assign(ref(ref(this, '_obj').get(), '_mc'), '=', lambda: ref(ref(this, '_parent').get(), 'sliderBtn').get())
        assign(ref(ref(this, '_obj').get(), '_bg'), '=', lambda: True)
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'slider_action'), [ref(this, '_obj').get()])
    return U

def Sub_Presenter_interface_loadProductionFunc(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_error'], ['_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', 'a_error'], closure, 'Sub_Presenter_interface')
    if truth(e.get('a_error')):
        assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get())
        assign(ref(ref(ref(e.get('_loc3_'), 'error_window').get(), 'text1').get(), 'htmlText'), '=', lambda: e.get('a_error'))
        assign(ref(ref(ref(e.get('_loc3_'), 'error_window').get(), 'btnOK').get(), 'onPress'), '=', lambda: ASFunction(f_38, e))
        assign(ref(ref(ref(e.get('_loc3_'), 'error_window').get(), 'btnOK').get(), 'onRollOver'), '=', lambda: ASFunction(f_39, e))
        assign(ref(ref(ref(e.get('_loc3_'), 'error_window').get(), 'btnOK').get(), 'onRollOut'), '=', lambda: ASFunction(f_40, e))
        return e.get('undefined')
    e.set('_loc4_', rt.construct(e.get('Array'), []))
    e.set('_loc5_', 0)
    while truth(binop('<', e.get('_loc5_'), ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'weaponStock').get(), 'weaponArr').get(), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc6_'), '=', lambda: ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'weaponStock').get(), 'weaponArr').get(), e.get('_loc5_')).get())
            if truth(binop('==', ref(e.get('_loc6_'), 'desireGroup').get(), 7)):
                rt.call_ref(ref(e.get('_loc4_'), 'push'), [arr([ref(e.get('_loc6_'), 'investment').get(), ref(e.get('_loc6_'), 'cost').get()])])
            assign(e.ref('_loc5_'), '=', lambda: binop('+', e.get('_loc5_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_production_specialStats'), [e.get('_loc4_')])
    e.set('_loc7_', 1)
    while truth(binop('<', e.get('_loc7_'), 9)):
        rt.tick()
        try:
            assign(e.ref('_loc8_'), '=', lambda: rt.construct(e.get('Object'), []))
            assign(ref(e.get('_loc8_'), 'num'), '=', lambda: e.get('_loc7_'))
            assign(ref(ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), binop('+', 'slide', e.get('_loc7_'))).get(), 'sliderBtn').get(), '_obj'), '=', lambda: e.get('_loc8_'))
            assign(ref(ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), binop('+', 'slide', e.get('_loc7_'))).get(), 'sliderBtn').get(), 'onPress'), '=', lambda: ASFunction(f_41, e))
            assign(ref(ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), binop('+', 'slide', e.get('_loc7_'))).get(), 'sliderBG').get(), '_obj'), '=', lambda: e.get('_loc8_'))
            assign(ref(ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), binop('+', 'slide', e.get('_loc7_'))).get(), 'sliderBG').get(), 'onPress'), '=', lambda: ASFunction(f_42, e))
            assign(e.ref('_loc7_'), '=', lambda: binop('+', e.get('_loc7_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Sub_Presenter_interface_removeBioClips(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'Sub_Presenter_interface')
    for key_43 in keys(ref(ref(this, 'view_interface').get(), 'actionBtn_arr').get()):
        e.ref('i').set(key_43)
        rt.tick()
        try:
            assign(ref(ref(ref(ref(this, 'view_interface').get(), 'actionBtn_arr').get(), e.get('i')).get(), 'bioloaded'), '=', lambda: False)
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_44 in keys(ref(ref(this, 'view_interface').get(), 'stockBtn_arr').get()):
        e.ref('i').set(key_44)
        rt.tick()
        try:
            assign(ref(ref(ref(ref(this, 'view_interface').get(), 'stockBtn_arr').get(), e.get('i')).get(), 'bioloaded'), '=', lambda: False)
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Sub_Presenter_interface_attachBioClips(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', 'i', 'j'], closure, 'Sub_Presenter_interface')
    for key_45 in keys(ref(ref(ref(this, 'model').get(), 'human').get(), 'bioloadedActionsArr').get()):
        e.ref('i').set(key_45)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'bioloadedActionsArr').get(), e.get('i')).get())
            for key_46 in keys(ref(ref(this, 'view_interface').get(), 'actionBtn_arr').get()):
                e.ref('j').set(key_46)
                rt.tick()
                try:
                    assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(this, 'view_interface').get(), 'actionBtn_arr').get(), e.get('j')).get())
                    if truth(binop('==', ref(e.get('_loc3_'), 'actionName').get(), e.get('_loc2_'))):
                        assign(ref(e.get('_loc3_'), 'bioloaded'), '=', lambda: True)
                except ASContinue:
                    pass
                except ASBreak:
                    break
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_47 in keys(ref(ref(ref(this, 'model').get(), 'human').get(), 'bioloadedStockArr').get()):
        e.ref('i').set(key_47)
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'bioloadedStockArr').get(), e.get('i')).get())
            for key_48 in keys(ref(ref(this, 'view_interface').get(), 'stockBtn_arr').get()):
                e.ref('j').set(key_48)
                rt.tick()
                try:
                    assign(e.ref('_loc5_'), '=', lambda: ref(ref(ref(this, 'view_interface').get(), 'stockBtn_arr').get(), e.get('j')).get())
                    if truth(binop('==', ref(e.get('_loc5_'), 'relatedWeapon').get(), e.get('_loc4_'))):
                        assign(ref(e.get('_loc5_'), 'bioloaded'), '=', lambda: True)
                except ASContinue:
                    pass
                except ASBreak:
                    break
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def f_49(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(e.get('_global'), 'model').get(), 'interface_research_error'), '=', lambda: e.get('undefined'))
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'update_centerScreenContent'), [])
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'set_research_after_error'), [])
    return U

def f_50(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'gotoAndStop'), [2])
    return U

def f_51(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'gotoAndStop'), [1])
    return U

def f_52(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPressed_techBox'), [ref(this, '_obj').get()])
    return U

def Sub_Presenter_interface_loadResearchFunc(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_error'], ['_loc10_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', 'a_error'], closure, 'Sub_Presenter_interface')
    if truth(e.get('a_error')):
        assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get())
        assign(ref(ref(ref(e.get('_loc3_'), 'error_window').get(), 'text1').get(), 'htmlText'), '=', lambda: e.get('a_error'))
        assign(ref(ref(ref(e.get('_loc3_'), 'error_window').get(), 'btnOK').get(), 'onPress'), '=', lambda: ASFunction(f_49, e))
        assign(ref(ref(ref(e.get('_loc3_'), 'error_window').get(), 'btnOK').get(), 'onRollOver'), '=', lambda: ASFunction(f_50, e))
        assign(ref(ref(ref(e.get('_loc3_'), 'error_window').get(), 'btnOK').get(), 'onRollOut'), '=', lambda: ASFunction(f_51, e))
        return e.get('undefined')
    e.set('_loc4_', 1)
    while truth(binop('<', e.get('_loc4_'), 8)):
        rt.tick()
        try:
            assign(e.ref('_loc5_'), '=', lambda: rt.construct(e.get('Array'), []))
            assign(e.ref('_loc6_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc6_'), ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'techTree').get(), 'techArr').get(), 'length').get())):
                rt.tick()
                try:
                    assign(e.ref('_loc7_'), '=', lambda: ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'techTree').get(), 'techArr').get(), e.get('_loc6_')).get())
                    if truth(binop('==', ref(e.get('_loc7_'), 'desireGroup').get(), ref(ref(ref(ref(this, 'model').get(), '_userSelectedResearchInvestmentArr').get(), e.get('_loc4_')).get(), 2).get())):
                        rt.call_ref(ref(e.get('_loc5_'), 'push'), [e.get('_loc7_')])
                    assign(e.ref('_loc6_'), '=', lambda: binop('+', e.get('_loc6_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            assign(e.ref('_loc9_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc9_'), ref(e.get('_loc5_'), 'length').get())):
                rt.tick()
                try:
                    if truth(logical('&&', unary('!', ref(ref(e.get('_loc5_'), e.get('_loc9_')).get(), 'invented').get()), lambda: logical('||', unary('!', ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get()), lambda: ref(ref(e.get('_loc5_'), e.get('_loc9_')).get(), 'allow_in_demo').get()))):
                        assign(e.ref('_loc8_'), '=', lambda: ref(e.get('_loc5_'), e.get('_loc9_')).get())
                        raise ASBreak()
                    assign(e.ref('_loc9_'), '=', lambda: binop('+', e.get('_loc9_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            assign(e.ref('_loc10_'), '=', lambda: ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), binop('+', 'tech', e.get('_loc4_'))).get())
            assign(ref(ref(e.get('_loc10_'), 'text1').get(), 'text'), '=', lambda: binop('+', binop('+', '$ ', ref(e.get('_loc8_'), 'cost').get()), '.000.000'))
            if truth(binop('<', ref(ref(ref(this, 'model').get(), 'human').get(), 'turnMoney').get(), binop('+', ref(e.get('_loc8_'), 'cost').get(), ref(ref(this, 'model').get(), 'researchMoneySpend').get()))):
                assign(ref(ref(e.get('_loc10_'), 'text1').get(), 'textColor'), '=', lambda: 13369344)
            else:
                assign(ref(ref(e.get('_loc10_'), 'text1').get(), 'textColor'), '=', lambda: 0)
            if truth(unary('!', e.get('_loc8_'))):
                rt.call_ref(ref(e.get('_loc10_'), 'gotoAndStop'), ['allInvented'])
                assign(ref(ref(e.get('_loc10_'), 'text1').get(), 'text'), '=', lambda: ' -- ')
                if truth(ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get()):
                    rt.call_ref(ref(e.get('_loc10_'), 'gotoAndStop'), ['demo'])
            else:
                if truth(unary('!', ref(e.get('_loc8_'), 'preOrder').get())):
                    rt.call_ref(ref(e.get('_loc10_'), 'gotoAndStop'), [ref(e.get('_loc8_'), 'techLevel').get()])
                else:
                    rt.call_ref(ref(e.get('_loc10_'), 'gotoAndStop'), [binop('+', ref(e.get('_loc8_'), 'techLevel').get(), 4)])
                    if truth(ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get()):
                        rt.call_ref(ref(e.get('_loc10_'), 'gotoAndStop'), ['demo'])
            assign(ref(e.get('_loc10_'), '_obj'), '=', lambda: obj({'_tech': e.get('_loc8_'), '_mc': e.get('_loc10_')}))
            assign(ref(e.get('_loc10_'), 'onPress'), '=', lambda: ASFunction(f_52, e))
            assign(e.ref('_loc4_'), '=', lambda: binop('+', e.get('_loc4_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Sub_Presenter_interface_play_sound_by_obj(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_obj'], ['_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_obj'], closure, 'Sub_Presenter_interface')
    e.set('_loc3_', rt.construct(e.get('Object'), []))
    e.set('_loc4_', rt.call_ref(ref(ref(ref(this, 'view').get(), 'srcMC').get(), 'createEmptyMovieClip'), [binop('+', 'sound', update(ref(ref(this, 'model').get(), 'soundCount'), 1, False)), rt.call_ref(ref(ref(ref(this, 'view').get(), 'srcMC').get(), 'getNextHighestDepth'), [])]))
    e.set('_loc5_', rt.construct(e.get('Sound'), [e.get('_loc4_')]))
    e.set('_loc6_', 0)
    e.set('_loc7_', 0)
    rt.call_ref(ref(e.get('_loc5_'), 'attachSound'), [ref(e.get('_obj'), '_soundName').get()])
    if truth(ref(e.get('_obj'), '_pan').get()):
        rt.call_ref(ref(e.get('_loc5_'), 'setPan'), [ref(e.get('_obj'), '_pan').get()])
    if truth(ref(e.get('_obj'), '_loops').get()):
        assign(e.ref('_loc6_'), '=', lambda: ref(e.get('_obj'), '_loops').get())
    if truth(ref(e.get('_obj'), '_startAt').get()):
        assign(e.ref('_loc7_'), '=', lambda: ref(e.get('_obj'), '_startAt').get())
    if truth(ref(e.get('_obj'), '_vol').get()):
        rt.call_ref(ref(e.get('_loc5_'), 'setVolume'), [ref(e.get('_obj'), '_vol').get()])
    rt.call_ref(ref(e.get('_loc5_'), 'start'), [e.get('_loc7_'), e.get('_loc6_')])
    if truth(unary('!', ref(e.get('_obj'), '_continues').get())):
        rt.call_ref(ref(ref(ref(this, 'model').get(), 'playedSounds_arr').get(), 'push'), [obj({'soundObj': e.get('_loc5_'), 'mc': e.get('_loc4_')})])
    return e.get('undefined')
    return U

def Sub_Presenter_interface_play_sound_by_action(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_action'], ['_action', '_loc3_', 'i'], closure, 'Sub_Presenter_interface')
    if truth(unary('!', ref(ref(ref(e.get('_global'), 'model').get(), 'option').get(), 'playSound').get())):
        return e.get('undefined')
    for key_53 in keys(ref(ref(this, 'model').get(), 'action_to_sound_arr').get()):
        e.ref('i').set(key_53)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'action_to_sound_arr').get(), e.get('i')).get())
            if truth(binop('==', ref(e.get('_loc3_'), '_actionName').get(), e.get('_action'))):
                rt.call_ref(ref(this, 'play_sound_by_obj'), [e.get('_loc3_')])
                return e.get('undefined')
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('undefined')
    return U

def Sub_Presenter_interface_play_sound_by_building(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_building', '_plrNum'], ['_building', '_loc0_', '_loc4_', '_plrNum', 'i'], closure, 'Sub_Presenter_interface')
    if truth(unary('!', ref(ref(ref(e.get('_global'), 'model').get(), 'option').get(), 'playSound').get())):
        return e.get('undefined')
    for key_54 in keys(ref(ref(this, 'model').get(), 'building_to_sound_arr').get()):
        e.ref('i').set(key_54)
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'building_to_sound_arr').get(), e.get('i')).get())
            if truth(binop('==', ref(e.get('_loc4_'), '_buildingName').get(), e.get('_building'))):
                if truth(binop('===', assign(e.ref('_loc0_'), '=', lambda: ref(e.get('_loc4_'), '_varSoundName').get()), 'religion')):
                    assign(ref(e.get('_loc4_'), '_soundName'), '=', lambda: binop('+', binop('+', 'Massmedia ', rt.call_ref(ref(ref(ref(this, 'model').get(), 'tools').get(), 'randRange'), [1, 4])), '.wav'))
                rt.call_ref(ref(this, 'play_sound_by_obj'), [e.get('_loc4_')])
                return e.get('undefined')
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('undefined')
    return U

def Sub_Presenter_interface_play_sound_by_event(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_event', '_panX'], ['_event', '_loc4_', '_panX', 'i'], closure, 'Sub_Presenter_interface')
    if truth(unary('!', ref(ref(ref(e.get('_global'), 'model').get(), 'option').get(), 'playSound').get())):
        return e.get('undefined')
    for key_55 in keys(ref(ref(this, 'model').get(), 'event_to_sound_arr').get()):
        e.ref('i').set(key_55)
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'event_to_sound_arr').get(), e.get('i')).get())
            if truth(binop('==', ref(e.get('_loc4_'), '_eventName').get(), e.get('_event'))):
                assign(ref(e.get('_loc4_'), '_pan'), '=', lambda: logical('||', rt.call_ref(ref(this, 'getPanBy_x'), [e.get('_panX')]), lambda: 0))
                rt.call_ref(ref(this, 'play_sound_by_obj'), [e.get('_loc4_')])
                return e.get('undefined')
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('undefined')
    return U

def Sub_Presenter_interface_getPanBy_x(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_xNum'], ['_loc3_', '_xNum'], closure, 'Sub_Presenter_interface')
    e.set('_loc3_', binop('*', binop('-', binop('/', e.get('_xNum'), 8), 50), 2))
    return e.get('_loc3_')
    return U

def Sub_Presenter_interface_explosion_sound_by_mc_name(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str', '_mcx'], ['_loc4_', '_mcx', '_str', 'i'], closure, 'Sub_Presenter_interface')
    for key_56 in keys(ref(ref(this, 'model').get(), 'explosion_MC_to_sound_arr').get()):
        e.ref('i').set(key_56)
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'explosion_MC_to_sound_arr').get(), e.get('i')).get())
            if truth(binop('==', ref(e.get('_loc4_'), '_mcName').get(), e.get('_str'))):
                assign(ref(e.get('_loc4_'), '_pan'), '=', lambda: rt.call_ref(ref(this, 'getPanBy_x'), [e.get('_mcx')]))
                rt.call_ref(ref(this, 'play_sound_by_obj'), [e.get('_loc4_')])
                return e.get('undefined')
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Sub_Presenter_interface_reset_leader_stat_bars(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_'], closure, 'Sub_Presenter_interface')
    e.set('_loc3_', 0)
    while truth(binop('<', e.get('_loc3_'), 6)):
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), binop('+', binop('+', binop('+', 'leaderStat', e.get('_loc3_')), '_'), 1)).get(), 'maskMC').get())
            assign(ref(e.get('_loc2_'), '_yscale'), '=', lambda: 0)
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), binop('+', binop('+', binop('+', 'leaderStat', e.get('_loc3_')), '_'), 2)).get(), 'maskMC').get())
            assign(ref(e.get('_loc2_'), '_yscale'), '=', lambda: 0)
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Sub_Presenter_interface_roll_over_stat(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['p_str', 'p_plr_num'], ['_loc4_', '_loc5_', '_loc6_', 'i', 'p_plr_num', 'p_str'], closure, 'Sub_Presenter_interface')
    switch_57 = e.get('p_str')
    case_58 = -1
    if case_58 == -1 and strict_eq(switch_57, 'regard'):
        case_58 = 0
    if case_58 == -1 and strict_eq(switch_57, 'population'):
        case_58 = 1
    if case_58 == -1:
        case_58 = 2
    try:
        if 0 <= case_58 <= 0:
            assign(e.ref('_loc4_'), '=', lambda: '')
            for key_59 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
                e.ref('i').set(key_59)
                rt.tick()
                try:
                    if truth(binop('==', ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get(), 'playerNum').get(), e.get('p_plr_num'))):
                        assign(e.ref('_loc5_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get())
                        assign(e.ref('_loc6_'), '=', lambda: ref(ref(e.get('_loc5_'), 'regardArr').get(), 0).get())
                        if truth(binop('>', e.get('_loc6_'), 75)):
                            assign(e.ref('_loc4_'), '=', lambda: 'regard5')
                        else:
                            if truth(binop('>', e.get('_loc6_'), 55)):
                                assign(e.ref('_loc4_'), '=', lambda: 'regard4')
                            else:
                                if truth(binop('>', e.get('_loc6_'), 45)):
                                    assign(e.ref('_loc4_'), '=', lambda: 'regard3')
                                else:
                                    if truth(binop('>', e.get('_loc6_'), 25)):
                                        assign(e.ref('_loc4_'), '=', lambda: 'regard2')
                                    else:
                                        assign(e.ref('_loc4_'), '=', lambda: 'regard1')
                except ASContinue:
                    pass
                except ASBreak:
                    break
            raise ASBreak()
            assign(ref(ref(this, 'view_interface').get(), 'infoLine'), '=', lambda: e.get('_loc4_'))
        if 0 <= case_58 <= 1:
            assign(ref(ref(this, 'view_interface').get(), 'infoLine'), '=', lambda: e.get('p_str'))
        if 0 <= case_58 <= 2:
            return U
    except ASBreak:
        pass
    return U

def Sub_Presenter_interface_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_Presenter_interface')
    pass

def register(rt):
    rt.define('Sub_Presenter_interface', 'Sub_sub_presenter_interface', Sub_Presenter_interface_fields, {'Sub_Presenter_interface': ASFunction(Sub_Presenter_interface_Sub_Presenter_interface), 'resetBtns': ASFunction(Sub_Presenter_interface_resetBtns), 'do_turn_backup': ASFunction(Sub_Presenter_interface_do_turn_backup), 'turnInterval_step1': ASFunction(Sub_Presenter_interface_turnInterval_step1), 'turnInterval_step2': ASFunction(Sub_Presenter_interface_turnInterval_step2), 'turnInterval_step3': ASFunction(Sub_Presenter_interface_turnInterval_step3), 'turnInterval_go': ASFunction(Sub_Presenter_interface_turnInterval_go), 'updateView': ASFunction(Sub_Presenter_interface_updateView), 'do_leader_face_MC_sequence_itteration': ASFunction(Sub_Presenter_interface_do_leader_face_MC_sequence_itteration), 'update_top_plrColor': ASFunction(Sub_Presenter_interface_update_top_plrColor), 'update_color_dots': ASFunction(Sub_Presenter_interface_update_color_dots), 'update_statistics': ASFunction(Sub_Presenter_interface_update_statistics), 'update_centerScreenContent': ASFunction(Sub_Presenter_interface_update_centerScreenContent), 'do_ch_func': ASFunction(Sub_Presenter_interface_do_ch_func), 'colorCities': ASFunction(Sub_Presenter_interface_colorCities), 'setSliderValue': ASFunction(Sub_Presenter_interface_setSliderValue), 'format_for_production': ASFunction(Sub_Presenter_interface_format_for_production), 'set_sliders_after_error': ASFunction(Sub_Presenter_interface_set_sliders_after_error), 'set_research_after_error': ASFunction(Sub_Presenter_interface_set_research_after_error), 'slider_action': ASFunction(Sub_Presenter_interface_slider_action), 'loadProductionFunc': ASFunction(Sub_Presenter_interface_loadProductionFunc), 'removeBioClips': ASFunction(Sub_Presenter_interface_removeBioClips), 'attachBioClips': ASFunction(Sub_Presenter_interface_attachBioClips), 'loadResearchFunc': ASFunction(Sub_Presenter_interface_loadResearchFunc), 'play_sound_by_obj': ASFunction(Sub_Presenter_interface_play_sound_by_obj), 'play_sound_by_action': ASFunction(Sub_Presenter_interface_play_sound_by_action), 'play_sound_by_building': ASFunction(Sub_Presenter_interface_play_sound_by_building), 'play_sound_by_event': ASFunction(Sub_Presenter_interface_play_sound_by_event), 'getPanBy_x': ASFunction(Sub_Presenter_interface_getPanBy_x), 'explosion_sound_by_mc_name': ASFunction(Sub_Presenter_interface_explosion_sound_by_mc_name), 'reset_leader_stat_bars': ASFunction(Sub_Presenter_interface_reset_leader_stat_bars), 'roll_over_stat': ASFunction(Sub_Presenter_interface_roll_over_stat)}, {'display_textFunds': ASFunction(Sub_Presenter_interface___get__display_textFunds), 'display_population': ASFunction(Sub_Presenter_interface___get__display_population), 'citiesSelectable': ASFunction(Sub_Presenter_interface___get__citiesSelectable)}, {'citiesSelectable': ASFunction(Sub_Presenter_interface___set__citiesSelectable)})
