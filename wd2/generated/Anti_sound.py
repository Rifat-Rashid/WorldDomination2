# Generated from __Packages/Anti_sound.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Anti_sound_Anti_sound(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Anti_sound')
    e.call('__super__', [])
    return U

def Anti_sound_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Anti_sound')
    ref(this, 'done').set(True)

def register(rt):
    rt.define('Anti_sound', 'Sound', Anti_sound_fields, {'Anti_sound': ASFunction(Anti_sound_Anti_sound)}, {}, {})
