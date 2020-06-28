class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        res = [0] * (n + 1)
        res[0] = 0
        res[1] = nums[0]
        res[2] = max(nums[1], nums[0])
        for i in range(3, n + 1):
            res[i] = max(res[i - 1], res[i - 2] + nums[i-1])
        return res[n]
