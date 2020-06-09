class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.postion = 0

    def visit(self, url: str) -> None:
        nums = len(self.stack) - 1
        for i in range(self.postion, nums):
            self.stack.pop()
        self.stack.append(url)
        self.postion += 1

    def back(self, steps: int) -> str:
        self.postion = max(0, self.postion - steps)
        return self.stack[self.postion]

    def forward(self, steps: int) -> str:
        self.postion = min(self.postion + steps, len(self.stack) - 1)
        return self.stack[self.postion]
