class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for j in range(1, n):
            dp[j][0] = dp[j - 1][0] + grid[j][0]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[n - 1][m - 1]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(2)]
        old = now = 1
        for i in range(n):
            old = now
            now = 1 - old

            for j in range(m):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                    continue
                t = sys.maxsize
                if i > 0:
                    t = min(t, dp[old][j])
                if j > 0:
                    t = min(t, dp[now][j - 1])
                dp[now][j] = t + grid[i][j]

        return dp[now][m - 1]