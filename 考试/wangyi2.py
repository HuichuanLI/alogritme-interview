import sys
from collections import deque
from collections import defaultdict


def bfs(end_x, end_y, graph):
    step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    start = (0, 0)
    queue = deque([start])
    visited = defaultdict(bool)
    visited[(0, 0)] = True
    index = 0
    while queue:
        size = len(queue)

        for i in range(size):
            cur_pos = queue.pop()
            for i in range(4):
                dx = cur_pos[0] + step[i][0]
                dy = cur_pos[1] + step[i][1]
                print(dx, dx)
                if (dx, dy) == (end_x, end_y):
                    return index + 1
                if (dx, dy) in graph and not visited[(dx, dy)]:
                    queue.append((dx, dy))
                    visited[(dx, dy)] = True
        index += 1
    return index


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    result = []
    for i in range(T):
        N = int(sys.stdin.readline().strip())
        cur_pos = [0, 0]
        graph = set()
        cur_step = (0, 0)
        for j in range(N):
            line = sys.stdin.readline().strip()
            direction, success = line.split()

            if int(success) == -1:
                continue
            else:
                direction = int(direction)
                if direction == 0:
                    cur_pos[0] -= 1
                elif direction == 1:
                    cur_pos[0] += 1
                elif direction == 2:
                    cur_pos[1] -= 1
                else:
                    cur_pos[1] += 1

            cur_step = (cur_pos[0], cur_pos[1])
            graph.add((cur_pos[0], cur_pos[1]))
        result.append(bfs(cur_pos[0], cur_pos[1], graph))

    for index, elem in enumerate(result):
        if index == len(result) - 1:
            print(elem, end="")
        else:
            print(elem)
