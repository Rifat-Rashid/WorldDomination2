# Generated from DefineSprite_5782_gameloader_mc/frame_10/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('stop', [])
    return U

def register(rt):
    rt.scripts['DefineSprite_5782_gameloader_mc/frame_10/DoAction.as'] = ASFunction(run)
