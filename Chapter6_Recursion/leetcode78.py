class Solution:
    def subsets(self, nums):
        if not nums:
            return []

        res = []
        self._subsets(nums, 0, [], res)
        return res

    def _subsets(self, nums, index, path, res):
        if index >= len(nums):
            res.append(path)
            return
        self._subsets(nums, index + 1, path + [nums[index]], res)
        self._subsets(nums, index + 1, path, res)
        return
