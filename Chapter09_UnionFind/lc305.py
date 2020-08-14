class UF:
    def __init__(self, capacity):
        self.uf = [i for i in range(capacity)]

    def union(self, p, q):
        p_parent = self.uf[p]
        q_parent = self.uf[q]
        for i in range(len(self.uf)):
            if self.uf[i] == p_parent:
                self.uf[i] = q_parent

    def find(self, p, q):
        return self.uf[p] == self.uf[q]


class Solution:
    step = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        Uf = UF(m * n)
        cnt = 0
        res = []
        for elem in positions:
            cnt += 1
            Uf.uf[m * elem[0] + elem[1]] = 0
            for m_step in self.step:
                next_x = elem[0] + m_step[0]
                next_y = elem[1] + m_step[1]
                if next_x >=0 and next_x < n and next_y >=0 and next_y <m:
                    if Uf.find(next_x*m+next_y,elem[0]*m+elem[1]):
                        cnt-=1
            res.append(cnt)
        return  res