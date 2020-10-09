class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit() and int(abbr[j]) != 0:
                cur = j
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                i += int(abbr[cur:j])
            else:
                return False
        if i == len(word) and j == len(abbr):
            return True
        else:
            return False
