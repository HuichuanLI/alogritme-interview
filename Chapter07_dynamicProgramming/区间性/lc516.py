class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """

    def longestPalindromeSubseq(self, s):
        size = len(s)
        if size <= 1:
            return size
        dp = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            dp[i][i] = 1
        for i in range(size - 1, -1, -1):
            for j in range(i + 1, size):
                if s[i] == s[j]:  # s[i]==s[j]时的转移方程
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:  # s[i]！=s[j]时的转移方程
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][size - 1]  # 最后结果在dp[0][size - 1]中
