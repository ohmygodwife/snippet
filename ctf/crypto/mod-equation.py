#guess_game, wdb-2020-3rd, https://y-y-k.tk/2020/05/18, http://igml.top/2020/05/18/2020
import gmpy2
import re

#a*x_n + c = x_n+1 % b
def inc_func(s, mod, mul):
  inc = (s[1] - s[0]*mul) % mod
  return mul, mod, inc

def mul_func(s, mod):
  mul = (s[2] - s[1]) * gmpy2.invert(s[1] - s[0], mod) % mod
  return inc_func(s, mod, mul)

def mod_func(s):
  diffs = [s1 - s0 for s0, s1 in zip(s, s[1:])]
  zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
  mod = abs(reduce(gmpy2.gcd, zeroes))
  return mul_func(s, mod)

data = r'''
Baby:16165764624647108869
Easy:11674741605768810814
Normal:3983449574939514562
Hard:6388974328514794605
Master:258322866271049685
Crazy:12079665329571814379
'''
#a:17907025976111260127
#b:16949211548533185781
#c:12870317947452580829
#hack:7452296024397055178

s = map(int, re.findall(':(\d+)\n', data))
print mod_func(s)

import itertools

#a*x+c=y % b
def inc_func(xy, a, b):
  c = (xy[0][1] - xy[0][0]*a) % b
  return a, b, c

def mul_func(xy, b):
  #a*(x1-x0)=(k1-k0)*b+(y1-y0)
  a = (xy[1][1] - xy[0][1]) * gmpy2.invert(xy[1][0]-xy[0][0], b) % b
  return inc_func(xy, a, b)

def mod_func(xy):
  b = None
  for i in itertools.combinations(xy, 3):
    #(x2-x1)*(y1-y0)-(x1-x0)*(y2-y1)
    v = (i[2][0] - i[1][0]) * (i[1][1]-i[0][1]) - (i[1][0]-i[0][0])*(i[2][1]-i[1][1])
    v = abs(v)
    if b is None:
      b = v
    else:
      b = gmpy2.gcd(b, v)
  return mul_func(xy, b)

print mod_func(zip(s, s[1:]))