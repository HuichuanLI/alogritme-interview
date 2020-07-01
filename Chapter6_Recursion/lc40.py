class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        candidates = [elem for elem in candidates if elem < target]
        self._combination([],target,candidates,0,res)
        return res

    def _combination(self, path, target, candidates, index, res):
        if sum(path) == target and path not in res:
            res.append(path)
            return
        for elem in range(index,len(candidates)):
            if candidates[elem] >= target:
                break
            self._combination(path + [candidates[elem]], target, candidates, elem+1,res)
