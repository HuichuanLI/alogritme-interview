class Solution(object):
    # - 时间复杂度: O(N^2)- 空间复杂度: O(1)
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)

    # - 时间复杂度: O(N) - 空间复杂度: O(1)
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx = 0
        while idx < len(nums):
            if nums[idx] == val:
                nums[idx] = nums[-1]
                del nums[-1]
            else:
                idx += 1
        return len(nums)