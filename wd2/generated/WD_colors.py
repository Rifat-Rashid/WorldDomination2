# Generated from __Packages/WD_colors.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def WD_colors_WD_colors(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'WD_colors')
    return U

def WD_colors_WDII_colors(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'WD_colors')
    return U

def WD_colors_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'WD_colors')
    ref(this, 'color_red').set(obj({'ra': 50, 'rb': 255, 'ga': 0, 'gb': 0, 'ba': 0, 'bb': 0, 'aa': 75, 'ab': 0}))
    ref(this, 'color_blu').set(obj({'ra': 15, 'rb': 0, 'ga': 74, 'gb': 0, 'ba': 100, 'bb': 255, 'aa': 100, 'ab': 0}))
    ref(this, 'color_gre').set(obj({'ra': 0, 'rb': 0, 'ga': 50, 'gb': 255, 'ba': 0, 'bb': 0, 'aa': 75, 'ab': 0}))
    ref(this, 'color_yel').set(obj({'ra': 50, 'rb': 255, 'ga': 50, 'gb': 255, 'ba': 0, 'bb': 0, 'aa': 75, 'ab': 0}))
    ref(this, 'color_ora').set(obj({'ra': 100, 'rb': 91, 'ga': 62, 'gb': 40, 'ba': 0, 'bb': 0, 'aa': 100, 'ab': 0}))
    ref(this, 'color_pur').set(obj({'ra': 70, 'rb': 0, 'ga': 40, 'gb': 0, 'ba': 100, 'bb': 0, 'aa': 100, 'ab': 0}))
    ref(this, 'city_red').set(obj({'ra': 100, 'rb': 200, 'ga': 100, 'gb': 0, 'ba': 100, 'bb': 0, 'aa': 75, 'ab': 0}))
    ref(this, 'city_green').set(obj({'ra': 50, 'rb': 0, 'ga': 100, 'gb': 100, 'ba': 50, 'bb': 0, 'aa': 75, 'ab': 0}))
    ref(this, '_default').set(obj({'ra': 100, 'rb': 0, 'ga': 100, 'gb': 0, 'ba': 100, 'bb': 0, 'aa': 100, 'ab': 0}))

def register(rt):
    rt.define('WD_colors', None, WD_colors_fields, {'WD_colors': ASFunction(WD_colors_WD_colors), 'WDII_colors': ASFunction(WD_colors_WDII_colors)}, {}, {})
