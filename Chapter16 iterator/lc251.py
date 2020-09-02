class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.stack = v[::-1]

    def next(self) -> int:
        if self.hasNext():
            return self.stack.pop()

    def hasNext(self) -> bool:
        while len(self.stack) > 0 and isinstance(self.stack[-1], list):
            self.stack.extend(self.stack.pop()[::-1])
        return len(self.stack) > 0
