from zio import *
import string
import random
import hashlib

def passpow(io,difficulty):
  io.read_until("[+] sha256(")
  prefix=io.read_until("+")[:-1]
  while 1:
    answer=''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
    hashresult=hashlib.sha256(prefix+answer).digest()
    bits=''.join(bin(ord(j))[2:].zfill(8) for j in hashresult)
    if bits.startswith('0'*difficulty):
      io.read_until("=")
      io.writeline(answer)
      return

ip = '139.224.254.172'
target=(ip,7777)
io = zio(target, timeout=10000, print_read=COLORED(RAW,'red'), print_write=COLORED(RAW,'green'))
passpow(io,5)
io.interact()