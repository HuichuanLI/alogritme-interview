class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """

    def kSum(self, A, k, target):
        # write your code here
        res = [[[0] * (target + 1) for _ in range(k + 1)] for _ in range(len(A) + 1)]
        res[0][0][0] = 1
        for i in range(1, len(A) + 1):
            res[i][0][0] = 1
            for j in range(1, k + 1):

                for t in range(1, target + 1):
                    res[i][j][k] = res[i - 1][j - 1][k]
                    if t >= A[i - 1] and j >= 1:
                        res[i][j][k] = res[i][j][k] + res[i - 1][j - 1][k - A[i - 1]]

        return res[-1][-1][-1]
