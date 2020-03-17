class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self._isSymmetric(root, root)

    def _isSymmetric(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return a.val == b.val and self._isSymmetric(a.left, b.right)
