
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 0:
            return 0
        res = [[0] * 6 for _ in range(n + 1)]
        res[0][1] = 0

        for i in range(n + 1):
            # 1,3,5
            for j in range(1, 6, 2):
                res[i][j] = res[i - 1][j]
                if j > 1 and i >= 2:
                    res[i][j] = max(res[i][j], res[i - 1][j - 1] + prices[i - 1] - prices[i - 2])
            # 2,4
            for j in range(2, 5, 2):
                res[i][j] = res[i - 1][j - 1]
                if i >= 2:
                    res[i][j] = max(res[i][j], res[i - 1][j] + prices[i - 1] - prices[i - 2])

        return max(max(res[n][1], res[n][3]), res[n][5])
