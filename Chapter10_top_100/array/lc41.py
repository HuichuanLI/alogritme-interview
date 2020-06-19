import sys


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_value = sys.maxsize
        max_value = 1
        for elm in nums:
            if elm > 0:
                max_value = max(max_value, elm)
                min_value = min(min_value, elm)

        for elem in range(1, max_value + 2):
            if elem not in nums:
                return elem
