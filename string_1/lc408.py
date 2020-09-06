class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        index = 0
        i = 0
        while i < len(word) and index < len(abbr):
            if word[i] == abbr[index]:
                index += 1
                i += 1
            elif abbr[index].isdigit() and abbr[index] != '0':
                start = index
                while index < len(abbr) and abbr[index].isdigit():
                    index += 1
                i += int(abbr[start: index])
            else:
                return False
        if i == len(word) and index == len(abbr):
            return True
        else:
            return False
