import sys


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 0:
            return -1

        res = [sys.maxsize] * (amount + 1)
        res[0] = 0
        for i in range(1, amount + 1):
            for elem in coins:
                if elem <= i:
                    res[i] = min(res[i], res[i - elem] + 1)

        if res[-1] == sys.maxsize:
            return -1
        return res[-1]
