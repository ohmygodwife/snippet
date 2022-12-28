'''
http://www.soreatu.com/posts/intended-solution-to-crypto-problems-in-nctf-2019
https://zeroyu.xyz/2018/11/02/Cracking-LCG/
'''
# python2
import hashlib
import primefac
from pwn import *
from Crypto.Util.number import *

host, port = '139.129.76.65', 60001
r = remote(host, port)

context.log_level = 'debug'

def proof_of_work():
    print '[+] Proof of work...'
    r.recvuntil('hexdigest() = ')
    digest = r.recvline().strip()
    r.recvuntil("s[:7].encode('hex') =")
    prefix = r.recvline().strip().decode('hex')
    # s = r.recvline().strip()
    for suffix in range(256**3):
        guess = prefix + long_to_bytes(suffix, 3)
        if hashlib.sha256(guess).hexdigest() == digest:
            print '[+] find: ' + guess.encode('hex')
            break
    r.recvuntil("s.encode('hex') = ")
    # r.sendline(s)
    r.sendline(guess.encode('hex'))

def solve1(N, a, b, n1):
    return (n1 - b) * inverse(a, N) % N

def solve2(N, a, n1, n2):
    b = (n2 - n1 * a) % N
    return solve1(N, a, b, n1)

def solve3(N, n1, n2, n3):
    a = (n3 - n2) * inverse(n2 - n1, N) % N
    return solve2(N, a, n1, n2)

def solve4(n1, n2, n3, n4, n5, n6):
    t1 = n2 - n1
    t2 = n3 - n2
    t3 = n4 - n3
    t4 = n5 - n4
    t5 = n6 - n5
    N = GCD(t3*t1 - t2**2, t5*t2 - t4*t3)
    factors = primefac.factorint(N)
    while not isPrime(N):
        for prime, order in factors.items():
            if prime.bit_length() > 128:
                continue
            N = N / prime**order
    return solve3(N, n1, n2, n3)

def challenge1():
    print '[+] Solving challenge1...'
    r.recvuntil('lcg.N = ')
    N = int(r.recvline().strip())
    r.recvuntil('lcg.a = ')
    a = int(r.recvline().strip())
    r.recvuntil('lcg.b = ')
    b = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next1 = int(r.recvline().strip())

    init_seed = solve1(N, a, b, next1)
    r.recvuntil('lcg.seed = ')
    r.sendline(str(init_seed))

def challenge2():
    print '[+] Solving challenge2...'
    r.recvuntil('lcg.N = ')
    N = int(r.recvline().strip())
    r.recvuntil('lcg.a = ')
    a = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next1 = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next2 = int(r.recvline().strip())

    init_seed = solve2(N, a, next1, next2)
    r.recvuntil('lcg.seed = ')
    r.sendline(str(init_seed))

def challenge3():
    print '[+] Solving challenge3...'
    r.recvuntil('lcg.N = ')
    N = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next1 = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next2 = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next3 = int(r.recvline().strip())

    init_seed = solve3(N, next1, next2, next3)
    r.recvuntil('lcg.seed = ')
    r.sendline(str(init_seed))

def challenge4():
    print '[+] Solving challenge4...'
    r.recvuntil('lcg.next() = ')
    next1 = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next2 = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next3 = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next4 = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next5 = int(r.recvline().strip())
    r.recvuntil('lcg.next() = ')
    next6 = int(r.recvline().strip())

    init_seed = solve4(next1, next2, next3, next4, next5, next6)
    r.recvuntil('lcg.seed = ')
    r.sendline(str(init_seed))

proof_of_work()

challenge1()
challenge2()
challenge3()
challenge4()

r.interactive()

'''
import gmpy2

def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment

def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * gmpy2.invert(states[1] - states[0], modulus) % modulus
    return crack_unknown_increment(states, modulus, multiplier)

def crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(gmpy2.gcd, zeroes))
    return crack_unknown_multiplier(states, modulus)

print crack_unknown_modulus([2818206783446335158, 3026581076925130250,
    136214319011561377, 359019108775045580, 2386075359657550866, 1705259547463444505])
'''