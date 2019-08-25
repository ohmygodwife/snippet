n = 3
m = 1

direction = [(-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2)]
#done = {(x, y):False for x in range(0,n+1) for y in range(0, m+1)}
#done[(0, 0)] = True
done = set([(0, 0)])
todo = [(0, 0, 0)]

def bfs():
  while len(todo):
    cur = todo.pop(0)
    for d in direction:
      x = cur[0] + d[0]
      y = cur[1] + d[1]
      if x < 0 or x > n or y < 0 or y > m:
        continue
      if (x,y) in done:
        continue
      if x == n and y == m:
        print cur[2] + 1
        return
      done.add((x,y))
      todo.append((x, y, cur[2]+1))
  print -1

bfs()