from collections import Counter, defaultdict


class Solution:

    def compare(self, dict1, dict2):
        for elema in dict1:
            if dict1[elema] != dict2[elema]:
                return False
        return True

    def findAnagrams(self, s, p):
        s_len = len(s)
        p_len = len(p)
        index = len(p)
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        res = []
        if s_len < p_len:
            return res
        for elema, elemb in zip(s[:len(p)], p):
            dict1[elema] += 1
            dict2[elemb] += 1
        if self.compare(dict1, dict2):
            res.append(0)
        while index < s_len:
            dict1[s[index]] += 1
            dict1[s[index - p_len]] -= 1
            if self.compare(dict1, dict2):
                res.append(index - p_len + 1)
            index += 1
        return res
