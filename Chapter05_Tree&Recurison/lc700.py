# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        return self.dfs(root, val)

    def dfs(self, node, val):

        if not node:
            return None
        if node.val == val:
            return node
        resleft = self.dfs(node.left, val)
        if resleft:
            return resleft

        resright = self.dfs(node.right, val)
        if resright:
            return resright
