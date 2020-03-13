class Solution:
    # 时间复杂度O（n）,空间复杂度O（1）
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        result = [0, 0, 0]
        for ele in nums:
            result[ele] += 1
        i = 0
        for _ in range(result[0]):
            nums[i] = 0
            i += 1
        for _ in range(result[1]):
            nums[i] = 1
            i += 1
        for _ in range(result[2]):
            nums[i] = 2
            i += 1

        return nums

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0
        for i in nums:
            if i == 0:
                red += 1
            elif i == 1:
                white += 1
        for i in range(red):
            nums[i] = 0
        for i in range(red, red + white):
            nums[i] = 1
        for i in range(red + white, len(nums)):
            nums[i] = 2

    def sortColors(self, nums):
        zero = -1
        one = 0
        two = len(nums)
        while one < two:
            if nums[one] == 1:
                one += 1
            elif nums[one] == 2:
                nums[one], nums[two - 1] = nums[two - 1], nums[one]
                two -= 1
            elif nums[one] == 0:
                nums[one], nums[zero + 1] = nums[zero + 1], nums[one]
                one += 1
                zero += 1
