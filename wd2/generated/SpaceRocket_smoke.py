# Generated from __Packages/SpaceRocket_smoke.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def SpaceRocket_smoke_SpaceRocket_smoke(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'SpaceRocket_smoke')
    e.call('__super__', [])
    assign(ref(this, 'groundY'), '=', lambda: ref(this, '_y').get())
    assign(ref(this, 'trailArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'interval_ID'), '=', lambda: rt.call_ref(ref(e.get('_global'), 'setInterval'), [this, 'removeTrail', 8000]))
    return U

def SpaceRocket_smoke_onEnterFrame(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'SpaceRocket_smoke')
    if truth(binop('>=', ref(this, 'offSet_toSpawn').get(), ref(this, 'offSet_toSpawn_max').get())):
        rt.call_ref(ref(this, 'addTrailElement'), [])
        assign(ref(this, 'trailCount'), '=', lambda: binop('+', ref(this, 'trailCount').get(), 1))
    else:
        assign(ref(this, 'offSet_toSpawn'), '=', lambda: binop('+', ref(this, 'offSet_toSpawn').get(), 1))
    rt.call_ref(ref(this, 'updateTrail'), [])
    return U

def SpaceRocket_smoke_addTrailElement(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'SpaceRocket_smoke')
    e.set('_loc2_', rt.call_ref(ref(ref(this, '_parent').get(), 'attachMovie'), ['spaceRocket_trail_element', binop('+', 'trail', ref(this, 'trailCount').get()), rt.call_ref(ref(ref(this, '_parent').get(), 'getNextHighestDepth'), [])]))
    assign(ref(e.get('_loc2_'), 'rootX'), '=', lambda: assign(ref(e.get('_loc2_'), '_x'), '=', lambda: ref(this, '_x').get()))
    assign(ref(e.get('_loc2_'), 'rootY'), '=', lambda: assign(ref(e.get('_loc2_'), '_y'), '=', lambda: ref(this, '_y').get()))
    assign(ref(e.get('_loc2_'), 'groundY'), '=', lambda: ref(this, 'groundY').get())
    rt.call_ref(ref(e.get('_loc2_'), 'spawn'), [])
    rt.call_ref(ref(ref(this, 'trailArr').get(), 'push'), [e.get('_loc2_')])
    return U

def SpaceRocket_smoke_updateTrail(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'SpaceRocket_smoke')
    for key_1 in keys(ref(this, 'trailArr').get()):
        e.ref('i').set(key_1)
        rt.tick()
        try:
            rt.call_ref(ref(ref(ref(this, 'trailArr').get(), e.get('i')).get(), 'setStep'), [ref(this, '_x').get(), ref(this, '_y').get()])
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def SpaceRocket_smoke_removeTrail(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['i'], closure, 'SpaceRocket_smoke')
    rt.call_ref(ref(e.get('_global'), 'clearInterval'), [ref(this, 'interval_ID').get()])
    assign(ref(this, 'onEnterFrame'), '=', lambda: e.get('undefined'))
    for key_2 in keys(ref(this, 'trailArr').get()):
        e.ref('i').set(key_2)
        rt.tick()
        try:
            rt.call_ref(ref(ref(ref(this, 'trailArr').get(), e.get('i')).get(), 'removeMovieClip'), [])
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def SpaceRocket_smoke_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'SpaceRocket_smoke')
    ref(this, 'trailCount').set(0)
    ref(this, 'trailCount_max').set(50)
    ref(this, 'offSet_toSpawn').set(0)
    ref(this, 'offSet_toSpawn_max').set(1)

def register(rt):
    rt.define('SpaceRocket_smoke', 'MovieClip', SpaceRocket_smoke_fields, {'SpaceRocket_smoke': ASFunction(SpaceRocket_smoke_SpaceRocket_smoke), 'onEnterFrame': ASFunction(SpaceRocket_smoke_onEnterFrame), 'addTrailElement': ASFunction(SpaceRocket_smoke_addTrailElement), 'updateTrail': ASFunction(SpaceRocket_smoke_updateTrail), 'removeTrail': ASFunction(SpaceRocket_smoke_removeTrail)}, {}, {})
