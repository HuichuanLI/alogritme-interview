class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        res = []
        self._inorder(root, res)
        for i in range(len(res) - 1):
            if res[i] > res[i + 1]:
                return False
        return True

    def _inorder(self, root, res):
        if not root:
            return
        self._inorder(root.left, res)
        res.append(root.val)
        self._inorder(root.right, res)
