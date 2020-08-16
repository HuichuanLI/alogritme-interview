from collections import defaultdict


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


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF()
        email_to_name = {}
        res = defaultdict(list)
        for acc in accounts:
            for index, email in enumerate(acc[1:]):
                email_to_name[email] = accounts[0]
                if index < len(accounts) - 1:
                    uf.union(accounts[index + 1], accounts[index + 2])
        for key in email_to_name:
            res[uf.find(key)].append(key)
        return [[email_to_name[value[0]]] + sorted(value) for value in res.values()]
