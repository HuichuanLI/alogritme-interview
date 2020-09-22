class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m, A, V):
        # write your code here
        n = len(A)
        res = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(1, m + 1):
                if i == 0 or j == 0:
                    res[i][j] = 0
                elif A[i - 1] <= j:
                    res[i][j] = max(res[i - 1][j], res[i - 1][j - A[i - 1]] + V[i - 1])
                else:
                    res[i][j] = res[i - 1][j]
        return res[n][m]
