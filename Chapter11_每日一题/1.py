import heapq

n, m, x = map(int, input().strip().split(' '))
grass = list(map(int, input().strip().split(' ')))
heapq.heapify(grass)
for _ in range(m):
    c = heapq.heappop(grass)
    heapq.heappush(grass, c + x)
print(str(heapq.heappop(grass)))

from collections import defaultdict
import heapq

n = int(input())
l = list(map(int, input().strip().split(' ')))
q = []
heapq.heapify(q)
c = defaultdict(list)
for idx, item in enumerate(l):
    c[item].append(idx)
for k in c:
    heapq.heapify(c[k])
    if len(c[k]) >= 2:
        heapq.heappush(q, k)
while q:
    t = heapq.heappop(q)
    re = heapq.heappop(c[t])
    l[re] = 'a'
    n = heapq.heappop(c[t])
    l[n] *= 2
    if len(c[t]) >= 2:
        heapq.heappush(q, t)
    if t * 2 in c:
        heapq.heappush(c[t * 2], n)
    else:
        c[t * 2] = [n]
        heapq.heapify(c[t * 2])
    if (len(c[t * 2]) >= 2) and ((t * 2) not in q):
        heapq.heappush(q, t * 2)
print(' '.join([str(i) for i in l if i != 'a']))
