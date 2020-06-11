class Solution:
    def translateNum(self, num: int) -> int:
        self.res = 0
        self.dfs(str(num), 0)
        return self.res

    def dfs(self, nums, index):
        if index >= len(nums):
            self.res += 1
            return

        self.dfs(nums, index + 1)
        if int(nums[index:index + 2]) >=10 and int(nums[index:index + 2]) < 26 and index+2 <= len(nums):
            self.dfs(nums, index + 2)
