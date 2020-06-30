class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums) - 1
        if end == -1:
            return -1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[start]:

                if target >= nums[start] and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if target >= nums[mid] and target <= nums[end]:
                    start = mid
                else:
                    end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

