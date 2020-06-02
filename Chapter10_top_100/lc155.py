class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
            self.minV = x
        else:
            if x < self.minV:
                self.minV = x
            self.stack.append(x)

    def pop(self) -> None:
        cur = self.stack.pop()
        if cur == self.minV and len(self.stack) > 0:
            self.minV = min(self.stack)



    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minV
