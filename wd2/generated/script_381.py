# Generated from DefineSprite_5912/frame_195/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    e.call('stop', [])
    assign(ref(ref(e.get('_root'), 'introMovie').get(), '_visible'), '=', lambda: False)
    assign(ref(ref(e.get('_root'), 'splashScreenMC').get(), '_visible'), '=', lambda: True)
    rt.call_ref(ref(ref(e.get('_global'), 'presenter_interface').get(), 'init_theme_snd'), [])
    return U

def register(rt):
    rt.scripts['DefineSprite_5912/frame_195/DoAction.as'] = ASFunction(run)
