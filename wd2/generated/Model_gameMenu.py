# Generated from __Packages/Model_gameMenu.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Model_gameMenu_Model_gameMenu(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Model_gameMenu')
    assign(ref(this, 'visible_leader_list_arr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'selected_leader_arr'), '=', lambda: rt.construct(e.get('Array'), []))
    return U

def Model_gameMenu_color_code_by_id(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_num'], ['a_num', 'i'], closure, 'Model_gameMenu')
    for key_1 in keys(ref(this, 'color_num_to_code_arr').get()):
        e.ref('i').set(key_1)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'color_num_to_code_arr').get(), e.get('i')).get(), 0).get(), e.get('a_num'))):
                return ref(ref(ref(this, 'color_num_to_code_arr').get(), e.get('i')).get(), 2).get()
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Model_gameMenu_color_hex_by_id(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_num'], ['a_num', 'i'], closure, 'Model_gameMenu')
    for key_2 in keys(ref(this, 'color_num_to_code_arr').get()):
        e.ref('i').set(key_2)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'color_num_to_code_arr').get(), e.get('i')).get(), 0).get(), e.get('a_num'))):
                return ref(ref(ref(this, 'color_num_to_code_arr').get(), e.get('i')).get(), 3).get()
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Model_gameMenu_color_hexStr_by_id(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_num'], ['a_num', 'i'], closure, 'Model_gameMenu')
    for key_3 in keys(ref(this, 'color_num_to_code_arr').get()):
        e.ref('i').set(key_3)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'color_num_to_code_arr').get(), e.get('i')).get(), 0).get(), e.get('a_num'))):
                return ref(ref(ref(this, 'color_num_to_code_arr').get(), e.get('i')).get(), 4).get()
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Model_gameMenu_color_name_by_id(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_num'], ['a_num', 'i'], closure, 'Model_gameMenu')
    for key_4 in keys(ref(this, 'color_num_to_code_arr').get()):
        e.ref('i').set(key_4)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'color_num_to_code_arr').get(), e.get('i')).get(), 0).get(), e.get('a_num'))):
                return ref(ref(ref(this, 'color_num_to_code_arr').get(), e.get('i')).get(), 1).get()
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Model_gameMenu_get_leader_by_ID(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_ID'], ['a_ID', 'i'], closure, 'Model_gameMenu')
    for key_5 in keys(ref(this, 'leader_arr').get()):
        e.ref('i').set(key_5)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'leader_arr').get(), e.get('i')).get(), 'ID').get(), e.get('a_ID'))):
                return ref(ref(this, 'leader_arr').get(), e.get('i')).get()
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Model_gameMenu_building_num_to_religion_code(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['_loc3_', 'a_nr'], closure, 'Model_gameMenu')
    e.set('_loc3_', 'chr')
    switch_6 = e.get('a_nr')
    case_7 = -1
    if case_7 == -1 and strict_eq(switch_6, 1):
        case_7 = 0
    if case_7 == -1 and strict_eq(switch_6, 2):
        case_7 = 1
    if case_7 == -1 and strict_eq(switch_6, 3):
        case_7 = 2
    if case_7 == -1 and strict_eq(switch_6, 4):
        case_7 = 3
    if case_7 == -1 and strict_eq(switch_6, 5):
        case_7 = 4
    if case_7 == -1:
        case_7 = 5
    try:
        if 0 <= case_7 <= 0:
            return 'bhu'
        if 0 <= case_7 <= 1:
            return 'chr'
        if 0 <= case_7 <= 2:
            return 'com'
        if 0 <= case_7 <= 3:
            return 'jew'
        if 0 <= case_7 <= 4:
            return 'mus'
        if 0 <= case_7 <= 5:
            return e.get('_loc3_')
    except ASBreak:
        pass
    return U

def Model_gameMenu_get_religion_buildingSet_by_code(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['_loc3_', 'a_nr'], closure, 'Model_gameMenu')
    e.set('_loc3_', 'christian_buildings')
    switch_8 = e.get('a_nr')
    case_9 = -1
    if case_9 == -1 and strict_eq(switch_8, 'bhu'):
        case_9 = 0
    if case_9 == -1 and strict_eq(switch_8, 'chr'):
        case_9 = 1
    if case_9 == -1 and strict_eq(switch_8, 'com'):
        case_9 = 2
    if case_9 == -1 and strict_eq(switch_8, 'jew'):
        case_9 = 3
    if case_9 == -1 and strict_eq(switch_8, 'mus'):
        case_9 = 4
    if case_9 == -1:
        case_9 = 5
    try:
        if 0 <= case_9 <= 0:
            return 'budhist_buildings'
        if 0 <= case_9 <= 1:
            return 'christian_buildings'
        if 0 <= case_9 <= 2:
            return 'communist_buildings'
        if 0 <= case_9 <= 3:
            return 'jewish_buildings'
        if 0 <= case_9 <= 4:
            return 'muslim_buildings'
        if 0 <= case_9 <= 5:
            return e.get('_loc3_')
    except ASBreak:
        pass
    return U

def Model_gameMenu_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Model_gameMenu')
    ref(this, 'leader_list_start_num').set(0)
    ref(this, 'color_num_to_code_arr').set(rt.construct(e.get('Array'), [arr([0, 'blue', 'blu', 255, '0x0000FF']), arr([1, 'red', 'red', 16711680, '0xFF0000']), arr([2, 'orange', 'ora', 16750848, '0xFF9900']), arr([3, 'yellow', 'yel', 1044480, '0xFF000']), arr([4, 'green', 'gre', 65280, '0x00FF00'])]))
    ref(this, 'leader_arr').set(rt.construct(e.get('Array'), [obj({'ID': 0, '_name': 'The Bombki', '_religion': 'chr', '_frame': 1, '_selected': False}), obj({'ID': 1, '_name': 'M. Headinajar', '_religion': 'mus', '_frame': 2, '_selected': False}), obj({'ID': 2, '_name': 'Col. Gedoffi', '_religion': 'mus', '_frame': 3, '_selected': False}), obj({'ID': 3, '_name': 'Reh Moose Hunt', '_religion': 'bhu', '_frame': 4, '_selected': False}), obj({'ID': 4, '_name': 'Asama Bin Loader', '_religion': 'mus', '_frame': 5, '_selected': False}), obj({'ID': 5, '_name': 'Any Kissonme', '_religion': 'bhu', '_frame': 6, '_selected': False}), obj({'ID': 6, '_name': "Psyman Para's", '_religion': 'jew', '_frame': 7, '_selected': False}), obj({'ID': 7, '_name': 'Ehum Oldbert', '_religion': 'jew', '_frame': 8, '_selected': False}), obj({'ID': 8, '_name': 'Ehum Bareass', '_religion': 'jew', '_frame': 9, '_selected': False}), obj({'ID': 9, '_name': 'Gladinme Putit', '_religion': 'com', '_frame': 10, '_selected': False}), obj({'ID': 10, '_name': 'Keen to Chill', '_religion': 'com', '_frame': 11, '_selected': False}), obj({'ID': 11, '_name': 'Angola Market', '_religion': 'chr', '_frame': 12, '_selected': False}), obj({'ID': 12, '_name': 'Ballony Stare', '_religion': 'chr', '_frame': 13, '_selected': False}), obj({'ID': 13, '_name': 'Who in There', '_religion': 'bhu', '_frame': 14, '_selected': False}), obj({'ID': 14, '_name': 'JP Barksender', '_religion': 'chr', '_frame': 15, '_selected': False}), obj({'ID': 15, '_name': 'Jack Searock', '_religion': 'chr', '_frame': 16, '_selected': False}), obj({'ID': 16, '_name': 'GW Blush', '_religion': 'chr', '_frame': 17, '_selected': False}), obj({'ID': 17, '_name': 'Taxi Isinawater', '_religion': 'bhu', '_frame': 18, '_selected': False}), obj({'ID': 18, '_name': 'Bossi Isasad', '_religion': 'mus', '_frame': 19, '_selected': False})]))

def register(rt):
    rt.define('Model_gameMenu', None, Model_gameMenu_fields, {'Model_gameMenu': ASFunction(Model_gameMenu_Model_gameMenu), 'color_code_by_id': ASFunction(Model_gameMenu_color_code_by_id), 'color_hex_by_id': ASFunction(Model_gameMenu_color_hex_by_id), 'color_hexStr_by_id': ASFunction(Model_gameMenu_color_hexStr_by_id), 'color_name_by_id': ASFunction(Model_gameMenu_color_name_by_id), 'get_leader_by_ID': ASFunction(Model_gameMenu_get_leader_by_ID), 'building_num_to_religion_code': ASFunction(Model_gameMenu_building_num_to_religion_code), 'get_religion_buildingSet_by_code': ASFunction(Model_gameMenu_get_religion_buildingSet_by_code)}, {}, {})
