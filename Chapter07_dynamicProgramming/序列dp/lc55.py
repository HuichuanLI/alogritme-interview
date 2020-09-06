class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = [False] * len(nums)
        res[0] = True
        for i in range(1, len(nums)):
            for j in range(i, -1, -1):
                if res[j] and j + nums[j] >= i:
                    res[i] = True
                    break
        return res[-1]
