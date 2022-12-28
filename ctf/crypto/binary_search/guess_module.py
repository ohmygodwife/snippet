#noise, D^3CTF-2019, https://gist.github.com/Chrstm/f225a5e67f12d20caba117224d1b4241

import random
import socket


class Socket:
    def __init__(self, host, port):
        self.s = socket.socket()
        self.s.connect((host, port))

    def send(self, m, output=True, end=b'\n'):
        if isinstance(m, str):
            m = m.encode('Latin1')
        m += end
        if output:
            print("send:", m)
        self.s.send(m)

    def recv(self, rec_bytes=2048, output=True):
        m = self.s.recv(rec_bytes).decode('Latin1')
        if output:
            print("recv:\n{}\n".format(m))
        return m


NUM_BIT = 1024
NOISE_BIT = 1000
scope = 1 << NOISE_BIT
s = Socket('localhost', 23334)
s.recv()
cnt = 0


def oracle(num, op='god'):
    global cnt
    cnt += 1
    if cnt > 50:
        print("Not very lucky ... try it again")
        exit(0)
    s.send(op)
    s.send(str(num))
    resp = s.recv().strip()
    if op == 'god':
        return int(resp)
    return resp


def check(L, R):
    t = (L - scope - 1) // (R - L)
    I = random.randint(t * R, (t + 1) * L - scope - 1)
    assert (I // L == t)
    assert (I // R == t)
    out = oracle(I)
    LL = I - out
    RR = I - out + scope
    ans_L, ans_R = (LL + t - 1) // t, RR // t #ceil(LL), floor(RR)
    return ans_L, ans_R


L = 0
R = 1 << NUM_BIT
while True:
    if L * 2 >= R + scope + 1:
        break
    mid = (L + R) >> 1
    if oracle(mid) > mid:
        # mid < mid + r < n
        L = mid + 1
    else:
        # n <= mid + r <= mid + scope
        R = min(R, mid + scope)

while L < R:
    try:
        L, R = check(L, R)
    except:
        break

for i in range(L, R + 1):
    if "CONGRATULATIONS" in oracle(i, op='bless'):
        break
print("total:", cnt)
