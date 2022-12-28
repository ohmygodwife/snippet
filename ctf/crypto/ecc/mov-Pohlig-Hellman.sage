#Trick,cmcc-200421
#https://sectt.github.io/writeups/Volga20/crypto_keygreed/README
#https://zhuanlan.zhihu.com/p/421541257

N2 = 6471339743593595797696002766822660599108196938080465998531085409467
A2 = 3199218821393204771660095172457569312269694438403110131957204042314
B2 = 762889472027318213897694878260359911054972690369935049954326689904
P2x = 2557373437970770011124755960432555084678930336188254243278984381842
P2y = 4442763096366920105760404533052204677305995021662082361185473321644
Q2x = 4834036103940457959470026215023033401071737087504569417466448644066
Q2y = 5511016821581393405975510064568222454318072088628361854656950557373
P2 = (P2x,P2y)
Q2 = (Q2x,Q2y)

p2 = 69857405335111415530599248077
q2 = 92636417177965240871815246762704348071

def mov():
  F = GF(p2)
  E = EllipticCurve(F,[A2,B2])
  print(E.order() == p2+1)
  k = 2 # min_k E.order() | (p^k-1)
  Fy = GF(p2^k,'y')
  Ee = EllipticCurve(Fy,[A2,B2])

  P = E(P2)
  xP = E(Q2)

  Pe = Ee(P)
  xPe = Ee(xP)

  while True:
    R = Ee.random_point()
    m = R.order()
    d = gcd(m, P.order())
    Q = (m//d)*R

    if P.order()/Q.order() in ZZ and P.order() == Q.order():
      break

  n = P.order()
  print('computing pairings')
  alpha = Pe.weil_pairing(Q,n)
  beta = xPe.weil_pairing(Q,n)

  print('computing log')
  return beta.log(alpha)

E2p = EllipticCurve(GF(p2), [A2, B2])
n2p = E2p.order()
P2p = E2p(P2)
Q2p = E2p(Q2)
print(n2p)

#mov attack
d2p = mov()
print(d2p)

E2q = EllipticCurve(GF(q2), [A2, B2])
n2q = E2q.order()
P2q = E2q(P2)
Q2q = E2q(Q2)
print(n2q)

# Pohlig Hellman
d2q = P2q.discrete_log(Q2q)
print(d2q)

d2 = crt([d2p, d2q], [P2p.order(), P2q.order()])
print(d2)
