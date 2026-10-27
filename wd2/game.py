"""Headless game adapter. Rules execute the recovered generated Python functions."""
import json
import math
from pathlib import Path
from .runtime import *
from .generated import register_all
from .host import HeadlessHost


class Game:
    def __init__(self,seed=0,difficulty=1):
        if difficulty not in (0,1,2): raise ValueError('Difficulty must be 0, 1 or 2')
        self.rt=Runtime(seed); register_all(self.rt); r=self.rt
        self.host=HeadlessHost(r)
        self.model=r.new('Model'); r.globals.set('model',self.model)
        self.model.set('difficulty_level',difficulty); self.model.set('turn',0)
        self.model.set('decisionPoints',r.new('DecisionPoints'))
        r.invoke(get(self.model,'decisionPoints'),'set_points_to_difficulty',difficulty)
        self.presenter=r.new('Presenter',self.model); r.globals.set('presenter',self.presenter)
        self.players=arr([r.new('Player','human' if i==0 else 'AI',i,arr([0,0])) for i in range(5)])
        self.model.set('playerArr',self.players); self.model.set('activePlayerArr',arr(self.players.items))
        self.human=self.players[0]; self.model.set('human',self.human)
        menu=r.new('Model_gameMenu')
        for i,p in enumerate(self.players):
            p.set('religion_code',['chr','mus','bhu','com','jew'][i])
            p.set('buildingSet_id',r.invoke(menu,'get_religion_buildingSet_by_code',get(p,'religion_code')))
            if i: self.model.set('comp'+str(i),p)
        r.invoke(self.presenter,'set_player_vars')
        battle=obj()
        root=Path(__file__).resolve().parents[1]
        anchor_path=root/'assets/runtime/battle_anchors.json'
        if anchor_path.exists():
            anchors=json.loads(anchor_path.read_text(encoding='utf-8'))
        else:
            placements=json.loads((root/'reverse/swf_inventory.json').read_text(encoding='utf-8'))['placements']
            anchors={p['name']:p['matrix'][4:] for p in placements if p['parent_id']==5766
                     and p.get('name','').startswith(('citypos','swp','twp'))}
        for i,positions in enumerate(get(self.model,'cityPositions')):
            for j,xy in enumerate(positions): battle.set(f'citypos{i}_{j}',obj({'_x':xy[0],'_y':xy[1]}))
            for j in (1,2): battle.set(f'ab{i}_{j}',self.host.clip())
        for name,xy in anchors.items():
            battle.set(name,obj({'_x':xy[0],'_y':xy[1]}))
        view=self.host.view(battle); self.presenter.set('view',view); r.globals.set('view',view)
        r.invoke(self.presenter,'spawn_cities')
        for i,p in enumerate(self.players):
            for j,city in enumerate(get(p,'cityArr')):
                xy=get(self.model,'cityPositions')[i][j]
                r.invoke(city,'setMapVars',battle,0,xy[0],xy[1])
                city.set('theme',get(p,'buildingSet_id'))
                clip=self.host.clip(); clip.set('propagandaBeams',self.host.clip()); clip.set('propagandaBeams2',self.host.clip()); city.set('image',clip)
                city.set('prevPopulation',get(city,'population')); clip.set('_currentframe',get(city,'size_and_frame'))
        self.events=[]

    def queue(self,action,*,target=1,city=0,weapon=None,payload=None,tech=None,category='soldier',percent=100,diplomacy=0):
        r=self.rt; human=self.human
        ta=r.invoke(human,'getNextTurnAction')
        if not truth(ta): raise ValueError('Both action slots are filled')
        if action not in ('resources','religion','production','research','attack','defense','propaganda','diplomacy','preAttack'): raise ValueError('Unknown action')
        other=self.players[target] if 0<=target<5 else U
        target_city=get(other,'cityArr')[city] if other is not U and 0<=city<5 else U
        if action in ('attack','propaganda','diplomacy') and (target==0 or not truth(get(other,'alive'))): raise ValueError('Choose a living opponent')
        if action in ('attack','propaganda') and not (number(get(target_city,'population'))>0): raise ValueError('Choose a populated city')
        stock=get(human,'weaponStock'); w=r.invoke(stock,'getWeaponByName',weapon) if weapon else U
        launching=action=='preAttack' and get(human,'preAttackStatus')=='ready'
        if launching: w=get(human,'preAttackWeapon'); weapon=get(w,'weaponName')
        if action in ('attack','defense','preAttack'):
            if w is U or not truth(get(w,'active')) or (not launching and number(get(w,'inStock'))-number(get(w,'inUse'))<=0): raise ValueError('Weapon is unavailable')
        if action in ('attack','propaganda') or launching:
            if truth(get(get(human,'ceaseFireArr')[target],'_status')) and get(w,'weaponType')!='spy': raise ValueError('A ceasefire prevents this attack')
        if action=='attack' and get(w,'weaponType') not in ('soldier','spy'): raise ValueError('This weapon requires preparation or defense')
        if action=='defense' and weapon not in ('antiAir','antiRocket'): raise ValueError('Select antiAir or antiRocket')
        if action=='production':
            if not 0<percent<=100: raise ValueError('Percentage must be 1..100')
            rows=get(ta,'productionInvestmentArr'); row=next((x for x in rows if isinstance(x,ASArray) and x[0]==category),None)
            if row is None: raise ValueError('Unknown production category')
            budget=math.floor(number(get(human,'turnMoney'))*percent/100)
            row.set(1,percent); row.set(3,budget); human.set('turnMoney',number(get(human,'turnMoney'))-budget)
        if action=='research':
            tree=get(human,'techTree'); t=r.invoke(tree,'getTechByName',tech) if isinstance(tech,str) else r.invoke(tree,'getTechByID',tech)
            if not truth(t) or truth(get(t,'invented')): raise ValueError('Choose an uninvented technology')
            prerequisite=get(t,'requiredTech')
            if number(get(t,'techLevel'))!=1 and not truth(get(prerequisite,'invented')): raise ValueError('Research the prerequisite first')
            cost=number(get(t,'cost'))
            if cost>number(get(human,'turnMoney')): raise ValueError('Not enough money')
            ta.set('researchArr',arr([obj({'techID':get(t,'techID')})])); human.set('turnMoney',number(get(human,'turnMoney'))-cost)
        if action in ('attack','defense'): ta.set('attackWeapon',w); w.set('inUse',number(get(w,'inUse'))+1)
        if action=='preAttack':
            if weapon not in ('rocket1','rocket2','rocket3','rocket4','plane1','plane2','sub','ship','space'): raise ValueError('Choose a carrier')
            ta.set('preAttackCarrier',w)
            if launching:
                pay=r.invoke(stock,'getWeaponByName',payload)
                if pay is U or not truth(get(pay,'active')) or number(get(pay,'inStock'))-number(get(pay,'inUse'))<1: raise ValueError('Choose an available payload')
                carrier_type=get(w,'weaponType')
                if carrier_type in ('rocket','plane') and (get(pay,'weaponCategory')!='payload' or number(get(pay,'weaponLevel'))>number(get(w,'weaponLevel'))): raise ValueError('Payload exceeds the carrier capacity')
                if carrier_type=='sub' and get(pay,'weaponCategory')!='payload': raise ValueError('Submarines require a warhead or bioload')
                if carrier_type=='space' and payload!='specialLoad': raise ValueError('Space rockets require a satellite')
                if carrier_type=='ship':
                    if get(pay,'weaponType')!='plane': raise ValueError('Aircraft carriers require a plane')
                    ta.set('ship_attack_arr',arr([obj({'city':get(target_city,'cityID'),'wpn':get(pay,'weaponID')})]))
                ta.set('preAttackPayload',pay)
                pay.set('inUse',number(get(pay,'inUse'))+1)
            w.set('inUse',number(get(w,'inUse'))+1)
        if action=='diplomacy':
            if not 0<=diplomacy<6: raise ValueError('Diplomacy option must be 0..5')
            option=get(self.model,'diplomacy_options_arr')[diplomacy]
            if option[0]=='offer':
                if number(get(human,'turnMoney'))<option[2]: raise ValueError('Not enough money')
                human.set('turnMoney',number(get(human,'turnMoney'))-option[2])
            ta.set('diplomacyLeader',target); ta.set('diplomacyOption',diplomacy)
        ta.set('action',action); ta.set('targetPlayer',other); ta.set('targetCity',target_city); ta.set('spyBuilding','spyCenter')
        return ta

    def clear_actions(self):
        for ta in get(self.human,'turnActionArr'): self.rt.invoke(ta,'doReset')
        self.human.set('turnMoney',get(self.human,'money'))

    def advance(self):
        if not truth(get(self.human,'allActionsSet')): raise ValueError('Choose two actions first')
        r=self.rt; r.reset_budget()
        r.invoke(self.model,'doTurn')
        r.invoke(self.presenter,'turnResults')
        results=get(self.model,'turnResultsArr')
        self.events=[{k:plain(v) for k,v in tr.props.items()} for tr in results]
        r.invoke(get(self.model,'battle'),'createBattleScriptVars')
        # In Flash, unit animations call this gameplay-affecting City method before
        # updatePlayerVars_1 checks defeat. Resolve those callbacks synchronously.
        for p in self.players:
            for city in get(p,'cityArr'):
                casualties=number(get(city,'total_battle_casualties'))
                casualties+=sum(number(x) for x in get(city,'propagandaMin'))
                casualties-=number(get(city,'propagandaPlus'))
                r.invoke(city,'size_and_frame_in_battle',casualties,False)
        r.invoke(self.presenter,'updatePlayerVars_1')
        for p in self.players:
            for city in get(p,'cityArr'):
                # View.updateCities normally reads this getter and synchronizes these fields.
                city.set('population',max(0,number(get(city,'population'))))
                get(city,'image').set('_currentframe',get(city,'size_and_frame'))
                city.set('prevPopulation',get(city,'population')); city.set('curCasualties',0)
        return self.snapshot()

    def snapshot(self):
        return {'turn':get(self.model,'turn'),'players':[{
            'id':get(p,'playerNum'),'alive':get(p,'alive'),'money':get(p,'money'),'population':get(p,'population'),
            'religion':get(p,'religion'),'score':get(p,'score'),'cities':[get(c,'population') for c in get(p,'cityArr')],
            'weapons':{get(w,'weaponName'):get(w,'inStock') for w in get(get(p,'weaponStock'),'weaponArr')},
            'research':[get(t,'techName') for t in get(get(p,'techTree'),'techArr') if truth(get(t,'invented'))],
            'messages':[get(msg,'_msg') for msg in get(p,'shortMSG_arr')]} for p in self.players],
            'missing_calls':self.rt.missing_calls.copy(),'host_state':self.host.state}


def plain(value,depth=0):
    if value is U: return None
    if isinstance(value,float) and not math.isfinite(value): return None
    if isinstance(value,ASArray): return [plain(x,depth+1) for x in value] if depth<5 else '[array]'
    if isinstance(value,ASObject): return {k:plain(v,depth+1) for k,v in value.props.items()} if depth<5 else '[object]'
    return value


def main():
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--turns',type=int,default=1); parser.add_argument('--seed',type=int,default=0); parser.add_argument('--difficulty',type=int,default=1)
    args=parser.parse_args(); game=Game(args.seed,args.difficulty)
    for _ in range(args.turns):
        if not truth(get(game.human,'alive')): break
        for __ in range(2):
            if truth(game.rt.invoke(game.human,'getNextTurnAction')): game.queue('resources')
        game.advance()
    print(json.dumps(plain(obj(game.snapshot())),indent=2,default=str))


if __name__=='__main__': main()
