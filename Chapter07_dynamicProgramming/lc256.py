class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        f = [[0] * 3 for _ in range(n+1)]
        for i in range(1, n + 1):
            for j in range(3):
                f[i][j] = sys.maxsize
                for k in range(3):
                    if j != k:
                        f[i][j] = min(f[i][j], f[i - 1][k] + costs[i-1][j])

        return min(f[len(costs)][0], min(f[len(costs)][1], f[len(costs)][2]))
