class Solution:
    # - 时间复杂度: O(N)- 空间复杂度: O(1)
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return
        i = 1
        cur = nums[0]
        while i < len(nums):
            if nums[i] == cur:
                del nums[i]
            else:
                cur = nums[i]
                i += 1

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        for num in nums:
            if idx < 1 or num != nums[idx - 1]:
                nums[idx] = num
                idx += 1
        return idx
