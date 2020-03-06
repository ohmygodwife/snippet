#flodbg-dfjkctf-2019, http://url.cn/5n9YZrX

from ida_bytes import get_bytes,patch_bytes
import re
addr = 0x400000
end = 0x402000

buf = get_bytes(addr, end-addr)

def handler(s):
  s = s.group(0)
  s = "\x90"*len(s)
  return s
  
patterns = [
r"\xE8\x00\x00\x00\x00\x5B\x48\x83\xC3\x0A\xFF\xE3\xEB\xEB\xEB", #call $+5 pop rbx
r"\xE8\x00\x00\x00\x00\x58\x48\x83\xC0\x0C\xFF\xE0\xEB\xEB\xEB\xEB\xEB", #call $+5 pop rax
r"\xE8\x00\x00\x00\x00\x58\x48\x83\xC0\x0A\xFF\xE0\xEB\xEB\xEB",
r"\xEB\xFF\xC0\xFF\xC8",
r"\x66\xB8\xEB\x05\x31\xC0\x74\xFA\xEB"
]

for p in patterns:
  buf = re.sub(p, handler, buf, flags=re.I)
  
patch_bytes(addr, buf)