class Solution:
    def postorderTraversal(self, root):
        res = []
        self._predorder(root, res)
        return  res

    def _predorder(self, root, res):
        if root != None:
            res.append(res.val)
            self._predorder(root.left,res)
            self._predorder(root.right,res)

# 非递归
class Solution:
    class Command:
        def __init__(self, s, node):
            self.s = s
            self.node = node

    def postorderTraversal(self, root):
        res = []
        stack = []
        if not root:
            return res
        stack.append(self.Command("go", root))
        while len(stack) > 0:
            command = stack.pop()
            if command.s == "print":
                res.append(command.node.val)
            else:
                stack.append(self.Command("print", command.node))
                if command.node.right:
                    stack.append(self.Command("go", command.node.right))

                if command.node.left:
                    stack.append(self.Command("go", command.node.left))

        return res