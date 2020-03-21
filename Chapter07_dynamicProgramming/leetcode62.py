class Solution:
    next_step = [[0, 1], [1, 0]]

    def uniquePaths(self, m, n):
        if n == 0 or m == 0:
            return 0
        if n == 1:
            return 1
        return self.countPath(1, 1, n, m)

    def countPath(self, i, j, n, m):
        if i == n and j == m:
            return 1
        res = 0
        for step in self.next_step:
            next_x = i + step[0]
            next_y = j + step[1]
            if next_x <= n and next_y <= m:
                res += self.countPath(next_x, next_y, n, m)
        return res


class Solution:
    next_step = [[0, 1], [1, 0]]

    def uniquePaths(self, m, n):
        if n == 0 or m == 0:
            return 0
        if n == 1:
            return 1
        self.memo = [[-1 for _ in range(m)] for _ in range(n)]
        self.countPath(0, 0, n, m)
        return self.memo[0][0]

    def countPath(self, i, j, n, m):
        if i == n - 1 and j == m - 1:
            return 1

        if self.memo[i][j] != -1:
            return self.memo[i][j]
        res = 0
        for step in self.next_step:
            next_x = i + step[0]
            next_y = j + step[1]
            if next_x <= n - 1 and next_y <= m - 1:
                res += self.countPath(next_x, next_y, n, m)
        self.memo[i][j] = res
        return res


# 动态规划
class Solution:
    def uniquePaths(self, m, n):
        self.memo = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                self.memo[i][j] = self.memo[i-1][j] + self.memo[i][j-1]
        return self.memo[n-1][m-1]