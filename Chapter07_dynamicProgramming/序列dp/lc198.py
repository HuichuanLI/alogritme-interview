class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        # 前i个房子能偷的房子
        res = [0] * (n + 1)
        # 没有房子
        res[0] = 0
        res[1] = nums[0]
        for i in range(2, n + 1):
            res[i] = max(res[i - 1], res[i - 2] + nums[i - 1])
        return res[-1]
