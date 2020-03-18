class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        res = []
        visited = [False for _ in range(len(candidates))]

        def helper(index, cur, cur_sum, visited):
            if index == n or cur_sum > target:
                return
            if cur_sum == target:
                res.append(cur)
                return
            if not visited[index]:
                visited[index] = True
                helper(index, cur + [candidates[index]], cur_sum + candidates[index], visited)

            visited[index] = False
            helper(index + 1, cur, cur_sum, visited)

        helper(0, [], 0, visited)
        return list(set([tuple(ele) for ele in res]))
