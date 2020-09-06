class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        res = [[0] * 6 for _ in range(n + 1)]
        res[0][1] = 0

        for i in range(n + 1):
            # 1,3,5 手中没有股票
            for j in range(1, 6, 2):
                # 从 1，3，5 没有股票
                res[i][j] = res[i - 1][j]
                if j > 1 and i >= 2:
                    res[i][j] = max(res[i][j], res[i - 1][j - 1] + prices[i - 1] - prices[i - 2])

            for j in range(2, 5, 2):
                # 有股票 2，4 有股票
                res[i][j] = res[i - 1][j - 1]
                if i >= 2:
                    res[i][j] = max(res[i][j], res[i - 1][j] + prices[i - 1] - prices[i - 2])

        return max(res[-1][3], res[-1][1], res[-1][5])
