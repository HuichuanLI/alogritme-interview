import sys


class Solution:
    # - 时间复杂度: O(N)- 空间复杂度: O(1)
    def minSubArrayLen(self, s, nums):
        start, end, sums, res = 0, 0, 0, sys.maxsize
        while end < len(nums):
            sums += nums[end]
            end += 1
            while sums > s:
                sums -= nums[start]
                start += 1
                res = min(res, end - start + 1)
        return res if res != sys.maxsize else 0