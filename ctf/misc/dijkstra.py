#https://www.cnblogs.com/P201521440001/p/11415504.html
#https://blog.csdn.net/imotolove/article/details/80633006
#https://blog.csdn.net/anlian523/article/details/80893372
#https://blog.csdn.net/AivenZhong/article/details/84385736
import heapq

class Node:
  def __init__(self, cur):
    self.cur = cur
    self.edges = {}
    self.parent = None
    self.distance = None
    self.is_visited = False
    
  def __lt__(self, other): # for heapq, not used here!
    return self.distance < other.distance
    
  def __str__(self):
    s = '['
    for end, edge in self.edges.items():
      s += end + str(edge)
    s += ']'
    return '({}, {}, {}, {})'.format(self.cur, s, self.parent, self.distance)

  def add_edge(self, end, edge):
    self.edges[end] = edge

class Edge:
  def __init__(self, weight, data):
    self.weight = int(weight)
    self.data = data
    
  def __str__(self):
    return '<{}, {}>'.format(self.weight, self.data)

def dijkstra(node_dict, start):
  heap = []
  start_node = node_dict[start]
  start_node.parent = start
  start_node.distance = 0
  heapq.heappush(heap, start_node)
  while heap:
    top = heapq.heappop(heap)
    #same node would be put into heap many times when distance is updated, need to verify parent
    if top.is_visited:
      continue
    
    for end, edge in top.edges.items():
      end_node = node_dict[end]
      v = top.distance + edge.weight
      #update distance, like DP
      if end_node.distance is None or v < end_node.distance:
        end_node.parent = top.cur
        end_node.distance = v
        heapq.heappush(heap, end_node) #same node would be put into heap many times, but the small ONE would stay first
        print end_node

def add_node(node_dict, start, end, edge):
  if start not in node_dict:
    node = Node(start)
    node_dict[start] = node
  else:
    node = node_dict[start]
  node.add_edge(end, edge)

def show(node_dict):
  for key, node in node_dict.items():
    print node

def init():
  node_dict = {}  # {start: [nodelist]}
  with open('dijkstra.txt', 'r') as f:
    for line in f:
      arr = line.strip().split(' ')
      if len(arr) < 4:
        continue

      add_node(node_dict, arr[0], arr[1], Edge(arr[2], arr[3]))
      #undirected graph would also need to add end -> start
      add_node(node_dict, arr[1], arr[0], Edge(arr[2], arr[3]))
  return node_dict

node_dict = init()
show(node_dict)
print '==================='
start = '1'
dijkstra(node_dict, start)
print '==================='
show(node_dict)
print '==================='
i = '26'
flag = ''
while i != start:
  node = node_dict[i]
  edge = node_dict[node.parent].edges[i]
  flag += edge.data[::-1]
  print i, node.parent, flag
  i = node.parent
  
print flag[::-1]
#FLAG{WEIVKASJVLSJCHFSJVHJSDEV}