class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: x[0])
        res = [0] * len(envelopes)
        n = len(envelopes)
        if n == 0:
            return 0
        res[0] = 1
        for i in range(n):
            res[i] = 1
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1] and envelopes[j][0] < envelopes[i][0]:
                    res[i] = max(res[i], res[j] + 1)
        return max(res)
