#https://196011564.github.io/2018/12/11/CTF-JarvisOJ-Crypto-[61dctf]bbencode/

def bbencode(n):
    a = 0
    for i in bin(n)[2:]:
        a = a << 1
        if (int(i)):
            a = a ^ n
        if a >> 256:
            a = a ^ 0x10000000000000000000000000000000000000000000000000000000000000223L
    return a

result = 61406787709715709430385495960238216763226399960658358000016620560764164045692

for i in range(10000):
    result = bbencode(result)
    if("666c6167" == str(hex(result))[2:10]):
        print i
        print hex(result)[2:-1].decode('hex')