class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    matrix[i][j] = int(matrix[i][j])
                elif matrix[i - 1][j] >= 1 and matrix[i][j] == '1':
                    matrix[i][j] = matrix[i - 1][j] + 1
                else:
                    matrix[i][j] = int(matrix[i][j])

        max_area = 0
        for i in range(len(matrix)):
            max_area = max(max_area, self.find_matrix(matrix[i]))
        return max_area

    def find_matrix(self, matrix):
        if len(matrix) == 0:
            return 0
        stack = []
        max_area = 0
        matrix = matrix + [0]
        for i in range(len(matrix)):
            while stack and matrix[stack[-1]] > matrix[i]:
                cur = stack.pop()
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                max_area = max(max_area, matrix[cur] * (i - left - 1))
            stack.append(i)
        return max_area
