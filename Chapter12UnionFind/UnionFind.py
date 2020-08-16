class UF:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        self.parent.setdefault(x, x)
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, p, q):
        self.parent[self.find(p)] = self.find(q)


