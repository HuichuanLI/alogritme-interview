class Solution:

    def backPackIII(self, A, V, m):
        # write your code here
        n = len(A)
        max_val = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for w in range(1, m + 1):
            max_val[0][w] = -1

        for i in range(1, n + 1):
            for w in range(1, m + 1):
                max_val[i][w] = max_val[i - 1][w]
                # 还要走k
                k = 1
                while w >= (k * A[i - 1]):
                    if max_val[i - 1][w - k * A[i - 1]] != -1:
                        max_val[i][w] = max(max_val[i][w], max_val[i - 1][w - k * A[i - 1]] + k * V[i - 1])
                    k += 1

        return max(max_val[n])

    def backPackIII(self, A, V, m):
        # write your code here
        n = len(A)
        max_val = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for w in range(1, m + 1):
            max_val[0][w] = -1

        for i in range(1, n + 1):
            for w in range(1, m + 1):
                max_val[i][w] = max_val[i - 1][w]
                if w >= A[i - 1] and max_val[i][w - A[i - 1]] != -1:
                    max_val[i][w] = max(max_val[i][w], max_val[i][w - A[i - 1]] + V[i - 1])

        return max(max_val[n])
