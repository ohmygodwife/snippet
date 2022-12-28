#Omni Crypto, pwn2win-2020, https://furutsuki.hatenablog.com/entry/2020/06/01/023111

def sqrt_power_of_2_mod(a, n):
    """find x^2 = a mod 2^n""" 
    assert a % 8 == 1

    res = []
    for x in [1, 3]:
        for k in range(3, n):
            i = ((x*x - a) // pow(2, k)) % 2
            x = x + i * pow(2, k-1)

        res.append(x)
        res.append(2**n - x)
    return res
    
from sage.all import *
import gmpy2
from Crypto.Util import number

N = 0xf7e6ddd1f49d9f875904d1280c675e0e03f4a02e2bec6ca62a2819d521441b727d313ec1b5f855e3f2a69516a3fea4e953435cbf7ac64062dd97157b6342912b7667b190fad36d54e378fede2a7a6d4cc801f1bc93159e405dd6d496bf6a11f04fdc04b842a84238cc3f677af67fa307b2b064a06d60f5a3d440c4cfffa4189e843602ba6f440a70668e071a9f18badffb11ed5cdfa6b49413cf4fa88b114f018eb0bba118f19dea2c08f4393b153bcbaf03ec86e2bab8f06e3c45acb6cd8d497062f5fdf19f73084a3a793fa20757178a546de902541dde7ff6f81de61a9e692145a793896a8726da7955dab9fc0668d3cfc55cd7a2d1d8b631f88cf5259ba1
c = 0xf177639388156bd71b533d3934016cc76342efae0739cb317eb9235cdb97ae50b1aa097f16686d0e171dccc4ec2c3747f9fbaba4794ee057964734835400194fc2ffa68a5c6250d49abb68a9e540b3d8dc515682f1cd61f46352efc8cc4a1fe1d975c66b1d53f6b5ff25fbac9fa09ef7a3d7e93e2a53f9c1bc1db30eed92a30586388cfef4d68516a8fdebe5ebf9c7b483718437fcf8693acd3118544249b6e62d30afa7def37aecf4da999c1e2b686ca9caca1b84503b8794273381b51d06d0dfb9c19125ce30e67a8cf72321ca8c50a481e4b96bbbc5b8932e8d5a32fa040c3e29ced4c8bf3541e846f832a7f9406d263a592c0a9bce88be6aed043a9867a7

e = 65537

def decrypt(p):
  q = N / p
  assert p * q == N
  phi = (p - 1) * (q - 1)
  d = e.inverse_mod(phi)
  m = pow(c, d, N)
  print number.long_to_bytes(m)

size = 1024
n_root, _ = gmpy2.iroot(N, 2)
for lsb_len in range(200, 400, 5):
    print(lsb_len)
    for msb_len in range(200, 400, 5):
        shift = int(n_root).bit_length() - msb_len
        msb = int(n_root) >> shift

        ls = sqrt_power_of_2_mod(N, lsb_len)
        for l in ls:
            lsb = l

            PR.<x> = PolynomialRing(Zmod(N))

            f = msb * (2 ** (size - msb_len)) + (x * (2 ** lsb_len)) + lsb
            f = f.monic()
            xs = f.small_roots(X=2**(size - msb_len - lsb_len), beta=0.3)
            for s in xs:
                p =  int(msb * (2 ** (size - msb_len)) + (s * (2 ** lsb_len)) + lsb)
                if N % p == 0:
                  decrypt(p)
                  
