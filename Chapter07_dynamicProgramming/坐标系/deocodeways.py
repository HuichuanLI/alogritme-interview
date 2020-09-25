class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """

    def numDecodings(self, s):
        n = len(s)
        MOD = 1000000007
        if n == 0 or s[0] == '0':
            return 0
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        if s[0] == '*':
            dp[1] = 9
        for i in range(2, n + 1):
            if s[i - 1] == '0':
                if s[i - 2] == '1' or s[i - 2] == '2':
                    dp[i] += dp[i - 2]
                elif s[i - 2] == '*':
                    dp[i] += 2 * dp[i - 2]
                else:
                    return 0
            elif s[i - 1] >= '1' and s[i - 1] <= '9':
                dp[i] += dp[i - 1]
                if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6'):
                    dp[i] += dp[i - 2]
                elif s[i - 2] == '*':
                    if s[i - 1] <= '6':
                        dp[i] += 2 * dp[i - 2]
                    else:
                        dp[i] += dp[i - 2]
            else:  # s[i - 1] == '*'
                dp[i] += 9 * dp[i - 1]
                if s[i - 2] == '1':
                    dp[i] += 9 * dp[i - 2]
                elif s[i - 2] == '2':
                    dp[i] += 6 * dp[i - 2]
                elif s[i - 2] == '*':
                    dp[i] += 15 * dp[i - 2]
            dp[i] %= MOD
        return dp[n]
