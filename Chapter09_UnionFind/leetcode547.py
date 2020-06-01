# QuickUnion
class UF1:
    def __init__(self, n):
        self.uf = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def Union(self, a, b):
        proot = self.Find(a)
        qroot = self.Find(b)
        if proot == qroot:
            return
        if self.size[proot] < self.size[qroot]:
            self.uf[proot] = qroot
            self.size[qroot] += self.size[proot]
        else:
            self.uf[qroot] = proot
            self.size[proot] += self.size[qroot]

    def Find(self, a):
        while self.uf[a] != a:
            a = self.uf[a]
        return a

    def isConnected(self, a, b):
        return self.Find(a) == self.Find(b)


class UF:
    def __init__(self, n):
        self.uf = [i for i in range(n)]

    def Union(self, a, b):
        if self.uf[a] == self.uf[b]:
            return
        cur = self.uf[a]
        for index, elem in enumerate(self.uf):
            if elem == cur:
                self.uf[index] = self.uf[b]
        return

    def Find(self, a):
        return self.uf[a]

    def isConnected(self, a, b):
        return self.Find(a) == self.Find(b)


class Solution:
    def findCircleNum(self, M):
        n = len(M)
        self.uf = UF(n)
        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    self.uf.Union(i, j)
        return len(set(self.uf.uf))