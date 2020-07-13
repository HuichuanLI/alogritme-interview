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

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        n = len(s)
        res = [[False] * n for _ in range(n)]
        self.cal(s, res)
        max_value = 0
        cur_string = ""
        for i in range(n):
            for j in range(i, n):
                if res[i][j] == True:
                    if j - i + 1 > max_value:
                        max_value = max(max_value, j - i + 1)
                        cur_string = s[i:j + 1]

        return cur_string
