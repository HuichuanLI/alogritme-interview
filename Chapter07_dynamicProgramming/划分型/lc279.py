class Solution:
    def numSquares(self, n: int) -> int:
        res = [sys.maxsize] * (n + 1)
        res[0] = 0
        res[1] = 1
        for i in range(2, n + 1):
            j = 1
            while i - j * j >= 0:
                res[i] = min(res[i - j * j] + 1, res[i])
                j += 1
        return res[-1]
