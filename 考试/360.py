import sys

n = int(sys.stdin.readline().strip())
res = 0
for i in range(n):
    line = sys.stdin.readline().strip()
    if len(line) >= 10:
        continue
    Flag = False
    for elem in line:
        if not elem.isalpha():
            Flag = True

    if not Flag:
        res += 1
print(res)
