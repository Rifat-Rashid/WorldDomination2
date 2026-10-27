# Generated from __Packages/Unit.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def Unit_Unit(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_unitID', 'param_container', 'param_targetType', 'param_newName', 'param_startX', 'param_startY', 'param_wayPointArr', 'param_result', 'param_tail', 'param_tailNum', 'param_force_MC', 'param_colorTrans', 'param_startNum', 'param_depth', 'param_targetPlayer', 'param_tr', 'param_playerNum', 'param_colorName', 'param_wildCard', 'param_explosion_mc_name'], ['_loc0_', '_loc22_', '_temp_1', '_temp_10', '_temp_11', '_temp_12', '_temp_13', '_temp_14', '_temp_15', '_temp_16', '_temp_17', '_temp_18', '_temp_19', '_temp_2', '_temp_20', '_temp_21', '_temp_22', '_temp_23', '_temp_24', '_temp_3', '_temp_4', '_temp_5', '_temp_6', '_temp_7', '_temp_8', '_temp_9', 'param_colorName', 'param_colorTrans', 'param_container', 'param_depth', 'param_explosion_mc_name', 'param_force_MC', 'param_newName', 'param_playerNum', 'param_result', 'param_startNum', 'param_startX', 'param_startY', 'param_tail', 'param_tailNum', 'param_targetPlayer', 'param_targetType', 'param_tr', 'param_unitID', 'param_wayPointArr', 'param_wildCard'], closure, 'Unit')
    assign(ref(this, 'xTargetStep'), '=', lambda: 0)
    assign(ref(this, 'yTargetStep'), '=', lambda: 0)
    assign(ref(this, 'targetX'), '=', lambda: 0)
    assign(ref(this, 'targetY'), '=', lambda: 0)
    assign(ref(this, 'curX'), '=', lambda: 0)
    assign(ref(this, 'curY'), '=', lambda: 0)
    assign(ref(this, 'prevX'), '=', lambda: 0)
    assign(ref(this, 'prevY'), '=', lambda: 0)
    assign(ref(this, 'adjside'), '=', lambda: 0)
    assign(ref(this, 'oppside'), '=', lambda: 0)
    assign(ref(this, 'angle'), '=', lambda: 0)
    assign(ref(this, 'xDist'), '=', lambda: 0)
    assign(ref(this, 'yDist'), '=', lambda: 0)
    assign(ref(this, 'step'), '=', lambda: 0)
    assign(ref(this, 'xStep'), '=', lambda: 0)
    assign(ref(this, 'yStep'), '=', lambda: 0)
    assign(ref(this, 'unloadTimer'), '=', lambda: 0)
    assign(ref(this, 'curWayPoint'), '=', lambda: 0)
    assign(ref(this, 'curShootOffset'), '=', lambda: 0)
    assign(ref(this, 'maxShootOffset'), '=', lambda: 0)
    assign(ref(this, 'unloadTailCount'), '=', lambda: 0)
    assign(ref(this, 'unloadNum'), '=', lambda: 0)
    assign(ref(this, 'multiFrame'), '=', lambda: False)
    assign(ref(this, 'atTarget'), '=', lambda: False)
    assign(ref(this, 'visible'), '=', lambda: True)
    assign(ref(this, 'countDownToStop'), '=', lambda: 250)
    assign(ref(this, 'shotCount'), '=', lambda: 0)
    assign(ref(this, 'dropCount'), '=', lambda: 0)
    assign(ref(this, 'trailActive'), '=', lambda: False)
    assign(ref(this, 'framesActive'), '=', lambda: 0)
    assign(ref(this, 'trailStart'), '=', lambda: False)
    assign(ref(this, 'curCountToStop'), '=', lambda: 0)
    assign(ref(this, 'unitStatus'), '=', lambda: 'alive')
    assign(ref(this, 'activeAndMoving'), '=', lambda: True)
    assign(ref(this, 'anti_initiated'), '=', lambda: False)
    assign(ref(this, 'anti_life_count'), '=', lambda: 0)
    assign(ref(this, 'anti_pos'), '=', lambda: arr([0, 0]))
    assign(ref(this, 'anti_mc_name'), '=', lambda: '')
    assign(ref(this, 'xyArr'), '=', lambda: rt.construct(e.get('Array'), [arr([0, 0]), arr([0, 0])]))
    assign(ref(this, 'unitID'), '=', lambda: e.get('param_unitID'))
    assign(ref(this, 'startX'), '=', lambda: e.get('param_startX'))
    assign(ref(this, 'startY'), '=', lambda: e.get('param_startY'))
    assign(ref(this, 'targetPlayer'), '=', lambda: e.get('param_targetPlayer'))
    assign(ref(this, 'tr'), '=', lambda: e.get('param_tr'))
    assign(ref(this, 'trailArr'), '=', lambda: rt.construct(e.get('Array'), []))
    assign(ref(this, 'playerNum'), '=', lambda: e.get('param_playerNum'))
    assign(ref(this, 'colorName'), '=', lambda: e.get('param_colorName'))
    assign(ref(this, 'wildCard'), '=', lambda: e.get('param_wildCard'))
    assign(ref(this, 'explosion_mc_name'), '=', lambda: e.get('param_explosion_mc_name'))
    if truth(e.get('param_force_MC')):
        assign(e.ref('param_targetType'), '=', lambda: e.get('param_force_MC'))
    if truth(ref(ref(this, 'wildCard').get(), 'anti').get()):
        assign(ref(this, 'anti_active'), '=', lambda: True)
        assign(ref(this, 'anti_num'), '=', lambda: ref(ref(this, 'wildCard').get(), 'antiNum').get())
    else:
        assign(ref(this, 'anti_active'), '=', lambda: False)
    assign(ref(this, 'colorTrans'), '=', lambda: e.get('param_colorTrans'))
    assign(ref(this, 'shadowXOffset'), '=', lambda: 0)
    assign(ref(this, 'shadowYOffset'), '=', lambda: 0)
    assign(ref(this, 'startNum'), '=', lambda: e.get('param_startNum'))
    assign(ref(this, 'plane_angle_step'), '=', lambda: ref(e.get('param_wildCard'), 'plane_angle_step').get())
    assign(ref(this, 'plane_angle_start'), '=', lambda: assign(ref(this, 'plane_cur_angle_in_circular_flight'), '=', lambda: ref(e.get('param_wildCard'), 'plane_angle_start').get()))
    assign(ref(this, 'plane_circular_modifier'), '=', lambda: ref(ref(this, 'wildCard').get(), 'circular_modifier_center').get())
    assign(ref(this, 'plane_circular_radius'), '=', lambda: logical('||', ref(ref(this, 'wildCard').get(), 'circular_radius').get(), lambda: 100))
    switch_1 = e.get('param_targetType')
    case_2 = -1
    if case_2 == -1 and strict_eq(switch_1, 'plane1'):
        case_2 = 0
    if case_2 == -1 and strict_eq(switch_1, 'plane2'):
        case_2 = 1
    if case_2 == -1 and strict_eq(switch_1, 'ship_plane'):
        case_2 = 2
    if case_2 == -1 and strict_eq(switch_1, 'boat'):
        case_2 = 3
    if case_2 == -1 and strict_eq(switch_1, 'chinook'):
        case_2 = 4
    if case_2 == -1 and strict_eq(switch_1, 'apache'):
        case_2 = 5
    if case_2 == -1 and strict_eq(switch_1, 'soldier'):
        case_2 = 6
    if case_2 == -1 and strict_eq(switch_1, 'tank_noShade'):
        case_2 = 7
    if case_2 == -1 and strict_eq(switch_1, 'tankTop'):
        case_2 = 8
    if case_2 == -1 and strict_eq(switch_1, 'marine'):
        case_2 = 9
    if case_2 == -1 and strict_eq(switch_1, 'suicide_bomber'):
        case_2 = 10
    if case_2 == -1 and strict_eq(switch_1, 'rocket'):
        case_2 = 11
    if case_2 == -1 and strict_eq(switch_1, 'sub_rocket'):
        case_2 = 12
    if case_2 == -1 and strict_eq(switch_1, 'plane2'):
        case_2 = 13
    if case_2 == -1 and strict_eq(switch_1, 'space'):
        case_2 = 14
    if case_2 == -1:
        case_2 = -1
    try:
        if 0 <= case_2 <= 0:
            assign(ref(this, 'action'), '=', lambda: 'liftOff')
            assign(ref(this, 'mcID'), '=', lambda: 'plane001')
            assign(ref(this, 'step'), '=', lambda: 12)
            assign(ref(this, 'range'), '=', lambda: 40)
            assign(ref(this, 'x_multiplier'), '=', lambda: logical('||', ref(ref(this, 'wildCard').get(), 'x_multiplier').get(), lambda: 0.5))
            assign(ref(this, 'y_multiplier'), '=', lambda: logical('||', ref(ref(this, 'wildCard').get(), 'y_multiplier').get(), lambda: 2))
            assign(ref(this, 'frameCount'), '=', lambda: 24)
            assign(ref(this, 'liftOff'), '=', lambda: True)
            assign(ref(this, 'hasShadow'), '=', lambda: True)
            assign(ref(this, 'tintMC_id'), '=', lambda: 'plane001_tint')
            assign(ref(this, 'shadowMC_id'), '=', lambda: 'plane001_shadow')
            assign(ref(this, 'shadowXOffset'), '=', lambda: 0)
            assign(ref(this, 'shadowYOffset'), '=', lambda: 0)
            assign(ref(this, 'activeAndMoving'), '=', lambda: True)
            assign(ref(this, 'trailCount'), '=', lambda: 1)
            assign(ref(this, 'trailCountDown'), '=', lambda: 5)
            assign(ref(this, 'trailSize'), '=', lambda: 50)
            assign(ref(this, 'trail_offset'), '=', lambda: 25)
            assign(ref(this, 'anti_type'), '=', lambda: 'air')
            assign(ref(this, 'anti_offset'), '=', lambda: 0)
            raise ASBreak()
        if 0 <= case_2 <= 1:
            assign(ref(this, 'action'), '=', lambda: 'liftOff')
            assign(ref(this, 'mcID'), '=', lambda: 'plane002')
            assign(ref(this, 'tintMC_id'), '=', lambda: 'plane002_tint')
            assign(ref(this, 'shadowMC_id'), '=', lambda: 'plane002_shadow')
            assign(ref(this, 'step'), '=', lambda: 12)
            assign(ref(this, 'range'), '=', lambda: 40)
            assign(ref(this, 'x_multiplier'), '=', lambda: logical('||', ref(ref(this, 'wildCard').get(), 'x_multiplier').get(), lambda: 0.5))
            assign(ref(this, 'y_multiplier'), '=', lambda: logical('||', ref(ref(this, 'wildCard').get(), 'y_multiplier').get(), lambda: 2))
            assign(ref(this, 'frameCount'), '=', lambda: 24)
            assign(ref(this, 'liftOff'), '=', lambda: True)
            assign(ref(this, 'trailCountDown'), '=', lambda: 1)
            assign(ref(this, 'trailCount'), '=', lambda: 2)
            assign(ref(this, 'trailSize'), '=', lambda: 22)
            assign(ref(this, 'hasShadow'), '=', lambda: True)
            assign(ref(this, 'anti_type'), '=', lambda: 'air')
            assign(ref(this, 'anti_offset'), '=', lambda: 0)
            raise ASBreak()
        if 0 <= case_2 <= 2:
            assign(ref(this, 'action'), '=', lambda: 'waitForLiftOff')
            assign(ref(this, 'mcID'), '=', lambda: 'ship_plane')
            assign(ref(this, 'trailCount'), '=', lambda: 2)
            assign(ref(this, 'trailSize'), '=', lambda: 8)
            assign(ref(this, 'trailMultiplier'), '=', lambda: 4)
            assign(ref(this, 'step'), '=', lambda: 10)
            assign(ref(this, 'range'), '=', lambda: 40)
            assign(ref(this, 'x_multiplier'), '=', lambda: 1)
            assign(ref(this, 'y_multiplier'), '=', lambda: 2)
            assign(ref(this, 'frameCount'), '=', lambda: 24)
            assign(ref(this, 'liftOff'), '=', lambda: True)
            assign(ref(this, 'hasShadow'), '=', lambda: True)
            assign(ref(this, 'tintMC_id'), '=', lambda: 'plane001_tint')
            assign(ref(this, 'shadowMC_id'), '=', lambda: 'plane001_shadow')
            assign(ref(this, 'activeAndMoving'), '=', lambda: True)
            assign(ref(this, 'trailCount'), '=', lambda: 1)
            assign(ref(this, 'trailCountDown'), '=', lambda: 5)
            assign(ref(this, 'anti_type'), '=', lambda: 'air')
            assign(ref(this, 'trailSize'), '=', lambda: 50)
            assign(ref(ref(this, 'wildCard').get(), 'liftOffCount'), '=', lambda: 0)
            assign(ref(this, 'idleFrame'), '=', lambda: 4)
            raise ASBreak()
        if 0 <= case_2 <= 3:
            assign(ref(this, 'unloadMax'), '=', lambda: 4)
            assign(ref(this, 'range'), '=', lambda: 15)
            assign(ref(this, 'action'), '=', lambda: 'default')
            assign(ref(this, 'mcID'), '=', lambda: 'boat001')
            assign(ref(this, 'tintMC_id'), '=', lambda: 'boat001_tint')
            assign(ref(this, 'step'), '=', lambda: 7)
            assign(ref(this, 'x_multiplier'), '=', lambda: 2)
            assign(ref(this, 'y_multiplier'), '=', lambda: 2)
            assign(ref(this, 'frameCount'), '=', lambda: 18)
            assign(ref(this, 'hasShadow'), '=', lambda: False)
            assign(ref(this, 'depthSwap'), '=', lambda: True)
            assign(ref(this, 'startSoundOnAAM'), '=', lambda: True)
            assign(ref(this, 'startSoundAction'), '=', lambda: 'boat_start')
            assign(ref(this, 'floorFrame'), '=', lambda: True)
            assign(ref(this, 'cancelBib'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_2 <= 4:
            assign(ref(this, 'unloadMax'), '=', lambda: 2)
            assign(ref(this, 'range'), '=', lambda: 25)
            assign(ref(this, 'action'), '=', lambda: 'waitForHeliStart')
            assign(ref(this, 'mcID'), '=', lambda: 'chinook')
            assign(ref(this, 'shadowMC_id'), '=', lambda: 'chinook_shadow')
            assign(ref(this, 'step'), '=', lambda: 8)
            assign(ref(this, 'x_multiplier'), '=', lambda: 2)
            assign(ref(this, 'y_multiplier'), '=', lambda: 2)
            assign(ref(this, 'frameCount'), '=', lambda: 18)
            assign(ref(this, 'multiFrame'), '=', lambda: True)
            assign(ref(this, 'frameOffset'), '=', lambda: 0)
            assign(ref(this, 'hasShadow'), '=', lambda: True)
            assign(ref(this, 'shadowXOffset'), '=', lambda: 0)
            assign(ref(this, 'shadowYOffset'), '=', lambda: 70)
            assign(ref(this, 'offsetFrames'), '=', lambda: 2)
            assign(ref(this, 'heliStartPlusX'), '=', lambda: 15)
            assign(ref(this, 'heliStartPlusY'), '=', lambda: unary('-', 100))
            assign(ref(this, 'fixedFrame'), '=', lambda: 4)
            raise ASBreak()
        if 0 <= case_2 <= 5:
            assign(ref(this, 'unloadMax'), '=', lambda: 4)
            assign(ref(this, 'range'), '=', lambda: 25)
            assign(ref(this, 'action'), '=', lambda: 'waitForHeliStart')
            assign(ref(this, 'mcID'), '=', lambda: 'apache')
            assign(ref(this, 'hasShadow'), '=', lambda: True)
            assign(ref(this, 'step'), '=', lambda: 8)
            assign(ref(this, 'x_multiplier'), '=', lambda: 2)
            assign(ref(this, 'y_multiplier'), '=', lambda: 2)
            assign(ref(this, 'frameCount'), '=', lambda: 18)
            assign(ref(this, 'multiFrame'), '=', lambda: True)
            assign(ref(this, 'frameOffset'), '=', lambda: 0)
            assign(ref(this, 'offsetFrames'), '=', lambda: 2)
            assign(ref(this, 'tintMC_id'), '=', lambda: 'apache_tint')
            assign(ref(this, 'shadowMC_id'), '=', lambda: 'apache_shadow')
            assign(ref(this, 'shadowXOffsetMax'), '=', lambda: 0)
            assign(ref(this, 'shadowYOffsetMax'), '=', lambda: 70)
            assign(ref(this, 'shadowXOffset'), '=', lambda: 0)
            assign(ref(this, 'shadowYOffset'), '=', lambda: 0)
            assign(ref(this, 'shadowStartAtUnitBase'), '=', lambda: True)
            assign(ref(this, 'heliStartPlusX'), '=', lambda: 25)
            assign(ref(this, 'heliStartPlusY'), '=', lambda: unary('-', 25))
            assign(ref(this, 'startSoundOnAAM'), '=', lambda: True)
            assign(ref(this, 'startSoundAction'), '=', lambda: 'apache_start')
            raise ASBreak()
        if 0 <= case_2 <= 6:
            assign(ref(this, 'range'), '=', lambda: 2)
            assign(ref(this, 'action'), '=', lambda: 'default')
            assign(ref(this, 'mcID'), '=', lambda: 'soldier001')
            assign(ref(this, 'step'), '=', lambda: 4)
            assign(ref(this, 'x_multiplier'), '=', lambda: 0.5)
            assign(ref(this, 'y_multiplier'), '=', lambda: 0.4)
            assign(ref(this, 'frameCount'), '=', lambda: 18)
            assign(ref(this, 'multiFrame'), '=', lambda: True)
            assign(ref(this, 'frameOffset'), '=', lambda: 1)
            assign(ref(this, 'hasShadow'), '=', lambda: False)
            assign(ref(this, 'offsetFrames'), '=', lambda: 12)
            assign(ref(this, 'visible'), '=', lambda: False)
            assign(ref(this, 'activeAndMoving'), '=', lambda: False)
            assign(ref(this, 'maxShotCount'), '=', lambda: 75)
            assign(ref(this, 'maxShootOffset'), '=', lambda: 4)
            assign(ref(this, 'schootMCID'), '=', lambda: 'soldier001_shoot')
            assign(ref(this, 'tintMC_id'), '=', lambda: 'soldier001_tint')
            assign(ref(this, 'shootTintMC_id'), '=', lambda: 'soldier001_shoot_tint')
            assign(ref(this, 'depthSwap'), '=', lambda: True)
            assign(ref(this, 'startSoundOnAAM'), '=', lambda: True)
            assign(ref(this, 'startSoundAction'), '=', lambda: 'soldier_running')
            assign(ref(this, 'instantTurn'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_2 <= 7:
            assign(ref(this, 'range'), '=', lambda: 10)
            assign(ref(this, 'action'), '=', lambda: 'tail')
            assign(ref(this, 'mcID'), '=', lambda: 'tank_noShade')
            assign(ref(this, 'step'), '=', lambda: 2)
            assign(ref(this, 'x_multiplier'), '=', lambda: 2)
            assign(ref(this, 'y_multiplier'), '=', lambda: 2)
            assign(ref(this, 'frameCount'), '=', lambda: 18)
            assign(ref(this, 'multiFrame'), '=', lambda: False)
            assign(ref(this, 'frameOffset'), '=', lambda: 1)
            assign(ref(this, 'hasShadow'), '=', lambda: False)
            assign(ref(this, 'activeAndMoving'), '=', lambda: False)
            assign(ref(this, 'dropDistance'), '=', lambda: 20)
            assign(ref(this, 'depthSwap'), '=', lambda: True)
            assign(ref(this, 'instantTurn'), '=', lambda: False)
            assign(ref(this, 'floorFrame'), '=', lambda: True)
            assign(ref(this, 'cancelBib'), '=', lambda: True)
            assign(ref(this, 'maxShotCount'), '=', lambda: 60)
            raise ASBreak()
        if 0 <= case_2 <= 8:
            assign(ref(this, 'action'), '=', lambda: 'tail')
            assign(ref(this, 'mcID'), '=', lambda: 'tankTop')
            assign(ref(this, 'step'), '=', lambda: 4)
            assign(ref(this, 'x_multiplier'), '=', lambda: 0.5)
            assign(ref(this, 'y_multiplier'), '=', lambda: 0.4)
            assign(ref(this, 'frameCount'), '=', lambda: 18)
            assign(ref(this, 'multiFrame'), '=', lambda: False)
            assign(ref(this, 'frameOffset'), '=', lambda: 1)
            assign(ref(this, 'hasShadow'), '=', lambda: False)
            assign(ref(this, 'activeAndMoving'), '=', lambda: False)
            assign(ref(this, 'depthSwap'), '=', lambda: True)
            assign(ref(this, 'instantTurn'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_2 <= 9:
            assign(ref(this, 'range'), '=', lambda: 10)
            assign(ref(this, 'action'), '=', lambda: 'default')
            assign(ref(this, 'mcID'), '=', lambda: 'marine')
            assign(ref(this, 'step'), '=', lambda: 4)
            assign(ref(this, 'x_multiplier'), '=', lambda: 0.5)
            assign(ref(this, 'y_multiplier'), '=', lambda: 0.4)
            assign(ref(this, 'frameCount'), '=', lambda: 18)
            assign(ref(this, 'multiFrame'), '=', lambda: True)
            assign(ref(this, 'frameOffset'), '=', lambda: 1)
            assign(ref(this, 'hasShadow'), '=', lambda: False)
            assign(ref(this, 'offsetFrames'), '=', lambda: 12)
            assign(ref(this, 'visible'), '=', lambda: False)
            assign(ref(this, 'activeAndMoving'), '=', lambda: False)
            assign(ref(this, 'maxShotCount'), '=', lambda: 60)
            assign(ref(this, 'maxShootOffset'), '=', lambda: 4)
            assign(ref(this, 'schootMCID'), '=', lambda: 'soldier001_shoot')
            assign(ref(this, 'tintMC_id'), '=', lambda: 'soldier001_tint')
            assign(ref(this, 'shootTintMC_id'), '=', lambda: 'soldier001_shoot_tint')
            assign(ref(this, 'depthSwap'), '=', lambda: True)
            assign(ref(this, 'startSoundOnAAM'), '=', lambda: True)
            assign(ref(this, 'startSoundAction'), '=', lambda: 'soldier_running')
            assign(ref(this, 'instantTurn'), '=', lambda: False)
            raise ASBreak()
        if 0 <= case_2 <= 10:
            assign(ref(this, 'range'), '=', lambda: 10)
            assign(ref(this, 'action'), '=', lambda: 'waitForHeliStart')
            assign(ref(this, 'mcID'), '=', lambda: 'suicide_bomber')
            assign(ref(this, 'step'), '=', lambda: 4)
            assign(ref(this, 'x_multiplier'), '=', lambda: 0.5)
            assign(ref(this, 'y_multiplier'), '=', lambda: 0.4)
            assign(ref(this, 'frameCount'), '=', lambda: 18)
            assign(ref(this, 'multiFrame'), '=', lambda: True)
            assign(ref(this, 'frameOffset'), '=', lambda: 1)
            assign(ref(this, 'hasShadow'), '=', lambda: False)
            assign(ref(this, 'offsetFrames'), '=', lambda: 12)
            assign(ref(this, 'activeAndMoving'), '=', lambda: False)
            assign(ref(this, 'maxShotCount'), '=', lambda: 60)
            assign(ref(this, 'maxShootOffset'), '=', lambda: 4)
            assign(ref(this, 'tintMC_id'), '=', lambda: 'suicide_bomber_tint')
            assign(ref(this, 'heliStartPlusX'), '=', lambda: 25)
            assign(ref(this, 'heliStartPlusY'), '=', lambda: unary('-', 50))
            assign(ref(this, 'depthSwap'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_2 <= 11:
            assign(ref(this, 'range'), '=', lambda: 14)
            assign(ref(this, 'action'), '=', lambda: 'default')
            assign(ref(this, 'mcID'), '=', lambda: 'rocket')
            assign(ref(this, 'step'), '=', lambda: 4)
            assign(ref(this, 'x_multiplier'), '=', lambda: 3)
            assign(ref(this, 'y_multiplier'), '=', lambda: 2)
            assign(ref(this, 'frameCount'), '=', lambda: 18)
            assign(ref(this, 'multiFrame'), '=', lambda: False)
            assign(ref(this, 'hasShadow'), '=', lambda: False)
            assign(ref(this, 'visible'), '=', lambda: True)
            assign(ref(this, 'activeAndMoving'), '=', lambda: True)
            assign(ref(this, 'trailCount'), '=', lambda: 1)
            assign(ref(this, 'trailSize'), '=', lambda: 50)
            assign(ref(this, 'trailMultiplier'), '=', lambda: 20)
            assign(ref(this, 'trailCountDown'), '=', lambda: 5)
            assign(ref(this, 'startSoundOnAAM'), '=', lambda: True)
            assign(ref(this, 'startSoundAction'), '=', lambda: 'rocket_launch')
            assign(ref(this, 'anti_type'), '=', lambda: 'rocket')
            raise ASBreak()
        if 0 <= case_2 <= 12:
            assign(ref(this, 'range'), '=', lambda: 14)
            assign(ref(this, 'action'), '=', lambda: 'default')
            assign(ref(this, 'mcID'), '=', lambda: 'sub_rocket')
            assign(ref(this, 'step'), '=', lambda: 4)
            assign(ref(this, 'x_multiplier'), '=', lambda: 3)
            assign(ref(this, 'y_multiplier'), '=', lambda: 2)
            assign(ref(this, 'frameCount'), '=', lambda: 18)
            assign(ref(this, 'multiFrame'), '=', lambda: False)
            assign(ref(this, 'hasShadow'), '=', lambda: False)
            assign(ref(this, 'visible'), '=', lambda: True)
            assign(ref(this, 'activeAndMoving'), '=', lambda: True)
            assign(ref(this, 'trailCount'), '=', lambda: 1)
            assign(ref(this, 'trailSize'), '=', lambda: 50)
            assign(ref(this, 'trailMultiplier'), '=', lambda: 20)
            assign(ref(this, 'trailCountDown'), '=', lambda: 5)
            assign(ref(this, 'startSoundOnAAM'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_2 <= 13:
            assign(ref(this, 'action'), '=', lambda: 'liftOff')
            assign(ref(this, 'mcID'), '=', lambda: 'plane002')
            assign(ref(this, 'tintMC_id'), '=', lambda: 'plane002_tint')
            assign(ref(this, 'shadowMC_id'), '=', lambda: 'plane002_shadow')
            assign(ref(this, 'step'), '=', lambda: 10)
            assign(ref(this, 'range'), '=', lambda: 60)
            assign(ref(this, 'x_multiplier'), '=', lambda: 0.5)
            assign(ref(this, 'y_multiplier'), '=', lambda: 0.7)
            assign(ref(this, 'frameCount'), '=', lambda: 24)
            assign(ref(this, 'liftOff'), '=', lambda: True)
            assign(ref(this, 'trailCountDown'), '=', lambda: 1)
            assign(ref(this, 'trailCount'), '=', lambda: 2)
            assign(ref(this, 'trailSize'), '=', lambda: 22)
            assign(ref(this, 'hasShadow'), '=', lambda: True)
            raise ASBreak()
        if 0 <= case_2 <= 14:
            assign(ref(this, 'action'), '=', lambda: 'wait')
            assign(ref(this, 'mcID'), '=', lambda: 'satellite')
    except ASBreak:
        pass
    assign(ref(this, 'container'), '=', lambda: e.get('param_container'))
    assign(ref(this, 'unitName'), '=', lambda: e.get('param_newName'))
    if truth(ref(this, 'depthSwap').get()):
        assign(ref(this, 'depth_'), '=', lambda: e.get('param_depth'))
    else:
        if truth(binop('==', ref(this, 'mcID').get(), 'sattelite')):
            assign(ref(this, 'depth_'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), []))
        else:
            assign(ref(this, 'depth_'), '=', lambda: binop('+', 800000, e.get('param_depth')))
    if truth(binop('==', ref(this, 'mcID').get(), 'tankTop')):
        assign(ref(this, 'MC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), [binop('+', binop('+', ref(this, 'mcID').get(), '_'), ref(this, 'colorName').get()), ref(this, 'unitName').get(), ref(this, 'depth_').get()]))
    else:
        if truth(ref(ref(this, 'wildCard').get(), '_number').get()):
            assign(ref(this, 'MC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), [ref(this, 'mcID').get(), ref(this, 'unitName').get(), binop('+', ref(this, 'depth_').get(), ref(ref(this, 'wildCard').get(), '_number').get())]))
        else:
            if truth(binop('==', ref(this, 'mcID').get(), 'sub_rocket')):
                assign(ref(this, 'MC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), ['rocket', ref(this, 'unitName').get(), rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), [])]))
                e.set('_temp_2', ref(this, 'MC').get())
                e.set('_temp_1', '_x')
                assign(ref(ref(this, 'MC').get(), '_yscale'), '=', lambda: assign(e.ref('_loc0_'), '=', lambda: 50))
                assign(ref(e.get('_temp_2'), e.get('_temp_1')), '=', lambda: e.get('_loc0_'))
                assign(ref(this, 'action'), '=', lambda: 'wait_for_sub_launch')
            else:
                assign(ref(this, 'MC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), [ref(this, 'mcID').get(), ref(this, 'unitName').get(), rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), [])]))
    if truth(binop('==', ref(this, 'mcID').get(), 'suicide_bomber')):
        rt.call_ref(ref(ref(this, 'MC').get(), 'swapDepths'), [rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), [])])
    assign(ref(this, 'activeAndMoving'), '=', lambda: False)
    assign(ref(this, 'curX'), '=', lambda: e.get('param_startX'))
    assign(ref(this, 'curY'), '=', lambda: e.get('param_startY'))
    if truth(logical('||', binop('==', e.get('param_targetType'), 'rocket'), lambda: binop('==', e.get('param_targetType'), 'sub_rocket'))):
        assign(ref(this, 'prevX'), '=', lambda: ref(this, 'curX').get())
        assign(ref(this, 'prevY'), '=', lambda: binop('+', ref(this, 'curY').get(), 5))
        assign(ref(this, 'tintMC'), '=', lambda: ref(ref(this, 'MC').get(), 'tintMC').get())
        assign(ref(this, 'colorObj'), '=', lambda: rt.construct(e.get('Color'), [ref(this, 'tintMC').get()]))
        rt.call_ref(ref(ref(this, 'colorObj').get(), 'setTransform'), [ref(this, 'colorTrans').get()])
        assign(ref(this, 'ellipseWidth'), '=', lambda: ref(ref(this, 'wildCard').get(), 'ellipseWidth').get())
        assign(ref(this, 'ellipseHeight'), '=', lambda: ref(ref(this, 'wildCard').get(), 'ellipseHeight').get())
        assign(ref(this, 'ellipseCenterX'), '=', lambda: ref(ref(this, 'wildCard').get(), 'ellipseCenterX').get())
        assign(ref(this, 'ellipseCenterY'), '=', lambda: ref(ref(this, 'wildCard').get(), 'ellipseCenterY').get())
        assign(ref(this, 'ellipseRadiusX'), '=', lambda: binop('/', ref(this, 'ellipseWidth').get(), 2))
        assign(ref(this, 'ellipseRadiusY'), '=', lambda: binop('/', ref(this, 'ellipseHeight').get(), 2))
        assign(ref(this, 'ellipseAngle'), '=', lambda: ref(ref(this, 'wildCard').get(), 'startAngle').get())
        assign(ref(this, 'ellipseDirectionMultiplier'), '=', lambda: ref(ref(this, 'wildCard').get(), 'directionMultiplier').get())
        assign(ref(this, 'ellipseSpeed'), '=', lambda: 3)
        assign(ref(this, 'ellipseTargetAngle'), '=', lambda: ref(ref(this, 'wildCard').get(), 'targetAngle').get())
        assign(ref(this, 'ellipseFinalAction'), '=', lambda: ref(ref(this, 'wildCard').get(), 'finalAction').get())
    assign(ref(this, 'tail'), '=', lambda: e.get('param_tail'))
    assign(ref(this, 'tailNum'), '=', lambda: e.get('param_tailNum'))
    if truth(ref(this, 'hasShadow').get()):
        assign(ref(this, 'shadowMC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), [ref(this, 'shadowMC_id').get(), binop('+', 'shadow_', ref(this, 'unitName').get()), rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), [])]))
        assign(ref(ref(this, 'shadowMC').get(), '_x'), '=', lambda: e.get('param_startX'))
        assign(ref(ref(this, 'shadowMC').get(), '_y'), '=', lambda: e.get('param_startY'))
        assign(ref(ref(this, 'shadowMC').get(), '_alpha'), '=', lambda: ref(this, 'shadowStartAlpha').get())
    if truth(ref(this, 'tintMC_id').get()):
        assign(ref(this, 'tintMC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), [ref(this, 'tintMC_id').get(), binop('+', 'tint', ref(this, 'unitName').get()), rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), [])]))
        assign(ref(this, 'colorObj'), '=', lambda: rt.construct(e.get('Color'), [ref(this, 'tintMC').get()]))
        rt.call_ref(ref(ref(this, 'colorObj').get(), 'setTransform'), [ref(this, 'colorTrans').get()])
    if truth(binop('==', ref(this, 'mcID').get(), 'apache')):
        e.set('_temp_12', ref(this, 'tintMC').get())
        e.set('_temp_11', '_xscale')
        e.set('_temp_10', ref(this, 'tintMC').get())
        e.set('_temp_9', '_yscale')
        e.set('_temp_8', ref(this, 'shadowMC').get())
        e.set('_temp_7', '_xscale')
        e.set('_temp_6', ref(this, 'shadowMC').get())
        e.set('_temp_5', '_yscale')
        e.set('_temp_4', ref(this, 'MC').get())
        e.set('_temp_3', '_xscale')
        assign(ref(ref(this, 'MC').get(), '_yscale'), '=', lambda: assign(e.ref('_loc0_'), '=', lambda: 50))
        assign(ref(e.get('_temp_4'), e.get('_temp_3')), '=', lambda: e.get('_loc0_'))
        assign(ref(e.get('_temp_6'), e.get('_temp_5')), '=', lambda: e.get('_loc0_'))
        assign(ref(e.get('_temp_8'), e.get('_temp_7')), '=', lambda: e.get('_loc0_'))
        assign(ref(e.get('_temp_10'), e.get('_temp_9')), '=', lambda: e.get('_loc0_'))
        assign(ref(e.get('_temp_12'), e.get('_temp_11')), '=', lambda: e.get('_loc0_'))
    if truth(binop('==', ref(this, 'mcID').get(), 'ship_plane')):
        e.set('_temp_14', ref(this, 'MC').get())
        e.set('_temp_13', '_xscale')
        assign(ref(ref(this, 'MC').get(), '_yscale'), '=', lambda: assign(e.ref('_loc0_'), '=', lambda: 10))
        assign(ref(e.get('_temp_14'), e.get('_temp_13')), '=', lambda: e.get('_loc0_'))
        e.set('_temp_16', ref(this, 'tintMC').get())
        e.set('_temp_15', '_xscale')
        assign(ref(ref(this, 'tintMC').get(), '_yscale'), '=', lambda: assign(e.ref('_loc0_'), '=', lambda: 10))
        assign(ref(e.get('_temp_16'), e.get('_temp_15')), '=', lambda: e.get('_loc0_'))
        e.set('_temp_18', ref(this, 'shadowMC').get())
        e.set('_temp_17', '_xscale')
        assign(ref(ref(this, 'shadowMC').get(), '_yscale'), '=', lambda: assign(e.ref('_loc0_'), '=', lambda: 10))
        assign(ref(e.get('_temp_18'), e.get('_temp_17')), '=', lambda: e.get('_loc0_'))
        assign(ref(ref(this, 'shadowMC').get(), '_visible'), '=', lambda: False)
    assign(ref(this, 'targetDot'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), ['redDot', binop('+', 'targetDot', ref(this, 'unitName').get()), rt.call_ref(ref(e.get('param_container'), 'getNextHighestDepth'), [])]))
    e.set('_loc22_', rt.construct(e.get('Color'), [ref(this, 'targetDot').get()]))
    rt.call_ref(ref(e.get('_loc22_'), 'setTransform'), [ref(this, 'colorTrans').get()])
    assign(ref(this, 'wayPointArr'), '=', lambda: e.get('param_wayPointArr'))
    if truth(ref(this, 'liftOff').get()):
        e.set('_temp_20', ref(this, 'MC').get())
        e.set('_temp_19', '_xscale')
        assign(ref(ref(this, 'MC').get(), '_yscale'), '=', lambda: assign(e.ref('_loc0_'), '=', lambda: 50))
        assign(ref(e.get('_temp_20'), e.get('_temp_19')), '=', lambda: e.get('_loc0_'))
        assign(ref(ref(this, 'MC').get(), '_alpha'), '=', lambda: 0)
        e.set('_temp_22', ref(this, 'shadowMC').get())
        e.set('_temp_21', '_xscale')
        assign(ref(ref(this, 'shadowMC').get(), '_yscale'), '=', lambda: assign(e.ref('_loc0_'), '=', lambda: 50))
        assign(ref(e.get('_temp_22'), e.get('_temp_21')), '=', lambda: e.get('_loc0_'))
        e.set('_temp_24', ref(this, 'tintMC').get())
        e.set('_temp_23', '_xscale')
        assign(ref(ref(this, 'tintMC').get(), '_yscale'), '=', lambda: assign(e.ref('_loc0_'), '=', lambda: ref(ref(this, 'MC').get(), '_xscale').get()))
        assign(ref(e.get('_temp_24'), e.get('_temp_23')), '=', lambda: e.get('_loc0_'))
    assign(ref(this, 'result'), '=', lambda: e.get('param_result'))
    assign(ref(ref(this, 'MC').get(), '_visible'), '=', lambda: ref(this, 'visible').get())
    assign(ref(ref(this, 'tintMC').get(), '_visible'), '=', lambda: ref(this, 'visible').get())
    if truth(binop('==', ref(this, 'mcID').get(), 'tank_noShade')):
        assign(ref(ref(ref(this, 'MC').get(), 'shadowMC').get(), '_visible'), '=', lambda: False)
        assign(ref(ref(ref(this, 'MC').get(), 'shadowMC').get(), '_y'), '+=', lambda: 40)
    if truth(ref(ref(this, 'wildCard').get(), 'satelliteFrame').get()):
        rt.call_ref(ref(ref(this, 'MC').get(), 'gotoAndStop'), [ref(ref(this, 'wildCard').get(), 'satelliteFrame').get()])
    assign(ref(this, 'laserStartMC'), '=', lambda: ref(ref(ref(this, 'MC').get(), 'mc').get(), 'laserStartMC').get())
    if truth(binop('==', ref(this, 'mcID').get(), 'chinook')):
        rt.call_ref(ref(this, 'soundAction'), ['chinook_start'])
    if truth(binop('==', ref(this, 'mcID').get(), 'suicide_bomber')):
        rt.call_ref(ref(ref(this, 'MC').get(), 'swapDepths'), [rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), [])])
    return U

def Unit___get__appMC_depth(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Unit')
    e.set('_loc2_', rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), []))
    if truth(binop('!=', ref(this, 'mcID').get(), 'tankTop')):
        assign(e.ref('_loc2_'), '=', lambda: binop('+', binop('+', binop('*', rt.call_ref(ref(e.get('Math'), 'floor'), [binop('/', ref(this, 'curY').get(), 10)]), 500), 120), ref(this, 'depth_').get()))
    else:
        assign(e.ref('_loc2_'), '=', lambda: binop('+', rt.call_ref(ref(ref(ref(this, 'tail').get(), 'MC').get(), 'getDepth'), []), 1))
    if truth(binop('==', ref(ref(this, 'tail').get(), 'mcID').get(), 'chinook')):
        assign(e.ref('_loc2_'), '=', lambda: binop('-', rt.call_ref(ref(ref(ref(this, 'tail').get(), 'MC').get(), 'getDepth'), []), 2))
    if truth(logical('&&', binop('==', ref(this, 'mcID').get(), 'soldier001'), lambda: binop('==', ref(this, 'playerNum').get(), 0))):
        pass
    return e.get('_loc2_')
    return U

def Unit___set__appMC_depth(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_param'], ['_param'], closure, 'Unit')
    return U

def Unit_moveUnit(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Unit')
    if truth(ref(this, 'unit_live_countdown_status').get()):
        if truth(binop('>=', update(ref(this, 'cur_unit_live'), -1, True), ref(this, 'max_unit_live').get())):
            assign(ref(this, 'action'), '=', lambda: 'stop')
    if truth(logical('&&', binop('==', ref(this, 'mcID').get(), 'tankTop'), lambda: binop('==', ref(ref(this, 'tail').get(), 'action').get(), 'tank_shoot'))):
        assign(ref(this, 'action'), '=', lambda: 'tank_top_shoot')
    switch_3 = ref(this, 'action').get()
    case_4 = -1
    if case_4 == -1 and strict_eq(switch_3, 'shoot'):
        case_4 = 0
    if case_4 == -1 and strict_eq(switch_3, 'tank_shoot'):
        case_4 = 1
    if case_4 == -1 and strict_eq(switch_3, 'tank_top_shoot'):
        case_4 = 2
    if case_4 == -1 and strict_eq(switch_3, 'tank_reset_range'):
        case_4 = 3
    if case_4 == -1 and strict_eq(switch_3, 'soldier_reset_range'):
        case_4 = 4
    if case_4 == -1 and strict_eq(switch_3, 'suicide_fade_out'):
        case_4 = 5
    if case_4 == -1 and strict_eq(switch_3, 'suicide_dissapear'):
        case_4 = 6
    if case_4 == -1 and strict_eq(switch_3, 'suicide_appear'):
        case_4 = 7
    if case_4 == -1 and strict_eq(switch_3, 'suicide_fade_in'):
        case_4 = 8
    if case_4 == -1 and strict_eq(switch_3, 'speedup_success'):
        case_4 = 9
    if case_4 == -1 and strict_eq(switch_3, 'speedup_die'):
        case_4 = 10
    if case_4 == -1 and strict_eq(switch_3, 'explode'):
        case_4 = 11
    if case_4 == -1 and strict_eq(switch_3, 'suicide_explode'):
        case_4 = 12
    if case_4 == -1 and strict_eq(switch_3, 'rocket_follow_ellipse_with_anti'):
        case_4 = 13
    if case_4 == -1 and strict_eq(switch_3, 'rocket_follow_ellipse'):
        case_4 = 14
    if case_4 == -1 and strict_eq(switch_3, 'rocket_explode_self'):
        case_4 = 15
    if case_4 == -1 and strict_eq(switch_3, 'rocket_explode_city'):
        case_4 = 16
    if case_4 == -1 and strict_eq(switch_3, 'rocket_explode_city_from_sub'):
        case_4 = 17
    if case_4 == -1 and strict_eq(switch_3, 'bomb'):
        case_4 = 18
    if case_4 == -1 and strict_eq(switch_3, 'ship_plane_bomb'):
        case_4 = 19
    if case_4 == -1 and strict_eq(switch_3, 'heli_unload'):
        case_4 = 20
    if case_4 == -1 and strict_eq(switch_3, 'unload'):
        case_4 = 21
    if case_4 == -1 and strict_eq(switch_3, 'flyOff'):
        case_4 = 22
    if case_4 == -1 and strict_eq(switch_3, 'liftOff'):
        case_4 = 23
    if case_4 == -1 and strict_eq(switch_3, 'taxi_a'):
        case_4 = 24
    if case_4 == -1 and strict_eq(switch_3, 'taxi_b'):
        case_4 = 25
    if case_4 == -1 and strict_eq(switch_3, 'plane_circular_flight'):
        case_4 = 26
    if case_4 == -1 and strict_eq(switch_3, 'sub_rocket_launch'):
        case_4 = 27
    if case_4 == -1:
        case_4 = -1
    try:
        if 0 <= case_4 <= 0:
            if truth(binop('==', ref(this, 'mcID').get(), 'soldier001')):
                rt.call_ref(ref(this, 'soundAction'), ['soldier_shoot'])
            else:
                rt.call_ref(ref(this, 'soundAction'), ['marine_shoot'])
            if truth(binop('==', ref(this, 'shotCount').get(), 0)):
                assign(ref(this, 'constantDir'), '=', lambda: ref(this, 'unitDirection').get())
                rt.call_ref(ref(this, 'setStep'), [])
                assign(ref(this, 'activeAndMoving'), '=', lambda: False)
                rt.call_ref(ref(ref(this, 'MC').get(), 'removeMovieClip'), [])
                rt.call_ref(ref(ref(this, 'tintMC').get(), 'removeMovieClip'), [])
                assign(ref(this, 'MC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), [ref(this, 'schootMCID').get(), ref(this, 'unitName').get(), rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), [])]))
                assign(ref(this, 'tintMC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), [ref(this, 'shootTintMC_id').get(), binop('+', 'tint', ref(this, 'unitName').get()), binop('+', rt.call_ref(ref(ref(this, 'MC').get(), 'getDepth'), []), 1)]))
                assign(ref(this, 'colorObj'), '=', lambda: rt.construct(e.get('Color'), [ref(this, 'tintMC').get()]))
                rt.call_ref(ref(ref(this, 'colorObj').get(), 'setTransform'), [ref(this, 'colorTrans').get()])
                assign(ref(this, 'offsetFrames'), '=', lambda: ref(this, 'maxShootOffset').get())
                rt.call_ref(ref(ref(this, 'MC').get(), 'gotoAndStop'), [5])
                rt.call_ref(ref(ref(this, 'tintMC').get(), 'gotoAndStop'), [5])
            if truth(binop('<', ref(this, 'shotCount').get(), ref(this, 'maxShotCount').get())):
                rt.call_ref(ref(ref(ref(rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(this, 'tr').get(), '_city').get()]), 'image').get(), 'bulletHoles').get(), 'play'), [])
                if truth(binop('==', ref(this, 'curShootOffset').get(), 0)):
                    assign(ref(this, 'curShootOffset'), '=', lambda: 1)
                else:
                    assign(ref(this, 'curShootOffset'), '=', lambda: 0)
                rt.call_ref(ref(ref(this, 'MC').get(), 'gotoAndStop'), [ref(this, 'constantDir').get()])
                rt.call_ref(ref(ref(this, 'tintMC').get(), 'gotoAndStop'), [ref(this, 'constantDir').get()])
                assign(ref(this, 'shotCount'), '=', lambda: binop('+', ref(this, 'shotCount').get(), 1))
            else:
                rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'updateSingleCity_byID'), [ref(ref(this, 'tr').get(), '_city').get(), binop('/', ref(ref(this, 'tr').get(), '_casualties').get(), 3)])
                assign(ref(this, 'action'), '=', lambda: 'stop')
            raise ASBreak()
        if 0 <= case_4 <= 1:
            raise ASBreak()
        if 0 <= case_4 <= 2:
            assign(ref(ref(this, 'tail').get(), 'activeAndMoving'), '=', lambda: False)
            rt.call_ref(ref(ref(ref(this, 'tail').get(), 'sound').get(), 'stop'), ['unit_Tank.wav'])
            if truth(binop('<', ref(ref(this, 'tail').get(), 'shotCount').get(), ref(ref(this, 'tail').get(), 'maxShotCount').get())):
                assign(e.ref('_loc2_'), '=', lambda: ref(ref(this, 'MC').get(), '_currentframe').get())
                if truth(logical('&&', binop('==', e.get('_loc2_'), binop('-', binop('*', ref(this, 'tankTopDirection').get(), 2), 1)), lambda: binop('>', ref(this, 'tank_preshot_count').get(), 25))):
                    rt.call_ref(ref(ref(this, 'MC').get(), 'nextFrame'), [])
                    assign(ref(this, 'tank_preshot_count'), '=', lambda: 0)
                    rt.call_ref(ref(this, 'soundAction'), ['tank_shoot'])
                else:
                    if truth(binop('>', ref(this, 'tank_preshot_count').get(), 3)):
                        rt.call_ref(ref(ref(this, 'MC').get(), 'gotoAndStop'), [binop('-', binop('*', ref(this, 'tankTopDirection').get(), 2), 1)])
                update(ref(ref(this, 'tail').get(), 'shotCount'), 1, False)
                assign(ref(this, 'tank_preshot_count'), '=', lambda: binop('+', ref(this, 'tank_preshot_count').get(), 1))
            else:
                rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'updateSingleCity_byID'), [ref(ref(ref(this, 'tail').get(), 'tr').get(), '_city').get(), ref(ref(ref(this, 'tail').get(), 'tr').get(), '_casualties').get()])
                assign(ref(ref(this, 'tail').get(), 'action'), '=', lambda: 'stop')
                assign(ref(this, 'action'), '=', lambda: 'stop')
            raise ASBreak()
        if 0 <= case_4 <= 3:
            assign(ref(this, 'range'), '=', lambda: 40)
            raise ASBreak()
        if 0 <= case_4 <= 4:
            if truth(binop('<', ref(this, 'curX').get(), ref(ref(ref(this, 'wayPointArr').get(), ref(this, 'curWayPoint').get()).get(), '_x').get())):
                assign(ref(this, 'range'), '=', lambda: 100)
            else:
                assign(ref(this, 'range'), '=', lambda: 25)
            raise ASBreak()
        if 0 <= case_4 <= 5:
            if truth(logical('&&', binop('>', ref(ref(this, 'MC').get(), '_alpha').get(), 0), lambda: ref(this, 'activeAndMoving').get())):
                assign(ref(ref(this, 'MC').get(), '_alpha'), '-=', lambda: 2)
                assign(ref(ref(this, 'tintMC').get(), '_alpha'), '=', lambda: ref(ref(this, 'MC').get(), '_alpha').get())
            raise ASBreak()
        if 0 <= case_4 <= 6:
            rt.call_ref(ref(this, 'soundAction'), ['suicide_scream'])
            assign(ref(this, 'activeAndMoving'), '=', lambda: False)
            rt.call_ref(ref(ref(this, 'MC').get(), 'gotoAndStop'), [17])
            rt.call_ref(ref(ref(this, 'tintMC').get(), 'gotoAndStop'), [17])
            if truth(binop('>=', ref(this, 'suicide_commando_wait_countDown_cur').get(), ref(this, 'suicide_commando_wait_countDown_max').get())):
                assign(ref(this, 'suicide_commando_wait_countDown_max'), '=', lambda: 0)
                assign(ref(this, 'activeAndMoving'), '=', lambda: True)
            else:
                assign(ref(this, 'suicide_commando_wait_countDown_cur'), '=', lambda: binop('+', ref(this, 'suicide_commando_wait_countDown_cur').get(), 1))
            assign(ref(this, 'curX'), '=', lambda: ref(ref(ref(this, 'wayPointArr').get(), ref(this, 'curWayPoint').get()).get(), '_x').get())
            assign(ref(this, 'curY'), '=', lambda: ref(ref(ref(this, 'wayPointArr').get(), ref(this, 'curWayPoint').get()).get(), '_y').get())
            raise ASBreak()
        if 0 <= case_4 <= 7:
            assign(ref(this, 'action'), '=', lambda: 'suicide_fade_in')
            raise ASBreak()
        if 0 <= case_4 <= 8:
            if truth(binop('<', ref(ref(this, 'MC').get(), '_alpha').get(), 100)):
                update(ref(ref(this, 'MC').get(), '_alpha'), 1, False)
                assign(ref(ref(this, 'tintMC').get(), '_alpha'), '=', lambda: ref(ref(this, 'MC').get(), '_alpha').get())
            raise ASBreak()
        if 0 <= case_4 <= 9:
            assign(ref(this, 'action'), '=', lambda: 'default')
            assign(ref(this, 'range'), '=', lambda: 70)
            assign(ref(this, 'step'), '=', lambda: 15)
            assign(ref(this, 'x_multiplier'), '=', lambda: 2)
            assign(ref(this, 'y_multiplier'), '=', lambda: 1)
            rt.call_ref(ref(ref(this, 'MC').get(), 'gotoAndStop'), [2])
            assign(ref(this, 'tintMC'), '=', lambda: ref(ref(this, 'MC').get(), 'tintMC').get())
            assign(ref(this, 'colorObj'), '=', lambda: rt.construct(e.get('Color'), [ref(this, 'tintMC').get()]))
            rt.call_ref(ref(ref(this, 'colorObj').get(), 'setTransform'), [ref(this, 'colorTrans').get()])
            raise ASBreak()
        if 0 <= case_4 <= 10:
            rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'fireDefense'), [ref(this, 'targetPlayer').get(), 'antiAir_fire'])
            rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'updateSingleCity_byID'), [ref(ref(this, 'tr').get(), '_city').get(), ref(ref(this, 'tr').get(), '_casualties').get()])
            assign(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(this, 'targetPlayer').get()).get(), 'anti_inBattle_target'), '=', lambda: e.get('undefined'))
            rt.call_ref(ref(e.get('_global'), 'explosion_sound_by_mc_name'), ['explosion003', ref(ref(this, 'MC').get(), '_x').get()])
            rt.call_ref(ref(this, 'killUnit'), ['rocket_self'])
            raise ASBreak()
        if 0 <= case_4 <= 11:
            rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'updateSingleCity_byID'), [ref(ref(this, 'tr').get(), '_city').get(), ref(ref(this, 'tr').get(), '_casualties').get()])
            rt.call_ref(ref(this, 'killUnit'), ['default'])
            raise ASBreak()
        if 0 <= case_4 <= 12:
            rt.call_ref(ref(e.get('_global'), 'explosion_sound_by_mc_name'), ['suicide', ref(ref(this, 'MC').get(), '_x').get()])
            rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'updateSingleCity_byID'), [ref(ref(this, 'tr').get(), '_city').get(), ref(ref(this, 'tr').get(), '_casualties').get()])
            rt.call_ref(ref(this, 'killUnit'), ['suicide'])
            raise ASBreak()
        if 0 <= case_4 <= 13:
            rt.call_ref(ref(ref(this, 'MC').get(), 'gotoAndStop'), [3])
            assign(ref(this, 'colorObj'), '=', lambda: rt.construct(e.get('Color'), [ref(this, 'tintMC').get()]))
            rt.call_ref(ref(ref(this, 'colorObj').get(), 'setTransform'), [ref(this, 'colorTrans').get()])
            rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'fireDefense'), [ref(this, 'targetPlayer').get(), 'antiRocket_fire'])
            assign(ref(this, 'rocket_follow_ellipse'), '=', lambda: True)
            assign(ref(this, 'action'), '=', lambda: 'none')
            raise ASBreak()
        if 0 <= case_4 <= 14:
            rt.call_ref(ref(ref(this, 'MC').get(), 'gotoAndStop'), [3])
            assign(ref(this, 'colorObj'), '=', lambda: rt.construct(e.get('Color'), [ref(this, 'tintMC').get()]))
            rt.call_ref(ref(ref(this, 'colorObj').get(), 'setTransform'), [ref(this, 'colorTrans').get()])
            assign(ref(this, 'rocket_follow_ellipse'), '=', lambda: True)
            assign(ref(this, 'action'), '=', lambda: 'none')
            raise ASBreak()
        if 0 <= case_4 <= 15:
            rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'updateSingleCity_byID'), [ref(ref(this, 'tr').get(), '_city').get(), ref(ref(this, 'tr').get(), '_casualties').get()])
            assign(ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playerArr').get(), ref(this, 'targetPlayer').get()).get(), 'anti_inBattle_target'), '=', lambda: e.get('undefined'))
            rt.call_ref(ref(this, 'killUnit'), ['rocket_self'])
            rt.call_ref(ref(e.get('_global'), 'explosion_sound_by_mc_name'), ['explosion002', ref(ref(this, 'MC').get(), '_x').get()])
            raise ASBreak()
        if 0 <= case_4 <= 16:
            rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'updateSingleCity_byID'), [ref(ref(this, 'tr').get(), '_city').get(), ref(ref(this, 'tr').get(), '_casualties').get()])
            rt.call_ref(ref(e.get('_global'), 'explosion_sound_by_mc_name'), [ref(this, 'explosion_mc_name').get(), ref(ref(this, 'MC').get(), '_x').get()])
            assign(ref(this, 'explosionMC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), [ref(this, 'explosion_mc_name').get(), binop('+', ref(this, 'unitName').get(), 'explosion'), rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), [])]))
            assign(ref(ref(this, 'explosionMC').get(), '_x'), '=', lambda: ref(ref(ref(this, 'wayPointArr').get(), binop('-', ref(ref(this, 'wayPointArr').get(), 'length').get(), 1)).get(), '_x').get())
            assign(ref(ref(this, 'explosionMC').get(), '_y'), '=', lambda: ref(ref(ref(this, 'wayPointArr').get(), binop('-', ref(ref(this, 'wayPointArr').get(), 'length').get(), 1)).get(), '_y').get())
            if truth(logical('&&', ref(ref(this, 'wildCard').get(), 'bioload').get(), lambda: ref(rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(this, 'tr').get(), '_city').get()]), 'bioload_in_battle').get())):
                rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'createBioCloud'), [rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(this, 'tr').get(), '_city').get()])])
            rt.call_ref(ref(this, 'killUnit'), [e.get('undefined')])
            raise ASBreak()
        if 0 <= case_4 <= 17:
            rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'updateSingleCity_byID'), [ref(ref(this, 'tr').get(), '_city').get(), ref(ref(this, 'tr').get(), '_casualties').get()])
            rt.call_ref(ref(e.get('_global'), 'explosion_sound_by_mc_name'), [ref(this, 'explosion_mc_name').get(), ref(ref(this, 'MC').get(), '_x').get()])
            assign(ref(this, 'explosionMC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), [ref(this, 'explosion_mc_name').get(), binop('+', ref(this, 'unitName').get(), 'explosion'), rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), [])]))
            assign(ref(ref(this, 'explosionMC').get(), '_x'), '=', lambda: ref(ref(ref(this, 'wayPointArr').get(), binop('-', ref(ref(this, 'wayPointArr').get(), 'length').get(), 1)).get(), '_x').get())
            assign(ref(ref(this, 'explosionMC').get(), '_y'), '=', lambda: ref(ref(ref(this, 'wayPointArr').get(), binop('-', ref(ref(this, 'wayPointArr').get(), 'length').get(), 1)).get(), '_y').get())
            if truth(logical('&&', ref(ref(this, 'wildCard').get(), 'bioload').get(), lambda: ref(rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(this, 'tr').get(), '_city').get()]), 'bioload_in_battle').get())):
                rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'createBioCloud'), [rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(this, 'tr').get(), '_city').get()])])
            rt.call_ref(ref(this, 'killUnit'), [e.get('undefined')])
            raise ASBreak()
        if 0 <= case_4 <= 18:
            rt.call_ref(ref(e.get('_global'), 'explosion_sound_by_mc_name'), [ref(this, 'explosion_mc_name').get(), ref(ref(this, 'MC').get(), '_x').get()])
            rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'updateSingleCity_byID'), [ref(ref(this, 'tr').get(), '_city').get(), ref(ref(this, 'tr').get(), '_casualties').get()])
            assign(ref(this, 'action'), '=', lambda: 'flyOff')
            assign(ref(this, 'explosionMC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), [ref(this, 'explosion_mc_name').get(), binop('+', ref(this, 'unitName').get(), 'explosion'), rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), [])]))
            assign(ref(ref(this, 'explosionMC').get(), '_x'), '=', lambda: ref(ref(ref(this, 'wayPointArr').get(), binop('-', ref(ref(this, 'wayPointArr').get(), 'length').get(), 1)).get(), '_x').get())
            assign(ref(ref(this, 'explosionMC').get(), '_y'), '=', lambda: binop('+', ref(ref(ref(this, 'wayPointArr').get(), binop('-', ref(ref(this, 'wayPointArr').get(), 'length').get(), 1)).get(), '_y').get(), 100))
            if truth(logical('&&', ref(ref(this, 'wildCard').get(), 'bioload').get(), lambda: ref(rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(this, 'wildCard').get(), 'city').get()]), 'bioload_in_battle').get())):
                rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'createBioCloud'), [rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(this, 'wildCard').get(), 'city').get()])])
            rt.call_ref(ref(this, 'removeTrail'), [])
            raise ASBreak()
        if 0 <= case_4 <= 19:
            rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'updateSingleCity_byID'), [ref(ref(this, 'wildCard').get(), '_city').get(), ref(ref(this, 'wildCard').get(), '_casualties').get()])
            assign(ref(this, 'action'), '=', lambda: 'flyOff')
            if truth(unary('!', ref(this, 'explosion_mc_name').get())):
                assign(ref(this, 'explosion_mc_name'), '=', lambda: 'explosion_warhead_1')
            rt.call_ref(ref(e.get('_global'), 'explosion_sound_by_mc_name'), [ref(this, 'explosion_mc_name').get(), ref(ref(this, 'MC').get(), '_x').get()])
            assign(ref(this, 'explosionMC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), [ref(this, 'explosion_mc_name').get(), binop('+', ref(this, 'unitName').get(), 'explosion'), rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), [])]))
            assign(ref(ref(this, 'explosionMC').get(), '_x'), '=', lambda: ref(ref(ref(this, 'wayPointArr').get(), binop('-', ref(ref(this, 'wayPointArr').get(), 'length').get(), 1)).get(), '_x').get())
            assign(ref(ref(this, 'explosionMC').get(), '_y'), '=', lambda: binop('+', ref(ref(ref(this, 'wayPointArr').get(), binop('-', ref(ref(this, 'wayPointArr').get(), 'length').get(), 1)).get(), '_y').get(), 104))
            if truth(logical('&&', ref(ref(this, 'wildCard').get(), 'bioload').get(), lambda: ref(rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(this, 'wildCard').get(), 'city').get()]), 'bioload_in_battle').get())):
                rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'createBioCloud'), [rt.call_ref(ref(ref(e.get('_global'), 'model').get(), 'getCityByID'), [ref(ref(this, 'wildCard').get(), 'city').get()])])
            rt.call_ref(ref(this, 'removeTrail'), [])
            raise ASBreak()
        if 0 <= case_4 <= 20:
            assign(ref(this, 'activeAndMoving'), '=', lambda: True)
            rt.call_ref(ref(this, 'soundAction'), ['apache_flyOff'])
            if truth(unary('!', ref(this, 'heli_unload_initial_y').get())):
                assign(ref(this, 'heli_unload_initial_y'), '=', lambda: ref(ref(this, 'MC').get(), '_y').get())
            if truth(binop('<', ref(this, 'curY').get(), binop('+', ref(this, 'heli_unload_initial_y').get(), 20))):
                assign(ref(this, 'curY'), '+=', lambda: 2)
                assign(ref(this, 'shadowYOffset'), '-=', lambda: 2)
            if truth(binop('>=', ref(this, 'unloadTimer').get(), 10)):
                rt.call_ref(ref(this, 'resetTailUnload'), ['flyOff'])
            else:
                assign(ref(this, 'unloadTimer'), '=', lambda: binop('+', ref(this, 'unloadTimer').get(), 1))
            raise ASBreak()
        if 0 <= case_4 <= 21:
            rt.call_ref(ref(this, 'soundAction'), ['boat_stop'])
            assign(ref(ref(this, 'tintMC').get(), '_x'), '=', lambda: ref(ref(this, 'MC').get(), '_x').get())
            assign(ref(ref(this, 'tintMC').get(), '_y'), '=', lambda: ref(ref(this, 'MC').get(), '_y').get())
            assign(ref(this, 'activeAndMoving'), '=', lambda: False)
            if truth(logical('&&', binop('==', ref(this, 'unloadTimer').get(), 0), lambda: logical('&&', binop('==', ref(this, 'unloadNum').get(), 0), lambda: unary('!', ref(this, 'bool1').get())))):
                assign(ref(this, 'bool1'), '=', lambda: True)
                rt.call_ref(ref(ref(this, 'MC').get(), 'removeMovieClip'), [])
                rt.call_ref(ref(ref(this, 'tintMC').get(), 'removeMovieClip'), [])
                assign(ref(this, 'MC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), ['boat001_still', ref(this, 'unitName').get(), ref(this, 'depth_').get()]))
                assign(ref(this, 'tintMC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), ['boat001_still_tint', binop('+', 'tint', ref(this, 'unitName').get()), binop('+', rt.call_ref(ref(ref(this, 'MC').get(), 'getDepth'), []), 1)]))
                assign(ref(ref(this, 'tintMC').get(), '_x'), '=', lambda: ref(this, 'prevX').get())
                assign(ref(ref(this, 'tintMC').get(), '_y'), '=', lambda: ref(this, 'prevY').get())
                assign(ref(this, 'colorObj'), '=', lambda: rt.construct(e.get('Color'), [ref(this, 'tintMC').get()]))
                rt.call_ref(ref(ref(this, 'colorObj').get(), 'setTransform'), [ref(this, 'colorTrans').get()])
            if truth(logical('&&', binop('>=', ref(this, 'unloadTimer').get(), 10), lambda: binop('<', ref(this, 'unloadNum').get(), 5))):
                rt.call_ref(ref(this, 'resetTailUnload'), ['stop'])
                rt.call_ref(ref(ref(this, 'MC').get(), 'gotoAndStop'), [binop('+', ref(this, 'unloadNum').get(), 2)])
                rt.call_ref(ref(ref(this, 'tintMC').get(), 'gotoAndStop'), [binop('+', ref(this, 'unloadNum').get(), 2)])
            else:
                assign(ref(this, 'unloadTimer'), '=', lambda: binop('+', ref(this, 'unloadTimer').get(), 1))
            raise ASBreak()
        if 0 <= case_4 <= 22:
            if truth(binop('==', ref(this, 'unitID').get(), 'boat001')):
                assign(ref(this, 'action'), '=', lambda: 'stop')
                raise ASBreak()
            if truth(binop('<=', ref(this, 'curCountToStop').get(), 0)):
                assign(ref(this, 'activeAndMoving'), '=', lambda: True)
            else:
                if truth(binop('<', ref(this, 'curCountToStop').get(), ref(this, 'countDownToStop').get())):
                    assign(ref(this, 'curCountToStop'), '=', lambda: binop('+', ref(this, 'curCountToStop').get(), 1))
                else:
                    if truth(binop('>=', ref(this, 'curCountToStop').get(), ref(this, 'countDownToStop').get())):
                        rt.call_ref(ref(ref(this, 'sound').get(), 'stop'), [])
                        ref(this, 'sound').delete()
                        assign(ref(this, 'action'), '=', lambda: 'stop')
            assign(ref(this, 'curCountToStop'), '=', lambda: binop('+', ref(this, 'curCountToStop').get(), 1))
            if truth(binop('>', rt.call_ref(ref(ref(this, 'sound').get(), 'getVolume'), []), 0)):
                rt.call_ref(ref(ref(this, 'sound').get(), 'setVolume'), [binop('-', rt.call_ref(ref(ref(this, 'sound').get(), 'getVolume'), []), 2)])
            raise ASBreak()
        if 0 <= case_4 <= 23:
            raise ASBreak()
        if 0 <= case_4 <= 24:
            if truth(binop('>', ref(this, 'TAXI_COUNT_MAX').get(), ref(this, 'cur_taxi_count').get())):
                assign(ref(this, 'cur_taxi_count'), '=', lambda: binop('+', ref(this, 'cur_taxi_count').get(), 1))
                assign(ref(this, 'curX'), '+=', lambda: 0.2)
                assign(ref(this, 'curY'), '-=', lambda: 0.5)
            else:
                assign(ref(this, 'action'), '=', lambda: 'liftOff')
            raise ASBreak()
        if 0 <= case_4 <= 25:
            if truth(binop('>', ref(this, 'TAXI_COUNT_MAX').get(), ref(this, 'cur_taxi_count').get())):
                assign(ref(this, 'cur_taxi_count'), '=', lambda: binop('+', ref(this, 'cur_taxi_count').get(), 1))
                assign(ref(this, 'curX'), '-=', lambda: 0.2)
                assign(ref(this, 'curY'), '-=', lambda: 0.5)
            else:
                assign(ref(this, 'action'), '=', lambda: 'liftOff')
            raise ASBreak()
        if 0 <= case_4 <= 26:
            if truth(binop('>', ref(this, 'plane_airTime').get(), 70)):
                assign(ref(this, 'action'), '=', lambda: 'default')
            assign(ref(this, 'plane_airTime'), '=', lambda: binop('+', ref(this, 'plane_airTime').get(), 1))
            raise ASBreak()
        if 0 <= case_4 <= 27:
            if truth(binop('>', ref(this, 'sub_launch_timer').get(), 34)):
                assign(ref(this, 'action'), '=', lambda: 'default')
                rt.call_ref(ref(this, 'soundAction'), ['rocket_launch'])
            else:
                assign(ref(this, 'sub_launch_timer'), '=', lambda: binop('+', ref(this, 'sub_launch_timer').get(), 1))
    except ASBreak:
        pass
    if truth(logical('&&', logical('||', binop('==', ref(this, 'mcID').get(), 'plane001'), lambda: logical('||', binop('==', ref(this, 'mcID').get(), 'plane002'), lambda: binop('==', ref(this, 'mcID').get(), 'ship_plane'))), lambda: logical('&&', ref(this, 'activeAndMoving').get(), lambda: logical('&&', binop('!=', ref(this, 'action').get(), 'taxi_a'), lambda: logical('&&', binop('!=', ref(this, 'action').get(), 'taxi_b'), lambda: binop('!=', ref(this, 'action').get(), 'waitForLiftOff')))))):
        if truth(binop('>', ref(this, 'PLANE_COUNT_TO_FREE_FLIGHT').get(), ref(this, 'cur_count_to_free_flight').get())):
            assign(ref(this, 'cur_count_to_free_flight'), '=', lambda: binop('+', ref(this, 'cur_count_to_free_flight').get(), 1))
            rt.call_ref(ref(this, 'soundAction'), [binop('+', ref(this, 'mcID').get(), '_takeOff')])
        else:
            if truth(binop('<', ref(this, 'shadowYOffset').get(), 90)):
                assign(ref(this, 'shadowYOffset'), '+=', lambda: 2)
    if truth(ref(this, 'activeAndMoving').get()):
        assign(ref(this, 'framesActive'), '=', lambda: binop('+', ref(this, 'framesActive').get(), 1))
        if truth(binop('==', ref(this, 'framesActive').get(), ref(this, 'trailCountDown').get())):
            assign(ref(this, 'trailActive'), '=', lambda: True)
        if truth(logical('&&', unary('!', ref(this, 'rocket_follow_ellipse').get()), lambda: logical('&&', unary('!', ref(this, 'rocket_do_drop').get()), lambda: logical('&&', binop('!=', ref(this, 'action').get(), 'heli_unload'), lambda: logical('&&', binop('!=', ref(this, 'action').get(), 'taxi_a'), lambda: logical('&&', binop('!=', ref(this, 'action').get(), 'taxi_b'), lambda: binop('!=', ref(this, 'action').get(), 'plane_circular_flight'))))))):
            rt.call_ref(ref(this, 'setStep'), [])
            assign(ref(this, 'prevX'), '=', lambda: ref(this, 'curX').get())
            assign(ref(this, 'prevY'), '=', lambda: ref(this, 'curY').get())
            assign(ref(this, 'curX'), '+=', lambda: ref(this, 'xStep').get())
            assign(ref(this, 'curY'), '+=', lambda: ref(this, 'yStep').get())
        else:
            if truth(ref(this, 'rocket_follow_ellipse').get()):
                rt.call_ref(ref(this, 'ellipse_step'), [])
            else:
                if truth(ref(this, 'rocket_do_drop').get()):
                    rt.call_ref(ref(this, 'rocket_drop'), [])
        if truth(logical('&&', binop('!=', ref(this, 'action').get(), 'taxi_a'), lambda: binop('!=', ref(this, 'action').get(), 'taxi_b'))):
            rt.call_ref(ref(this, 'updateTrail'), [])
        if truth(ref(this, 'atTarget').get()):
            assign(ref(this, 'action'), '=', lambda: ref(ref(ref(this, 'wayPointArr').get(), ref(this, 'curWayPoint').get()).get(), '_type').get())
            assign(ref(this, 'curWayPoint'), '=', lambda: binop('+', ref(this, 'curWayPoint').get(), 1))
            assign(ref(this, 'atTarget'), '=', lambda: False)
        if truth(binop('==', ref(this, 'action').get(), 'plane_circular_flight')):
            assign(ref(this, 'plane_countdown_default'), '=', lambda: binop('-', ref(this, 'plane_countdown_default').get(), 1))
            if truth(unary('!', ref(this, 'plane_angle_center').get())):
                assign(ref(this, 'plane_angle_center'), '=', lambda: arr([binop('+', ref(this, 'curX').get(), ref(ref(this, 'plane_circular_modifier').get(), 0).get()), binop('+', ref(this, 'curY').get(), ref(ref(this, 'plane_circular_modifier').get(), 1).get())]))
            rt.call_ref(ref(this, 'setStep'), [])
            rt.call_ref(ref(this, 'plane_circular_step'), [])
            if truth(logical('&&', binop('<', rt.call_ref(ref(this, 'distanceBetween'), [arr([ref(this, 'targetX').get(), ref(this, 'targetY').get()]), ref(this, 'plane_coords_at_cur_direction').get()]), 40), lambda: binop('<', ref(this, 'plane_countdown_default').get(), 0))):
                assign(ref(this, 'action'), '=', lambda: 'default')
    else:
        if truth(unary('!', ref(this, 'activeAndMoving').get())):
            if truth(binop('==', ref(this, 'mcID').get(), 'soldier001')):
                if truth(logical('&&', binop('==', ref(ref(this, 'tail').get(), 'action').get(), 'unload'), lambda: binop('==', ref(ref(this, 'tail').get(), 'unloadNum').get(), ref(this, 'tailNum').get()))):
                    assign(ref(this, 'action'), '=', lambda: 'default')
                    assign(ref(this, 'prevX'), '=', lambda: ref(ref(this, 'tail').get(), 'curX').get())
                    assign(ref(this, 'prevY'), '=', lambda: ref(ref(this, 'tail').get(), 'curY').get())
                    assign(ref(this, 'curX'), '=', lambda: binop('+', ref(ref(ref(this, 'wayPointArr').get(), 0).get(), '_x').get(), rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [0, 5])))
                    assign(ref(this, 'curY'), '=', lambda: binop('+', ref(ref(ref(this, 'wayPointArr').get(), 0).get(), '_y').get(), rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [0, 5])))
                    assign(ref(this, 'frameOffset'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [0, 6]))
                    assign(ref(ref(this, 'MC').get(), '_visible'), '=', lambda: True)
                    assign(ref(ref(this, 'tintMC').get(), '_visible'), '=', lambda: True)
                    assign(ref(this, 'activeAndMoving'), '=', lambda: True)
                    assign(ref(this, 'tail'), '=', lambda: False)
                    assign(ref(this, 'range'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [5, 8]))
                    assign(ref(this, 'traceMe'), '=', lambda: True)
                    rt.call_ref(ref(this, 'soundAction'), ['soldier_running'])
            else:
                if truth(binop('==', ref(this, 'mcID').get(), 'marine')):
                    if truth(logical('&&', binop('==', ref(ref(this, 'tail').get(), 'action').get(), 'heli_unload'), lambda: binop('==', ref(ref(this, 'tail').get(), 'unloadNum').get(), ref(this, 'tailNum').get()))):
                        assign(ref(this, 'prevX'), '=', lambda: ref(ref(this, 'tail').get(), 'curX').get())
                        assign(ref(this, 'prevY'), '=', lambda: ref(ref(this, 'tail').get(), 'curY').get())
                        assign(ref(this, 'curX'), '=', lambda: binop('+', ref(ref(ref(this, 'wayPointArr').get(), 0).get(), '_x').get(), rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [0, 20])))
                        assign(ref(this, 'frameOffset'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [0, 6]))
                        assign(ref(this, 'curY'), '=', lambda: binop('+', ref(ref(ref(this, 'wayPointArr').get(), 0).get(), '_y').get(), rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [0, 15])))
                        assign(ref(ref(this, 'MC').get(), '_visible'), '=', lambda: True)
                        assign(ref(ref(this, 'tintMC').get(), '_visible'), '=', lambda: True)
                        assign(ref(this, 'activeAndMoving'), '=', lambda: True)
                        assign(ref(this, 'tail'), '=', lambda: False)
                        assign(ref(this, 'range'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [5, 10]))
                        rt.call_ref(ref(this, 'soundAction'), ['marine_running'])
                else:
                    if truth(binop('==', ref(this, 'mcID').get(), 'tank_noShade')):
                        if truth(logical('&&', binop('==', ref(this, 'action').get(), 'tail'), lambda: binop('!=', ref(ref(this, 'tail').get(), 'action').get(), 'drop'))):
                            assign(ref(this, 'prevX'), '=', lambda: ref(this, 'curX').get())
                            assign(ref(this, 'prevY'), '=', lambda: ref(this, 'curY').get())
                            assign(ref(this, 'curX'), '=', lambda: binop('+', ref(ref(this, 'tail').get(), 'curX').get(), 2))
                            assign(ref(this, 'curY'), '=', lambda: binop('+', ref(ref(this, 'tail').get(), 'curY').get(), 30))
                            rt.call_ref(ref(ref(this, 'MC').get(), 'gotoAndStop'), [ref(this, 'unitDirection').get()])
                        else:
                            if truth(binop('==', ref(ref(this, 'tail').get(), 'action').get(), 'drop')):
                                assign(ref(this, 'unit_live_countdown_status'), '=', lambda: True)
                                rt.call_ref(ref(ref(this, 'tail').get(), 'soundAction'), ['chinook_flyOff'])
                                if truth(binop('>', ref(this, 'dropDistance').get(), ref(this, 'dropCount').get())):
                                    assign(ref(this, 'dropCount'), '=', lambda: binop('+', ref(this, 'dropCount').get(), 1))
                                    assign(ref(this, 'curY'), '+=', lambda: 2)
                                    assign(ref(ref(ref(this, 'MC').get(), 'shadowMC').get(), '_y'), '-=', lambda: 2)
                                    assign(ref(ref(ref(this, 'MC').get(), 'shadowMC').get(), '_visible'), '=', lambda: True)
                                else:
                                    rt.call_ref(ref(ref(this, 'MC').get(), 'removeMovieClip'), [])
                                    assign(ref(this, 'MC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), ['tankBase', ref(this, 'unitName').get(), ref(this, 'depth_').get()]))
                                    rt.call_ref(ref(this, 'soundAction'), ['tank_drive'])
                                    assign(ref(this, 'activeAndMoving'), '=', lambda: True)
                                    assign(ref(ref(this, 'tail').get(), 'action'), '=', lambda: 'flyOff')
                                    assign(ref(this, 'tail'), '=', lambda: e.get('undefined'))
                    else:
                        if truth(binop('==', ref(this, 'mcID').get(), 'tankTop')):
                            assign(ref(this, 'curX'), '=', lambda: ref(ref(this, 'tail').get(), 'curX').get())
                            assign(ref(this, 'curY'), '=', lambda: ref(ref(this, 'tail').get(), 'curY').get())
                            if truth(binop('!=', ref(this, 'action').get(), 'tank_top_shoot')):
                                rt.call_ref(ref(ref(this, 'MC').get(), 'gotoAndStop'), [binop('-', binop('*', ref(this, 'tankTopDirection').get(), 2), 1)])
                                if truth(binop('==', ref(ref(this, 'tail').get(), 'action').get(), 'stop')):
                                    assign(ref(this, 'action'), '=', lambda: 'stop')
    return U

def Unit_setStep(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Unit')
    if truth(rt.call_ref(ref(e.get('_global'), 'isNaN'), [ref(this, 'curX').get()])):
        assign(ref(this, 'curX'), '=', lambda: ref(ref(this, 'MC').get(), '_x').get())
    if truth(rt.call_ref(ref(e.get('_global'), 'isNaN'), [ref(this, 'curY').get()])):
        assign(ref(this, 'curY'), '=', lambda: ref(ref(this, 'MC').get(), '_y').get())
    if truth(unary('!', ref(this, 'tail').get())):
        assign(ref(this, 'targetX'), '=', lambda: ref(ref(ref(this, 'wayPointArr').get(), ref(this, 'curWayPoint').get()).get(), '_x').get())
        assign(ref(this, 'targetY'), '=', lambda: ref(ref(ref(this, 'wayPointArr').get(), ref(this, 'curWayPoint').get()).get(), '_y').get())
    else:
        assign(ref(this, 'targetX'), '=', lambda: ref(ref(this, 'tail').get(), 'curX').get())
        assign(ref(this, 'targetY'), '=', lambda: ref(ref(this, 'tail').get(), 'curY').get())
    if truth(binop('>', ref(this, 'targetX').get(), ref(this, 'curX').get())):
        assign(ref(this, 'xDist'), '=', lambda: binop('-', ref(this, 'targetX').get(), ref(this, 'curX').get()))
        assign(ref(this, 'xTargetStep'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'floor'), [binop('*', binop('/', ref(this, 'step').get(), 100), binop('*', binop('/', 100, binop('+', ref(this, 'xDist').get(), ref(this, 'yDist').get())), ref(this, 'xDist').get()))]))
        if truth(logical('&&', binop('>', ref(this, 'xTargetStep').get(), ref(this, 'xStep').get()), lambda: unary('!', ref(this, 'instantTurn').get()))):
            assign(ref(this, 'xStep'), '+=', lambda: ref(this, 'x_multiplier').get())
    else:
        assign(ref(this, 'xDist'), '=', lambda: binop('-', ref(this, 'curX').get(), ref(this, 'targetX').get()))
        assign(ref(this, 'xTargetStep'), '=', lambda: binop('*', rt.call_ref(ref(e.get('Math'), 'floor'), [binop('*', binop('/', ref(this, 'step').get(), 100), binop('*', binop('/', 100, binop('+', ref(this, 'xDist').get(), ref(this, 'yDist').get())), ref(this, 'xDist').get()))]), unary('-', 1)))
        if truth(logical('&&', binop('<', ref(this, 'xTargetStep').get(), ref(this, 'xStep').get()), lambda: unary('!', ref(this, 'instantTurn').get()))):
            assign(ref(this, 'xStep'), '-=', lambda: ref(this, 'x_multiplier').get())
    if truth(binop('>', ref(this, 'targetY').get(), ref(this, 'curY').get())):
        assign(ref(this, 'yDist'), '=', lambda: binop('-', ref(this, 'targetY').get(), ref(this, 'curY').get()))
        assign(ref(this, 'yTargetStep'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'floor'), [binop('*', binop('/', ref(this, 'step').get(), 100), binop('*', binop('/', 100, binop('+', ref(this, 'xDist').get(), ref(this, 'yDist').get())), ref(this, 'yDist').get()))]))
        if truth(logical('&&', binop('>', ref(this, 'yTargetStep').get(), ref(this, 'yStep').get()), lambda: unary('!', ref(this, 'instantTurn').get()))):
            assign(ref(this, 'yStep'), '+=', lambda: ref(this, 'y_multiplier').get())
    else:
        assign(ref(this, 'yDist'), '=', lambda: binop('-', ref(this, 'curY').get(), ref(this, 'targetY').get()))
        assign(ref(this, 'yTargetStep'), '=', lambda: binop('*', rt.call_ref(ref(e.get('Math'), 'floor'), [binop('*', binop('/', ref(this, 'step').get(), 100), binop('*', binop('/', 100, binop('+', ref(this, 'xDist').get(), ref(this, 'yDist').get())), ref(this, 'yDist').get()))]), unary('-', 1)))
        if truth(logical('&&', binop('<', ref(this, 'yTargetStep').get(), ref(this, 'yStep').get()), lambda: unary('!', ref(this, 'instantTurn').get()))):
            assign(ref(this, 'yStep'), '-=', lambda: ref(this, 'y_multiplier').get())
    if truth(ref(this, 'instantTurn').get()):
        assign(ref(this, 'xStep'), '=', lambda: ref(this, 'xTargetStep').get())
        assign(ref(this, 'yStep'), '=', lambda: ref(this, 'yTargetStep').get())
    if truth(logical('&&', binop('<', ref(this, 'curX').get(), binop('+', ref(this, 'targetX').get(), ref(this, 'range').get())), lambda: logical('&&', binop('>', ref(this, 'curX').get(), binop('-', ref(this, 'targetX').get(), ref(this, 'range').get())), lambda: logical('&&', binop('<', ref(this, 'curY').get(), binop('+', ref(this, 'targetY').get(), ref(this, 'range').get())), lambda: binop('>', ref(this, 'curY').get(), binop('-', ref(this, 'targetY').get(), ref(this, 'range').get())))))):
        assign(ref(this, 'atTarget'), '=', lambda: True)
    if truth(logical('||', binop('==', ref(this, 'mcID').get(), 'rocket'), lambda: binop('==', ref(this, 'mcID').get(), 'sub_rocket'))):
        if truth(logical('&&', binop('==', ref(this, 'action').get(), 'default'), lambda: ref(ref(this, 'MC').get(), 'maskMC').get())):
            assign(ref(ref(ref(this, 'MC').get(), 'maskMC').get(), '_x'), '-=', lambda: ref(this, 'yStep').get())
    if truth(binop('==', ref(this, 'mcID').get(), 'apache')):
        if truth(binop('<', ref(ref(this, 'MC').get(), '_xscale').get(), 100)):
            assign(ref(ref(this, 'MC').get(), '_xscale'), '+=', lambda: 1)
            assign(ref(ref(this, 'tintMC').get(), '_xscale'), '=', lambda: assign(ref(ref(this, 'tintMC').get(), '_yscale'), '=', lambda: assign(ref(ref(this, 'MC').get(), '_yscale'), '=', lambda: ref(ref(this, 'MC').get(), '_xscale').get())))
        if truth(logical('&&', binop('==', ref(this, 'action').get(), 'liftOff'), lambda: binop('==', ref(this, 'heli_direction_set').get(), 2))):
            assign(ref(this, 'prevY'), '=', lambda: ref(this, 'fixedPrevY').get())
            assign(ref(this, 'prevX'), '=', lambda: ref(this, 'fixedPrevX').get())
            rt.call_ref(ref(ref(this, 'MC').get(), 'gotoAndStop'), [ref(this, 'fixedFrame').get()])
            if truth(binop('<', ref(this, 'apache_liftOffCount').get(), binop('-', ref(this, 'apache_liftOffCountMax').get(), 8))):
                assign(ref(this, 'xStep'), '=', lambda: 0)
                assign(ref(this, 'yStep'), '=', lambda: unary('-', 3))
            else:
                assign(ref(this, 'xStep'), '=', lambda: 0)
                assign(ref(this, 'yStep'), '=', lambda: unary('-', 1))
            assign(ref(this, 'shadowYOffset'), '-=', lambda: ref(this, 'yStep').get())
            assign(ref(this, 'apache_liftOffCount'), '=', lambda: binop('+', ref(this, 'apache_liftOffCount').get(), 1))
            if truth(binop('>=', ref(this, 'apache_liftOffCount').get(), ref(this, 'apache_liftOffCountMax').get())):
                assign(ref(this, 'action'), '=', lambda: 'default')
        if truth(binop('<', ref(this, 'heli_direction_set').get(), 2)):
            assign(ref(this, 'heli_direction_set'), '=', lambda: binop('+', ref(this, 'heli_direction_set').get(), 1))
            assign(ref(this, 'fixedFrame'), '=', lambda: ref(this, 'unitDirection').get())
            assign(ref(this, 'fixedPrevX'), '=', lambda: ref(this, 'curX').get())
            assign(ref(this, 'fixedPrevY'), '=', lambda: ref(this, 'curY').get())
    if truth(binop('==', ref(this, 'mcID').get(), 'chinook')):
        if truth(binop('==', ref(this, 'action').get(), 'liftOff')):
            assign(ref(this, 'action'), '=', lambda: 'default')
    rt.call_ref(ref(this, 'updatePan'), [])
    return U

def Unit_deg2rad(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['degree'], ['degree'], closure, 'Unit')
    return binop('*', e.get('degree'), binop('/', ref(e.get('Math'), 'PI').get(), 180))
    return U

def Unit_rocket_drop(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Unit')
    assign(ref(this, 'prevX'), '=', lambda: ref(this, 'curX').get())
    assign(ref(this, 'prevY'), '=', lambda: ref(this, 'curY').get())
    assign(ref(this, 'curY'), '+=', lambda: 10)
    assign(ref(this, 'targetY'), '=', lambda: ref(ref(ref(this, 'wayPointArr').get(), ref(this, 'curWayPoint').get()).get(), '_y').get())
    if truth(binop('>=', ref(this, 'curY').get(), binop('-', ref(this, 'targetY').get(), 20))):
        assign(ref(this, 'atTarget'), '=', lambda: True)
    return U

def Unit_ellipse_step(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Unit')
    e.set('_loc2_', rt.call_ref(ref(this, 'deg2rad'), [ref(this, 'ellipseAngle').get()]))
    assign(ref(this, 'prevX'), '=', lambda: ref(this, 'curX').get())
    assign(ref(this, 'prevY'), '=', lambda: ref(this, 'curY').get())
    assign(ref(this, 'curX'), '=', lambda: binop('+', ref(this, 'ellipseCenterX').get(), binop('*', ref(this, 'ellipseRadiusX').get(), rt.call_ref(ref(e.get('Math'), 'cos'), [e.get('_loc2_')]))))
    assign(ref(this, 'curY'), '=', lambda: binop('+', ref(this, 'ellipseCenterY').get(), binop('*', ref(this, 'ellipseRadiusY').get(), rt.call_ref(ref(e.get('Math'), 'sin'), [e.get('_loc2_')]))))
    assign(ref(this, 'ellipseAngle'), '+=', lambda: binop('*', rt.call_ref(ref(e.get('Math'), 'round'), [binop('/', binop('+', ref(this, 'xStep').get(), ref(this, 'yStep').get()), 1.5)]), ref(this, 'ellipseDirectionMultiplier').get()))
    assign(ref(this, 'ellipseAngle'), '%=', lambda: 360)
    if truth(logical('||', logical('&&', binop('==', ref(this, 'ellipseDirectionMultiplier').get(), unary('-', 1)), lambda: logical('||', binop('>=', ref(this, 'ellipseAngle').get(), ref(this, 'ellipseTargetAngle').get()), lambda: binop('<', ref(this, 'ellipseAngle').get(), 50))), lambda: logical('&&', binop('==', ref(this, 'ellipseDirectionMultiplier').get(), 1), lambda: logical('||', binop('<=', ref(this, 'ellipseAngle').get(), ref(this, 'ellipseTargetAngle').get()), lambda: binop('<', ref(this, 'ellipseAngle').get(), unary('-', 180)))))):
        assign(ref(this, 'rocket_follow_ellipse'), '=', lambda: False)
        assign(ref(this, 'rocket_do_drop'), '=', lambda: True)
    assign(ref(ref(ref(this, 'MC').get(), 'maskMC').get(), '_x'), '+=', lambda: 1)
    return U

def Unit_randRange(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['min', 'max'], ['_loc4_', 'max', 'min'], closure, 'Unit')
    e.set('_loc4_', binop('+', rt.call_ref(ref(e.get('Math'), 'floor'), [binop('*', rt.call_ref(ref(e.get('Math'), 'random'), []), binop('+', binop('-', e.get('max'), e.get('min')), 1))]), e.get('min')))
    return e.get('_loc4_')
    return U

def Unit_resetTailUnload(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['param_next'], ['param_next'], closure, 'Unit')
    assign(ref(this, 'unloadNum'), '=', lambda: binop('+', ref(this, 'unloadNum').get(), 1))
    assign(ref(this, 'unloadTimer'), '=', lambda: 0)
    if truth(binop('==', ref(this, 'unloadNum').get(), ref(this, 'unloadMax').get())):
        switch_5 = e.get('param_next')
        case_6 = -1
        if case_6 == -1 and strict_eq(switch_5, 'flyOff'):
            case_6 = 0
        if case_6 == -1 and strict_eq(switch_5, 'stop'):
            case_6 = 1
        if case_6 == -1:
            case_6 = 2
        try:
            if 0 <= case_6 <= 0:
                assign(ref(this, 'action'), '=', lambda: 'flyOff')
                assign(ref(this, 'activeAndMoving'), '=', lambda: True)
                raise ASBreak()
            if 0 <= case_6 <= 1:
                assign(ref(this, 'action'), '=', lambda: 'stop')
            if 0 <= case_6 <= 2:
                return U
        except ASBreak:
            pass
    return U

def Unit___get__tankTopDirection(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Unit')
    assign(ref(this, 'adjside'), '=', lambda: binop('-', ref(ref(ref(this, 'wayPointArr').get(), 0).get(), '_x').get(), ref(this, 'curX').get()))
    assign(ref(this, 'oppside'), '=', lambda: binop('*', unary('-', 1), binop('-', ref(ref(ref(this, 'wayPointArr').get(), 0).get(), '_y').get(), ref(this, 'curY').get())))
    assign(ref(this, 'angle'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'atan2'), [ref(this, 'oppside').get(), ref(this, 'adjside').get()]))
    assign(ref(this, 'angle'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [binop('*', binop('/', ref(this, 'angle').get(), ref(e.get('Math'), 'PI').get()), 180)]))
    assign(ref(this, 'angle'), '+=', lambda: 181)
    assign(ref(this, 'frame'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [binop('*', binop('/', binop('*', binop('/', ref(this, 'angle').get(), 360), 100), 100), ref(this, 'frameCount').get())]))
    return ref(this, 'frame').get()
    return U

def Unit___get__unitDirection(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Unit')
    assign(ref(this, 'adjside'), '=', lambda: binop('-', ref(this, 'curX').get(), ref(this, 'prevX').get()))
    assign(ref(this, 'oppside'), '=', lambda: binop('*', unary('-', 1), binop('-', ref(this, 'curY').get(), ref(this, 'prevY').get())))
    assign(ref(this, 'angle'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'atan2'), [ref(this, 'oppside').get(), ref(this, 'adjside').get()]))
    assign(ref(this, 'angle'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [binop('*', binop('/', ref(this, 'angle').get(), ref(e.get('Math'), 'PI').get()), 180)]))
    assign(ref(this, 'angle'), '+=', lambda: 181)
    e.set('_loc2_', True)
    if truth(logical('&&', ref(this, 'instantTurn').get(), lambda: binop('!=', ref(this, 'mcID').get(), 'soldier001'))):
        if truth(logical('&&', binop('==', ref(this, 'prev_prev_angle').get(), ref(this, 'prev_angle').get()), lambda: binop('!=', ref(this, 'prev_angle').get(), ref(this, 'angle').get()))):
            assign(e.ref('_loc2_'), '=', lambda: True)
        else:
            assign(e.ref('_loc2_'), '=', lambda: False)
    assign(ref(this, 'prev_prev_angle'), '=', lambda: ref(this, 'prev_angle').get())
    assign(ref(this, 'prev_angle'), '=', lambda: ref(this, 'angle').get())
    if truth(e.get('_loc2_')):
        assign(ref(this, 'frame'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [binop('*', binop('/', binop('*', binop('/', ref(this, 'angle').get(), 360), 100), 100), ref(this, 'frameCount').get())]))
    if truth(logical('&&', binop('==', ref(this, 'mcID').get(), 'suicide_bomber'), lambda: unary('!', ref(this, 'activeAndMoving').get()))):
        assign(ref(this, 'frame'), '=', lambda: 50)
    if truth(binop('==', ref(this, 'mcID').get(), 'apache')):
        if truth(logical('&&', binop('<', ref(this, 'frameFixedAfterLiftOff').get(), 3), lambda: binop('!=', ref(this, 'action').get(), 'liftOff'))):
            assign(ref(this, 'frameFixedAfterLiftOff'), '=', lambda: binop('+', ref(this, 'frameFixedAfterLiftOff').get(), 1))
            assign(ref(this, 'frame'), '=', lambda: ref(this, 'fixedFrame').get())
    assign(ref(this, 'prev_targetX'), '=', lambda: ref(this, 'targetX').get())
    return ref(this, 'frame').get()
    return U

def Unit___get__rocketRotation(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Unit')
    assign(ref(this, 'adjside'), '=', lambda: binop('-', ref(this, 'curX').get(), ref(this, 'prevX').get()))
    assign(ref(this, 'oppside'), '=', lambda: binop('*', unary('-', 1), binop('-', ref(this, 'curY').get(), ref(this, 'prevY').get())))
    assign(ref(this, 'angle'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'atan2'), [ref(this, 'oppside').get(), ref(this, 'adjside').get()]))
    assign(ref(this, 'angle'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [binop('*', binop('/', ref(this, 'angle').get(), ref(e.get('Math'), 'PI').get()), 180)]))
    assign(ref(this, 'angle'), '+=', lambda: 181)
    return binop('*', ref(this, 'angle').get(), unary('-', 1))
    return U

def Unit___get__anti_distance(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Unit')
    e.set('_loc2_', rt.call_ref(ref(e.get('Math'), 'sqrt'), [binop('+', binop('*', binop('-', ref(this, 'curX').get(), ref(ref(this, 'anti_pos').get(), 0).get()), binop('-', ref(this, 'curX').get(), ref(ref(this, 'anti_pos').get(), 0).get())), binop('*', binop('-', ref(this, 'curY').get(), ref(ref(this, 'anti_pos').get(), 1).get()), binop('-', ref(this, 'curY').get(), ref(ref(this, 'anti_pos').get(), 1).get())))]))
    return e.get('_loc2_')
    return U

def Unit___get__anti_direction(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_'], closure, 'Unit')
    e.set('_loc2_', binop('-', ref(this, 'curX').get(), ref(ref(this, 'anti_pos').get(), 0).get()))
    e.set('_loc3_', binop('*', unary('-', 1), binop('-', ref(this, 'curY').get(), ref(ref(this, 'anti_pos').get(), 1).get())))
    assign(ref(this, 'angle'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'atan2'), [e.get('_loc3_'), e.get('_loc2_')]))
    assign(ref(this, 'angle'), '=', lambda: rt.call_ref(ref(e.get('Math'), 'round'), [binop('*', binop('/', ref(this, 'angle').get(), ref(e.get('Math'), 'PI').get()), 180)]))
    assign(ref(this, 'angle'), '+=', lambda: 181)
    e.set('_loc4_', rt.call_ref(ref(e.get('Math'), 'round'), [binop('*', binop('/', binop('*', binop('/', ref(this, 'angle').get(), 360), 100), 100), 18)]))
    return e.get('_loc4_')
    return U

def Unit___get__plane_distance_to_target(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Unit')
    assign(ref(this, 'targetX'), '=', lambda: ref(ref(ref(this, 'wayPointArr').get(), ref(this, 'curWayPoint').get()).get(), '_x').get())
    assign(ref(this, 'targetY'), '=', lambda: ref(ref(ref(this, 'wayPointArr').get(), ref(this, 'curWayPoint').get()).get(), '_y').get())
    e.set('_loc2_', rt.call_ref(ref(e.get('Math'), 'sqrt'), [binop('+', binop('*', binop('-', ref(this, 'curX').get(), ref(this, 'targetX').get()), binop('-', ref(this, 'curX').get(), ref(this, 'targetX').get())), binop('*', binop('-', ref(this, 'curY').get(), ref(this, 'targetY').get()), binop('-', ref(this, 'curY').get(), ref(this, 'targetY').get())))]))
    return e.get('_loc2_')
    return U

def Unit___get__plane_coords_at_cur_direction(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_', '_loc3_', '_loc4_'], closure, 'Unit')
    e.set('_loc2_', binop('-', ref(this, 'curX').get(), ref(this, 'prevX').get()))
    e.set('_loc3_', binop('*', unary('-', 1), binop('-', ref(this, 'curY').get(), ref(this, 'prevY').get())))
    e.set('_loc4_', binop('+', rt.call_ref(ref(e.get('Math'), 'atan2'), [ref(this, 'adjside').get(), ref(this, 'oppside').get()]), 5))
    assign(ref(this, 'plane_potential_target_x'), '=', lambda: binop('+', binop('*', rt.call_ref(ref(e.get('Math'), 'cos'), [e.get('_loc4_')]), ref(this, 'plane_distance_to_target').get()), ref(this, 'curX').get()))
    assign(ref(this, 'plane_potential_target_y'), '=', lambda: binop('+', binop('*', rt.call_ref(ref(e.get('Math'), 'sin'), [e.get('_loc4_')]), ref(this, 'plane_distance_to_target').get()), ref(this, 'curY').get()))
    return arr([ref(this, 'plane_potential_target_x').get(), ref(this, 'plane_potential_target_y').get()])
    return U

def Unit_distanceBetween(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_arr1', '_arr2'], ['_arr1', '_arr2', '_loc4_'], closure, 'Unit')
    e.set('_loc4_', rt.call_ref(ref(e.get('Math'), 'sqrt'), [binop('+', binop('*', binop('-', ref(e.get('_arr1'), 0).get(), ref(e.get('_arr2'), 0).get()), binop('-', ref(e.get('_arr1'), 0).get(), ref(e.get('_arr2'), 0).get())), binop('*', binop('-', ref(e.get('_arr1'), 1).get(), ref(e.get('_arr2'), 1).get()), binop('-', ref(e.get('_arr1'), 1).get(), ref(e.get('_arr2'), 1).get())))]))
    return e.get('_loc4_')
    return U

def Unit_distanceTo(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_arr'], ['_arr', '_loc3_', '_loc4_', '_loc5_'], closure, 'Unit')
    e.set('_loc3_', ref(e.get('_arr'), 0).get())
    e.set('_loc4_', ref(e.get('_arr'), 1).get())
    e.set('_loc5_', rt.call_ref(ref(e.get('Math'), 'sqrt'), [binop('+', binop('*', binop('-', ref(this, 'curX').get(), e.get('_loc3_')), binop('-', ref(this, 'curX').get(), e.get('_loc3_'))), binop('*', binop('-', ref(this, 'curY').get(), e.get('_loc4_')), binop('-', ref(this, 'curY').get(), e.get('_loc4_'))))]))
    return e.get('_loc5_')
    return U

def Unit_plane_circular_step(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Unit')
    assign(ref(this, 'prevX'), '=', lambda: ref(this, 'curX').get())
    assign(ref(this, 'prevY'), '=', lambda: ref(this, 'curY').get())
    e.set('_loc2_', binop('/', binop('*', ref(this, 'plane_cur_angle_in_circular_flight').get(), ref(e.get('Math'), 'PI').get()), 180))
    assign(ref(this, 'curX'), '=', lambda: binop('+', ref(ref(this, 'plane_angle_center').get(), 0).get(), binop('*', ref(this, 'plane_circular_radius').get(), rt.call_ref(ref(e.get('Math'), 'cos'), [e.get('_loc2_')]))))
    assign(ref(this, 'curY'), '=', lambda: binop('+', ref(ref(this, 'plane_angle_center').get(), 1).get(), binop('*', ref(this, 'plane_circular_radius').get(), rt.call_ref(ref(e.get('Math'), 'sin'), [e.get('_loc2_')]))))
    assign(ref(this, 'plane_cur_angle_in_circular_flight'), '%=', lambda: 360)
    assign(ref(this, 'plane_circular_radius'), '-=', lambda: 0.5)
    assign(ref(this, 'plane_cur_angle_in_circular_flight'), '+=', lambda: binop('*', 8, ref(this, 'plane_angle_step').get()))
    return U

def Unit_satellite_explosion(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Unit')
    if truth(unary('!', ref(this, 'satellite_eplosion_initiated').get())):
        assign(ref(this, 'satellite_eplosion_initiated'), '=', lambda: True)
        assign(ref(this, 'explosionMC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), ['explosion_warhead_4', binop('+', ref(this, 'unitName').get(), 'explosion'), rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), [])]))
        assign(ref(ref(this, 'explosionMC').get(), '_x'), '=', lambda: ref(ref(this, 'wildCard').get(), 'cityX').get())
        assign(ref(ref(this, 'explosionMC').get(), '_y'), '=', lambda: ref(ref(this, 'wildCard').get(), 'cityY').get())
        rt.call_ref(ref(ref(e.get('_global'), 'presenter').get(), 'updateSingleCity_byID'), [ref(ref(this, 'tr').get(), '_city').get(), ref(ref(this, 'tr').get(), '_casualties').get()])
    return U

def Unit_killUnit(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_explosionType'], ['_explosionType', '_loc0_'], closure, 'Unit')
    rt.call_ref(ref(this, 'removeTrail'), [])
    rt.call_ref(ref(ref(this, 'sound').get(), 'stop'), [])
    assign(ref(this, 'action'), '=', lambda: 'dying')
    rt.call_ref(ref(ref(this, 'MC').get(), 'removeMovieClip'), [])
    rt.call_ref(ref(ref(this, 'shadowMC').get(), 'removeMovieClip'), [])
    rt.call_ref(ref(ref(this, 'tintMC').get(), 'removeMovieClip'), [])
    if truth(e.get('_explosionType')):
        if truth(binop('!==', assign(e.ref('_loc0_'), '=', lambda: e.get('_explosionType')), 'rocket_self')):
            assign(ref(this, 'explosionMC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), ['explosion001', binop('+', ref(this, 'unitName').get(), 'explosion'), rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), [])]))
            assign(ref(ref(this, 'explosionMC').get(), '_x'), '=', lambda: ref(this, 'curX').get())
            assign(ref(ref(this, 'explosionMC').get(), '_y'), '=', lambda: ref(this, 'curY').get())
        else:
            assign(ref(this, 'explosionMC'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), ['explosion003', binop('+', ref(this, 'unitName').get(), 'explosion'), rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), [])]))
            assign(ref(ref(this, 'explosionMC').get(), '_x'), '=', lambda: ref(this, 'curX').get())
            assign(ref(ref(this, 'explosionMC').get(), '_y'), '=', lambda: ref(this, 'curY').get())
    assign(ref(this, 'unitStatus'), '=', lambda: 'dead')
    if truth(ref(this, 'anti_type').get()):
        assign(ref(this, 'anti_offset'), '=', lambda: 2)
        rt.call_ref(ref(ref(e.get('_global'), 'view').get(), 'updateAnti'), [this])
    return U

def Unit_removeUnit(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Unit')
    return U

def Unit_removeTrail(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc2_'], closure, 'Unit')
    assign(ref(this, 'trailActive'), '=', lambda: False)
    if truth(binop('>', ref(this, 'trailSize').get(), 0)):
        assign(e.ref('_loc2_'), '=', lambda: 0)
        while truth(binop('<', e.get('_loc2_'), binop('+', ref(this, 'trailSize').get(), 5))):
            rt.tick()
            try:
                if truth(ref(ref(this, 'container').get(), binop('+', binop('+', ref(this, 'unitName').get(), 'trailLeft'), e.get('_loc2_'))).get()):
                    rt.call_ref(ref(ref(ref(this, 'container').get(), binop('+', binop('+', ref(this, 'unitName').get(), 'trailLeft'), e.get('_loc2_'))).get(), 'removeMovieClip'), [])
                    rt.call_ref(ref(ref(ref(this, 'container').get(), binop('+', binop('+', ref(this, 'unitName').get(), 'trailRight'), e.get('_loc2_'))).get(), 'removeMovieClip'), [])
                else:
                    if truth(ref(ref(this, 'container').get(), binop('+', binop('+', ref(this, 'unitName').get(), 'trail'), e.get('_loc2_'))).get()):
                        rt.call_ref(ref(ref(ref(this, 'container').get(), binop('+', binop('+', ref(this, 'unitName').get(), 'trail'), e.get('_loc2_'))).get(), 'removeMovieClip'), [])
                assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
            except ASContinue:
                pass
            except ASBreak:
                break
    return U

def Unit_updateTrail(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], ['_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc14_', '_loc15_', '_loc16_', '_loc2_', '_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_'], closure, 'Unit')
    assign(ref(this, 'bool1'), '=', lambda: False)
    assign(ref(this, 'bool2'), '=', lambda: False)
    assign(ref(this, 'bool3'), '=', lambda: False)
    assign(ref(this, 'bool4'), '=', lambda: False)
    e.set('_loc2_', 0)
    while truth(binop('<', e.get('_loc2_'), ref(this, 'trailSize').get())):
        rt.tick()
        try:
            if truth(binop('==', ref(this, 'trailCount').get(), 2)):
                if truth(ref(this, 'trailActive').get()):
                    if truth(logical('&&', unary('!', ref(ref(this, 'container').get(), binop('+', binop('+', ref(this, 'unitName').get(), 'trailLeft'), e.get('_loc2_'))).get()), lambda: logical('&&', unary('!', ref(ref(this, 'trailArr').get(), e.get('_loc2_')).get()), lambda: unary('!', ref(this, 'bool1').get())))):
                        assign(e.ref('_loc3_'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), ['trail', binop('+', binop('+', ref(this, 'unitName').get(), 'trailLeft'), e.get('_loc2_')), rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), [])]))
                        assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), ['trail', binop('+', binop('+', ref(this, 'unitName').get(), 'trailRight'), e.get('_loc2_')), rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), [])]))
                        assign(ref(ref(this, 'trailArr').get(), e.get('_loc2_')), '=', lambda: True)
                        assign(ref(this, 'bool1'), '=', lambda: True)
                        assign(e.ref('_loc5_'), '=', lambda: ref(ref(this, 'container').get(), binop('+', binop('+', ref(this, 'unitName').get(), 'trailLeft'), e.get('_loc2_'))).get())
                        assign(e.ref('_loc6_'), '=', lambda: ref(ref(this, 'container').get(), binop('+', binop('+', ref(this, 'unitName').get(), 'trailRight'), e.get('_loc2_'))).get())
                        assign(e.ref('_loc7_'), '=', lambda: binop('*', binop('*', binop('/', binop('-', ref(this, 'angle').get(), 90), 180), ref(e.get('Math'), 'PI').get()), unary('-', 1)))
                        assign(e.ref('_loc8_'), '=', lambda: binop('*', binop('*', binop('/', binop('+', ref(this, 'angle').get(), 90), 180), ref(e.get('Math'), 'PI').get()), unary('-', 1)))
                        assign(ref(e.get('_loc5_'), '_alpha'), '-=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [binop('-', ref(this, 'trailSize').get(), e.get('_loc2_')), binop('-', 100, e.get('_loc2_'))]))
                        assign(ref(e.get('_loc6_'), '_alpha'), '-=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [binop('-', ref(this, 'trailSize').get(), e.get('_loc2_')), binop('-', 100, e.get('_loc2_'))]))
                        assign(ref(e.get('_loc5_'), '_x'), '=', lambda: binop('+', ref(this, 'curX').get(), binop('*', rt.call_ref(ref(e.get('Math'), 'cos'), [e.get('_loc7_')]), 15)))
                        assign(ref(e.get('_loc5_'), '_y'), '=', lambda: binop('+', ref(this, 'curY').get(), binop('*', rt.call_ref(ref(e.get('Math'), 'sin'), [e.get('_loc7_')]), 15)))
                        assign(ref(e.get('_loc6_'), '_x'), '=', lambda: binop('+', ref(this, 'curX').get(), binop('*', rt.call_ref(ref(e.get('Math'), 'cos'), [e.get('_loc8_')]), 15)))
                        assign(ref(e.get('_loc6_'), '_y'), '=', lambda: binop('+', ref(this, 'curY').get(), binop('*', rt.call_ref(ref(e.get('Math'), 'sin'), [e.get('_loc8_')]), 15)))
                        assign(ref(e.get('_loc5_'), '_sizePlus'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [1, 2]))
                        assign(ref(e.get('_loc5_'), '_alphaMin'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [1, 4]))
                        assign(ref(e.get('_loc6_'), '_sizePlus'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [1, 2]))
                        assign(ref(e.get('_loc6_'), '_alphaMin'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [1, 4]))
                if truth(ref(ref(this, 'container').get(), binop('+', binop('+', ref(this, 'unitName').get(), 'trailLeft'), e.get('_loc2_'))).get()):
                    assign(e.ref('_loc9_'), '=', lambda: ref(ref(this, 'container').get(), binop('+', binop('+', ref(this, 'unitName').get(), 'trailLeft'), e.get('_loc2_'))).get())
                    assign(e.ref('_loc10_'), '=', lambda: ref(ref(this, 'container').get(), binop('+', binop('+', ref(this, 'unitName').get(), 'trailRight'), e.get('_loc2_'))).get())
                    assign(ref(e.get('_loc9_'), '_height'), '+=', lambda: ref(e.get('_loc9_'), '_sizePlus').get())
                    assign(ref(e.get('_loc9_'), '_width'), '+=', lambda: ref(e.get('_loc9_'), '_sizePlus').get())
                    assign(ref(e.get('_loc9_'), '_alpha'), '-=', lambda: ref(e.get('_loc9_'), '_alphaMin').get())
                    if truth(binop('<=', ref(e.get('_loc9_'), '_alpha').get(), 0)):
                        rt.call_ref(ref(e.get('_loc9_'), 'removeMovieClip'), [])
                        rt.call_ref(ref(e.get('_loc10_'), 'removeMovieClip'), [])
                    assign(ref(e.get('_loc10_'), '_height'), '+=', lambda: ref(e.get('_loc10_'), '_sizePlus').get())
                    assign(ref(e.get('_loc10_'), '_width'), '+=', lambda: ref(e.get('_loc10_'), '_sizePlus').get())
                    assign(ref(e.get('_loc10_'), '_alpha'), '-=', lambda: ref(e.get('_loc10_'), '_alphaMin').get())
                    if truth(binop('<=', ref(e.get('_loc10_'), '_alpha').get(), 0)):
                        rt.call_ref(ref(e.get('_loc9_'), 'removeMovieClip'), [])
                        rt.call_ref(ref(e.get('_loc10_'), 'removeMovieClip'), [])
            else:
                if truth(binop('==', ref(this, 'trailCount').get(), 1)):
                    assign(ref(this, 'countDown_to_rocket_smoke'), '=', lambda: binop('-', ref(this, 'countDown_to_rocket_smoke').get(), 1))
                    if truth(logical('&&', ref(this, 'trailActive').get(), lambda: logical('||', logical('&&', binop('==', ref(this, 'mcID').get(), 'rocket'), lambda: binop('<=', ref(this, 'countDown_to_rocket_smoke').get(), 0)), lambda: binop('!=', ref(this, 'mcID').get(), 'rocket')))):
                        if truth(logical('&&', unary('!', ref(ref(this, 'container').get(), binop('+', binop('+', ref(this, 'unitName').get(), 'trail'), e.get('_loc2_'))).get()), lambda: logical('&&', unary('!', ref(ref(this, 'trailArr').get(), e.get('_loc2_')).get()), lambda: logical('&&', unary('!', ref(this, 'bool4').get()), lambda: logical('&&', binop('!=', ref(this, 'action').get(), 'rocket_follow_ellipse'), lambda: binop('!=', ref(this, 'action').get(), 'rocket_follow_ellipse_with_anti')))))):
                            assign(ref(ref(this, 'trailArr').get(), e.get('_loc2_')), '=', lambda: True)
                            assign(ref(this, 'bool1'), '=', lambda: True)
                            if truth(logical('&&', ref(this, 'bool1').get(), lambda: unary('!', ref(this, 'bool2').get()))):
                                assign(ref(this, 'bool2'), '=', lambda: True)
                            else:
                                if truth(logical('&&', ref(this, 'bool2').get(), lambda: unary('!', ref(this, 'bool3').get()))):
                                    assign(ref(this, 'bool3'), '=', lambda: True)
                                else:
                                    if truth(logical('&&', ref(this, 'bool3').get(), lambda: unary('!', ref(this, 'bool4').get()))):
                                        assign(ref(this, 'bool4'), '=', lambda: True)
                            assign(e.ref('_loc11_'), '=', lambda: rt.call_ref(ref(ref(this, 'container').get(), 'attachMovie'), ['trail', binop('+', binop('+', ref(this, 'unitName').get(), 'trail'), e.get('_loc2_')), rt.call_ref(ref(ref(this, 'container').get(), 'getNextHighestDepth'), [])]))
                            assign(ref(e.get('_loc11_'), '_width'), '=', lambda: assign(ref(e.get('_loc11_'), '_height'), '=', lambda: 8))
                            rt.call_ref(ref(e.get('_loc11_'), 'stop'), [])
                            if truth(binop('==', e.get('_loc2_'), ref(this, 'trailSize').get())):
                                pass
                            assign(e.ref('_loc12_'), '=', lambda: binop('*', binop('*', binop('/', ref(this, 'angle').get(), 180), ref(e.get('Math'), 'PI').get()), unary('-', 1)))
                            assign(e.ref('_loc13_'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [20, 45]))
                            assign(e.ref('_loc14_'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [28, 32]))
                            if truth(logical('||', binop('==', ref(this, 'mcID').get(), 'rocket'), lambda: binop('==', ref(this, 'mcID').get(), 'sub_rocket'))):
                                assign(e.ref('_loc15_'), '=', lambda: obj({'x': ref(ref(ref(this, 'MC').get(), 'smokeBase').get(), '_x').get(), 'y': ref(ref(ref(this, 'MC').get(), 'smokeBase').get(), '_y').get()}))
                                rt.call_ref(ref(ref(this, 'MC').get(), 'localToGlobal'), [e.get('_loc15_')])
                                assign(ref(e.get('_loc11_'), '_x'), '=', lambda: binop('+', ref(e.get('_loc15_'), 'x').get(), 4))
                                assign(ref(e.get('_loc11_'), '_y'), '=', lambda: ref(e.get('_loc15_'), 'y').get())
                            else:
                                if truth(binop('==', ref(this, 'mcID').get(), 'ship_plane')):
                                    assign(ref(e.get('_loc11_'), '_x'), '=', lambda: binop('+', ref(this, 'curX').get(), binop('*', rt.call_ref(ref(e.get('Math'), 'cos'), [e.get('_loc12_')]), ref(this, 'trail_offset').get())))
                                    assign(ref(e.get('_loc11_'), '_y'), '=', lambda: binop('+', binop('+', ref(this, 'curY').get(), 5), binop('*', rt.call_ref(ref(e.get('Math'), 'sin'), [e.get('_loc12_')]), ref(this, 'trail_offset').get())))
                                else:
                                    assign(ref(e.get('_loc11_'), '_x'), '=', lambda: ref(this, 'prevX').get())
                                    assign(ref(e.get('_loc11_'), '_y'), '=', lambda: ref(this, 'prevY').get())
                            assign(ref(e.get('_loc11_'), '_sizePlus'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [5, 11]))
                            assign(ref(e.get('_loc11_'), '_alphaMin'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [3, 15]))
                            assign(ref(e.get('_loc11_'), '_sizePlus'), '/=', lambda: 12)
                            assign(ref(e.get('_loc11_'), '_alphaMin'), '/=', lambda: 3)
                            assign(ref(e.get('_loc11_'), '_alpha'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'tools').get(), 'randRange'), [binop('-', ref(this, 'trailSize').get(), e.get('_loc2_')), binop('-', 100, e.get('_loc2_'))]))
                    if truth(ref(ref(this, 'container').get(), binop('+', binop('+', ref(this, 'unitName').get(), 'trail'), e.get('_loc2_'))).get()):
                        assign(e.ref('_loc16_'), '=', lambda: ref(ref(this, 'container').get(), binop('+', binop('+', ref(this, 'unitName').get(), 'trail'), e.get('_loc2_'))).get())
                        assign(ref(e.get('_loc16_'), '_height'), '+=', lambda: ref(e.get('_loc16_'), '_sizePlus').get())
                        assign(ref(e.get('_loc16_'), '_width'), '+=', lambda: ref(e.get('_loc16_'), '_sizePlus').get())
                        assign(ref(e.get('_loc16_'), '_alpha'), '-=', lambda: ref(e.get('_loc16_'), '_alphaMin').get())
                        if truth(binop('==', ref(this, 'mcID').get(), 'rocket')):
                            assign(ref(e.get('_loc16_'), '_y'), '-=', lambda: 0.3)
                        if truth(binop('<=', ref(e.get('_loc16_'), '_alpha').get(), 0)):
                            rt.call_ref(ref(e.get('_loc16_'), 'removeMovieClip'), [])
            assign(e.ref('_loc2_'), '=', lambda: binop('+', e.get('_loc2_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return U

def Unit_startSound(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Unit')
    if truth(unary('!', ref(this, 'soundPlaying').get())):
        rt.call_ref(ref(this, 'soundAction'), [ref(this, 'startSoundAction').get()])
        assign(ref(this, 'soundPlaying'), '=', lambda: True)
    return U

def Unit___get__soundPan(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Unit')
    return rt.call_ref(ref(e.get('Math'), 'round'), [binop('*', binop('-', binop('/', ref(ref(this, 'MC').get(), '_x').get(), 8), 50), 2)])
    return U

def Unit_updatePan(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Unit')
    rt.call_ref(ref(ref(this, 'sound').get(), 'setPan'), [ref(this, 'soundPan').get()])
    return U

def Unit_plane_flight_sound(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Unit')
    rt.call_ref(ref(this, 'soundAction'), [binop('+', ref(this, 'mcID').get(), '_flight')])
    return U

def f_7(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'attachSound'), [''])
    assign(ref(this, 'done'), '=', lambda: True)
    return U

def Unit_sound_anti_shoot(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['mc'], ['mc'], closure, 'Unit')
    if truth(logical('||', ref(ref(this, 'anti_shoot_sound').get(), 'done').get(), lambda: unary('!', ref(this, 'anti_shoot_sound').get()))):
        assign(ref(this, 'anti_shoot_sound'), '=', lambda: rt.construct(e.get('Anti_sound'), [e.get('mc')]))
        assign(ref(ref(this, 'anti_shoot_sound').get(), 'done'), '=', lambda: False)
        if truth(ref(ref(ref(e.get('_global'), 'model').get(), 'option').get(), 'playSound').get()):
            if truth(binop('==', ref(this, 'anti_type').get(), 'air')):
                rt.call_ref(ref(ref(this, 'anti_shoot_sound').get(), 'attachSound'), ['building_Anti air gun.wav'])
                rt.call_ref(ref(ref(this, 'anti_shoot_sound').get(), 'start'), [0, 8])
            else:
                rt.call_ref(ref(ref(this, 'anti_shoot_sound').get(), 'attachSound'), ['building_Anti rocket fire 4.wav'])
                rt.call_ref(ref(ref(this, 'anti_shoot_sound').get(), 'start'), [])
            assign(ref(ref(this, 'anti_shoot_sound').get(), 'onSoundComplete'), '=', lambda: ASFunction(f_7, e))
    return U

def f_8(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(this, 'curSound'), '=', lambda: e.get('undefined'))
    return U

def f_9(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    assign(ref(this, 'curSound'), '=', lambda: e.get('undefined'))
    return U

def Unit_sound_anti(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str', 'x'], ['_loc4_', '_str', 'x'], closure, 'Unit')
    if truth(unary('!', ref(ref(ref(e.get('_global'), 'model').get(), 'option').get(), 'playSound').get())):
        return e.get('undefined')
    if truth(unary('!', ref(this, 'anti_sound').get())):
        assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(ref(ref(e.get('_global'), 'view').get(), 'srcMC').get(), 'createEmptyMovieClip'), ['sound_mc', rt.call_ref(ref(ref(ref(e.get('_global'), 'view').get(), 'srcMC').get(), 'getNextHighestDepth'), [])]))
        assign(ref(this, 'anti_sound'), '=', lambda: rt.construct(e.get('Anti_sound'), [e.get('_loc4_')]))
        rt.call_ref(ref(ref(ref(e.get('_global'), 'model').get(), 'playedSounds_arr').get(), 'push'), [obj({'soundObj': ref(this, 'anti_sound').get(), 'mc': e.get('_loc4_')})])
    if truth(logical('&&', binop('==', ref(this, 'anti_type').get(), 'air'), lambda: unary('!', ref(ref(this, 'anti_sound').get(), 'curSound').get()))):
        assign(ref(ref(this, 'anti_sound').get(), 'curSound'), '=', lambda: 'rotate_anti')
        rt.call_ref(ref(ref(this, 'anti_sound').get(), 'attachSound'), ['building_Anti air rotate.wav'])
        assign(ref(ref(this, 'anti_sound').get(), 'onSoundComplete'), '=', lambda: ASFunction(f_8, e))
        rt.call_ref(ref(ref(this, 'anti_sound').get(), 'start'), [])
    else:
        if truth(logical('&&', binop('==', ref(this, 'anti_type').get(), 'rocket'), lambda: unary('!', ref(ref(this, 'anti_sound').get(), 'curSound').get()))):
            assign(ref(ref(this, 'anti_sound').get(), 'curSound'), '=', lambda: 'rotate_anti')
            rt.call_ref(ref(ref(this, 'anti_sound').get(), 'attachSound'), ['building_Anti air rotate.wav'])
            assign(ref(ref(this, 'anti_sound').get(), 'onSoundComplete'), '=', lambda: ASFunction(f_9, e))
            rt.call_ref(ref(ref(this, 'anti_sound').get(), 'start'), [])
    return U

def f_12(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'attachSound'), ['unit_fighterflight.wav'])
    rt.call_ref(ref(this, 'start'), [])
    return U

def f_13(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'attachSound'), ['unit_Carrierjet flight.wav'])
    rt.call_ref(ref(this, 'start'), [0, 999])
    return U

def f_14(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'attachSound'), ['unit_fighterflight.wav'])
    rt.call_ref(ref(this, 'start'), [])
    return U

def f_16(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    return U

def f_15(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, None)
    rt.call_ref(ref(this, 'attachSound'), ['Sattelite attack.wav'])
    rt.call_ref(ref(this, 'start'), [])
    assign(ref(this, 'onSoundComplete'), '=', lambda: ASFunction(f_16, e))
    return U

def Unit_soundAction(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['_str'], ['_str'], closure, 'Unit')
    if truth(logical('&&', binop('!=', ref(this, 'lastPlayedSoundAction').get(), e.get('_str')), lambda: ref(ref(ref(e.get('_global'), 'model').get(), 'option').get(), 'playSound').get())):
        assign(ref(this, 'lastPlayedSoundAction'), '=', lambda: e.get('_str'))
        switch_10 = e.get('_str')
        case_11 = -1
        if case_11 == -1 and strict_eq(switch_10, 'boat_start'):
            case_11 = 0
        if case_11 == -1 and strict_eq(switch_10, 'boat_stop'):
            case_11 = 1
        if case_11 == -1 and strict_eq(switch_10, 'soldier_running'):
            case_11 = 2
        if case_11 == -1 and strict_eq(switch_10, 'soldier_shoot'):
            case_11 = 3
        if case_11 == -1 and strict_eq(switch_10, 'marine_running'):
            case_11 = 4
        if case_11 == -1 and strict_eq(switch_10, 'marine_shoot'):
            case_11 = 5
        if case_11 == -1 and strict_eq(switch_10, 'apache_start'):
            case_11 = 6
        if case_11 == -1 and strict_eq(switch_10, 'apache_flyOff'):
            case_11 = 7
        if case_11 == -1 and strict_eq(switch_10, 'chinook_start'):
            case_11 = 8
        if case_11 == -1 and strict_eq(switch_10, 'chinook_flyOff'):
            case_11 = 9
        if case_11 == -1 and strict_eq(switch_10, 'tank_drive'):
            case_11 = 10
        if case_11 == -1 and strict_eq(switch_10, 'tank_shoot'):
            case_11 = 11
        if case_11 == -1 and strict_eq(switch_10, 'tank_stop'):
            case_11 = 12
        if case_11 == -1 and strict_eq(switch_10, 'suicide_scream'):
            case_11 = 13
        if case_11 == -1 and strict_eq(switch_10, 'suicide_explode'):
            case_11 = 14
        if case_11 == -1 and strict_eq(switch_10, 'rocket_launch'):
            case_11 = 15
        if case_11 == -1 and strict_eq(switch_10, 'plane001_takeOff'):
            case_11 = 16
        if case_11 == -1 and strict_eq(switch_10, 'plane001_flight'):
            case_11 = 17
        if case_11 == -1 and strict_eq(switch_10, 'plane002_takeOff'):
            case_11 = 18
        if case_11 == -1 and strict_eq(switch_10, 'plane002_flight'):
            case_11 = 19
        if case_11 == -1 and strict_eq(switch_10, 'ship_plane_takeOff'):
            case_11 = 20
        if case_11 == -1 and strict_eq(switch_10, 'sat_laser'):
            case_11 = 21
        if case_11 == -1 and strict_eq(switch_10, '_'):
            case_11 = 22
        if case_11 == -1:
            case_11 = 23
        try:
            if 0 <= case_11 <= 0:
                assign(ref(this, 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(this, 'MC').get()]))
                rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['unit_Soldier Motorboat loop.wav'])
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [0, 999])
                raise ASBreak()
            if 0 <= case_11 <= 1:
                rt.call_ref(ref(ref(this, 'sound').get(), 'stop'), [])
                ref(this, 'sound').delete()
                raise ASBreak()
            if 0 <= case_11 <= 2:
                assign(ref(this, 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(this, 'MC').get()]))
                rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['unit_Soldier running.wav'])
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [0, 999])
                raise ASBreak()
            if 0 <= case_11 <= 3:
                rt.call_ref(ref(ref(this, 'sound').get(), 'stop'), [])
                ref(this, 'sound').delete()
                assign(ref(this, 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(this, 'MC').get()]))
                rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['unit_Soldier gun.wav'])
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [0, 11])
                raise ASBreak()
            if 0 <= case_11 <= 4:
                assign(ref(this, 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(this, 'MC').get()]))
                rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['unit_seal running.wav'])
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [0, 999])
                raise ASBreak()
            if 0 <= case_11 <= 5:
                rt.call_ref(ref(ref(this, 'sound').get(), 'stop'), [])
                ref(this, 'sound').delete()
                assign(ref(this, 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(this, 'MC').get()]))
                rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['unit_seal gun.wav'])
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [0, 5])
                raise ASBreak()
            if 0 <= case_11 <= 6:
                assign(ref(this, 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(this, 'MC').get()]))
                rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['unit_seal chopper.wav'])
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [0, 999])
                raise ASBreak()
            if 0 <= case_11 <= 7:
                rt.call_ref(ref(ref(this, 'sound').get(), 'stop'), [])
                ref(this, 'sound').delete()
                assign(ref(this, 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(this, 'MC').get()]))
                rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['unit_seal chopper.wav'])
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [0, 2])
                raise ASBreak()
            if 0 <= case_11 <= 8:
                assign(ref(this, 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(this, 'MC').get()]))
                rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['unit_Tank chopper.wav'])
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [0, 999])
                raise ASBreak()
            if 0 <= case_11 <= 9:
                rt.call_ref(ref(ref(this, 'sound').get(), 'stop'), [])
                ref(this, 'sound').delete()
                assign(ref(this, 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(this, 'MC').get()]))
                rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['unit_Tank chopper.wav'])
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [0, 2])
                raise ASBreak()
            if 0 <= case_11 <= 10:
                assign(ref(this, 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(this, 'MC').get()]))
                rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['unit_Tank.wav'])
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [0, 6])
                raise ASBreak()
            if 0 <= case_11 <= 11:
                assign(ref(this, 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(this, 'MC').get()]))
                rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['unit_Tank gun.wav'])
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [0, 2])
                raise ASBreak()
            if 0 <= case_11 <= 12:
                rt.call_ref(ref(ref(this, 'sound').get(), 'stop'), [])
                ref(this, 'sound').delete()
                raise ASBreak()
            if 0 <= case_11 <= 13:
                rt.call_ref(ref(ref(this, 'sound').get(), 'stop'), [])
                ref(this, 'sound').delete()
                assign(ref(this, 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(this, 'MC').get()]))
                rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['unit_Suicide scream.wav'])
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [])
                raise ASBreak()
            if 0 <= case_11 <= 14:
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [])
                raise ASBreak()
            if 0 <= case_11 <= 15:
                assign(ref(this, 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(this, 'MC').get()]))
                rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['unit_Warrocket.wav'])
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [])
                raise ASBreak()
            if 0 <= case_11 <= 16:
                assign(ref(this, 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(this, 'MC').get()]))
                rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['unit_Fightertakeoff.wav'])
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [])
                assign(ref(ref(this, 'sound').get(), 'onSoundComplete'), '=', lambda: ASFunction(f_12, e))
                raise ASBreak()
            if 0 <= case_11 <= 17:
                pass
            if 0 <= case_11 <= 18:
                assign(ref(this, 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(this, 'MC').get()]))
                rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['unit_Carrierjet take off.wav'])
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [])
                assign(ref(ref(this, 'sound').get(), 'onSoundComplete'), '=', lambda: ASFunction(f_13, e))
                raise ASBreak()
            if 0 <= case_11 <= 19:
                pass
            if 0 <= case_11 <= 20:
                assign(ref(this, 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(this, 'MC').get()]))
                rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['unit_Fightertakeoff.wav'])
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [])
                assign(ref(ref(this, 'sound').get(), 'onSoundComplete'), '=', lambda: ASFunction(f_14, e))
                raise ASBreak()
            if 0 <= case_11 <= 21:
                assign(ref(this, 'sound'), '=', lambda: rt.construct(e.get('Sound'), [ref(this, 'MC').get()]))
                rt.call_ref(ref(ref(this, 'sound').get(), 'attachSound'), ['unit_Sattelite Lasershot.wav'])
                rt.call_ref(ref(ref(this, 'sound').get(), 'start'), [])
                assign(ref(ref(this, 'sound').get(), 'onSoundComplete'), '=', lambda: ASFunction(f_15, e))
                raise ASBreak()
            if 0 <= case_11 <= 22:
                pass
            if 0 <= case_11 <= 23:
                return U
        except ASBreak:
            pass
    return U

def Unit_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'Unit')
    ref(this, 'debug').set(False)
    ref(this, 'liftOff').set(False)
    ref(this, 'maxShotCount').set(10)
    ref(this, 'depthSet').set(False)
    ref(this, 'depthSwap').set(False)
    ref(this, 'scale_up').set(False)
    ref(this, 'scale_down').set(False)
    ref(this, 'trailCountDown').set(0)
    ref(this, 'bool1').set(False)
    ref(this, 'bool2').set(False)
    ref(this, 'bool3').set(False)
    ref(this, 'bool4').set(False)
    ref(this, 'apache_liftOffCount').set(0)
    ref(this, 'apache_liftOffCountMax').set(25)
    ref(this, 'heliStartPlusX').set(0)
    ref(this, 'heliStartPlusY').set(0)
    ref(this, 'suicide_commando_wait_countDown_max').set(25)
    ref(this, 'suicide_commando_wait_countDown_cur').set(0)
    ref(this, 'rocket_follow_ellipse').set(False)
    ref(this, 'rocket_do_drop').set(False)
    ref(this, 'anti_fire_start_distance').set(25)
    ref(this, 'shadowStartAlpha').set(100)
    ref(this, 'shadowStartAtUnitBase').set(False)
    ref(this, 'heli_direction_set').set(0)
    ref(this, 'frameFixedAfterLiftOff').set(0)
    ref(this, 'TAXI_COUNT_MAX').set(30)
    ref(this, 'cur_taxi_count').set(0)
    ref(this, 'PLANE_COUNT_TO_FREE_FLIGHT').set(8)
    ref(this, 'cur_count_to_free_flight').set(0)
    ref(this, 'plane_cur_angle_in_circular_flight').set(100)
    ref(this, 'plane_cur_angle_on_map').set(0)
    ref(this, 'plane_potential_target_x').set(0)
    ref(this, 'plane_potential_target_y').set(0)
    ref(this, 'plane_circular_flight_center_x').set(0)
    ref(this, 'plane_circular_flight_center_y').set(0)
    ref(this, 'PLANE_COUNTDOWN_TO_SET_DIRECTION_MAX').set(5)
    ref(this, 'plane_cur_countdown_to_set_direction').set(0)
    ref(this, 'plane_circular_radius').set(100)
    ref(this, 'countDown_antiStart').set(50)
    ref(this, 'satellite_lineAlphaStart').set(0)
    ref(this, 'satellite_alphaPlus').set(True)
    ref(this, 'satellite_eplosion_initiated').set(False)
    ref(this, 'soundPlaying').set(False)
    ref(this, 'instantTurn').set(False)
    ref(this, 'floorFrame').set(False)
    ref(this, 'prev_angle').set(0)
    ref(this, 'prev_prev_angle').set(0)
    ref(this, 'plane_countdown_default').set(6)
    ref(this, 'cancelBib').set(False)
    ref(this, 'max_unit_live').set(5000)
    ref(this, 'cur_unit_live').set(0)
    ref(this, 'unit_live_countdown_status').set(False)
    ref(this, 'traceMe').set(False)
    ref(this, 'countDown_to_rocket_smoke').set(500)
    ref(this, 'plane_circFlight_frames_count').set(0)
    ref(this, 'sub_launch_timer').set(0)
    ref(this, 'trail_offset').set(20)
    ref(this, 'has_fired_laser_sound').set(False)
    ref(this, 'tank_preshot_count').set(0)
    ref(this, 'plane_airTime').set(0)

def register(rt):
    rt.define('Unit', None, Unit_fields, {'Unit': ASFunction(Unit_Unit), 'moveUnit': ASFunction(Unit_moveUnit), 'setStep': ASFunction(Unit_setStep), 'deg2rad': ASFunction(Unit_deg2rad), 'rocket_drop': ASFunction(Unit_rocket_drop), 'ellipse_step': ASFunction(Unit_ellipse_step), 'randRange': ASFunction(Unit_randRange), 'resetTailUnload': ASFunction(Unit_resetTailUnload), 'distanceBetween': ASFunction(Unit_distanceBetween), 'distanceTo': ASFunction(Unit_distanceTo), 'plane_circular_step': ASFunction(Unit_plane_circular_step), 'satellite_explosion': ASFunction(Unit_satellite_explosion), 'killUnit': ASFunction(Unit_killUnit), 'removeUnit': ASFunction(Unit_removeUnit), 'removeTrail': ASFunction(Unit_removeTrail), 'updateTrail': ASFunction(Unit_updateTrail), 'startSound': ASFunction(Unit_startSound), 'updatePan': ASFunction(Unit_updatePan), 'plane_flight_sound': ASFunction(Unit_plane_flight_sound), 'sound_anti_shoot': ASFunction(Unit_sound_anti_shoot), 'sound_anti': ASFunction(Unit_sound_anti), 'soundAction': ASFunction(Unit_soundAction)}, {'appMC_depth': ASFunction(Unit___get__appMC_depth), 'tankTopDirection': ASFunction(Unit___get__tankTopDirection), 'unitDirection': ASFunction(Unit___get__unitDirection), 'rocketRotation': ASFunction(Unit___get__rocketRotation), 'anti_distance': ASFunction(Unit___get__anti_distance), 'anti_direction': ASFunction(Unit___get__anti_direction), 'plane_distance_to_target': ASFunction(Unit___get__plane_distance_to_target), 'plane_coords_at_cur_direction': ASFunction(Unit___get__plane_coords_at_cur_direction), 'soundPan': ASFunction(Unit___get__soundPan)}, {'appMC_depth': ASFunction(Unit___set__appMC_depth)})
