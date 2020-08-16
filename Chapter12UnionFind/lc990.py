class UF:
    def __init__(self):
        self.parent = {}

    def find(self, p):
        self.parent.setdefault(p, p)
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def union(self, p, q):
        self.parent[self.find(p)] = self.find(q)

    def change(self,p,q):
        self.parent.setdefault(p, p)
        self.parent.setdefault(q, q)

        return self.find(p) == self.find(q)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF()
        equations_all = [elem for elem in equations if "==" in elem]
        equations_not = [elem for elem in equations if "!=" in elem]

        for elem in equations_all:
            v1, v2 = elem.split("==")
            uf.union(v1, v2)
        for elem in equations_not:
            v1, v2 = elem.split("!=")
            if uf.change(v1, v2):
                return False
        return True
