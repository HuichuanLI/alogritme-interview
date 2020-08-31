import sys

n = int(sys.stdin.readline().strip())
result = []
for i in range(n):
    m = int(sys.stdin.readline().strip())
    res = [0] * 100000
    for j in range(m):
        cur_line = sys.stdin.readline().strip()
        start, latter = cur_line.split()
        start = int(start)
        latter = int(latter)
        if start == latter:
            res[start] += 1
        else:
            for i in range(start, latter + 1):
                res[i] += 1
    result.append(max(res))

for elem in result:
    print(elem)
