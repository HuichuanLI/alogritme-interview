# 回溯法
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums = sorted(nums)
        self.dfs(res, path, 0, nums)
        return res

    def dfs(self, result, path, index, nums):
        result.append(path.copy())
        for pos in range(index, len(nums)):
            if pos != index and nums[pos] == nums[pos - 1]:
                continue
            path.append(nums[pos])
            self.dfs(result, path, pos + 1, nums)
            path.pop(len(path) - 1)
        return
