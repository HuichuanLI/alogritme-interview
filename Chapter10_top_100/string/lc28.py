class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            j = 0
            Flag = True
            while j < len(needle) and len(haystack) - i + 1 > len(needle):
                if haystack[i + j] != needle[j]:
                    Flag = False
                j += 1
            if Flag:
                return i
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1
