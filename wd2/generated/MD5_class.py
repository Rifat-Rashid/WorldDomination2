# Generated from __Packages/MD5_class.as; edit tools/transpile.py to regenerate.
from wd2.runtime import *

def MD5_class_MD5_class(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'MD5_class')
    return U

def MD5_class_hex_md5(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['s'], ['s'], closure, 'MD5_class')
    return rt.call_ref(ref(this, 'binl2hex'), [rt.call_ref(ref(this, 'core_md5'), [rt.call_ref(ref(this, 'str2binl'), [e.get('s')]), binop('*', ref(e.get('s'), 'length').get(), ref(this, 'chrsz').get())])])
    return U

def MD5_class_b64_md5(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['s'], ['s'], closure, 'MD5_class')
    return rt.call_ref(ref(this, 'binl2b64'), [rt.call_ref(ref(this, 'core_md5'), [rt.call_ref(ref(this, 'str2binl'), [e.get('s')]), binop('*', ref(e.get('s'), 'length').get(), ref(this, 'chrsz').get())])])
    return U

def MD5_class_str_md5(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['s'], ['s'], closure, 'MD5_class')
    return rt.call_ref(ref(this, 'binl2str'), [rt.call_ref(ref(this, 'core_md5'), [rt.call_ref(ref(this, 'str2binl'), [e.get('s')]), binop('*', ref(e.get('s'), 'length').get(), ref(this, 'chrsz').get())])])
    return U

def MD5_class_hex_hmac_md5(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['key', 'data'], ['data', 'key'], closure, 'MD5_class')
    return rt.call_ref(ref(this, 'binl2hex'), [rt.call_ref(ref(this, 'core_hmac_md5'), [e.get('key'), e.get('data')])])
    return U

def MD5_class_b64_hmac_md5(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['key', 'data'], ['data', 'key'], closure, 'MD5_class')
    return rt.call_ref(ref(this, 'binl2b64'), [rt.call_ref(ref(this, 'core_hmac_md5'), [e.get('key'), e.get('data')])])
    return U

def MD5_class_str_hmac_md5(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['key', 'data'], ['data', 'key'], closure, 'MD5_class')
    return rt.call_ref(ref(this, 'binl2str'), [rt.call_ref(ref(this, 'core_hmac_md5'), [e.get('key'), e.get('data')])])
    return U

def MD5_class_md5_vm_test(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'MD5_class')
    return binop('==', rt.call_ref(ref(this, 'hex_md5'), ['abc']), '900150983cd24fb0d6963f7d28e17f72')
    return U

def MD5_class_core_md5(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['x', 'len'], ['_loc10_', '_loc11_', '_loc12_', '_loc13_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', '_loc9_', 'len', 'x'], closure, 'MD5_class')
    assign(ref(e.get('x'), binop('>>', e.get('len'), 5)), '|=', lambda: binop('<<', 128, binop('%', e.get('len'), 32)))
    assign(ref(e.get('x'), binop('+', binop('<<', binop('>>>', binop('+', e.get('len'), 64), 9), 4), 14)), '=', lambda: e.get('len'))
    e.set('_loc4_', 1732584193)
    e.set('_loc5_', unary('-', 271733879))
    e.set('_loc6_', unary('-', 1732584194))
    e.set('_loc7_', 271733878)
    e.set('_loc8_', 0)
    while truth(binop('<', e.get('_loc8_'), ref(e.get('x'), 'length').get())):
        rt.tick()
        try:
            assign(e.ref('_loc9_'), '=', lambda: e.get('_loc4_'))
            assign(e.ref('_loc10_'), '=', lambda: e.get('_loc5_'))
            assign(e.ref('_loc11_'), '=', lambda: e.get('_loc6_'))
            assign(e.ref('_loc12_'), '=', lambda: e.get('_loc7_'))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'md5_ff'), [e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 0)).get(), 7, unary('-', 680876936)]))
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(this, 'md5_ff'), [e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 1)).get(), 12, unary('-', 389564586)]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(this, 'md5_ff'), [e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 2)).get(), 17, 606105819]))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(this, 'md5_ff'), [e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 3)).get(), 22, unary('-', 1044525330)]))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'md5_ff'), [e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 4)).get(), 7, unary('-', 176418897)]))
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(this, 'md5_ff'), [e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 5)).get(), 12, 1200080426]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(this, 'md5_ff'), [e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 6)).get(), 17, unary('-', 1473231341)]))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(this, 'md5_ff'), [e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 7)).get(), 22, unary('-', 45705983)]))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'md5_ff'), [e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 8)).get(), 7, 1770035416]))
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(this, 'md5_ff'), [e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 9)).get(), 12, unary('-', 1958414417)]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(this, 'md5_ff'), [e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 10)).get(), 17, unary('-', 42063)]))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(this, 'md5_ff'), [e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 11)).get(), 22, unary('-', 1990404162)]))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'md5_ff'), [e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 12)).get(), 7, 1804603682]))
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(this, 'md5_ff'), [e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 13)).get(), 12, unary('-', 40341101)]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(this, 'md5_ff'), [e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 14)).get(), 17, unary('-', 1502002290)]))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(this, 'md5_ff'), [e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 15)).get(), 22, 1236535329]))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'md5_gg'), [e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 1)).get(), 5, unary('-', 165796510)]))
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(this, 'md5_gg'), [e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 6)).get(), 9, unary('-', 1069501632)]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(this, 'md5_gg'), [e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 11)).get(), 14, 643717713]))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(this, 'md5_gg'), [e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 0)).get(), 20, unary('-', 373897302)]))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'md5_gg'), [e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 5)).get(), 5, unary('-', 701558691)]))
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(this, 'md5_gg'), [e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 10)).get(), 9, 38016083]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(this, 'md5_gg'), [e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 15)).get(), 14, unary('-', 660478335)]))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(this, 'md5_gg'), [e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 4)).get(), 20, unary('-', 405537848)]))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'md5_gg'), [e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 9)).get(), 5, 568446438]))
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(this, 'md5_gg'), [e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 14)).get(), 9, unary('-', 1019803690)]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(this, 'md5_gg'), [e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 3)).get(), 14, unary('-', 187363961)]))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(this, 'md5_gg'), [e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 8)).get(), 20, 1163531501]))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'md5_gg'), [e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 13)).get(), 5, unary('-', 1444681467)]))
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(this, 'md5_gg'), [e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 2)).get(), 9, unary('-', 51403784)]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(this, 'md5_gg'), [e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 7)).get(), 14, 1735328473]))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(this, 'md5_gg'), [e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 12)).get(), 20, unary('-', 1926607734)]))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'md5_hh'), [e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 5)).get(), 4, unary('-', 378558)]))
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(this, 'md5_hh'), [e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 8)).get(), 11, unary('-', 2022574463)]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(this, 'md5_hh'), [e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 11)).get(), 16, 1839030562]))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(this, 'md5_hh'), [e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 14)).get(), 23, unary('-', 35309556)]))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'md5_hh'), [e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 1)).get(), 4, unary('-', 1530992060)]))
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(this, 'md5_hh'), [e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 4)).get(), 11, 1272893353]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(this, 'md5_hh'), [e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 7)).get(), 16, unary('-', 155497632)]))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(this, 'md5_hh'), [e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 10)).get(), 23, unary('-', 1094730640)]))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'md5_hh'), [e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 13)).get(), 4, 681279174]))
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(this, 'md5_hh'), [e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 0)).get(), 11, unary('-', 358537222)]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(this, 'md5_hh'), [e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 3)).get(), 16, unary('-', 722521979)]))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(this, 'md5_hh'), [e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 6)).get(), 23, 76029189]))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'md5_hh'), [e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 9)).get(), 4, unary('-', 640364487)]))
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(this, 'md5_hh'), [e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 12)).get(), 11, unary('-', 421815835)]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(this, 'md5_hh'), [e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 15)).get(), 16, 530742520]))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(this, 'md5_hh'), [e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 2)).get(), 23, unary('-', 995338651)]))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'md5_ii'), [e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 0)).get(), 6, unary('-', 198630844)]))
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(this, 'md5_ii'), [e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 7)).get(), 10, 1126891415]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(this, 'md5_ii'), [e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 14)).get(), 15, unary('-', 1416354905)]))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(this, 'md5_ii'), [e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 5)).get(), 21, unary('-', 57434055)]))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'md5_ii'), [e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 12)).get(), 6, 1700485571]))
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(this, 'md5_ii'), [e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 3)).get(), 10, unary('-', 1894986606)]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(this, 'md5_ii'), [e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 10)).get(), 15, unary('-', 1051523)]))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(this, 'md5_ii'), [e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 1)).get(), 21, unary('-', 2054922799)]))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'md5_ii'), [e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 8)).get(), 6, 1873313359]))
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(this, 'md5_ii'), [e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 15)).get(), 10, unary('-', 30611744)]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(this, 'md5_ii'), [e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 6)).get(), 15, unary('-', 1560198380)]))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(this, 'md5_ii'), [e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 13)).get(), 21, 1309151649]))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'md5_ii'), [e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 4)).get(), 6, unary('-', 145523070)]))
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(this, 'md5_ii'), [e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 11)).get(), 10, unary('-', 1120210379)]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(this, 'md5_ii'), [e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), e.get('_loc5_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 2)).get(), 15, 718787259]))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(this, 'md5_ii'), [e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_'), e.get('_loc4_'), ref(e.get('x'), binop('+', e.get('_loc8_'), 9)).get(), 21, unary('-', 343485551)]))
            assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'safe_add'), [e.get('_loc4_'), e.get('_loc9_')]))
            assign(e.ref('_loc5_'), '=', lambda: rt.call_ref(ref(this, 'safe_add'), [e.get('_loc5_'), e.get('_loc10_')]))
            assign(e.ref('_loc6_'), '=', lambda: rt.call_ref(ref(this, 'safe_add'), [e.get('_loc6_'), e.get('_loc11_')]))
            assign(e.ref('_loc7_'), '=', lambda: rt.call_ref(ref(this, 'safe_add'), [e.get('_loc7_'), e.get('_loc12_')]))
            assign(e.ref('_loc8_'), '+=', lambda: 16)
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc13_', rt.construct(e.get('Array'), [e.get('_loc4_'), e.get('_loc5_'), e.get('_loc6_'), e.get('_loc7_')]))
    return e.get('_loc13_')
    return U

def MD5_class_md5_cmn(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['q', 'a', 'b', 'x', 's', 't'], ['a', 'b', 'q', 's', 't', 'x'], closure, 'MD5_class')
    return rt.call_ref(ref(this, 'safe_add'), [rt.call_ref(ref(this, 'bit_rol'), [rt.call_ref(ref(this, 'safe_add'), [rt.call_ref(ref(this, 'safe_add'), [e.get('a'), e.get('q')]), rt.call_ref(ref(this, 'safe_add'), [e.get('x'), e.get('t')])]), e.get('s')]), e.get('b')])
    return U

def MD5_class_md5_ff(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a', 'b', 'c', 'd', 'x', 's', 't'], ['a', 'b', 'c', 'd', 's', 't', 'x'], closure, 'MD5_class')
    return rt.call_ref(ref(this, 'md5_cmn'), [binop('|', binop('&', e.get('b'), e.get('c')), binop('&', binop('^', e.get('b'), unary('-', 1)), e.get('d'))), e.get('a'), e.get('b'), e.get('x'), e.get('s'), e.get('t')])
    return U

def MD5_class_md5_gg(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a', 'b', 'c', 'd', 'x', 's', 't'], ['a', 'b', 'c', 'd', 's', 't', 'x'], closure, 'MD5_class')
    return rt.call_ref(ref(this, 'md5_cmn'), [binop('|', binop('&', e.get('b'), e.get('d')), binop('&', e.get('c'), binop('^', e.get('d'), unary('-', 1)))), e.get('a'), e.get('b'), e.get('x'), e.get('s'), e.get('t')])
    return U

def MD5_class_md5_hh(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a', 'b', 'c', 'd', 'x', 's', 't'], ['a', 'b', 'c', 'd', 's', 't', 'x'], closure, 'MD5_class')
    return rt.call_ref(ref(this, 'md5_cmn'), [binop('^', binop('^', e.get('b'), e.get('c')), e.get('d')), e.get('a'), e.get('b'), e.get('x'), e.get('s'), e.get('t')])
    return U

def MD5_class_md5_ii(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['a', 'b', 'c', 'd', 'x', 's', 't'], ['a', 'b', 'c', 'd', 's', 't', 'x'], closure, 'MD5_class')
    return rt.call_ref(ref(this, 'md5_cmn'), [binop('^', e.get('c'), binop('|', e.get('b'), binop('^', e.get('d'), unary('-', 1)))), e.get('a'), e.get('b'), e.get('x'), e.get('s'), e.get('t')])
    return U

def MD5_class_core_hmac_md5(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['key', 'data'], ['_loc4_', '_loc5_', '_loc6_', '_loc7_', '_loc8_', 'data', 'key'], closure, 'MD5_class')
    e.set('_loc4_', rt.call_ref(ref(this, 'str2binl'), [e.get('key')]))
    if truth(binop('>', ref(e.get('_loc4_'), 'length').get(), 16)):
        assign(e.ref('_loc4_'), '=', lambda: rt.call_ref(ref(this, 'core_md5'), [e.get('_loc4_'), binop('*', ref(e.get('key'), 'length').get(), ref(this, 'chrsz').get())]))
    e.set('_loc5_', e.call('Array', [16]))
    e.set('_loc6_', e.call('Array', [16]))
    e.set('_loc7_', 0)
    while truth(binop('<', e.get('_loc7_'), 16)):
        rt.tick()
        try:
            assign(ref(e.get('_loc5_'), e.get('_loc7_')), '=', lambda: binop('^', ref(e.get('_loc4_'), e.get('_loc7_')).get(), 909522486))
            assign(ref(e.get('_loc6_'), e.get('_loc7_')), '=', lambda: binop('^', ref(e.get('_loc4_'), e.get('_loc7_')).get(), 1549556828))
            assign(e.ref('_loc7_'), '=', lambda: binop('+', e.get('_loc7_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    e.set('_loc8_', rt.call_ref(ref(this, 'core_md5'), [rt.call_ref(ref(e.get('_loc5_'), 'concat'), [rt.call_ref(ref(this, 'str2binl'), [e.get('data')])]), binop('+', 512, binop('*', ref(e.get('data'), 'length').get(), ref(this, 'chrsz').get()))]))
    return rt.call_ref(ref(this, 'core_md5'), [rt.call_ref(ref(e.get('_loc6_'), 'concat'), [e.get('_loc8_')]), binop('+', 512, 128)])
    return U

def MD5_class_safe_add(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['x', 'y'], ['_loc4_', '_loc5_', 'x', 'y'], closure, 'MD5_class')
    e.set('_loc4_', binop('+', binop('&', e.get('x'), 65535), binop('&', e.get('y'), 65535)))
    e.set('_loc5_', binop('+', binop('+', binop('>>', e.get('x'), 16), binop('>>', e.get('y'), 16)), binop('>>', e.get('_loc4_'), 16)))
    return binop('|', binop('<<', e.get('_loc5_'), 16), binop('&', e.get('_loc4_'), 65535))
    return U

def MD5_class_bit_rol(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['num', 'cnt'], ['cnt', 'num'], closure, 'MD5_class')
    return binop('|', binop('<<', e.get('num'), e.get('cnt')), binop('>>>', e.get('num'), binop('-', 32, e.get('cnt'))))
    return U

def MD5_class_str2binl(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['str'], ['_loc3_', '_loc4_', '_loc5_', 'str'], closure, 'MD5_class')
    e.set('_loc3_', rt.construct(e.get('Array'), []))
    e.set('_loc4_', binop('-', binop('<<', 1, ref(this, 'chrsz').get()), 1))
    e.set('_loc5_', 0)
    while truth(binop('<', e.get('_loc5_'), binop('*', ref(e.get('str'), 'length').get(), ref(this, 'chrsz').get()))):
        rt.tick()
        try:
            assign(ref(e.get('_loc3_'), binop('>>', e.get('_loc5_'), 5)), '|=', lambda: binop('<<', binop('&', rt.call_ref(ref(e.get('str'), 'charCodeAt'), [binop('/', e.get('_loc5_'), ref(this, 'chrsz').get())]), e.get('_loc4_')), binop('%', e.get('_loc5_'), 32)))
            assign(e.ref('_loc5_'), '+=', lambda: ref(this, 'chrsz').get())
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc3_')
    return U

def MD5_class_binl2str(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['bin'], ['_loc3_', '_loc4_', '_loc5_', 'bin'], closure, 'MD5_class')
    e.set('_loc3_', '')
    e.set('_loc4_', binop('-', binop('<<', 1, ref(this, 'chrsz').get()), 1))
    e.set('_loc5_', 0)
    while truth(binop('<', e.get('_loc5_'), binop('*', ref(e.get('bin'), 'length').get(), 32))):
        rt.tick()
        try:
            assign(e.ref('_loc3_'), '+=', lambda: rt.call_ref(ref(e.get('String'), 'fromCharCode'), [binop('&', binop('>>>', ref(e.get('bin'), binop('>>', e.get('_loc5_'), 5)).get(), binop('%', e.get('_loc5_'), 32)), e.get('_loc4_'))]))
            assign(e.ref('_loc5_'), '+=', lambda: ref(this, 'chrsz').get())
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc3_')
    return U

def MD5_class_binl2hex(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['binarray'], ['_loc3_', '_loc4_', '_loc5_', 'binarray'], closure, 'MD5_class')
    e.set('_loc3_', ('0123456789abcdef' if truth(unary('!', ref(this, 'hexcase').get())) else '0123456789ABCDEF'))
    e.set('_loc4_', '')
    e.set('_loc5_', 0)
    while truth(binop('<', e.get('_loc5_'), binop('*', ref(e.get('binarray'), 'length').get(), 4))):
        rt.tick()
        try:
            assign(e.ref('_loc4_'), '+=', lambda: binop('+', rt.call_ref(ref(e.get('_loc3_'), 'charAt'), [binop('&', binop('>>', ref(e.get('binarray'), binop('>>', e.get('_loc5_'), 2)).get(), binop('+', binop('*', binop('%', e.get('_loc5_'), 4), 8), 4)), 15)]), rt.call_ref(ref(e.get('_loc3_'), 'charAt'), [binop('&', binop('>>', ref(e.get('binarray'), binop('>>', e.get('_loc5_'), 2)).get(), binop('*', binop('%', e.get('_loc5_'), 4), 8)), 15)])))
            assign(e.ref('_loc5_'), '=', lambda: binop('+', e.get('_loc5_'), 1))
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc4_')
    return U

def MD5_class_binl2b64(rt, this, args, closure=None):
    e = Scope(rt, this, args, ['binarray'], ['_loc3_', '_loc4_', '_loc5_', '_loc6_', '_loc7_', 'binarray'], closure, 'MD5_class')
    e.set('_loc3_', 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')
    e.set('_loc4_', '')
    e.set('_loc5_', 0)
    while truth(binop('<', e.get('_loc5_'), binop('*', ref(e.get('binarray'), 'length').get(), 4))):
        rt.tick()
        try:
            assign(e.ref('_loc6_'), '=', lambda: binop('|', binop('|', binop('<<', binop('&', binop('>>', ref(e.get('binarray'), binop('>>', e.get('_loc5_'), 2)).get(), binop('*', 8, binop('%', e.get('_loc5_'), 4))), 255), 16), binop('<<', binop('&', binop('>>', ref(e.get('binarray'), binop('>>', binop('+', e.get('_loc5_'), 1), 2)).get(), binop('*', 8, binop('%', binop('+', e.get('_loc5_'), 1), 4))), 255), 8)), binop('&', binop('>>', ref(e.get('binarray'), binop('>>', binop('+', e.get('_loc5_'), 2), 2)).get(), binop('*', 8, binop('%', binop('+', e.get('_loc5_'), 2), 4))), 255)))
            assign(e.ref('_loc7_'), '=', lambda: 0)
            while truth(binop('<', e.get('_loc7_'), 4)):
                rt.tick()
                try:
                    if truth(binop('>', binop('+', binop('*', e.get('_loc5_'), 8), binop('*', e.get('_loc7_'), 6)), binop('*', ref(e.get('binarray'), 'length').get(), 32))):
                        assign(e.ref('_loc4_'), '+=', lambda: ref(this, 'b64pad').get())
                    else:
                        assign(e.ref('_loc4_'), '+=', lambda: rt.call_ref(ref(e.get('_loc3_'), 'charAt'), [binop('&', binop('>>', e.get('_loc6_'), binop('*', 6, binop('-', 3, e.get('_loc7_')))), 63)]))
                    assign(e.ref('_loc7_'), '=', lambda: binop('+', e.get('_loc7_'), 1))
                except ASContinue:
                    pass
                except ASBreak:
                    break
            assign(e.ref('_loc5_'), '+=', lambda: 3)
        except ASContinue:
            pass
        except ASBreak:
            break
    return e.get('_loc4_')
    return U

def MD5_class_fields(rt, this, args, closure=None):
    e = Scope(rt, this, args, [], [], closure, 'MD5_class')
    ref(this, 'hexcase').set(0)
    ref(this, 'b64pad').set('')
    ref(this, 'chrsz').set(8)

def register(rt):
    rt.define('MD5_class', None, MD5_class_fields, {'MD5_class': ASFunction(MD5_class_MD5_class), 'hex_md5': ASFunction(MD5_class_hex_md5), 'b64_md5': ASFunction(MD5_class_b64_md5), 'str_md5': ASFunction(MD5_class_str_md5), 'hex_hmac_md5': ASFunction(MD5_class_hex_hmac_md5), 'b64_hmac_md5': ASFunction(MD5_class_b64_hmac_md5), 'str_hmac_md5': ASFunction(MD5_class_str_hmac_md5), 'md5_vm_test': ASFunction(MD5_class_md5_vm_test), 'core_md5': ASFunction(MD5_class_core_md5), 'md5_cmn': ASFunction(MD5_class_md5_cmn), 'md5_ff': ASFunction(MD5_class_md5_ff), 'md5_gg': ASFunction(MD5_class_md5_gg), 'md5_hh': ASFunction(MD5_class_md5_hh), 'md5_ii': ASFunction(MD5_class_md5_ii), 'core_hmac_md5': ASFunction(MD5_class_core_hmac_md5), 'safe_add': ASFunction(MD5_class_safe_add), 'bit_rol': ASFunction(MD5_class_bit_rol), 'str2binl': ASFunction(MD5_class_str2binl), 'binl2str': ASFunction(MD5_class_binl2str), 'binl2hex': ASFunction(MD5_class_binl2hex), 'binl2b64': ASFunction(MD5_class_binl2b64)}, {}, {})
