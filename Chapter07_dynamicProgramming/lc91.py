class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 1
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(1, n + 1):
            f[i] = 0
            if s[i - 1] >= '1' and s[i - 1] <= '9':
                f[i] += f[i - 1]
            if i > 1:
                j = 10 * (int(s[i - 2]) - 0) + (int(s[i - 1]) - 0)
                if j >= 10 and j <= 26:
                    f[i] += f[i - 2]
        return f[n]
