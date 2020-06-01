class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        return self.length(root.left)+self.length(root.right)
    def length(self, root):
        if not root:
            return 0
        left = self.length(root.left)
        right = self.length(root.right)
        return max(left,right)+1