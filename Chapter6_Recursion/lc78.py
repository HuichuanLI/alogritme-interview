# 回溯法
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        self.dfs(res, path, 0, nums)
        return res

    def dfs(self, result, path, index, nums):
        result.append(path.copy())
        for pos in range(index, len(nums)):
            path.append(nums[pos])
            self.dfs(result, path, pos + 1, nums)
            path.pop(len(path) - 1)
        return
