import sys


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        if k == 1:
            return costs[0][0]
        f = [[0] * k for _ in range(n + 1)]
        min1, min2 = sys.maxsize, sys.maxsize
        id1, id2 = 0, 0
        for i in range(1, n + 1):
            min1 = min2 = sys.maxsize
            for j in range(k):
                if f[i - 1][j] < min1:
                    min2 = min1
                    id2 = id1
                    min1 = f[i - 1][j]
                    id1 = j
                elif f[i - 1][j] < min2:
                    min2 = f[i - 1][j]
                    id2 = j

            print(min1, min2, id1, id2)

            for j in range(k):
                f[i][j] = costs[i - 1][j]
                if j != id1:
                    f[i][j] += min1
                else:
                    f[i][j] += min2

        res = sys.maxsize
        for i in range(k):
            res = min(res, f[n][i])

        return res
