import sys
from collections import deque

line = sys.stdin.readline().strip()
n, m = list(map(int, line.split()))

line = sys.stdin.readline().strip()
operation = list(map(int, line.split()))

res = [str(i + 1) for i in range(n)]

i = 0
a = 1
b = 2
now = 1
for op in operation:
    if op == 1:
        if now:
            a += 2
        else:
            b += 2
    now = 1 - now

for i in range(n):
    if i != 1:
        print(" ")
    if (i + 1 + now) % 2 == 1:
        a = a % n if a % n == 1 else n
        print(a)
        a += 2
    else:
        b = b % n if b % n == 1 else n
        print(b)
        b += 2
