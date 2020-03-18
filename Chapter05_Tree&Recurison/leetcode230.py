class Solution(object):
    def kthSmallest(self, root,k):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        res = []
        self._inorder(root, res)
        return res[k-1]

    def _inorder(self, root, res):
        if not root:
            return
        self._inorder(root.left, res)
        res.append(root.val)
        self._inorder(root.right, res)