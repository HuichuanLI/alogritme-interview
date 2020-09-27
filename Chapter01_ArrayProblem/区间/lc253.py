class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = [(iv[0], 1) for iv in intervals] + [(iv[1], -1) for iv in intervals]
        events.sort()
        ans = cur = 0
        for _, e in events:
            cur += e
            ans = max(ans, cur)
        return ans
