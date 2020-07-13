class Solution:

    def calcuate(self, res, s):
        n = len(s)
        for c in range(n):
            i = j = c
            while i >= 0 and j < n and s[i] == s[j]:
                res[i][j] = True
                i -= 1
                j += 1

        for c in range(n):
            i = c
            j = c + 1
            while i >= 0 and j < n and s[i] == s[j]:
                res[i][j] = True
                i -= 1
                j += 1

    def minCut(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        res = [[False] * n for _ in range(n)]
        self.calcuate(res, s)
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            f[i] = sys.maxsize
            for j in range(i):
                if res[j][i - 1]:
                    f[i] = min(f[i], f[j] + 1)

        return f[n] - 1