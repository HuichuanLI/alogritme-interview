#
class Solution:
    def lengthOfLongestSubstring(self, s):
        # write code here
        if len(s) == 0:
            return 0
        l, r = 0, 0
        ans = -1
        for l in range(len(s)):
            while l <= r and r < len(s) and len(s[l:r]) == len(set(s[l:r])):
                r += 1
                ans = max(ans, r - l)
        return ans


print(Solution().lengthOfLongestSubstring("zasdwzshda"))
