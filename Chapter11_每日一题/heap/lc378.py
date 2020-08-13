import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 边界检查
        if not matrix or not matrix[0] or k <= 0: return

        rows, cols = len(matrix), len(matrix[0])
        # 初始化第一列为堆的初始状态，元组为 (val, i, j)
        h = [(matrix[i][0], i, 0) for i in range(rows)]
        heapq.heapify(h)

        res = 0
        for i in range(k):
            res, i, j = heapq.heappop(h)
            if j != cols - 1:  # 不是当前行最后一个元素的话，则追加本行下一个元素。
                heapq.heappush(h, (matrix[i][j + 1], i, j + 1))
        return res
