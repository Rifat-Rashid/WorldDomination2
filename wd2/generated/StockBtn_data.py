# Generated from __Packages/StockBtn_data.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def StockBtn_data_StockBtn_data(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'StockBtn_data')
    assign(ref(this, 'dataArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(ref(this, 'dataArr').get(), 0), '=', lambda: e.get('undefined'))
    assign(ref(ref(this, 'dataArr').get(), 1), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [1, 'roc1', '10 meg', 'rocket1', 1, False]))
    assign(ref(ref(this, 'dataArr').get(), 2), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [2, 'roc2', '25 meg', 'rocket2', 1, False]))
    assign(ref(ref(this, 'dataArr').get(), 3), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [3, 'roc3', '50 meg', 'rocket3', 1, True]))
    assign(ref(ref(this, 'dataArr').get(), 4), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [4, 'roc4', '95 meg', 'rocket4', 1, True]))
    assign(ref(ref(this, 'dataArr').get(), 5), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [5, 'Air1', 'Fighter', 'plane1', 2, False]))
    assign(ref(ref(this, 'dataArr').get(), 6), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [6, 'Air2', 'Bomber', 'plane2', 2, True]))
    assign(ref(ref(this, 'dataArr').get(), 7), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [7, 'SpeC1', 'Submarine', 'sub', 3, False]))
    assign(ref(ref(this, 'dataArr').get(), 8), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [8, 'SpeC2', 'Aircraft Carrier', 'ship', 3, True]))
    assign(ref(ref(this, 'dataArr').get(), 9), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [9, 'SpeC3', 'Space Rocket', 'space', 3, True]))
    assign(ref(ref(this, 'dataArr').get(), 10), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [10, 'SpeC4', 'Satellite', 'specialLoad', 3, True]))
    assign(ref(ref(this, 'dataArr').get(), 11), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [11, 'war1', '10 meg', 'warhead1', 4, False]))
    assign(ref(ref(this, 'dataArr').get(), 12), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [12, 'war2', '25 meg', 'warhead2', 4, False]))
    assign(ref(ref(this, 'dataArr').get(), 13), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [13, 'war3', '50 meg', 'warhead3', 4, True]))
    assign(ref(ref(this, 'dataArr').get(), 14), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [14, 'war4', '95 meg', 'warhead4', 4, True]))
    assign(ref(ref(this, 'dataArr').get(), 15), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [15, 'bio1', '10 meg', 'bioload1', 5, False]))
    assign(ref(ref(this, 'dataArr').get(), 16), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [16, 'bio2', '25 meg', 'bioload2', 5, False]))
    assign(ref(ref(this, 'dataArr').get(), 17), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [17, 'bio3', '50 meg', 'bioload3', 5, True]))
    assign(ref(ref(this, 'dataArr').get(), 18), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [18, 'bio4', '95 meg', 'bioload4', 5, True]))
    assign(ref(ref(this, 'dataArr').get(), 19), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [19, 'sol1', 'Soldiers', 'soldier1', 6, False]))
    assign(ref(ref(this, 'dataArr').get(), 20), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [20, 'sol2', 'Seals', 'soldier2', 6, False]))
    assign(ref(ref(this, 'dataArr').get(), 21), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [21, 'sol3', 'Tank', 'soldier3', 6, True]))
    assign(ref(ref(this, 'dataArr').get(), 22), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [22, 'sol4', 'Specials', 'soldier4', 6, True]))
    assign(ref(ref(this, 'dataArr').get(), 23), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [23, 'spy1', 'spy 1', 'spy1', 7, False]))
    assign(ref(ref(this, 'dataArr').get(), 24), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [24, 'spy2', 'spy 2', 'spy2', 7, False]))
    assign(ref(ref(this, 'dataArr').get(), 25), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [25, 'spy3', 'spy 3', 'spy3', 7, True]))
    assign(ref(ref(this, 'dataArr').get(), 26), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [25, 'spy4', 'spy 4', 'spy4', 7, True]))
    assign(ref(ref(this, 'dataArr').get(), 27), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [25, 'anti1', 'Aircraft', 'antiAir', 8, False]))
    assign(ref(ref(this, 'dataArr').get(), 28), '=', lambda: rt.construct(e.get('StockBtn_data_obj'), [25, 'anti2', 'Rocket', 'antiRocket', 8, False]))
    e.set('_loc2_', 1)
    while truth(binop('<', e.get('_loc2_'), ref(ref(this, 'dataArr').get(), 'length').get())):
        rt.tick()
        try:
            assign(ref(ref(ref(this, 'dataArr').get(), e.get('_loc2_')).get(), 'overlayMC_name'), '=', lambda: binop('+', 'btn', binop('+', e.get('_loc2_'), 9)))
            assign(ref(ref(ref(this, 'dataArr').get(), e.get('_loc2_')).get(), 'scrnMC_name'), '=', lambda: binop('+', 'scrn', binop('+', e.get('_loc2_'), 9)))
            assign(ref(ref(ref(this, 'dataArr').get(), e.get('_loc2_')).get(), 'btnSwitchMC_name'), '=', lambda: binop('+', 'switch', binop('+', e.get('_loc2_'), 9)))
            assign(ref(ref(ref(this, 'dataArr').get(), e.get('_loc2_')).get(), 'scrnTF_name'), '=', lambda: binop('+', 'scrnTxt', binop('+', e.get('_loc2_'), 9)))
            assign(ref(ref(ref(this, 'dataArr').get(), e.get('_loc2_')).get(), 'labelTF_name'), '=', lambda: binop('+', 'stockTxt', e.get('_loc2_')))
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def StockBtn_data_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'StockBtn_data')
    pass

def register(rt):
    rt.define('StockBtn_data', None, StockBtn_data_fields, {'StockBtn_data': ASFunction(StockBtn_data_StockBtn_data)}, {}, {})
