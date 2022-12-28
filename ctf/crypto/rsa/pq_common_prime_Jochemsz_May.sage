#common_rsa, xiangyun-2022, https://mp.weixin.qq.com/s/4JVUFZ-pAMqoF8ZxSiolWA

# the following attack is due to Ellen Jochemsz and Alexander May
# see https://www.iacr.org/archive/asiacrypt2006/42840270/42840270.pdf

n = 253784908428481171520644795825628119823506176672683456544539675613895749357067944465796492899363087465652749951069021248729871498716450122759675266109104893465718371075137027806815473672093804600537277140261127375373193053173163711234309619016940818893190549811778822641165586070952778825226669497115448984409
e = 31406775715899560162787869974700016947595840438708247549520794775013609818293759112173738791912355029131497095419469938722402909767606953171285102663874040755958087885460234337741136082351825063419747360169129165
cipher = 97724073843199563126299138557100062208119309614175354104566795999878855851589393774478499956448658027850289531621583268783154684298592331328032682316868391120285515076911892737051842116394165423670275422243894220422196193336551382986699759756232962573336291032572968060586136317901595414796229127047082707519

gamma = 320/1024 # p = 2 * a * g + 1, g bit length 320
delta = 135/1024 # d = getPrime(135)
m = 2
tau = (1 / 2 + gamma - 4 * delta) / (2 * delta)
t = ZZ(floor(tau * m))

X = ZZ(floor(n ^ delta))
Y = ZZ(floor(n ^ (delta + 1 / 2 - gamma)))
Z = ZZ(floor(n ^ (delta + 1 / 2 - gamma)))
W = ZZ(floor(n ^ (2 + 2 * delta - 2 * gamma)))
R = W * X ^ (2 * (m - 1) + t) * (Y * Z) ^ (m - 1)

# assert X ^ (7 + 9 * tau + 3 * tau ^ 2) * (Y * Z) ^ (5 + 9 * tau / 2) < W ^ (3 + 3 * tau)

P = PolynomialRing(ZZ, 'x,y,z')
x,y,z = P.gens()

# we know that ed = k(2gab) + 1 = k(p - 1)b + 1 = ka(q - 1) + 1
# we can multiply the last two expressions to get a semi-symmetric equation for
# (ed)^2, of which we want to find its roots
f = e^2 * x^2 + e * x * (y + z - 2) - (n - 1) * y * z - (y + z - 1)
assert f.constant_coefficient() == 1

M = set()
S = set()
# generate monomials
# S contains monomials of f^{m - 1} with x-shifts
# M contains monomials of f^{m} with x-shifts \setminus S
for i3 in range(0, m):
    for i2 in range(0, m):
        for i1 in range(0, 2 * (m - 1) - (i2 + i3) + t + 1):
            S.add(x ^ i1 * y ^ i2 * z ^ i3)
for i3 in range(0, m + 1):
    for i2 in range(0, m + 1):
        for i1 in range(0, 2 * m - (i2 + i3) + t + 1):
            M.add(x ^ i1 * y ^ i2 * z ^ i3)
M_S = M - S
M_S = sorted(M_S)
S   = sorted(S)
M   = sorted(M)

# use a dict to map each shift polynomial with its lowest order monomial to
# make diagonalizing the basis matrix easier
g   = {}

# generate shift polynomials
# the shift polynomials are generated with a polynomial derived from f (mod R)
# namely ff = a0^{-1} * f (mod R) such that the constant term of ff is 1
# i am fairly certain any polynomial with constant term 1 and the correct roots
# can be used here, although i have only tested it with ff and f
ff = f.change_ring(Zmod(R)).change_ring(ZZ)
for mono in S:
    i1, i2, i3 = mono.degree(x), mono.degree(y), mono.degree(z)
    fn = mono * ff(x, y, z) * X ^ (2 * (m - 1) + t - i1) * Y ^ (m - 1 - i2) * Z ^ (m - 1 - i3)
    fn = expand(fn(x * X, y * Y, z * Z))
    g[mono] = fn
for mono in M_S:
    fn = R * mono
    fn = expand(fn(x * X, y * Y, z * Z))
    g[mono] = fn

npolys = len(g)
nmonos = len(M)
print("polynomials: {}".format(npolys))
print("monomials:   {}".format(nmonos))
assert npolys == nmonos

B = Matrix(ZZ, npolys, nmonos)
C = Matrix(ZZ, npolys, nmonos)

for row, mono in enumerate(M):
    i1, i2, i3 = mono.degree(x), mono.degree(y), mono.degree(z)
    for c, mono_ in g[mono]:
        col = M.index(mono_)
        C[row, col] = 1
        B[row, col] = c

    # assert that diagonal elements are what they should be
    idx = M.index(mono)
    if mono in S:
        assert B[idx, idx] == X ^ (2 * (m - 1) + t) * (Y * Z) ^ (m - 1)
    elif mono in M_S:
        assert B[idx, idx] == R * X ^ i1 * Y ^ i2 * Z ^ i3
    else:
        raise Exception("what")

print(C.str())

# assert triangular form
for col in range(nmonos):
    for row in range(col + 1, npolys):
    # for row in xrange(col):
        assert B[row, col] == 0
    assert B[col, col] != 0

print("LLL...")
BB = B.LLL(algorithm='fpLLL:proved', fp='rr')
CC = Matrix(ZZ, npolys, nmonos)
for row in range(npolys):
    for col in range(nmonos):
        if BB[row, col] != 0:
            CC[row, col] = 1
print(CC.str())

# helper to construct a polynomial from coefficients
def topoly(r):
    RR = PolynomialRing(QQ, 'x,y,z')
    pol = 0
    for col in range(nmonos):
        pol += r[col] * M[col]
    pol = RR(pol(x / X, y / Y, z / Z))
    for c, _ in pol:
        assert c.is_integer()
    return P(pol)

# pull out h1, h2
hv = [expand(topoly(r)) for r in BB]
h1, h2 = hv[0:2]

# at some point we need to polynomial engines to something that can solve for
# roots, the default univariate engine works
s, = PolynomialRing(ZZ, 's').gens()

# these should be algebraically independent
assert h1.gcd(f).degree() == 0
assert h2.gcd(f).degree() == 0
assert h1.gcd(h2).degree() == 0

# take care that resultants are computed with f and not ff, which is a
# polynomial mod R
# these resultants eliminate z
h1x = h1.resultant(f, z)
h2x = h2.resultant(f, z)
hh  = h1.resultant(h2, z)

# this eliminates y
hy = h1x.resultant(h2x, y)

# now we can solve for roots via back substitution
d = []
for r, m in hy(x=s).roots():
    if r == 0:
        continue
    d.append(r)
assert len(d) == 1
d = d[0]

ka = []
for r, m in hh(x=d, y=s).roots():
    if r == 0:
        continue
    ka.append(r)
# f(x, y, z) = f(x, z, y) so we should have two solutions here
assert len(ka) == 2
ka = ka[0]

kb = []
for r, m in f(x=d, y=ka, z=s).roots():
    if r == 0:
        continue
    kb.append(r)
assert len(kb) == 1
kb = kb[0]

print("found d  = {}".format(d))
print("found ka = {}".format(ka))
print("found kb = {}".format(kb))

k = gcd(ka, kb)
a = ka // k
b = kb // k
g = (e * d - 1) // (2 * k * a * b)
p = 2 * g * a + 1
q = 2 * g * b + 1

from Crypto.Util.number import *

print(long_to_bytes(int(pow(cipher,d,n))))