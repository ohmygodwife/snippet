from pwn import *
#context.log_level = 'debug'
import hashlib

i = 0
array= {}
while True:
  value = hashlib.md5(str(i)).hexdigest()[-6:]
  array[value] = str(i)
  i += 1
  if i > 10000000:
   break

print "start"

def getMd5Remote():
  while True:
    p = remote('106.75.73.28', 20000)
    #Submit a printable string X, such that md5(X)[-6:] = b9c418
    p.recvuntil('such that ')
    method = p.recvuntil('(', drop=True)
    if cmp("md5", method) == 0:
      return p
    p.close()

while True:      
  p = getMd5Remote()
  p.recvuntil('= ')
  data = p.recvuntil('\n', drop=True)
  print data
  if array.has_key(data):
    p.sendline(array[data])
    break

print p.recv()
p.interactive()
