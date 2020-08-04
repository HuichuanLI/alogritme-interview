class Solution:
    # For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.
    def binarySearch(self, nums, target):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1


print(Solution().binarySearch([1, 1, 2, 3, 4], 1))
