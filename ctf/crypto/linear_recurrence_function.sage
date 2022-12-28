#https://blog.csdn.net/ZXW_NUDT/article/details/126582089
#https://www.nullhardware.com/reference/hacking-101/picoctf-2022-greatest-hits/sequences/, easywork, wangdingcup-2022bh
#https://ctftime.org/writeup/32913

import gmpy2
from functools import reduce

arr = [150532854791355748039117763516755705063,
335246949167877025932432065299887980427,
186623163520020374273300614035532913241,
215621842477244010690624570814660992556,
220694532805562822940506614120520015819,
17868778653481346517880312348382129728,
160572327041397126918110376968541265339
]

def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment

def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * gmpy2.invert(states[1] - states[0], modulus) % modulus
    return crack_unknown_increment(states, modulus, multiplier)

def crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(gmpy2.gcd, zeroes))
    return crack_unknown_multiplier(states, modulus)

(n, a, b) = crack_unknown_modulus(arr)
print (n, a, b)
c = 114514
e = int(2e8)
mod=10 ** 10000

M=matrix(Zmod(mod),[[c, 0, 0],[a, b, n],[0,0,1]])
C=matrix(Zmod(mod),[[c],[1],[1]])
s=(M^e)*C
sol = str(s[1]).strip('()')

import hashlib
sol_md5 = hashlib.md5(sol.encode()).hexdigest()

from Crypto.Util.strxor import *
flag = b'UUV\x04H\x01T\x01P\x03\t\x04\t\x1fW\x00T\x02LRSPT\x1d\x02\x02^\x01N[\\R\x02\tSV\x07\x06P\x01QK'
print(strxor((2*sol_md5.encode())[:len(flag)],flag))

'''
from sympy import *
M=Matrix([[c, 0, 0],[a, b, n],[0,0,1]])
P,D = M.diagonalize()
Pi=P**-1
print(f"M = {M}\nP*D*P^-1 = {P*D*Pi}\n")
L=Matrix([[0, 1, 0]])*P # pre-multiply by [0,1,0]
R=Pi*Matrix([[c],[1],[1]]) #post-multiply by [c;1;1]
f=1/gcd(tuple(R)) # pull out the gcd
R=f*R
print(f"f(i) = {L} * {D}**i * {R} // {f}")
i=symbols("i")
print(f"f(i) = ({(L*D**i*R)[0]}) // {f}")

from gmpy2 import mpz

m_func = lambda i: (-3615776451043895909488663421812446413391085884025996921937787909467945292584005296*mpz(114514)**int(i) + 3615832628247399739065778439780322260147935253937774030993191987478412908418812461*mpz(121870392737324465817476070178603827899)**int(i) - 41324810877879869210637781736248415910104434256002149754789105770257575792435) // 14852392625949707904380186139598340939265477521106905649288904697358259014730

def str_xor(s: str, k: str):
    k = (k * (len(s) // len(k) + 1))[0:len(s)]
    return ''.join(chr(a ^ b) for a, b in zip(s, k))

import hashlib
flag = b'UUV\x04H\x01T\x01P\x03\t\x04\t\x1fW\x00T\x02LRSPT\x1d\x02\x02^\x01N[\\R\x02\tSV\x07\x06P\x01QK'
def encrypt_flag(sol):
    sol = sol % (10**10000)
    sol = str(sol)
#    print(sol)
    sol_md5 = hashlib.md5(sol.encode()).hexdigest()
    return  str_xor(flag, sol_md5.encode())

sol = (m_func(e))
print(encrypt_flag(sol))
'''