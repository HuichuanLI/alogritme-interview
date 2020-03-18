class Solution:
    def sumNumbers(self, root):
        if not root:
            return 0

        res = self.path(root)
        return sum([int("".join(ele)) for ele in res])

    def path(self, root):
        res = []
        if not root:
            return []
        if not root.left and not root.right:
            res.append([root.val])
            return res
        for ele in self.path(root.left):
            ele.insert(0, root.val)
            res.append(ele)
        for ele in self.path(root.right):
            ele.insert(0, root.val)
            res.append(ele)
        return res
