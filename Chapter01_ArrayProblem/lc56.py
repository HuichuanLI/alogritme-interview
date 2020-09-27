class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda key: key[0])
        res = []
        for elem in intervals:
            if not res or elem[0] > res[-1][1]:
                res.append(elem)
            else:
                cur = res.pop()
                res.append([cur[0], max(cur[1], elem[-1])])
        return res
