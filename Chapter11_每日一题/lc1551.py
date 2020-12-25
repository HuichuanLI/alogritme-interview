# -*- coding:utf-8 -*-
# @Time : 2020/12/22 9:46 下午
# @Author : huichuan LI
# @File : lc1551.py
# @Software: PyCharm

class Solution:
    def minOperations(self, n: int) -> int:
        return (n * n - (n & 1)) >> 2


class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            return n * n // 4
        if n % 2 != 0:
            return (n * 2 - 1) // 4
