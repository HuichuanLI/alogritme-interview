class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """

    # 只能放一次，统计能放多少次
    def backPackV(self, nums, target):
        # write your code here
        res = [[0] * (target + 1) for _ in range(2)]
        res[0][0] = 1
        for i in range(1, len(nums) + 1):
            res[i % 2][0] = 1
            for j in range(1, target + 1):
                if j >= nums[i - 1]:
                    res[i % 2][j] = res[(i - 1) % 2][j] + res[(i - 1) % 2][j - nums[i - 1]]
                else:
                    res[i % 2][j] = res[(i - 1) % 2][j]
        return res[len(nums) % 2][-1]
