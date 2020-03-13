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
