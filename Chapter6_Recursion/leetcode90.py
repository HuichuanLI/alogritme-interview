class Solution:
    def subsetsWithDup(self, nums):
        if not nums:
            return []

        res = set()
        self._subsets(nums, 0, [], res)
        return list(res)

    def _subsets(self, nums, index, path, res):
        if index >= len(nums):
            res.add(tuple(sorted(path)))
            return
        self._subsets(nums, index + 1, path + [nums[index]], res)
        self._subsets(nums, index + 1, path, res)
        return
