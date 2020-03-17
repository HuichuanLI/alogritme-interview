class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        if self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val):
            return True
        return False
