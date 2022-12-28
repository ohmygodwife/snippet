#https://hgarrereyn.gitbooks.io/th3g3ntl3man-ctf-writeups/content/2017/picoCTF_2017/problems/cryptography/ECC2/ECC2.html

M = 93556643250795678718734474880013829509320385402690660619699653921022012489089
A = 66001598144012865876674115570268990806314506711104521036747533612798434904785
B = 25255205054024371783896605039267101837972419055969636393425590261926131199030
P = (56027910981442853390816693056740903416379421186644480759538594137486160388926, 65533262933617146434438829354623658858649726233622196512439589744498050226926)
Q = (61124499720410964164289905006830679547191538609778446060514645905829507254103, 2595146854028317060979753545310334521407008629091560515441729386088057610440)

#E = EllipticCurve(GF(n), [0, 0, 0, A, B])
E = EllipticCurve(GF(M),[A,B]) #GF is short for FiniteField
P = E.point(P)
Q = E.point(Q)
factors, exponents = zip(*factor(E.order()))
print(factors)
print(exponents)
primes = [factors[i] ^ exponents[i] for i in range(len(factors))][:1] #last two factors are too large to calculate the discrete log, so just ignore them!!!
dlogs = []
for fac in primes:
    t = int(int(P.order()) / int(fac))
    dlog = discrete_log(t*Q,t*P,operation="+")
    dlogs += [dlog]
    print("factor: "+str(fac)+", Discrete Log: "+str(dlog)) #calculates discrete logarithm for each prime order

l = crt(dlogs,primes)
print(l)
