from collections import defaultdict, Counter


class Solution:
    def findAnagrams(self, s, p):
        dict_p = Counter(p)
        lookup = defaultdict(int)
        start, end, postion, inital = 0, 0, [], ''
        while end < len(s):
            if s[end] in p and lookup[s[end]] < dict_p[s[end]]:
                inital += s[end]
                lookup[s[end]] += 1
                end += 1
                if len(inital) == len(p):
                    postion.append(start)
            elif s[end] in p and lookup[s[end]] >= dict_p[s[end]]:
                lookup[s[start]] -= 1
                start += 1
                inital = s[start:end]
            else:
                lookup = defaultdict(int)
                inital = ""
                end += 1
                start = end
