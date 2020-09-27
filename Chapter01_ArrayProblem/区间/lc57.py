class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.append(newInterval)
        return self.merge(intervals)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for elem in intervals:
            if not res or res[-1][1] < elem[0]:
                res.append(elem)
            else:
                res[-1][1] = max(res[-1][1], elem[1])

        return res
