# 递归解法
class Solution:
    def climbStairs(self, n):
        if n == 1 or n == 0:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# 记忆化搜索
class Solution:
    def climbStairs(self, n):
        if n == 1 or n == 0:
            return 1
        res = [0] * (n + 1)
        res[0] = 1
        res[1] = 1

        self._climbStairs(n, res)
        return res[n]

    def _climbStairs(self, n, res):
        if res[n] == 0:
            res[n] = self._climbStairs(n - 1, res) + self._climbStairs(n - 2, res)
        return res[n]


# 动态规划
class Solution:
    def climbStairs(self, n):
        if n == 1 or n == 0:
            return 1
        res = [0] * (n + 1)
        res[0] = 1
        res[1] = 1

        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]
        return res[n]
