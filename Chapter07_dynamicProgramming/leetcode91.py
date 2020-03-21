class Solution:
    def numDecodings(self, s):
        if not s:
            return 0
        return self.divide(s, 0)

    # 从s[index:]能有多少个
    def divide(self, s, index):
        if index >= len(s):
            return 1
        if s[index] == '0':
            return 0
        res = 0
        if index + 1 < len(s) and int(s[index:index + 2]) <= 26:
            res = self.divide(s, index + 2)
        res += self.divide(s, index + 1)
        return res


# 记忆化搜索

class Solution:
    def numDecodings(self, s):
        if not s:
            return 0
        self.memo = [-1] * (len(s) + 1)
        return self.divide(s, 0)

    # 从s[index:]能有多少个
    def divide(self, s, index):
        if index >= len(s):
            return 1
        if s[index] == '0':
            return 0
        if self.memo[index] != -1:
            return self.memo[index]
        res = 0
        if index + 1 < len(s) and int(s[index:index + 2]) <= 26:
            res = self.divide(s, index + 2)
        res += self.divide(s, index + 1)
        self.memo[index] = res
        return res


# 动态规划


class Solution:
    def numDecodings(self, s):
        if not s:
            return 0
        if len(s) == 1:
            return int(int(s) != 0)
        self.memo = [0] * (len(s) + 1)
        self.memo[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] != '0':
                self.memo[i] = self.memo[i + 1]
                if i + 1 < len(s) and int(s[i:i + 2]) <= 26:
                    self.memo[i] += self.memo[i + 2]
        return self.memo[0]