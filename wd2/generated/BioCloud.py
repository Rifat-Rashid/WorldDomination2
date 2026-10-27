# Generated from __Packages/BioCloud.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def BioCloud_BioCloud(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'BioCloud')
    e.call('__super__', [])
    assign(ref(this, 'maxFloat'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(this, 'maxFloat').get(), '_x'), '=', lambda: 0)
    assign(ref(ref(this, 'maxFloat').get(), '_y'), '=', lambda: 0)
    return U

def BioCloud_spawn(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'BioCloud')
    assign(ref(this, '_x'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [unary('-', 25), 25]))
    assign(ref(this, '_y'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [unary('-', 20), 0]))
    assign(ref(this, '_alpha'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [30, 50]))
    assign(ref(this, '_xscale'), '=', lambda: assign(ref(this, '_yscale'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [40, 80])))
    assign(ref(this, 'alpha_decay'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [1, 3]))
    assign(ref(this, 'size_decay'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [2, 15]))
    assign(ref(this, 'ySpeed'), '=', lambda: 2)
    assign(ref(this, 'cur_horizontalFloat_offset'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [binop('*', ref(this, 'horizontalFloat_max').get(), unary('-', 1)), ref(this, 'horizontalFloat_max').get()]))
    assign(ref(this, 'cur_horizontalFloat_multiplier'), '=', lambda: 1)
    return U

def BioCloud_onEnterFrame(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'BioCloud')
    if truth(binop('<=', ref(this, '_alpha').get(), 0)):
        rt.call_ref(ref(this, 'spawn'), [])
    else:
        assign(ref(this, '_x'), '+=', lambda: binop('*', 0.3, ref(this, 'cur_horizontalFloat_multiplier').get()))
        assign(ref(this, 'cur_horizontalFloat_offset'), '=', lambda: binop('-', ref(this, 'cur_horizontalFloat_offset').get(), 1))
        if truth(binop('<=', ref(this, 'cur_horizontalFloat_offset').get(), 0)):
            assign(ref(this, 'cur_horizontalFloat_multiplier'), '*=', lambda: unary('-', 1))
            assign(ref(this, 'cur_horizontalFloat_offset'), '=', lambda: ref(this, 'horizontalFloat_max').get())
        assign(ref(this, '_y'), '-=', lambda: ref(this, 'ySpeed').get())
        assign(ref(this, '_alpha'), '-=', lambda: ref(this, 'alpha_decay').get())
        assign(ref(this, '_xscale'), '+=', lambda: ref(this, 'size_decay').get())
        assign(ref(this, '_yscale'), '+=', lambda: ref(this, 'size_decay').get())
    return U

def BioCloud_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'BioCloud')
    ref(this, 'horizontalFloat_max').set(10)

def register(rt):
    rt.define('BioCloud', 'MovieClip', BioCloud_fields, {'BioCloud': ASFunction(BioCloud_BioCloud), 'spawn': ASFunction(BioCloud_spawn), 'onEnterFrame': ASFunction(BioCloud_onEnterFrame)}, {}, {})
