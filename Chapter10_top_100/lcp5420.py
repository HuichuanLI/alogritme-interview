class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for index, price in enumerate(prices):
            cur_prices = 0
            j = index + 1
            for j in range(index + 1, len(prices)):
                if prices[j] <= price:
                    cur_prices = prices[j]
                    break

            price -= cur_prices
            res.append(cur_prices)

        return res
