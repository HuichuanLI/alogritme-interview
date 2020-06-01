class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        for index in range(len(prices)):
            if prices[index] >= max(prices[index:]):
                continue
            else:
                if max(prices[index:]) - prices[index] > res:
                    res = max(prices[index:]) - prices[index]
        return res


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit
