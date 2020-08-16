import heapq


class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """

    def trapRainWater(self, boards):
        # write your code here
        if not boards or not boards[0]:
            return 0

        heap = []
        # 存储格式(val, x, y),表示在点(x, y)处的吃水线
        visited = [[False for i in range(len(boards[0]))] for j in range(len(boards))]
        for i in range(len(boards)):
            for j in range(len(boards[0])):
                if i == 0 or i == len(boards) - 1 or j == 0 or j == len(boards[0]) - 1:
                    heapq.heappush(heap, (boards[i][j], i, j))
                    # print(heap)
                    visited[i][j] = True

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        result = 0
        while heap:
            # print(heap)
            val, x, y = heapq.heappop(heap)
            for i in range(4):
                x_ = x + dx[i]
                y_ = y + dy[i]
                if x_ >= 0 and x_ < len(boards) and y_ >= 0 and y_ < len(boards[0]) and not visited[x_][y_]:
                    # (x, y) is P
                    # f(P) = val
                    # (x_, y_) is Q
                    # f(Q) = max(f(P), h(Q))
                    h = max(val, boards[x_][y_])
                    result += (h - boards[x_][y_])
                    heapq.heappush(heap, (h, x_, y_))
                    visited[x_][y_] = True
        return result
