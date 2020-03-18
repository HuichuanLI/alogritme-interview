class Solution:
    def binaryTreePaths(self, root):
        res = []
        if not root:
            return res

        if not root.left and not root.right:
            res.append(str(root.val))
            return res

        for elem in self.binaryTreePaths(root.left):
            res.append(str(root.val) + "->" + elem)

        for elem in self.binaryTreePaths(root.right):
            res.append(str(root.val) + "->" + elem)

        return res
