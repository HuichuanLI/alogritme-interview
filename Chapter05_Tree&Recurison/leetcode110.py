class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        res = []
        self.calculate_height(root,res)
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
