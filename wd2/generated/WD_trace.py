# Generated from __Packages/WD_trace.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def WD_trace_WD_trace(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'WD_trace')
    assign(ref(this, 'lc'), '=', lambda: rt.construct(e.get('LocalConnection'), []))
    return U

def WD_trace_trace(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str'], closure, 'WD_trace')
    rt.call_ref(ref(ref(this, 'lc').get(), 'send'), ['WD2', 'trace', e.get('_str')])
    return U

def WD_trace_specific_trace(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str', '_str2'], ['_loc10_', '_loc11_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', '_str', '_str2', 'i', 'j'], closure, 'WD_trace')
    e.set('_loc4_', '')
    e.set('_loc5_', '')
    switch_1 = e.get('_str')
    case_2 = -1
    if case_2 == -1 and strict_eq(switch_1, 'aiGameVars'):
        case_2 = 0
    if case_2 == -1 and strict_eq(switch_1, 'lastAction'):
        case_2 = 1
    if case_2 == -1 and strict_eq(switch_1, 'stock'):
        case_2 = 2
    if case_2 == -1 and strict_eq(switch_1, 'proTech'):
        case_2 = 3
    if case_2 == -1 and strict_eq(switch_1, 'bio'):
        case_2 = 4
    if case_2 == -1 and strict_eq(switch_1, 'ceaseFire'):
        case_2 = 5
    if case_2 == -1 and strict_eq(switch_1, 'regard'):
        case_2 = 6
    if case_2 == -1 and strict_eq(switch_1, 'crashTest'):
        case_2 = 7
    if case_2 == -1:
        case_2 = 8
    try:
        if 0 <= case_2 <= 0:
            for key_3 in keys(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get()):
                e.ref('i').set(key_3)
                rt.tick()
                try:
                    assign(e.ref('_loc6_'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), e.get('i')).get())
                    assign(e.ref('_loc4_'), '+=', lambda: binop('+', binop('+', binop('+', binop('+', 'player ', ref(e.get('_loc6_'), 'playerNum').get()), ': Money: '), ref(e.get('_loc6_'), 'money').get()), ' <br/> '))
                    assign(e.ref('_loc4_'), '+=', lambda: binop('+', binop('+', binop('+', binop('+', 'player ', ref(e.get('_loc6_'), 'playerNum').get()), ': religion: '), ref(e.get('_loc6_'), 'religion').get()), ' <br/> '))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            raise ASBreak()
            rt.call_ref(ref(ref(this, 'lc').get(), 'send'), ['WD2', 'specific_trace', 'aiGameVars', e.get('_loc4_')])
        if 0 <= case_2 <= 1:
            for key_4 in keys(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get()):
                e.ref('i').set(key_4)
                rt.tick()
                try:
                    assign(e.ref('_loc6_'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), e.get('i')).get())
                    assign(e.ref('_loc4_'), '+=', lambda: binop('+', binop('+', binop('+', binop('+', binop('+', binop('+', 'player ', ref(e.get('_loc6_'), 'playerNum').get()), ': Action 1 - '), ref(ref(e.get('_loc6_'), 'turnAction_1').get(), 'action').get()), ' turn: '), ref(ref(e.get('_global'), 'model').get(), 'turn').get()), ' <br/> '))
                    assign(e.ref('_loc4_'), '+=', lambda: binop('+', binop('+', binop('+', binop('+', binop('+', binop('+', 'player ', ref(e.get('_loc6_'), 'playerNum').get()), ': Action 2 - '), ref(ref(e.get('_loc6_'), 'turnAction_2').get(), 'action').get()), ' turn: '), ref(ref(e.get('_global'), 'model').get(), 'turn').get()), ' <br/> '))
                    assign(e.ref('_loc5_'), '+=', lambda: binop('+', binop('+', binop('+', binop('+', binop('+', ' <u> --Player: ', ref(e.get('_loc6_'), 'playerNum').get()), ' turn: '), ref(ref(e.get('_global'), 'model').get(), 'turn').get()), ', action 1: </u><br/>'), ref(ref(e.get('_loc6_'), 'turnAction_1').get(), 'actionNames').get()))
                    assign(e.ref('_loc5_'), '+=', lambda: binop('+', binop('+', binop('+', binop('+', binop('+', ' <u> --Player: ', ref(e.get('_loc6_'), 'playerNum').get()), ' turn: '), ref(ref(e.get('_global'), 'model').get(), 'turn').get()), ', action 2: </u><br/>'), ref(ref(e.get('_loc6_'), 'turnAction_2').get(), 'actionNames').get()))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            raise ASBreak()
            rt.call_ref(ref(ref(this, 'lc').get(), 'send'), ['WD2', 'specific_trace', 'lastActionDetails', e.get('_loc5_')])
        if 0 <= case_2 <= 2:
            for key_5 in keys(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get()):
                e.ref('i').set(key_5)
                rt.tick()
                try:
                    assign(e.ref('_loc6_'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), e.get('i')).get())
                    assign(e.ref('_loc4_'), '+=', lambda: binop('+', binop('+', ' ---  player: ', ref(e.get('_loc6_'), 'playerNum').get()), ' <br/> '))
                    for key_6 in keys(ref(ref(e.get('_loc6_'), 'weaponStock').get(), 'weaponArr').get()):
                        e.ref('j').set(key_6)
                        rt.tick()
                        try:
                            assign(e.ref('_loc7_'), '=', lambda: ref(ref(ref(e.get('_loc6_'), 'weaponStock').get(), 'weaponArr').get(), e.get('j')).get())
                            if truth(ref(e.get('_loc7_'), 'active').get()):
                                assign(e.ref('_loc4_'), '+=', lambda: binop('+', binop('+', binop('+', ref(e.get('_loc7_'), 'weaponName').get(), ' : '), ref(e.get('_loc7_'), 'inStock').get()), ' <br/> '))
                        except ASContinue:
                            pass
                        except ASBreak:
                            break
                    assign(e.ref('_loc4_'), '+=', lambda: binop('+', binop('+', 'Anti Air: ', ref(ref(ref(e.get('_loc6_'), 'weaponStock').get(), 'antiAir').get(), 'inStock').get()), ' <br /> '))
                    assign(e.ref('_loc4_'), '+=', lambda: binop('+', binop('+', 'Anti Roc: ', ref(ref(ref(e.get('_loc6_'), 'weaponStock').get(), 'antiRocket').get(), 'inStock').get()), ' <br />'))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            raise ASBreak()
            rt.call_ref(ref(ref(this, 'lc').get(), 'send'), ['WD2', 'specific_trace', 'stock', e.get('_loc4_')])
        if 0 <= case_2 <= 3:
            for key_7 in keys(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get()):
                e.ref('i').set(key_7)
                rt.tick()
                try:
                    assign(e.ref('_loc6_'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), e.get('i')).get())
                    assign(e.ref('_loc4_'), '+=', lambda: binop('+', binop('+', ' ---  player: ', ref(e.get('_loc6_'), 'playerNum').get()), ' <br/> '))
                    assign(e.ref('_loc8_'), '=', lambda: 0)
                    while truth(binop('<', e.get('_loc8_'), ref(ref(e.get('_loc6_'), 'shortMSG_arr').get(), 'length').get())):
                        rt.tick()
                        try:
                            assign(e.ref('_loc9_'), '=', lambda: ref(ref(e.get('_loc6_'), 'shortMSG_arr').get(), e.get('_loc8_')).get())
                            if truth(logical('&&', binop('!=', ref(e.get('_loc9_'), '_msg').get(), ''), lambda: ref(e.get('_loc9_'), '_msg').get())):
                                assign(e.ref('_loc4_'), '+=', lambda: binop('+', ref(e.get('_loc9_'), '_msg').get(), '<br />'))
                            assign(e.ref('_loc8_'), '=', lambda: binop('+', e.get('_loc8_'), 1))
                        except ASContinue:
                            pass
                        except ASBreak:
                            break
                except ASContinue:
                    pass
                except ASBreak:
                    break
            raise ASBreak()
            rt.call_ref(ref(ref(this, 'lc').get(), 'send'), ['WD2', 'specific_trace', 'proTech', e.get('_loc4_')])
        if 0 <= case_2 <= 4:
            for key_8 in keys(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get()):
                e.ref('i').set(key_8)
                rt.tick()
                try:
                    assign(e.ref('_loc6_'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), e.get('i')).get())
                    assign(e.ref('_loc4_'), '+=', lambda: binop('+', binop('+', ' ---  player: ', ref(e.get('_loc6_'), 'playerNum').get()), ' <br/> '))
                    for key_9 in keys(ref(e.get('_loc6_'), 'bioloadedActionsArr').get()):
                        e.ref('j').set(key_9)
                        rt.tick()
                        try:
                            assign(e.ref('_loc4_'), '+=', lambda: binop('+', ref(ref(e.get('_loc6_'), 'bioloadedActionsArr').get(), e.get('j')).get(), ' <br />'))
                        except ASContinue:
                            pass
                        except ASBreak:
                            break
                except ASContinue:
                    pass
                except ASBreak:
                    break
            raise ASBreak()
            rt.call_ref(ref(ref(this, 'lc').get(), 'send'), ['WD2', 'specific_trace', 'bio', e.get('_loc4_')])
        if 0 <= case_2 <= 5:
            for key_10 in keys(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get()):
                e.ref('i').set(key_10)
                rt.tick()
                try:
                    assign(e.ref('_loc6_'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), e.get('i')).get())
                    assign(e.ref('_loc4_'), '+=', lambda: binop('+', binop('+', ' ---  player: ', ref(e.get('_loc6_'), 'playerNum').get()), ' <br/> '))
                    assign(e.ref('_loc10_'), '=', lambda: 0)
                    while truth(binop('<', e.get('_loc10_'), ref(ref(e.get('_loc6_'), 'ceaseFireArr').get(), 'length').get())):
                        rt.tick()
                        try:
                            if truth(ref(ref(ref(e.get('_loc6_'), 'ceaseFireArr').get(), e.get('_loc10_')).get(), '_status').get()):
                                assign(e.ref('_loc4_'), '+=', lambda: binop('+', binop('+', binop('+', binop('+', 'cease fire with: ', e.get('_loc10_')), ' for: '), ref(ref(ref(e.get('_loc6_'), 'ceaseFireArr').get(), e.get('_loc10_')).get(), '_turnsLeft').get()), ' turns'))
                            assign(e.ref('_loc10_'), '=', lambda: binop('+', e.get('_loc10_'), 1))
                        except ASContinue:
                            pass
                        except ASBreak:
                            break
                except ASContinue:
                    pass
                except ASBreak:
                    break
            raise ASBreak()
        if 0 <= case_2 <= 6:
            for key_11 in keys(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get()):
                e.ref('i').set(key_11)
                rt.tick()
                try:
                    assign(e.ref('_loc6_'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), e.get('i')).get())
                    assign(e.ref('_loc4_'), '+=', lambda: binop('+', binop('+', ' Player: ', ref(e.get('_loc6_'), 'playerNum').get()), ' <br/>'))
                    assign(e.ref('_loc11_'), '=', lambda: 0)
                    while truth(binop('<', e.get('_loc11_'), ref(ref(e.get('_loc6_'), 'regardArr').get(), 'length').get())):
                        rt.tick()
                        try:
                            assign(e.ref('_loc4_'), '+=', lambda: binop('+', binop('+', binop('+', binop('+', '  -- towards: ', e.get('_loc11_')), ' : '), ref(ref(e.get('_loc6_'), 'regardArr').get(), e.get('_loc11_')).get()), '<br/>'))
                            assign(e.ref('_loc11_'), '=', lambda: binop('+', e.get('_loc11_'), 1))
                        except ASContinue:
                            pass
                        except ASBreak:
                            break
                except ASContinue:
                    pass
                except ASBreak:
                    break
            raise ASBreak()
        if 0 <= case_2 <= 7:
            rt.call_ref(ref(ref(this, 'lc').get(), 'send'), ['WD2', 'specific_trace', 'ceaseFire', e.get('_str2')])
        if 0 <= case_2 <= 8:
            return U
    except ASBreak:
        pass
    return U

def WD_trace_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'WD_trace')
    pass

def register(rt):
    rt.define('WD_trace', None, WD_trace_fields, {'WD_trace': ASFunction(WD_trace_WD_trace), 'trace': ASFunction(WD_trace_trace), 'specific_trace': ASFunction(WD_trace_specific_trace)}, {}, {})
