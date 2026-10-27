# Generated from __Packages/Cloud.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Cloud_Cloud(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Cloud')
    e.call('__super__', [])
    assign(ref(this, '_startLoc'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(this, '_pivotLoc'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(this, '_x'), '=', lambda: 0)
    assign(ref(this, '_y'), '=', lambda: 0)
    return U

def Cloud___set__angleChange(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_num'], ['_num'], closure, 'Cloud')
    assign(ref(this, '_angleChange'), '=', lambda: binop('/', e.get('_num'), 10))
    return U

def Cloud___get__angleChange(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Cloud')
    return ref(this, '_angleChange').get()
    return U

def Cloud___set__startLoc(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_obj'], ['_obj'], closure, 'Cloud')
    assign(ref(ref(this, '_pivotLoc').get(), '_x'), '=', lambda: assign(ref(ref(this, '_startLoc').get(), '_x'), '=', lambda: ref(e.get('_obj'), '_x').get()))
    assign(ref(ref(this, '_pivotLoc').get(), '_y'), '=', lambda: assign(ref(ref(this, '_startLoc').get(), '_y'), '=', lambda: ref(e.get('_obj'), '_y').get()))
    return U

def Cloud_initialLoc(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Cloud')
    assign(ref(this, '_x'), '=', lambda: ref(ref(this, '_startLoc').get(), '_x').get())
    assign(ref(this, '_y'), '=', lambda: ref(ref(this, '_startLoc').get(), '_y').get())
    return U

def Cloud___get__startLoc(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Cloud')
    return ref(this, '_startLoc').get()
    return U

def Cloud_frame_step(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Cloud')
    rt.call_ref(ref(this, 'pivot_step'), [])
    e.set('_loc2_', binop('*', ref(this, '_angle').get(), binop('/', ref(e.get('Math'), 'PI').get(), 180)))
    assign(ref(this, '_x'), '=', lambda: binop('+', ref(ref(this, '_pivotLoc').get(), '_x').get(), binop('*', ref(this, 'xRadius').get(), rt.call_ref(ref(e.get('Math'), 'cos'), [e.get('_loc2_')]))))
    assign(ref(this, '_y'), '=', lambda: binop('+', ref(ref(this, '_pivotLoc').get(), '_y').get(), binop('*', ref(this, 'yRadius').get(), rt.call_ref(ref(e.get('Math'), 'sin'), [e.get('_loc2_')]))))
    assign(ref(this, '_angle'), '+=', lambda: ref(this, 'angleChange').get())
    assign(ref(this, '_angle'), '%=', lambda: 360)
    return U

def Cloud_pivot_step(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Cloud')
    e.set('_loc2_', binop('*', ref(this, '_pivotAngle').get(), binop('/', ref(e.get('Math'), 'PI').get(), 180)))
    assign(ref(ref(this, '_pivotLoc').get(), '_x'), '=', lambda: binop('+', ref(ref(this, '_startLoc').get(), '_x').get(), binop('*', 40, rt.call_ref(ref(e.get('Math'), 'cos'), [e.get('_loc2_')]))))
    assign(ref(ref(this, '_pivotLoc').get(), '_y'), '=', lambda: binop('+', ref(ref(this, '_startLoc').get(), '_y').get(), binop('*', 70, rt.call_ref(ref(e.get('Math'), 'sin'), [e.get('_loc2_')]))))
    assign(ref(this, '_pivotAngle'), '+=', lambda: 0.1)
    assign(ref(this, '_pivotAngle'), '%=', lambda: 360)
    return U

def Cloud___get__dist(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Cloud')
    return rt.call_ref(ref(e.get('Math'), 'sqrt'), [binop('+', binop('*', binop('-', ref(this, '_x').get(), ref(ref(this, '_startLoc').get(), '_x').get()), binop('-', ref(this, '_x').get(), ref(ref(this, '_startLoc').get(), '_x').get())), binop('*', binop('-', ref(this, '_y').get(), ref(ref(this, '_startLoc').get(), '_y').get()), binop('-', ref(this, '_y').get(), ref(ref(this, '_startLoc').get(), '_y').get())))])
    return U

def Cloud___set__curPosByObj(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_obj'], ['_obj'], closure, 'Cloud')
    assign(ref(this, '_x'), '=', lambda: ref(e.get('_obj'), '_x').get())
    assign(ref(this, '_y'), '=', lambda: ref(e.get('_obj'), '_y').get())
    return U

def Cloud___set__frameLocOffset(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_obj'], ['_obj'], closure, 'Cloud')
    assign(ref(this, '_frameLocOffset'), '=', lambda: e.get('_obj'))
    return U

def Cloud_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Cloud')
    ref(this, '_angle').set(0)
    ref(this, 'xRadius').set(20)
    ref(this, 'yRadius').set(20)
    ref(this, '_angleChange').set(1)
    ref(this, '_pivotAngle').set(0)
    ref(this, 'completeCloud_angle').set(0)

def register(rt):
    rt.define('Cloud', 'MovieClip', Cloud_fields, {'Cloud': ASFunction(Cloud_Cloud), 'initialLoc': ASFunction(Cloud_initialLoc), 'frame_step': ASFunction(Cloud_frame_step), 'pivot_step': ASFunction(Cloud_pivot_step)}, {'angleChange': ASFunction(Cloud___get__angleChange), 'startLoc': ASFunction(Cloud___get__startLoc), 'dist': ASFunction(Cloud___get__dist)}, {'angleChange': ASFunction(Cloud___set__angleChange), 'startLoc': ASFunction(Cloud___set__startLoc), 'curPosByObj': ASFunction(Cloud___set__curPosByObj), 'frameLocOffset': ASFunction(Cloud___set__frameLocOffset)})
