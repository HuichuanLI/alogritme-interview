# -*- coding:utf-8 -*-
# @Time : 2020/12/25 9:37 下午
# @Author : huichuan LI
# @File : lc1137.py
# @Software: PyCharm
import numpy as np


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0

        x, y, z = 0, 1, 1
        for _ in range(n - 2):
            x, y, z = y, z, x + y + z
        return z


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0

        x, y, z = 0, 1, 1
        for _ in range(n - 2):
            [x, y, z] = np.dot(np.array([[x, y, z]]),np.array([[0, 0, 1], [1, 0, 1], [0, 1, 1]]))[0]
        return z
