class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        s = 0
        ans = 0
        prefix = {}

        prefix[0] = 0
        for i in range(len(nums)):
            s += nums[i]
            if s not in prefix:
                prefix[s] = i + 1
            if s - k in prefix:
                ans = max(ans, i + 1 - prefix[s - k])

        return ans
