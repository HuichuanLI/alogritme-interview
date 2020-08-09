class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(len(nums)):
            if i % 2 == 1:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        return nums
