# g1 = x^e - c1, g2 = (x+y)^e - c2, m2 = m1 + y

def short_pad_attack(c1, c2, e, n):
    PRxy.<x,y> = PolynomialRing(Zmod(n))
    PRx.<xn> = PolynomialRing(Zmod(n))
    PRZZ.<xz,yz> = PolynomialRing(Zmod(n))

    g1 = x^e - c1
    g2 = (x+y)^e - c2

    q1 = g1.change_ring(PRZZ)
    q2 = g2.change_ring(PRZZ)

    h = q2.resultant(q1)
    h = h.univariate_polynomial()
    h = h.change_ring(PRx).subs(y=xn)
    h = h.monic()

    kbits = n.nbits()//(2*e*e)
    diff = h.small_roots(X=2^kbits, beta=0.5)[0]  # find root < 2^kbits with factor >= n^0.5

    return diff

def related_message_attack(c1, c2, diff, e, n):
    PRx.<x> = PolynomialRing(Zmod(n))
    g1 = x^e - c1
    g2 = (x+diff)^e - c2

    def gcd(g1, g2):
        while g2:
            g1, g2 = g2, g1 % g2
        return g1.monic()

    return -gcd(g1, g2)[0]


if __name__ == '__main__':
    n = 0x00bef498e6eb2cffe71312da47ab89d2c47db7438ea2cfa992ddddbc2a01978001fc51e286e6ebf028396cdb8b3323c60e6b9d50cd84187cf7f48e3875a2f0890f70b02333ad89db2923863ce146562286f63fb0a1d0198e3a6862ba5ac12e85a5c6d0d27cb1c81bdf69cc5bc95b8001a2f744517f9437b4ddd5a076fc0e9a5de1a7a268c40f31aa29e8dc27c0b3a182299ca7a9335b4bd4585452f6107c238e486c98dd73a5f9862e9e80b152f53381c72f897107551c281259ac3ee32c4b4f46cc03127d1bf699acd0266f3c6729253c70da0c69b1560fa172735709866b375b6eba294e1ce8b46fba798ba380080b4bf9603998cac199d9cd46e30ae8da9e7f
    e = 3

    nbits = n.nbits()
    kbits = nbits//(2*e*e)
    print "upper %d bits (of %d bits) is same" % (nbits-kbits, nbits)

    # ^^ = bit-wise XOR
    # http://doc.sagemath.org/html/en/faq/faq-usage.html#how-do-i-use-the-bitwise-xor-operator-in-sage
    m1 = randrange(2^nbits)
    m2 = m1 ^^ randrange(2^kbits)
    c1 = pow(m1, e, n)
    c2 = pow(m2, e, n)

    diff = short_pad_attack(c1, c2, e, n)
    print "difference of two messages is %d" % diff

    print m1
    m1 = related_message_attack(c1, c2, diff, e, n)
    print m1
    print m2
    print m1 + diff