#dancing circle: https://bbs.pediy.com/thread-250243.htm
from ida_bytes import get_bytes, patch_bytes
 
addr = 0x401000
buf = get_bytes(addr, 0x4B9CD0-addr)
def patch_at(p, ln):
    global buf
    buf = buf[:p] + "\x90" * ln + buf[p+ln:]
 
# jx / jnx
fake_jcc = []
for opcode in xrange(0x70, 0x7F, 2):
    pattern = chr(opcode) + "\x03" + chr(opcode | 1) + "\x01"
    fake_jcc.append(pattern)
    pattern = chr(opcode | 1) + "\x03" + chr(opcode) + "\x01"
    fake_jcc.append(pattern)
 
for pattern in fake_jcc:
    p = buf.find(pattern)
    while p != -1:
        patch_at(p, 5)
        p = buf.find(pattern, p+1)
 
# call / pop
pattern = '\xE8'
p = buf.find(pattern)
while p != -1:
    if buf[p + 2:p + 5] == '\x00\x00\x00':
        dst = p + 5 + ord(buf[p + 1])
        if buf[dst:dst + 3] == '\x83\xC4\x04':
            ln = dst - p + 3
            patch_at(p, ln)
        elif buf[dst] == '\x58':
            ln = dst - p + 1
            if buf[p - 1] == '\x50' and buf[dst + 1] == '\x58':
                patch_at(p - 1, ln + 2)
            else:
                patch_at(p, ln)
        elif buf[dst:dst + 5] == '\x83\x04\x24\x06\xc3':
            ln = dst - p + 5
            patch_at(p, ln)
        else:
            print("E80n", hex(p + addr), hex(dst + addr), buf[dst:dst + 3].encode('hex'))
    else:
        pass
    p = buf.find(pattern, p+1)
 
# stx / jx
fake_jcc = ['\xF8\x73', '\xF9\x72']
for pattern in fake_jcc:
    p = buf.find(pattern)
    while p != -1:
        if ord(buf[p + 2]) < 0x80:
            dst = p + 3 + ord(buf[p + 2])
            ln = dst - p
            patch_at(p, ln)
        else:
            print("CLC", hex(p + addr))
        p = buf.find(pattern, p+1)
 
fake_jcc = ['\x7C\x03\xEB\x03']
for pattern in fake_jcc:
    p = buf.find(pattern)
    while p != -1:
        if buf[p + 5:p + 5 + 2] == '\x74\xFB':
            ln = 7
            patch_at(p, ln)
        else:
            print("CLC", hex(p + addr))
        p = buf.find(pattern, p+1)
 
patch_bytes(addr, buf)
print('done')