#https://mp.weixin.qq.com/s/1TcCCBV8noAhahupI1Xi2Q
import marshal
import dis
f = open('py.pyc', 'rb')
f.read(8)
code = marshal.load(f)

print code.co_consts
print code.co_names

count = code.co_consts[6]
print count.co_varnames
print count.co_consts

dis.disassemble_string(count.co_code)