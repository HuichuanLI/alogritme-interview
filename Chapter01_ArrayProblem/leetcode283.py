class Solution:
    # O（n） 空间O（n）
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        for ele in nums:
            if ele != 0:
                res.append(ele)

        for i in range(len(nums)):
            if i < len(res):
                nums[i] = res[i]
            else:
                nums[i] = 0
        return nums

    # O(n) , O(1)
    def moveZeroes2(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        while j < len(nums):
            nums[j] = 0
            j += 1
        return nums

    def moveZeroes3(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0 and i != j:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
            elif nums[i] != 0:
                j += 1

        return nums


if __name__ == "__main__":
    arr = [1, 2, 3, 0, 0, 4, 5]
    print(Solution().moveZeroes2(arr))
