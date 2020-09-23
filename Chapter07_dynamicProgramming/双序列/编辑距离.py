class Solution:
    def minDistance(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        res = [[0] * (n1 + 1) for i in range(n2 + 1)]
        for i in range(n1 + 1):
            res[0][i] = i
        for j in range(n2 + 1):
            res[j][0] = j

        for j in range(1, n1 + 1):
            for i in range(1, n2 + 1):
                if s[j - 1] == t[i - 1]:
                    res[i][j] = res[i - 1][j - 1]
                else:
                    res[i][j] = min(res[i - 1][j - 1], res[i][j - 1], res[i - 1][j]) + 1
        return res[-1][-1]
