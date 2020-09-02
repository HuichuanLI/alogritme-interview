class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while len(self.stack) > 0 and self.stack[-1].isInteger() == False:
            self.stack += self.stack.pop().getList()[::-1]
        return len(self.stack) > 0
