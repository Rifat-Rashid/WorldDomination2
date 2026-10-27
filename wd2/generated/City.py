# Generated from __Packages/City.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def City_City(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_num', 'param_population', 'param_plr'], ['param_num', 'param_plr', 'param_population'], closure, 'City')
    assign(ref(this, 'num'), '=', lambda: e.get('param_num'))
    assign(ref(this, 'cityID'), '=', lambda: e.get('param_num'))
    assign(ref(this, 'prevPopulation'), '=', lambda: e.get('param_population'))
    assign(ref(this, 'population'), '=', lambda: e.get('param_population'))
    assign(ref(this, 'plr'), '=', lambda: e.get('param_plr'))
    assign(ref(this, 'selectionObj'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(this, 'selectionObj').get(), 'mcArray'), '=', lambda: arr([]))
    assign(ref(ref(this, 'selectionObj').get(), 'attack'), '=', lambda: False)
    assign(ref(ref(this, 'selectionObj').get(), 'attackMC'), '=', lambda: e.get('undefined'))
    assign(ref(ref(this, 'selectionObj').get(), 'preAttack'), '=', lambda: False)
    assign(ref(ref(this, 'selectionObj').get(), 'preAttackMC'), '=', lambda: e.get('undefined'))
    assign(ref(ref(this, 'selectionObj').get(), 'preAttackWeapon'), '=', lambda: e.get('undefined'))
    assign(ref(ref(this, 'selectionObj').get(), 'propaganda'), '=', lambda: False)
    assign(ref(ref(this, 'selectionObj').get(), 'propagandaMC'), '=', lambda: e.get('undefined'))
    assign(ref(ref(this, 'selectionObj').get(), 'ship'), '=', lambda: False)
    assign(ref(ref(this, 'selectionObj').get(), 'shipCount'), '=', lambda: 0)
    assign(ref(ref(this, 'selectionObj').get(), 'shipMC_arr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'total_battle_casualties'), '=', lambda: 0)
    assign(ref(this, 'propagandaMin'), '=', lambda: arr([]))
    assign(ref(this, 'propagandaMinIndex'), '=', lambda: 0)
    assign(ref(this, 'propagandaPlus'), '=', lambda: 0)
    assign(ref(this, 'hideForSelection'), '=', lambda: False)
    assign(ref(this, 'showForSelection'), '=', lambda: False)
    assign(ref(this, 'bioloaded'), '=', lambda: False)
    assign(ref(this, 'bioload_in_battle'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'bioCloud_container'), '=', lambda: e.get('undefined'))
    assign(ref(this, 'bioCloud_arr'), '=', lambda: arr([]))
    assign(ref(this, 'battle_loop_casualties'), '=', lambda: 0)
    assign(ref(this, 'propaganda_exclude'), '=', lambda: False)
    return U

def City_selectForShipAttack(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'City')
    update(ref(ref(this, 'selectionObj').get(), 'shipCount'), 1, False)
    assign(ref(ref(this, 'selectionObj').get(), 'ship'), '=', lambda: True)
    return U

def City_deselectForShipAttack(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'City')
    rt.call_ref(ref(ref(ref(ref(this, 'selectionObj').get(), 'shipMC_arr').get(), 0).get(), 'removeMovieClip'), [])
    rt.call_ref(ref(ref(ref(this, 'selectionObj').get(), 'shipMC_arr').get(), 'splice'), [0, 1])
    update(ref(ref(this, 'selectionObj').get(), 'shipCount'), -1, False)
    if truth(binop('<=', ref(ref(this, 'selectionObj').get(), 'shipCount').get(), 0)):
        rt.call_ref(ref(this, 'removeSelection'), ['ship'])
    return U

def City_setMapVars(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_mapMC', 'param_depth', 'param_xPos', 'param_yPos'], ['_loc6_', '_loc7_', 'param_depth', 'param_mapMC', 'param_xPos', 'param_yPos'], closure, 'City')
    assign(ref(this, 'mapMC'), '=', lambda: e.get('param_mapMC'))
    assign(ref(this, 'yPos'), '=', lambda: e.get('param_yPos'))
    assign(ref(this, 'xPos'), '=', lambda: e.get('param_xPos'))
    assign(ref(this, 'image_depth'), '=', lambda: binop('+', binop('*', rt.call_ref(ref(e.get('Math'), 'floor'), [binop('/', binop('+', ref(this, 'yPos').get(), 15), 10)]), 500), binop('+', 4, ref(this, 'cityID').get())))
    e.set('_loc6_', False)
    e.set('_loc7_', 0)
    while truth(unary('!', e.get('_loc6_'))):
        rt.tick()
        try:
            if truth(rt.call_ref(ref(this, 'checkDepth'), [ref(this, 'image_depth').get()])):
                assign(e.ref('_loc6_'), '=', lambda: True)
            else:
                assign(ref(this, 'image_depth'), '=', lambda: binop('-', ref(this, 'image_depth').get(), 1))
            assign(e.ref('_loc7_'), '=', lambda: binop('+', e.get('_loc7_'), 1))
            if truth(binop('>', e.get('_loc7_'), 90)):
                assign(e.ref('_loc6_'), '=', lambda: True)
        except ASContinue:
            pass
        except ASBreak:
            break
    rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'cityDepthArr').get(), 'push'), [ref(this, 'image_depth').get()])
    return U

def City_checkDepth(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_nr'], ['_loc3_', '_nr', 'i'], closure, 'City')
    e.set('_loc3_', True)
    for key_1 in keys(ref(ref(e.get('_global'), 'model').get(), 'cityDepthArr').get()):
        e.ref('i').set(key_1)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(e.get('_global'), 'model').get(), 'cityDepthArr').get(), e.get('i')).get(), e.get('_nr'))):
                return False
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc3_')
    return U

def City___set__theme(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'City')
    assign(ref(this, 'citySet'), '=', lambda: e.get('_param'))
    return U

def City___get___isSelected(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'City')
    e.set('_loc2_', False)
    assign(ref(this, 'selectionCount'), '=', lambda: 0)
    if truth(ref(ref(this, 'selectionObj').get(), 'attack').get()):
        assign(e.ref('_loc2_'), '=', lambda: True)
        assign(ref(this, 'selectionCount'), '=', lambda: binop('+', ref(this, 'selectionCount').get(), 1))
    if truth(ref(ref(this, 'selectionObj').get(), 'preAttack').get()):
        assign(e.ref('_loc2_'), '=', lambda: True)
        assign(ref(this, 'selectionCount'), '=', lambda: binop('+', ref(this, 'selectionCount').get(), 1))
    if truth(ref(ref(this, 'selectionObj').get(), 'propaganda').get()):
        assign(e.ref('_loc2_'), '=', lambda: True)
        assign(ref(this, 'selectionCount'), '=', lambda: binop('+', ref(this, 'selectionCount').get(), 1))
    if truth(ref(ref(this, 'selectionObj').get(), 'ship').get()):
        assign(e.ref('_loc2_'), '=', lambda: True)
        assign(ref(this, 'selectionCount'), '+=', lambda: ref(ref(this, 'selectionObj').get(), 'shipCount').get())
    return e.get('_loc2_')
    return U

def City_removeSelection(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_action'], ['_action'], closure, 'City')
    switch_2 = e.get('_action')
    case_3 = -1
    if case_3 == -1 and strict_eq(switch_2, 'preAttack'):
        case_3 = 0
    if case_3 == -1 and strict_eq(switch_2, 'attack'):
        case_3 = 1
    if case_3 == -1 and strict_eq(switch_2, 'propaganda'):
        case_3 = 2
    if case_3 == -1 and strict_eq(switch_2, 'ship'):
        case_3 = 3
    if case_3 == -1 and strict_eq(switch_2, 'all'):
        case_3 = 4
    if case_3 == -1:
        case_3 = -1
    try:
        if 0 <= case_3 <= 0:
            assign(ref(ref(this, 'selectionObj').get(), 'preAttack'), '=', lambda: False)
            assign(ref(ref(this, 'selectionObj').get(), 'preAttackWeapon'), '=', lambda: e.get('undefined'))
            assign(ref(this, 'selectionCount'), '=', lambda: binop('-', ref(this, 'selectionCount').get(), 1))
            rt.call_ref(ref(ref(ref(this, 'selectionObj').get(), 'preAttackMC').get(), 'removeMovieClip'), [])
            raise ASBreak()
        if 0 <= case_3 <= 1:
            assign(ref(ref(this, 'selectionObj').get(), 'attack'), '=', lambda: False)
            assign(ref(this, 'selectionCount'), '=', lambda: binop('-', ref(this, 'selectionCount').get(), 1))
            rt.call_ref(ref(ref(ref(this, 'selectionObj').get(), 'attackMC').get(), 'removeMovieClip'), [])
            raise ASBreak()
        if 0 <= case_3 <= 2:
            assign(ref(ref(this, 'selectionObj').get(), 'propaganda'), '=', lambda: False)
            assign(ref(this, 'selectionCount'), '=', lambda: binop('-', ref(this, 'selectionCount').get(), 1))
            rt.call_ref(ref(ref(ref(this, 'selectionObj').get(), 'propagandaMC').get(), 'removeMovieClip'), [])
            raise ASBreak()
        if 0 <= case_3 <= 3:
            assign(ref(ref(this, 'selectionObj').get(), 'ship'), '=', lambda: False)
            assign(ref(ref(this, 'selectionObj').get(), 'shipMC_arr'), '=', lambda: arr([]))
            assign(ref(ref(this, 'selectionObj').get(), 'shipCount'), '=', lambda: 0)
            raise ASBreak()
        if 0 <= case_3 <= 4:
            rt.call_ref(ref(ref(this, 'selectionMC').get(), 'removeMovieClip'), [])
            assign(ref(this, 'selectionCount'), '=', lambda: 0)
            assign(ref(ref(this, 'selectionObj').get(), 'attack'), '=', lambda: False)
            rt.call_ref(ref(ref(ref(this, 'selectionObj').get(), 'attackMC').get(), 'removeMovieClip'), [])
            assign(ref(ref(this, 'selectionObj').get(), 'preAttack'), '=', lambda: False)
            rt.call_ref(ref(ref(ref(this, 'selectionObj').get(), 'preAttackMC').get(), 'removeMovieClip'), [])
            assign(ref(ref(this, 'selectionObj').get(), 'propaganda'), '=', lambda: False)
            rt.call_ref(ref(ref(ref(this, 'selectionObj').get(), 'propagandaMC').get(), 'removeMovieClip'), [])
            assign(ref(ref(this, 'selectionObj').get(), 'ship'), '=', lambda: False)
            assign(ref(ref(this, 'selectionObj').get(), 'shipMC_arr'), '=', lambda: arr([]))
            assign(ref(ref(this, 'selectionObj').get(), 'shipCount'), '=', lambda: 0)
    except ASBreak:
        pass
    if truth(unary('!', ref(this, '_isSelected').get())):
        assign(ref(this, '_selected'), '=', lambda: False)
        rt.call_ref(ref(ref(this, 'selectionMC').get(), 'removeMovieClip'), [])
        assign(ref(this, 'selectionMC'), '=', lambda: e.get('undefined'))
    return U

def City_alignSelectionMC(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', 'i'], closure, 'City')
    assign(ref(ref(this, 'selectionMC').get(), '_x'), '=', lambda: ref(this, 'xPos').get())
    assign(ref(ref(this, 'selectionMC').get(), '_y'), '=', lambda: binop('-', ref(this, 'yPos').get(), 25))
    e.set('_loc2_', 0)
    for key_4 in keys(ref(ref(this, 'selectionObj').get(), 'mcArray').get()):
        e.ref('i').set(key_4)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '+=', lambda: ref(ref(ref(ref(this, 'selectionObj').get(), 'mcArray').get(), e.get('i')).get(), '_width').get())
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc3_', 0)
    while truth(binop('<', e.get('_loc3_'), ref(ref(ref(this, 'selectionObj').get(), 'mcArray').get(), 'length').get())):
        rt.tick()
        try:
            if truth(binop('==', e.get('_loc3_'), 0)):
                assign(ref(ref(ref(ref(this, 'selectionObj').get(), 'mcArray').get(), e.get('_loc3_')).get(), '_x'), '=', lambda: binop('/', unary('-', e.get('_loc2_')), 2))
            else:
                assign(ref(ref(ref(ref(this, 'selectionObj').get(), 'mcArray').get(), e.get('_loc3_')).get(), '_x'), '=', lambda: binop('+', ref(ref(ref(ref(this, 'selectionObj').get(), 'mcArray').get(), binop('-', e.get('_loc3_'), 1)).get(), '_x').get(), ref(ref(ref(ref(this, 'selectionObj').get(), 'mcArray').get(), binop('-', e.get('_loc3_'), 1)).get(), '_width').get()))
            assign(ref(ref(ref(ref(this, 'selectionObj').get(), 'mcArray').get(), e.get('_loc3_')).get(), '_y'), '=', lambda: 25)
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def City_updateIMG(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'City')
    rt.call_ref(ref(ref(this, 'image').get(), 'gotoAndStop'), [ref(this, 'size_and_frame').get()])
    return U

def City___get__size_and_frame(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_'], closure, 'City')
    e.set('_loc2_', rt.call_ref(ref(e.get('Math'), 'ceil'), [binop('*', binop('/', ref(this, 'population').get(), ref(this, 'frame_divider').get()), 6)]))
    assign(ref(ref(this, 'debugTextField').get(), 'text'), '=', lambda: binop('+', 'pop: ', ref(this, 'population').get()))
    if truth(logical('&&', ref(this, 'deathFrame').get(), lambda: binop('<=', ref(this, 'population').get(), 0))):
        return ref(this, 'deathFrame').get()
    if truth(logical('&&', binop('<=', ref(this, 'population').get(), 0), lambda: binop('!=', ref(this, '_prevFrame').get(), 99))):
        assign(ref(this, 'population'), '=', lambda: 0)
        assign(e.ref('_loc3_'), '=', lambda: binop('+', ref(this, '_prevFrame').get(), 9))
        assign(ref(this, '_prevFrame'), '=', lambda: 99)
        return e.get('_loc3_')
    if truth(binop('<', ref(this, 'population').get(), 0)):
        assign(ref(this, 'population'), '=', lambda: 0)
    if truth(binop('<=', e.get('_loc2_'), 6)):
        assign(ref(this, '_prevFrame'), '=', lambda: e.get('_loc2_'))
        return e.get('_loc2_')
    assign(ref(this, '_prevFrame'), '=', lambda: 6)
    return 6
    return U

def City_removeBioload(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'City')
    assign(ref(this, 'bioloaded'), '=', lambda: False)
    for key_5 in keys(ref(this, 'bioCloud_arr').get()):
        e.ref('i').set(key_5)
        rt.tick()
        try:
            rt.call_ref(ref(ref(ref(this, 'bioCloud_arr').get(), e.get('i')).get(), 'removeMovieClip'), [])
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(this, 'bioCloud_arr'), '=', lambda: arr([]))
    rt.call_ref(ref(ref(this, 'bioCloud_container').get(), 'removeMovieClip'), [])
    return U

def City_propagandaMin_func(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'City')
    rt.call_ref(ref(this, 'size_and_frame_in_battle'), [ref(ref(this, 'propagandaMin').get(), ref(this, 'propagandaMinIndex').get()).get(), True, 'propaganda'])
    assign(ref(this, 'propagandaMinIndex'), '=', lambda: binop('+', ref(this, 'propagandaMinIndex').get(), 1))
    return U

def City_propagandaPlus_func(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'City')
    assign(ref(this, 'curCasualties'), '-=', lambda: ref(this, 'propagandaPlus').get())
    rt.call_ref(ref(this, 'size_and_frame_in_battle'), [0, True])
    return U

def City_size_and_frame_in_battle(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['casualties', 'play_sequence', 'extra_string'], ['_loc5_', 'casualties', 'extra_string', 'play_sequence'], closure, 'City')
    if truth(logical('&&', ref(this, 'deathFrame').get(), lambda: binop('<=', ref(this, 'population').get(), 0))):
        return ref(this, 'deathFrame').get()
    assign(ref(this, 'curCasualties'), '+=', lambda: e.get('casualties'))
    e.set('_loc5_', rt.call_ref(ref(e.get('Math'), 'ceil'), [binop('*', binop('/', binop('-', ref(this, 'prevPopulation').get(), ref(this, 'curCasualties').get()), ref(this, 'frame_divider').get()), 6)]))
    if truth(binop('<=', binop('-', ref(this, 'prevPopulation').get(), ref(this, 'curCasualties').get()), 0)):
        if truth(unary('!', ref(this, '_prevFrame').get())):
            assign(ref(this, '_prevFrame'), '=', lambda: ref(ref(this, 'image').get(), '_currentframe').get())
        assign(ref(this, 'deathFrame'), '=', lambda: binop('+', ref(this, '_prevFrame').get(), 9))
        assign(ref(this, 'population'), '=', lambda: 0)
        rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'city_shrink_sequence'), [ref(this, 'image').get(), ref(this, 'deathFrame').get()])
        return ref(this, 'deathFrame').get()
    if truth(binop('<', ref(this, 'population').get(), 0)):
        assign(ref(this, 'population'), '=', lambda: 0)
    assign(ref(ref(this, 'debugTextField').get(), 'text'), '=', lambda: binop('+', 'pop: ', ref(this, 'population').get()))
    if truth(binop('<=', e.get('_loc5_'), 6)):
        if truth(logical('&&', binop('!=', e.get('_loc5_'), ref(this, '_prevFrame').get()), lambda: e.get('play_sequence'))):
            rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'city_shrink_sequence'), [ref(this, 'image').get(), e.get('_loc5_'), e.get('extra_string'), ref(this, 'propagandaMinIndex').get()])
        assign(ref(this, '_prevFrame'), '=', lambda: e.get('_loc5_'))
        return e.get('_loc5_')
    assign(ref(this, '_prevFrame'), '=', lambda: 6)
    return 6
    return U

def City___set__size_and_frame(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'City')
    return U

def City_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'City')
    ref(this, '_theme').set('string')
    ref(this, 'curCasualties').set(0)
    ref(this, 'prevPopulation').set(0)
    ref(this, 'selectionCount').set(0)
    ref(this, 'frame_divider').set(90)
    ref(this, 'carrierAttackCount').set(0)

def register(rt):
    rt.define('City', None, City_fields, {'City': ASFunction(City_City), 'selectForShipAttack': ASFunction(City_selectForShipAttack), 'deselectForShipAttack': ASFunction(City_deselectForShipAttack), 'setMapVars': ASFunction(City_setMapVars), 'checkDepth': ASFunction(City_checkDepth), 'removeSelection': ASFunction(City_removeSelection), 'alignSelectionMC': ASFunction(City_alignSelectionMC), 'updateIMG': ASFunction(City_updateIMG), 'removeBioload': ASFunction(City_removeBioload), 'propagandaMin_func': ASFunction(City_propagandaMin_func), 'propagandaPlus_func': ASFunction(City_propagandaPlus_func), 'size_and_frame_in_battle': ASFunction(City_size_and_frame_in_battle)}, {'_isSelected': ASFunction(City___get___isSelected), 'size_and_frame': ASFunction(City___get__size_and_frame)}, {'theme': ASFunction(City___set__theme), 'size_and_frame': ASFunction(City___set__size_and_frame)})
