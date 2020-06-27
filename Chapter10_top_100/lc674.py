class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        res = [0] * n
        res[0] = 1
        for i in range(n):
            res[i] = 1
            if nums[i] > nums[i-1]:
                res[i] = res[i-1]
        return max(res)
