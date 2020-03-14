class Solution:
    # - 时间复杂度: O(N) - 空间复杂度: O(N)

    def lengthOfLongestSubstring(self, s):
        start, end, maxlenth, inital = 0, 0, 0, ''
        while end < len(s):
            while s[end] in inital:
                start += 1
                inital = s[start:end]
            inital += s[end]
            end += 1
            if len(inital) > maxlenth:
                maxlenth = len(inital)
        return maxlenth
