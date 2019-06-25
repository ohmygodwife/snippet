from pwn import *
context.log_level = 'debug'
import hashlib

def proof(p):
  p.recvuntil('Please find a string whose SHA256 starts with "')
  data=p.recvuntil('"', drop=True)
  i = 0
  while True:
    value = hashlib.sha256(str(i)).hexdigest()
    if value.startswith(data):
      p.sendline(str(i))
      return
    i += 1

p = remote('49.4.79.193', 30619)
proof(p)
print p.recv()
p.interactive()
