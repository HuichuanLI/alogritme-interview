class Solution(object):
    # DP
    def isMatch(self, s, p):
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == "*":
                dp[0][i] = dp[0][i - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[-1][-1]
