import sys

n = int(sys.stdin.readline().strip())
s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

s1 = s1.replace(' ', '')
s2 = s2.replace(' ', '')


def longestCommonSubsequence(A, B, n):
    m = n = n
    dp = [[0] * (n + 1) for _ in range(2)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
            else:
                dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])

    return dp[m % 2][n]


print(longestCommonSubsequence(s1, s2, n))
