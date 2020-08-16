DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class TrieNode:  # 定义字典树的节点
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):  # 字典树插入单词
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()  # 在此节点申请节点
            node = node.children[c]  # 继续遍历
        node.is_word = True
        node.word = word  # 存入单词

    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None

        return node


class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def findWords(self, board, words):
        if board is None or len(board) == 0:
            return []

        trie = Trie()
        for word in words:  # 插入单词
            trie.add(word)

        result = set()
        for i in range(len(board)):  # 遍历字母矩阵，将每个字母作为单词首字母开始搜索
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(
                    board,
                    i,
                    j,
                    trie.root.children.get(c),
                    set([(i, j)]),
                    result,
                )

        return list(result)

    def search(self, board, x, y, node, visited, result):  # 在字典树上dfs查找
        if node is None:
            return

        if node.is_word:
            result.add(node.word)

        for delta_x, delta_y in DIRECTIONS:
            x_ = x + delta_x
            y_ = y + delta_y

            if not self.inside(board, x_, y_):
                continue
            if (x_, y_) in visited:
                continue

            visited.add((x_, y_))
            self.search(
                board,
                x_,
                y_,
                node.children.get(board[x_][y_]),
                visited,
                result,
            )
            visited.remove((x_, y_))

    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
