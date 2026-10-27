# Generated from __Packages/Presenter_interface.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Presenter_interface_Presenter_interface(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_interface')
    e.call('__super__', [])
    assign(ref(this, 'sliderListener'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(this, 'help_data'), '=', lambda: rt.construct(e.get('Help_data'), []))
    return U

def Presenter_interface_debug_automate_func(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_nr'], ['_nr'], closure, 'Presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'debug_automate_interval_ID').get()])
    return U

def Presenter_interface_btnPressed_accept(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', 'i'], closure, 'Presenter_interface')
    e.set('_loc2_', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get())
    if truth(logical('||', binop('==', e.get('_loc2_'), 'skip_action'), lambda: logical('||', binop('==', e.get('_loc2_'), 'resources'), lambda: logical('||', logical('&&', binop('==', e.get('_loc2_'), 'production'), lambda: binop('>', ref(ref(this, 'model').get(), 'userSelectedProductionInvestmentArr_total_amount').get(), 0)), lambda: logical('||', logical('&&', binop('==', e.get('_loc2_'), 'research'), lambda: binop('>', ref(ref(ref(this, 'model').get(), 'userSelectedResearchArr').get(), 'length').get(), 0)), lambda: logical('||', binop('==', e.get('_loc2_'), 'religion'), lambda: logical('||', logical('&&', binop('==', e.get('_loc2_'), 'attack'), lambda: logical('&&', ref(ref(this, 'model').get(), 'userSelectedCity').get(), lambda: ref(ref(this, 'model').get(), 'userSelectedWeapon').get())), lambda: logical('||', logical('||', logical('&&', binop('==', e.get('_loc2_'), 'preAttack'), lambda: logical('&&', binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready'), lambda: logical('&&', ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), lambda: ref(ref(this, 'model').get(), 'userSelectedCity').get()))), lambda: logical('||', logical('&&', binop('!=', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready'), lambda: ref(ref(this, 'model').get(), 'userSelectedWeapon').get()), lambda: logical('&&', binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready'), lambda: logical('&&', binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponName').get(), 'ship'), lambda: binop('>', ref(ref(ref(this, 'model').get(), 'ship_attack_arr').get(), 'length').get(), 0))))), lambda: logical('||', logical('&&', binop('==', e.get('_loc2_'), 'defense'), lambda: ref(ref(this, 'model').get(), 'userSelectedWeapon').get()), lambda: logical('||', logical('&&', binop('==', e.get('_loc2_'), 'propaganda'), lambda: ref(ref(this, 'model').get(), 'userSelectedCity').get()), lambda: logical('&&', binop('==', e.get('_loc2_'), 'diplomacy'), lambda: logical('&&', binop('!=', ref(ref(this, 'model').get(), 'userSelectedDiplomacyLeader').get(), e.get('undefined')), lambda: logical('&&', binop('!=', ref(ref(this, 'model').get(), 'userSelectedDiplomacyOption').get(), e.get('undefined')), lambda: logical('||', binop('<=', ref(ref(ref(ref(this, 'model').get(), 'diplomacy_options_arr').get(), ref(ref(this, 'model').get(), 'userSelectedDiplomacyOption').get()).get(), 2).get(), ref(ref(ref(this, 'model').get(), 'human').get(), 'turnMoney').get()), lambda: binop('==', ref(ref(ref(ref(this, 'model').get(), 'diplomacy_options_arr').get(), ref(ref(this, 'model').get(), 'userSelectedDiplomacyOption').get()).get(), 0).get(), 'demand'))))))))))))))):
        for key_1 in keys(ref(ref(this, 'view_interface').get(), 'actionBtn_arr').get()):
            e.ref('i').set(key_1)
            rt.tick()
            try:
                assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(this, 'view_interface').get(), 'actionBtn_arr').get(), e.get('i')).get())
                if truth(binop('==', ref(e.get('_loc3_'), 'actionName').get(), ref(ref(this, 'model_interface').get(), 'selected_action_name').get())):
                    assign(ref(e.get('_loc3_'), 'isSetAction'), '=', lambda: True)
            except ASContinue:
                pass
            except ASBreak:
                break
        assign(ref(ref(ref(this, 'model_interface').get(), 'cur_pressed_action_btn').get(), 'isSetAction'), '=', lambda: True)
        rt.call_ref(ref(ref(this, 'model').get(), 'setHumanTurnAction'), [])
        rt.call_ref(ref(this, 'resetBtns'), [])
        rt.call_ref(ref(this, 'play_sound_by_action'), ['interface_acceptAction_btn'])
    if truth(logical('&&', binop('==', e.get('_loc2_'), 'diplomacy'), lambda: logical('&&', binop('>', ref(ref(ref(ref(this, 'model').get(), 'diplomacy_options_arr').get(), ref(ref(this, 'model').get(), 'userSelectedDiplomacyOption').get()).get(), 2).get(), ref(ref(ref(this, 'model').get(), 'human').get(), 'turnMoney').get()), lambda: binop('==', ref(ref(ref(ref(this, 'model').get(), 'diplomacy_options_arr').get(), ref(ref(this, 'model').get(), 'userSelectedDiplomacyOption').get()).get(), 0).get(), 'demand')))):
        assign(ref(ref(this, 'model').get(), 'interface_diplomacy_error'), '=', lambda: 'Not enough money')
        rt.call_ref(ref(this, 'update_centerScreenContent'), [])
        return e.get('undefined')
    if truth(logical('&&', binop('==', e.get('_loc2_'), 'diplomacyPending'), lambda: logical('||', logical('&&', binop('==', ref(ref(this, 'curDiplomacyOptionArr').get(), 0).get(), 'demand'), lambda: binop('>=', ref(ref(ref(this, 'model').get(), 'human').get(), 'turnMoney').get(), ref(ref(this, 'curDiplomacyOptionArr').get(), 2).get())), lambda: binop('==', ref(ref(this, 'curDiplomacyOptionArr').get(), 0).get(), 'offer')))):
        rt.call_ref(ref(this, 'accept_pending_diplomacy'), [])
        rt.call_ref(ref(this, 'play_sound_by_action'), ['interface_acceptAction_btn'])
        return e.get('undefined')
    if truth(logical('&&', binop('==', e.get('_loc2_'), 'diplomacyPending'), lambda: binop('<', ref(ref(ref(this, 'model').get(), 'human').get(), 'turnMoney').get(), ref(ref(this, 'curDiplomacyOptionArr').get(), 2).get()))):
        assign(ref(ref(e.get('_global'), 'model').get(), 'interface_diplomacy_error'), '=', lambda: 'Not enough money')
        rt.call_ref(ref(this, 'update_centerScreenContent'), [])
        return e.get('undefined')
    if truth(binop('==', e.get('_loc2_'), 'cancelPreAttack')):
        rt.call_ref(ref(this, 'play_sound_by_action'), ['interface_acceptAction_btn'])
        assign(ref(ref(this, 'model').get(), 'userSelectedCarrier'), '=', lambda: e.get('undefined'))
        assign(ref(ref(this, 'model').get(), 'userSelectedWeapon'), '=', lambda: e.get('undefined'))
        assign(ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus'), '=', lambda: 'inactive')
        assign(ref(ref(this, 'model').get(), 'userSelectedActionBtn'), '=', lambda: e.get('undefined'))
        rt.call_ref(ref(this, 'resetBtns'), [])
    return U

def Presenter_interface_btnPress(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_arrIndex'], ['_arrIndex', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_'], closure, 'Presenter_interface')
    e.set('_loc3_', ref(ref(ref(ref(ref(this, 'view_interface').get(), 'btn_arr').get(), e.get('_arrIndex')).get(), '_btn').get(), 'type').get())
    if truth(unary('!', ref(this, 'blockAllBtns').get())):
        switch_2 = e.get('_loc3_')
        case_3 = -1
        if case_3 == -1 and strict_eq(switch_2, 'action'):
            case_3 = 0
        if case_3 == -1 and strict_eq(switch_2, 'stock'):
            case_3 = 1
        if case_3 == -1:
            case_3 = -1
        try:
            if 0 <= case_3 <= 0:
                if truth(binop('==', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), 'diplomacyPending')):
                    return e.get('undefined')
                assign(ref(ref(this, 'model').get(), 'interface_research_error'), '=', lambda: e.get('undefined'))
                assign(ref(ref(this, 'model').get(), 'interface_production_error'), '=', lambda: e.get('undefined'))
                assign(ref(ref(this, 'model').get(), 'interface_diplomacy_error'), '=', lambda: e.get('undefined'))
                assign(ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'inUse'), '=', lambda: 0)
                assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(ref(this, 'view_interface').get(), 'btn_arr').get(), e.get('_arrIndex')).get(), '_btn').get())
                if truth(logical('&&', unary('!', ref(ref(ref(this, 'model').get(), 'human').get(), 'allActionsSet').get()), lambda: unary('!', ref(e.get('_loc4_'), 'bioloaded').get()))):
                    if truth(binop('==', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), ref(e.get('_loc4_'), 'actionName').get())):
                        assign(ref(ref(this, 'model').get(), 'userSelectedActionBtn'), '=', lambda: e.get('undefined'))
                        assign(ref(e.get('_loc4_'), 'pressed'), '=', lambda: False)
                        rt.call_ref(ref(this, 'play_sound_by_action'), ['interface_actionBtn_off'])
                    else:
                        if truth(unary('!', ref(e.get('_loc4_'), 'isSetAction').get())):
                            rt.call_ref(ref(this, 'play_sound_by_action'), ['interface_actionBtn_on'])
                            rt.call_ref(ref(this, 'btnPressed_cancel'), [])
                            assign(ref(ref(this, 'model').get(), 'userSelectedActionBtn'), '=', lambda: ref(e.get('_loc4_'), 'actionName').get())
                            assign(ref(ref(this, 'model_interface').get(), 'cur_pressed_action_btn'), '=', lambda: e.get('_loc4_'))
                            assign(ref(e.get('_loc4_'), 'pressed'), '=', lambda: True)
                if truth(ref(e.get('_loc4_'), 'isSetAction').get()):
                    rt.call_ref(ref(this, 'play_sound_by_action'), ['interface_actionBtn_off'])
                    if truth(binop('==', ref(e.get('_loc4_'), 'actionName').get(), ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnAction_1').get(), 'action').get())):
                        rt.call_ref(ref(this, 'btnPressed_tube'), [ref(ref(this, 'view_interface').get(), 'actionTube1').get()])
                    else:
                        rt.call_ref(ref(this, 'btnPressed_tube'), [ref(ref(this, 'view_interface').get(), 'actionTube2').get()])
                raise ASBreak()
            if 0 <= case_3 <= 1:
                if truth(ref(ref(ref(this, 'model').get(), 'human').get(), 'allActionsSet').get()):
                    return e.get('undefined')
                assign(e.ref('_loc5_'), '=', lambda: ref(ref(ref(ref(this, 'view_interface').get(), 'btn_arr').get(), e.get('_arrIndex')).get(), '_btn').get())
                assign(e.ref('_loc6_'), '=', lambda: ref(e.get('_loc5_'), 'stockPanelNum').get())
                assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'weaponStock').get(), 'getWeaponByName'), [ref(e.get('_loc5_'), 'relatedWeapon').get()]))
                rt.call_ref(ref(ref(ref(this, 'model').get(), 'userSelectedCity').get(), 'removeSelection'), ['all'])
                assign(ref(ref(this, 'model').get(), 'userSelectedCity'), '=', lambda: e.get('undefined'))
                if truth(logical('&&', logical('||', logical('&&', binop('==', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), 'attack'), lambda: logical('&&', logical('||', binop('==', e.get('_loc6_'), 6), lambda: binop('==', e.get('_loc6_'), 7)), lambda: logical('||', binop('!=', ref(e.get('_loc7_'), 'weaponType').get(), 'spy'), lambda: logical('&&', binop('==', ref(e.get('_loc7_'), 'weaponType').get(), 'spy'), lambda: binop('>=', binop('/', ref(ref(ref(this, 'model').get(), 'human').get(), 'spy_readiness').get(), 25), ref(e.get('_loc7_'), 'weaponLevel').get()))))), lambda: logical('||', logical('&&', binop('==', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), 'preAttack'), lambda: logical('&&', binop('!=', ref(e.get('_loc7_'), 'weaponName').get(), 'specialLoad'), lambda: logical('||', logical('&&', binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready'), lambda: logical('&&', logical('||', binop('==', e.get('_loc6_'), 4), lambda: binop('==', e.get('_loc6_'), 5)), lambda: binop('<=', ref(e.get('_loc7_'), 'weaponLevel').get(), ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponLevel').get()))), lambda: logical('&&', binop('!=', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready'), lambda: logical('||', binop('==', e.get('_loc6_'), 1), lambda: logical('||', binop('==', e.get('_loc6_'), 2), lambda: binop('==', e.get('_loc6_'), 3))))))), lambda: logical('||', logical('&&', binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponName').get(), 'space'), lambda: logical('&&', binop('==', ref(e.get('_loc7_'), 'weaponName').get(), 'specialLoad'), lambda: binop('==', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), 'preAttack'))), lambda: logical('&&', binop('==', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get(), 'defense'), lambda: binop('==', e.get('_loc6_'), 8))))), lambda: logical('&&', binop('>', binop('-', ref(e.get('_loc7_'), 'inStock').get(), ref(e.get('_loc7_'), 'inUse').get()), 0), lambda: ref(e.get('_loc7_'), 'active').get()))):
                    if truth(binop('==', ref(ref(this, 'model').get(), 'userSelectedStockBtn').get(), ref(e.get('_loc5_'), 'relatedWeapon').get())):
                        assign(ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'inUse'), '=', lambda: 0)
                        assign(ref(ref(this, 'model').get(), 'userSelectedStockBtn'), '=', lambda: e.get('undefined'))
                        assign(ref(ref(this, 'model').get(), 'userSelectedWeapon'), '=', lambda: e.get('undefined'))
                    else:
                        if truth(binop('!=', ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponName').get(), 'ship')):
                            assign(ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'inUse'), '=', lambda: 0)
                            assign(ref(e.get('_loc7_'), 'inUse'), '=', lambda: binop('+', ref(e.get('_loc7_'), 'inUse').get(), 1))
                        if truth(logical('||', logical('&&', binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponName').get(), 'ship'), lambda: binop('<', ref(ref(ref(this, 'model').get(), 'ship_attack_arr').get(), 'length').get(), 3)), lambda: binop('!=', ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponName').get(), 'ship'))):
                            assign(ref(ref(this, 'model').get(), 'userSelectedWeapon'), '=', lambda: e.get('_loc7_'))
                            assign(ref(ref(this, 'model').get(), 'userSelectedStockBtn'), '=', lambda: ref(e.get('_loc5_'), 'relatedWeapon').get())
                            rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_select_stock'])
                if truth(logical('&&', binop('==', ref(e.get('_loc7_'), 'weaponType').get(), 'spy'), lambda: logical('&&', binop('<', binop('/', ref(ref(ref(this, 'model').get(), 'human').get(), 'spy_readiness').get(), 25), ref(e.get('_loc7_'), 'weaponLevel').get()), lambda: binop('>', ref(e.get('_loc7_'), 'inStock').get(), 0)))):
                    assign(ref(ref(this, 'model').get(), 'interface_spy_error'), '=', lambda: 'Your spy readiness is not high enough to use this spy. <br> Choose a different spy or wait a few turns. ')
                    rt.call_ref(ref(this, 'updateView'), [])
                if truth(logical('&&', unary('!', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get()), lambda: logical('&&', binop('>', ref(e.get('_loc7_'), 'inStock').get(), 0), lambda: ref(e.get('_loc7_'), 'active').get()))):
                    if truth(logical('&&', logical('||', binop('==', e.get('_loc6_'), 6), lambda: binop('==', e.get('_loc6_'), 7)), lambda: unary('!', ref(ref(ref(this, 'model').get(), 'human').get(), 'allActionsSet').get()))):
                        rt.call_ref(ref(this, 'btnPress'), [4])
                        rt.call_ref(ref(this, 'btnPress'), [e.get('_arrIndex')])
                        rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_select_stock'])
                    if truth(logical('||', logical('&&', binop('!=', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready'), lambda: logical('||', binop('==', e.get('_loc6_'), 1), lambda: logical('||', binop('==', e.get('_loc6_'), 2), lambda: binop('==', e.get('_loc6_'), 3)))), lambda: logical('&&', binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready'), lambda: logical('&&', logical('||', binop('==', e.get('_loc6_'), 4), lambda: binop('==', e.get('_loc6_'), 5)), lambda: binop('<=', ref(e.get('_loc7_'), 'weaponLevel').get(), ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponLevel').get()))))):
                        rt.call_ref(ref(this, 'btnPress'), [5])
                        rt.call_ref(ref(this, 'btnPress'), [e.get('_arrIndex')])
                        rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_select_stock'])
                    if truth(logical('&&', binop('==', e.get('_loc6_'), 8), lambda: unary('!', ref(ref(ref(this, 'model').get(), 'human').get(), 'allActionsSet').get()))):
                        rt.call_ref(ref(this, 'btnPress'), [6])
                        rt.call_ref(ref(this, 'btnPress'), [e.get('_arrIndex')])
                        rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_select_stock'])
                    if truth(logical('&&', binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready'), lambda: logical('&&', binop('==', ref(e.get('_loc7_'), 'weaponName').get(), 'specialLoad'), lambda: binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponName').get(), 'space')))):
                        rt.call_ref(ref(this, 'btnPress'), [5])
                        rt.call_ref(ref(this, 'btnPress'), [e.get('_arrIndex')])
                        rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_select_stock'])
        except ASBreak:
            pass
        rt.call_ref(ref(this, 'updateView'), [])
    return U

def Presenter_interface_accept_pending_diplomacy(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_interface')
    if truth(binop('==', ref(ref(this, 'curDiplomacyOptionArr').get(), 0).get(), 'demand')):
        assign(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnMoney'), '-=', lambda: ref(ref(this, 'curDiplomacyOptionArr').get(), 2).get())
    rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'diplomacyAcceptedArr').get(), 'push'), [rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'diplomacyPendingArr').get(), 'shift'), [])])
    rt.call_ref(ref(this, 'resetBtns'), [])
    rt.call_ref(ref(this, 'updateView'), [])
    return U

def Presenter_interface_reject_pending_diplomacy(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_interface')
    rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'diplomacyRejectedArr').get(), 'push'), [rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'diplomacyPendingArr').get(), 'shift'), [])])
    rt.call_ref(ref(this, 'resetBtns'), [])
    rt.call_ref(ref(this, 'updateView'), [])
    return U

def Presenter_interface_btnPressed_cancel(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_actionName'], ['_actionName', '_loc3_', '_loc4_', 'i'], closure, 'Presenter_interface')
    e.set('_loc3_', logical('||', e.get('_actionName'), lambda: ref(ref(this, 'model').get(), 'userSelectedActionBtn').get()))
    switch_4 = e.get('_loc3_')
    case_5 = -1
    if case_5 == -1 and strict_eq(switch_4, 'research'):
        case_5 = 0
    if case_5 == -1 and strict_eq(switch_4, 'production'):
        case_5 = 1
    if case_5 == -1 and strict_eq(switch_4, 'diplomacyPending'):
        case_5 = 2
    if case_5 == -1 and strict_eq(switch_4, 'attack'):
        case_5 = 3
    if case_5 == -1 and strict_eq(switch_4, 'preAttack'):
        case_5 = 4
    if case_5 == -1 and strict_eq(switch_4, 'cancelPreAttack'):
        case_5 = 5
    if case_5 == -1:
        case_5 = 6
    try:
        if 0 <= case_5 <= 0:
            for key_6 in keys(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'techTree').get(), 'techArr').get()):
                e.ref('i').set(key_6)
                rt.tick()
                try:
                    assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'techTree').get(), 'techArr').get(), e.get('i')).get())
                    assign(ref(e.get('_loc4_'), 'preOrder'), '=', lambda: False)
                except ASContinue:
                    pass
                except ASBreak:
                    break
            rt.call_ref(ref(this, 'resetBtns'), [])
            return U
        if 0 <= case_5 <= 1:
            rt.call_ref(ref(this, 'resetBtns'), [])
            return U
        if 0 <= case_5 <= 2:
            rt.call_ref(ref(this, 'reject_pending_diplomacy'), [])
            rt.call_ref(ref(this, 'resetBtns'), [])
            return U
        if 0 <= case_5 <= 3:
            assign(ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'inUse'), '=', lambda: 0)
            rt.call_ref(ref(this, 'resetBtns'), [])
            return U
        if 0 <= case_5 <= 4:
            assign(ref(ref(ref(this, 'model').get(), 'userSelectedWeapon').get(), 'inUse'), '=', lambda: 0)
            if truth(logical('&&', binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready'), lambda: binop('!=', ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponName').get(), 'ship'))):
                assign(ref(ref(this, 'model').get(), 'userSelectedActionBtn'), '=', lambda: 'cancelPreAttack')
            else:
                if truth(binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponName').get(), 'ship')):
                    rt.call_ref(ref(ref(this, 'presenter').get(), 'removeShipSelection'), [])
                rt.call_ref(ref(this, 'resetBtns'), [])
            rt.call_ref(ref(this, 'updateView'), [])
            return U
        if 0 <= case_5 <= 5:
            rt.call_ref(ref(ref(this, 'presenter').get(), 'removeShipSelection'), [])
            rt.call_ref(ref(this, 'resetBtns'), [])
            return U
        if 0 <= case_5 <= 6:
            rt.call_ref(ref(this, 'resetBtns'), [])
            return U
    except ASBreak:
        pass
    return U

def Presenter_interface_btnPressed_turn(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_interface')
    assign(ref(ref(ref(this, 'view_interface').get(), 'turnBtn').get(), 'state'), '=', lambda: 'green')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'doTurn_backup_intervalID').get()])
    assign(ref(this, 'doTurn_backup_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'do_turn_backup', 2000]))
    if truth(unary('!', ref(this, 'block_start_btn').get())):
        if truth(logical('&&', ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnAction_1').get(), 'action').get(), lambda: ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnAction_2').get(), 'action').get())):
            rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'doTurn_intervalID').get()])
            assign(ref(this, 'doTurn_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'turnInterval_step1', 200]))
            assign(ref(this, 'blockAllBtns'), '=', lambda: True)
            assign(ref(this, 'block_start_btn'), '=', lambda: True)
            assign(ref(ref(ref(this, 'view_interface').get(), 'actionTube1').get(), 'state'), '=', lambda: 'closed')
        else:
            assign(ref(this, 'blockAllBtns'), '=', lambda: False)
    return U

def Presenter_interface_btnPressed_tube(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_btn'], ['_btn', '_loc3_'], closure, 'Presenter_interface')
    if truth(logical('&&', ref(ref(e.get('_btn'), 'associatedTA').get(), 'action').get(), lambda: unary('!', ref(this, 'blockAllBtns').get()))):
        rt.call_ref(ref(this, 'play_sound_by_action'), ['interface_open_tube'])
        assign(e.ref('_loc3_'), '=', lambda: ref(ref(e.get('_btn'), 'associatedTA').get(), 'action').get())
        if truth(logical('&&', binop('==', e.get('_loc3_'), 'preAttack'), lambda: binop('==', ref(ref(ref(this, 'model').get(), 'userSelectedCarrier').get(), 'weaponName').get(), 'ship'))):
            rt.call_ref(ref(ref(this, 'presenter').get(), 'removeShipSelection'), [ref(e.get('_btn'), 'associatedTA').get()])
        rt.call_ref(ref(ref(this, 'model').get(), 'deselectCities'), [e.get('_loc3_')])
        assign(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnMoney'), '+=', lambda: ref(ref(e.get('_btn'), 'associatedTA').get(), 'researchMoneySpend').get())
        assign(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnMoney'), '+=', lambda: ref(ref(e.get('_btn'), 'associatedTA').get(), 'productionMoneySpend').get())
        if truth(binop('==', ref(ref(ref(ref(this, 'model').get(), 'diplomacy_options_arr').get(), ref(ref(e.get('_btn'), 'associatedTA').get(), 'diplomacyOption').get()).get(), 0).get(), 'offer')):
            assign(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnMoney'), '+=', lambda: ref(ref(ref(ref(this, 'model').get(), 'diplomacy_options_arr').get(), ref(ref(e.get('_btn'), 'associatedTA').get(), 'diplomacyOption').get()).get(), 2).get())
        rt.call_ref(ref(this, 'btnPressed_cancel'), [e.get('_loc3_')])
        rt.call_ref(ref(ref(e.get('_btn'), 'associatedTA').get(), 'doReset'), [])
        rt.call_ref(ref(ref(this, 'model').get(), 'resetUserSelections'), [])
        rt.call_ref(ref(this, 'resetBtns'), [])
        rt.call_ref(ref(this, 'updateView'), [])
    else:
        if truth(logical('&&', unary('!', ref(ref(this, 'model').get(), 'userSelectedActionBtn').get()), lambda: unary('!', ref(this, 'blockAllBtns').get()))):
            assign(ref(ref(this, 'model').get(), 'userSelectedActionBtn'), '=', lambda: 'skip_action')
            rt.call_ref(ref(this, 'updateView'), [])
            rt.call_ref(ref(this, 'play_sound_by_action'), ['interface_open_tube'])
    return U

def Presenter_interface_btnPressed_scroll_MSG(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str'], closure, 'Presenter_interface')
    rt.call_ref(ref(ref(this, 'view_interface').get(), 'scroll_msg_txt'), [e.get('_str')])
    return U

def Presenter_interface_btnRoll_on(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_index'], ['_index'], closure, 'Presenter_interface')
    assign(ref(ref(ref(ref(ref(this, 'view_interface').get(), 'btn_arr').get(), ref(ref(this, 'model_interface').get(), 'cur_hover_btn_array_index').get()).get(), '_btn').get(), 'hover'), '=', lambda: False)
    if truth(rt.call_ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'getNextTurnAction'), [])):
        assign(ref(ref(this, 'model_interface').get(), 'cur_hover_btn_array_index'), '=', lambda: e.get('_index'))
        assign(ref(ref(ref(ref(ref(this, 'view_interface').get(), 'btn_arr').get(), e.get('_index')).get(), '_btn').get(), 'hover'), '=', lambda: True)
    return U

def Presenter_interface_full_version_mc_sound_start(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_interface')
    if truth(unary('!', ref(ref(ref(this, 'model').get(), 'option').get(), 'music').get())):
        rt.call_ref(ref(this, 'btnPressed_option'), ['music'])
    return U

def f_9(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'start'), [0, 1])
    return U

def Presenter_interface_btnPressed_option(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str', 'dont_update'], ['_str', 'dont_update'], closure, 'Presenter_interface')
    switch_7 = e.get('_str')
    case_8 = -1
    if case_8 == -1 and strict_eq(switch_7, 'sound'):
        case_8 = 0
    if case_8 == -1 and strict_eq(switch_7, 'music'):
        case_8 = 1
    if case_8 == -1:
        case_8 = -1
    try:
        if 0 <= case_8 <= 0:
            rt.call_ref(ref(ref(ref(this, 'model').get(), 'option').get(), 'setSound'), [])
            raise ASBreak()
        if 0 <= case_8 <= 1:
            if truth(ref(ref(ref(this, 'model').get(), 'option').get(), 'music').get()):
                rt.call_ref(ref(ref(ref(this, 'model').get(), 'theme_sound').get(), 'stop'), [])
            else:
                rt.call_ref(ref(ref(ref(this, 'model').get(), 'theme_sound').get(), 'start'), [0, 1])
                assign(ref(ref(ref(this, 'model').get(), 'theme_sound').get(), 'onSoundComplete'), '=', lambda: ASFunction(f_9, e))
            rt.call_ref(ref(ref(ref(this, 'model').get(), 'option').get(), 'setMusic'), [])
    except ASBreak:
        pass
    if truth(unary('!', e.get('dont_update'))):
        rt.call_ref(ref(this, 'updateView'), [])
    return U

def Presenter_interface_init_theme_snd(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_interface')
    if truth(unary('!', ref(ref(ref(this, 'model').get(), 'option').get(), 'music').get())):
        rt.call_ref(ref(this, 'btnPressed_option'), ['music', True])
    return U

def Presenter_interface_btnPressed_diplomacy(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_cat', '_num'], ['_cat', '_loc4_', '_num'], closure, 'Presenter_interface')
    switch_10 = e.get('_cat')
    case_11 = -1
    if case_11 == -1 and strict_eq(switch_10, 'leader'):
        case_11 = 0
    if case_11 == -1 and strict_eq(switch_10, 'option'):
        case_11 = 1
    if case_11 == -1:
        case_11 = -1
    try:
        if 0 <= case_11 <= 0:
            rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_select_diplo_leader'])
            assign(ref(ref(this, 'model').get(), 'userSelectedDiplomacyLeader'), '=', lambda: e.get('_num'))
            raise ASBreak()
        if 0 <= case_11 <= 1:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'diplomacy_options_arr').get(), e.get('_num')).get())
            if truth(logical('&&', binop('<', ref(ref(ref(this, 'model').get(), 'human').get(), 'turnMoney').get(), ref(e.get('_loc4_'), 2).get()), lambda: binop('==', ref(e.get('_loc4_'), 0).get(), 'offer'))):
                assign(ref(ref(e.get('_global'), 'model').get(), 'interface_diplomacy_error'), '=', lambda: 'Not enough money')
                rt.call_ref(ref(this, 'update_centerScreenContent'), [])
            else:
                assign(ref(ref(this, 'model').get(), 'userSelectedDiplomacyOption'), '=', lambda: e.get('_num'))
                rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_select_diplo_option'])
    except ASBreak:
        pass
    rt.call_ref(ref(this, 'updateView'), [])
    return U

def Presenter_interface_btnPressed_techBox(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_obj'], ['_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc8_', '_loc9_', '_obj'], closure, 'Presenter_interface')
    e.set('_loc3_', ref(e.get('_obj'), '_tech').get())
    e.set('_loc4_', False)
    e.set('_loc5_', False)
    if truth(unary('!', e.get('_loc3_'))):
        return e.get('undefined')
    if truth(ref(e.get('_loc3_'), 'preOrder').get()):
        assign(ref(e.get('_loc3_'), 'preOrder'), '=', lambda: False)
        rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_select_tech'])
    else:
        if truth(logical('||', binop('>=', ref(ref(ref(this, 'model').get(), 'human').get(), 'turnMoney').get(), binop('+', ref(e.get('_loc3_'), 'cost').get(), ref(ref(this, 'model').get(), 'researchMoneySpend').get())), lambda: logical('&&', binop('>=', ref(ref(ref(this, 'model').get(), 'human').get(), 'turnMoney').get(), ref(e.get('_loc3_'), 'cost').get()), lambda: unary('!', ref(ref(this, 'model').get(), 'researchMoneySpend').get())))):
            assign(e.ref('_loc4_'), '=', lambda: True)
        else:
            assign(e.ref('_loc4_'), '=', lambda: False)
            assign(e.ref('_loc6_'), '=', lambda: 'Not enough money!')
            rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_select_tech_false'])
        if truth(logical('&&', binop('==', ref(e.get('_loc3_'), 'desireGroup').get(), 7), lambda: ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'techTree').get(), 'allow_special').get())):
            assign(e.ref('_loc5_'), '=', lambda: True)
        else:
            if truth(binop('!=', ref(e.get('_loc3_'), 'desireGroup').get(), 7)):
                assign(e.ref('_loc5_'), '=', lambda: True)
            else:
                assign(e.ref('_loc5_'), '=', lambda: False)
                assign(e.ref('_loc6_'), '=', lambda: 'You need to invent   4 complete technologies before you can start inventing special weapons.')
        if truth(logical('&&', ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get(), lambda: unary('!', ref(e.get('_loc3_'), 'allow_in_demo').get()))):
            assign(e.ref('_loc5_'), '=', lambda: False)
            assign(e.ref('_loc6_'), '=', lambda: 'This technologie are only available in de FULL VERSION.')
        if truth(logical('&&', e.get('_loc5_'), lambda: e.get('_loc4_'))):
            assign(ref(e.get('_loc3_'), 'preOrder'), '=', lambda: True)
        else:
            if truth(e.get('_loc6_')):
                assign(ref(ref(e.get('_global'), 'model').get(), 'interface_research_error'), '=', lambda: binop('+', e.get('_loc6_'), ' <br /> '))
            if truth(e.get('_loc7_')):
                assign(ref(ref(e.get('_global'), 'model').get(), 'interface_research_error'), '+=', lambda: e.get('_loc7_'))
        rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_select_tech'])
    e.set('_loc8_', ' ')
    e.set('_loc9_', ' ')
    e.set('_loc10_', '')
    e.set('_loc11_', 0)
    assign(ref(ref(this, 'model').get(), 'userSelectedResearchArr'), '=', lambda: arr([]))
    e.set('_loc13_', 0)
    while truth(binop('<', e.get('_loc13_'), ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'techTree').get(), 'techArr').get(), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc12_'), '=', lambda: ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'techTree').get(), 'techArr').get(), e.get('_loc13_')).get())
            if truth(ref(e.get('_loc12_'), 'preOrder').get()):
                assign(e.ref('_loc8_'), '+=', lambda: binop('+', ref(e.get('_loc12_'), 'prettyName').get(), '<br /> '))
                assign(e.ref('_loc9_'), '+=', lambda: binop('+', ref(e.get('_loc12_'), 'cost').get(), '.000.000 <br /> '))
                assign(e.ref('_loc11_'), '+=', lambda: ref(e.get('_loc12_'), 'cost').get())
                rt.call_ref(ref(ref(ref(this, 'model').get(), 'userSelectedResearchArr').get(), 'push'), [obj({'techID': ref(e.get('_loc12_'), 'techID').get()})])
            assign(e.ref('_loc13_'), '=', lambda: binop('+', e.get('_loc13_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(ref(this, 'model').get(), 'researchMoneySpend'), '=', lambda: e.get('_loc11_'))
    assign(e.ref('_loc10_'), '=', lambda: binop('+', binop('+', 'estimated total: ', e.get('_loc11_')), '.000.000'))
    rt.call_ref(ref(ref(this, 'view_interface').get(), 'set_researchText'), [e.get('_loc8_'), e.get('_loc9_'), e.get('_loc10_')])
    rt.call_ref(ref(this, 'loadResearchFunc'), [])
    rt.call_ref(ref(this, 'updateView'), [])
    return U

def Presenter_interface_btn_pressed_full(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_interface')
    assign(ref(ref(e.get('_level0'), 'full_version_MC').get(), '_visible'), '=', lambda: True)
    rt.call_ref(ref(ref(e.get('_level0'), 'full_version_MC').get(), 'play'), [])
    return U

def f_12(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_'], closure, None)
    switch_13 = rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'get_demo_version_name'), [])
    case_14 = -1
    if case_14 == -1 and strict_eq(switch_13, 'Affiliates'):
        case_14 = 0
    if case_14 == -1 and strict_eq(switch_13, 'Miniclip'):
        case_14 = 1
    if case_14 == -1 and strict_eq(switch_13, 'Totallygame'):
        case_14 = 2
    if case_14 == -1 and strict_eq(switch_13, 'NewGrounds'):
        case_14 = 3
    if case_14 == -1 and strict_eq(switch_13, 'Arcadetown'):
        case_14 = 4
    if case_14 == -1 and strict_eq(switch_13, 'Agame'):
        case_14 = 5
    if case_14 == -1:
        case_14 = 6
    try:
        if 0 <= case_14 <= 0:
            assign(e.ref('_loc2_'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'unescape'), [ref(e.get('_root'), '_url').get()]))
            assign(e.ref('_loc3_'), '=', lambda: rt.call_ref(ref(e.get('_loc2_'), 'lastIndexOf'), ['_']))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(e.get('_loc2_'), 'lastIndexOf'), ['.swf']))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(e.get('_loc2_'), 'slice'), [0, e.get('_loc4_')]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(e.get('_loc5_'), 'slice'), [binop('+', e.get('_loc3_'), 1)]))
            e.call('getURL', [binop('+', 'https://secure.bmtmicro.com/servlets/Orders.ShoppingCart?CLR=0&CID=2249&PRODUCTID=22490032&AID=', e.get('_loc6_')), '_blank'])
            raise ASBreak()
        if 0 <= case_14 <= 1:
            e.call('getURL', ['http://www.miniclip.com/buy_worlddominationii.htm', '_blank'])
            raise ASBreak()
        if 0 <= case_14 <= 2:
            e.call('getURL', ['http://www.youdagames.com/World+Domination+2-game-info-107/', '_blank'])
            raise ASBreak()
        if 0 <= case_14 <= 3:
            e.call('getURL', ['https://secure.bmtmicro.com/servlets/Orders.ShoppingCart?CLR=0&CID=2249&PRODUCTID=22490032&AID=1071719', '_blank'])
            raise ASBreak()
        if 0 <= case_14 <= 4:
            e.call('getURL', [rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'get_demo_version_url'), []), '_blank'])
            raise ASBreak()
        if 0 <= case_14 <= 5:
            e.call('getURL', [rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'get_demo_version_url'), []), '_blank'])
        if 0 <= case_14 <= 6:
            return U
    except ASBreak:
        pass
    return U

def f_15(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_level0'), 'full_version_MC').get(), 'gotoAndStop'), [1])
    assign(ref(ref(e.get('_level0'), 'full_version_MC').get(), '_visible'), '=', lambda: False)
    return U

def f_16(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    return U

def Presenter_interface_load_full_version_btns(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['mc'], ['mc'], closure, 'Presenter_interface')
    assign(ref(ref(ref(e.get('mc'), 'txtMC_buy').get(), 'txt').get(), 'text'), '=', lambda: 'BUY FULL VERSION')
    assign(ref(ref(e.get('mc'), 'btn_buy').get(), 'onPress'), '=', lambda: ASFunction(f_12, e))
    assign(ref(ref(ref(e.get('mc'), 'txtMC_back').get(), 'txt').get(), 'text'), '=', lambda: 'BACK')
    assign(ref(ref(e.get('mc'), 'btn_back').get(), 'onPress'), '=', lambda: ASFunction(f_15, e))
    assign(ref(ref(ref(e.get('_level0'), 'full_version_MC').get(), 'bg').get(), 'onPress'), '=', lambda: ASFunction(f_16, e))
    assign(ref(ref(ref(e.get('_level0'), 'full_version_MC').get(), 'bg').get(), 'useHandCursor'), '=', lambda: False)
    return U

def Presenter_interface_btnPressed_spyBuilding(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_num'], ['_num'], closure, 'Presenter_interface')
    rt.call_ref(ref(e.get('_global'), 'play_sound_by_action'), ['interface_select_spy_building'])
    assign(ref(ref(this, 'model').get(), 'userSelectedSpyBuilding'), '=', lambda: ref(ref(ref(this, 'model').get(), 'spyBuildingArr').get(), e.get('_num')).get())
    rt.call_ref(ref(this, 'update_centerScreenContent'), [])
    return U

def Presenter_interface_btnRoll_off(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_interface')
    assign(ref(ref(ref(ref(ref(this, 'view_interface').get(), 'btn_arr').get(), ref(ref(this, 'model_interface').get(), 'cur_hover_btn_array_index').get()).get(), '_btn').get(), 'hover'), '=', lambda: False)
    assign(ref(ref(this, 'model_interface').get(), 'cur_hover_btn_array_index'), '=', lambda: unary('-', 1))
    return U

def Presenter_interface_btnPressed_index_c(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_mc'], ['a_mc'], closure, 'Presenter_interface')
    if truth(binop('==', ref(ref(this, 'model').get(), 'm11').get(), 'xx1231')):
        assign(ref(ref(this, 'model').get(), 'userSelectedActionBtn'), '=', lambda: 'cheat')
        rt.call_ref(ref(this, 'updateView'), [])
    if truth(binop('==', ref(ref(ref(ref(e.get('a_mc'), '_parent').get(), 'input_').get(), 'chTXT').get(), 'text').get(), 'youda')):
        assign(ref(ref(this, 'model').get(), 'm11'), '=', lambda: 'xx1231')
        assign(ref(ref(this, 'model').get(), 'userSelectedActionBtn'), '=', lambda: 'cheat')
        rt.call_ref(ref(this, 'updateView'), [])
    rt.call_ref(ref(ref(ref(e.get('a_mc'), '_parent').get(), 'input_').get(), 'nextFrame'), [])
    return U

def Presenter_interface___set__citiesSelectable(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_bln'], ['_bln', 'i', 'j'], closure, 'Presenter_interface')
    for key_17 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_17)
        rt.tick()
        try:
            for key_18 in keys(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get(), 'cityArr').get()):
                e.ref('j').set(key_18)
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

def Presenter_interface___get__citiesSelectable(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_interface')
    return True
    return U

def Presenter_interface_setSliderValue(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc0_', '_loc2_', '_loc3_', '_loc4_', '_loc5_'], closure, 'Presenter_interface')
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

def Presenter_interface_format_for_production(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['_loc3_', '_loc4_', '_loc5_', 'a_nr'], closure, 'Presenter_interface')
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

def Presenter_interface_display_format_dot_notation(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['_loc3_', '_loc4_', '_loc5_', 'a_nr'], closure, 'Presenter_interface')
    e.set('_loc3_', binop('+', e.get('a_nr'), ''))
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

def Presenter_interface_set_sliders_after_error(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_'], closure, 'Presenter_interface')
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

def Presenter_interface_set_research_after_error(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_'], closure, 'Presenter_interface')
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
                assign(e.ref('_loc3_'), '+=', lambda: binop('+', ref(e.get('_loc2_'), 'prettyName').get(), ' <br /> '))
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

def f_19(rt, this, args, closure=None):
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

def f_20(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'setSliderValue'), [])
    assign(ref(ref(e.get('_global'), 'presenter_interface').get(), 'pressedSliderObj'), '=', lambda: e.get('undefined'))
    rt.call_ref(ref(e.get('Mouse'), 'removeListener'), [ref(ref(e.get('_global'), 'presenter_interface').get(), 'sliderListener').get()])
    return U

def Presenter_interface_slider_action(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['__obj'], ['__obj'], closure, 'Presenter_interface')
    assign(ref(this, 'pressedSliderObj'), '=', lambda: e.get('__obj'))
    if truth(unary('!', ref(e.get('__obj'), '_bg').get())):
        assign(ref(ref(this, 'pressedSliderObj').get(), 'regPoint'), '=', lambda: ref(ref(e.get('__obj'), '_mc').get(), '_xmouse').get())
    else:
        assign(ref(ref(this, 'pressedSliderObj').get(), 'regPoint'), '=', lambda: 0)
    assign(ref(ref(this, 'pressedSliderObj').get(), 'curVal'), '=', lambda: 0)
    assign(ref(ref(this, 'pressedSliderObj').get(), 'type'), '=', lambda: ref(e.get('__obj'), 'type').get())
    assign(ref(ref(this, 'pressedSliderObj').get(), 'num'), '=', lambda: ref(e.get('__obj'), 'num').get())
    assign(ref(ref(this, 'sliderListener').get(), 'onMouseMove'), '=', lambda: ASFunction(f_19, e))
    assign(ref(ref(this, 'sliderListener').get(), 'onMouseUp'), '=', lambda: ASFunction(f_20, e))
    rt.call_ref(ref(e.get('Mouse'), 'addListener'), [ref(this, 'sliderListener').get()])
    if truth(ref(e.get('__obj'), '_bg').get()):
        rt.call_ref(ref(ref(this, 'sliderListener').get(), 'onMouseMove'), [])
    return U

def Presenter_interface_roll_over_map(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_num'], ['_loc3_', 'a_num'], closure, 'Presenter_interface')
    if truth(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('a_num')).get(), 'alive').get()):
        assign(e.ref('_loc3_'), '=', lambda: rt.construct(e.get('Color'), [ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), binop('+', 'leader_flash', e.get('a_num'))).get()]))
        rt.call_ref(ref(e.get('_loc3_'), 'setTransform'), [ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('a_num')).get(), 'playerColorTint1').get()])
        rt.call_ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), binop('+', 'leader_flash', e.get('a_num'))).get(), 'play'), [])
    return U

def f_21(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(e.get('_global'), 'model').get(), 'interface_production_error'), '=', lambda: e.get('undefined'))
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'update_centerScreenContent'), [])
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'set_sliders_after_error'), [])
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
    if truth(unary('!', rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'techTree').get(), 'allow_production_by_group'), [ref(ref(ref(ref(e.get('_global'), 'model').get(), '_userSelectedProductionInvestmentArr').get(), ref(ref(this, '_obj').get(), 'num').get()).get(), 2).get()]))):
        assign(ref(ref(e.get('_global'), 'model').get(), 'interface_production_error'), '=', lambda: 'You have not yet invented this Technology')
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'updateView'), [])
    else:
        assign(ref(ref(this, '_obj').get(), '_mc'), '=', lambda: this)
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'slider_action'), [ref(this, '_obj').get()])
    return U

def f_25(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(unary('!', rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'techTree').get(), 'allow_production_by_group'), [ref(ref(ref(ref(e.get('_global'), 'model').get(), '_userSelectedProductionInvestmentArr').get(), ref(ref(this, '_obj').get(), 'num').get()).get(), 2).get()]))):
        assign(ref(ref(e.get('_global'), 'model').get(), 'interface_production_error'), '=', lambda: 'You have not yet invented this Technology')
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'updateView'), [])
    else:
        assign(ref(ref(this, '_obj').get(), '_mc'), '=', lambda: ref(ref(this, '_parent').get(), 'sliderBtn').get())
        assign(ref(ref(this, '_obj').get(), '_bg'), '=', lambda: True)
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'slider_action'), [ref(this, '_obj').get()])
    return U

def Presenter_interface_loadProductionFunc(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_error'], ['_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', 'a_error'], closure, 'Presenter_interface')
    if truth(e.get('a_error')):
        assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get())
        assign(ref(ref(ref(e.get('_loc3_'), 'error_window').get(), 'text1').get(), 'htmlText'), '=', lambda: e.get('a_error'))
        assign(ref(ref(ref(e.get('_loc3_'), 'error_window').get(), 'btnOK').get(), 'onPress'), '=', lambda: ASFunction(f_21, e))
        assign(ref(ref(ref(e.get('_loc3_'), 'error_window').get(), 'btnOK').get(), 'onRollOver'), '=', lambda: ASFunction(f_22, e))
        assign(ref(ref(ref(e.get('_loc3_'), 'error_window').get(), 'btnOK').get(), 'onRollOut'), '=', lambda: ASFunction(f_23, e))
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
            assign(ref(ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), binop('+', 'slide', e.get('_loc7_'))).get(), 'sliderBtn').get(), 'onPress'), '=', lambda: ASFunction(f_24, e))
            assign(ref(ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), binop('+', 'slide', e.get('_loc7_'))).get(), 'sliderBG').get(), '_obj'), '=', lambda: e.get('_loc8_'))
            assign(ref(ref(ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), 'centerScreen').get(), binop('+', 'slide', e.get('_loc7_'))).get(), 'sliderBG').get(), 'onPress'), '=', lambda: ASFunction(f_25, e))
            assign(e.ref('_loc7_'), '=', lambda: binop('+', e.get('_loc7_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Presenter_interface_removeBioClips(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'Presenter_interface')
    for key_26 in keys(ref(ref(this, 'view_interface').get(), 'actionBtn_arr').get()):
        e.ref('i').set(key_26)
        rt.tick()
        try:
            assign(ref(ref(ref(ref(this, 'view_interface').get(), 'actionBtn_arr').get(), e.get('i')).get(), 'bioloaded'), '=', lambda: False)
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_27 in keys(ref(ref(this, 'view_interface').get(), 'stockBtn_arr').get()):
        e.ref('i').set(key_27)
        rt.tick()
        try:
            assign(ref(ref(ref(ref(this, 'view_interface').get(), 'stockBtn_arr').get(), e.get('i')).get(), 'bioloaded'), '=', lambda: False)
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Presenter_interface_attachBioClips(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', 'i', 'j'], closure, 'Presenter_interface')
    for key_28 in keys(ref(ref(ref(this, 'model').get(), 'human').get(), 'bioloadedActionsArr').get()):
        e.ref('i').set(key_28)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'bioloadedActionsArr').get(), e.get('i')).get())
            for key_29 in keys(ref(ref(this, 'view_interface').get(), 'actionBtn_arr').get()):
                e.ref('j').set(key_29)
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
    for key_30 in keys(ref(ref(ref(this, 'model').get(), 'human').get(), 'bioloadedStockArr').get()):
        e.ref('i').set(key_30)
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'bioloadedStockArr').get(), e.get('i')).get())
            for key_31 in keys(ref(ref(this, 'view_interface').get(), 'stockBtn_arr').get()):
                e.ref('j').set(key_31)
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

def Presenter_interface_launch_space_rocket_sound(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_interface')
    rt.call_ref(ref(this, 'play_sound_by_event'), ['space_launch'])
    return U

def Presenter_interface_play_sound_by_obj(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_obj'], ['_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_obj'], closure, 'Presenter_interface')
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

def Presenter_interface_play_ambient_sound_by_building_frame(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_frame'], ['_frame', '_loc3_', '_loc4_', 'i'], closure, 'Presenter_interface')
    if truth(unary('!', ref(ref(ref(e.get('_global'), 'model').get(), 'option').get(), 'playSound').get())):
        return e.get('undefined')
    for key_32 in keys(ref(ref(this, 'model').get(), 'active_ambient_sounds').get()):
        e.ref('i').set(key_32)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'model').get(), 'active_ambient_sounds').get(), e.get('i')).get(), e.get('_frame'))):
                return e.get('undefined')
        except ASContinue:
            pass
        except ASBreak:
            break
    if truth(unary('!', ref(ref(ref(this, 'view').get(), 'srcMC').get(), binop('+', 'ambient_sound_', ref(ref(this, 'model').get(), 'ambient_sound_index').get())).get())):
        rt.call_ref(ref(ref(ref(this, 'view').get(), 'srcMC').get(), 'createEmptyMovieClip'), [binop('+', 'ambient_sound_', ref(ref(this, 'model').get(), 'ambient_sound_index').get()), rt.call_ref(ref(ref(ref(this, 'view').get(), 'srcMC').get(), 'getNextHighestDepth'), [])])
    e.set('_loc3_', ref(ref(ref(this, 'view').get(), 'srcMC').get(), binop('+', 'ambient_sound_', ref(ref(this, 'model').get(), 'ambient_sound_index').get())).get())
    e.set('_loc4_', rt.construct(e.get('Sound'), [e.get('_loc3_')]))
    for key_33 in keys(ref(ref(this, 'model').get(), 'ambient_sound_arr').get()):
        e.ref('i').set(key_33)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(ref(this, 'model').get(), 'ambient_sound_arr').get(), e.get('i')).get(), '_building').get(), e.get('_frame'))):
                rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'playing_ambient_sound_arr').get(), ref(ref(this, 'model').get(), 'ambient_sound_index').get()).get(), 'stop'), [])
                rt.call_ref(ref(e.get('_loc4_'), 'attachSound'), [ref(ref(ref(ref(this, 'model').get(), 'ambient_sound_arr').get(), e.get('i')).get(), '_soundName').get()])
                rt.call_ref(ref(e.get('_loc4_'), 'start'), [0, 9999])
                rt.call_ref(ref(e.get('_loc4_'), 'setVolume'), [21])
                assign(ref(ref(ref(this, 'model').get(), 'playing_ambient_sound_arr').get(), ref(ref(this, 'model').get(), 'ambient_sound_index').get()), '=', lambda: e.get('_loc4_'))
                rt.call_ref(ref(ref(this, 'model').get(), 'next_ambient_sound_index'), [])
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Presenter_interface_play_sound_by_action(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_action'], ['_action', '_loc3_', 'i'], closure, 'Presenter_interface')
    if truth(unary('!', ref(ref(ref(e.get('_global'), 'model').get(), 'option').get(), 'playSound').get())):
        return e.get('undefined')
    for key_34 in keys(ref(ref(this, 'model').get(), 'action_to_sound_arr').get()):
        e.ref('i').set(key_34)
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

def Presenter_interface_play_sound_by_building(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_building', '_plrNum'], ['_building', '_loc0_', '_loc4_', '_plrNum', 'i'], closure, 'Presenter_interface')
    if truth(unary('!', ref(ref(ref(e.get('_global'), 'model').get(), 'option').get(), 'playSound').get())):
        return e.get('undefined')
    for key_35 in keys(ref(ref(this, 'model').get(), 'building_to_sound_arr').get()):
        e.ref('i').set(key_35)
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

def Presenter_interface_play_satellite_sound(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_interface')
    if truth(ref(ref(e.get('_global'), 'model').get(), 'satellite_sound_playing').get()):
        return e.get('undefined')
    assign(ref(ref(e.get('_global'), 'model').get(), 'satellite_sound_playing'), '=', lambda: True)
    rt.call_ref(ref(this, 'play_sound_by_event'), ['satellite_flight'])
    return U

def Presenter_interface_play_sound_by_event(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_event', '_panX'], ['_event', '_loc4_', '_panX', 'i'], closure, 'Presenter_interface')
    if truth(unary('!', ref(ref(ref(e.get('_global'), 'model').get(), 'option').get(), 'playSound').get())):
        return e.get('undefined')
    for key_36 in keys(ref(ref(this, 'model').get(), 'event_to_sound_arr').get()):
        e.ref('i').set(key_36)
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

def Presenter_interface_getPanBy_x(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_xNum'], ['_loc3_', '_xNum'], closure, 'Presenter_interface')
    e.set('_loc3_', binop('*', binop('-', binop('/', e.get('_xNum'), 8), 50), 2))
    return e.get('_loc3_')
    return U

def Presenter_interface_explosion_sound_by_mc_name(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str', '_mcx'], ['_loc4_', '_mcx', '_str', 'i'], closure, 'Presenter_interface')
    for key_37 in keys(ref(ref(this, 'model').get(), 'explosion_MC_to_sound_arr').get()):
        e.ref('i').set(key_37)
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

def Presenter_interface_reset_leader_stat_bars(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_'], closure, 'Presenter_interface')
    e.set('_loc3_', 0)
    while truth(binop('<', e.get('_loc3_'), 6)):
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), binop('+', binop('+', binop('+', 'leaderStat', e.get('_loc3_')), '_'), 1)).get(), 'maskMC').get())
            assign(ref(e.get('_loc2_'), '_yscale'), '=', lambda: 0)
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), binop('+', binop('+', binop('+', 'leaderStat', e.get('_loc3_')), '_'), 2)).get(), 'maskMC').get())
            assign(ref(e.get('_loc2_'), '_yscale'), '=', lambda: 0)
            assign(e.ref('_loc4_'), '=', lambda: rt.construct(e.get('Color'), [ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), binop('+', binop('+', binop('+', 'leaderStat', e.get('_loc3_')), '_'), 1)).get()]))
            assign(e.ref('_loc5_'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), e.get('_loc3_')).get())
            rt.call_ref(ref(e.get('_loc4_'), 'setTransform'), [ref(e.get('_loc5_'), 'playerColorTint1').get()])
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Presenter_interface_roll_over_stat(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['p_str', 'p_plr_num'], ['_loc4_', '_loc5_', '_loc6_', 'i', 'p_plr_num', 'p_str'], closure, 'Presenter_interface')
    switch_38 = e.get('p_str')
    case_39 = -1
    if case_39 == -1 and strict_eq(switch_38, 'regard'):
        case_39 = 0
    if case_39 == -1 and strict_eq(switch_38, 'population'):
        case_39 = 1
    if case_39 == -1:
        case_39 = 2
    try:
        if 0 <= case_39 <= 0:
            assign(e.ref('_loc4_'), '=', lambda: '')
            for key_40 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
                e.ref('i').set(key_40)
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
        if 0 <= case_39 <= 1:
            assign(ref(ref(this, 'view_interface').get(), 'infoLine'), '=', lambda: e.get('p_str'))
        if 0 <= case_39 <= 2:
            return U
    except ASBreak:
        pass
    return U

def Presenter_interface_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Presenter_interface')
    pass

def register(rt):
    rt.define('Presenter_interface', 'Sub_Presenter_interface', Presenter_interface_fields, {'Presenter_interface': ASFunction(Presenter_interface_Presenter_interface), 'debug_automate_func': ASFunction(Presenter_interface_debug_automate_func), 'btnPressed_accept': ASFunction(Presenter_interface_btnPressed_accept), 'btnPress': ASFunction(Presenter_interface_btnPress), 'accept_pending_diplomacy': ASFunction(Presenter_interface_accept_pending_diplomacy), 'reject_pending_diplomacy': ASFunction(Presenter_interface_reject_pending_diplomacy), 'btnPressed_cancel': ASFunction(Presenter_interface_btnPressed_cancel), 'btnPressed_turn': ASFunction(Presenter_interface_btnPressed_turn), 'btnPressed_tube': ASFunction(Presenter_interface_btnPressed_tube), 'btnPressed_scroll_MSG': ASFunction(Presenter_interface_btnPressed_scroll_MSG), 'btnRoll_on': ASFunction(Presenter_interface_btnRoll_on), 'full_version_mc_sound_start': ASFunction(Presenter_interface_full_version_mc_sound_start), 'btnPressed_option': ASFunction(Presenter_interface_btnPressed_option), 'init_theme_snd': ASFunction(Presenter_interface_init_theme_snd), 'btnPressed_diplomacy': ASFunction(Presenter_interface_btnPressed_diplomacy), 'btnPressed_techBox': ASFunction(Presenter_interface_btnPressed_techBox), 'btn_pressed_full': ASFunction(Presenter_interface_btn_pressed_full), 'load_full_version_btns': ASFunction(Presenter_interface_load_full_version_btns), 'btnPressed_spyBuilding': ASFunction(Presenter_interface_btnPressed_spyBuilding), 'btnRoll_off': ASFunction(Presenter_interface_btnRoll_off), 'btnPressed_index_c': ASFunction(Presenter_interface_btnPressed_index_c), 'setSliderValue': ASFunction(Presenter_interface_setSliderValue), 'format_for_production': ASFunction(Presenter_interface_format_for_production), 'display_format_dot_notation': ASFunction(Presenter_interface_display_format_dot_notation), 'set_sliders_after_error': ASFunction(Presenter_interface_set_sliders_after_error), 'set_research_after_error': ASFunction(Presenter_interface_set_research_after_error), 'slider_action': ASFunction(Presenter_interface_slider_action), 'roll_over_map': ASFunction(Presenter_interface_roll_over_map), 'loadProductionFunc': ASFunction(Presenter_interface_loadProductionFunc), 'removeBioClips': ASFunction(Presenter_interface_removeBioClips), 'attachBioClips': ASFunction(Presenter_interface_attachBioClips), 'launch_space_rocket_sound': ASFunction(Presenter_interface_launch_space_rocket_sound), 'play_sound_by_obj': ASFunction(Presenter_interface_play_sound_by_obj), 'play_ambient_sound_by_building_frame': ASFunction(Presenter_interface_play_ambient_sound_by_building_frame), 'play_sound_by_action': ASFunction(Presenter_interface_play_sound_by_action), 'play_sound_by_building': ASFunction(Presenter_interface_play_sound_by_building), 'play_satellite_sound': ASFunction(Presenter_interface_play_satellite_sound), 'play_sound_by_event': ASFunction(Presenter_interface_play_sound_by_event), 'getPanBy_x': ASFunction(Presenter_interface_getPanBy_x), 'explosion_sound_by_mc_name': ASFunction(Presenter_interface_explosion_sound_by_mc_name), 'reset_leader_stat_bars': ASFunction(Presenter_interface_reset_leader_stat_bars), 'roll_over_stat': ASFunction(Presenter_interface_roll_over_stat)}, {'citiesSelectable': ASFunction(Presenter_interface___get__citiesSelectable)}, {'citiesSelectable': ASFunction(Presenter_interface___set__citiesSelectable)})
