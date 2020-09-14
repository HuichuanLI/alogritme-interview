class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        sell = [0 for _ in range(n)]

        cool = [0 for _ in range(n)]

        buy = [0 for _ in range(n)]

        buy[0] = -prices[0]
        for i in range(1, n):
            buy[i] = max(cool[i - 1] - prices[i], buy[i - 1])

            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])

            cool[i] = max(sell[i - 1], buy[i - 1], cool[i - 1])
        return sell[-1]
