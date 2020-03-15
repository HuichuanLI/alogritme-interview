from collections import Counter


class Solution:
    def containsDuplicate(self, nums):
        if len(nums) == 0:
            return False
        return Counter(nums).most_common()[0][1] > 1