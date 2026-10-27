# Generated from __Packages/Main.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def f_1(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str'], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'play_sound_by_action'), [e.get('_str')])
    return U

def f_2(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str'], closure, None)
    if truth(ref(ref(ref(e.get('_global'), 'model').get(), 'option').get(), 'playSound').get()):
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'play_sound_by_building'), [e.get('_str')])
    return U

def f_3(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str', '_pan'], ['_pan', '_str'], closure, None)
    if truth(ref(ref(ref(e.get('_global'), 'model').get(), 'option').get(), 'playSound').get()):
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'play_sound_by_event'), [e.get('_str'), e.get('_pan')])
    return U

def f_4(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str', '_pan'], ['_pan', '_str'], closure, None)
    if truth(ref(ref(ref(e.get('_global'), 'model').get(), 'option').get(), 'playSound').get()):
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'explosion_sound_by_mc_name'), [e.get('_str'), e.get('_pan')])
    return U

def f_5(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    update(ref(ref(e.get('_root'), 'battleMC').get(), '_visible'), -1, False)
    update(ref(ref(e.get('_root'), 'sidePanels').get(), '_visible'), -1, False)
    update(ref(ref(e.get('_root'), 'interfaceMC').get(), '_visible'), -1, False)
    return U

def f_6(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, None)
    e.set('_loc2_', 0)
    while truth(binop('<', e.get('_loc2_'), 1)):
        rt.tick()
        try:
            rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'doTurn'), [])
            rt.call_ref(ref(ref(e.get('_global'), 'main').get(), 'updateStageTxt'), [])
            rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'initBattle'), [])
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def f_7(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, None)
    e.set('_loc2_', 0)
    while truth(binop('<', e.get('_loc2_'), 25)):
        rt.tick()
        try:
            rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'doTurn'), [])
            rt.call_ref(ref(ref(e.get('_global'), 'main').get(), 'updateStageTxt'), [])
            rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'initBattle'), [])
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def f_8(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(e.get('_level0'), 'splashScreenMC').get(), '_visible'), '=', lambda: False)
    assign(ref(ref(e.get('_level0'), 'gameMenu').get(), '_visible'), '=', lambda: True)
    return U

def f_9(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_level0'), 'introMovie').get(), 'gotoAndStop'), [2])
    assign(ref(ref(e.get('_level0'), 'introMovie').get(), '_visible'), '=', lambda: False)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'init_theme_snd'), [])
    return U

def Main_Main(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Main')
    e.call('fscommand', ['allowscale', False])
    e.call('fscommand', ['showmenu', False])
    assign(ref(e.get('_global'), '_quality'), '=', lambda: 'BEST')
    assign(ref(e.get('_global'), 'WDTrace'), '=', lambda: rt.construct(e.get('WD_trace'), []))
    assign(ref(e.get('_global'), 'debug'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(this, 'FORCE_COMPILTION'), '=', lambda: rt.construct(e.get('SpaceRocket_smoke'), []))
    assign(ref(this, 'FORCE_COMPILTION'), '=', lambda: rt.construct(e.get('SpaceRocket_trail_element'), []))
    assign(ref(e.get('_global'), 'model'), '=', lambda: rt.construct(e.get('Model'), []))
    assign(ref(this, 'model'), '=', lambda: ref(e.get('_global'), 'model').get())
    assign(ref(ref(this, 'model').get(), 'turnActions'), '=', lambda: 0)
    assign(ref(ref(this, 'model').get(), 'turn'), '=', lambda: 0)
    assign(ref(ref(this, 'model').get(), 'maxFunds'), '=', lambda: 100)
    assign(ref(ref(this, 'model').get(), 'decisionPoints'), '=', lambda: rt.construct(e.get('DecisionPoints'), []))
    assign(ref(e.get('_global'), 'presenter'), '=', lambda: rt.construct(e.get('Presenter'), [ref(this, 'model').get()]))
    assign(ref(this, 'presenter'), '=', lambda: ref(e.get('_global'), 'presenter').get())
    assign(ref(e.get('_global'), 'view'), '=', lambda: rt.construct(e.get('View'), [ref(this, 'model').get(), ref(this, 'presenter').get(), ref(e.get('_root'), 'interfaceMC').get(), ref(e.get('_root'), 'battleMC').get()]))
    assign(ref(this, 'view'), '=', lambda: ref(e.get('_global'), 'view').get())
    assign(ref(ref(this, 'presenter').get(), 'view'), '=', lambda: ref(this, 'view').get())
    assign(ref(e.get('_global'), 'model_interface'), '=', lambda: assign(ref(this, 'model_interface'), '=', lambda: rt.construct(e.get('Model_interface'), [])))
    assign(ref(e.get('_global'), 'presenter_interface'), '=', lambda: assign(ref(this, 'presenter_interface'), '=', lambda: rt.construct(e.get('Presenter_interface'), [])))
    assign(ref(e.get('_global'), 'view_interface'), '=', lambda: assign(ref(this, 'view_interface'), '=', lambda: rt.construct(e.get('View_interface'), [ref(e.get('_level0'), 'interfaceMC').get()])))
    assign(ref(e.get('_global'), 'presenter_gameMenu'), '=', lambda: assign(ref(this, 'presenter_gameMenu'), '=', lambda: rt.construct(e.get('Presenter_gameMenu'), [])))
    assign(ref(e.get('_global'), 'view_gameMenu'), '=', lambda: assign(ref(this, 'view_gameMenu'), '=', lambda: rt.construct(e.get('View_gameMenu'), [ref(e.get('_root'), 'gameMenu').get()])))
    assign(ref(e.get('_global'), 'model_gameMenu'), '=', lambda: assign(ref(this, 'model_gameMenu'), '=', lambda: rt.construct(e.get('Model_gameMenu'), [])))
    assign(ref(ref(this, 'model_gameMenu').get(), 'presenter'), '=', lambda: ref(this, 'presenter_gameMenu').get())
    assign(ref(ref(this, 'presenter_gameMenu').get(), 'view'), '=', lambda: ref(this, 'view_gameMenu').get())
    assign(ref(ref(this, 'presenter_gameMenu').get(), 'model'), '=', lambda: ref(this, 'model_gameMenu').get())
    rt.call_ref(ref(ref(this, 'presenter_gameMenu').get(), 'initialize_gameMenu'), [])
    assign(ref(e.get('_global'), 'play_sound_by_action'), '=', lambda: ASFunction(f_1, e))
    assign(ref(e.get('_global'), 'play_sound_by_building'), '=', lambda: ASFunction(f_2, e))
    assign(ref(e.get('_global'), 'play_sound_by_event'), '=', lambda: ASFunction(f_3, e))
    assign(ref(e.get('_global'), 'explosion_sound_by_mc_name'), '=', lambda: ASFunction(f_4, e))
    assign(ref(ref(this, 'presenter_interface').get(), 'view_interface'), '=', lambda: ref(this, 'view_interface').get())
    assign(ref(ref(this, 'presenter_interface').get(), 'presenter'), '=', lambda: ref(this, 'presenter').get())
    assign(ref(ref(this, 'presenter_interface').get(), 'model'), '=', lambda: ref(e.get('_global'), 'model').get())
    assign(ref(ref(this, 'presenter_interface').get(), 'model_interface'), '=', lambda: ref(this, 'model_interface').get())
    assign(ref(ref(this, 'presenter_interface').get(), 'view'), '=', lambda: ref(this, 'view').get())
    assign(ref(ref(this, 'view_interface').get(), 'presenter_interface'), '=', lambda: ref(this, 'presenter_interface').get())
    assign(ref(ref(this, 'view_interface').get(), 'model_interface'), '=', lambda: ref(this, 'model_interface').get())
    assign(ref(ref(this, 'view').get(), 'view_interface'), '=', lambda: ref(this, 'view_interface').get())
    assign(ref(ref(this, 'view').get(), 'presenter_interface'), '=', lambda: ref(this, 'presenter_interface').get())
    assign(ref(ref(this, 'view').get(), 'clipSrc'), '=', lambda: rt.call_ref(ref(e.get('_root'), 'createEmptyMovieClip'), ['windowContainer', 9000]))
    assign(ref(ref(this, 'view').get(), '_graphMC'), '=', lambda: ref(e.get('_root'), 'graphMC').get())
    rt.call_ref(ref(ref(this, 'model').get(), 'set_city_position_to_array'), [])
    assign(ref(ref(e.get('_level0'), 'endGameMC').get(), '_visible'), '=', lambda: False)
    assign(ref(ref(e.get('_root'), 'debugBtn1').get(), 'onPress'), '=', lambda: ASFunction(f_5, e))
    assign(ref(ref(e.get('_root'), 'turnBtn').get(), 'onPress'), '=', lambda: ASFunction(f_6, e))
    assign(ref(ref(e.get('_root'), 'turnBtn2').get(), 'onPress'), '=', lambda: ASFunction(f_7, e))
    rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'cloudTicker_initiate'), [])
    rt.call_ref(ref(ref(this, 'model').get(), 'set_city_position_to_array'), [])
    assign(ref(ref(ref(ref(ref(this, 'model').get(), 'comp2').get(), 'cityArr').get(), 1).get(), 'population'), '=', lambda: 2)
    assign(ref(ref(e.get('_level0'), 'interfaceMC').get(), '_visible'), '=', lambda: False)
    assign(ref(ref(e.get('_level0'), 'gameMenu').get(), '_visible'), '=', lambda: False)
    assign(ref(ref(e.get('_level0'), 'splashScreenMC').get(), 'onPress'), '=', lambda: ASFunction(f_8, e))
    assign(ref(ref(e.get('_level0'), 'introMovie').get(), 'onPress'), '=', lambda: ASFunction(f_9, e))
    rt.call_ref(ref(e.get('_level0'), 'createEmptyMovieClip'), ['theme_sound_mc', rt.call_ref(ref(e.get('_level0'), 'getNextHighestDepth'), [])])
    assign(ref(ref(this, 'model').get(), 'theme_sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(e.get('_level0'), 'theme_sound_mc').get()]))
    rt.call_ref(ref(ref(ref(this, 'model').get(), 'theme_sound').get(), 'attachSound'), ['WDTheme.wav'])
    rt.call_ref(ref(ref(ref(this, 'model').get(), 'option').get(), 'setMusic'), [])
    e.call('fscommand', ['allowscale', 'false'])
    e.call('fscommand', ['showmenu', 'false'])
    return U

def Main_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Main')
    pass

def register(rt):
    rt.define('Main', None, Main_fields, {'Main': ASFunction(Main_Main)}, {}, {})
