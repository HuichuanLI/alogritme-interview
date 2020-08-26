import sys


def question(total):
    if total < 4:
        return 0
    if total < 7:
        return 1
    min_s = (total - 1) // 3
    max_s = min_s
    for x in range(2, min_s):
        total_square = 2 * x * (x + 1)
        s = x * x
        if total <= total:
            rest = total - total_square
            rest_long = rest // (2 * x + 1)
            rest_rest = rest - rest_long * (2 * x + 1)
            rest_rest_s = (rest_rest - 1) // 2
            s = s + rest_long * x + rest_rest_s
            max_s = max(s, max_s)
    return max_s


n = int(sys.stdin.readline().strip())
res = 0
for i in range(n):
    target = int(sys.stdin.readline().strip())
    print(question(target))
