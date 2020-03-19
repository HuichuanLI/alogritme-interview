class Solution:
    postion = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def exist(self, board, word):
        visited = [[False for _ in range(len(board[i]))] for i in range(len(board))]

        if not word or not word:
            return False
        i, j = 0, 0
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if self._exist(board, word, 0, i, j, visited):
                    return True
        return False

    def _exist(self, board, word, index, i, j, visited):
        if index == len(word) - 1:
            return board[i][j] == word[index]
        visited[i][j] = True
        if board[i][j] == word[index]:
            for next_step in self.postion:
                temp_i = i + next_step[0]
                temp_j = j + next_step[1]
                if temp_i >= 0 and temp_i < len(board) and temp_j >= 0 and temp_j < len(board[i]) and not \
                visited[temp_i][temp_j]:
                    if self._exist(board, word, index + 1, temp_i, temp_j, visited):
                        return True
            visited[i][j] = False
        else:
            visited[i][j] = False
            return
