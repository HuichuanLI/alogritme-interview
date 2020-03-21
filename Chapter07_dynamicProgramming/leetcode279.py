import math


# 记忆化搜索
class Solution:
    def numSquares(self, n):
        if n == 1:
            return 1
        self.memo = [-1] * (n + 1)
        self.memo[0] = 0
        self.memo[1] = 1
        return self.divide(n)

    def divide(self, n):
        if self.memo[n] != -1:
            return self.memo[n]
        index = 1
        res = 10000
        while index * index <= n:
            if self.memo[n - index * index] == -1:
                self.memo[n - index * index] = self.divide(n - index * index)
            res = min(res, self.memo[n - index * index] + 1)
            index += 1
        self.memo[n] = res
        return res


# 动态规划
class Solution:
    def numSquares(self, n):
        if n == 1:
            return 1
        self.memo = [-1] * (n + 1)
        self.memo[0] = 0
        self.memo[1] = 1
        for i in range(2, n + 1):
            j = 1
            res = 100000
            while j * j <= i:
                res = min(res, self.memo[i - j * j]+1)
                j += 1
            self.memo[i] = res
        return self.memo[n]