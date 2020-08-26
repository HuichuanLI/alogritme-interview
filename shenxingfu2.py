import sys

line1 = sys.stdin.readline().strip()
n, m, k = list(map(int, line1.split()))
line2 = sys.stdin.readline().strip()
a = list(map(int, line2.split()))

key_gen = []
for i in range(m):
    cur_line = sys.stdin.readline().strip()
    cur_array = cur_line.split()
    key_gen.append([int(cur_array[0]), int(cur_array[1])])

key_result = []
for i in range(n):
    cur_max = -1
    for j in range(i + 1, n):

        if a[i] * a[j] + a[i] + a[j] == k:
            key_result.append([i + 1, j + 1])
            break
for elem in key_gen:
    sum = 0
    for cur_array in key_result:
        if cur_array[0] >= elem[0] and cur_array[1] <= elem[1]:
            sum += 1
    print(sum)
