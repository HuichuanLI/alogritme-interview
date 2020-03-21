class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals = sorted(intervals, key=lambda key: key[1])
        if len(intervals) <= 1:
            return 0
        res = 1
        pre = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[pre][1]:
                res += 1
                pre = i

        return len(intervals) - res
