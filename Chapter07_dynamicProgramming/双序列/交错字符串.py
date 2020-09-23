class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        res = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        res[0][0] = True
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if j > 0 and s3[i + j - 1] == s2[j - 1]:
                    res[i][j] = res[i][j - 1] or res[i][j]

                if i > 0 and s3[i + j - 1] == s1[i - 1]:
                    res[i][j] = res[i - 1][j] or res[i][j]

        return res[-1][-1]
