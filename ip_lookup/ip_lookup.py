#python3
QQWRY_DAT = 'D:\soft\cz88.net\ip\qqwry.dat'

from qqwry import QQwry

q = QQwry()
q.load_file(QQWRY_DAT)
result = q.lookup('8.8.8.8')
print(result)