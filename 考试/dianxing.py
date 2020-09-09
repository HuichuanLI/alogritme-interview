import heapq
from collections import defaultdict
import sys

n = int(sys.stdin.readline().strip())


def nthUglyNumber(n):
    res = [1, 2, 3, 5]
    heapq.heapify(res)
    cur_val = 1
    dict = defaultdict(bool)
    for i in range(n):
        while dict[cur_val]:
            cur_val = heapq.heappop(res)
        dict[cur_val] = True
        heapq.heappush(res, cur_val * 2)
        heapq.heappush(res, cur_val * 3)
        heapq.heappush(res, cur_val * 5)
    return cur_val


print(nthUglyNumber(n))
