# 完全背包问题
class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """

    def backPackIV(self, nums, target):
        # write your code here
        n = len(nums)
        res = [[0] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            res[i][0] = 1
            for j in range(1, target + 1):
                k = 0
                while j - k * nums[i - 1] >= 0:
                    res[i][j] += res[i - 1][j - k * nums[i - 1]]
                    k += 1
        return res[n][target]
