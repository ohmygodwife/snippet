'''
https://github.com/p4-team/ctf/tree/master/2015-10-18-hitcon/crypto_314_rsabin
https://193s.github.io/blog/2015/10/19/hitcon-2015-rsabin-writeup/
https://github.com/pwning/public-writeup/tree/master/hitcon2015/crypto314-rsabin
'''
from Crypto.Util.number import *
import string
def egcd(a, b):
    u, u1 = 1, 0
    v, v1 = 0, 1
    while b:
        q = a // b
        u, u1 = u1, u - q * u1
        v, v1 = v1, v - q * v1
        a, b = b, a - q * b
    return a, u, v


def phi(p, q):
    return (p - 1) * (q - 1)


def get_d(p, n, e):
    q = n / p
    phi_v = phi(p, q)
    _gcd, d, _2 = egcd(e, phi_v)
    if d < 0:
        d += phi_v
    return d


def modular_sqrt(a, p):
    """ Find a quadratic residue (mod p) of 'a'. p
        must be an odd prime.

        Solve the congruence of the form:
            x^2 = a (mod p)
        And returns x. Note that p - x is also a root.

        0 is returned is no square root exists for
        these a and p.

        The Tonelli-Shanks algorithm is used (except
        for some simple cases in which the solution
        is known from an identity). This algorithm
        runs in polynomial time (unless the
        generalized Riemann hypothesis is false).
    """
    # Simple cases
    #
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) / 4, p)

    # Partition p-1 to s * 2^e for an odd s (i.e.
    # reduce all the powers of 2 from p-1)
    #
    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1

    # Find some 'n' with a legendre symbol n|p = -1.
    # Shouldn't take long.
    #
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Here be dragons!
    # Read the paper "Square roots from 1; 24, 51,
    # 10 to Dan Shanks" by Ezra Brown for more
    # information
    #

    # x is a guess of the square root that gets better
    # with each iteration.
    # b is the "fudge factor" - by how much we're off
    # with the guess. The invariant x^2 = ab (mod p)
    # is maintained throughout the loop.
    # g is used for successive powers of n to update
    # both a and b
    # r is the exponent - decreases with each update
    #
    x = pow(a, (s + 1) / 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in xrange(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x
        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def legendre_symbol(a, p):
    ls = pow(a, (p - 1) / 2, p)
    return -1 if ls == p - 1 else ls


class Rabin(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p * q

    def encrypt(self, m):
        return (m * m) % self.n

    def decrypt(self, c):
        try:
            gcd, yp, yq = egcd(self.p, self.q)
            mp = modular_sqrt(c, self.p)
            mq = modular_sqrt(c, self.q)
            assert yp * self.p + yq * self.q == 1
            assert (mp * mp) % self.p == c % self.p
            assert (mq * mq) % self.q == c % self.q
            r1 = (yp * self.p * mq + yq * self.q * mp) % self.n
            s1 = (yp * self.p * mq - yq * self.q * mp) % self.n
            r2 = self.n - r1
            s2 = self.n - s1
            return r1, s1, r2, s2
        except AssertionError:
            return []


n = 20313365319875646582924758840260496108941009482470626789052986536609343163264552626895564532307L
p = 123722643358410276082662590855480232574295213977L
q = n / p
e = 31415926535897932384L
e_p = e / 32
ct = 19103602508342401901122269279664114182748999577286972038123073823905007006697188423804611222902
d = get_d(p, n, e_p)

rabin = Rabin(p, q)
partially_decoded_ct = [ct]
for i in range(5):
    new_partially_decoded_ct = []
    for ct_p in partially_decoded_ct:
        new_ct_p = rabin.decrypt(ct_p)
        new_partially_decoded_ct.extend(list(new_ct_p))
    partially_decoded_ct = set(new_partially_decoded_ct)

potential_plaintext = []
for potential_rsa_ct in partially_decoded_ct:
    pt = pow(potential_rsa_ct, d, n)
    potential_plaintext.append(pt)

#assert len(flag) == 50
def crack_flag(ct, n):
    n_len = 40
    flag_len = 50
    const = int('hitcon{'.encode('hex'), 16) * (256**(flag_len - 7))
    for a in range(32, 128):
        for b in range(32, 128):
            for c in range(32, 127):
                brute = (a * 256 * 256 + b * 256 + c) * (256**(flag_len - 10))
                flag = (ct - const - brute) % n 
                flag = (flag - ord('}')) * modinv(256, n) % n
                flagstr = long_to_bytes(flag)
                if all(32 <= ord(c) <= 128 for c in flagstr):
                    print chr(a) + chr(b) + chr(c) + flagstr
'''
for msg in possible_inputs:
    print 'testing', msg
    crack_flag(msg, n)
'''

# FLAG = x*N+m, brute force x
def brute_force_x():
  charset = string.printable

  for m in potential_plaintext:
    print '#', m
    sr = (bytes_to_long('hitcon{')<<(8*43)) / n
    v_flag = False
    las_g = ''
    x = sr + 210000000
    while x <= sr + 900000000:
      r = long_to_bytes(m + n*x)
      if not v_flag and r[-1] == '}':
        v_flag = True
      if r.startswith('hitcon{'):
        g = r[7:11]
        # hitcon{(g)...
        if g[0] != las_g:
          print repr(g)
          las_g = g[0]
        if all([c in charset for c in r]):
          # found flag ! hitcon{[:print:]+}
          print '***************************************************'
          print x
          print r
          exit(0)
      x += 256 if v_flag else 1

#brute_force_x()

#hitcon{***} + i * n * 2**8
def brute_force_i():
  for m in potential_plaintext:
    print 'm = {}'.format(m)

    # OH NO! They left out a bunch of bits :(
    flagfmt = 'hitcon{' + ' '*42 + '}' #space is the smallest char in printable
    assert len(flagfmt) == 50
    # make curm as 'hitcon{***}' and mod n = m
    curm = bytes_to_long(flagfmt) // n * n + m
    while curm % 256 != ord('}'):
        curm += n

    assert curm % n == m
    assert pow(curm, e, n) == ct

    import re
    valid_flag_re = re.compile(r'^[\x20-\x7e]+$')

    increment = n * 256 # leave the last byte (}) unchanged
#    for i in xrange(1000000000):
    i = 0
    while True:
        s = long_to_bytes(curm, 50)
        if s > 'hitcon{\x7f':
            break
        if all([c in string.printable for c in s]): #if valid_flag_re.match(s):
            print i, repr(s)
            exit(0)
#        if i % 10000 == 0:
#            print i, repr(s[:10])

        curm += increment
        i += 1
        
brute_force_i()
#950499 "hitcon{Congratz~~! Let's eat an apple pi <3.14159}"