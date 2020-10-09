class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """

    def mountainSequence(self, nums):
        # write your code here
        if len(nums) == 0:
            return -1

        if len(nums) == 0:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid
            else:
                right = mid
        if nums[left] > nums[right]:
            return nums[left]
        return nums[right]
