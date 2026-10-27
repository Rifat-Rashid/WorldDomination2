# Generated from __Packages/StockRequirements_list.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def StockRequirements_list_StockRequirements_list(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'StockRequirements_list')
    assign(ref(this, '_default'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(this, '_default').get(), 'active'), '=', lambda: False)
    assign(ref(ref(this, '_default').get(), 'state2_arr'), '=', lambda: arr(['false']))
    assign(ref(ref(this, '_default').get(), 'state4_arr'), '=', lambda: arr(['false']))
    assign(ref(this, 'resources'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(this, 'resources').get(), 'active'), '=', lambda: False)
    assign(ref(ref(this, 'resources').get(), 'state4_arr'), '=', lambda: arr(['false']))
    assign(ref(this, 'production'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(this, 'production').get(), 'active'), '=', lambda: False)
    assign(ref(ref(this, 'production').get(), 'state2_arr'), '=', lambda: arr(['false']))
    assign(ref(ref(this, 'production').get(), 'state4_arr'), '=', lambda: arr(['false']))
    assign(ref(this, 'research'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(this, 'research').get(), 'active'), '=', lambda: False)
    assign(ref(ref(this, 'research').get(), 'state2_arr'), '=', lambda: arr(['nextInvention']))
    assign(ref(ref(this, 'research').get(), 'state3_arr'), '=', lambda: arr(['nextInvention']))
    assign(ref(ref(this, 'research').get(), 'state4_arr'), '=', lambda: arr(['false']))
    assign(ref(this, 'religion'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(this, 'religion').get(), 'active'), '=', lambda: False)
    assign(ref(ref(this, 'religion').get(), 'state2_arr'), '=', lambda: arr(['false']))
    assign(ref(ref(this, 'religion').get(), 'state4_arr'), '=', lambda: arr(['false']))
    assign(ref(this, 'preAttack'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(this, 'preAttack').get(), 'active'), '=', lambda: True)
    assign(ref(ref(this, 'preAttack').get(), 'state2_arr'), '=', lambda: arr(['preAttackRelated', 'isActive', 'weaponInStock', 'isPayload_pre', 'isCarrier_pre']))
    assign(ref(ref(this, 'preAttack').get(), 'state3_arr'), '=', lambda: arr(['??']))
    assign(ref(ref(this, 'preAttack').get(), 'state4_arr'), '=', lambda: arr(['inactive']))
    assign(ref(this, 'attack'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(this, 'attack').get(), 'active'), '=', lambda: True)
    assign(ref(ref(this, 'attack').get(), 'state2_arr'), '=', lambda: arr(['attackRelated', 'isActive', 'weaponInStock', 'spy_allowed']))
    assign(ref(ref(this, 'attack').get(), 'state4_arr'), '=', lambda: arr(['inactive']))
    assign(ref(this, 'defense'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(this, 'defense').get(), 'active'), '=', lambda: True)
    assign(ref(ref(this, 'defense').get(), 'state2_arr'), '=', lambda: arr(['defenseRelated', 'weaponInStock']))
    assign(ref(ref(this, 'defense').get(), 'state4_arr'), '=', lambda: arr(['inactive']))
    assign(ref(this, 'propaganda'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(this, 'propaganda').get(), 'active'), '=', lambda: False)
    assign(ref(ref(this, 'propaganda').get(), 'state2_arr'), '=', lambda: arr(['false']))
    assign(ref(ref(this, 'propaganda').get(), 'state4_arr'), '=', lambda: arr(['false']))
    assign(ref(this, 'diplomacy'), '=', lambda: rt.construct(e.get('Object'), []))
    assign(ref(ref(this, 'diplomacy').get(), 'active'), '=', lambda: False)
    assign(ref(ref(this, 'diplomacy').get(), 'state2_arr'), '=', lambda: arr(['false']))
    assign(ref(ref(this, 'diplomacy').get(), 'state4_arr'), '=', lambda: arr(['false']))
    return U

def StockRequirements_list_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'StockRequirements_list')
    pass

def register(rt):
    rt.define('StockRequirements_list', None, StockRequirements_list_fields, {'StockRequirements_list': ASFunction(StockRequirements_list_StockRequirements_list)}, {}, {})
