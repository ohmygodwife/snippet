'''
http://www.cnblogs.com/WangAoBo/p/7541481.html
Whctf-2017-UNTITLED
'''
n = 0x621725fc8ce7ce38c3ff9da9e7d4a9d8764eac78985f5abcf52bbad15f172d76c0d9cc4b08b1bbcd36590bc0050ab492f7df58404c0bca8b178e7e0f07c0c08e46ae63d8248b1f1cdd3f6cfed6fcc348b62e1cb7b269fc800c77d303ae154e1ade78a7492158c80818b8b180699e709764d31e08544e9c6dd75788d468ce1288927d5cea4336d6a76a9998731e15285c4695550c4db7210d09168903774ccee5dda6f8d3a502f8eac38a97c0cd84b3c3be87751dfc9f3bbcdec881d20fc7cb0086f71a0146b2e11e688372f809e401b9f19c003f75920df962631127dbda84cc781870b7895382c02d726eabc8373e73aec38f0a1dad4b8d0060c47511ef75d3
p = 0xb447abcd768378f05675b98f4724e934b1a7251749b14b11d3af19d3a47e98dbf90b94a77a01ab76e6a7f99d5b79cfce8e9edfcc7b626ed0f1699d743fa78bd73ff4a03f904bde

import string
dic = string.digits + "abcdef"

# lack two hex digits
for a in dic:
    for b in dic:
        pp = hex(p) + a + b
        pp += '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
#       pp = int(pp, 16)
#        p_fake = pp+0x10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        pbits = 1024
        kbits = pbits-576
#        pbar = p_fake & (2^pbits-2^kbits)
        pbar = int(pp, 16)
#        print "upper %d bits (of %d bits) is given" % (pbits-kbits, pbits)
        PR.<x> = PolynomialRing(Zmod(n))
        f = x + pbar
        try:
            x0 = f.small_roots(X=2^kbits, beta=0.4)[0]  # find root < 2^kbits with factor >= n^0.4
            print(x0 + pbar)
        except:
            pass