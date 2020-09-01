class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        n = len(matrix)

        m = len(matrix[0])

        result = 0

        # 求出前缀和数组

        pre = [[0 for i in range(m + 1)] for j in range(n + 1)]

        pre[1][1] = matrix[0][0]

        for i in range(2, n + 1):
            pre[i][1] = pre[i - 1][1] + matrix[i - 1][0]

        for i in range(2, m + 1):
            pre[1][i] = pre[1][i - 1] + matrix[0][i - 1]

        for i in range(2, n + 1):

            for j in range(2, m + 1):
                pre[i][j] = pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1] + matrix[i - 1][j - 1]

        # 枚举左上角

        for x1 in range(1, n + 1):

            for y1 in range(1, m + 1):

                # 枚举右下角

                for x2 in range(x1, n + 1):

                    for y2 in range(y1, m + 1):

                        # 若矩阵和为0，则返回

                        if pre[x2][y2] - pre[x1 - 1][y2] - pre[x2][y1 - 1] + pre[x1 - 1][y1 - 1] == target:
                            result += 1

        return  result
