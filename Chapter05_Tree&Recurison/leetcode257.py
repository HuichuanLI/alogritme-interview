class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self._binaryTreePaths(root, [], res)
        return res

    def _binaryTreePaths(self, root, path, res):
        if not root:
            res.append(path)
            return
        path.append(root)
        self._binaryTreePaths(root.left, path, res)
        self._binaryTreePaths(root.right, path, res)
        return
