class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        res = []
        self.calculate_height(root, res)
        if max(res) > 1:
            return False
        else:
            return True

    def calculate_height(self, s, res):
        if not s:
            return 0
        left_height = self.calculate_height(s.left)
        right_height = self.calculate_height(s.right)
        res.append(abs(left_height - right_height))
        return 1 + max(left_height, right_height)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.maxDepth(root) != -1

    def maxDepth(self, root):
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
