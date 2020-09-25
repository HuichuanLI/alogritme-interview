class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        t = len(strs)
        dp = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(2)]

        for index in range(1, t + 1):
            zero = 0
            one = 0
            for ch in strs[index - 1]:
                if ch == "1":
                    one += 1
                else:
                    zero += 1
            for i in range(n + 1):
                for j in range(m + 1):
                    dp[index % 2][i][j] = dp[(index - 1) % 2][i][j]
                    if i >= one and j >= zero:
                        dp[index % 2][i][j] = max(dp[index % 2][i][j], dp[(index - 1) % 2][i - one][j - zero] + 1)

        return dp[t % 2][-1][-1]
