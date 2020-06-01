class Solution:
    def findDisappearedNumbers(self, nums):
        if not nums:
            return  []
        max_value = max(nums)
        min_value = min(nums)
        res = []
        for elem in range(min_value,max_value):
            if elem not  in nums:
                res.append(elem)

        return res
