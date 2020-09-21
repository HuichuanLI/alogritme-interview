import sys


class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copyBooks(self, pages, k):
        # write your code here
        if not pages or not k:
            return 0
        n = len(pages)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + pages[i - 1]

        # 给定划分的个数

        # state: dp[i][j] 表示前 i 个人，划分给 j 个本书，最少需要耗费多少时间
        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        for i in range(n + 1):
            dp[0][i] = sys.maxsize
        dp[0][0] = 0

        for k in range(1, k + 1):
            dp[k][0] = 0
            for j in range(1, n + 1):
                for prev in range(j):
                    cost = prefix_sum[j] - prefix_sum[prev]
                    dp[k][j] = min(dp[k][j], max(dp[k - 1][prev], cost))

        return dp[-1][-1]
