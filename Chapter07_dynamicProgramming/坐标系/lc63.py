class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0

        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    res[0][0] = 1
                    continue
                if i == 0 and j > 0:
                    res[i][j] = res[i][j - 1]
                elif j == 0 and i > 0:
                    res[i][j] = res[i - 1][j]
                else:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]
        return res[m - 1][n - 1]
