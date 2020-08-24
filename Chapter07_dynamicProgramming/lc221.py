class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """

    def maxSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])

        # intialization
        f = [[0] * m for _ in range(n)]
        for i in range(m):
            f[0][i] = matrix[0][i]

        edge = max(matrix[0])
        for i in range(1, n):
            f[i][0] = matrix[i][0]
            for j in range(1, m):
                if matrix[i][j]:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
                else:
                    f[i][j] = 0
            edge = max(edge, max(f[i]))

        return edge * edge
