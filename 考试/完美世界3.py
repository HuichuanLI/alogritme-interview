import heapq
import sys

m = int(sys.stdin.readline().strip())
start = list(map(int, sys.stdin.readline().strip().split()))
end = list(map(int, sys.stdin.readline().strip().split()))

intervals = []
for elema, elemb in zip(start, end):
    intervals.append([elema, elemb])


def result(time):
    if not time:
        return 0

    free_people = []

    time.sort(key=lambda x: x[0])

    heapq.heappush(free_people, time[0][1])

    for i in intervals[1:]:

        if free_people[0] <= i[0]:
            heapq.heappop(free_people)

        heapq.heappush(free_people, i[1])

    return len(free_people)


print(result(intervals))
