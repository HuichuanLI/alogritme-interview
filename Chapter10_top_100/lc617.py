# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        root = self.preOrder(t1, t2)
        return root

    def preOrder(self, t1, t2):
        if t1 and t2:
            newNode = TreeNode(t1.val + t2.val)
        elif not t1 and not t2:
            newNode = None
            return newNode
        elif not t1 and t2:
            newNode = t2
            return newNode
        else:
            newNode = t1
            return newNode
        newNode.left = self.preOrder(t1.left, t2.left)
        newNode.right = self.preOrder(t1.right, t2.right)

        return newNode