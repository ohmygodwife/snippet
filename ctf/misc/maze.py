#maze, 201226zongheng
#https://blog.csdn.net/qq_29681777/article/details/83719680

from pwn import *

sh = remote("182.92.203.154", 11001)

def Search(x, y):
    global route
    for i in range(4):
        currentX, currentY = x + vct[i][0], y + vct[i][1]
    if mz_map[currentX][currentY] == '$':
        tmp.append(i)
        route = tmp[::]
        return
    if mz_map[currentX][currentY] == ' ' and mine[currentX][currentY] == 0:
        tmp.append(i)
        mine[currentX][currentY] = 1
        Search(currentX, currentY)
        mine[currentX][currentY] = 0
        tmp.pop()

dire = ['a', 's', 'd', 'w']
vct = [[0,-1],[1,0],[0,1],[-1,0]]

sh.sendafter('start.', '\n')
for line_num in range(1, 6):
    if line_num != 1:
        sh.recvuntil('win\n')
    tmp, route = [],[]
    mine = [[0 for i in range(150)] for i in range(100)]
    mz_map = sh.readlines(line_num*10+1)
    Search(1, 1)
    for i in route:
        sh.sendline(dire[i])

sh.interactive()