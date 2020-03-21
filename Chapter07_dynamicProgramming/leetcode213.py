class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        return max(self.combination(nums[1:]), self.combination(nums[:-1]))

    def combination(self, nums):
        if len(nums) == 2:
            return max(nums)
        res = [-1 for _ in range(len(nums))]
        res[len(nums) - 1] = nums[len(nums) - 1]

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i, len(nums)):
                res[i] = max(res[i], nums[j] + (res[j + 2] if j + 2 < len(nums) else 0))
        return res[0]