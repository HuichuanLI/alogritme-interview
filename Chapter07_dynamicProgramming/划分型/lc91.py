class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        n = len(s)
        res = [0] * (n + 1)
        res[0] = 1
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                res[i] = res[i - 1]
            if i > 1 and int(s[i - 2:i]) >= 10 and int(s[i - 2:i]) <= 26:
                res[i] += res[i - 2]
        return res[-1]
