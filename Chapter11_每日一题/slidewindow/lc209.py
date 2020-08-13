import sys
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j=i=0
        sum = 0
        ans = sys.maxsize
        for i in range(len(nums)):
            while j < len(nums) and sum < s:
                sum += nums[j]
                j+=1
            if sum >= s:
                ans = min(ans,j-i)
            sum -= nums[i]
        if ans == sys.maxsize:
            return 0
        return ans