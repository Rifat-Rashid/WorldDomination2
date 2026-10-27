import hashlib
import math
import random
import pytest

from wd2.runtime import *
from wd2.generated import register_all


@pytest.fixture
def rt():
    runtime=Runtime(0); register_all(runtime); return runtime


def test_as2_truthiness_and_equality():
    assert not truth(U) and not truth(None) and not truth(float('nan'))
    assert truth(arr()) and truth(obj()) and truth('0')
    assert eq(U,None) and eq('10',10) and eq(False,0)
    assert not eq(False,None) and not eq(0,U) and not strict_eq(True,1)
    assert not strict_eq(float('nan'),float('nan'))


def test_number_and_string_operations():
    assert binop('+','city',4)=='city4'
    assert binop('+',4,5)==9
    assert binop('/',1,0)==float('inf')
    assert math.isnan(binop('/',0,0))
    assert binop('%',-5,3)==-2
    assert binop('>>>',-1,0)==4294967295
    assert binop('<<',0x7fffffff,1)==-2
    assert number('0xff')==255
    assert get('hello','charAt')(9)==''
    assert get('abc','charCodeAt')(1)==98


def test_assignment_evaluation_and_short_circuit():
    target=obj({'v':2}); events=[]
    assert assign(ref(target,'v'),'+=',lambda:events.append(1) or 3)==5
    assert events==[1] and get(target,'v')==5
    assert update(ref(target,'v'),1,False)==5 and get(target,'v')==6
    assert logical('&&',False,lambda:1/0) is False
    assert logical('||','x',lambda:1/0)=='x'


def test_arrays_and_sort_on():
    a=arr([3,1]); assert a.get(5) is U
    a.set(3,9); assert a.items==[3,1,U,9]
    assert a.splice(1,2,7).items==[1,U] and a.items==[3,7,9]
    assert keys(a)==['2','1','0']
    data=arr([obj({'n':2}),obj({'n':10}),obj({'n':1})])
    data.sort_on('n',18); assert [get(v,'n') for v in data]==[10,2,1]


@pytest.mark.parametrize('message',['','a','abc','message digest','abcdefghijklmnopqrstuvwxyz','World Domination 2','x'*1000])
def test_recovered_md5_against_standard_library(rt,message):
    md5=rt.new('MD5_class')
    assert rt.invoke(md5,'hex_md5',message)==hashlib.md5(message.encode('ascii')).hexdigest()


def test_getters_setters_and_inheritance(rt):
    p=rt.new('Player','human',0,arr([0,0])); p.set('religion',37)
    assert get(p,'religion')==37 and get(p,'religionLevel')==37
    p.set('cityArr',arr([rt.new('City',0,45,p),rt.new('City',1,80,p)]))
    assert get(p,'population')==125
    assert get(rt.invoke(p,'largest_city'),'cityID')==1
    m=rt.new('Model'); assert get(m,'difficulty_level')==1
    assert get(m,'MD5').cls.name=='MD5_class'
    assert rt.invoke(m,'get_religion_name_by_code','chr')=='Christian'


def test_prototype_defaults_match_original_pcode(rt):
    a,b=rt.new('Sub_model'),rt.new('Sub_model')
    # JPEXS p-code sets these defaults on the prototype, outside constructors.
    assert get(a,'cityPositions') is get(b,'cityPositions')
    a.set('difficulty_level',2); assert get(b,'difficulty_level')==1


def test_catalog_recovered_values(rt):
    stock=rt.new('WeaponStock')
    assert len(get(stock,'weaponArr'))==26 and len(get(stock,'counterArr'))==2
    soldier=rt.invoke(stock,'getWeaponByName','soldier1')
    assert get(soldier,'cost')==5 and get(soldier,'maxKills')==4
    warhead=rt.invoke(stock,'getWeaponByName','warhead4')
    assert get(warhead,'cost')==20 and get(warhead,'maxKills')==150
    assert len(get(rt.new('TechTree'),'techArr'))==28
