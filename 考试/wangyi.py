from collections import defaultdict
import sys

n = int(sys.stdin.readline().strip())
ans = 0
res = defaultdict(set)
for i in range(n):
    # 读取每一行
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    id, name = line.split()
    res[name].add(id)
result = 0
for elem, values in res.items():
    if len(values) >= 2:
        result += 1
print(result)
