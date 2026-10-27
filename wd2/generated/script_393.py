# Generated from frame_4/DoAction.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def f_1(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    if truth(binop('==', e.get('loaded'), 100)):
        assign(e.ref('loaded'), '=', lambda: e.get('undefined'))
        assign(ref(this, 'onEnterFrame'), '=', lambda: e.get('undefined'))
        e.call('play', [])
    else:
        assign(e.ref('loaded'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [binop('*', binop('/', rt.call_ref(ref(this, 'getBytesLoaded'), []), rt.call_ref(ref(this, 'getBytesTotal'), [])), 100)]))
        assign(ref(ref(ref(this, 'youdapreloader').get(), 'percentloaded_bar_mc').get(), '_xscale'), '=', lambda: e.get('loaded'))
        assign(ref(ref(ref(this, 'youdapreloader').get(), 'loaded_txt').get(), 'text'), '=', lambda: binop('+', e.get('loaded'), '%'))
        e.call('stop', [])
    return U

def run(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['loaded'], closure, None)
    e.set('loaded', 0)
    assign(ref(e.get('_root'), 'onEnterFrame'), '=', lambda: ASFunction(f_1, e))
    e.call('stop', [])
    return U

def register(rt):
    rt.scripts['frame_4/DoAction.as'] = ASFunction(run)
