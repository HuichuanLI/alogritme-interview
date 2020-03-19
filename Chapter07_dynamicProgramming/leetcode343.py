# 记忆化搜索
class Solution:
    def integerBreak(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        res = [0] * (n + 1)
        self.breakInteger(n, res)
        return res[n]

    def breakInteger(self, n, res):
        if n == 1:
            return 1
        if res[n] != 0:
            return res[n]
        produit = 1
        for i in range(1, n):
            if res[n - i] == 0:
                res[n - i] = max(self.breakInteger(n - i, res), n - i)
            if i * res[n - i] > produit:
                produit = i * res[n - i]
        res[n] = produit
        return produit


class Solution:
    def integerBreak(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        res = [0] * (n + 1)
        res[1] = 1
        for i in range(2, n + 1):
            produit = 1
            for j in range(1, i):
                if j * res[i - j] > produit:
                    produit = j * res[i - j]
            res[i] = max(produit, i)
        return res[n]
