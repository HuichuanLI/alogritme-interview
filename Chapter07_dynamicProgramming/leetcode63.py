class Solution:
    next_step = [[0, 1], [1, 0]]

    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if n == 0 or m == 0:
            return 0

        self.memo = [[-1 for _ in range(m)] for _ in range(n)]
        return self.countPath(0, 0, n, m, obstacleGrid)

    def countPath(self, i, j, n, m, obstacleGrid):
        if obstacleGrid[i][j] == 1:
            return 0

        if i == n - 1 and j == m - 1:
            return 1

        if self.memo[i][j] != -1:
            return self.memo[i][j]
        res = 0
        for step in self.next_step:
            next_x = i + step[0]
            next_y = j + step[1]
            if next_x <= n - 1 and next_y <= m - 1:
                res += self.countPath(next_x, next_y, n, m, obstacleGrid)
        self.memo[i][j] = res
        return res
