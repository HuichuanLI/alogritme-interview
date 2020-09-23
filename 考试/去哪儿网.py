import sys

m = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())

if n == 1:
    print(1)
    exit()
if m == 1:
    print(n)
    exit()

a = b = result = 1
minNI = min(n, m - n)
for j in range(0, minNI):
    a = a * (m - j)
    b = b * (minNI - j)
    result = a // b
print(result)
