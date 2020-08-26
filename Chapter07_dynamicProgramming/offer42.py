class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = nums[0]
        sum_value = nums[0]
        for i in range(1, n):
            if sum_value < 0:
                sum_value = nums[i]
            else:
                sum_value += nums[i]

            if sum_value > max_value:
                max_value = sum_value
        return max_value
