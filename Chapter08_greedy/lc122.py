class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for elem in range(len(prices) - 1):
            if prices[elem] < prices[elem + 1]:
                res += (prices[elem + 1] - prices[elem])
        return res
