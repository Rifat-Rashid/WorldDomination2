# Generated from __Packages/Sub_sub_presenter_interface.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Sub_sub_presenter_interface_Sub_sub_presenter_interface(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_sub_presenter_interface')
    return U

def f_1(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('getURL', [rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'get_demo_version_url'), []), '_blank'])
    return U

def Sub_sub_presenter_interface_updateView_debug_1(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_sub_presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
    rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'remove_city_popups'), [])
    if truth(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'diplomacyPendingArr').get(), 0).get()):
        assign(ref(ref(this, 'model').get(), 'userSelectedActionBtn'), '=', lambda: 'diplomacyPending')
    if truth(ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get()):
        assign(ref(ref(ref(ref(e.get('_global'), 'view').get(), 'srcMC').get(), 'get_full_version_btn').get(), 'onPress'), '=', lambda: ASFunction(f_1, e))
    else:
        assign(ref(ref(ref(ref(e.get('_global'), 'view').get(), 'srcMC').get(), 'get_full_version_btn').get(), '_visible'), '=', lambda: False)
        assign(ref(ref(ref(ref(e.get('_global'), 'view').get(), 'srcMC').get(), 'get_full_version_text').get(), '_visible'), '=', lambda: False)
        rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'view').get(), 'srcMC').get(), 'demo_stock_overlay').get(), 'gotoAndStop'), [1])
        assign(ref(ref(ref(ref(e.get('_global'), 'view').get(), 'srcMC').get(), 'demo_stock_overlay').get(), '_visible'), '=', lambda: False)
    assign(ref(ref(this, 'view_interface').get(), 'shortMSG_text'), '=', lambda: ref(ref(ref(this, 'model').get(), 'human').get(), 'shortMSG_arr').get())
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'updateView_debug_2', 5]))
    return U

def Sub_sub_presenter_interface_updateView_debug_2(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', 'i', 'j'], closure, 'Sub_sub_presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
    for key_2 in keys(ref(ref(this, 'view_interface').get(), 'stockBtn_arr').get()):
        e.ref('i').set(key_2)
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
            for key_3 in keys(ref(ref(ref(ref(this, 'view_interface').get(), 'stockRequirements_list').get(), ref(ref(this, 'model_interface').get(), 'selected_action_name').get()).get(), 'state2_arr').get()):
                e.ref('j').set(key_3)
                rt.tick()
                try:
                    if truth(unary('!', rt.call_ref(ref(this, 'stock_req_check_single'), [ref(ref(ref(ref(ref(this, 'view_interface').get(), 'stockRequirements_list').get(), ref(ref(this, 'model_interface').get(), 'selected_action_name').get()).get(), 'state2_arr').get(), e.get('j')).get(), e.get('_loc2_')]))):
                        assign(e.ref('_loc4_'), '=', lambda: False)
                        raise ASBreak()
                except ASContinue:
                    pass
                except ASBreak:
                    break
            for key_4 in keys(ref(ref(ref(ref(this, 'view_interface').get(), 'stockRequirements_list').get(), ref(ref(this, 'model_interface').get(), 'selected_action_name').get()).get(), 'state4_arr').get()):
                e.ref('j').set(key_4)
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
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'updateView_debug_3', 5]))
    return U

def Sub_sub_presenter_interface_updateView_debug_3(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'Sub_sub_presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
    for key_5 in keys(ref(ref(this, 'view_interface').get(), 'actionBtn_arr').get()):
        e.ref('i').set(key_5)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(this, 'view_interface').get(), 'actionBtn_arr').get(), e.get('i')).get())
            if truth(unary('!', rt.call_ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'getNextTurnAction'), []))):
                if truth(logical('&&', binop('!=', ref(e.get('_loc2_'), 'actionName').get(), ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnAction_1').get(), 'action').get()), lambda: binop('!=', ref(e.get('_loc2_'), 'actionName').get(), ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnAction_2').get(), 'action').get()))):
                    assign(ref(e.get('_loc2_'), 'handCursor'), '=', lambda: False)
            else:
                assign(ref(e.get('_loc2_'), 'handCursor'), '=', lambda: True)
            if truth(ref(e.get('_loc2_'), 'isSetAction').get()):
                assign(ref(e.get('_loc2_'), 'state'), '=', lambda: 3)
            else:
                if truth(ref(e.get('_loc2_'), 'pressed').get()):
                    assign(ref(e.get('_loc2_'), 'state'), '=', lambda: 2)
                else:
                    if truth(logical('&&', binop('==', ref(e.get('_loc2_'), 'actionName').get(), 'preAttack'), lambda: binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready'))):
                        assign(ref(e.get('_loc2_'), 'state'), '=', lambda: 4)
                    else:
                        assign(ref(e.get('_loc2_'), 'state'), '=', lambda: 1)
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'updateView_debug_4', 5]))
    return U

def f_6(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(e.get('_global'), 'presenter_interface').get(), 'blockAllBtns'), '=', lambda: True)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btnPressed_turn'), [])
    return U

def Sub_sub_presenter_interface_updateView_debug_4(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_sub_presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
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
                assign(ref(ref(ref(ref(this, 'view_interface').get(), 'turnBtn').get(), 'btnMC').get(), 'onPress'), '=', lambda: ASFunction(f_6, e))
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'updateView_debug_5', 5]))
    return U

def Sub_sub_presenter_interface_updateView_debug_5(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc10_', '_loc11_', '_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_'], closure, 'Sub_sub_presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
    if truth(rt.call_ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'getNextTurnAction'), [])):
        assign(ref(ref(ref(this, 'view_interface').get(), 'turnBtn').get(), 'state'), '=', lambda: 'closed')
    e.set('_loc2_', 0)
    while truth(binop('<', e.get('_loc2_'), ref(ref(ref(this, 'view_interface').get(), 'actionNames_arr').get(), 'length').get())):
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'view_interface').get(), 'actionNames_arr').get(), e.get('_loc2_')).get(), ref(ref(this, 'model').get(), 'userSelectedActionBtn').get())):
                switch_7 = ref(ref(ref(ref(this, 'view_interface').get(), 'stockPanel_mask_states_arr').get(), e.get('_loc2_')).get(), 0).get()
                case_8 = -1
                if case_8 == -1 and strict_eq(switch_7, 0):
                    case_8 = 0
                if case_8 == -1 and strict_eq(switch_7, 1):
                    case_8 = 1
                if case_8 == -1 and strict_eq(switch_7, 2):
                    case_8 = 2
                if case_8 == -1 and strict_eq(switch_7, 3):
                    case_8 = 3
                if case_8 == -1:
                    case_8 = -1
                try:
                    if 0 <= case_8 <= 0:
                        assign(e.ref('_loc4_'), '=', lambda: 1)
                        while truth(binop('<', e.get('_loc4_'), 9)):
                            rt.tick()
                            try:
                                assign(e.ref('_loc5_'), '=', lambda: e.call('Number', [e.get('_loc4_')]))
                                rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_stockPanel_alpha'), [e.get('_loc5_'), 100])
                                assign(e.ref('_loc4_'), '=', lambda: binop('+', e.get('_loc4_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        raise ASBreak()
                    if 0 <= case_8 <= 1:
                        assign(e.ref('_loc6_'), '=', lambda: 1)
                        while truth(binop('<', e.get('_loc6_'), 9)):
                            rt.tick()
                            try:
                                assign(e.ref('_loc7_'), '=', lambda: e.call('Number', [e.get('_loc6_')]))
                                if truth(binop('==', ref(ref(ref(ref(this, 'view_interface').get(), 'stockPanel_mask_states_arr').get(), e.get('_loc2_')).get(), e.get('_loc7_')).get(), 1)):
                                    assign(e.ref('_loc3_'), '=', lambda: 100)
                                else:
                                    assign(e.ref('_loc3_'), '=', lambda: 0)
                                rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_stockPanel_alpha'), [e.get('_loc7_'), e.get('_loc3_')])
                                assign(e.ref('_loc6_'), '=', lambda: binop('+', e.get('_loc6_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        raise ASBreak()
                    if 0 <= case_8 <= 2:
                        assign(e.ref('_loc8_'), '=', lambda: 1)
                        while truth(binop('<', e.get('_loc8_'), 9)):
                            rt.tick()
                            try:
                                assign(e.ref('_loc9_'), '=', lambda: e.call('Number', [e.get('_loc8_')]))
                                if truth(binop('==', ref(ref(ref(ref(this, 'view_interface').get(), 'stockPanel_mask_states_arr').get(), e.get('_loc2_')).get(), e.get('_loc9_')).get(), 1)):
                                    assign(e.ref('_loc3_'), '=', lambda: 100)
                                else:
                                    assign(e.ref('_loc3_'), '=', lambda: 0)
                                rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_stockPanel_alpha'), [e.get('_loc9_'), e.get('_loc3_')])
                                assign(e.ref('_loc8_'), '=', lambda: binop('+', e.get('_loc8_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                        raise ASBreak()
                    if 0 <= case_8 <= 3:
                        assign(e.ref('_loc10_'), '=', lambda: 1)
                        while truth(binop('<', e.get('_loc10_'), 9)):
                            rt.tick()
                            try:
                                assign(e.ref('_loc11_'), '=', lambda: e.call('Number', [e.get('_loc10_')]))
                                rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_stockPanel_alpha'), [e.get('_loc11_'), 0])
                                assign(e.ref('_loc10_'), '=', lambda: binop('+', e.get('_loc10_'), 1))
                            except ASContinue:
                                pass
                            except ASBreak:
                                break
                except ASBreak:
                    pass
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'updateView_debug_6', 5]))
    return U

def Sub_sub_presenter_interface_updateView_debug_6(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_'], closure, 'Sub_sub_presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
    if truth(binop('==', ref(ref(e.get('_global'), 'model').get(), 'view_leader_MCs_played').get(), 'done')):
        assign(e.ref('_loc2_'), '=', lambda: 1)
        while truth(binop('<', e.get('_loc2_'), ref(ref(ref(this, 'model').get(), 'playerArr').get(), 'length').get())):
            rt.tick()
            try:
                assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('_loc2_')).get())
                assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), binop('+', 'leaderMC', e.get('_loc2_'))).get())
                assign(ref(e.get('_loc4_'), 'num'), '=', lambda: e.get('_loc2_'))
                assign(e.ref('_loc6_'), '=', lambda: 0)
                rt.call_ref(ref(ref(e.get('_loc4_'), 'cfIcon1').get(), 'gotoAndStop'), [1])
                rt.call_ref(ref(ref(e.get('_loc4_'), 'cfIcon2').get(), 'gotoAndStop'), [1])
                rt.call_ref(ref(ref(e.get('_loc4_'), 'cfIcon3').get(), 'gotoAndStop'), [1])
                assign(e.ref('_loc7_'), '=', lambda: 1)
                while truth(binop('<', e.get('_loc7_'), ref(ref(e.get('_loc3_'), 'ceaseFireArr').get(), 'length').get())):
                    rt.tick()
                    try:
                        if truth(ref(ref(ref(e.get('_loc3_'), 'ceaseFireArr').get(), e.get('_loc7_')).get(), '_status').get()):
                            assign(e.ref('_loc6_'), '=', lambda: binop('+', e.get('_loc6_'), 1))
                            rt.call_ref(ref(ref(e.get('_loc4_'), binop('+', 'cfIcon', e.get('_loc6_'))).get(), 'gotoAndStop'), [2])
                            assign(e.ref('_loc8_'), '=', lambda: rt.construct(e.get('Color'), [ref(e.get('_loc4_'), binop('+', 'cfIcon', e.get('_loc6_'))).get()]))
                            rt.call_ref(ref(e.get('_loc8_'), 'setTransform'), [ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('_loc7_')).get(), 'playerColorTint1').get()])
                        assign(e.ref('_loc7_'), '=', lambda: binop('+', e.get('_loc7_'), 1))
                    except ASContinue:
                        pass
                    except ASBreak:
                        break
                if truth(ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'ceaseFireArr').get(), e.get('_loc2_')).get(), '_status').get()):
                    assign(e.ref('_loc9_'), '=', lambda: rt.construct(e.get('Color'), [ref(e.get('_loc4_'), 'iconCeaseFire').get()]))
                    rt.call_ref(ref(e.get('_loc9_'), 'setTransform'), [ref(ref(ref(this, 'model').get(), 'human').get(), 'playerColorTint1').get()])
                    rt.call_ref(ref(ref(e.get('_loc4_'), 'iconCeaseFire').get(), 'gotoAndStop'), [2])
                    assign(ref(ref(ref(e.get('_loc4_'), 'iconCeaseFire').get(), 'txt').get(), 'text'), '=', lambda: ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'ceaseFireArr').get(), e.get('_loc2_')).get(), '_turnsLeft').get())
                else:
                    rt.call_ref(ref(ref(e.get('_loc4_'), 'iconCeaseFire').get(), 'gotoAndStop'), [1])
                if truth(ref(e.get('_loc3_'), 'bioloaded').get()):
                    rt.call_ref(ref(ref(e.get('_loc4_'), 'iconBio').get(), 'gotoAndStop'), [2])
                else:
                    rt.call_ref(ref(ref(e.get('_loc4_'), 'iconBio').get(), 'gotoAndStop'), [1])
                assign(e.ref('_loc5_'), '=', lambda: ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), binop('+', binop('+', binop('+', 'leaderStat', e.get('_loc2_')), '_'), 1)).get(), 'maskMC').get())
                assign(ref(e.get('_loc5_'), '_yscale'), '=', lambda: ref(ref(e.get('_loc3_'), 'regardArr').get(), 0).get())
                assign(e.ref('_loc5_'), '=', lambda: ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), binop('+', binop('+', binop('+', 'leaderStat', e.get('_loc2_')), '_'), 2)).get(), 'maskMC').get())
                assign(ref(e.get('_loc5_'), '_yscale'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'populationPercentage'), [e.get('_loc3_')]))
                assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
            except ASContinue:
                pass
            except ASBreak:
                break
    else:
        if truth(binop('==', ref(ref(e.get('_global'), 'model').get(), 'view_leader_MCs_played').get(), 'false')):
            rt.call_ref(ref(this, 'set_leader_face_MC_sequence'), [])
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'updateView_debug_7', 9]))
    return U

def Sub_sub_presenter_interface_updateView_debug_7(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_sub_presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
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
    if truth(binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready')):
        pass
    if truth(binop('==', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), 'attack')):
        if truth(binop('>=', ref(ref(ref(this, 'model').get(), 'human').get(), 'spy_readiness').get(), 25)):
            pass
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'updateView_debug_8', 9]))
    return U

def Sub_sub_presenter_interface_updateView_debug_8(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_sub_presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
    assign(ref(ref(ref(this, 'view_interface').get(), 'btn_sound').get(), 'state'), '=', lambda: ref(ref(ref(this, 'model').get(), 'option').get(), 'sound').get())
    assign(ref(ref(ref(this, 'view_interface').get(), 'btn_music').get(), 'state'), '=', lambda: ref(ref(ref(this, 'model').get(), 'option').get(), 'music').get())
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'updateView_debug_9', 9]))
    return U

def Sub_sub_presenter_interface_updateView_debug_9(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_sub_presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
    rt.call_ref(ref(ref(this, 'view').get(), 'updateCities'), [])
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'updateView_debug_10', 9]))
    return U

def Sub_sub_presenter_interface_updateView_debug_10(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_sub_presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'update_statistics'), [])
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'updateView_debug_11', 9]))
    return U

def Sub_sub_presenter_interface_updateView_debug_11(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_sub_presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'update_centerScreenContent'), [])
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'updateView_debug_12', 9]))
    return U

def Sub_sub_presenter_interface_updateView_debug_12(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_sub_presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
    rt.call_ref(ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'view_interface').get(), 'update_highScore'), [ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'score').get()])
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [ref(e.get('_global'), 'view').get(), 'to_interface_timed_4', 9]))
    return U

def Sub_sub_presenter_interface_stock_req_check_single(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_req', '_btn'], ['_btn', '_loc4_', '_loc5_', '_req'], closure, 'Sub_sub_presenter_interface')
    e.set('_loc4_', False)
    e.set('_loc5_', rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'weaponStock').get(), 'getWeaponByName'), [ref(e.get('_btn'), 'relatedWeapon').get()]))
    switch_9 = e.get('_req')
    case_10 = -1
    if case_10 == -1 and strict_eq(switch_9, 'isActive'):
        case_10 = 0
    if case_10 == -1 and strict_eq(switch_9, 'weaponInStock'):
        case_10 = 1
    if case_10 == -1 and strict_eq(switch_9, 'isPayload_pre'):
        case_10 = 2
    if case_10 == -1 and strict_eq(switch_9, 'isCarrier_pre'):
        case_10 = 3
    if case_10 == -1 and strict_eq(switch_9, 'preAttackRelated'):
        case_10 = 4
    if case_10 == -1 and strict_eq(switch_9, 'attackRelated'):
        case_10 = 5
    if case_10 == -1 and strict_eq(switch_9, 'inactive'):
        case_10 = 6
    if case_10 == -1 and strict_eq(switch_9, 'defenseRelated'):
        case_10 = 7
    if case_10 == -1 and strict_eq(switch_9, 'spy_allowed'):
        case_10 = 8
    if case_10 == -1 and strict_eq(switch_9, 'false'):
        case_10 = 9
    if case_10 == -1:
        case_10 = -1
    try:
        if 0 <= case_10 <= 0:
            if truth(ref(e.get('_loc5_'), 'active').get()):
                assign(e.ref('_loc4_'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_10 <= 1:
            if truth(binop('>', ref(e.get('_loc5_'), 'inStock').get(), 0)):
                assign(e.ref('_loc4_'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_10 <= 2:
            if truth(binop('==', ref(e.get('_loc5_'), 'weaponCategory').get(), 'payload')):
                if truth(binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready')):
                    assign(e.ref('_loc4_'), '=', lambda: True)
                else:
                    assign(e.ref('_loc4_'), '=', lambda: False)
            else:
                assign(e.ref('_loc4_'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_10 <= 3:
            if truth(binop('==', ref(e.get('_loc5_'), 'weaponCategory').get(), 'carrier')):
                if truth(binop('!=', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready')):
                    assign(e.ref('_loc4_'), '=', lambda: True)
                else:
                    assign(e.ref('_loc4_'), '=', lambda: False)
            else:
                assign(e.ref('_loc4_'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_10 <= 4:
            if truth(logical('||', binop('==', ref(e.get('_loc5_'), 'weaponCategory').get(), 'carrier'), lambda: logical('||', binop('==', ref(e.get('_loc5_'), 'weaponCategory').get(), 'payload'), lambda: logical('||', binop('==', ref(e.get('_loc5_'), 'weaponCategory').get(), 'specialCarrier'), lambda: binop('==', ref(e.get('_loc5_'), 'weaponCategory').get(), 'specialLoad'))))):
                if truth(binop('==', ref(e.get('_loc5_'), 'weaponCategory').get(), 'payload')):
                    if truth(binop('>=', ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponLevel').get(), ref(e.get('_loc5_'), 'weaponLevel').get())):
                        assign(e.ref('_loc4_'), '=', lambda: True)
                    else:
                        assign(e.ref('_loc4_'), '=', lambda: False)
                else:
                    assign(e.ref('_loc4_'), '=', lambda: True)
            else:
                assign(e.ref('_loc4_'), '=', lambda: False)
            raise ASBreak()
        if 0 <= case_10 <= 5:
            if truth(binop('==', ref(e.get('_loc5_'), 'weaponCategory').get(), 'conventional')):
                assign(e.ref('_loc4_'), '=', lambda: True)
            else:
                assign(e.ref('_loc4_'), '=', lambda: False)
            raise ASBreak()
        if 0 <= case_10 <= 6:
            if truth(unary('!', ref(e.get('_loc5_'), 'active').get())):
                assign(e.ref('_loc4_'), '=', lambda: True)
            else:
                assign(e.ref('_loc4_'), '=', lambda: False)
            raise ASBreak()
        if 0 <= case_10 <= 7:
            if truth(binop('==', ref(e.get('_loc5_'), 'weaponCategory').get(), 'anti')):
                assign(e.ref('_loc4_'), '=', lambda: True)
            else:
                assign(e.ref('_loc4_'), '=', lambda: False)
            raise ASBreak()
        if 0 <= case_10 <= 8:
            if truth(binop('==', ref(e.get('_loc5_'), 'weaponCategory').get(), 'spy')):
                if truth(binop('>=', binop('/', ref(ref(ref(this, 'model').get(), 'human').get(), 'spy_readiness').get(), 25), ref(e.get('_loc5_'), 'weaponLevel').get())):
                    assign(e.ref('_loc4_'), '=', lambda: True)
                raise ASBreak()
            return True
            raise ASBreak()
        if 0 <= case_10 <= 9:
            return False
    except ASBreak:
        pass
    return e.get('_loc4_')
    return U

def Sub_sub_presenter_interface_update_leaderFaces(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_'], closure, 'Sub_sub_presenter_interface')
    if truth(binop('==', ref(ref(this, 'model').get(), 'view_leader_MCs_played').get(), 'done')):
        assign(e.ref('_loc2_'), '=', lambda: 0)
        while truth(binop('<', e.get('_loc2_'), 6)):
            rt.tick()
            try:
                rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_leaderFace'), [e.get('_loc2_'), 1, True, True])
                assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
            except ASContinue:
                pass
            except ASBreak:
                break
        assign(e.ref('_loc3_'), '=', lambda: 0)
        while truth(binop('<', e.get('_loc3_'), ref(ref(ref(this, 'model').get(), 'playerArr').get(), 'length').get())):
            rt.tick()
            try:
                assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('_loc3_')).get())
                rt.call_ref(ref(ref(this, 'view_interface').get(), 'update_leaderFace'), [ref(e.get('_loc4_'), 'playerNum').get(), ref(e.get('_loc4_'), 'faceFrame').get(), ref(e.get('_loc4_'), 'alive').get(), False, ref(e.get('_loc4_'), 'dead_avatar_played').get()])
                if truth(logical('&&', unary('!', ref(e.get('_loc4_'), 'dead_avatar_played').get()), lambda: unary('!', ref(e.get('_loc4_'), 'alive').get()))):
                    assign(ref(e.get('_loc4_'), 'dead_avatar_played'), '=', lambda: True)
                assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
            except ASContinue:
                pass
            except ASBreak:
                break
    else:
        if truth(binop('==', ref(ref(this, 'model').get(), 'view_leader_MCs_played').get(), 'false')):
            assign(e.ref('_loc5_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc5_'), 6)):
                rt.tick()
                try:
                    rt.call_ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), binop('+', 'leaderMC', e.get('_loc5_'))).get(), 'gotoAndPlay'), [e.get('_loc5_')])
                    assign(e.ref('_loc5_'), '=', lambda: binop('+', e.get('_loc5_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
    return U

def Sub_sub_presenter_interface_set_leader_face_MC_sequence(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_sub_presenter_interface')
    rt.call_ref(ref(this, 'update_leaderFaces'), [])
    assign(ref(ref(this, 'model').get(), 'view_leader_MCs_played'), '=', lambda: 'pending')
    assign(ref(ref(this, 'model').get(), 'view_leader_MCs_played_max'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), 'length').get())
    assign(ref(ref(this, 'model').get(), 'view_leader_MCs_sequence_interval_id'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'do_leader_face_MC_sequence_itteration', 500]))
    return U

def Sub_sub_presenter_interface_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Sub_sub_presenter_interface')
    ref(this, 'testVar').set('test')
    ref(this, 'minimalProductionInvestment').set(0)
    ref(this, 'megaton_by_level_arr').set(arr(['', '10 megaton', '25 megaton', '50 megaton', '95 megaton']))
    ref(this, 'blockAllBtns').set(False)
    ref(this, 'block_start_btn').set(False)

def register(rt):
    rt.define('Sub_sub_presenter_interface', None, Sub_sub_presenter_interface_fields, {'Sub_sub_presenter_interface': ASFunction(Sub_sub_presenter_interface_Sub_sub_presenter_interface), 'updateView_debug_1': ASFunction(Sub_sub_presenter_interface_updateView_debug_1), 'updateView_debug_2': ASFunction(Sub_sub_presenter_interface_updateView_debug_2), 'updateView_debug_3': ASFunction(Sub_sub_presenter_interface_updateView_debug_3), 'updateView_debug_4': ASFunction(Sub_sub_presenter_interface_updateView_debug_4), 'updateView_debug_5': ASFunction(Sub_sub_presenter_interface_updateView_debug_5), 'updateView_debug_6': ASFunction(Sub_sub_presenter_interface_updateView_debug_6), 'updateView_debug_7': ASFunction(Sub_sub_presenter_interface_updateView_debug_7), 'updateView_debug_8': ASFunction(Sub_sub_presenter_interface_updateView_debug_8), 'updateView_debug_9': ASFunction(Sub_sub_presenter_interface_updateView_debug_9), 'updateView_debug_10': ASFunction(Sub_sub_presenter_interface_updateView_debug_10), 'updateView_debug_11': ASFunction(Sub_sub_presenter_interface_updateView_debug_11), 'updateView_debug_12': ASFunction(Sub_sub_presenter_interface_updateView_debug_12), 'stock_req_check_single': ASFunction(Sub_sub_presenter_interface_stock_req_check_single), 'update_leaderFaces': ASFunction(Sub_sub_presenter_interface_update_leaderFaces), 'set_leader_face_MC_sequence': ASFunction(Sub_sub_presenter_interface_set_leader_face_MC_sequence)}, {}, {})
