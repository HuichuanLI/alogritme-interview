from collections import Counter


class Solution:
    def frequencySort(self, s):
        dict_s = Counter(s)
        dict_s = dict(sorted(dict_s.items(), key=lambda index: index[1], reverse=True))
        res = ''
        for char, times in dict_s.items():
            res += char * times

        return res