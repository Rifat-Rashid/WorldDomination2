# Generated from __Packages/Help_data.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Help_data_Help_data(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Help_data')
    return U

def Help_data_get_data(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_current'], ['a_current', 'i'], closure, 'Help_data')
    for key_1 in keys(ref(this, 'page_arr').get()):
        e.ref('i').set(key_1)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'page_arr').get(), e.get('i')).get(), '_pgName').get(), e.get('a_current'))):
                return ref(ref(this, 'page_arr').get(), e.get('i')).get()
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Help_data_get_next(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_current'], ['_loc3_', 'a_current', 'i'], closure, 'Help_data')
    for key_2 in keys(ref(this, 'page_arr').get()):
        e.ref('i').set(key_2)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'page_arr').get(), e.get('i')).get(), '_pgName').get(), e.get('a_current'))):
                assign(e.ref('_loc3_'), '=', lambda: ref(ref(this, 'page_arr').get(), e.get('i')).get())
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_3 in keys(ref(this, 'page_arr').get()):
        e.ref('i').set(key_3)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'page_arr').get(), e.get('i')).get(), '_id').get(), binop('+', ref(e.get('_loc3_'), '_id').get(), 1))):
                return ref(ref(ref(this, 'page_arr').get(), e.get('i')).get(), '_pgName').get()
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Help_data_get_prev(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_current'], ['_loc3_', 'a_current', 'i'], closure, 'Help_data')
    for key_4 in keys(ref(this, 'page_arr').get()):
        e.ref('i').set(key_4)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'page_arr').get(), e.get('i')).get(), '_pgName').get(), e.get('a_current'))):
                assign(e.ref('_loc3_'), '=', lambda: ref(ref(this, 'page_arr').get(), e.get('i')).get())
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_5 in keys(ref(this, 'page_arr').get()):
        e.ref('i').set(key_5)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(this, 'page_arr').get(), e.get('i')).get(), '_id').get(), binop('-', ref(e.get('_loc3_'), '_id').get(), 1))):
                return ref(ref(ref(this, 'page_arr').get(), e.get('i')).get(), '_pgName').get()
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Help_data_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Help_data')
    ref(this, 'page_arr').set(rt.construct(e.get('Array'), [obj({'_id': 0, '_pgName': 'help_index', '_btnArr': arr([obj({'_mcName': 'btn_overview', '_trgtString': 'help_overview'}), obj({'_mcName': 'btn_interface', '_trgtString': 'help_interface'}), obj({'_mcName': 'btn_attacking', '_trgtString': 'help_attacking'}), obj({'_mcName': 'btn_weapondetails', '_trgtString': 'help_weapondetail'}), obj({'_mcName': 'btn_actiondetails', '_trgtString': 'help_actiondetails'})])}), obj({'_id': 1, '_pgName': 'help_weapondetail', '_indexBtn': True, '_btnArr': arr([obj({'_mcName': 'btn_rockets', '_trgtString': 'help_rockets'}), obj({'_mcName': 'btn_aircraft', '_trgtString': 'help_aircraft'}), obj({'_mcName': 'btn_specialcarriers', '_trgtString': 'help_subs'}), obj({'_mcName': 'btn_warheads', '_trgtString': 'help_warheads'}), obj({'_mcName': 'btn_infanterie', '_trgtString': 'help_infanterie'}), obj({'_mcName': 'btn_intelligence', '_trgtString': 'help_intelligence'}), obj({'_mcName': 'btn_antiweapons', '_trgtString': 'help_antiweapons'})])}), obj({'_id': 2, '_pgName': 'help_actiondetails', '_indexBtn': True, '_btnArr': arr([obj({'_mcName': 'btn_resources', '_trgtString': 'help_resources'}), obj({'_mcName': 'btn_production', '_trgtString': 'help_production'}), obj({'_mcName': 'btn_technology', '_trgtString': 'help_technology'}), obj({'_mcName': 'btn_massmedia', '_trgtString': 'help_massmedia'}), obj({'_mcName': 'btn_directattack', '_trgtString': 'help_directattack'}), obj({'_mcName': 'btn_preparedattack', '_trgtString': 'help_preattack'}), obj({'_mcName': 'btn_defense', '_trgtString': 'help_defense'}), obj({'_mcName': 'btn_propaganda', '_trgtString': 'help_propaganda'}), obj({'_mcName': 'btn_diplomacy', '_trgtString': 'help_diplomacy'})])}), obj({'_id': 3, '_pgName': 'help_overview', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 4, '_pgName': 'help_interface', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 5, '_pgName': 'help_interface2', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 6, '_pgName': 'help_interface3', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 7, '_pgName': 'help_interface4', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 8, '_pgName': 'help_attacking', '_btnNext': True, '_btnNext': True, '_btnIndex': True}), obj({'_id': 9, '_pgName': 'help_attacking2', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 10, '_pgName': 'help_attacking3', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 11, '_pgName': 'help_rockets', '_btnNext': True, '_btnNext': True, '_btnIndex': True}), obj({'_id': 12, '_pgName': 'help_aircraft', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 13, '_pgName': 'help_subs', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 14, '_pgName': 'help_carrier', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 15, '_pgName': 'help_space', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 16, '_pgName': 'help_warheads', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 17, '_pgName': 'help_infantrie', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 18, '_pgName': 'help_intelligence', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 19, '_pgName': 'help_resources', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 20, '_pgName': 'help_production', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 21, '_pgName': 'help_technology', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 22, '_pgName': 'help_massmedia', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 23, '_pgName': 'help_directattack', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 24, '_pgName': 'help_preattack', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 25, '_pgName': 'help_defense', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 26, '_pgName': 'help_propaganda', '_btnNext': True, '_btnPrev': True, '_btnIndex': True}), obj({'_id': 27, '_pgName': 'help_diplomacy', '_btnPrev': True, '_btnPrev': True, '_btnIndex': True})]))

def register(rt):
    rt.define('Help_data', None, Help_data_fields, {'Help_data': ASFunction(Help_data_Help_data), 'get_data': ASFunction(Help_data_get_data), 'get_next': ASFunction(Help_data_get_next), 'get_prev': ASFunction(Help_data_get_prev)}, {}, {})
