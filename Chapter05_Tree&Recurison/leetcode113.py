class Solution:
    def pathSum(self, root, sum):
        res = []
        if not root:
            return []
        if sum == root.val and not root.left and not root.right:
            res.append([root.val])
            return res

        if sum != root.val and not root.left and not root.right:
            return res

        for ele in self.pathSum(root.left, sum - root.val):
            ele.insert(0, root.val)
            res.append(ele)

        for ele in self.pathSum(root.right, sum - root.val):
            ele.insert(0, root.val)
            res.append(ele)

        return res
