class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.calcul_pow(1.0 / x, -n)

        return self.calcul_pow(x, n)

    def calcul_pow(self, x, n):
        if n == 0:
            return 1.0
        y = self.calcul_pow(x, n // 2)
        return y * y if n % 2 == 0 else y * y * x


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
