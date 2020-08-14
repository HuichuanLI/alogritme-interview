import math
import sys

n = int(sys.stdin.readline().strip())
res = [i for i in range(n + 1)]
for i in range(2, n):
    for j in range(2, n):
        if i * j < n + 1:
            res[i * j] = 0

res[1] = 0
res[0] = 0
i = 1
result = 0
while i <= n:
    while i<=n and res[i] == 0:
        i = i + 1
        continue
    cnt = 0
    j = i
    while cnt < n and j <n+1:
        cnt += res[j]
        j += 1

    if cnt == n:
        result += 1
    i = i + 1

print(result)
