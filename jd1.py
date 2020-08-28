import sys

n = int(sys.stdin.readline().strip())

res = []
for i in range(n):
    cur = sys.stdin.readline().strip()
    cur_res = list(map(int, cur.split()))
    res.append(cur_res)

dp = res[-1]
for i in range(len(res) - 2, -1, -1):
    for j in range(2 * i + 1):
        dp[j] = res[i][j] + max(dp[j], dp[j + 1], dp[j + 2])

print(dp[0])
