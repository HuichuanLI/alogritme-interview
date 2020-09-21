class Solution:
    """

    @param nums: an integer array and all positive numbers, no duplicates

    @param target: An integer

    @return: An integer

    """

    # 这个去统计 又少种可能性没有顺序的
    def backPackVI(self, nums, target):

        dp = [0 for i in range(target + 1)]

        dp[0] = 1

        for i in range(1, target + 1):

            for j in nums:
                if i >= j:
                    dp[i] += dp[i - j]

        return dp[target]
