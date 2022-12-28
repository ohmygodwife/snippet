#https://zhuanlan.zhihu.com/p/398817594,Ferman,CryptoCTF-2021

from Crypto.Util.number import isPrime, long_to_bytes
import gmpy2

e = 65537
c = 59903633185427893959377666141195141335949903109093969136657116694622223939297263400038957081629880639790822689750406752167194829622741887848555827724297235217131141017110810496070249970562873247688939261306546249688313511725121026031313489405922735718594383906176003654976929312618218560308949622591734167295494292979021272112049896348581744336084174194602412376605368254897005787912271897492544405635649478443744534415975298067269303070546074815372739424518343282200990909180511
base = [6625282065037, 287469038944943593, 188481945421316245985002832952993782537]

def my_exgcd(p, x, y):
    if (x * x < p and y * y < p):
        return x, y
    else:
        return my_exgcd(p, y, x%y)

def get_sol(p):
    g = 2
    while (pow(g, (p-1) // 2, p) == 1):
        g += 1
    c = pow(g, (p-1) // 4, p)
    return my_exgcd(p, p, c)

sols = [get_sol(p) for p in base]
sols = sols * 7

cur_set = set([(0, 1), (0, -1), (1, 0), (-1, 0)])
for a, b in sols:
    pre_set = cur_set
    cur_set = set()
    for c, d in pre_set:
        cur_set.add((a*c+b*d, a*d-b*c))
        cur_set.add((a*c-b*d, a*d+b*c))

def rsa(p, q):
    d = gmpy2.invert(e, (p-1)*(q-1))
    m = pow(c, d, p*q)
    print(long_to_bytes(m))

for a, b in cur_set:
    p = a + 797
    q = b + 1302
    if (isPrime(p) and isPrime(q)):
        print(p)
        print(q)
        rsa(p, q)