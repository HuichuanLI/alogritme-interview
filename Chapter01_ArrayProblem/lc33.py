class Solution:
    def search(self, nums: List[int], target: int) -> int:

        res = -1
        if not nums:
            return res
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] < nums[mid]:
                if nums[left] <= target and nums[mid] >= target:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target and nums[right] >= target:
                    left = mid
                else:
                    right = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
