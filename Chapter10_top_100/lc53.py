class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = [nums[0]]
        for index, elem in enumerate(nums):
            if index == 0:
                continue
            else:
                arr.append(max(arr[-1] + elem, elem))

        return max(arr)
