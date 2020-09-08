import sys

line = sys.stdin.readline().strip()
n, m = list(map(int, line.split()))
res = [[0] * m for _ in range(n)]
arr = [i + 1 for i in range(n * m)]

index = 0
i = 0
j = 0
row = 0
while index < len(arr):
    if i < 0 or j > m - 1:
        row += 1
        if row <= n - 1:
            i = row
        else:
            i = n - 1
        j = row - 1
    res[i][j] = arr[index]
    i -= 1
    j += 1
    index += 1

print(res)
