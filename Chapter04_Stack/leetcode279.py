from collections import deque

class Solution:
    def numSquares(self, n):
        if n <= 0:
            return 0
        queue = deque()
        queue.append((n, 0))
        visited = [False for _ in range(n+1)]
        visited[n] = True
        while len(queue) > 0:
            ele = queue.popleft()
            i = 1
            while ele[0] - i * i >= 0:
                a = ele[0] - i * i
                if not visited[a]:
                    if a == 0:
                        return ele[1] + 1
                    queue.append((a, ele[1] + 1))
                    visited[a] = True
                i += 1