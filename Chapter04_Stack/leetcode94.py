class Solution:
    def inorderTraversal(self, root):
        res = []
        self._predorder(root, res)
        return  res

    def _predorder(self, root, res):
        if root != None:
            res.append(res.val)
            self._predorder(root.left,res)
            self._predorder(root.right,res)