# 有排成一行的ｎ个方格，用红(Red)、粉(Pink)、绿(Green)三色涂每个格子，每格涂一色，
# 要求任何相邻的方格不能同色，且首尾两格也不同色
# ．求全部的满足要求的涂法.
# RPG 难题


def result(n):
    res = [0] * (n + 1)
    res[1] = 3
    res[2] = 6
    for i in range(3, n + 1):
        res[i] = res[i - 1] + 2 * res[i - 2]
    return res[-1]


print(result(10))
