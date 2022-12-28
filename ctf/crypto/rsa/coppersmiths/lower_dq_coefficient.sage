#corrupted_key, bluehat-2022, https://mp.weixin.qq.com/s/A9OmgHAmGLJPEL4cQBU8zQ

n = 0x00d7152506aa9cec05e5335d6b46f5491407c3199fd51091f1f6030d3762b9e03f49c9dcdc075054e0cc148b974b41854bd93b4ee16a2a876ee62005e80ef806b7aa3b64b1bf9b1fa773e353d0cdb9ff9783ddd5f5e67499ad10f361e938d00b82a6a4c42a0535c5e76721798e86b45cd4b8d03b0d7e75c2be8766a1e843bdc641
coefficient = 0x00e3016cb3609c1d643c167439c3b938b881f4237f24860d3b1cb85a626d5ccd4726964e0f8270d6c4df9ebfebcc538e4ee5e1a7b7368ede51ec6ae917f78eb598
e = 0x010001
dq_l = 0xc90bcecf1cbab3358585e8a041d1b1

for k in range(59199,59222):
    F.<x> = PolynomialRing(Zmod(n))
    if k%100 == 0:
        print("%d times"%k)
    q = (x * 2**120 + dq_l)
    f = q * e - 1   + k   
    TT= coefficient*f*f-k*f
    TT=TT.monic()
    sss = TT.small_roots(X = 2**(512-120),beta=0.4)
    if (len(sss)) != 0 :
        print(k)
        print(coefficient)
        print(sss)
        dq = int(sss[0] * 2**120 + dq_l)
        break
  
q = GCD((dq * e - 1   + k) ,n)
if n % q == 0:
    p = n/q
else:
    raise Exception

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
with open('flag.enc', 'rb') as f:
    c = f.read()
    phin = (p-1)*(q-1)
    d = inverse_mod(e, phin)
    privkey=RSA.construct((int(n),long(e),int(d)))
    m = PKCS1_OAEP.new(privkey).decrypt(c)
    print m