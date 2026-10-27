# Generated from DefineButton2_5783/BUTTONCONDACTION on(press).as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('getURL', ['www.youdagames.com', '_blank'])
    return U

def register(rt):
    rt.scripts['DefineButton2_5783/BUTTONCONDACTION on(press).as'] = ASFunction(run)
