class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if len(envelopes) == 0:
            return 0

        envelopes = sorted(envelopes, key=lambda x: x[0])

        n = len(envelopes)
        res = [0] * n
        for i in range(n):
            res[i] = 1
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    res[i] = max(res[j] + 1, res[i])

        return max(res)
