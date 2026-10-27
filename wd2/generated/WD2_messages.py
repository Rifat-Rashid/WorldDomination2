# Generated from __Packages/WD2_messages.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def WD2_messages_WD2_messages(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'WD2_messages')
    return U

def WD2_messages_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'WD2_messages')
    ref(this, 'action_production_initial_infoText').set("Please choose a weapon from your arsenal on the left. <br> Only weapons displayed in orange can be purchased, other weapons are inactive and need to be invented first. Choose the 'technology' action for this")
    ref(this, 'action_production_initial_infoLine').set('Production: Select weapons')
    ref(this, 'action_research_initial_infoLine').set('Research technology: Select from your arsenal')
    ref(this, 'action_research_initial_infoText').set('Choose a technology to invent from your arsenal')
    ref(this, 'action_resources_initial_infoLine').set('Resources: Increase your money')
    ref(this, 'action_resources_initial_infoText').set('Increase your money by gathering resources.')
    ref(this, 'action_religion_initial_infoLine').set('Religion: Defend agains propaganda attacks')
    ref(this, 'action_religion_initial_infoText').set('Increase the religion level of your people and prevent propaganda attacks')
    ref(this, 'action_preAttack_initial_infoLine').set('Prepaired attack: ')
    ref(this, 'action_preAttack_initial_infoText').set('Prepare an attack. Select a rocket or plane from your arsenal. You can launch this weapon in the next turn')
    ref(this, 'action_dirattack_initial_infoLine').set('Attack the enemy!')
    ref(this, 'action_dirattack_initial_infoText').set('Select a weapon from your arsenal to attack the enemy')
    ref(this, 'action_defense_initial_infoLine').set('Defend against a prepaired attack')
    ref(this, 'action_defense_initial_infoText').set('Select anti-air or anti-rocket defense from your arsenal')
    ref(this, 'action_propaganda_initial_infoLine').set('Propaganda attack on an enemy city:')
    ref(this, 'action_propaganda_initial_infoText').set('Select an enemy city on the map to perform the propaganda attack on ')
    ref(this, 'action_diplomacy_initial_infoLine').set('Diplomacy: Select an player')
    ref(this, 'action_diplomacy_initial_infoText').set('Choose an opponent to perform the diplomacy action on')

def register(rt):
    rt.define('WD2_messages', None, WD2_messages_fields, {'WD2_messages': ASFunction(WD2_messages_WD2_messages)}, {}, {})
