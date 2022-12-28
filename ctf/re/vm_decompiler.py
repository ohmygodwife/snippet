#https://panda0s.top/2021/08/24/LightningSystem/
import ctypes

#data_code = binascii.a2b_hex(data2)
data_code = '0300aa0301b0010005000104000104040000f303000203012c020005000104000104040000f3'.decode('hex')
data_code = map(ord, data_code)
print data_code
#print(data_code.encode('hex'))

def gen(pc, ins_text):
    return "_0x%x: %s;" % (pc, ins_text)

def decompiler(data):
    pc = 0
    while pc < len(data):
        opcode = (data[pc])
        op1 = (data[pc + 1])
        op2 = (data[pc + 2])
        op3 = (data[pc + 3])
        asm_text = gen(pc, "Undefine")
        if opcode == 0:
            asm_text = gen(pc, "nop")
            pc += 1
        elif opcode == 1:
            asm_text = gen(pc, "putchar(mem[mem[0x%x]])" % op1)
            pc += 2
        elif opcode == 2:
            asm_text = gen(pc, "mem[mem[0x%x]] = getchar()" % op1)
            pc += 2
        elif opcode == 3:
            asm_text = gen(pc, "mem[0x%x] = 0x%x" % (op1, op2))
            pc += 3
        elif opcode == 4:
            asm_text = gen(pc, "if(mem[0x%x] == mem[0x%x]) goto _0x%x" % (op1, op2, pc + ctypes.c_int8(op3).value + 4))
            pc += 4
        elif opcode == 5:
            asm_text = gen(pc, "mem[0x%x] += 0x%x" % (op1, op2))
            pc += 3
        elif opcode == 6:
           asm_text = gen(pc, "mem2[0x%x] = ror(mem2[0x%x], 0x%x)" % (op1, op1, op2))
           pc += 3
        elif opcode == 7:
            asm_text = gen(pc, "mem2[0x%x] = mem[mem[0x%x]]" % (op1, op2))
            pc += 3
        elif opcode == 8:
            asm_text = gen(pc, "mem2[0x%x] += mem2[0x%x]" % (op1, op2))
            pc += 3
        elif opcode == 9:
            asm_text = gen(pc, "mem[0x%x] = mem[0x%x]" % (op1, op2))
            pc += 3
        elif opcode == 10:
            asm_text = gen(pc, "mem[0x%x] *= 0x%x" % (op1, op2))
            pc += 3
        elif opcode == 11:
            asm_text = gen(pc, "mem2[0x%x] -= mem2[0x%x]" % (op1, op2))
            pc += 3
        elif opcode == 12:
            if ctypes.c_int8(op2).value < 0:
                asm_text = gen(pc, "mem2[0x%x] <<= 0x%x" % (op1, 0x100 - op2)) #negative  7
            else:
                asm_text = gen(pc, "mem2[0x%x] >>= 0x%x" % (op1, op2)) #negative
            pc += 3
        elif opcode == 13:
            asm_text = gen(pc, "mem2[0x%x] ^= 0x%x" % (op1, op2))
            pc += 3
        elif opcode == 14:
            asm_text = gen(pc, "mem2[0x%x] *= 0x%x" % (op1, op2))
            pc += 3
        elif opcode == 15:
            asm_text = gen(pc, "mem2[mem[0x%x]] = mem2[0x%x]" % (op1, op2))
            pc += 3
        elif opcode == 16:
            asm_text = gen(pc, "mem[0x%x] = mem[mem[0x%x]]" % (op1, op2))
            pc += 3
        elif opcode == 0xff:
            return
        else:
            print("Undefine: 0x%x opcode:%d" % (pc, opcode))
            raise
        print(asm_text)

decompiler(data_code)
#result compile as c, then disasm by IDA