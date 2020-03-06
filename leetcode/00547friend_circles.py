M = [[1,1,0],
 [1,1,0],
 [0,0,1]]

class UnionFind:
    parent = {}
    size = {}
    cnt = 0
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.cnt = len(M)
        for i in range(self.cnt):
            self.parent[i] = i
            self.size[i] = 1
        
        n = len(M)
        for i in range(n - 1):
            for j in range(i+1, n):
                if (M[i][j] == 1):
                    self.union(i, j)
                    
        return self.cnt

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
            self.parent[x] = self.parent[self.parent[x]]
        return x
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if (root_p == root_q):
            return
        if self.size[root_p] < self.size[root_q]:
            self.parent[root_p] = root_q
            self.size[root_q] +=self.size[root_p]
        else:
            self.parent[root_q] = root_p
            self.size[root_p] +=self.size[root_q]
        self.cnt -= 1
    def connected(self, p, q):
        return self.find(p) == self.find(q)

uf = UnionFind()
print uf.findCircleNum(M)