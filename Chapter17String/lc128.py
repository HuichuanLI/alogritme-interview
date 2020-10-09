from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = defaultdict(bool)
        res = defaultdict(list)
        result = 0
        nums = set(nums)
        for elem in nums:
            if not visited[elem]:
                cur_result = []
                pre = elem - 1
                next = elem + 1
                cur_result.append(elem)
                while pre in nums:
                    cur_result.append(pre)
                    pre = pre - 1
                    visited[pre] = True
                while next in nums:
                    cur_result.append(next)
                    next = next + 1
                    visited[next] = True
                result = max(result, len(cur_result))
        return result
