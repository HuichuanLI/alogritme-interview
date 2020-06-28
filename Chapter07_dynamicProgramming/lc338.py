class Solution:
    def countBits(self, num: int) -> List[int]:
        f = [0] * (num + 1)
        for i in range(1, num + 1):
            f[i] = f[i >> 1] + (i % 2)
        return f
