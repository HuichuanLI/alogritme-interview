class Solution:
    res = []

    def letterCombinations(self, digits):
        if digits == "":
            return []
        self.res = []
        self.findcombination(digits, 0, "")
        return self.res

    def findcombination(self, digits, index, string):
        if index == len(digits):
            self.res.append(string)
            return
        KEY = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        c = digits[index]
        for elem in KEY[c]:
            self.findcombination(digits, index + 1, string + elem)
        return


