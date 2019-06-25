#http://z3prover.github.io/api/html/namespacez3py.html
from z3 import *
import gmpy2

z=213932962252915797768584248464896200082707350140827098890648372492180142394587
m=282832747915637398142431587525135167098126503327259369230840635687863475396299
x=254732859357467931957861825273244795556693016657393159194417526480484204095858
y=261877836792399836452074575192123520294695871579540257591169122727176542734080

encrypted = [IntVal(i) for i in encrypted]
message = [Int('flag%d' % i) for i in range(len(encrypted)-1)]
a, b, c = BitVecs('a b c', 262) # make sure not overflow, a+c*8<2^257 * 9 < 2 ^ 261
s = Solver()
s.add(UGT(a, pow(2, 256, m)))
s.add(ULT(a, pow(2, 257, m)))
s.add(UGT(b, pow(2, 256, m)))
s.add(ULT(b, pow(2, 257, m)))
s.add(UGT(c, pow(2, 256, m)))
s.add(ULT(c, pow(2, 257, m)))
s.add(x == (a + b * 3) % m)
s.add(y == (b - c * 5) % m)
s.add(z == (a + c * 8) % m)
while s.check() == sat:
    A,B= s.model()[a].as_long(),s.model()[b].as_long()
    if gmpy2.gcd(A,B) == 1:
        print A,B
        break


def gen():
  v12 = BitVec('x', 32+7)
  s = Solver()
#  s.add(v12 >= 2 ** 31)
#  s.add(v12 < 2 ** 32)
  
  v9 = 0
  for i in range(32):
    v8 = v9 ^ (v12 & 0xff) ^ byte_404020[i]
    if i < 5:
      s.add(v8 == ord('FLAG{'[i]))
    elif i == 31:
      s.add(v8 == ord('}'))
    else:
      s.add(Or(And(v8 >= ord('A'), v8 <= ord('Z')), v8 == ord('_')))
    v9 ^= byte_404020[i]
    v12 >>= 1
  
  if s.check() == sat:
    print s.model()