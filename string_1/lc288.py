from collections import defaultdict


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.mp = defaultdict(set)
        for s in dictionary:
            abbr = self.getAbbr(s)
            self.mp[abbr].add(s)

    def isUnique(self, word: str) -> bool:
        abbr = self.getAbbr(word)
        if abbr not in self.mp:
            return True
        return len(self.mp[abbr]) == 1 and word in self.mp[abbr]

    def getAbbr(self, s):
        if len(s) <= 2:
            return s
        return s[0] + str(len(s) - 2) + s[-1]

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
