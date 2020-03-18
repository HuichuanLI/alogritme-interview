class Solution:
    def combinationSum(self, candidates, target):
        if target == 0:
            return []
        res = set()
        self._combinationSum(candidates, target, [], res)
        return list(res)

    def _combinationSum(self, candidates, target, path, res):
        if target in candidates:
            res.add(tuple(sorted(path + [target])))

        for elem in candidates:
            if target - elem < 0:
                continue
            self._combinationSum(candidates, target - elem, path + [elem], res)
        return
