import sys


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        min_array = [sys.maxsize] * n
        max_array = [-sys.maxsize] * n
        min_array[0] = nums[0]
        max_array[0] = nums[0]
        res = nums[0]
        for i in range(1, n):
            min_array[i] = min(nums[i], min_array[i - 1] * nums[i], max_array[i - 1] * nums[i])
            max_array[i] = max(nums[i], max_array[i - 1] * nums[i], min_array[i - 1] * nums[i])

            res = max(res, min_array[i], max_array[i])
        return res
