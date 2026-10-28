"""Independent original-bytecode decision expectations with controlled draws.

Covers three difficulties, early/late funds and religion, expanded equipment,
and special/suicide flags. Expectations include actions, targets, weapons,
diplomacy, RNG count/state and scores rounded to nine decimals. Equal-score
ordering is deliberately not asserted; native Flash RNG is not reproduced.
"""
import hashlib
import pytest
import wd2.game as engine
from wd2.runtime import Runtime, get, arr, string

class Draws:
    def __init__(self, seed): self.state=seed; self.count=0
    def random(self):
        self.state=(self.state*1664525+1013904223)%4294967296
        self.count+=1
        return self.state/4294967296

def configure(g,case):
    phase=case//3
    g.model.set('turn',phase*5)
    for i,p in enumerate(g.players):
        if i==0: continue
        if phase>0:
            p.set('money',phase*30+i*7);p.set('religion',(phase*17+i*11)%101)
            p.set('regardArr',arr([(phase*13+i*7+j*11)%101 for j in range(5)]))
        if phase>=4:
            g.rt.invoke(get(p,'techTree'),'invent_below_tech_level',4)
            g.rt.invoke(get(p,'weaponStock'),'set_wpn_stock_per_level',1,3)
            g.rt.invoke(get(p,'weaponStock'),'set_wpn_stock_per_level',2,2)
            for w in get(get(p,'weaponStock'),'weaponArr'):
                w.set('active',get(g.rt.invoke(get(p,'techTree'),'getTechByName',get(w,'relatedTechName')),'invented'))
        if phase in (7,8): p.set('special_person',True)
        if phase in (9,10): p.set('suicide_person',True)

def value(x):
    return string(x)

def trace(g,case,draws):
    rows=[f'PROBE|rng|{case}|{draws.count}|{draws.state}']
    for i,p in enumerate(g.players):
        if not i:continue
        for score in get(p,'actionArr'):
            rows.append('|'.join(map(value,['PROBE','score',case,i,get(score,'id'),get(score,'amount')])))
        for ta in get(p,'turnActionArr'):
            vals=[get(ta,'action'),get(get(ta,'targetPlayer'),'playerNum'),get(get(ta,'targetCity'),'cityID')]
            vals += [get(get(ta,k),'weaponName') for k in ('attackWeapon','preAttackCarrier','preAttackPayload')]
            vals += [get(ta,k) for k in ('diplomacyLeader','diplomacyOption','spyBuilding')]
            rows.append('|'.join(map(value,['PROBE','action',case,i,*vals])))
    return rows

EXPECTED = [
    '7fdd1afadb2df9b0cb048954bbd7112394c13bd17a907a417bd2192be6e17937',
    '0e3ad5fe0054dcd4455751b9dee1293a5d1599e67cc7ad2f204ff1ac1d4a716e',
    'f50ff8bd57471c049d45e2d984faa288057f70fefc7d144f4bf8c9961766ba38',
    '3c0471c8312bdc15413f5564377d7e8c654dcc11c16153d4db636b6b6e2241de',
    '8b89a71f48cb866d151b423f341c1025ff4d6a3702661ceafe04fa62d1d5beae',
    '3b2aada951fa28c6d782ec01f9af6e61aa8cdc7443a66a146d9acdb93c70538a',
    'acaafedf87817cf5234b2a0312edf9ad45902eb43c07eb88fc1e60192fa072c2',
    '777275b3dc808c407b3ff909d31919853b75a499974290ebb4bfcc339a92ba11',
    '8485df0a53edd00f3197cc5ca5880eeb162b7012f0cd33b30671f78ec87228a6',
    '9bb325176a6223bf29a89de149b773c20407f1ae102ecc90215f35bf438a4074',
    '824afd1345bee554ebd5d43dfedf501d1fff31d93cf2b3006720633d95125c2f',
    '3171ff85fde96a2cd45ab9562d46914dc5de1a56f9127a7c71879a3158c27030',
    '6f24cd2d794afa3527238eefe4c79d33f3e4b2d792fe834069d0c8dc4b84503d',
    '6854f13a9477f782d18acae9f2134beb1b94562bb35bf4897e30186527cbe2b2',
    '37b674add17a90d66928f4acfa1d988242454088295979752e10474197d45424',
    '4ffc1dfec16412f3edde900391454c4f624ac06d04ee3722167fd4b1211a218c',
    'a6596fe78b36e7b30f23273011c1039f12ee50626165b571bc643b5afaa651e6',
    '802e1b56e291e46b4788ff998bf38970b622ff2029d01f413ea5e61eb024375b',
    '54deaf58c5b8fa47742e8cbf1b6ea371d3037c8eba386011281d63dbfb9f79e2',
    '568b751ff32e504166cb3b6bca6c68ccc7c29dcf7aacfeb164bc347be737fc73',
    '2401176f1cd5b6c5250e6cf07fdabd9ffc00a6bdec176d7be0d37b10c378f5db',
    '41584ed413c9987f6edb41b1681d69bd3d8f3daad96df5eeb533eeb8646aec3d',
    '074b1244d3e3a5adcd3b0ade7e6d86be8b92dc9938f376591e23e932e2691b06',
    '9e14658e407d5fa4334f1f38ba7f59c8fbdf4bd68b8e37d3fc407a068b63aeb5',
    'bb9aeb31af97934a162c99e166436c8ab645557f5be12a5a342e5cfc0bc98c87',
    '9bd588795b028af94d81241ecd94b542ee059492d8b7796aa065bf8e6deb1180',
    '5472f490acc238d6d8e4536ca2bac1c7e7f53582bfb100481b2bbd6c7153a5f3',
    '384cbd4b2b9490e7bdc904196d62e6b63429a722c229eab20a29f08210ca64cd',
    'af7ece7f0216a0f6fcbf259b79922d12b5ceacbcfb8e69b09e5259c5faa49bff',
    'dce2f5fda3d61511bc3ea679c94c04aacc671fb81bc9c0b2a0d2376b6e47594f',
    'd44636ed9cc66fef3cc50084f35690c9dac84fbd5eb43244c9c4d1b47631691d',
    'c61f897b0d088e25acc8ee0a1cd351678333d1e19eae2780421946aeebc6e185',
    '0f2225891cea24e49643cd47d938a60a527290ea4b4a99ecaf1c1412cb1f6554',
    'b285071884d1880a66ecd2ddc04d34e01b457ab831ce2eaba4d0bf92f5e2a5ec',
    'b707b02640ea1f96268e501a5ac37e339143bf3b51deb773f3c8bee2d92f6295',
    '9818ee62faebe5608dba2c355495f6a498d8cda1e13343f3afd5ef9dbbf93cb7',
]

@pytest.mark.parametrize('case', range(36))
def test_ai_decisions_match_independent_bytecode_expectations(monkeypatch, case):
    draws = Draws(case + 1)
    def runtime(seed):
        rt = Runtime(seed)
        get(rt.globals, 'Math').set('random', draws.random)
        return rt
    monkeypatch.setattr(engine, 'Runtime', runtime)
    game = engine.Game(0, case % 3)
    configure(game, case)
    game.rt.invoke(game.model, 'doTurn')
    rows = []
    for row in trace(game, case, draws):
        values = row.split('|')
        if values[1] == 'score':
            values[-1] = format(float(values[-1]), '.9f')
        rows.append('|'.join(values))
    digest = hashlib.sha256('\n'.join(sorted(rows)).encode()).hexdigest()
    assert digest == EXPECTED[case]
