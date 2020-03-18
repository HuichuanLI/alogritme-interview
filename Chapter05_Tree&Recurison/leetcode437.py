class Solution:
    def pathSum(self, root, sum):
        if not root:
            return 0
        res = self.findpath(root, sum)
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        return res

    def findpath(self, node, sum):
        if not node:
            return 0

        res = 0
        if node.val == sum:
            res += 1

        res += self.findpath(node.left, sum - node.val)
        res += self.findpath(node.right, sum - node.val)

        return res
