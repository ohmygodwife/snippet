#hamburgerRSA, meituan-2021, https://blog.maple3142.net/2021/08/01/cryptoctf-2021-writeups/

from Crypto.Util.number import *

n = 177269125756508652546242326065138402971542751112423326033880862868822164234452280738170245589798474033047460920552550018968571267978283756742722231922451193
c = 47718022601324543399078395957095083753201631332808949406927091589044837556469300807728484035581447960954603540348152501053100067139486887367207461593404096

# https://github.com/defund/coppersmith/blob/master/coppersmith.sage
load("/mnt/hgfs/snippet/ctf/crypto/rsa/coppersmiths/coppersmith.sage")

for plen in [20, 19]:
    for qlen in [20, 19]:
        Plen = plen + plen
        Qlen = qlen + qlen
        Z = Zmod(100 * n + 1) #Notice, not ONLY n!
        PZ = PolynomialRing(Z, "p,q")
        p, q = PZ.gens()
        P = p * 10 ^ plen + p
        Q = q * 10 ^ qlen + q
        PPP = P * 10 ^ Qlen + Q
        QQQ = Q * 10 ^ Plen + P
        f = PPP * QQQ - n
        sol = small_roots(f, (2 ^ 65, 2 ^ 65), m=7, d=3)
        if len(sol) > 0:
            p, q = sol[0]
            PPP = PPP(p, q)
            QQQ = QQQ(p, q)
            assert PPP * QQQ == n
            d = inverse_mod(65537, (PPP - 1) * (QQQ - 1))
            m = power_mod(c, d, n)
            print(long_to_bytes(m))
            exit()
