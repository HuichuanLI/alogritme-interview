import sys
from collections import deque

line = sys.stdin.reaimport sys
from collections import deque

line = sys.stdin.readline().strip()
n, m = list(map(int, line.split()))

line = sys.stdin.readline().strip()
operation = list(map(int, line.split()))

res = [str(i + 1) for i in range(n)]

i = 0

while i < len(operation):
    if operation[i] == 2 and operation[i] == operation[i - 1]:
        operation.pop(i - 1)
        operation.pop(i - 1)
    elif i < len(operation) and operation[i] == 1:
        orginal = i
        index = 1
        while operation[i] == 1:
            index += 1
            i += 1
            if index == n:
                for i in range(n):
                    operation.pop(orginal)
    else:
        i += 1

for op in operation:
    if op == 1:
        res.append(res[0])
        res = res[1:]
    else:
        for i in range(0, n, 2):
            res[i], res[i + 1] = res[i + 1], res[i]

print(" ".join(res))
dline().strip()
n, m = list(map(int, line.split()))

line = sys.stdin.readline().strip()
operation = list(map(int, line.split()))

res = [str(i + 1) for i in range(n)]

i = 0

while i < len(operation):
    if operation[i] == 2 and operation[i] == operation[i - 1]:
        operation.pop(i - 1)
        operation.pop(i - 1)
    elif i < len(operation) and operation[i] == 1:
        orginal = i
        index = 1
        while operation[i] == 1:
            index += 1
            i += 1
            if index == n:
                for i in range(n):
                    operation.pop(orginal)
    else:
        i += 1

for op in operation:
    if op == 1:
        res.append(res[0])
        res = res[1:]
    else:
        for i in range(0, n, 2):
            res[i], res[i + 1] = res[i + 1], res[i]

print(" ".join(res))
