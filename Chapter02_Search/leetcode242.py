from collections import Counter


class Solution:
    def isAnagram(self, s, t):
        a = Counter(s)
        b = Counter(t)
        return a == b
