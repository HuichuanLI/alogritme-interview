class Solution:
    def totalNQueens(self, n):
        if n == 0:
            return []
        board = [["." for _ in range(n)] for i in range(n)]
        cols = [False for _ in range(n)]
        t1 = [False for _ in range(2 * n - 1)]
        t2 = [False for _ in range(2 * n - 1)]
        return  self._dfs(board, 0, cols, t1, t2)

    def _dfs(self, board, steps, cols, t1, t2):
        res = 0
        if steps == len(board):
            return 1
        for i in range(len(board)):
            if not cols[i] and not t1[steps + i] and not t2[steps - i + len(board) - 1]:
                board[steps][i] = 'Q'
                cols[i] = True
                t1[steps + i] = True
                t2[steps - i + len(board) - 1] = True
                res += self._dfs(board, steps + 1, cols, t1, t2)
                board[steps][i] = '.'
                cols[i] = False
                t1[steps + i] = False
                t2[steps - i + len(board) - 1] = False
        return res
