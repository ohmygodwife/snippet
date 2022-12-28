#Dasctf-20220423, CVE OF RSA, https://4xwi11.github.io/posts/9171e9d7/
#sage -python roca.py

import logging
import os
import sys
from math import log

from sage.all import Zmod
from sage.all import factor

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(os.path.abspath(__file__)))))
if sys.path[1] != path:
    sys.path.insert(1, path)

import sys
sys.path.append('/mnt/hgfs/tools/crypto/rsa/crypto-attacks') 
from shared.small_roots import howgrave_graham


def _prime_power_divisors(M):
    divisors = []
    for p, e in factor(M):
        for i in range(1, e + 1):
            divisors.append(p ** i)

    divisors.sort()
    return divisors


# Algorithm 2.
def compute_max_M_(M, ord_):
    for p in _prime_power_divisors(M):
        ordp = Zmod(p)(65537).multiplicative_order()
        if ord_ % ordp != 0:
            M //= p

    return M


# Section 2.7.2.
def _greedy_find_M_(n, M):
    ord = Zmod(M)(65537).multiplicative_order()
    while True:
        best_r = 0
        best_ord_ = ord
        best_M_ = M
        for p in _prime_power_divisors(ord):
            ord_ = ord // p
            M_ = compute_max_M_(M, ord_)
            r = (log(ord, 2) - log(ord_, 2)) / (log(M, 2) - log(M_, 2))
            if r > best_r:
                best_r = r
                best_ord_ = ord_
                best_M_ = M_

        if log(best_M_, 2) < log(n, 2) / 4:
            return M

        ord = best_ord_
        M = best_M_


def factorize(N, M, m, t, g=65537):
    """
    Recovers the prime factors from a modulus using the ROCA method.
    More information: Nemec M. et al., "The Return of Coppersmith's Attack: Practical Factorization of Widely Used RSA Moduli"
    :param N: the modulus
    :param M: the primorial used to generate the primes
    :param m: the m parameter for Coppersmith's method
    :param t: the t parameter for Coppersmith's method
    :param g: the generator value (default: 65537)
    :return: a tuple containing the prime factors
    """
    logging.info("Generating M'...")
    M_ = _greedy_find_M_(N, M)
    ZmodM_ = Zmod(M_)
    g = ZmodM_(g)
    c_ = ZmodM_(N).log(g)
    ord_ = g.multiplicative_order()

    x = Zmod(N)["x"].gen()
    X = int(2 * N ** 0.5 // M_)
    logging.info("Starting exhaustive a' search...")
    for a_ in range(c_ // 2, (c_ + ord_) // 2 + 1):
        f = M_ * x + int(g ** a_)
        for k_, in howgrave_graham.modular_univariate(f, N, m, t, X):
            p = int(f(k_))
            if N % p == 0:
                return p, N // p

# Some logging so we can see what's happening.
logging.basicConfig(level=logging.DEBUG)

M = 962947420735983927056946215901134429196419130606213075415963491270
N = 14481363580917358871472996410471767154481047067466167591298208947805462002275531552979475988627964256677709787930755013972295770123571982960720640872341517
#https://acmccs.github.io/papers/p1631-nemecA.pdf
''' n bit length:
512: m=5,t=6
1024: m=4,t=5
2048: m=6,t=7
3072: m=25,t=26
4096: m=7,t=8
'''
p, q = factorize(N, M, 5, 6)

print("Found p = {} and q = {}".format(p, q))

from Crypto.Util.number import  *
from gmpy2 import invert

c = 3679892564888936950542940140902963743841717939818025696558626052971555790204073416047068709668040686939721666022034628127241497612925260505783618939964139

d = invert(0x10001, N - p - q + 1)
m = pow(c, d, N)
print(long_to_bytes(m))
# flag{e28e6991-080d-4587-900d-db3c47139453}

