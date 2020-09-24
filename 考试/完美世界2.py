import sys

m = int(sys.stdin.readline().strip())
v = list(map(int, sys.stdin.readline().strip().split()))
p = list(map(int, sys.stdin.readline().strip().split()))

m = int(sys.stdin.readline().strip())


def backPack(m, A, V):
    n = len(A)
    res = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(1, m + 1):
            if i == 0 or j == 0:
                res[i][j] = 0
            elif A[i - 1] <= j:
                res[i][j] = max(res[i - 1][j], res[i - 1][j - A[i - 1]] + V[i - 1])
            else:
                res[i][j] = res[i - 1][j]
    return res[n][m]


print(backPack(m, p, v))
