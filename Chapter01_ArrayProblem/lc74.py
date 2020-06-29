class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        for elem in matrix:
            res.extend(elem)
        left, right = 0, len(res)-1
        while left + 1 < right:
            mid = int(left + (right - left) / 2)
            if res[mid] == target:
                return True
            elif res[mid] < target:
                left = mid
            else:
                right = mid
        if res[left] == target:
            return True
        if res[right] == target:
            return True
        return False