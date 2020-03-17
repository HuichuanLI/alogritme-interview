class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        return self._sum(root, root)

    def _sum(self, root, parent):
        if not root:
            return 0
        if root and not root.left and not root.right and parent.left == root:
            return root.val
        res = 0
        if root.left:
            res += self._sum(root.left, root)
        if root.right:
            res += self._sum(root.right, root)
        return res

