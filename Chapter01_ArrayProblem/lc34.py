class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]

        if n == 1 and nums[0] == target:
            return [0, 0]
        elif n == 1 and nums[0] != target:
            return [-1, -1]
        flag = False
        res = [-1, -1]
        for elem in range(len(nums)):
            if nums[elem] == target and not flag:
                res[0] = elem
                res[1] = elem
                flag = True

            elif nums[elem] == target and flag:
                res[1] = elem

        return res
