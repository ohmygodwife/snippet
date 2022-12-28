from pwn import *
#context.log_level = 'debug'
import hashlib
import itertools, string

table = string.ascii_letters + string.digits
print table

def proof(p):
  p.recvuntil("b'[+] sha256(XXXX+")
  suffix=p.recvuntil(') == ', drop=True)
  target=p.recvuntil("'\n[+] Plz Tell Me XXXX :", drop=True)
  print(suffix, target)
  for i in itertools.product(table, repeat = 4):
    x = ''.join(i)
    if str(hashlib.sha256(x + suffix).hexdigest()) == target:
        p.sendline(x)
        return

p = remote('node4.buuoj.cn', 25084)
proof(p)
print p.recv()
p.interactive()