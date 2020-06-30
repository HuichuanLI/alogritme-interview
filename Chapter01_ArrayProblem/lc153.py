class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= nums[end]:
                start = mid
            else:
                end = mid
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]
