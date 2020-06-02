class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        res = []
        def in_order(node):
            if not node:
                return
            in_order(node.left)
            res.append(node)
            in_order(node.right)
        in_order(root)
        for i in range(len(res)-1, -1, -1):
            if i == len(res) - 1:
                continue
            else:
                res[i].val += res[i+1].val
        return root

