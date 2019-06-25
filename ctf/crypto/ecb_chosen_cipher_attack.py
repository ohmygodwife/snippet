'''https://blog.csdn.net/u014549283/article/details/81486284
2.enc = encrypt(test+flag)
Enter the information you want to encrypt:
aaaaaaaaaaaaaaaa
--->0f6008039cd1ddd548f04cea4b599380cdc148b622432eb5a2e57ecece121413a8fe056413730670bb5eb4d21ac11e156266c110db031479820defcf44dfc7e3<---
3.enc = encrypt(test)
Enter the information you want to encrypt:
aaaaaaaaaaaaaaaa
--->0f6008039cd1ddd548f04cea4b599380<---
'''
from pwn import *
#context.log_level = 'debug'

p = remote('101.71.29.5', 10014)

def menu(index, content):
  p.recvuntil('3) test\n', drop=True)
  p.sendline(str(index))
  p.recvuntil('encrypt:\n', drop=True)
  p.sendline(content)
  p.recvuntil('--->', drop=True)
  data = p.recvuntil('<---', drop=True)
  return data

all = string.ascii_letters + string.digits + '{}'
ret = ''
for i in range(16 * 3):
  prefix = 'a' * (16 * 3 - 1 - i)
  print prefix
  target = menu(2, prefix)
  for ch in all:
    data = menu(3, prefix + ret + ch)
    if target.startswith(data):
      print ch
      ret += ch
      
print ret

''' from end to start
#all = string.digits + 'abcdeflg{}'
flag = ''
for i in range(11,49): #padding with '0'*11, so here start from 11
  tmp = menu(2, '0'*i)
  tt = tmp[96:]
  for ch in all:
    tmp2 = menu(3, ch+flag)
    if tt = tmp2:
      flag = ch + flag
      print flag
      break
'''