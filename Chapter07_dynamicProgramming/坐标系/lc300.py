class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        res = [0] * n
        res[0] = 1
        for i in range(1, n):
            res[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    res[i] = max(res[i], res[j] + 1)
        return max(res)
