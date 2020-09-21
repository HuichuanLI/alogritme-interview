import sys

line1 = sys.stdin.readline().strip()

arr = list(map(int, line1.split()))

k = int(sys.stdin.readline().strip())

x = int(sys.stdin.readline().strip())

l = 0
r = len(arr)

dict_res = {}
for i, v in enumerate(arr):
    s = v - x
    dict_res[i] = abs(s)

sorted_list = sorted(dict_res.items(), key=lambda x: x[1])
result = sorted([arr[i[0]] for i in sorted_list][:k])

print(" ".join([str(elem) for elem in result]))
