class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        self.partition(nums, 0, len(nums) - 1)
        for i in range(2, len(nums), 2):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
        return nums

    def partition(self, nums, start, end):
        if start >= end:
            return
        pivot = nums[(start + end) // 2]
        left, right = start, end
        while left <= right:
            while left <= right and nums[right] > pivot:
                right -= 1
            while left <= right and nums[left] < pivot:
                left += 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        self.partition(nums, start, right)
        self.partition(nums, left, end)
