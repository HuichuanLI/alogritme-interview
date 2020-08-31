#
# 求字符串的回文子字符串的个数
# @param str string字符串
# @return int整型
#


class Solution:

    def cal(self, s, res):
        n = len(s)
        for c in range(n):
            i = j = c
            while i >= 0 and j < n and s[i] == s[j]:
                res[i][j] = True
                i -= 1
                j += 1

        for c in range(n):
            i = c
            j = c + 1
            while i >= 0 and j < n and s[i] == s[j]:
                res[i][j] = True
                i -= 1
                j += 1

    def num_plalindrome_substr(self, s: str) -> int:
        if len(s) == 0:
            return 0
        n = len(s)
        res = [[False] * n for _ in range(n)]
        self.cal(s, res)
        sum = 0
        for i in range(n):
            for j in range(i, n):
                if res[i][j] == True:
                    sum += 1
        return sum