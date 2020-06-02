class Solution:
    def __index__(self):
        self.res = 0

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.dfs(nums, 0, S, 0)
        return self.res


    def dfs(self, nums, index, target, sum):
        if index == len(nums) and target == sum:
            self.res += 1
            return
        self.dfs(nums, index + 1, target, sum + nums[index])
        self.dfs(nums, index + 1, target, sum - nums[index])
