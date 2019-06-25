# f(x) = x + pbar = 0 (mod b)

p = 0x00f23799c031b942026e420769b74d22fa2114428189139c43c366c6ab8367c6b3d6f821449aafb2058b0e6ed964fa0ad45fb306f96376e80823a72b58101919e50acad3b5e6d079e7ff9218ed6df6edbef536742714ce88b2e717f45af53ef0d04c89faf01c80b28e764973aba27726c85c0236e8756a865c03577722bac5e391
q = 0x00c9d24330fa4945cfe1e5d6912d6bde0231035a1cc8d8ae67d949347b895f8d579bce2adaf37c568957b17a6564dbf80d36d81e4622ab30e02132b0155aefbd3912a27c625a9b7b05bc72217039f5aa88c20cbf9871c3228e9d80d9106f94b11c1f50c40c96862b5cd6b6f781883dd2eff80a059d3ca027af6a03edeb34a7390f
n = p*q
e = 3

beta = 0.5
epsilon = beta^2/7

pbits = p.nbits()
kbits = floor(n.nbits()*(beta^2-epsilon))
pbar = p & (2^pbits-2^kbits)
print "upper %d bits (of %d bits) is given" % (pbits-kbits, pbits)

PR.<x> = PolynomialRing(Zmod(n))
f = x + pbar

print p
x0 = f.small_roots(X=2^kbits, beta=0.3)[0]  # find root < 2^kbits with factor >= n^0.3
print x0 + pbar