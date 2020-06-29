class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end
        return end + 1
