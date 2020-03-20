class Soultion:
    def knapsnacl01(self, w, v, C):
        n = len(w)
        return self.bestvalue(w, v, n, C)

    def bestvalue(self, w, v, index, C):
        if index < 0 or C == 0:
            return 0
        res = self.bestvalue(w, v, index - 1, C)
        if C >= w[index]:
            res = max(res, v[index] + self.bestvalue(w, v, index - 1, C - w[index]))
        return res


# 记忆化搜索(len(w),C)
class Soultion:
    def knapsnacl01(self, w, v, C):
        n = len(w)
        self.memo = [[-1 for i in range(C + 1)] for _ in range(len(w))]
        return self.bestvalue(w, v, n, C)

    def bestvalue(self, w, v, index, C):
        if index < 0 or C == 0:
            return 0
        if self.memo[index][C] != -1:
            return self.memo[index][C]
        res = self.bestvalue(w, v, index - 1, C)
        if C >= w[index]:
            res = max(res, v[index] + self.bestvalue(w, v, index - 1, C - w[index]))
        self.memo[index][C] = res
        return res


# dynamic programming

class Soultion:
    def knapsnacl01(self, w, v, C):
        n = len(w)
        self.memo = [[-1 for i in range(C + 1)] for _ in range(len(w))]
        for i in range(C + 1):
            self.memo[0][i] = w[0] if i > w[0] else 0
        for i in range(1, n):
            for j in range(0, C + 1):
                self.memo[i][j] = self.memo[i - 1][j]
                if j >= w[i]:
                    self.memo[i][j] = max(self.memo[i][j], v[i] + self.memo[i - 1][j - w[i]])
        return self.memo[n - 1][C]


# dynamic programming 优化O(2*C)

class Soultion:
    def knapsnacl01(self, w, v, C):
        n = len(w)
        self.memo = [[-1 for i in range(C + 1)] for _ in range(2)]
        for i in range(C + 1):
            self.memo[0][i] = w[0] if i > w[0] else 0
        for i in range(1, n):
            for j in range(0, C + 1):
                self.memo[i % 2][j] = self.memo[(i - 1) % 2][j]
                if j >= w[i]:
                    self.memo[i % 2][j] = max(self.memo[i % 2][j], v[i] + self.memo[(i - 1) % 2][j - w[i]])
        return self.memo[(n - 1) % 2][C]

# dynamic programming 优化O(C)
class Soultion:
    def knapsnacl01(self, w, v, C):
        n = len(w)
        self.memo = [-1 for i in range(C + 1)]
        for i in range(C + 1):
            self.memo[i] = w[0] if i > w[0] else 0
        for i in range(1, n):
            for j in range(C + 1, w[i], -1):
                self.memo[j] = max(self.memo[j], v[i] + self.memo[j - w[i]])
        return self.memo[C]
