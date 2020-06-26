
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        if len(word) > 0:
            return len(word[-1])
        else:
            return 0