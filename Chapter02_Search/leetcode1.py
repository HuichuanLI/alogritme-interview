class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for index, ele in enumerate(nums):
            if target - ele in dict.keys():
                return [dict[target - ele], index]
            dict[ele] = index
        return []