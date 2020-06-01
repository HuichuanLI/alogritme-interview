from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(Counter(nums).most_common(1)[0][0])


class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

# 方法五：Boyer-Moore 投票算法
