import math
import pytest
from wd2.game import Game
from wd2.runtime import *


def quiet_opponents(game):
    # Isolate human actions by suppressing AI selection, retaining all cities.
    game.model.set('doTurn',lambda:game.model.set('turn',get(game.model,'turn')+1))


@pytest.mark.parametrize('difficulty,money,population',[(0,80,500),(1,65,450),(2,55,400)])
def test_initial_difficulty_tables(difficulty,money,population):
    game=Game(0,difficulty)
    assert get(game.human,'money')==money
    assert get(game.human,'population')==population
    assert all(get(p,'population')==450 for p in game.players.items[1:])
    assert (get(get(game.human,'cityArr')[0],'xPos'),get(get(game.human,'cityArr')[0],'yPos'))==(335.65,416.7)


def test_resources_and_religion_execute_recovered_rules():
    g=Game(0,1); quiet_opponents(g)
    g.queue('resources'); g.queue('religion'); g.advance()
    # 450 / 11 rounded = 41; media falls 5..10 then receives 30 points.
    assert get(g.human,'money')==106
    assert 85<=get(g.human,'religion')<=90
    assert get(g.model,'turn')==1


def test_direct_attack_consumes_stock_and_applies_calculated_casualties():
    g=Game(); quiet_opponents(g); city=get(g.players[1],'cityArr')[0]; before=get(city,'population')
    g.queue('attack',weapon='soldier1',target=1,city=0); g.queue('resources'); g.advance()
    event=next(e for e in g.events if e.get('_item')=='battle' and e.get('_player')==0)
    assert 2<=event['_casualties']<=4
    assert get(city,'population')==before-event['_casualties']
    assert get(g.rt.invoke(get(g.human,'weaponStock'),'getWeaponByName','soldier1'),'inStock')==0


def test_research_unlock_and_production():
    g=Game(); quiet_opponents(g)
    g.queue('research',tech='soldier2'); g.queue('production',category='soldier',percent=50); g.advance()
    assert truth(get(g.rt.invoke(get(g.human,'techTree'),'getTechByName','soldier2'),'invented'))
    assert get(g.rt.invoke(get(g.human,'weaponStock'),'getWeaponByName','soldier1'),'inStock')>1
    assert get(g.human,'money')<65


def test_prepare_then_launch_consumes_carrier_and_payload():
    g=Game(); quiet_opponents(g); city=get(g.players[1],'cityArr')[0]; before=get(city,'population')
    g.queue('preAttack',weapon='rocket1'); g.queue('resources'); g.advance()
    assert get(g.human,'preAttackStatus')=='ready'
    g.queue('preAttack',payload='warhead1',target=1,city=0); g.queue('resources'); g.advance()
    event=next(e for e in g.events if e.get('_item')=='battle' and e.get('_player')==0)
    assert 10<=event['_casualties']<=15
    assert get(city,'population')==before-event['_casualties']
    assert get(g.human,'preAttackStatus')=='inactive'
    for name in ('rocket1','warhead1'):
        assert get(g.rt.invoke(get(g.human,'weaponStock'),'getWeaponByName',name),'inStock')==0


def test_clear_refunds_reservations_and_requires_two_actions():
    g=Game(); g.queue('production',category='soldier',percent=50)
    assert get(g.human,'turnMoney')<65
    with pytest.raises(ValueError,match='two actions'): g.advance()
    g.clear_actions(); assert get(g.human,'turnMoney')==65
    assert all(get(t,'action') is U for t in get(g.human,'turnActionArr'))


def test_invalid_attack_does_not_consume_action():
    g=Game()
    with pytest.raises(ValueError): g.queue('attack',weapon='soldier4')
    assert all(get(t,'action') is U for t in get(g.human,'turnActionArr'))


def test_last_city_destruction_eliminates_player_in_same_turn():
    g=Game(); quiet_opponents(g)
    enemy=g.players[1]
    for i,c in enumerate(get(enemy,'cityArr')):
        c.set('population',1 if i==0 else 0); c.set('prevPopulation',1 if i==0 else 0)
    g.queue('attack',weapon='soldier1',target=1,city=0); g.queue('resources'); g.advance()
    assert get(enemy,'population')==0 and not truth(get(enemy,'alive'))
    assert enemy not in get(g.model,'activePlayerArr').items


@pytest.mark.parametrize('difficulty,seed',[(0,0),(0,9),(1,0),(1,9),(2,0),(2,9)])
def test_forty_turns_with_original_ai(difficulty,seed):
    g=Game(seed,difficulty)
    for _ in range(40):
        if not truth(get(g.human,'alive')): break
        g.queue('resources'); g.queue('religion'); g.advance()
        for player in g.players:
            assert math.isfinite(number(get(player,'money')))
            assert math.isfinite(number(get(player,'population')))
    # This unresolved typo exists in the original AI_specialization.as:30.
    # Calls to absent UI children can occur when original code removes effects.
    assert set(g.rt.missing_calls)<= {'randrange','removeMovieClip','gotoAndStop'}
