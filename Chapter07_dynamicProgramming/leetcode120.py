# 递归
class Solution:
    def minimumTotal(self, triangle):
        res = []
        if not triangle:
            return 0
        self._minimumTotal(0, 0, triangle, 0, res)
        return min(res)

    def _minimumTotal(self, i, j, triangle, sum, res):
        if i == len(triangle) - 1:
            res.append(sum + triangle[i][j])
            return
        self._minimumTotal(i + 1, j, triangle, sum + triangle[i][j], res)
        self._minimumTotal(i + 1, j + 1, triangle, sum + triangle[i][j], res)
        return


# 记忆化搜索
class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        res = [[-1 for _ in range(i + 1)] for i in range(len(triangle))]
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            res[i][0] = res[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                res[i][j] = min(res[i - 1][j], res[i - 1], [j - 1]) + triangle[i][j]
            res[i][j] = res[i - 1][j - 1] + triangle[i][j]

        return min(res[len(triangle) - 1])


# 动态规划
class Solution:
    def minimumTotal(self, triangle):
        if not triangle or not triangle[0]:
            return 0
        res = [[0 for _ in range(i + 1)] for i in range(len(triangle))]
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            res[i][0] = res[i - 1][0] + triangle[i][0]
            res[i][i] = res[i - 1][i - 1] + triangle[i][i]
        for i in range(1, len(triangle)):
            for j in range(1, i):
                res[i][j] = min(res[i - 1][j], res[i - 1][j - 1]) + triangle[i][j]
        return min(res[len(triangle)-1])

