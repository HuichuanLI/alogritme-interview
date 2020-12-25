# -*- coding:utf-8 -*-
# @Time : 2020/12/25 9:20 下午
# @Author : huichuan LI
# @File : lc50.py
# @Software: PyCharm

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return 1 / self.pow(x, -n) if n < 0 else self.pow(x, n)

    def pow(self, x, n):
        r = 1
        while n:
            if n & 1 == 1:
                r *= x
            x *= x
            n = n // 2
        return r
