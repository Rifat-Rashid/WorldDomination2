# Generated from __Packages/View.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def View_View(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_model', 'param_presenter', 'param_srcMC', 'param_battleSrcMC'], ['_loc6_', 'param_battleSrcMC', 'param_model', 'param_presenter', 'param_srcMC'], closure, 'View')
    e.set('_loc6_', rt.construct(e.get('Cloud'), []))
    assign(ref(this, 'model'), '=', lambda: e.get('param_model'))
    rt.call_ref(ref(e.get('AsBroadcaster'), 'initialize'), [ref(ref(this, 'model').get(), '_broadcaster').get()])
    assign(ref(this, 'presenter'), '=', lambda: e.get('param_presenter'))
    rt.call_ref(ref(ref(ref(this, 'model').get(), '_broadcaster').get(), 'addListener'), [this])
    assign(ref(this, 'textFormats'), '=', lambda: rt.construct(e.get('TextFormats'), []))
    assign(ref(this, 'srcMC'), '=', lambda: e.get('param_srcMC'))
    assign(ref(ref(this, 'srcMC').get(), 'view'), '=', lambda: this)
    rt.call_ref(ref(ref(ref(this, 'srcMC').get(), 'bg').get(), 'swapDepths'), [ref(this, 'interfaceBGDepth').get()])
    rt.call_ref(ref(ref(ref(this, 'srcMC').get(), 'infoText').get(), 'swapDepths'), [ref(this, 'infoTextDepth').get()])
    rt.call_ref(ref(ref(ref(this, 'srcMC').get(), 'infoLine').get(), 'swapDepths'), [ref(this, 'scrollTextDepth').get()])
    rt.call_ref(ref(ref(ref(this, 'srcMC').get(), 'statsMC').get(), 'swapDepths'), [ref(this, 'statBarDepth').get()])
    rt.call_ref(ref(ref(ref(this, 'srcMC').get(), 'hatch46').get(), 'swapDepths'), [ref(this, 'exBtnSrcDepth').get()])
    rt.call_ref(ref(ref(ref(this, 'srcMC').get(), 'btn49').get(), 'swapDepths'), [ref(this, 'exBtnOvrDepth').get()])
    assign(ref(this, 'battleSrcMC'), '=', lambda: e.get('param_battleSrcMC'))
    assign(ref(this, 'fadeClipsTicker'), '=', lambda: rt.call_ref(ref(ref(this, 'srcMC').get(), 'createEmptyMovieClip'), ['fadeClipsTicker', ref(this, 'ticker2Depth').get()]))
    assign(ref(this, 'popupTicker'), '=', lambda: rt.call_ref(ref(ref(this, 'srcMC').get(), 'createEmptyMovieClip'), ['popupTicker', ref(this, 'ticker3Depth').get()]))
    assign(ref(this, 'typeEffectTicker'), '=', lambda: rt.call_ref(ref(ref(this, 'srcMC').get(), 'createEmptyMovieClip'), ['typeEffectTicker', ref(this, 'ticker4Depth').get()]))
    assign(ref(this, 'scrollTicker'), '=', lambda: rt.call_ref(ref(ref(this, 'srcMC').get(), 'createEmptyMovieClip'), ['scrollTicker', ref(this, 'ticker5Depth').get()]))
    assign(ref(this, 'hatchTicker'), '=', lambda: rt.call_ref(ref(ref(this, 'srcMC').get(), 'createEmptyMovieClip'), ['hatchticker', ref(this, 'ticker6Depth').get()]))
    rt.call_ref(ref(e.get('AsBroadcaster'), 'initialize'), [ref(this, 'btnBroadcaster').get()])
    assign(ref(this, 'actionTextMCArr'), '=', lambda: arr([e.get('undefined'), ref(ref(this, 'srcMC').get(), 'action_text_resources').get(), ref(ref(this, 'srcMC').get(), 'action_text_production').get(), ref(ref(this, 'srcMC').get(), 'action_text_research').get(), ref(ref(this, 'srcMC').get(), 'action_text_religion').get(), ref(ref(this, 'srcMC').get(), 'action_text_preAttack').get(), ref(ref(this, 'srcMC').get(), 'action_text_attack').get(), ref(ref(this, 'srcMC').get(), 'action_text_defense').get(), ref(ref(this, 'srcMC').get(), 'action_text_propaganda').get(), ref(ref(this, 'srcMC').get(), 'action_text_diplomacy').get()]))
    return U

def View___set__clipSrc(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param'], ['param'], closure, 'View')
    assign(ref(this, '_clipSrc'), '=', lambda: e.get('param'))
    return U

def f_1(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_'], closure, None)
    assign(ref(this, 'view'), '=', lambda: ref(ref(this, '_parent').get(), 'view').get())
    e.set('_loc2_', 0)
    e.set('_loc3_', 0)
    while truth(binop('<', e.get('_loc3_'), ref(ref(ref(this, 'view').get(), 'fadeClipsArr').get(), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(ref(this, 'view').get(), 'fadeClipsArr').get(), e.get('_loc3_')).get(), 'clip').get())
            assign(e.ref('_loc5_'), '=', lambda: ref(ref(ref(ref(this, 'view').get(), 'fadeClipsArr').get(), e.get('_loc3_')).get(), 'targetAlpha').get())
            assign(e.ref('_loc6_'), '=', lambda: ref(ref(ref(ref(this, 'view').get(), 'fadeClipsArr').get(), e.get('_loc3_')).get(), 'amount').get())
            assign(e.ref('_loc7_'), '=', lambda: ref(ref(ref(ref(this, 'view').get(), 'fadeClipsArr').get(), e.get('_loc3_')).get(), 'fade').get())
            assign(e.ref('_loc8_'), '=', lambda: ref(ref(ref(ref(this, 'view').get(), 'fadeClipsArr').get(), e.get('_loc3_')).get(), 'isStockBtn').get())
            if truth(e.get('_loc8_')):
                assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
            if truth(binop('==', e.get('_loc7_'), 'in')):
                if truth(binop('>', e.get('_loc5_'), ref(e.get('_loc4_'), '_alpha').get())):
                    if truth(binop('>', binop('+', ref(e.get('_loc4_'), '_alpha').get(), e.get('_loc6_')), e.get('_loc5_'))):
                        assign(ref(e.get('_loc4_'), '_alpha'), '=', lambda: e.get('_loc5_'))
                    else:
                        assign(ref(e.get('_loc4_'), '_alpha'), '+=', lambda: e.get('_loc6_'))
                else:
                    rt.call_ref(ref(ref(ref(this, 'view').get(), 'fadeClipsArr').get(), 'splice'), [e.get('_loc3_'), 1])
            else:
                if truth(binop('==', e.get('_loc7_'), 'out')):
                    if truth(binop('<', e.get('_loc5_'), ref(e.get('_loc4_'), '_alpha').get())):
                        if truth(binop('<', binop('-', ref(e.get('_loc4_'), '_alpha').get(), e.get('_loc6_')), e.get('_loc5_'))):
                            assign(ref(e.get('_loc4_'), '_alpha'), '=', lambda: e.get('_loc5_'))
                        else:
                            assign(ref(e.get('_loc4_'), '_alpha'), '-=', lambda: e.get('_loc6_'))
                    else:
                        rt.call_ref(ref(ref(ref(this, 'view').get(), 'fadeClipsArr').get(), 'splice'), [e.get('_loc3_'), 1])
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    if truth(logical('&&', ref(ref(e.get('_global'), 'view').get(), 'fadeStockActive').get(), lambda: binop('==', e.get('_loc2_'), 0))):
        rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'fadeStockBtn_update'), [])
        assign(ref(ref(e.get('_global'), 'view').get(), 'fadeStockActive'), '=', lambda: False)
    if truth(logical('&&', binop('==', ref(ref(ref(e.get('_global'), 'view').get(), 'fadeClipsArr').get(), 'length').get(), 0), lambda: unary('!', ref(ref(e.get('_global'), 'view').get(), 'fadeStockActive').get()))):
        ref(this, 'onEnterFrame').delete()
    return U

def View_fadeClip(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_clip', 'param_targetAlpha', 'param_fade', 'param_amount', 'param_isStockBtn'], ['_loc7_', 'param_amount', 'param_clip', 'param_fade', 'param_isStockBtn', 'param_targetAlpha'], closure, 'View')
    if truth(binop('==', e.get('param_fade'), 'unset')):
        if truth(binop('>', ref(e.get('param_clip'), '_alpha').get(), e.get('param_targetAlpha'))):
            assign(e.ref('param_fade'), '=', lambda: 'out')
        else:
            assign(e.ref('param_fade'), '=', lambda: 'in')
    if truth(binop('==', ref(ref(this, 'fadeClipsArr').get(), 'length').get(), 0)):
        rt.call_ref(ref(ref(this, 'fadeClipsArr').get(), 'push'), [obj({'clip': e.get('param_clip'), 'targetAlpha': e.get('param_targetAlpha'), 'fade': e.get('param_fade'), 'amount': e.get('param_amount'), 'isStockBtn': e.get('param_isStockBtn')})])
        assign(ref(ref(this, 'fadeClipsTicker').get(), 'onEnterFrame'), '=', lambda: ASFunction(f_1, e))
    else:
        assign(e.ref('_loc7_'), '=', lambda: 0)
        while truth(binop('<', e.get('_loc7_'), ref(ref(this, 'fadeClipsArr').get(), 'length').get())):
            rt.tick()
            try:
                if truth(binop('==', ref(ref(ref(this, 'fadeClipsArr').get(), e.get('_loc7_')).get(), 'clip').get(), e.get('param_clip'))):
                    rt.call_ref(ref(ref(this, 'fadeClipsArr').get(), 'splice'), [e.get('_loc7_'), 1])
                    raise ASBreak()
                assign(e.ref('_loc7_'), '=', lambda: binop('+', e.get('_loc7_'), 1))
            except ASContinue:
                pass
            except ASBreak:
                break
        rt.call_ref(ref(ref(this, 'fadeClipsArr').get(), 'push'), [obj({'clip': e.get('param_clip'), 'targetAlpha': e.get('param_targetAlpha'), 'fade': e.get('param_fade'), 'amount': e.get('param_amount'), 'isStockBtn': e.get('param_isStockBtn')})])
    return U

def View_updateView(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View')
    if truth(rt.call_ref(ref(ref(this, 'presenter').get(), 'allow_curAction_approve'), [])):
        rt.call_ref(ref(ref(this, 'presenter').get(), 'approveAction'), [])
    rt.call_ref(ref(this, 'updateCities'), [])
    return U

def View_error(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param1'], ['param1'], closure, 'View')
    rt.call_ref(ref(this, 'createMessageWindow'), ['Error occured!', e.get('param1')])
    return U

def View_welcomeWindow(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View')
    rt.call_ref(ref(this, 'createMessageWindow'), ['Welcome', 'Welcome to the original World Domination II [tm] AI TEST application! '])
    return U

def f_2(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(this, '_parent').get(), '_alpha'), '=', lambda: 75)
    rt.call_ref(ref(ref(this, '_parent').get(), 'startDrag'), [])
    return U

def f_3(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(ref(this, '_parent').get(), '_alpha'), '=', lambda: 100)
    rt.call_ref(ref(ref(this, '_parent').get(), 'stopDrag'), [])
    return U

def f_5(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(binop('>', ref(this, '_alpha').get(), 0)):
        assign(ref(this, '_alpha'), '-=', lambda: 20)
    else:
        if truth(binop('<=', ref(this, '_alpha').get(), 0)):
            rt.call_ref(ref(this, 'removeMovieClip'), [])
    return U

def f_4(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(this, 'onEnterFrame'), '=', lambda: ASFunction(f_5, e))
    return U

def f_6(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(this, '_parent').get(), 'fadeOutAndRemove'), [])
    return U

def f_7(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'gotoAndStop'), [2])
    return U

def f_8(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'gotoAndStop'), [1])
    return U

def View_createMessageWindow(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_header', 'param_txt'], ['param_header', 'param_txt'], closure, 'View')
    assign(ref(this, '_messageWindow'), '=', lambda: rt.call_ref(ref(ref(this, '_clipSrc').get(), 'attachMovie'), ['messageWindow', 'messageWindow', 9001]))
    assign(ref(ref(this, '_messageWindow').get(), '_x'), '=', lambda: 238)
    assign(ref(ref(this, '_messageWindow').get(), '_y'), '=', lambda: 313)
    assign(ref(ref(ref(this, '_messageWindow').get(), 'header').get(), 'htmlText'), '=', lambda: e.get('param_header'))
    assign(ref(ref(ref(this, '_messageWindow').get(), 'drag').get(), 'onPress'), '=', lambda: ASFunction(f_2, e))
    assign(ref(ref(ref(this, '_messageWindow').get(), 'drag').get(), 'onRelease'), '=', lambda: ASFunction(f_3, e))
    assign(ref(ref(this, '_messageWindow').get(), 'fadeOutAndRemove'), '=', lambda: ASFunction(f_4, e))
    assign(ref(ref(ref(this, '_messageWindow').get(), 'btn').get(), 'onPress'), '=', lambda: ASFunction(f_6, e))
    assign(ref(ref(ref(this, '_messageWindow').get(), 'btn').get(), 'onRollOver'), '=', lambda: ASFunction(f_7, e))
    assign(ref(ref(ref(this, '_messageWindow').get(), 'btn').get(), 'onRollOut'), '=', lambda: ASFunction(f_8, e))
    assign(ref(ref(ref(this, '_messageWindow').get(), 'txt').get(), 'htmlText'), '=', lambda: e.get('param_txt'))
    return U

def View_updateSingleCity(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['city', 'casualties'], ['casualties', 'city'], closure, 'View')
    rt.call_ref(ref(e.get('city'), 'size_and_frame_in_battle'), [e.get('casualties'), True])
    return U

def f_9(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(unary('!', ref(this, 'explosionPlayed').get())):
        if truth(unary('!', ref(this, 'explosion').get())):
            assign(ref(this, 'explosion'), '=', lambda: rt.call_ref(ref(this, 'attachMovie'), ['explosion_dust', binop('+', 'explosion_dust', ref(this, 'randString').get()), rt.call_ref(ref(this, 'getNextHighestDepth'), [])]))
            if truth(ref(this, 'explosion').get()):
                pass
            assign(ref(ref(this, 'explosion').get(), '_x'), '-=', lambda: 10)
            assign(ref(ref(this, 'explosion').get(), '_y'), '-=', lambda: 3)
            assign(ref(ref(this, 'explosion').get(), '_xscale'), '=', lambda: assign(ref(ref(this, 'explosion').get(), '_yscale'), '=', lambda: 130))
            rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'battle').get(), '_toDeleteExplosionMC_arr').get(), 'push'), [ref(this, 'explosion').get()])
        assign(ref(this, 'explosionPlayed'), '=', lambda: True)
        assign(ref(this, 'explosion'), '=', lambda: e.get('undefined'))
    switch_10 = ref(this, 'step').get()
    case_11 = -1
    if case_11 == -1 and strict_eq(switch_10, 1):
        case_11 = 0
    if case_11 == -1 and strict_eq(switch_10, 2):
        case_11 = 1
    if case_11 == -1 and strict_eq(switch_10, 3):
        case_11 = 2
    if case_11 == -1:
        case_11 = 3
    try:
        if 0 <= case_11 <= 0:
            if truth(binop('>', ref(this, '_alpha').get(), 0)):
                assign(ref(this, '_alpha'), '-=', lambda: 15)
            else:
                assign(ref(this, 'step'), '=', lambda: 2)
            raise ASBreak()
        if 0 <= case_11 <= 1:
            rt.call_ref(ref(this, 'gotoAndStop'), [ref(this, 'targetFrame').get()])
            if truth(binop('==', ref(this, 'extra_string').get(), 'propaganda')):
                rt.call_ref(ref(ref(this, 'propagandaBeams').get(), 'play'), [])
                if truth(binop('>', ref(this, 'propaganda_count').get(), 1)):
                    rt.call_ref(ref(ref(this, 'propagandaBeams2').get(), 'gotoAndPlay'), [3])
            assign(ref(this, 'step'), '=', lambda: 3)
            raise ASBreak()
        if 0 <= case_11 <= 2:
            if truth(binop('<', ref(this, '_alpha').get(), 100)):
                assign(ref(this, '_alpha'), '+=', lambda: 15)
            else:
                ref(this, 'onEnterFrame').delete()
        if 0 <= case_11 <= 3:
            return U
    except ASBreak:
        pass
    return U

def View_city_shrink_sequence(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['MC', 'p_targetFrame', 'extra_string', 'propaganda_count'], ['MC', 'extra_string', 'p_targetFrame', 'propaganda_count'], closure, 'View')
    assign(ref(e.get('MC'), 'targetFrame'), '=', lambda: e.get('p_targetFrame'))
    assign(ref(e.get('MC'), 'step'), '=', lambda: 1)
    assign(ref(e.get('MC'), 'explosionPlayed'), '=', lambda: False)
    assign(ref(e.get('MC'), 'extra_string'), '=', lambda: e.get('extra_string'))
    assign(ref(e.get('MC'), 'propaganda_count'), '=', lambda: e.get('propaganda_count'))
    assign(ref(e.get('MC'), 'randString'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [10000, 99999]))
    assign(ref(e.get('MC'), 'onEnterFrame'), '=', lambda: ASFunction(f_9, e))
    return U

def f_12(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'citySelect'), [ref(this, 'obj').get()])
    return U

def View_spawnCity(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['city', 'mapType'], ['city', 'mapType'], closure, 'View')
    assign(ref(e.get('city'), 'image'), '=', lambda: rt.call_ref(ref(ref(e.get('city'), 'mapMC').get(), 'attachMovie'), [ref(e.get('city'), 'citySet').get(), binop('+', 'city', ref(e.get('city'), 'num').get()), ref(e.get('city'), 'image_depth').get()]))
    assign(ref(ref(ref(e.get('city'), 'image').get(), 'mc').get(), 'obj'), '=', lambda: e.get('city'))
    assign(ref(ref(ref(e.get('city'), 'image').get(), 'mc').get(), 'btnSet'), '=', lambda: 'city')
    assign(ref(ref(ref(e.get('city'), 'image').get(), 'mc').get(), 'onPress'), '=', lambda: ASFunction(f_12, e))
    assign(ref(ref(e.get('city'), 'image').get(), '_x'), '=', lambda: ref(e.get('city'), 'xPos').get())
    assign(ref(ref(e.get('city'), 'image').get(), '_y'), '=', lambda: ref(e.get('city'), 'yPos').get())
    rt.call_ref(ref(ref(e.get('city'), 'image').get(), 'gotoAndStop'), [ref(e.get('city'), 'size_and_frame').get()])
    assign(ref(ref(e.get('city'), 'image').get(), '_xscale'), '=', lambda: assign(ref(ref(e.get('city'), 'image').get(), '_yscale'), '=', lambda: 80))
    assign(ref(e.get('city'), 'debugTextField'), '=', lambda: ref(ref(e.get('city'), 'image').get(), 'debugTXT').get())
    assign(ref(ref(e.get('city'), 'debugTextField').get(), 'text'), '=', lambda: binop('+', 'pop.: ', ref(e.get('city'), 'population').get()))
    assign(ref(ref(e.get('city'), 'debugTextField').get(), 'embedFonts'), '=', lambda: True)
    return U

def View_update_flags(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_'], closure, 'View')
    e.set('_loc2_', 0)
    while truth(binop('<', e.get('_loc2_'), 6)):
        rt.tick()
        try:
            rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', 'flag', e.get('_loc2_'))).get(), 'gotoAndStop'), ['empty'])
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc3_', 0)
    while truth(binop('<', e.get('_loc3_'), ref(ref(ref(this, 'model').get(), 'playerArr').get(), 'length').get())):
        rt.tick()
        try:
            if truth(unary('!', ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('_loc3_')).get(), 'alive').get())):
                assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('_loc3_')).get())
                rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', 'flag', e.get('_loc3_'))).get(), 'gotoAndStop'), [ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc4_'), 'lastAttackedBy_num').get()).get(), 'religion_code').get()])
                assign(e.ref('_loc5_'), '=', lambda: rt.construct(e.get('Color'), [ref(ref(ref(this, 'battleSrcMC').get(), binop('+', 'flag', e.get('_loc3_'))).get(), 'tintMC').get()]))
                rt.call_ref(ref(e.get('_loc5_'), 'setTransform'), [ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), ref(e.get('_loc4_'), 'lastAttackedBy_num').get()).get(), 'playerColorTint1').get()])
            assign(e.ref('_loc3_'), '=', lambda: binop('+', e.get('_loc3_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc6_', 0)
    while truth(binop('<', e.get('_loc6_'), ref(ref(ref(this, 'model').get(), 'activePlayerArr').get(), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc7_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'activePlayerArr').get(), e.get('_loc6_')).get())
            rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', 'flag', ref(e.get('_loc7_'), 'playerNum').get())).get(), 'gotoAndStop'), [ref(e.get('_loc7_'), 'religion_code').get()])
            assign(e.ref('_loc8_'), '=', lambda: rt.construct(e.get('Color'), [ref(ref(ref(this, 'battleSrcMC').get(), binop('+', 'flag', ref(e.get('_loc7_'), 'playerNum').get())).get(), 'tintMC').get()]))
            rt.call_ref(ref(e.get('_loc8_'), 'setTransform'), [ref(e.get('_loc7_'), 'playerColorTint1').get()])
            assign(e.ref('_loc6_'), '=', lambda: binop('+', e.get('_loc6_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def View_remove_city_popups(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'View')
    for key_13 in keys(ref(ref(ref(this, 'model').get(), 'human').get(), 'cityArr').get()):
        e.ref('i').set(key_13)
        rt.tick()
        try:
            rt.call_ref(ref(ref(ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'cityArr').get(), e.get('i')).get(), 'image').get(), 'citizensMovie').get(), 'gotoAndStop'), [1])
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def f_16(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(logical('&&', binop('==', ref(ref(e.get('_global'), 'view').get(), 'currentViewType').get(), 'interface'), lambda: binop('>', ref(this, 'population').get(), 0))):
        rt.call_ref(ref(ref(this, 'citizensMovie').get(), 'gotoAndStop'), [2])
        assign(ref(ref(ref(this, 'citizensMovie').get(), 'txt1').get(), 'text'), '=', lambda: ref(this, 'population').get())
        assign(ref(ref(this, 'citizensMovie').get(), '_xscale'), '=', lambda: assign(ref(ref(this, 'citizensMovie').get(), '_yscale'), '=', lambda: 200))
    return U

def f_17(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(this, 'citizensMovie').get(), 'gotoAndStop'), [1])
    return U

def f_18(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(binop('==', ref(ref(e.get('_global'), 'view').get(), 'currentViewType').get(), 'interface')):
        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'roll_over_map'), [ref(this, 'roll_num').get()])
    return U

def View_updateCities(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', 'i', 'j'], closure, 'View')
    rt.call_ref(ref(this, 'update_flags'), [])
    for key_14 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_14)
        rt.tick()
        try:
            for key_15 in keys(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get(), 'cityArr').get()):
                e.ref('j').set(key_15)
                rt.tick()
                try:
                    assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get(), 'cityArr').get(), e.get('j')).get())
                    rt.call_ref(ref(ref(e.get('_loc2_'), 'image').get(), 'gotoAndStop'), [ref(e.get('_loc2_'), 'size_and_frame').get()])
                    assign(ref(ref(e.get('_loc2_'), 'image').get(), 'population'), '=', lambda: ref(e.get('_loc2_'), 'population').get())
                    if truth(binop('==', ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get(), ref(ref(this, 'model').get(), 'human').get())):
                        assign(ref(ref(e.get('_loc2_'), 'image').get(), 'useHandCursor'), '=', lambda: False)
                        assign(ref(ref(e.get('_loc2_'), 'image').get(), 'population'), '=', lambda: ref(e.get('_loc2_'), 'population').get())
                        assign(ref(ref(e.get('_loc2_'), 'image').get(), 'onRollOver'), '=', lambda: ASFunction(f_16, e))
                        assign(ref(ref(e.get('_loc2_'), 'image').get(), 'onRollOut'), '=', lambda: ASFunction(f_17, e))
                    else:
                        assign(ref(ref(ref(e.get('_loc2_'), 'image').get(), 'mc').get(), 'roll_num'), '=', lambda: e.get('i'))
                        assign(ref(ref(ref(e.get('_loc2_'), 'image').get(), 'mc').get(), 'onRollOver'), '=', lambda: ASFunction(f_18, e))
                    assign(ref(e.get('_loc2_'), 'curCasualties'), '=', lambda: 0)
                    assign(ref(e.get('_loc2_'), 'prevPopulation'), '=', lambda: ref(e.get('_loc2_'), 'population').get())
                    rt.call_ref(ref(ref(e.get('_loc2_'), 'explosion').get(), 'removeMovieClip'), [])
                    assign(ref(e.get('_loc2_'), 'explosion'), '=', lambda: e.get('undefined'))
                    assign(ref(ref(e.get('_loc2_'), 'debugTextField').get(), 'text'), '=', lambda: binop('+', 'pop: ', ref(e.get('_loc2_'), 'population').get()))
                    if truth(unary('!', ref(ref(this, 'battleSrcMC').get(), binop('+', 'city', ref(e.get('_loc2_'), 'num').get())).get())):
                        rt.call_ref(ref(e.get('_loc2_'), 'setMapVars'), [ref(this, 'battleSrcMC').get(), binop('+', ref(this, 'smallMapCityDepthStart').get(), ref(e.get('_loc2_'), 'num').get()), ref(ref(ref(ref(ref(this, 'model').get(), 'cityPositions').get(), e.get('i')).get(), e.get('j')).get(), 0).get(), ref(ref(ref(ref(ref(this, 'model').get(), 'cityPositions').get(), e.get('i')).get(), e.get('j')).get(), 1).get()])
                        assign(ref(e.get('_loc2_'), 'theme'), '=', lambda: ref(ref(e.get('_loc2_'), 'plr').get(), 'buildingSet_id').get())
                        rt.call_ref(ref(this, 'spawnCity'), [e.get('_loc2_'), 'battleMap'])
                    if truth(binop('<', ref(e.get('_loc2_'), 'population').get(), 0)):
                        assign(ref(e.get('_loc2_'), 'population'), '=', lambda: 0)
                    if truth(ref(e.get('_loc2_'), '_isSelected').get()):
                        if truth(unary('!', ref(e.get('_loc2_'), 'selectionMC').get())):
                            assign(ref(e.get('_loc2_'), 'selectionMC'), '=', lambda: rt.call_ref(ref(ref(e.get('_loc2_'), 'mapMC').get(), 'attachMovie'), ['map_icon_crosshair', binop('+', 'crosshair', ref(e.get('_loc2_'), 'cityID').get()), binop('+', ref(e.get('_loc2_'), 'image_depth').get(), ref(this, 'citySelectionDepthStart').get())]))
                        assign(ref(ref(e.get('_loc2_'), 'selectionMC').get(), '_xscale'), '=', lambda: assign(ref(ref(e.get('_loc2_'), 'selectionMC').get(), '_yscale'), '=', lambda: 200))
                        assign(ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'mcArray'), '=', lambda: arr([]))
                        if truth(logical('&&', ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'attack').get(), lambda: unary('!', ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'attackMC').get()))):
                            assign(ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'attackMC'), '=', lambda: rt.call_ref(ref(ref(e.get('_loc2_'), 'selectionMC').get(), 'attachMovie'), ['map_icon_soldier', 'map_icon_soldier', 1]))
                            rt.call_ref(ref(ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'mcArray').get(), 'push'), [ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'attackMC').get()])
                        if truth(logical('&&', ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'preAttack').get(), lambda: unary('!', ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'preAttackMC').get()))):
                            assign(ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'preAttackMC'), '=', lambda: rt.call_ref(ref(ref(e.get('_loc2_'), 'selectionMC').get(), 'attachMovie'), [binop('+', 'map_icon_', ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'preAttackWeapon').get()), 'map_icon_pre', 2]))
                            rt.call_ref(ref(ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'mcArray').get(), 'push'), [ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'preAttackMC').get()])
                        if truth(logical('&&', ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'propaganda').get(), lambda: unary('!', ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'preAttackMC').get()))):
                            assign(ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'propagandaMC'), '=', lambda: rt.call_ref(ref(ref(e.get('_loc2_'), 'selectionMC').get(), 'attachMovie'), ['map_icon_propaganda', 'map_icon_propaganda', 3]))
                            rt.call_ref(ref(ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'mcArray').get(), 'push'), [ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'propagandaMC').get()])
                        if truth(logical('&&', ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'ship').get(), lambda: binop('!=', ref(ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'shipMC_arr').get(), 'length').get(), ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'shipCount').get()))):
                            assign(e.ref('_loc4_'), '=', lambda: 0)
                            while truth(binop('<', e.get('_loc4_'), ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'shipCount').get())):
                                rt.tick()
                                try:
                                    assign(e.ref('_loc3_'), '=', lambda: rt.call_ref(ref(ref(e.get('_loc2_'), 'selectionMC').get(), 'attachMovie'), ['map_icon_special', 'map_icon_special', binop('+', e.get('_loc4_'), 4)]))
                                    rt.call_ref(ref(ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'shipMC_arr').get(), 'push'), [e.get('_loc3_')])
                                    rt.call_ref(ref(ref(ref(e.get('_loc2_'), 'selectionObj').get(), 'mcArray').get(), 'push'), [e.get('_loc3_')])
                                    assign(e.ref('_loc4_'), '=', lambda: binop('+', e.get('_loc4_'), 1))
                                except ASContinue:
                                    pass
                                except ASBreak:
                                    break
                        rt.call_ref(ref(e.get('_loc2_'), 'alignSelectionMC'), [])
                    else:
                        if truth(ref(e.get('_loc2_'), 'hideForSelection').get()):
                            assign(ref(e.get('_loc2_'), 'colorIMG_red'), '=', lambda: rt.construct(e.get('Color'), [ref(e.get('_loc2_'), 'image').get()]))
                            rt.call_ref(ref(ref(e.get('_loc2_'), 'colorIMG_red').get(), 'setTransform'), [ref(ref(ref(e.get('_global'), 'model').get(), 'wd_colors').get(), 'city_red').get()])
                        else:
                            if truth(logical('&&', ref(e.get('_loc2_'), 'showForSelection').get(), lambda: binop('>', ref(e.get('_loc2_'), 'population').get(), 0))):
                                assign(ref(e.get('_loc2_'), 'colorIMG_green'), '=', lambda: rt.construct(e.get('Color'), [ref(e.get('_loc2_'), 'image').get()]))
                                rt.call_ref(ref(ref(e.get('_loc2_'), 'colorIMG_green').get(), 'setTransform'), [ref(ref(ref(e.get('_global'), 'model').get(), 'wd_colors').get(), 'city_green').get()])
                            else:
                                assign(ref(ref(e.get('_loc2_'), 'image').get(), '_alpha'), '=', lambda: 100)
                                assign(ref(e.get('_loc2_'), 'colorIMG_red'), '=', lambda: rt.construct(e.get('Color'), [ref(e.get('_loc2_'), 'image').get()]))
                                rt.call_ref(ref(ref(e.get('_loc2_'), 'colorIMG_red').get(), 'setTransform'), [ref(ref(ref(e.get('_global'), 'model').get(), 'wd_colors').get(), '_default').get()])
                    if truth(logical('&&', ref(e.get('_loc2_'), 'bioloaded').get(), lambda: unary('!', ref(ref(e.get('_loc2_'), 'image').get(), 'bioCloud_container').get()))):
                        rt.call_ref(ref(this, 'createBioCloud'), [e.get('_loc2_')])
                except ASContinue:
                    pass
                except ASBreak:
                    break
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def View_resetActionBuildings(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_'], closure, 'View')
    e.set('_loc2_', 0)
    while truth(binop('<=', e.get('_loc2_'), 4)):
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), e.get('_loc2_')).get())
            if truth(binop('!=', ref(e.get('_loc3_'), 'preAttackStatus').get(), 'ready')):
                rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', binop('+', 'ab', e.get('_loc2_')), '_1')).get(), 'gotoAndStop'), [1])
                rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', binop('+', 'ab', e.get('_loc2_')), '_2')).get(), 'gotoAndStop'), [1])
            else:
                if truth(binop('!=', ref(e.get('_loc3_'), 'preLocation').get(), 1)):
                    rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', binop('+', 'ab', e.get('_loc2_')), '_1')).get(), 'gotoAndStop'), [1])
                else:
                    if truth(binop('!=', ref(e.get('_loc3_'), 'preLocation').get(), 2)):
                        rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', binop('+', 'ab', e.get('_loc2_')), '_2')).get(), 'gotoAndStop'), [1])
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def View_changeOver(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_loc0_', '_loc3_', '_loc4_', '_loc5_', '_param', '_temp_1', '_temp_2', '_temp_3', '_temp_4', 'i'], closure, 'View')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(this, 'presenter_interface').get(), 'debug_automate_interval_ID').get()])
    for key_19 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_19)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get())
            assign(e.ref('_loc4_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc4_'), ref(ref(e.get('_loc3_'), 'regardArr').get(), 'length').get())):
                rt.tick()
                try:
                    if truth(binop('>', ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')).get(), 100)):
                        assign(ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')), '=', lambda: 100)
                    else:
                        if truth(binop('<', ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')).get(), 0)):
                            assign(ref(ref(e.get('_loc3_'), 'regardArr').get(), e.get('_loc4_')), '=', lambda: 0)
                    assign(e.ref('_loc4_'), '=', lambda: binop('+', e.get('_loc4_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            if truth(binop('==', ref(ref(e.get('_loc3_'), 'preAttackWeapon').get(), 'weaponName').get(), 'ship')):
                rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', 'carrier', ref(e.get('_loc3_'), 'playerNum').get())).get(), 'gotoAndStop'), [2])
            rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', 'carrier', ref(e.get('_loc3_'), 'playerNum').get())).get(), 'gotoAndStop'), [ref(e.get('_loc3_'), 'shipFrame').get()])
            assign(e.ref('_loc5_'), '=', lambda: rt.construct(e.get('Color'), [ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', 'carrier', ref(e.get('_loc3_'), 'playerNum').get())).get(), 'mc').get(), 'carrier_tint').get()]))
            rt.call_ref(ref(e.get('_loc5_'), 'setTransform'), [ref(e.get('_loc3_'), 'playerColorTint1').get()])
        except ASContinue:
            pass
        except ASBreak:
            break
    rt.call_ref(ref(this, 'setMapFrames'), [])
    rt.call_ref(ref(this, 'setFaceFrames'), [])
    rt.call_ref(ref(this, 'curActionText'), ['none'])
    rt.call_ref(ref(ref(this, 'presenter').get(), 'remove_played_sound_objects'), [])
    switch_20 = e.get('_param')
    case_21 = -1
    if case_21 == -1 and strict_eq(switch_20, 'toBattle'):
        case_21 = 0
    if case_21 == -1 and strict_eq(switch_20, 'toInterface'):
        case_21 = 1
    if case_21 == -1 and strict_eq(switch_20, 'toPlayerLost'):
        case_21 = 2
    if case_21 == -1 and strict_eq(switch_20, 'toPlayerWin'):
        case_21 = 3
    if case_21 == -1:
        case_21 = 4
    try:
        if 0 <= case_21 <= 0:
            assign(ref(ref(e.get('_global'), 'model').get(), 'satellite_sound_playing'), '=', lambda: False)
            assign(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), '_visible'), '=', lambda: False)
            assign(ref(this, 'currentViewType'), '=', lambda: 'battle')
            e.set('_temp_2', ref(this, 'battleSrcMC').get())
            e.set('_temp_1', '_xscale')
            assign(ref(ref(this, 'battleSrcMC').get(), '_yscale'), '=', lambda: assign(e.ref('_loc0_'), '=', lambda: 100))
            assign(ref(e.get('_temp_2'), e.get('_temp_1')), '=', lambda: e.get('_loc0_'))
            assign(ref(ref(this, 'battleSrcMC').get(), '_x'), '=', lambda: 0)
            assign(ref(ref(this, 'battleSrcMC').get(), '_y'), '=', lambda: 0)
            rt.call_ref(ref(this, 'setABDepth'), [])
            rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'deselectCities'), ['all'])
            if truth(rt.call_ref(ref(ref(this, 'presenter').get(), 'check_ch_active'), ['kill_all'])):
                rt.call_ref(ref(ref(this, 'presenter').get(), 'explode_all'), [])
            if truth(rt.call_ref(ref(ref(this, 'presenter').get(), 'check_ch_active'), ['tech'])):
                rt.call_ref(ref(ref(this, 'presenter').get(), 'deactivate_ch'), ['tech'])
                rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'techTree').get(), 'force_invent_tech_ch'), [])
                rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'weaponStock').get(), 'activateAll'), [])
            if truth(rt.call_ref(ref(ref(this, 'presenter').get(), 'check_ch_active'), ['stock'])):
                rt.call_ref(ref(ref(this, 'presenter').get(), 'deactivate_ch'), ['stock'])
                rt.call_ref(ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'weaponStock').get(), 'max_stock'), [])
            if truth(rt.call_ref(ref(ref(this, 'presenter').get(), 'check_ch_active'), ['cash'])):
                rt.call_ref(ref(ref(this, 'presenter').get(), 'deactivate_ch'), ['cash'])
                assign(ref(ref(ref(this, 'model').get(), 'human').get(), 'money'), '=', lambda: 1000)
            if truth(rt.call_ref(ref(ref(this, 'presenter').get(), 'check_ch_active'), ['nessy'])):
                rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), 'nessy').get(), 'play'), [])
            if truth(rt.call_ref(ref(ref(this, 'presenter').get(), 'check_ch_active'), ['orca'])):
                rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), 'orca').get(), 'play'), [])
            if truth(rt.call_ref(ref(ref(this, 'presenter').get(), 'check_ch_active'), ['bush'])):
                rt.call_ref(ref(ref(this, 'presenter').get(), 'deactivate_ch'), ['bush'])
                rt.call_ref(ref(ref(this, 'presenter').get(), 'explode_self'), [])
            raise ASBreak()
        if 0 <= case_21 <= 1:
            assign(ref(ref(ref(ref(e.get('_global'), 'view_interface').get(), 'interfaceMC').get(), 'shortMSG_textField').get(), 'scroll'), '=', lambda: 0)
            assign(ref(ref(this, 'model').get(), 'active_ambient_sounds'), '=', lambda: rt.construct(e.get('Array'), []))
            assign(ref(ref(this, 'presenter_interface').get(), 'blockAllBtns'), '=', lambda: False)
            assign(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), '_visible'), '=', lambda: True)
            e.set('_temp_4', ref(this, 'battleSrcMC').get())
            e.set('_temp_3', '_xscale')
            assign(ref(ref(this, 'battleSrcMC').get(), '_yscale'), '=', lambda: assign(e.ref('_loc0_'), '=', lambda: 46))
            assign(ref(e.get('_temp_4'), e.get('_temp_3')), '=', lambda: e.get('_loc0_'))
            assign(ref(ref(this, 'battleSrcMC').get(), '_x'), '=', lambda: 205)
            assign(ref(ref(this, 'battleSrcMC').get(), '_y'), '=', lambda: 135)
            assign(ref(this, 'currentViewType'), '=', lambda: 'interface')
            if truth(logical('||', binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'ready'), lambda: binop('==', ref(ref(ref(this, 'model').get(), 'human').get(), 'preAttackStatus').get(), 'active'))):
                assign(ref(ref(this, 'model').get(), 'userSelectedActionBtn'), '=', lambda: 'preAttack')
            rt.call_ref(ref(ref(this, 'presenter_interface').get(), 'removeBioClips'), [])
            rt.call_ref(ref(ref(this, 'presenter_interface').get(), 'attachBioClips'), [])
            rt.call_ref(ref(ref(this, 'presenter').get(), 'stop_continues_sound_objects'), [])
            rt.call_ref(ref(ref(this, 'presenter_interface').get(), 'resetBtns'), [])
            assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [ref(e.get('_global'), 'view').get(), 'to_interface_timed_3', 5]))
            raise ASBreak()
        if 0 <= case_21 <= 2:
            rt.call_ref(ref(this, 'interface_before_end_game_sequence'), ['lost'])
            raise ASBreak()
        if 0 <= case_21 <= 3:
            rt.call_ref(ref(this, 'interface_before_end_game_sequence'), ['win'])
        if 0 <= case_21 <= 4:
            return U
    except ASBreak:
        pass
    return U

def View_to_interface_timed_3(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'View')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
    for key_22 in keys(ref(ref(e.get('_global'), 'view_interface').get(), 'actionBtn_arr').get()):
        e.ref('i').set(key_22)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(this, 'view_interface').get(), 'actionBtn_arr').get(), e.get('i')).get())
            if truth(logical('&&', binop('!=', ref(e.get('_loc2_'), 'actionName').get(), ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnAction_1').get(), 'action').get()), lambda: binop('!=', ref(e.get('_loc2_'), 'actionName').get(), ref(ref(ref(ref(this, 'model').get(), 'human').get(), 'turnAction_2').get(), 'action').get()))):
                assign(ref(e.get('_loc2_'), 'isSetAction'), '=', lambda: False)
            else:
                if truth(unary('!', ref(e.get('_loc2_'), 'isSetAction').get())):
                    assign(ref(e.get('_loc2_'), 'state'), '=', lambda: 1)
                    rt.call_ref(ref(e.get('_loc2_'), 'updateBtn'), [])
            assign(ref(ref(ref(ref(e.get('_global'), 'view_interface').get(), 'btn_arr').get(), e.get('i')).get(), 'pressed'), '=', lambda: False)
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [ref(e.get('_global'), 'view').get(), 'to_interface_timed_3_A', 5]))
    return U

def View_to_interface_timed_3_A(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
    rt.call_ref(ref(ref(this, 'model').get(), 'deselectCities'), [ref(ref(this, 'model').get(), 'userSelectedActionBtn').get()])
    assign(ref(ref(this, 'model').get(), 'userSelectedStockBtn'), '=', lambda: e.get('undefined'))
    assign(ref(ref(this, 'model').get(), 'userSelectedActionBtn'), '=', lambda: e.get('undefined'))
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [ref(e.get('_global'), 'view').get(), 'to_interface_timed_3_B', 5]))
    return U

def View_to_interface_timed_3_B(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
    rt.call_ref(ref(ref(this, 'model').get(), 'resetUserSelections'), [])
    assign(ref(ref(e.get('_global'), 'model_interface').get(), 'cur_pressed_action_btn'), '=', lambda: e.get('undefined'))
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [ref(e.get('_global'), 'view').get(), 'to_interface_timed_3_C', 5]))
    return U

def View_to_interface_timed_3_C(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'updateView_debug_1'), [])
    return U

def View_to_interface_timed_4(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
    rt.call_ref(ref(ref(this, 'presenter_interface').get(), 'update_leaderFaces'), [])
    return U

def View_to_interface_timed_5(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
    assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [ref(e.get('_global'), 'view').get(), 'to_interface_timed_6', 5]))
    return U

def View_interface_before_end_game_sequence(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_status'], ['a_status'], closure, 'View')
    assign(ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'presenter_interface').get(), 'blockAllBtns'), '=', lambda: True)
    assign(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), '_visible'), '=', lambda: True)
    assign(ref(ref(this, 'battleSrcMC').get(), '_xscale'), '=', lambda: assign(ref(ref(this, 'battleSrcMC').get(), '_yscale'), '=', lambda: 46))
    assign(ref(ref(this, 'battleSrcMC').get(), '_x'), '=', lambda: 205)
    assign(ref(ref(this, 'battleSrcMC').get(), '_y'), '=', lambda: 135)
    rt.call_ref(ref(ref(this, 'presenter_interface').get(), 'updateView'), [])
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'endgame_interval_1_id').get()])
    assign(ref(this, 'endgame_interval_1_id'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'end_game_sequence', 3000, e.get('a_status')]))
    rt.call_ref(ref(ref(this, 'presenter').get(), 'stop_continues_sound_objects'), [])
    return U

def View_end_game_sequence(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_status'], ['a_status'], closure, 'View')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'endgame_interval_1_id').get()])
    assign(ref(ref(e.get('_level0'), 'endGameMC').get(), '_visible'), '=', lambda: True)
    rt.call_ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'gotoAndStop'), [e.get('a_status')])
    assign(ref(ref(ref(this, 'view_interface').get(), 'interfaceMC').get(), '_visible'), '=', lambda: False)
    assign(ref(this, 'endgame_interval_1_id'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'end_game_sequence_2', 2000, e.get('a_status')]))
    return U

def f_27(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(binop('==', rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'get_demo_version_name'), []), 'Miniclip')):
        rt.call_ref(ref(ref(ref(ref(this, '_parent').get(), '_parent').get(), 'highscore').get(), 'gotoAndStop'), [2])
    if truth(binop('==', rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'get_demo_version_name'), []), '2dplay')):
        rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'submit_2dplay_score'), [])
    else:
        rt.call_ref(ref(ref(ref(ref(this, '_parent').get(), '_parent').get(), 'highscore').get(), 'loadMovie'), ['http://www.youdagames.com/highscores/flash.php'])
        assign(ref(ref(ref(ref(this, '_parent').get(), '_parent').get(), 'fade_out').get(), '_alpha'), '=', lambda: 55)
    return U

def f_24(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    switch_25 = ref(this, 'cur_sequence').get()
    case_26 = -1
    if case_26 == -1 and strict_eq(switch_25, 1):
        case_26 = 0
    if case_26 == -1 and strict_eq(switch_25, 2):
        case_26 = 1
    if case_26 == -1 and strict_eq(switch_25, 3):
        case_26 = 2
    if case_26 == -1 and strict_eq(switch_25, 4):
        case_26 = 3
    if case_26 == -1:
        case_26 = -1
    try:
        if 0 <= case_26 <= 0:
            assign(ref(this, 'maxPlus'), '=', lambda: binop('/', ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'score').get(), 100))
            assign(ref(this, 'score_count'), '+=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [1, ref(this, 'maxPlus').get()]))
            if truth(binop('>=', ref(this, 'score_count').get(), ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'score').get())):
                assign(ref(this, 'score_count'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'score').get())
                rt.call_ref(ref(ref(this, 'sound').get(), 'stop'), [])
                assign(ref(this, 'cur_sequence'), '=', lambda: 2)
            assign(ref(ref(this, 'txt2').get(), 'text'), '=', lambda: rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'display_format_dot_notation'), [ref(this, 'score_count').get()]))
            raise ASBreak()
        if 0 <= case_26 <= 1:
            if truth(ref(this, 'satellite_multiplier_count').get()):
                assign(ref(this, 'count1'), '=', lambda: binop('+', ref(this, 'count1').get(), 1))
                if truth(binop('>', ref(this, 'count1').get(), 40)):
                    rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['Satelite multiplier.Mp3'])
                    rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [])
                    assign(ref(this, 'count1'), '=', lambda: 0)
                    assign(ref(this, 'cur_satellite_count'), '=', lambda: binop('+', ref(this, 'cur_satellite_count').get(), 1))
                    assign(ref(this, 'txt_1'), '=', lambda: binop('+', binop('+', 'Space satellite multiplier: x ', ref(this, 'cur_satellite_count').get()), ' <br/> '))
                if truth(logical('&&', binop('==', ref(this, 'count1').get(), 2), lambda: binop('>', ref(this, 'cur_satellite_count').get(), 0))):
                    assign(ref(ref(this, 'txt2').get(), 'text'), '=', lambda: '')
                    assign(ref(this, 'score_count'), '*=', lambda: 2)
                if truth(logical('&&', binop('==', ref(this, 'count1').get(), 6), lambda: binop('>', ref(this, 'cur_satellite_count').get(), 0))):
                    assign(ref(ref(this, 'txt2').get(), 'text'), '=', lambda: rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'display_format_dot_notation'), [ref(this, 'score_count').get()]))
                if truth(logical('&&', binop('==', ref(this, 'cur_satellite_count').get(), ref(this, 'satellite_multiplier_count').get()), lambda: binop('>', ref(this, 'count1').get(), 7))):
                    assign(ref(this, 'cur_sequence'), '=', lambda: 3)
            else:
                assign(ref(this, 'cur_sequence'), '=', lambda: 3)
            raise ASBreak()
        if 0 <= case_26 <= 2:
            if truth(ref(this, 'flag_bonus').get()):
                assign(ref(this, 'count2'), '=', lambda: binop('+', ref(this, 'count2').get(), 1))
                if truth(binop('>', ref(this, 'count2').get(), 40)):
                    rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['Country domination bonus.Mp3'])
                    rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [])
                    assign(ref(this, 'count2'), '=', lambda: 0)
                    assign(ref(this, 'cur_flag_bonus'), '=', lambda: binop('+', ref(this, 'cur_flag_bonus').get(), 1))
                    assign(ref(this, 'txt_2'), '=', lambda: binop('+', binop('+', 'Flag bonus (250.000): x ', ref(this, 'cur_flag_bonus').get()), ' <br/> '))
                if truth(logical('&&', binop('==', ref(this, 'count2').get(), 2), lambda: binop('>', ref(this, 'cur_flag_bonus').get(), 0))):
                    assign(ref(ref(this, 'txt2').get(), 'text'), '=', lambda: '')
                    assign(ref(this, 'score_count'), '+=', lambda: binop('*', 250000, ref(this, 'cur_flag_bonus').get()))
                if truth(logical('&&', binop('==', ref(this, 'count2').get(), 6), lambda: binop('>', ref(this, 'cur_flag_bonus').get(), 0))):
                    assign(ref(ref(this, 'txt2').get(), 'text'), '=', lambda: rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'display_format_dot_notation'), [ref(this, 'score_count').get()]))
                if truth(logical('&&', binop('==', ref(this, 'cur_flag_bonus').get(), ref(this, 'flag_bonus').get()), lambda: binop('>', ref(this, 'count2').get(), 7))):
                    ref(this, 'onEnterFrame').delete()
            else:
                assign(ref(this, 'cur_sequence'), '=', lambda: 4)
            raise ASBreak()
        if 0 <= case_26 <= 3:
            rt.call_ref(ref(ref(this, 'btnMC_submitScore').get(), 'gotoAndStop'), [2])
            assign(ref(ref(ref(ref(this, 'btnMC_submitScore').get(), 'txtMC_submit').get(), 'txt').get(), 'text'), '=', lambda: 'Submit highscore')
            assign(ref(ref(ref(this, 'btnMC_submitScore').get(), 'btn_submit').get(), 'onPress'), '=', lambda: ASFunction(f_27, e))
            ref(this, 'onEnterFrame').delete()
    except ASBreak:
        pass
    assign(ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'txt3').get(), 'htmlText'), '=', lambda: binop('+', ref(this, 'txt_1').get(), ref(this, 'txt_2').get()))
    return U

def f_28(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'btn_pressed_full'), [])
    return U

def f_29(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('getURL', [ref(ref(e.get('_global'), 'model').get(), 'full_version_url').get(), '_blank'])
    return U

def f_30(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'btn_pressed_new_game'), [])
    return U

def View_end_game_sequence_2(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_status'], ['_loc3_', '_loc4_', '_loc5_', '_loc6_', 'a_status', 'i'], closure, 'View')
    assign(ref(e.get('_root'), 'hs_score'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'human').get(), 'score').get())
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'endgame_interval_1_id').get()])
    if truth(binop('==', e.get('a_status'), 'lost')):
        assign(e.ref('_loc3_'), '=', lambda: rt.call_ref(ref(e.get('_level0'), 'createEmptyMovieClip'), ['loose_sound', rt.call_ref(ref(e.get('_level0'), 'getNextHighestDepth'), [])]))
        assign(e.ref('_loc4_'), '=', lambda: rt.construct(e.get('Sound'), [e.get('_loc3_')]))
        rt.call_ref(ref(e.get('_loc4_'), 'attachSound'), ['Loose.Mp3'])
        rt.call_ref(ref(e.get('_loc4_'), 'start'), [])
    if truth(ref(ref(this, 'model').get(), 'corrupt_highscore').get()):
        assign(ref(ref(ref(this, 'model').get(), 'human').get(), 'score'), '=', lambda: 0)
    e.set('_loc5_', rt.construct(e.get('Object'), [obj({'win': "After killing most of the world's population, your country stands victorious in its quest for world domination. ", 'lost': 'Your country was destroyed. <br/> You lost the war for World Domination. '})]))
    e.set('_loc6_', rt.construct(e.get('Object'), [obj({'win': '', 'lost': ''})]))
    rt.call_ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'gotoAndStop'), [binop('+', e.get('a_status'), 2)])
    assign(ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'txt1').get(), 'htmlText'), '=', lambda: ref(e.get('_loc5_'), e.get('a_status')).get())
    assign(ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'txt2').get(), 'text'), '=', lambda: 0)
    assign(ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'txt3').get(), 'htmlText'), '=', lambda: '')
    assign(ref(ref(e.get('_level0'), 'endGameMC').get(), 'score_count'), '=', lambda: 0)
    assign(ref(ref(e.get('_level0'), 'endGameMC').get(), 'satellite_multiplier_count'), '=', lambda: ref(ref(ref(this, 'model').get(), 'human').get(), 'satellites_used').get())
    assign(ref(ref(e.get('_level0'), 'endGameMC').get(), 'cur_satellite_count'), '=', lambda: 0)
    assign(ref(ref(e.get('_level0'), 'endGameMC').get(), 'flag_bonus'), '=', lambda: 0)
    for key_23 in keys(ref(ref(this, 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_23)
        rt.tick()
        try:
            if truth(binop('==', ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('i')).get(), 'lastAttackedBy_num').get(), 0)):
                update(ref(ref(e.get('_level0'), 'endGameMC').get(), 'flag_bonus'), 1, False)
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(ref(e.get('_level0'), 'endGameMC').get(), 'cur_flag_bonus'), '=', lambda: 0)
    assign(ref(ref(e.get('_level0'), 'endGameMC').get(), 'txt_1'), '=', lambda: '')
    assign(ref(ref(e.get('_level0'), 'endGameMC').get(), 'txt_2'), '=', lambda: '')
    rt.call_ref(ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'sound').get(), 'stop'), [])
    assign(ref(ref(e.get('_level0'), 'endGameMC').get(), 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(e.get('_level0'), 'endGameMC').get()]))
    rt.call_ref(ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'sound').get(), 'attachSound'), ['Score counter.Mp3'])
    rt.call_ref(ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'sound').get(), 'start'), [0, 9999])
    assign(ref(ref(e.get('_level0'), 'endGameMC').get(), 'cur_sequence'), '=', lambda: 1)
    assign(ref(ref(e.get('_level0'), 'endGameMC').get(), 'winloose'), '=', lambda: e.get('a_status'))
    assign(ref(ref(e.get('_level0'), 'endGameMC').get(), 'count1'), '=', lambda: 0)
    assign(ref(ref(e.get('_level0'), 'endGameMC').get(), 'count2'), '=', lambda: 0)
    if truth(unary('!', ref(ref(this, 'model').get(), 'corrupt_highscore').get())):
        assign(ref(ref(e.get('_level0'), 'endGameMC').get(), 'onEnterFrame'), '=', lambda: ASFunction(f_24, e))
    else:
        assign(ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'txt2').get(), 'text'), '=', lambda: '!!CHEATED!!')
    if truth(ref(ref(e.get('_global'), 'model').get(), 'zs66hj8s').get()):
        assign(ref(ref(ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'demo_MC').get(), 'txtMC_buy').get(), 'txt').get(), 'text'), '=', lambda: 'BUY FULL VERSION')
        assign(ref(ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'demo_MC').get(), 'btn_buy').get(), 'onPress'), '=', lambda: ASFunction(f_28, e))
    else:
        assign(ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'demo_MC').get(), '_visible'), '=', lambda: False)
    assign(ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'btn_website').get(), 'onPress'), '=', lambda: ASFunction(f_29, e))
    assign(ref(ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'txtMC_website').get(), 'txt').get(), 'text'), '=', lambda: 'Website')
    assign(ref(ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'txtMC_new').get(), 'txt').get(), 'text'), '=', lambda: 'New Game')
    assign(ref(ref(ref(e.get('_level0'), 'endGameMC').get(), 'btn_new').get(), 'onPress'), '=', lambda: ASFunction(f_30, e))
    return U

def View_setMapFrames(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', 'i'], closure, 'View')
    e.set('_loc2_', 0)
    while truth(binop('<', e.get('_loc2_'), 6)):
        rt.tick()
        try:
            rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', 'land0', e.get('_loc2_'))).get(), 'gotoAndStop'), [1])
            rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', 'water_overlay_', e.get('_loc2_'))).get(), 'gotoAndStop'), [2])
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_31 in keys(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_31)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), e.get('i')).get())
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(this, 'battleSrcMC').get(), binop('+', 'land0', ref(e.get('_loc3_'), 'mapSide').get())).get())
            rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', 'land0', ref(e.get('_loc3_'), 'mapSide').get())).get(), 'gotoAndStop'), [ref(e.get('_loc3_'), 'religion_code').get()])
            rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', 'water_overlay_', ref(e.get('_loc3_'), 'mapSide').get())).get(), 'gotoAndStop'), [1])
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def View_setFaceFrames(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', 'i'], closure, 'View')
    e.set('_loc2_', 0)
    while truth(binop('<', e.get('_loc2_'), 6)):
        rt.tick()
        try:
            rt.call_ref(ref(ref(ref(this, 'srcMC').get(), binop('+', 'face', e.get('_loc2_'))).get(), 'gotoAndStop'), ['empty'])
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    for key_32 in keys(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_32)
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), e.get('i')).get())
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(this, 'srcMC').get(), binop('+', 'face', ref(e.get('_loc3_'), 'playerNum').get())).get())
            rt.call_ref(ref(e.get('_loc4_'), 'gotoAndStop'), [ref(e.get('_loc3_'), 'faceFrame').get()])
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def View_playSubMC(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_obj'], ['_loc3_', '_loc4_', '_obj'], closure, 'View')
    assign(ref(ref(e.get('_global'), 'model').get(), 'cur_sub_launch_num'), '=', lambda: ref(e.get('_obj'), '_player').get())
    e.set('_loc3_', ref(ref(ref(this, 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'sub_', ref(e.get('_obj'), '_locPlr').get()), '_'), ref(e.get('_obj'), '_locPos').get())).get(), 'tintMC').get())
    e.set('_loc4_', rt.construct(e.get('Color'), [e.get('_loc3_')]))
    rt.call_ref(ref(e.get('_loc4_'), 'setTransform'), [ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_obj'), '_player').get()).get(), 'playerColorTint1').get()])
    rt.call_ref(ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'sub_', ref(e.get('_obj'), '_locPlr').get()), '_'), ref(e.get('_obj'), '_locPos').get())).get(), 'subMC').get(), 'play'), [])
    rt.call_ref(ref(e.get('_loc3_'), 'play'), [])
    rt.call_ref(ref(e.get('_global'), 'play_sound_by_event'), ['sub_surface', ref(e.get('_loc3_'), '_x').get()])
    return U

def View_playCarrierMC(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_obj'], ['_loc3_', '_obj'], closure, 'View')
    if truth(ref(e.get('_obj'), '_locPlr').get()):
        rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', 'carrier', ref(e.get('_obj'), '_locPlr').get())).get(), 'gotoAndStop'), [2])
    if truth(logical('||', ref(e.get('_obj'), '_player').get(), lambda: binop('==', ref(e.get('_obj'), '_player').get(), 0))):
        rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', 'carrier', ref(e.get('_obj'), '_player').get())).get(), 'gotoAndStop'), [2])
    e.set('_loc3_', rt.construct(e.get('Color'), [ref(ref(ref(ref(this, 'battleSrcMC').get(), binop('+', 'carrier', ref(e.get('_obj'), '_player').get())).get(), 'mc').get(), 'carrier_tint').get()]))
    rt.call_ref(ref(e.get('_loc3_'), 'setTransform'), [ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_obj'), '_player').get()).get(), 'playerColorTint1').get()])
    return U

def View_reset_schemeMC(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'View')
    rt.call_ref(ref(ref(ref(ref(this, 'battleSrcMC').get(), 'curActionDisplay').get(), 'schemeMC').get(), 'gotoAndStop'), [2])
    rt.call_ref(ref(ref(ref(ref(this, 'battleSrcMC').get(), 'curActionDisplay').get(), 'schemeMC').get(), 'gotoAndStop'), [1])
    e.set('_loc2_', 0)
    while truth(binop('<', e.get('_loc2_'), 5)):
        rt.tick()
        try:
            if truth(unary('!', ref(ref(ref(ref(this, 'model').get(), 'playerArr').get(), e.get('_loc2_')).get(), 'alive').get())):
                assign(ref(ref(ref(ref(ref(this, 'battleSrcMC').get(), 'curActionDisplay').get(), 'schemeMC').get(), binop('+', 'mc', e.get('_loc2_'))).get(), '_alpha'), '=', lambda: 30)
            else:
                assign(ref(ref(ref(ref(ref(this, 'battleSrcMC').get(), 'curActionDisplay').get(), 'schemeMC').get(), binop('+', 'mc', e.get('_loc2_'))).get(), '_alpha'), '=', lambda: 100)
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def View_curActionText(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str', '_plrNum'], ['_loc4_', '_plrNum', '_str'], closure, 'View')
    switch_33 = e.get('_str')
    case_34 = -1
    if case_34 == -1 and strict_eq(switch_33, 'factory'):
        case_34 = 0
    if case_34 == -1 and strict_eq(switch_33, 'silo'):
        case_34 = 1
    if case_34 == -1 and strict_eq(switch_33, 'airfield'):
        case_34 = 2
    if case_34 == -1 and strict_eq(switch_33, 'Air_still'):
        case_34 = 3
    if case_34 == -1 and strict_eq(switch_33, 'antiRocket_still'):
        case_34 = 4
    if case_34 == -1:
        case_34 = -1
    try:
        if 0 <= case_34 <= 0:
            assign(e.ref('_str'), '=', lambda: 'production')
            raise ASBreak()
        if 0 <= case_34 <= 1:
            pass
        if 0 <= case_34 <= 2:
            pass
        if 0 <= case_34 <= 3:
            pass
        if 0 <= case_34 <= 4:
            pass
    except ASBreak:
        pass
    if truth(binop('!=', e.get('_str'), ref(this, 'cur_actionDisplay_frame').get())):
        assign(ref(this, 'cur_actionDisplay_frame'), '=', lambda: e.get('_str'))
        rt.call_ref(ref(this, 'reset_schemeMC'), [])
    if truth(binop('!=', e.get('_str'), 'none')):
        if truth(binop('<', ref(ref(ref(this, 'battleSrcMC').get(), 'curActionDisplay').get(), '_alpha').get(), 20)):
            rt.call_ref(ref(this, 'fadeClip'), [ref(ref(this, 'battleSrcMC').get(), 'curActionDisplay').get(), 80, 'in', 20, False])
        rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), 'curActionDisplay').get(), 'gotoAndStop'), [e.get('_str')])
    else:
        rt.call_ref(ref(ref(ref(this, 'battleSrcMC').get(), 'curActionDisplay').get(), 'gotoAndStop'), [1])
        rt.call_ref(ref(this, 'fadeClip'), [ref(ref(this, 'battleSrcMC').get(), 'curActionDisplay').get(), 0, 'out', 20, False])
    rt.call_ref(ref(ref(ref(ref(ref(this, 'battleSrcMC').get(), 'curActionDisplay').get(), 'schemeMC').get(), binop('+', 'mc', e.get('_plrNum'))).get(), 'gotoAndStop'), [2])
    rt.call_ref(ref(ref(ref(ref(ref(this, 'battleSrcMC').get(), 'curActionDisplay').get(), 'schemeMC').get(), binop('+', 'mc', e.get('_plrNum'))).get(), 'gotoAndStop'), [1])
    e.set('_loc4_', rt.construct(e.get('Color'), [ref(ref(ref(ref(this, 'battleSrcMC').get(), 'curActionDisplay').get(), 'schemeMC').get(), binop('+', 'mc', e.get('_plrNum'))).get()]))
    rt.call_ref(ref(e.get('_loc4_'), 'setTransform'), [ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), e.get('_plrNum')).get(), 'playerColorTint1').get()])
    return U

def View_updateAnti(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['unit'], ['_loc3_', '_loc4_', '_loc5_', 'unit'], closure, 'View')
    if truth(unary('!', ref(e.get('unit'), 'anti_mc_name').get())):
        assign(ref(e.get('unit'), 'anti_mc_name'), '=', lambda: binop('+', binop('+', binop('+', 'ab', ref(e.get('unit'), 'anti_num').get()), '_'), ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('unit'), 'targetPlayer').get()).get(), 'anti_loc').get()))
    if truth(unary('!', ref(e.get('unit'), 'anti_active').get())):
        return e.get('undefined')
    e.set('_loc3_', ref(ref(ref(ref(this, 'battleSrcMC').get(), ref(e.get('unit'), 'anti_mc_name').get()).get(), 'mc').get(), 'mc').get())
    e.set('_loc4_', ref(e.get('_loc3_'), '_currentframe').get())
    e.set('_loc5_', ref(e.get('unit'), 'anti_direction').get())
    if truth(binop('!=', ref(e.get('_loc3_'), '_currentframe').get(), e.get('_loc5_'))):
        rt.call_ref(ref(e.get('unit'), 'sound_anti'), ['move'])
    rt.call_ref(ref(e.get('_loc3_'), 'gotoAndPlay'), [binop('-', binop('*', e.get('_loc5_'), 2), 1)])
    if truth(binop('<', ref(e.get('unit'), 'anti_distance').get(), 170)):
        if truth(binop('==', ref(e.get('unit'), 'anti_offset').get(), 1)):
            assign(ref(e.get('unit'), 'anti_offset'), '=', lambda: 2)
        else:
            assign(ref(e.get('unit'), 'anti_offset'), '=', lambda: 1)
    if truth(binop('==', ref(e.get('unit'), 'anti_offset').get(), 1)):
        rt.call_ref(ref(e.get('_loc3_'), 'nextFrame'), [])
        rt.call_ref(ref(e.get('unit'), 'sound_anti_shoot'), [e.get('_loc3_')])
    if truth(binop('<=', ref(e.get('unit'), 'countDown_antiStart').get(), 0)):
        if truth(binop('<', ref(e.get('_loc3_'), '_alpha').get(), 100)):
            assign(ref(e.get('_loc3_'), '_alpha'), '+=', lambda: 10)
    else:
        assign(ref(e.get('unit'), 'countDown_antiStart'), '=', lambda: binop('-', ref(e.get('unit'), 'countDown_antiStart').get(), 1))
    if truth(logical('||', binop('==', ref(e.get('unit'), 'unitStatus').get(), 'dead'), lambda: unary('!', e.get('unit')))):
        if truth(binop('==', binop('/', ref(e.get('_loc3_'), '_currentframe').get(), rt.call_ref(ref(e.get('Math'), 'floor'), [binop('/', ref(e.get('_loc3_'), '_currentframe').get(), 2)])), 2)):
            rt.call_ref(ref(e.get('_loc3_'), 'prevFrame'), [])
    return U

def View_createBioCloud(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['city'], ['_loc4_', '_loc5_', 'city', 'i'], closure, 'View')
    assign(ref(e.get('city'), 'bioloaded'), '=', lambda: True)
    if truth(unary('!', ref(ref(e.get('city'), 'image').get(), 'bioCloud_container').get())):
        assign(ref(e.get('city'), 'bioCloud_container'), '=', lambda: rt.call_ref(ref(ref(e.get('city'), 'image').get(), 'createEmptyMovieClip'), ['bioCloud_container', rt.call_ref(ref(ref(e.get('city'), 'image').get(), 'getNextHighestDepth'), [])]))
        assign(ref(ref(e.get('city'), 'bioCloud_container').get(), 'city'), '=', lambda: e.get('city'))
        assign(e.ref('_loc4_'), '=', lambda: 0)
        while truth(binop('<', e.get('_loc4_'), ref(this, 'cloudMax').get())):
            rt.tick()
            try:
                rt.call_ref(ref(ref(e.get('city'), 'bioCloud_arr').get(), 'push'), [rt.call_ref(ref(ref(e.get('city'), 'bioCloud_container').get(), 'attachMovie'), ['bioCloud', binop('+', 'bioCloud_', e.get('_loc4_')), rt.call_ref(ref(ref(ref(e.get('city'), 'image').get(), 'bioCloud_container').get(), 'getNextHighestDepth'), [])])])
                assign(e.ref('_loc4_'), '=', lambda: binop('+', e.get('_loc4_'), 1))
            except ASContinue:
                pass
            except ASBreak:
                break
        for key_35 in keys(ref(e.get('city'), 'bioCloud_arr').get()):
            e.ref('i').set(key_35)
            rt.tick()
            try:
                assign(e.ref('_loc5_'), '=', lambda: ref(ref(e.get('city'), 'bioCloud_arr').get(), e.get('i')).get())
                rt.call_ref(ref(e.get('_loc5_'), 'spawn'), [])
            except ASContinue:
                pass
            except ASBreak:
                break
    return U

def View_createClouds(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_'], closure, 'View')
    e.set('_loc3_', 0)
    while truth(binop('<', e.get('_loc3_'), ref(this, 'cloudPacks').get())):
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc4_'), ref(this, 'cloudMax').get())):
                rt.tick()
                try:
                    assign(e.ref('_loc2_'), '=', lambda: rt.call_ref(ref(ref(this, 'battleSrcMC').get(), 'attachMovie'), ['cloud', binop('+', binop('+', binop('+', 'cloud', e.get('_loc3_')), '_'), e.get('_loc4_')), rt.call_ref(ref(ref(this, 'battleSrcMC').get(), 'getNextHighestDepth'), [])]))
                    assign(ref(e.get('_loc2_'), 'startLoc'), '=', lambda: obj({'_x': binop('+', ref(ref(ref(this, 'cloudCenterPositions').get(), e.get('_loc3_')).get(), 0).get(), rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [unary('-', 30), 30])), '_y': binop('+', ref(ref(ref(this, 'cloudCenterPositions').get(), e.get('_loc3_')).get(), 1).get(), rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [unary('-', 30), 30]))}))
                    rt.call_ref(ref(e.get('_loc2_'), 'initialLoc'), [])
                    assign(ref(e.get('_loc2_'), '_alpha'), '=', lambda: 30)
                    assign(ref(e.get('_loc2_'), '_xscale'), '=', lambda: assign(ref(e.get('_loc2_'), '_yscale'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [800, 1100])))
                    assign(ref(e.get('_loc2_'), 'xRadius'), '=', lambda: assign(ref(e.get('_loc2_'), 'yRadius'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [10, 30])))
                    assign(ref(e.get('_loc2_'), 'angleChange'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [unary('-', 9), 9]))
                    rt.call_ref(ref(ref(this, 'cloudArr').get(), 'push'), [e.get('_loc2_')])
                    assign(e.ref('_loc4_'), '=', lambda: binop('+', e.get('_loc4_'), 1))
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

def View_cloud_interval_func(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', 'i'], closure, 'View')
    for key_36 in keys(ref(this, 'cloudArr').get()):
        e.ref('i').set(key_36)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(this, 'cloudArr').get(), e.get('i')).get())
            rt.call_ref(ref(e.get('_loc2_'), 'frame_step'), [])
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def View_cloudTicker_initiate(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View')
    if truth(unary('!', ref(ref(this, 'cloudArr').get(), 0).get())):
        rt.call_ref(ref(this, 'createClouds'), [])
        assign(ref(this, 'cloudIntervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'cloud_interval_func', 3500]))
    return U

def f_37(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc14_', '_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', 'i'], closure, None)
    assign(ref(this, 'ticker_count'), '=', lambda: binop('+', ref(this, 'ticker_count').get(), 1))
    if truth(logical('||', logical('&&', binop('==', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'battle').get(), '_activeUnitsArr').get(), 'length').get(), 0), lambda: binop('==', ref(ref(ref(e.get('_global'), 'model').get(), 'attackingSubs_arr').get(), 'length').get(), 0)), lambda: binop('>', ref(this, 'ticker_count').get(), 800))):
        if truth(unary('!', rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'check_ch_active'), ['kill_all']))):
            ref(ref(ref(e.get('_global'), 'view').get(), 'battleSrcMC').get(), 'onEnterFrame').delete()
            rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID').get()])
            assign(ref(ref(e.get('_global'), 'presenter').get(), 'allUnitsDone_intervalID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [ref(e.get('_global'), 'presenter').get(), 'allUnitsDone', 2500]))
            return e.get('undefined')
    else:
        if truth(ref(ref(e.get('_global'), 'model').get(), 'battleMC_units_active').get()):
            if truth(binop('<=', ref(ref(e.get('_global'), 'model').get(), 'battleCounter').get(), 0)):
                if truth(unary('!', ref(ref(e.get('_global'), 'model').get(), 'lastUnitWasBuilding').get())):
                    assign(ref(ref(e.get('_global'), 'model').get(), 'battleCounter'), '=', lambda: 1)
                    ref(ref(ref(e.get('_global'), 'model').get(), 'battleTimerArr').get(), ref(ref(e.get('_global'), 'model').get(), 'battleTimerIndex').get()).get()
                    update(ref(ref(e.get('_global'), 'model').get(), 'unitStartNum'), 1, False)
                else:
                    assign(ref(ref(e.get('_global'), 'model').get(), 'battleCounter'), '=', lambda: 1)
                    update(ref(ref(e.get('_global'), 'model').get(), 'unitStartNum'), 1, False)
            update(ref(ref(e.get('_global'), 'model').get(), 'battleCounter'), -1, False)
        for key_38 in keys(ref(ref(ref(e.get('_global'), 'model').get(), 'battle').get(), '_activeUnitsArr').get()):
            e.ref('i').set(key_38)
            rt.tick()
            try:
                assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(ref(e.get('_global'), 'model').get(), 'battle').get(), '_activeUnitsArr').get(), e.get('i')).get())
                if truth(unary('!', ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'battle').get(), '_activeUnitsArr').get(), e.get('i')).get(), '_building').get())):
                    if truth(logical('&&', unary('!', ref(e.get('_loc2_'), 'tail').get()), lambda: logical('&&', binop('==', ref(e.get('_loc2_'), 'startNum').get(), ref(ref(e.get('_global'), 'model').get(), 'unitStartNum').get()), lambda: logical('&&', unary('!', ref(e.get('_loc2_'), 'activeAndMoving').get()), lambda: binop('!=', ref(e.get('_loc2_'), 'action').get(), 'stop'))))):
                        rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'curActionText'), ['none'])
                        assign(ref(e.get('_loc2_'), 'activeAndMoving'), '=', lambda: True)
                        if truth(ref(e.get('_loc2_'), 'startSoundOnAAM').get()):
                            rt.call_ref(ref(e.get('_loc2_'), 'startSound'), [])
                        assign(ref(ref(e.get('_global'), 'model').get(), 'lastUnitWasBuilding'), '=', lambda: False)
                    if truth(logical('||', binop('==', ref(e.get('_loc2_'), 'unitStatus').get(), 'dead'), lambda: binop('==', ref(e.get('_loc2_'), 'action').get(), 'stop'))):
                        if truth(binop('==', ref(e.get('_loc2_'), 'mcID').get(), 'boat001')):
                            rt.call_ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'gotoAndStop'), [6])
                        rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'battle').get(), '_toDeleteUnitsArr').get(), 'push'), [e.get('_loc2_')])
                        rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'battle').get(), '_activeUnitsArr').get(), 'splice'), [e.get('i'), 1])
                        if truth(logical('||', binop('==', ref(e.get('_loc2_'), 'mcID').get(), 'marine'), lambda: binop('==', ref(e.get('_loc2_'), 'mcID').get(), 'soldier001'))):
                            assign(ref(e.get('_loc2_'), 'activeAndMoving'), '=', lambda: False)
                            return e.get('undefined')
                    if truth(binop('==', ref(e.get('_loc2_'), 'action').get(), 'die')):
                        rt.call_ref(ref(e.get('_loc2_'), 'killUnit'), [])
                    if truth(binop('==', ref(e.get('_loc2_'), 'action').get(), 'dying')):
                        if truth(binop('==', ref(ref(e.get('_loc2_'), 'shadowMC').get(), '_x').get(), 0)):
                            pass
                    if truth(logical('&&', ref(e.get('_loc2_'), 'activeAndMoving').get(), lambda: ref(ref(e.get('_loc2_'), 'wildCard').get(), 'satellite').get())):
                        rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'play_satellite_sound'), [])
                        if truth(binop('<', ref(ref(e.get('_loc2_'), 'MC').get(), '_x').get(), ref(ref(e.get('_loc2_'), 'wildCard').get(), 'targetX').get())):
                            assign(ref(e.get('_loc2_'), 'curX'), '+=', lambda: 3)
                            assign(ref(e.get('_loc2_'), 'curY'), '=', lambda: binop('+', ref(e.get('_loc2_'), 'curY').get(), 1))
                            rt.call_ref(ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'mc').get(), 'gotoAndStop'), [rt.call_ref(ref(e.get('Math'), 'round'), [binop('/', ref(ref(e.get('_loc2_'), 'MC').get(), '_x').get(), 26)])])
                        else:
                            if truth(logical('&&', binop('!=', ref(e.get('_loc2_'), 'action').get(), 'fire'), lambda: logical('&&', binop('!=', ref(e.get('_loc2_'), 'action').get(), 'idle'), lambda: binop('!=', ref(e.get('_loc2_'), 'action').get(), 'firing_clear')))):
                                assign(ref(e.get('_loc2_'), 'action'), '=', lambda: 'fire')
                                rt.call_ref(ref(e.get('_loc2_'), 'satellite_explosion'), [])
                            else:
                                if truth(binop('==', ref(e.get('_loc2_'), 'action').get(), 'fire')):
                                    rt.call_ref(ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'mc').get(), 'clear'), [])
                                    if truth(unary('!', ref(e.get('_loc2_'), 'has_fired_laser_sound').get())):
                                        rt.call_ref(ref(e.get('_loc2_'), 'soundAction'), ['sat_laser'])
                                        assign(ref(e.get('_loc2_'), 'has_fired_laser_sound'), '=', lambda: True)
                                    assign(ref(e.get('_loc2_'), 'satellite_lineAlpha'), '=', lambda: ref(e.get('_loc2_'), 'satellite_lineAlphaStart').get())
                                    if truth(logical('&&', binop('<', ref(e.get('_loc2_'), 'satellite_lineAlphaStart').get(), 100), lambda: ref(e.get('_loc2_'), 'satellite_alphaPlus').get())):
                                        assign(ref(e.get('_loc2_'), 'satellite_lineAlphaStart'), '+=', lambda: 15)
                                    else:
                                        if truth(binop('>=', ref(e.get('_loc2_'), 'satellite_lineAlphaStart').get(), 100)):
                                            assign(ref(e.get('_loc2_'), 'satellite_alphaPlus'), '=', lambda: False)
                                    if truth(unary('!', ref(e.get('_loc2_'), 'satellite_alphaPlus').get())):
                                        assign(ref(e.get('_loc2_'), 'satellite_lineAlphaStart'), '-=', lambda: 5)
                                        if truth(binop('<=', ref(e.get('_loc2_'), 'satellite_lineAlphaStart').get(), 0)):
                                            assign(ref(e.get('_loc2_'), 'action'), '=', lambda: 'stop')
                                            raise ASBreak()
                                    assign(ref(e.get('_loc2_'), 'satellite_line_xOffset'), '=', lambda: unary('-', 4))
                                    assign(ref(e.get('_loc2_'), 'satellite_line_xLocation'), '=', lambda: binop('-', binop('-', ref(ref(e.get('_loc2_'), 'wildCard').get(), 'cityX').get(), ref(ref(e.get('_loc2_'), 'MC').get(), '_x').get()), ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'mc').get(), '_x').get()))
                                    assign(ref(e.get('_loc2_'), 'satellite_line_yLocation'), '=', lambda: binop('-', binop('-', ref(ref(e.get('_loc2_'), 'wildCard').get(), 'cityY').get(), ref(ref(e.get('_loc2_'), 'MC').get(), '_y').get()), ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'mc').get(), '_y').get()))
                                    assign(e.ref('_loc3_'), '=', lambda: ref(ref(e.get('_loc2_'), 'wildCard').get(), 'laser_hex_color').get())
                                    assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'brighter_hex_by_steps'), [e.get('_loc3_'), 2]))
                                    assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'brighter_hex_by_steps'), [e.get('_loc4_'), 2]))
                                    assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'brighter_hex_by_steps'), [e.get('_loc5_'), 3]))
                                    assign(e.ref('_loc7_'), '=', lambda: rt.construct(e.get('Array'), [e.get('_loc4_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc6_'), '0xFFFFFF', '0xFFFFFF', '0xFFFFFF']))
                                    assign(e.ref('_loc8_'), '=', lambda: 0)
                                    while truth(binop('<', e.get('_loc8_'), 4)):
                                        rt.tick()
                                        try:
                                            assign(e.ref('_loc9_'), '=', lambda: ref(ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'mc').get(), 'laserStartMC').get(), '_x').get())
                                            assign(e.ref('_loc10_'), '=', lambda: ref(ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'mc').get(), 'laserStartMC').get(), '_y').get())
                                            rt.call_ref(ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'mc').get(), 'moveTo'), [e.get('_loc9_'), binop('-', e.get('_loc10_'), e.get('_loc8_'))])
                                            rt.call_ref(ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'mc').get(), 'lineStyle'), [1, e.call('Number', [ref(e.get('_loc7_'), binop('-', 6, e.get('_loc8_'))).get()]), ref(e.get('_loc2_'), 'satellite_lineAlpha').get()])
                                            rt.call_ref(ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'mc').get(), 'lineTo'), [binop('+', ref(e.get('_loc2_'), 'satellite_line_xLocation').get(), e.get('_loc8_')), binop('-', ref(e.get('_loc2_'), 'satellite_line_yLocation').get(), e.get('_loc8_'))])
                                            rt.call_ref(ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'mc').get(), 'moveTo'), [e.get('_loc9_'), binop('+', e.get('_loc10_'), e.get('_loc8_'))])
                                            rt.call_ref(ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'mc').get(), 'lineStyle'), [1, e.call('Number', [ref(e.get('_loc7_'), binop('-', 6, e.get('_loc8_'))).get()]), ref(e.get('_loc2_'), 'satellite_lineAlpha').get()])
                                            rt.call_ref(ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'mc').get(), 'lineTo'), [ref(e.get('_loc2_'), 'satellite_line_xLocation').get(), binop('+', ref(e.get('_loc2_'), 'satellite_line_yLocation').get(), e.get('_loc8_'))])
                                            assign(ref(ref(e.get('_loc2_'), 'MC').get(), 'lineAlpha'), '-=', lambda: 15)
                                            assign(e.ref('_loc8_'), '=', lambda: binop('+', e.get('_loc8_'), 1))
                                        except ASContinue:
                                            pass
                                        except ASBreak:
                                            break
                                    if truth(binop('>=', ref(e.get('_loc2_'), 'satellite_line_xOffset').get(), 4)):
                                        assign(ref(e.get('_loc2_'), 'satellite_line_xOffset'), '=', lambda: unary('-', 4))
                                    else:
                                        assign(ref(e.get('_loc2_'), 'satellite_line_xOffset'), '=', lambda: binop('+', ref(e.get('_loc2_'), 'satellite_line_xOffset').get(), 1))
                    if truth(logical('&&', binop('==', ref(e.get('_loc2_'), 'action').get(), 'waitForLiftOff'), lambda: ref(e.get('_loc2_'), 'activeAndMoving').get())):
                        update(ref(ref(e.get('_loc2_'), 'wildCard').get(), 'liftOffCount'), 1, False)
                        if truth(binop('>=', e.call('Number', [ref(ref(e.get('_loc2_'), 'wildCard').get(), 'liftOffCount').get()]), e.call('Number', [binop('*', ref(ref(e.get('_loc2_'), 'wildCard').get(), '_number').get(), 20)]))):
                            assign(ref(e.get('_loc2_'), 'action'), '=', lambda: 'liftOff')
                    else:
                        if truth(logical('&&', binop('==', ref(e.get('_loc2_'), 'mcID').get(), 'sub_rocket'), lambda: binop('==', ref(e.get('_loc2_'), 'action').get(), 'wait_for_sub_launch'))):
                            if truth(binop('==', ref(ref(e.get('_global'), 'model').get(), 'cur_sub_launch_num').get(), ref(ref(e.get('_loc2_'), 'wildCard').get(), 'sub_launch_num').get())):
                                assign(ref(e.get('_loc2_'), 'action'), '=', lambda: 'sub_rocket_countDown_1')
                        else:
                            if truth(binop('==', ref(e.get('_loc2_'), 'action').get(), 'sub_rocket_countDown_1')):
                                if truth(binop('>', ref(e.get('_loc2_'), 'sub_launch_timer').get(), 34)):
                                    assign(ref(e.get('_loc2_'), 'action'), '=', lambda: 'sub_rocket_launch')
                                assign(ref(e.get('_loc2_'), 'sub_launch_timer'), '=', lambda: binop('+', ref(e.get('_loc2_'), 'sub_launch_timer').get(), 1))
                            else:
                                rt.call_ref(ref(e.get('_loc2_'), 'moveUnit'), [])
                                assign(ref(ref(e.get('_loc2_'), 'MC').get(), '_y'), '=', lambda: ref(e.get('_loc2_'), 'curY').get())
                                assign(ref(ref(e.get('_loc2_'), 'MC').get(), '_x'), '=', lambda: ref(e.get('_loc2_'), 'curX').get())
                                if truth(logical('&&', binop('<', ref(ref(e.get('_loc2_'), 'MC').get(), '_xscale').get(), 100), lambda: logical('&&', ref(e.get('_loc2_'), 'activeAndMoving').get(), lambda: logical('&&', unary('!', ref(e.get('_loc2_'), 'scale_down').get()), lambda: logical('&&', unary('!', ref(e.get('_loc2_'), 'scale_up').get()), lambda: logical('&&', binop('!=', ref(e.get('_loc2_'), 'action').get(), 'taxi_a'), lambda: logical('&&', binop('!=', ref(e.get('_loc2_'), 'action').get(), 'taxi_b'), lambda: logical('&&', binop('!=', ref(e.get('_loc2_'), 'mcID').get(), 'ship_plane'), lambda: logical('||', logical('&&', binop('!=', ref(e.get('_loc2_'), 'mcID').get(), 'plane001'), lambda: binop('!=', ref(e.get('_loc2_'), 'mcID').get(), 'plane002')), lambda: binop('<=', ref(e.get('_loc2_'), 'PLANE_COUNT_TO_FREE_FLIGHT').get(), ref(e.get('_loc2_'), 'cur_count_to_free_flight').get())))))))))):
                                    if truth(logical('&&', logical('||', binop('==', ref(e.get('_loc2_'), 'mcID').get(), 'plane001'), lambda: binop('==', ref(e.get('_loc2_'), 'mcID').get(), 'plane002')), lambda: binop('<', ref(ref(e.get('_loc2_'), 'MC').get(), '_xscale').get(), 80))):
                                        assign(ref(ref(e.get('_loc2_'), 'MC').get(), '_xscale'), '+=', lambda: 2)
                                        assign(ref(ref(e.get('_loc2_'), 'MC').get(), '_yscale'), '+=', lambda: 2)
                                        if truth(ref(e.get('_loc2_'), 'hasShadow').get()):
                                            assign(ref(ref(e.get('_loc2_'), 'shadowMC').get(), '_xscale'), '+=', lambda: 2)
                                            assign(ref(ref(e.get('_loc2_'), 'shadowMC').get(), '_yscale'), '+=', lambda: 2)
                                        if truth(ref(e.get('_loc2_'), 'tintMC_id').get()):
                                            assign(ref(ref(e.get('_loc2_'), 'tintMC').get(), '_xscale'), '=', lambda: assign(ref(ref(e.get('_loc2_'), 'tintMC').get(), '_yscale'), '=', lambda: ref(ref(e.get('_loc2_'), 'MC').get(), '_xscale').get()))
                                if truth(logical('&&', ref(e.get('_loc2_'), 'scale_up').get(), lambda: logical('&&', binop('>', ref(ref(e.get('_loc2_'), 'MC').get(), '_xscale').get(), 50), lambda: ref(e.get('_loc2_'), 'activeAndMoving').get()))):
                                    assign(ref(ref(e.get('_loc2_'), 'MC').get(), '_xscale'), '-=', lambda: 1)
                                if truth(logical('&&', ref(e.get('_loc2_'), 'scale_down').get(), lambda: logical('&&', binop('<', ref(ref(e.get('_loc2_'), 'MC').get(), '_xscale').get(), 100), lambda: ref(e.get('_loc2_'), 'activeAndMoving').get()))):
                                    assign(ref(ref(e.get('_loc2_'), 'MC').get(), '_xscale'), '+=', lambda: 2)
                                if truth(logical('&&', binop('<', ref(ref(e.get('_loc2_'), 'MC').get(), '_alpha').get(), 100), lambda: logical('&&', ref(e.get('_loc2_'), 'activeAndMoving').get(), lambda: binop('!=', ref(e.get('_loc2_'), 'mcID').get(), 'suicide_bomber')))):
                                    assign(ref(ref(e.get('_loc2_'), 'MC').get(), '_alpha'), '+=', lambda: 10)
                                    if truth(unary('!', ref(e.get('_loc2_'), 'tintMC_id').get())):
                                        pass
                                if truth(logical('&&', binop('==', ref(e.get('_loc2_'), 'mcID').get(), 'ship_plane'), lambda: logical('&&', binop('<', ref(ref(e.get('_loc2_'), 'MC').get(), '_xscale').get(), 70), lambda: binop('!=', ref(e.get('_loc2_'), 'action').get(), 'waitForLiftOff')))):
                                    update(ref(ref(e.get('_loc2_'), 'MC').get(), '_xscale'), 1, False)
                                    update(ref(ref(e.get('_loc2_'), 'MC').get(), '_yscale'), 1, False)
                                    update(ref(ref(e.get('_loc2_'), 'tintMC').get(), '_xscale'), 1, False)
                                    update(ref(ref(e.get('_loc2_'), 'tintMC').get(), '_yscale'), 1, False)
                                    update(ref(ref(e.get('_loc2_'), 'shadowMC').get(), '_xscale'), 1, False)
                                    update(ref(ref(e.get('_loc2_'), 'shadowMC').get(), '_yscale'), 1, False)
                    if truth(binop('==', ref(e.get('_loc2_'), 'action').get(), 'waitForHeliStart')):
                        if truth(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'heliStart').get(), ref(e.get('_loc2_'), 'playerNum').get()).get(), 0).get()):
                            assign(ref(ref(e.get('_loc2_'), 'MC').get(), '_x'), '=', lambda: assign(ref(e.get('_loc2_'), 'curX'), '=', lambda: binop('+', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'heliStart').get(), ref(e.get('_loc2_'), 'playerNum').get()).get(), 0).get(), ref(e.get('_loc2_'), 'heliStartPlusX').get())))
                            assign(ref(ref(e.get('_loc2_'), 'MC').get(), '_y'), '=', lambda: assign(ref(e.get('_loc2_'), 'curY'), '=', lambda: binop('+', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'heliStart').get(), ref(e.get('_loc2_'), 'playerNum').get()).get(), 1).get(), ref(e.get('_loc2_'), 'heliStartPlusY').get())))
                            if truth(binop('!=', ref(e.get('_loc2_'), 'mcID').get(), 'suicide_bomber')):
                                assign(ref(e.get('_loc2_'), 'action'), '=', lambda: 'liftOff')
                            else:
                                if truth(binop('==', ref(e.get('_loc2_'), 'mcID').get(), 'suicide_bomber')):
                                    assign(ref(e.get('_loc2_'), 'action'), '=', lambda: 'suicide_fade_out')
                                    assign(ref(ref(ref(e.get('_loc2_'), 'wayPointArr').get(), 0).get(), '_x'), '=', lambda: ref(ref(ref(ref(e.get('_global'), 'model').get(), 'heliStart').get(), ref(e.get('_loc2_'), 'playerNum').get()).get(), 0).get())
                                    assign(ref(ref(ref(e.get('_loc2_'), 'wayPointArr').get(), 0).get(), '_y'), '=', lambda: binop('-', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'heliStart').get(), ref(e.get('_loc2_'), 'playerNum').get()).get(), 1).get(), 70))
                                    assign(ref(ref(ref(e.get('_loc2_'), 'wayPointArr').get(), 1).get(), '_x'), '=', lambda: ref(ref(ref(ref(e.get('_global'), 'model').get(), 'heliStart').get(), ref(e.get('_loc2_'), 'playerNum').get()).get(), 0).get())
                                    assign(ref(ref(ref(e.get('_loc2_'), 'wayPointArr').get(), 1).get(), '_y'), '=', lambda: binop('-', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'heliStart').get(), ref(e.get('_loc2_'), 'playerNum').get()).get(), 1).get(), 70))
                        if truth(binop('==', ref(e.get('_loc2_'), 'mcID').get(), 'suicide_bomber')):
                            rt.call_ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'swapDepths'), [rt.call_ref(ref(ref(e.get('_loc2_'), 'container').get(), 'getNextHighestDepth'), [])])
                    if truth(binop('!=', ref(e.get('_loc2_'), 'action').get(), 'unload')):
                        if truth(binop('==', ref(e.get('_loc2_'), 'action').get(), 'plane_circular_flight')):
                            assign(ref(e.get('_loc2_'), 'plane_circFlight_frames_count'), '=', lambda: binop('+', ref(e.get('_loc2_'), 'plane_circFlight_frames_count').get(), 1))
                        if truth(logical('&&', ref(e.get('_loc2_'), 'multiFrame').get(), lambda: ref(e.get('_loc2_'), 'activeAndMoving').get())):
                            assign(e.ref('_loc11_'), '=', lambda: 0)
                            if truth(binop('==', ref(e.get('_loc2_'), 'action').get(), 'liftOff')):
                                assign(e.ref('_loc11_'), '=', lambda: binop('+', binop('-', binop('*', ref(e.get('_loc2_'), 'fixedFrame').get(), ref(e.get('_loc2_'), 'offsetFrames').get()), binop('-', ref(e.get('_loc2_'), 'offsetFrames').get(), 1)), ref(e.get('_loc2_'), 'frameOffset').get()))
                            else:
                                assign(e.ref('_loc11_'), '=', lambda: binop('+', binop('-', binop('*', ref(e.get('_loc2_'), 'unitDirection').get(), ref(e.get('_loc2_'), 'offsetFrames').get()), binop('-', ref(e.get('_loc2_'), 'offsetFrames').get(), 1)), ref(e.get('_loc2_'), 'frameOffset').get()))
                            rt.call_ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'gotoAndStop'), [e.get('_loc11_')])
                            if truth(binop('<', ref(e.get('_loc2_'), 'frameOffset').get(), ref(e.get('_loc2_'), 'offsetFrames').get())):
                                assign(ref(e.get('_loc2_'), 'frameOffset'), '=', lambda: binop('+', ref(e.get('_loc2_'), 'frameOffset').get(), 1))
                            else:
                                assign(ref(e.get('_loc2_'), 'frameOffset'), '=', lambda: 1)
                        else:
                            if truth(logical('&&', binop('!=', ref(e.get('_loc2_'), 'mcID').get(), 'tankTop'), lambda: logical('&&', binop('!=', ref(e.get('_loc2_'), 'mcID').get(), 'rocket'), lambda: logical('&&', binop('!=', ref(e.get('_loc2_'), 'mcID').get(), 'sub_rocket'), lambda: binop('!=', ref(e.get('_loc2_'), 'action').get(), 'plane_circular_flight'))))):
                                if truth(logical('||', logical('&&', logical('||', binop('==', ref(e.get('_loc2_'), 'mcID').get(), 'soldier001'), lambda: binop('==', ref(e.get('_loc2_'), 'mcID').get(), 'marine')), lambda: ref(e.get('_loc2_'), 'activeAndMoving').get()), lambda: logical('&&', binop('!=', ref(e.get('_loc2_'), 'mcID').get(), 'soldier001'), lambda: binop('!=', ref(e.get('_loc2_'), 'mcID').get(), 'marine')))):
                                    rt.call_ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'gotoAndStop'), [ref(e.get('_loc2_'), 'unitDirection').get()])
                        if truth(logical('&&', binop('==', ref(e.get('_loc2_'), 'action').get(), 'plane_circular_flight'), lambda: binop('>', ref(e.get('_loc2_'), 'plane_circFlight_frames_count').get(), 3))):
                            rt.call_ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'gotoAndStop'), [ref(e.get('_loc2_'), 'unitDirection').get()])
                        else:
                            if truth(logical('||', binop('==', ref(e.get('_loc2_'), 'mcID').get(), 'rocket'), lambda: binop('==', ref(e.get('_loc2_'), 'mcID').get(), 'sub_rocket'))):
                                assign(ref(ref(e.get('_loc2_'), 'MC').get(), '_rotation'), '=', lambda: ref(e.get('_loc2_'), 'rocketRotation').get())
                                if truth(logical('&&', binop('<', ref(e.get('_loc2_'), 'anti_distance').get(), 150), lambda: unary('!', ref(e.get('_loc2_'), 'result').get()))):
                                    assign(ref(e.get('_loc2_'), 'action'), '=', lambda: 'rocket_explode_self')
                                if truth(logical('&&', ref(e.get('_loc2_'), 'anti_active').get(), lambda: logical('&&', ref(e.get('_loc2_'), 'activeAndMoving').get(), lambda: logical('&&', binop('==', ref(ref(e.get('_loc2_'), 'anti_pos').get(), 0).get(), 0), lambda: unary('!', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), 'targetPlayer').get()).get(), 'anti_inBattle_target').get()))))):
                                    assign(ref(ref(e.get('_loc2_'), 'anti_pos').get(), 0), '=', lambda: ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), 'targetPlayer').get()).get(), 'anti_pos_arr').get(), 0).get())
                                    assign(ref(ref(e.get('_loc2_'), 'anti_pos').get(), 1), '=', lambda: ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), 'targetPlayer').get()).get(), 'anti_pos_arr').get(), 1).get())
                                    assign(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), 'targetPlayer').get()).get(), 'anti_inBattle_target'), '=', lambda: e.get('_loc2_'))
                                if truth(logical('&&', binop('==', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), 'targetPlayer').get()).get(), 'anti_inBattle_target').get(), e.get('_loc2_')), lambda: logical('&&', unary('!', ref(e.get('_loc2_'), 'anti_initiated').get()), lambda: logical('&&', ref(e.get('_loc2_'), 'anti_active').get(), lambda: binop('<', ref(e.get('_loc2_'), 'anti_distance').get(), 400))))):
                                    rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'updateAnti'), [e.get('_loc2_')])
                        if truth(binop('==', ref(e.get('_loc2_'), 'mcID').get(), 'ship_plane')):
                            if truth(binop('==', ref(e.get('_loc2_'), 'action').get(), 'waitForLiftOff')):
                                rt.call_ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'gotoAndStop'), [ref(e.get('_loc2_'), 'idleFrame').get()])
                            else:
                                rt.call_ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'gotoAndStop'), [ref(e.get('_loc2_'), 'unitDirection').get()])
                                assign(ref(ref(e.get('_loc2_'), 'shadowMC').get(), '_visible'), '=', lambda: True)
                            if truth(logical('&&', ref(e.get('_loc2_'), 'anti_active').get(), lambda: logical('&&', ref(e.get('_loc2_'), 'activeAndMoving').get(), lambda: logical('&&', binop('==', ref(ref(e.get('_loc2_'), 'anti_pos').get(), 0).get(), 0), lambda: unary('!', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), 'targetPlayer').get()).get(), 'anti_inBattle_target').get()))))):
                                assign(ref(ref(e.get('_loc2_'), 'anti_pos').get(), 0), '=', lambda: ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), 'targetPlayer').get()).get(), 'anti_pos_arr').get(), 0).get())
                                assign(ref(ref(e.get('_loc2_'), 'anti_pos').get(), 1), '=', lambda: ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), 'targetPlayer').get()).get(), 'anti_pos_arr').get(), 1).get())
                                assign(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), 'targetPlayer').get()).get(), 'anti_inBattle_target'), '=', lambda: e.get('_loc2_'))
                            if truth(logical('&&', binop('==', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), 'targetPlayer').get()).get(), 'anti_inBattle_target').get(), e.get('_loc2_')), lambda: logical('&&', unary('!', ref(e.get('_loc2_'), 'anti_initiated').get()), lambda: logical('&&', ref(e.get('_loc2_'), 'anti_active').get(), lambda: binop('<', ref(e.get('_loc2_'), 'anti_distance').get(), 400))))):
                                rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'updateAnti'), [e.get('_loc2_')])
                            assign(ref(ref(e.get('_loc2_'), 'MC').get(), '_x'), '=', lambda: ref(e.get('_loc2_'), 'curX').get())
                            assign(ref(ref(e.get('_loc2_'), 'MC').get(), '_y'), '=', lambda: ref(e.get('_loc2_'), 'curY').get())
                            assign(ref(ref(e.get('_loc2_'), 'MC').get(), '_alpha'), '=', lambda: 100)
                        if truth(ref(e.get('_loc2_'), 'hasShadow').get()):
                            rt.call_ref(ref(ref(ref(e.get('_loc2_'), 'shadowMC').get(), 'mc').get(), 'gotoAndStop'), [ref(ref(e.get('_loc2_'), 'MC').get(), '_currentframe').get()])
                            assign(ref(ref(e.get('_loc2_'), 'shadowMC').get(), '_x'), '=', lambda: binop('+', ref(e.get('_loc2_'), 'curX').get(), ref(e.get('_loc2_'), 'shadowXOffset').get()))
                            assign(ref(ref(e.get('_loc2_'), 'shadowMC').get(), '_y'), '=', lambda: binop('+', ref(e.get('_loc2_'), 'curY').get(), ref(e.get('_loc2_'), 'shadowYOffset').get()))
                        if truth(ref(e.get('_loc2_'), 'tintMC_id').get()):
                            rt.call_ref(ref(ref(e.get('_loc2_'), 'tintMC').get(), 'gotoAndStop'), [ref(ref(e.get('_loc2_'), 'MC').get(), '_currentframe').get()])
                            assign(ref(ref(e.get('_loc2_'), 'tintMC').get(), '_x'), '=', lambda: ref(e.get('_loc2_'), 'curX').get())
                            assign(ref(ref(e.get('_loc2_'), 'tintMC').get(), '_y'), '=', lambda: ref(e.get('_loc2_'), 'curY').get())
                    if truth(ref(e.get('_loc2_'), 'depthSwap').get()):
                        if truth(binop('!=', rt.call_ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'getDepth'), []), ref(e.get('_loc2_'), 'appMC_depth').get())):
                            rt.call_ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'swapDepths'), [ref(e.get('_loc2_'), 'appMC_depth').get()])
                        if truth(ref(e.get('_loc2_'), 'tintMC').get()):
                            rt.call_ref(ref(ref(e.get('_loc2_'), 'tintMC').get(), 'swapDepths'), [binop('+', rt.call_ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'getDepth'), []), 1)])
                if truth(binop('==', ref(e.get('_loc2_'), 'anti_type').get(), 'air')):
                    if truth(logical('&&', ref(e.get('_loc2_'), 'anti_active').get(), lambda: logical('&&', ref(e.get('_loc2_'), 'activeAndMoving').get(), lambda: logical('&&', binop('==', ref(ref(e.get('_loc2_'), 'anti_pos').get(), 0).get(), 0), lambda: unary('!', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), 'targetPlayer').get()).get(), 'anti_inBattle_target').get()))))):
                        assign(ref(ref(e.get('_loc2_'), 'anti_pos').get(), 0), '=', lambda: ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), 'targetPlayer').get()).get(), 'anti_pos_arr').get(), 0).get())
                        assign(ref(ref(e.get('_loc2_'), 'anti_pos').get(), 1), '=', lambda: ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), 'targetPlayer').get()).get(), 'anti_pos_arr').get(), 1).get())
                        assign(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), 'targetPlayer').get()).get(), 'anti_inBattle_target'), '=', lambda: e.get('_loc2_'))
                    if truth(logical('&&', binop('==', ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc2_'), 'targetPlayer').get()).get(), 'anti_inBattle_target').get(), e.get('_loc2_')), lambda: logical('&&', unary('!', ref(e.get('_loc2_'), 'anti_initiated').get()), lambda: ref(e.get('_loc2_'), 'anti_active').get()))):
                        rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'updateAnti'), [e.get('_loc2_')])
                if truth(binop('==', ref(e.get('_loc2_'), 'action').get(), 'shoot')):
                    assign(e.ref('_loc12_'), '=', lambda: binop('+', binop('-', binop('*', ref(e.get('_loc2_'), 'unitDirection').get(), ref(e.get('_loc2_'), 'offsetFrames').get()), binop('-', ref(e.get('_loc2_'), 'offsetFrames').get(), 1)), ref(e.get('_loc2_'), 'frameOffset').get()))
                    rt.call_ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'gotoAndStop'), [e.get('_loc12_')])
                    rt.call_ref(ref(ref(e.get('_loc2_'), 'tintMC').get(), 'gotoAndStop'), [e.get('_loc12_')])
                    if truth(binop('<', ref(e.get('_loc2_'), 'frameOffset').get(), ref(e.get('_loc2_'), 'offsetFrames').get())):
                        assign(ref(e.get('_loc2_'), 'frameOffset'), '=', lambda: binop('+', ref(e.get('_loc2_'), 'frameOffset').get(), 1))
                    else:
                        assign(ref(e.get('_loc2_'), 'frameOffset'), '=', lambda: 1)
                if truth(logical('&&', binop('==', ref(e.get('_loc2_'), 'mcID').get(), 'chinook'), lambda: unary('!', ref(e.get('_loc2_'), 'activeAndMoving').get()))):
                    assign(e.ref('_loc13_'), '=', lambda: binop('+', binop('-', binop('*', ref(e.get('_loc2_'), 'fixedFrame').get(), ref(e.get('_loc2_'), 'offsetFrames').get()), binop('-', ref(e.get('_loc2_'), 'offsetFrames').get(), 1)), ref(e.get('_loc2_'), 'frameOffset').get()))
                    rt.call_ref(ref(ref(e.get('_loc2_'), 'MC').get(), 'gotoAndStop'), [e.get('_loc13_')])
                    if truth(binop('<', ref(e.get('_loc2_'), 'frameOffset').get(), ref(e.get('_loc2_'), 'offsetFrames').get())):
                        assign(ref(e.get('_loc2_'), 'frameOffset'), '=', lambda: binop('+', ref(e.get('_loc2_'), 'frameOffset').get(), 1))
                    else:
                        assign(ref(e.get('_loc2_'), 'frameOffset'), '=', lambda: 1)
                if truth(logical('&&', ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'battle').get(), '_activeUnitsArr').get(), e.get('i')).get(), '_building').get(), lambda: ref(ref(e.get('_global'), 'model').get(), 'battleMC_units_active').get())):
                    assign(ref(ref(e.get('_global'), 'model').get(), 'battleCounter'), '=', lambda: 0)
                    assign(e.ref('_loc14_'), '=', lambda: ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'battle').get(), '_activeUnitsArr').get(), e.get('i')).get(), 'obj').get())
                    if truth(binop('==', ref(ref(e.get('_global'), 'model').get(), 'unitStartNum').get(), ref(e.get('_loc14_'), '_startNum').get())):
                        rt.call_ref(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'battle').get(), '_activeUnitsArr').get(), 'splice'), [e.get('i'), 1])
                        if truth(logical('&&', binop('==', ref(e.get('_loc14_'), '_building').get(), 'sub'), lambda: unary('!', ref(e.get('_loc14_'), '_addToSubArr').get()))):
                            rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'playSubMC'), [e.get('_loc14_')])
                        else:
                            if truth(binop('==', ref(e.get('_loc14_'), '_building').get(), 'ship')):
                                pass
            except ASContinue:
                pass
            except ASBreak:
                break
    return U

def View_createUnitTicker(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View')
    assign(ref(ref(this, 'battleSrcMC').get(), 'ticker_count'), '=', lambda: 0)
    assign(ref(ref(this, 'battleSrcMC').get(), 'onEnterFrame'), '=', lambda: ASFunction(f_37, e))
    return U

def View_play_AB_selectMC(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_loc10_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', '_str', 'j'], closure, 'View')
    rt.call_ref(ref(e.get('_global'), 'play_sound_by_building'), [e.get('_str')])
    e.set('_loc3_', False)
    e.set('_loc4_', False)
    e.set('_loc5_', False)
    e.set('_loc6_', False)
    for key_39 in keys(ref(ref(e.get('_global'), 'model').get(), 'playerAB_position_arr').get()):
        e.ref('j').set(key_39)
        rt.tick()
        try:
            assign(e.ref('_loc7_'), '=', lambda: ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerAB_position_arr').get(), e.get('j')).get(), 'building_name').get())
            if truth(binop('==', e.get('_str'), 'preAttack')):
                if truth(logical('&&', binop('==', e.get('_loc7_'), 'airfield'), lambda: unary('!', e.get('_loc3_')))):
                    assign(e.ref('_loc3_'), '=', lambda: True)
                    rt.call_ref(ref(e.get('_global'), 'play_sound_by_building'), ['airfield'])
                else:
                    if truth(logical('&&', binop('==', e.get('_loc7_'), 'silo'), lambda: unary('!', e.get('_loc4_')))):
                        assign(e.ref('_loc4_'), '=', lambda: True)
                        rt.call_ref(ref(e.get('_global'), 'play_sound_by_building'), ['silo'])
                    else:
                        if truth(logical('&&', binop('==', e.get('_loc7_'), 'sub'), lambda: unary('!', e.get('_loc5_')))):
                            assign(e.ref('_loc5_'), '=', lambda: True)
                            rt.call_ref(ref(e.get('_global'), 'play_sound_by_building'), ['sub'])
                        else:
                            if truth(logical('&&', binop('==', e.get('_loc7_'), 'space'), lambda: unary('!', e.get('_loc6_')))):
                                assign(e.ref('_loc6_'), '=', lambda: True)
                                rt.call_ref(ref(e.get('_global'), 'play_sound_by_building'), ['space'])
            else:
                if truth(binop('==', e.get('_str'), 'attack')):
                    if truth(binop('==', e.get('_loc7_'), 'hatch')):
                        rt.call_ref(ref(e.get('_global'), 'play_sound_by_building'), ['hatch'])
        except ASContinue:
            pass
        except ASBreak:
            break
    if truth(binop('==', e.get('_str'), 'propaganda')):
        rt.call_ref(ref(ref(this, 'presenter').get(), 'doPropaganda'), [])
    e.set('_loc8_', 0)
    while truth(binop('<', e.get('_loc8_'), 5)):
        rt.tick()
        try:
            assign(e.ref('_loc9_'), '=', lambda: rt.call_ref(ref(ref(this, 'model').get(), 'get_playerAB_mc'), [e.get('_loc8_'), e.get('_str')]))
            assign(e.ref('_loc10_'), '=', lambda: ref(e.get('_loc9_'), 'citySelectMC').get())
            if truth(e.get('_loc10_')):
                switch_40 = e.get('_str')
                case_41 = -1
                if case_41 == -1 and strict_eq(switch_40, 'diplomacy'):
                    case_41 = 0
                if case_41 == -1 and strict_eq(switch_40, 'production'):
                    case_41 = 1
                if case_41 == -1 and strict_eq(switch_40, 'tech'):
                    case_41 = 2
                if case_41 == -1 and strict_eq(switch_40, 'religion'):
                    case_41 = 3
                if case_41 == -1 and strict_eq(switch_40, 'tech'):
                    case_41 = 4
                if case_41 == -1 and strict_eq(switch_40, 'hatch'):
                    case_41 = 5
                if case_41 == -1 and strict_eq(switch_40, 'attack'):
                    case_41 = 6
                if case_41 == -1 and strict_eq(switch_40, 'preAttack'):
                    case_41 = 7
                if case_41 == -1:
                    case_41 = -1
                try:
                    if 0 <= case_41 <= 0:
                        rt.call_ref(ref(ref(ref(e.get('_loc9_'), 'mc').get(), 'mc').get(), 'play'), [])
                        raise ASBreak()
                    if 0 <= case_41 <= 1:
                        rt.call_ref(ref(ref(ref(e.get('_loc9_'), 'mc').get(), 'mc').get(), 'play'), [])
                        raise ASBreak()
                    if 0 <= case_41 <= 2:
                        rt.call_ref(ref(ref(ref(e.get('_loc9_'), 'mc').get(), 'mc').get(), 'play'), [])
                        raise ASBreak()
                    if 0 <= case_41 <= 3:
                        rt.call_ref(ref(ref(ref(e.get('_loc9_'), 'mc').get(), 'mc').get(), 'play'), [])
                        raise ASBreak()
                    if 0 <= case_41 <= 4:
                        rt.call_ref(ref(ref(ref(e.get('_loc9_'), 'mc').get(), 'mc').get(), 'play'), [])
                        raise ASBreak()
                    if 0 <= case_41 <= 5:
                        rt.call_ref(ref(ref(ref(e.get('_loc9_'), 'mc').get(), 'mc').get(), 'play'), [])
                        raise ASBreak()
                    if 0 <= case_41 <= 6:
                        rt.call_ref(ref(ref(ref(e.get('_loc9_'), 'mc').get(), 'mc').get(), 'play'), [])
                        raise ASBreak()
                    if 0 <= case_41 <= 7:
                        rt.call_ref(ref(ref(ref(e.get('_loc9_'), 'mc').get(), 'mc').get(), 'play'), [])
                except ASBreak:
                    pass
                rt.call_ref(ref(e.get('_loc10_'), 'play'), [])
                rt.call_ref(ref(this, 'curActionText'), [e.get('_str'), e.get('_loc8_')])
            assign(e.ref('_loc8_'), '=', lambda: binop('+', e.get('_loc8_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def View_initiate_AB_interval(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'View')
    e.set('_loc2_', ref(this, 'AB_interval_start_index').get())
    while truth(binop('<', e.get('_loc2_'), ref(ref(ref(this, 'model').get(), 'actionNames_arr').get(), 'length').get())):
        rt.tick()
        try:
            assign(ref(this, 'AB_interval_start_index'), '=', lambda: binop('+', ref(this, 'AB_interval_start_index').get(), 1))
            if truth(rt.call_ref(ref(ref(this, 'model').get(), 'string_is_used_action'), [ref(ref(ref(this, 'model').get(), 'actionNames_arr').get(), e.get('_loc2_')).get()])):
                rt.call_ref(ref(this, 'play_AB_selectMC'), [ref(ref(ref(this, 'model').get(), 'actionNames_arr').get(), e.get('_loc2_')).get()])
                return e.get('undefined')
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    assign(ref(this, 'submarine_interval_ID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'submarineSequence', 8000]))
    rt.call_ref(ref(ref(this, 'presenter').get(), 'stop_continues_sound_objects'), [])
    assign(ref(ref(this, 'model').get(), 'battleMC_units_active'), '=', lambda: True)
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'AB_interval_ID').get()])
    return U

def View_timedSubmarine(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['obj'], ['obj'], closure, 'View')
    rt.call_ref(ref(this, 'playSubMC'), [e.get('obj')])
    return U

def View_submarineSequence(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'View')
    e.set('_loc2_', ref(ref(ref(this, 'model').get(), 'attackingSubs_arr').get(), 0).get())
    if truth(e.get('_loc2_')):
        rt.call_ref(ref(ref(ref(this, 'model').get(), 'attackingSubs_arr').get(), 'splice'), [0, 1])
        rt.call_ref(ref(this, 'timedSubmarine'), [e.get('_loc2_')])
    else:
        rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'submarine_interval_ID').get()])
        assign(ref(ref(this, 'model').get(), 'attackingSubs_arr'), '=', lambda: arr([]))
    return U

def View_interval_func(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View')
    rt.call_ref(ref(this, 'initiate_AB_interval'), [])
    return U

def View_showActionBuildingFromObj(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_obj'], ['_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_obj', 'i'], closure, 'View')
    e.set('_loc3_', e.get('_obj'))
    e.set('_loc4_', ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_player').get()).get())
    if truth(unary('!', ref(e.get('_loc3_'), '_fixedLoc').get())):
        if truth(binop('==', e.get('_loc4_'), ref(ref(this, 'model').get(), 'human').get())):
            pass
        if truth(logical('||', unary('!', ref(e.get('_loc4_'), 'preLocation').get()), lambda: unary('!', ref(e.get('_loc4_'), 'preBuilding_this_turn').get()))):
            assign(e.ref('_loc5_'), '=', lambda: ref(e.get('_loc4_'), 'nextActionBuilding').get())
        else:
            if truth(binop('==', ref(e.get('_loc4_'), 'preLocation').get(), 1)):
                assign(ref(e.get('_loc4_'), 'building1Shown'), '=', lambda: True)
                assign(e.ref('_loc5_'), '=', lambda: 2)
            else:
                if truth(binop('==', ref(e.get('_loc4_'), 'preLocation').get(), 2)):
                    assign(ref(e.get('_loc4_'), 'building2Shown'), '=', lambda: True)
                    assign(e.ref('_loc5_'), '=', lambda: 1)
        assign(e.ref('_loc6_'), '=', lambda: ref(ref(this, 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'ab', ref(e.get('_loc3_'), '_player').get()), '_'), e.get('_loc5_'))).get())
    else:
        assign(e.ref('_loc6_'), '=', lambda: ref(ref(this, 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'ab', ref(e.get('_loc3_'), '_player').get()), '_'), ref(e.get('_loc4_'), 'preLocation').get())).get())
    if truth(binop('==', e.get('_loc4_'), ref(ref(this, 'model').get(), 'human').get())):
        for key_42 in keys(e.get('_obj')):
            e.ref('i').set(key_42)
            rt.tick()
            try:
                pass
            except ASContinue:
                pass
            except ASBreak:
                break
    rt.call_ref(ref(e.get('_loc6_'), 'gotoAndStop'), [ref(e.get('_loc3_'), '_frame').get()])
    rt.call_ref(ref(ref(e.get('_loc6_'), 'mc').get(), 'gotoAndStop'), [ref(e.get('_loc4_'), 'religion_code').get()])
    if truth(logical('&&', binop('==', ref(e.get('_loc3_'), '_frame').get(), 'airfield'), lambda: logical('||', binop('==', ref(e.get('_loc4_'), 'playerNum').get(), 2), lambda: binop('==', ref(e.get('_loc4_'), 'playerNum').get(), 3)))):
        rt.call_ref(ref(ref(ref(e.get('_loc6_'), 'mc').get(), 'mc_').get(), 'gotoAndStop'), [2])
    if truth(binop('==', ref(e.get('_loc3_'), '_frame').get(), 'propaganda')):
        assign(ref(e.get('_loc4_'), '_propagandaMC'), '=', lambda: e.get('_loc6_'))
    if truth(logical('&&', binop('==', ref(e.get('_loc3_'), '_frame').get(), 'religion'), lambda: rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'check_ch_active'), ['disco']))):
        rt.call_ref(ref(ref(e.get('_loc6_'), 'mc').get(), 'gotoAndStop'), ['disco'])
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'play_ambient_sound_by_building_frame'), [ref(e.get('_loc3_'), '_frame').get()])
    if truth(binop('==', ref(e.get('_loc3_'), '_frame').get(), 'propaganda_2')):
        assign(e.ref('_loc7_'), '=', lambda: rt.construct(e.get('Color'), [ref(ref(e.get('_loc6_'), 'mc').get(), 'beamMC').get()]))
        rt.call_ref(ref(e.get('_loc7_'), 'setTransform'), [ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_player').get()).get(), 'playerColorTint1').get()])
        rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'updateSingleCity_byID'), [ref(e.get('_loc3_'), '_targetCity_id').get(), 0, True, ref(e.get('_loc3_'), '_player').get()])
        rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'update_propaganda_plus'), [ref(e.get('_loc3_'), '_player').get()])
    rt.call_ref(ref(ref(e.get('_loc6_'), 'mc').get(), 'gotoAndStop'), [ref(e.get('_loc4_'), 'religion_code').get()])
    rt.call_ref(ref(this, 'fadeClip'), [e.get('_loc6_'), 100, 'in', 5, False])
    if truth(ref(e.get('_loc3_'), '_setHeliStart').get()):
        assign(ref(e.get('_loc4_'), 'heliStart'), '=', lambda: arr([binop('-', ref(e.get('_loc6_'), '_x').get(), 15), binop('+', ref(e.get('_loc6_'), '_y').get(), 25)]))
        assign(ref(ref(ref(e.get('_global'), 'model').get(), 'heliStart').get(), ref(e.get('_loc3_'), '_player').get()), '=', lambda: arr([binop('-', ref(e.get('_loc6_'), '_x').get(), 15), binop('+', ref(e.get('_loc6_'), '_y').get(), 25)]))
    if truth(binop('==', ref(e.get('_loc3_'), '_frame').get(), 'ship')):
        rt.call_ref(ref(this, 'playCarrierMC'), [e.get('_loc3_')])
    if truth(logical('&&', ref(e.get('_loc3_'), '_setPreStart').get(), lambda: unary('!', ref(e.get('_loc4_'), 'preLocation').get()))):
        assign(ref(e.get('_loc4_'), 'preStart'), '=', lambda: arr([ref(e.get('_loc6_'), '_x').get(), binop('+', ref(e.get('_loc6_'), '_y').get(), 25)]))
        assign(ref(e.get('_loc4_'), 'preLocation'), '=', lambda: e.get('_loc5_'))
    if truth(ref(ref(e.get('_loc3_'), '_anti_arr').get(), 0).get()):
        assign(ref(e.get('_loc4_'), 'anti_active'), '=', lambda: ref(ref(e.get('_loc3_'), '_anti_arr').get(), 0).get())
        assign(ref(e.get('_loc4_'), 'anti_type'), '=', lambda: ref(ref(e.get('_loc3_'), '_anti_arr').get(), 1).get())
        assign(ref(e.get('_loc4_'), 'anti_pos_arr'), '=', lambda: arr([ref(e.get('_loc6_'), '_x').get(), ref(e.get('_loc6_'), '_y').get()]))
        assign(ref(e.get('_loc4_'), 'anti_loc'), '=', lambda: e.get('_loc5_'))
    if truth(logical('&&', binop('==', ref(e.get('_loc3_'), '_frame').get(), 'religion'), lambda: rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'check_ch_active'), ['disco']))):
        rt.call_ref(ref(ref(e.get('_loc6_'), 'mc').get(), 'gotoAndStop'), ['disco'])
    return e.get('_loc6_')
    return U

def View_getIntervalBuildingsArray(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View')
    if truth(unary('!', rt.call_ref(ref(this, 'showBuildingsFromArray'), [ref(ref(ref(e.get('_global'), 'model').get(), 'battle').get(), 'toShowLastABArr').get()]))):
        rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(ref(e.get('_global'), 'model').get(), 'actionBuildingInterval').get()])
        rt.call_ref(ref(ref(this, 'presenter').get(), 'endBattle'), [])
    return U

def View_showBuildingsFromArray(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_array'], ['_array', '_loc3_', '_loc4_', '_loc5_', '_loc6_'], closure, 'View')
    rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'curActionText'), [ref(e.get('_array'), '_frame').get(), ref(e.get('_array'), '_player').get()])
    e.set('_loc3_', e.get('_array'))
    if truth(unary('!', ref(e.get('_loc3_'), '_empty').get())):
        assign(e.ref('_loc4_'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(e.get('_loc3_'), '_player').get()).get())
        if truth(binop('==', ref(e.get('_loc4_'), 'playerNum').get(), 0)):
            pass
        if truth(unary('!', ref(e.get('_loc3_'), '_fixedLoc').get())):
            assign(e.ref('_loc5_'), '=', lambda: ref(e.get('_loc4_'), 'nextActionBuilding').get())
            assign(e.ref('_loc6_'), '=', lambda: ref(ref(this, 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'ab', ref(e.get('_loc3_'), '_player').get()), '_'), e.get('_loc5_'))).get())
        else:
            assign(e.ref('_loc6_'), '=', lambda: ref(ref(this, 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'ab', ref(e.get('_loc3_'), '_player').get()), '_'), ref(e.get('_loc4_'), 'preLocation').get())).get())
        rt.call_ref(ref(e.get('_loc6_'), 'gotoAndStop'), [ref(e.get('_loc3_'), '_frame').get()])
        rt.call_ref(ref(ref(e.get('_loc6_'), 'mc').get(), 'gotoAndStop'), [ref(e.get('_loc4_'), 'religion_code').get()])
        if truth(logical('&&', binop('==', ref(e.get('_loc3_'), '_frame').get(), 'airfield'), lambda: logical('||', binop('==', ref(e.get('_loc4_'), 'playerNum').get(), 2), lambda: binop('==', ref(e.get('_loc4_'), 'playerNum').get(), 3)))):
            rt.call_ref(ref(ref(ref(e.get('_loc6_'), 'mc').get(), 'mc').get(), 'gotoAndStop'), [2])
        rt.call_ref(ref(this, 'fadeClip'), [e.get('_loc6_'), 100, 'in', 5, False])
        if truth(ref(e.get('_loc3_'), '_setPreStart').get()):
            assign(ref(e.get('_loc4_'), 'preStart'), '=', lambda: arr([ref(e.get('_loc6_'), '_x').get(), binop('+', ref(e.get('_loc6_'), '_y').get(), 25)]))
            assign(ref(e.get('_loc4_'), 'preLocation'), '=', lambda: e.get('_loc5_'))
        if truth(ref(ref(e.get('_loc3_'), '_anti_arr').get(), 0).get()):
            assign(ref(e.get('_loc4_'), 'anti_active'), '=', lambda: ref(ref(e.get('_loc3_'), '_anti_arr').get(), 0).get())
            assign(ref(e.get('_loc4_'), 'anti_type'), '=', lambda: ref(ref(e.get('_loc3_'), '_anti_arr').get(), 1).get())
            assign(ref(e.get('_loc4_'), 'anti_pos_arr'), '=', lambda: arr([ref(e.get('_loc6_'), '_x').get(), ref(e.get('_loc6_'), '_y').get()]))
            assign(ref(e.get('_loc4_'), 'anti_loc'), '=', lambda: e.get('_loc5_'))
            assign(ref(ref(e.get('_loc6_'), 'mc').get(), '_alpha'), '=', lambda: 0)
        assign(ref(ref(ref(e.get('_global'), 'model').get(), 'heliStart').get(), ref(e.get('_loc3_'), '_player').get()), '=', lambda: arr([binop('-', ref(e.get('_loc6_'), '_x').get(), 15), binop('+', ref(e.get('_loc6_'), '_y').get(), 25)]))
        return True
    return False
    return U

def View_set_crash_text(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a_str'], ['a_str'], closure, 'View')
    assign(ref(ref(e.get('_level0'), 'crashText').get(), 'text'), '=', lambda: binop('+', 'Code report: ', e.get('a_str')))
    return U

def View_setABDepth(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_', '_loc5_', 'i'], closure, 'View')
    for key_43 in keys(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get()):
        e.ref('i').set(key_43)
        rt.tick()
        try:
            assign(e.ref('_loc2_'), '=', lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), e.get('i')).get())
            assign(e.ref('_loc3_'), '=', lambda: ref(ref(this, 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'ab', ref(e.get('_loc2_'), 'playerNum').get()), '_'), 1)).get())
            assign(e.ref('_loc4_'), '=', lambda: ref(ref(this, 'battleSrcMC').get(), binop('+', binop('+', binop('+', 'ab', ref(e.get('_loc2_'), 'playerNum').get()), '_'), 2)).get())
            assign(e.ref('_loc5_'), '=', lambda: ref(ref(this, 'battleSrcMC').get(), binop('+', 'flag', ref(e.get('_loc2_'), 'playerNum').get())).get())
            rt.call_ref(ref(e.get('_loc3_'), 'swapDepths'), [binop('+', binop('*', rt.call_ref(ref(e.get('Math'), 'floor'), [binop('/', ref(e.get('_loc3_'), '_y').get(), 10)]), 500), 2)])
            rt.call_ref(ref(e.get('_loc4_'), 'swapDepths'), [binop('+', binop('*', rt.call_ref(ref(e.get('Math'), 'floor'), [binop('/', ref(e.get('_loc4_'), '_y').get(), 10)]), 500), 1)])
            rt.call_ref(ref(e.get('_loc5_'), 'swapDepths'), [binop('+', binop('*', rt.call_ref(ref(e.get('Math'), 'floor'), [binop('/', ref(e.get('_loc4_'), '_y').get(), 10)]), 500), 3)])
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def View_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'View')
    ref(this, 'someString').set('blaat')
    ref(this, 'interfaceBGDepth').set(210)
    ref(this, 'actionLightDepthStart').set(211)
    ref(this, 'actionTextDepthStart').set(221)
    ref(this, 'ticker1Depth').set(250)
    ref(this, 'ticker2Depth').set(251)
    ref(this, 'infoTextDepth').set(252)
    ref(this, 'scrollTextDepth').set(253)
    ref(this, 'ticker3Depth').set(254)
    ref(this, 'ticker4Depth').set(255)
    ref(this, 'ticker5Depth').set(256)
    ref(this, 'ticker6Depth').set(257)
    ref(this, 'statBarDepth').set(258)
    ref(this, 'exBtnSrcDepth').set(259)
    ref(this, 'exBtnOvrDepth').set(260)
    ref(this, 'smallMapCityDepthStart').set(270)
    ref(this, 'playerOutlineDepthStart').set(350)
    ref(this, 'cloudTickerDepth').set(360)
    ref(this, 'citySelectionDepthStart').set(1500)
    ref(this, 'nextUnusedDepthPleaseRenameThisVarBecauseItsTooLong').set(1500)
    ref(this, 'popupDepthStart').set(4000)
    ref(this, 'btnArr').set(arr([0, 0]))
    ref(this, 'btnSet_actions').set(rt.construct(e.get('Array'), []))
    ref(this, 'btnSet_stock').set(rt.construct(e.get('Array'), []))
    ref(this, 'actionTextMCArr').set(rt.construct(e.get('Array'), []))
    ref(this, 'fadeClipsArr').set(rt.construct(e.get('Array'), []))
    ref(this, 'openPopupsArr').set(rt.construct(e.get('Array'), []))
    ref(this, 'btnBroadcaster').set(rt.construct(e.get('Object'), []))
    ref(this, 'fadeStockBtnArr').set(rt.construct(e.get('Array'), []))
    ref(this, 'fadeStockActive').set(False)
    ref(this, 'typeEffectArr').set(rt.construct(e.get('Array'), []))
    ref(this, 'scrollTextStartIndex').set(0)
    ref(this, 'scrollTickerActive').set(False)
    ref(this, 'scrollMaxChars').set(60)
    ref(this, 'currentViewType').set('interface')
    ref(this, 'allowTextEffect').set(False)
    ref(this, 'textEffectInterval').set(12)
    ref(this, 'curTextEffectIntervalCount').set(0)
    ref(this, 'cloudArr').set(arr([]))
    ref(this, 'cloudPacks').set(0)
    ref(this, 'cloudMax').set(17)
    ref(this, 'cloudCenterPositions').set(rt.construct(e.get('Array'), [arr([416, 350]), arr([180, 180]), arr([650, 150]), arr([180, 480]), arr([640, 470])]))
    ref(this, 'AB_interval_start_index').set(0)

def register(rt):
    rt.define('View', None, View_fields, {'View': ASFunction(View_View), 'fadeClip': ASFunction(View_fadeClip), 'updateView': ASFunction(View_updateView), 'error': ASFunction(View_error), 'welcomeWindow': ASFunction(View_welcomeWindow), 'createMessageWindow': ASFunction(View_createMessageWindow), 'updateSingleCity': ASFunction(View_updateSingleCity), 'city_shrink_sequence': ASFunction(View_city_shrink_sequence), 'spawnCity': ASFunction(View_spawnCity), 'update_flags': ASFunction(View_update_flags), 'remove_city_popups': ASFunction(View_remove_city_popups), 'updateCities': ASFunction(View_updateCities), 'resetActionBuildings': ASFunction(View_resetActionBuildings), 'changeOver': ASFunction(View_changeOver), 'to_interface_timed_3': ASFunction(View_to_interface_timed_3), 'to_interface_timed_3_A': ASFunction(View_to_interface_timed_3_A), 'to_interface_timed_3_B': ASFunction(View_to_interface_timed_3_B), 'to_interface_timed_3_C': ASFunction(View_to_interface_timed_3_C), 'to_interface_timed_4': ASFunction(View_to_interface_timed_4), 'to_interface_timed_5': ASFunction(View_to_interface_timed_5), 'interface_before_end_game_sequence': ASFunction(View_interface_before_end_game_sequence), 'end_game_sequence': ASFunction(View_end_game_sequence), 'end_game_sequence_2': ASFunction(View_end_game_sequence_2), 'setMapFrames': ASFunction(View_setMapFrames), 'setFaceFrames': ASFunction(View_setFaceFrames), 'playSubMC': ASFunction(View_playSubMC), 'playCarrierMC': ASFunction(View_playCarrierMC), 'reset_schemeMC': ASFunction(View_reset_schemeMC), 'curActionText': ASFunction(View_curActionText), 'updateAnti': ASFunction(View_updateAnti), 'createBioCloud': ASFunction(View_createBioCloud), 'createClouds': ASFunction(View_createClouds), 'cloud_interval_func': ASFunction(View_cloud_interval_func), 'cloudTicker_initiate': ASFunction(View_cloudTicker_initiate), 'createUnitTicker': ASFunction(View_createUnitTicker), 'play_AB_selectMC': ASFunction(View_play_AB_selectMC), 'initiate_AB_interval': ASFunction(View_initiate_AB_interval), 'timedSubmarine': ASFunction(View_timedSubmarine), 'submarineSequence': ASFunction(View_submarineSequence), 'interval_func': ASFunction(View_interval_func), 'showActionBuildingFromObj': ASFunction(View_showActionBuildingFromObj), 'getIntervalBuildingsArray': ASFunction(View_getIntervalBuildingsArray), 'showBuildingsFromArray': ASFunction(View_showBuildingsFromArray), 'set_crash_text': ASFunction(View_set_crash_text), 'setABDepth': ASFunction(View_setABDepth)}, {}, {'clipSrc': ASFunction(View___set__clipSrc)})
