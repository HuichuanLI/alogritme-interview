import sys

word1 = sys.stdin.readline().strip()

target = sys.stdin.readline().strip()

word_list = sys.stdin.readline().strip().split()


def difference(a, b):
    dif = 0
    for i, j in zip(a, b):
        if i != j:
            dif += 1
        if dif > 1:
            return -1
    return dif


from collections import defaultdict, deque

if target not in word_list:
    print(0)
    exit()
if word1 == target:
    print(1)
    exit()
queue = deque([(word1, 1)])
visited = defaultdict(bool)
while len(queue) > 0:
    size = len(queue)
    for _ in range(size):
        cur_value = queue.popleft()
        if difference(target, cur_value[0]) == 1:
            print(cur_value[1] + 1)
            exit()
        for elem in word_list:
            if not visited[elem] and difference(elem, cur_value[0]) == 1:
                queue.append([elem, cur_value[1] + 1])
                visited[elem] = True
print(0)
