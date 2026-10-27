# Generated from __Packages/Option.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Option_Option(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Option')
    return U

def Option_setSound(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Option')
    if truth(unary('!', ref(this, 'sound').get())):
        assign(ref(this, 'sound'), '=', lambda: True)
    else:
        assign(ref(this, 'sound'), '=', lambda: False)
    return U

def Option___get__playSound(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Option')
    return ref(this, 'sound').get()
    return U

def Option_setMusic(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Option')
    if truth(unary('!', ref(this, 'music').get())):
        assign(ref(this, 'music'), '=', lambda: True)
    else:
        assign(ref(this, 'music'), '=', lambda: False)
    return U

def Option___get__playMusic(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Option')
    return ref(this, 'music').get()
    return U

def Option_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Option')
    ref(this, 'sound').set(True)
    ref(this, 'music').set(True)

def register(rt):
    rt.define('Option', None, Option_fields, {'Option': ASFunction(Option_Option), 'setSound': ASFunction(Option_setSound), 'setMusic': ASFunction(Option_setMusic)}, {'playSound': ASFunction(Option___get__playSound), 'playMusic': ASFunction(Option___get__playMusic)}, {})
