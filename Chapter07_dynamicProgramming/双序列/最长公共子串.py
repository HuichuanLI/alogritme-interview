class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        res = [[0] * (len(text2) + 1) for _ in range((len(text1) + 1))]
        for i in range(len(text1) + 1):
            for j in range(len(text2) + 1):
                if i == 0 or j == 0:
                    res[i][j] = 0
                else:
                    res[i][j] = max(res[i - 1][j], res[i][j - 1])
                    if text1[i - 1] == text2[j - 1]:
                        res[i][j] = max(res[i][j], res[i - 1][j - 1] + 1)

        return res[-1][-1]
