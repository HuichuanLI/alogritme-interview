class Solution:
    # - 时间复杂度: O(N) - 空间复杂度: O(1)

    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        i = 2
        cur_0 = nums[0]
        cur_1 = nums[1]
        while i < len(nums):
            if nums[i] == cur_0 and nums[i] == cur_1:
                del nums[i]
            else:
                cur_0 = cur_1
                cur_1 = nums[i]
                i += 1
        return len(nums)

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        for num in nums:
            if idx < 2 or num > nums[idx - 2]:
                nums[idx] = num
                idx += 1
        return idx
