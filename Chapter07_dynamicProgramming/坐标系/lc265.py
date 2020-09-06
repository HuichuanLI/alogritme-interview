import sys


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        if n == 1:
            return min(costs[0])
        k = len(costs[0])

        if n == 0:
            return 0
        f = [[0] * k for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(k):
                f[i][j] = sys.maxsize
                for m in range(k):
                    if j != m:
                        f[i][j] = min(f[i][j], f[i - 1][m] + costs[i - 1][j])
        return min(f[-1])
