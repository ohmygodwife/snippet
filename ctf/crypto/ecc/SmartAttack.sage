#https://zhuanlan.zhihu.com/p/421202600

from Crypto.Util.number import *

def SmartAttack(P,Q,p):
    E = P.curve()
    Eqp = EllipticCurve(Qp(p, 2), [ ZZ(t) + randint(0,p)*p for t in E.a_invariants() ])

    P_Qps = Eqp.lift_x(ZZ(P.xy()[0]), all=True)
    for P_Qp in P_Qps:
        if GF(p)(P_Qp.xy()[1]) == P.xy()[1]:
            break

    Q_Qps = Eqp.lift_x(ZZ(Q.xy()[0]), all=True)
    for Q_Qp in Q_Qps:
        if GF(p)(Q_Qp.xy()[1]) == Q.xy()[1]:
            break

    p_times_P = p*P_Qp
    p_times_Q = p*Q_Qp

    x_P,y_P = p_times_P.xy()
    x_Q,y_Q = p_times_Q.xy()

    phi_P = -(x_P/y_P)
    phi_Q = -(x_Q/y_Q)
    k = phi_Q/phi_P
    return ZZ(k)
    
N1 = 27544759469094453505371358768052861416297003882211878831861112512567899543941
A1 = 4208715803791813173086894172778966025419787767340027559010619240548499823390
B1 = 11846440123913040489420209031751160809904311707943252241515965930654415480691
P1x = 479750084250968709343887919962436485997147832319843477221083468203689368148
P1y = 15452861783577624143044213767588871736433639621547613407582902947429567101675

Q1x = 14736970297054248276364510675718632926198693034158620007675880103924809577805
Q1y = 3447209262654420855289144268810543114387612255490962015335062266658385100211

p1 = 92636417177965240871815246762704348071
q1 = 297342668339361548416629796745639177971

P1 = (P1x, P1y)
Q1 = (Q1x, Q1y)
E1p = EllipticCurve(Zmod(p1), [0, 0, 0, A1, B1])
n1p = E1p.order()
P1p = E1p(P1)
Q1p = E1p(Q1)

print(n1p == p1)
# Pohlig Hellman
d1p = P1p.discrete_log(Q1p)

E1q = EllipticCurve(Zmod(q1), [0, 0, 0, A1, B1])
n1q = E1q.order()
P1q = E1q(P1)
Q1q = E1q(Q1)

print(n1q == q1)
# Smart
d1q = SmartAttack(P1q, Q1q, q1)

d1 = crt([d1p, d1q], [P1p.order(), P1q.order()])
print(d1)