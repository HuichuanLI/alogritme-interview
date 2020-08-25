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
            res[i][0] = 0
            for j in range(1, m + 1):
                res[i][j] = res[i - 1][j]
                if 0 <= j - A[i - 1]:
                    res[i][j] = max(res[i][j], res[i - 1][j - A[i - 1]] + V[i - 1])
        return max(res[n])
