class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        n = len(s)
        res= [0] * (n+1)

        for index in range(1,n+1):
            if s[index-1] == ')' and s[index-2] == '(' and index -2 >=0 :
                res[index] = res[index-2] +2
            if s[index-1] == ")" and s[index-2] == ')' and index >=2 :
                if s[index - res[index]-1] == '(' and index-res[index] - 1 >0:
                    res[index] = res[index - res[index]-1] +2

        return max(res)