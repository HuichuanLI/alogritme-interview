import re


class Solution:
    def isPalindrome(self, s):
        new = ''
        s = s.lower()

        for i in s:
            if '0' <= i <= '9' or 'a' <= i <= 'z':
                new += i
        return new == new[::-1]

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub('[^0-9a-zA-Z]+', '', s).lower()
        return s == s[::-1]

    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
