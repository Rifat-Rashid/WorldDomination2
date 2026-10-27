# Generated from __Packages/View_gameMenu.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def View_gameMenu_View_gameMenu(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_src_MC'], ['a_src_MC'], closure, 'View_gameMenu')
    assign(ref(this, 'src_MC'), '=', lambda: e.get('a_src_MC'))
    assign(ref(ref(ref(ref(this, 'src_MC').get(), 'txtMC1').get(), 'txt').get(), 'text'), '=', lambda: 'EASY')
    rt.call_ref(ref(ref(ref(ref(this, 'src_MC').get(), 'txtMC1').get(), 'txt').get(), 'setTextFormat'), [ref(ref(ref(e.get('_global'), 'view').get(), 'textFormats').get(), 'interface_actionText_1').get()])
    assign(ref(ref(ref(ref(this, 'src_MC').get(), 'txtMC1').get(), 'txt').get(), 'embedFonts'), '=', lambda: True)
    assign(ref(ref(ref(ref(this, 'src_MC').get(), 'txtMC2').get(), 'txt').get(), 'text'), '=', lambda: 'MEDIUM')
    rt.call_ref(ref(ref(ref(ref(this, 'src_MC').get(), 'txtMC2').get(), 'txt').get(), 'setTextFormat'), [ref(ref(ref(e.get('_global'), 'view').get(), 'textFormats').get(), 'interface_actionText_1').get()])
    assign(ref(ref(ref(ref(this, 'src_MC').get(), 'txtMC2').get(), 'txt').get(), 'embedFonts'), '=', lambda: True)
    assign(ref(ref(ref(ref(this, 'src_MC').get(), 'txtMC3').get(), 'txt').get(), 'text'), '=', lambda: 'HARD')
    rt.call_ref(ref(ref(ref(ref(this, 'src_MC').get(), 'txtMC3').get(), 'txt').get(), 'setTextFormat'), [ref(ref(ref(e.get('_global'), 'view').get(), 'textFormats').get(), 'interface_actionText_1').get()])
    assign(ref(ref(ref(ref(this, 'src_MC').get(), 'txtMC3').get(), 'txt').get(), 'embedFonts'), '=', lambda: True)
    assign(ref(ref(ref(ref(this, 'src_MC').get(), 'txtMC_start').get(), 'txt').get(), 'text'), '=', lambda: 'START GAME')
    rt.call_ref(ref(ref(ref(ref(this, 'src_MC').get(), 'txtMC_start').get(), 'txt').get(), 'setTextFormat'), [ref(ref(ref(e.get('_global'), 'view').get(), 'textFormats').get(), 'interface_actionText_1').get()])
    assign(ref(ref(ref(ref(this, 'src_MC').get(), 'txtMC_start').get(), 'txt').get(), 'embedFonts'), '=', lambda: True)
    return U

def View_gameMenu___set__active_difficulty_btn(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['a_nr'], closure, 'View_gameMenu')
    rt.call_ref(ref(ref(ref(this, 'src_MC').get(), 'scrn1').get(), 'gotoAndStop'), [1])
    rt.call_ref(ref(ref(ref(this, 'src_MC').get(), 'scrn2').get(), 'gotoAndStop'), [1])
    rt.call_ref(ref(ref(ref(this, 'src_MC').get(), 'scrn3').get(), 'gotoAndStop'), [1])
    rt.call_ref(ref(ref(ref(this, 'src_MC').get(), binop('+', 'scrn', e.get('a_nr'))).get(), 'gotoAndStop'), [2])
    return e.get('undefined')
    return U

def View_gameMenu___set__active_player_color_btn(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['_loc3_', 'a_nr'], closure, 'View_gameMenu')
    e.set('_loc3_', 1)
    while truth(binop('<', e.get('_loc3_'), 6)):
        rt.tick()
        try:
            rt.call_ref(ref(ref(ref(this, 'src_MC').get(), binop('+', 'colorIndicator', e.get('_loc3_'))).get(), 'gotoAndStop'), [1])
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    rt.call_ref(ref(ref(ref(this, 'src_MC').get(), binop('+', 'colorIndicator', e.get('a_nr'))).get(), 'gotoAndStop'), [e.get('a_nr')])
    return e.get('undefined')
    return U

def View_gameMenu___set__active_color_btn(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['_loc3_', 'a_nr'], closure, 'View_gameMenu')
    e.set('_loc3_', 1)
    while truth(binop('<', e.get('_loc3_'), 6)):
        rt.tick()
        try:
            rt.call_ref(ref(ref(ref(this, 'src_MC').get(), binop('+', 'colorIndicator', e.get('_loc3_'))).get(), 'gotoAndStop'), [1])
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    rt.call_ref(ref(ref(ref(this, 'src_MC').get(), binop('+', 'colorIndicator', e.get('a_nr'))).get(), 'gotoAndStop'), [2])
    return e.get('undefined')
    return U

def View_gameMenu___set__active_building_btn(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_nr'], ['_loc3_', 'a_nr'], closure, 'View_gameMenu')
    e.set('_loc3_', 1)
    while truth(binop('<', e.get('_loc3_'), 6)):
        rt.tick()
        try:
            rt.call_ref(ref(ref(ref(this, 'src_MC').get(), binop('+', 'buildingIndicator', e.get('_loc3_'))).get(), 'gotoAndStop'), [1])
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    rt.call_ref(ref(ref(ref(this, 'src_MC').get(), binop('+', 'buildingIndicator', e.get('a_nr'))).get(), 'gotoAndStop'), [2])
    if truth(ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get()):
        assign(ref(ref(ref(this, 'src_MC').get(), 'buildingIndicator3').get(), '_alpha'), '=', lambda: 40)
        assign(ref(ref(ref(this, 'src_MC').get(), 'buildingIndicator4').get(), '_alpha'), '=', lambda: 40)
        assign(ref(ref(ref(this, 'src_MC').get(), 'buildingIndicator5').get(), '_alpha'), '=', lambda: 40)
        rt.call_ref(ref(ref(ref(this, 'src_MC').get(), 'full_version_building_mc').get(), 'gotoAndStop'), [2])
    return e.get('undefined')
    return U

def View_gameMenu_update_leader_screen(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_MC', 'a_nr'], ['a_MC', 'a_nr'], closure, 'View_gameMenu')
    rt.call_ref(ref(e.get('a_MC'), 'gotoAndStop'), [e.get('a_nr')])
    return U

def View_gameMenu_hide_gameMenu(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View_gameMenu')
    assign(ref(ref(this, 'src_MC').get(), '_visible'), '=', lambda: False)
    return U

def View_gameMenu_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View_gameMenu')
    pass

def register(rt):
    rt.define('View_gameMenu', None, View_gameMenu_fields, {'View_gameMenu': ASFunction(View_gameMenu_View_gameMenu), 'update_leader_screen': ASFunction(View_gameMenu_update_leader_screen), 'hide_gameMenu': ASFunction(View_gameMenu_hide_gameMenu)}, {}, {'active_difficulty_btn': ASFunction(View_gameMenu___set__active_difficulty_btn), 'active_player_color_btn': ASFunction(View_gameMenu___set__active_player_color_btn), 'active_color_btn': ASFunction(View_gameMenu___set__active_color_btn), 'active_building_btn': ASFunction(View_gameMenu___set__active_building_btn)})
