# Generated from __Packages/SpaceRocket_trail_element.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def SpaceRocket_trail_element_SpaceRocket_trail_element(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'SpaceRocket_trail_element')
    e.call('__super__', [])
    return U

def SpaceRocket_trail_element_spawn(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'SpaceRocket_trail_element')
    assign(ref(this, '_x'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [binop('-', ref(this, 'rootX').get(), 2), binop('+', ref(this, 'rootX').get(), 2)]))
    assign(ref(this, '_y'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [binop('-', ref(this, 'rootY').get(), 5), binop('+', ref(this, 'rootY').get(), 5)]))
    assign(ref(this, '_xscale'), '=', lambda: assign(ref(this, '_yscale'), '=', lambda: 100))
    assign(ref(this, '_alpha'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [50, 60]))
    assign(ref(this, 'xAdd'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [unary('-', 1), 1]))
    assign(ref(this, 'yAdd'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [1, 2]))
    assign(ref(this, 'xAdd_decay'), '=', lambda: 0.2)
    assign(ref(this, 'sizeDecay_decay'), '=', lambda: 0.2)
    assign(ref(this, 'sizeDecay'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [3, 15]))
    assign(ref(this, 'alphaDecay'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [2, 4]))
    return U

def SpaceRocket_trail_element_setStep(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_rootX', '_rootY'], ['_rootX', '_rootY'], closure, 'SpaceRocket_trail_element')
    assign(ref(this, '_x'), '+=', lambda: ref(this, 'xAdd').get())
    assign(ref(this, 'sizeDecay'), '-=', lambda: ref(this, 'sizeDecay_decay').get())
    if truth(binop('<=', ref(this, '_y').get(), ref(this, 'groundY').get())):
        assign(ref(this, '_y'), '+=', lambda: ref(this, 'yAdd').get())
    else:
        assign(ref(this, '_x'), '+=', lambda: binop('*', ref(this, 'xAdd').get(), 3))
        assign(ref(this, '_alpha'), '-=', lambda: binop('*', ref(this, 'alphaDecay').get(), 2))
    assign(ref(this, '_alpha'), '-=', lambda: ref(this, 'alphaDecay').get())
    assign(ref(this, '_xscale'), '=', lambda: assign(ref(this, '_yscale'), '+=', lambda: ref(this, 'sizeDecay').get()))
    if truth(binop('<=', ref(this, '_alpha').get(), 0)):
        assign(ref(this, 'rootX'), '=', lambda: e.get('_rootX'))
        assign(ref(this, 'rootY'), '=', lambda: e.get('_rootY'))
        rt.call_ref(ref(this, 'spawn'), [])
    return U

def SpaceRocket_trail_element_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'SpaceRocket_trail_element')
    pass

def register(rt):
    rt.define('SpaceRocket_trail_element', 'MovieClip', SpaceRocket_trail_element_fields, {'SpaceRocket_trail_element': ASFunction(SpaceRocket_trail_element_SpaceRocket_trail_element), 'spawn': ASFunction(SpaceRocket_trail_element_spawn), 'setStep': ASFunction(SpaceRocket_trail_element_setStep)}, {}, {})
