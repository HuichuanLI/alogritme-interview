class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        f = [0] * n
        g = [0] * n
        for i in range(n):
            f[i] = nums[i]
            if i > 0:
                f[i] = max(f[i], max(nums[i] * f[i - 1], nums[i] * g[i - 1]))

            g[i] = nums[i]
            if i > 0:
                g[i] = min(g[i], min(nums[i] * f[i - 1], nums[i] * g[i - 1]))

            res = max(res, f[i])

        return  res
