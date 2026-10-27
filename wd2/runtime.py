"""AS2 value semantics for the generated Python sources.

This is not a Flash player. Display/audio integration is separate. Missing native
calls are recorded, so headless execution cannot be mistaken for visual parity.
"""
import functools
import math
import random
import time
import urllib.parse


class Undefined:
    def __repr__(self): return 'undefined'
    def __bool__(self): return False
U = Undefined()


def truth(v):
    if v is U or v is None: return False
    if isinstance(v, (bool, int, float, str)):
        return bool(v) and not (isinstance(v, float) and math.isnan(v))
    return True


def number(v=U):
    if v is U: return float('nan')
    if v is None: return 0
    if isinstance(v, (bool, int, float)): return int(v) if isinstance(v, bool) else v
    if isinstance(v, ASArray): v = string(v)
    if isinstance(v, str):
        try:
            s = v.strip()
            if not s: return 0
            return int(s, 16) if s.lower().startswith(('0x', '+0x', '-0x')) else float(s)
        except ValueError: return float('nan')
    return float('nan')


def string(v=U):
    if v is U: return 'undefined'
    if v is None: return 'null'
    if v is True: return 'true'
    if v is False: return 'false'
    if isinstance(v, ASArray): return ','.join('' if x is U or x is None else string(x) for x in v.items)
    if isinstance(v, float):
        if math.isnan(v): return 'NaN'
        if math.isinf(v): return '-Infinity' if v < 0 else 'Infinity'
        if v.is_integer(): return str(int(v))
    if isinstance(v, ASObject): return '[object Object]'
    return str(v)


def uint32(v):
    n = number(v)
    return 0 if not math.isfinite(n) else int(n) & 0xffffffff


def int32(v):
    v = uint32(v)
    return v - 0x100000000 if v >= 0x80000000 else v


def strict_eq(a, b):
    if a is U or b is U or a is None or b is None: return a is b
    if isinstance(a, bool) or isinstance(b, bool): return type(a) is type(b) and a == b
    if isinstance(a, (float,int)) and isinstance(b, (float,int)): return a == b
    if isinstance(a, str) and isinstance(b, str): return a == b
    return a is b


def eq(a, b):
    if (a is U or a is None) and (b is U or b is None): return True
    if a is U or a is None or b is U or b is None: return False
    if strict_eq(a,b): return True
    if isinstance(a, bool) or isinstance(b, bool): return number(a) == number(b)
    if isinstance(a, (int,float)) and isinstance(b,str) or isinstance(b,(int,float)) and isinstance(a,str): return number(a) == number(b)
    return False


def primitive(v): return string(v) if isinstance(v, ASObject) else v


def binop(op, a, b):
    if op == '===': return strict_eq(a,b)
    if op == '!==': return not strict_eq(a,b)
    if op == '==': return eq(a,b)
    if op == '!=': return not eq(a,b)
    if op == '+':
        a,b = primitive(a),primitive(b)
        return string(a)+string(b) if isinstance(a,str) or isinstance(b,str) else number(a)+number(b)
    if op == 'in': return ref(b,a).exists()
    if op == 'instanceof': return isinstance(a, ASObject) and isinstance(b, ASClass) and b in a.cls.lineage()
    if op in ('<','>','<=','>='):
        a,b = primitive(a),primitive(b)
        if not (isinstance(a,str) and isinstance(b,str)): a,b = number(a),number(b)
        return {'<':lambda:a<b, '>':lambda:a>b, '<=':lambda:a<=b, '>=':lambda:a>=b}[op]()
    if op == '&': return int32(a) & int32(b)
    if op == '|': return int32(a) | int32(b)
    if op == '^': return int32(a) ^ int32(b)
    if op == '<<': return int32(int32(a) << (uint32(b)&31))
    if op == '>>': return int32(a) >> (uint32(b)&31)
    if op == '>>>': return uint32(a) >> (uint32(b)&31)
    a,b = number(a),number(b)
    if op == '-': return a-b
    if op == '*': return a*b
    if op == '/':
        if b == 0: return float('nan') if a == 0 or math.isnan(a) else math.copysign(float('inf'), a*math.copysign(1,b))
        return a/b
    if op == '%':
        if b == 0 or math.isnan(a) or math.isnan(b) or math.isinf(a): return float('nan')
        return a if math.isinf(b) else math.fmod(a,b)
    raise NotImplementedError(op)


def unary(op,v):
    if op == '!': return not truth(v)
    if op == '-': return -number(v)
    if op == '+': return number(v)
    if op == '~': return ~int32(v)
    if op == 'void': return U
    if op == 'typeof':
        if v is U: return 'undefined'
        if isinstance(v, bool): return 'boolean'
        if isinstance(v, (int,float)): return 'number'
        if isinstance(v, str): return 'string'
        if isinstance(v, (ASFunction,ASClass)) or callable(v): return 'function'
        return 'object'
    raise NotImplementedError(op)


def logical(op,a,other): return (other() if truth(a) else a) if op=='&&' else (a if truth(a) else other())


class ASObject:
    def __init__(self, props=None, cls=None, rt=None):
        self.props = dict(props or {})
        self.cls, self.rt = cls, rt
    def get(self,key):
        key=string(key)
        if self.cls:
            getter = self.cls.lookup('getters',key)
            if getter is not U: return self.rt.call(getter,self,[])
        if key in self.props: return self.props[key]
        if self.cls:
            method = self.cls.lookup('methods',key)
            if method is not U: return method
            for c in self.cls.lineage():
                c.initialize_fields()
                if key in c.prototype.props: return c.prototype.props[key]
        if key == 'toString': return lambda *args: string(self)
        if key == 'hasOwnProperty': return lambda k=U: string(k) in self.props
        return U
    def set(self,key,value):
        key=string(key)
        if self.cls:
            setter=self.cls.lookup('setters',key)
            if setter is not U:
                self.rt.call(setter,self,[value]); return value
        self.props[key]=value
        return value
    def has(self,key):
        key=string(key)
        return key in self.props or bool(self.cls and (any(self.cls.lookup(t,key) is not U for t in ('methods','getters','setters')) or any(key in c.prototype.props for c in self.cls.lineage())))
    def delete(self,key): self.props.pop(string(key),None); return True
    def keys(self): return list(reversed(self.props))
    def __repr__(self): return f'<{self.cls.name if self.cls else "Object"} {list(self.props)[:8]}>'


class ASArray(ASObject):
    def __init__(self,items=()): super().__init__(); self.items=list(items)
    @staticmethod
    def index(key):
        s=string(key)
        if s.isdigit() and (s=='0' or not s.startswith('0')) and int(s)<0xffffffff: return int(s)
        return None
    def get(self,key):
        k=string(key); i=self.index(key)
        if i is not None: return self.items[i] if i<len(self.items) else U
        if k=='length': return len(self.items)
        methods={'push':self.push,'pop':self.pop,'shift':self.shift,'unshift':self.unshift,'splice':self.splice,'slice':self.slice,'concat':self.concat,'sortOn':self.sort_on,'sort':self.sort,'join':lambda sep=',':string(sep).join(string(x) if x is not U and x is not None else '' for x in self.items),'reverse':self.reverse}
        return methods[k] if k in methods else super().get(k)
    def set(self,key,value):
        i=self.index(key)
        if i is not None:
            if i>1000000: raise ValueError('Array index exceeds runtime limit')
            if i>=len(self.items): self.items.extend([U]*(i+1-len(self.items)))
            self.items[i]=value
        elif string(key)=='length':
            n=max(0,int(number(value)))
            if n>1000000: raise ValueError('Array length exceeds runtime limit')
            self.items[n:]=[]
            self.items.extend([U]*max(0,n-len(self.items)))
        else: super().set(key,value)
        return value
    def has(self,key):
        i=self.index(key)
        return i is not None and i<len(self.items) or string(key)=='length' or super().has(key)
    def delete(self,key):
        i=self.index(key)
        if i is not None and i<len(self.items): self.items[i]=U
        else: super().delete(key)
        return True
    def keys(self): return super().keys()+[str(i) for i in range(len(self.items)-1,-1,-1)]
    def push(self,*values): self.items.extend(values); return len(self.items)
    def pop(self): return self.items.pop() if self.items else U
    def shift(self): return self.items.pop(0) if self.items else U
    def unshift(self,*values): self.items[:0]=values; return len(self.items)
    def reverse(self): self.items.reverse(); return self
    def slice(self,start=0,end=U): return arr(self.items[int(number(start)):None if end is U else int(number(end))])
    def splice(self,start=0,count=U,*values):
        start=int(number(start)); start=max(len(self.items)+start,0) if start<0 else min(start,len(self.items))
        count=len(self.items)-start if count is U else max(0,int(number(count)))
        removed=self.items[start:start+count]; self.items[start:start+count]=values
        return arr(removed)
    def concat(self,*values):
        result=self.items.copy()
        for v in values: result.extend(v.items if isinstance(v,ASArray) else [v])
        return arr(result)
    def sort_on(self,field,flags=0):
        fields=field.items if isinstance(field,ASArray) else [field]
        options=flags.items if isinstance(flags,ASArray) else [flags]*len(fields)
        def compare(a,b):
            for k,f in zip(fields,options):
                f=int(number(f)); x,y=get(a,k),get(b,k)
                x,y=(number(x),number(y)) if f&16 else (string(x),string(y))
                if f&1 and isinstance(x,str): x,y=x.lower(),y.lower()
                n=(x>y)-(x<y)
                if n: return -n if f&2 else n
            return 0
        self.items.sort(key=functools.cmp_to_key(compare)); return self
    def sort(self,flags=0):
        flags=int(number(flags)); self.items.sort(key=number if flags&16 else string,reverse=bool(flags&2)); return self
    def __iter__(self): return iter(self.items)
    def __len__(self): return len(self.items)
    def __getitem__(self,index): return self.get(index)
    def __repr__(self): return repr(self.items)


def arr(items=()): return ASArray(items)
def obj(props=None): return ASObject(props)


def get(target,key):
    if isinstance(target,(ASObject,ASClass,NativeClass,SuperProxy)): return target.get(key)
    key=string(key)
    if isinstance(target,str):
        if key=='length': return len(target.encode('utf-16-le','surrogatepass'))//2
        def units(s):
            b=s.encode('utf-16-le','surrogatepass'); return [chr(int.from_bytes(b[i:i+2],'little')) for i in range(0,len(b),2)]
        chars=units(target)
        if key=='charAt': return lambda i=0: chars[int(number(i))] if 0<=int(number(i))<len(chars) else ''
        if key=='charCodeAt': return lambda i=0: ord(chars[int(number(i))]) if 0<=int(number(i))<len(chars) else float('nan')
        if key=='toUpperCase': return lambda:target.upper()
        if key=='toLowerCase': return lambda:target.lower()
        if key=='split': return lambda sep=U: arr([target] if sep is U else list(target) if sep=='' else target.split(string(sep)))
        if key=='slice': return lambda start=0,end=U:target[int(number(start)):None if end is U else int(number(end))]
        if key=='substr': return lambda start=0,count=U: target[max(len(target)+int(number(start)),0) if number(start)<0 else int(number(start)):][:None if count is U else max(0,int(number(count)))]
        if key=='substring': return lambda start=0,end=U:target[min(max(0,int(number(start))),len(target) if end is U else max(0,int(number(end)))):max(max(0,int(number(start))),len(target) if end is U else max(0,int(number(end))))]
        if key=='indexOf': return lambda sub,start=0:target.find(string(sub),max(0,int(number(start))))
        if key=='lastIndexOf': return lambda sub,start=U:target.rfind(string(sub),0,len(target) if start is U else int(number(start))+len(string(sub)))
    if key=='toString':
        def to_string(radix=10):
            if number(radix)==10: return string(target)
            n=int(number(target)); radix=int(number(radix)); digits='0123456789abcdefghijklmnopqrstuvwxyz'; s=''
            if not 2<=radix<=36: return string(target)
            sign='-' if n<0 else ''; n=abs(n)
            while n: s=digits[n%radix]+s; n//=radix
            return sign+(s or '0')
        return to_string
    return U


class Ref:
    def __init__(self,target,key): self.target,self.key=target,key
    def get(self): return get(self.target,self.key)
    def set(self,value):
        if isinstance(self.target,(ASObject,Scope)): return self.target.set(self.key,value)
        return value
    def exists(self): return isinstance(self.target,ASObject) and self.target.has(self.key)
    def delete(self): return self.target.delete(self.key) if isinstance(self.target,(ASObject,Scope)) else True


def ref(target,key): return Ref(target,key)
def keys(target): return target.keys() if isinstance(target,ASObject) else []
def assign(r,op,value):
    old=r.get() if op!='=' else U
    result=value()
    return r.set(result if op=='=' else binop(op[:-1],old,result))
def update(r,delta,prefix):
    old=number(r.get()); new=old+delta; r.set(new); return new if prefix else old


class ASBreak(Exception): pass
class ASContinue(Exception): pass
class ASException(Exception): pass


class ASFunction:
    def __init__(self,fn,closure=None): self.fn,self.closure=fn,closure
    def call(self,rt,this,args): return self.fn(rt,this,args,self.closure)


class ASClass:
    def __init__(self,rt,name,base,fields,methods,getters,setters):
        self.rt,self.name,self.base,self.fields,self.methods,self.getters,self.setters=rt,name,base,fields,methods,getters,setters
        self.prototype=obj(); self.initialized=False
    def initialize_fields(self):
        if not self.initialized:
            self.initialized=True
            self.fields(self.rt,self.prototype,[])
    def lineage(self):
        parent=self.rt.classes.get(self.base)
        return [self]+(parent.lineage() if parent else [])
    def lookup(self,kind,key):
        for c in self.lineage():
            if key in getattr(c,kind): return getattr(c,kind)[key]
        return U
    def get(self,key): return self.lookup('methods',string(key))
    def construct(self,args):
        for c in reversed(self.lineage()): c.initialize_fields()
        instance=ASObject(cls=self,rt=self.rt)
        ctor=self.methods.get(self.name)
        if ctor: self.rt.call(ctor,instance,args)
        return instance


class NativeClass:
    def __init__(self,fn,props=None): self.fn,self.props=fn,props or {}
    def get(self,key): return self.props.get(string(key),U)
    def construct(self,args): return self.fn(*args)


class SuperProxy:
    def __init__(self,scope): self.scope=scope
    def get(self,key):
        owner=self.scope.rt.classes.get(self.scope.owner)
        parent=self.scope.rt.classes.get(owner.base) if owner else None
        fn=parent.lookup('methods',string(key)) if parent else U
        return lambda *args:self.scope.rt.call(fn,self.scope.this,list(args))


class Scope:
    def __init__(self,rt,this,args,params,locals_,closure=None,owner=None):
        self.rt,self.this,self.closure,self.owner=rt,this,closure,owner
        self.values=dict.fromkeys(locals_,U)
        self.values.update({p:args[i] if i<len(args) else U for i,p in enumerate(params)})
        self.values['arguments']=arr(args)
    def get(self,name):
        if name=='__super__': return SuperProxy(self)
        if name in self.values: return self.values[name]
        if self.closure:
            scope=self.closure
            while scope:
                if name in scope.values: return scope.values[name]
                scope=scope.closure
        if isinstance(self.this,ASObject) and self.this.has(name): return self.this.get(name)
        return self.rt.globals.get(name)
    def set(self,name,value):
        if name in self.values: self.values[name]=value; return value
        if self.closure:
            scope=self.closure
            while scope:
                if name in scope.values: scope.values[name]=value; return value
                scope=scope.closure
        if isinstance(self.this,ASObject) and self.this.has(name): return self.this.set(name,value)
        return self.rt.globals.set(name,value)
    def delete(self,name):
        if name in self.values: return False
        return self.this.delete(name) if isinstance(self.this,ASObject) and self.this.has(name) else self.rt.globals.delete(name)
    def ref(self,name): return ScopeRef(self,name)
    def call(self,name,args):
        if name=='__super__':
            owner=self.rt.classes.get(self.owner)
            parent=self.rt.classes.get(owner.base) if owner else None
            return self.rt.call(parent.methods.get(parent.name,U),self.this,args) if parent else U
        target=self.this if isinstance(self.this,ASObject) and self.this.has(name) else self.rt.globals
        return self.rt.call(self.get(name),target,args)


class ScopeRef(Ref):
    def get(self): return self.target.get(self.key)


class Runtime:
    def __init__(self,seed=0):
        self.rng=random.Random(seed)
        self.classes={}; self.scripts={}; self.globals=obj(); self.missing_calls={}; self.external_requests=[]
        self.iterations=0; self.iteration_limit=2000000
        self.globals.set('_global',self.globals)
        self.root=obj(); self.globals.set('_root',self.root); self.globals.set('_level0',self.root)
        def array_constructor(*args):
            return arr([U]*int(args[0])) if len(args)==1 and isinstance(args[0],(int,float)) and not isinstance(args[0],bool) else arr(args)
        def parse_int(s,base=0):
            import re
            s=string(s).lstrip(); base=int(number(base))
            if base==0: base=16 if s.lstrip('+-').lower().startswith('0x') else 10
            sign=-1 if s.startswith('-') else 1; s=s.lstrip('+-')
            if base==16 and s.lower().startswith('0x'): s=s[2:]
            chars='0123456789abcdefghijklmnopqrstuvwxyz'[:base]; match=re.match('['+chars+']+',s.lower())
            return sign*int(match[0],base) if match else float('nan')
        def safe_math(fn):
            def call(*args):
                try: return fn(*(number(a) for a in args))
                except (ValueError,OverflowError): return float('nan')
            return call
        math_obj=obj({n:safe_math(getattr(math,n)) for n in ('floor','ceil','sqrt','sin','cos','atan2','tan','pow','abs') if hasattr(math,n)})
        math_obj.props.update({'random':self.rng.random,'round':safe_math(lambda x:math.floor(x+0.5)),'abs':lambda x:abs(number(x)),'min':lambda *x:min(map(number,x),default=float('inf')),'max':lambda *x:max(map(number,x),default=-float('inf')),'PI':math.pi})
        builtins={'undefined':U,'NaN':float('nan'),'Infinity':float('inf'),'Math':math_obj,
                  'Array':NativeClass(array_constructor,{'DESCENDING':2,'NUMERIC':16,'CASEINSENSITIVE':1,'UNIQUESORT':4,'RETURNINDEXEDARRAY':8}),
                  'Object':NativeClass(lambda value=U:value if isinstance(value,ASObject) else obj()),
                  'Number':NativeClass(number),'String':NativeClass(string,{'fromCharCode':lambda *values:''.join(chr(uint32(x)&0xffff) for x in values)}),'Boolean':NativeClass(truth),
                  'parseInt':parse_int,'isNaN':lambda v=U:math.isnan(number(v)),'int':lambda v=0:int32(v),'random':lambda n:self.rng.randrange(max(1,int(number(n)))),
                  'unescape':lambda s:urllib.parse.unquote(string(s)),'escape':lambda s:urllib.parse.quote(string(s)),
                  'trace':lambda *args:U,'fscommand':lambda *args:U,'getTimer':lambda:int(time.monotonic()*1000),
                  'getURL':lambda *args:self.external_requests.append(args),'stopAllSounds':lambda:U}
        self.globals.props.update(builtins)
        self.globals.set('System',obj({'security':obj({'allowDomain':lambda *args:U})}))
    def define(self,name,base,fields,methods,getters,setters):
        cls=ASClass(self,name,base,fields,methods,getters,setters)
        self.classes[name]=cls; self.globals.set(name,cls)
    def construct(self,cls,args):
        if isinstance(cls,(ASClass,NativeClass)): return cls.construct(args)
        raise TypeError(f'Cannot construct {cls!r}')
    def new(self,name,*args): return self.construct(self.globals.get(name),list(args))
    def call(self,fn,this,args):
        if isinstance(fn,ASFunction): return fn.call(self,this,args)
        if isinstance(fn,NativeClass): return fn.construct(args)
        if callable(fn): return fn(*args)
        if fn is U or fn is None:
            self.missing_calls['undefined function']=self.missing_calls.get('undefined function',0)+1
            return U
        raise TypeError(f'Not callable: {fn!r}')
    def call_ref(self,r,args):
        fn=r.get()
        if fn is U:
            key=string(r.key); self.missing_calls[key]=self.missing_calls.get(key,0)+1
            return U
        return self.call(fn,r.target,args)
    def invoke(self,target,name,*args): return self.call_ref(ref(target,name),list(args))
    def tick(self):
        self.iterations+=1
        if self.iterations>self.iteration_limit: raise RuntimeError('AS2 iteration budget exceeded; possible missing host behavior')
    def reset_budget(self): self.iterations=0
