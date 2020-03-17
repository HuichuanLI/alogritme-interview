class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        res = 0
        self._countNode(root, res)

    def _countNode(self, root, res):
        if not root:
            return 0
        return 1 + self._countNode(root.left) + self._countNode(root.right)
