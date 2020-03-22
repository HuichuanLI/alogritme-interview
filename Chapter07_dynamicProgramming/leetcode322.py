class Solution:
    def coinChange(self, coins, amount):
        if not coins:
            return -1
        if amount == 0:
            return 0
        self.res = [-1] * (amount + 1)

    def divide(self, amounts, coins):
        if amounts == 0:
            return 0
        if self.res[amounts] != -1:
            return self.res[amounts]
        res = 10000
        if amounts < min(coins):
            return -1
        for elem in coins:
            if amounts >= elem:
                if self.divide(amounts - elem, coins) != -1:
                    res = min(res, 1 + self.divide(amounts - elem, coins))
        if res == 10000:
            self.res[amounts] = -1
        else:
            res.res[amounts] = res
        return res


class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coins]) + 1
        return dp[amount] if dp[amount] != float('inf') else -1


