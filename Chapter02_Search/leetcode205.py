class Solution:
    # - 时间复杂度: O(N) - 空间复杂度: O(N)

    def isIsomorphic(self, s, t):
        tmp = len(set(zip(s, t)))
        return tmp == len(set(s)) and tmp == len(set(t))
