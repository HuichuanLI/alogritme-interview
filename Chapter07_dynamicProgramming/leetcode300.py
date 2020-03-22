class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                dp[i] = max(dp[i], (dp[j] + 1 if nums[i] > nums[j] else 1))

        return max(dp)