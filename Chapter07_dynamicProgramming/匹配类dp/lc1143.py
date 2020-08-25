class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """

    def longestCommonSubsequence(self, A, B):
        if not A or not B:
            return 0

        n, m = len(A), len(B)
        # state & initialization
        dp = [[0] * (m + 1) for i in range(n + 1)]

        # function
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

        # answer
        return dp[n][m]
