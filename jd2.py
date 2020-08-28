import sys

m = int(sys.stdin.readline().strip())

result = []
res = []
for i in range(m):
    cur = sys.stdin.readline().strip()
    cur_array = list(map(int, cur.split()))
    if cur_array[0] == 1:
        res.insert(cur_array[1] - 1, str(cur_array[2]))
    elif cur_array[0] == 2:
        if len(res) > 0:
            res.pop(cur_array[1] - 1)
    elif cur_array[0] == 3:
        result.append(res.copy())

for elem in result:
    print(" ".join(elem))
