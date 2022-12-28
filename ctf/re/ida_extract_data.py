'''https://blog.csdn.net/LoopherBear/article/details/87198647
mnemonic=idc.GetMnem(addr) #imul
op1=idc.GetOpnd(addr,0) #eax
type=idc.GetOpType(addr,0) == ida_ua.o_imm #0:o_void;1:o_reg;2:o_mem;5:o_imm
value=idc.GetOperandValue(addr,0) #0
'''


addr = 0x11c7
end_addr = 0x4963c

coefficient = []
result = []

while(addr <= end_addr):
  mnemonic=idc.GetMnem(addr)
  if mnemonic == 'imul':
    coefficient.append(idc.GetOperandValue(addr,2))
  elif mnemonic == 'cmp':
    result.append(idc.GetOperandValue(addr,1))
  addr = idc.NextHead(addr)
    
print coefficient
print result
