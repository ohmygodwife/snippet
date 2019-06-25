'''
m=nextprime(p) * nextprime(q) = (p + x) * (q + y)
'''
import gmpy2
n = 0x78e2e04bdc50ea0b297fe9228f825543f2ee0ed4c0ad94b6198b672c3b005408fd8330c36f55d36fb129d308c23e5cb8f4d61aa7b058c23607cef83d63c4ed0f066fc0b3c0062a2ac68c75ca8035b3bd7a320bdf29cfcf6cc30377743d2a8cc29f7c588b8043412366ab69ec824309cb1ef3851d4fb14a1f0a58e4a1193f5518fa1d0c159621e1f832b474182593db2352ef05101bf367865ad26efe14fce977e9e48d3310a18b67991958d1a01bd0f3276a669866f4deaef2a68bfaefd35fe2ba5023a22c32ae8b2979c26923ee3f855363f18d8d58bb1bc3b7f585c9d9f6618c727f0f7b9e6f32af2864a77402803011874ed2c65545ced72b183f5c55d4d1L
m = 0x78e2e04bdc50ea0b297fe9228f825543f2ee0ed4c0ad94b6198b672c3b005408fd8330c36f55d36fb129d308c23e5cb8f4d61aa7b058c23607cef83d63c4ed0f066fc0b3c0062a2ac68c75ca8035b3bd7a320bdf29cfcf6cc30377743d2a8cc29f7c588b8043412366ab69ec824309cb1ef3851d4fb14a1f0a58e4a1193f5a58ee70a59ac06b64dbe04b876ff69436b78cf03371f2062707897bf4e580870e42b5e62709b69f6d4939ac5641ea0f29de44aaee8f2fcd0f66aaa720b584f7c801e52ce7cd41db45ceb99ebd7b51bef8d0cd2deb5c50b59f168276c9c98d46a1c37bd3d6ef81f2c6e89028680a172e00d92dd8b392135112dd16efab57d00b26b9L
def quadratic(a,b,c):
    ga=gmpy2.mpz(a)
    gb=gmpy2.mpz(b)
    gc=gmpy2.mpz(c)
    delta=gb**2-4*ga*gc
    if delta<=0 or a==0:
        return 0
    tmp=gmpy2.iroot(delta,2)
    if tmp[1]==True:
        x1 = (-gb + tmp[0]) / (2*ga)
        x2 = (-gb - tmp[0]) / (2 * ga)
        if x1>0 and n%x1==0:
            print x1
            return x1
        if x2>0 and n%x2==0:
            print x2
            return x2
    return 0
def main():
    for x in range(1500):
        print x
        for y in range(1500):
            a=y
            b=x*y-m+n
            c=x*n
            if quadratic(a,b,c)!=0:
                return 0
main()