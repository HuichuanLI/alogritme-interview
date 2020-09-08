import sys

line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()

n1 = len(line1)
n2 = len(line2)
if n1 > n2:
    line1, line2 = line2, line1
    n1, n2 = n2, n1
Flag = False
for i in range(n1, 0, -1):
    if n2 % i == 0 and n1 % i == 0 and line1[:i] * (n2 // i) == line2 and line1[:i] * (n1 // i) == line1:
        print(line1[:i])
        Flag = True
        break
if not Flag:
    print("")
