# Generated from __Packages/StockBtn_data_obj.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def StockBtn_data_obj_StockBtn_data_obj(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_id', '_name', '_label', '_weaponName', '_stockPanelNum', '_deactivate_in_demo'], ['_deactivate_in_demo', '_id', '_label', '_name', '_stockPanelNum', '_weaponName'], closure, 'StockBtn_data_obj')
    assign(ref(this, 'id'), '=', lambda: e.get('_id'))
    assign(ref(this, 'name'), '=', lambda: e.get('_name'))
    assign(ref(this, 'label'), '=', lambda: e.get('_label'))
    assign(ref(this, 'weaponName'), '=', lambda: e.get('_weaponName'))
    assign(ref(this, 'stockPanelNum'), '=', lambda: e.get('_stockPanelNum'))
    assign(ref(this, 'deactivate_in_demo'), '=', lambda: e.get('_deactivate_in_demo'))
    return U

def StockBtn_data_obj_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'StockBtn_data_obj')
    pass

def register(rt):
    rt.define('StockBtn_data_obj', None, StockBtn_data_obj_fields, {'StockBtn_data_obj': ASFunction(StockBtn_data_obj_StockBtn_data_obj)}, {}, {})
