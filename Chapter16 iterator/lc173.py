class BSTIterator:

    def __init__(self, root: TreeNode):
        self.curt = root
        self.stack = []

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.curt:
            self.stack.append(self.curt)
            self.curt = self.curt.left
        self.curt = self.stack.pop()
        node = self.curt
        self.curt = self.curt.right
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.curt is not None or len(self.stack) > 0
