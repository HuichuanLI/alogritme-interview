class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ans = 0
        j = 0
        for i in range(len(s)):
            while j < len(s) and len(set(s[i:j + 1])) == j - i + 1:
                ans = max(ans, j - i + 1)
                j += 1

        return ans
