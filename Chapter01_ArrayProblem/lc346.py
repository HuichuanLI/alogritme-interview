class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.sum = [0] * (size)
        self.size = size
        self.index = 0

    def next(self, val: int) -> float:
        self.sum[(self.index + 1) % self.size] = self.sum[self.index % self.size] + val
        self.index += 1
        if self.size < self.index:

            return self.sum[(self.index) % self.size] / self.size
        else:
            return self.sum[(self.index) % self.size] / self.index


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.sum = [0] * (size + 1)
        self.size = size + 1
        self.index = 0

    def next(self, val: int) -> float:
        self.sum[(self.index + 1) % self.size] = self.sum[self.index % self.size] + val
        self.index += 1
        if self.size <= self.index:
            return (self.sum[(self.index) % self.size] - self.sum[(self.index - self.size + 1) % self.size]) / (
                    self.size - 1)
        else:
            return self.sum[(self.index) % self.size] / self.index


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.sum = [0] * (size + 1)
        self.size = size + 1
        self.index = 0

    def next(self, val: int) -> float:
        self.sum[(self.index + 1) % self.size] = self.sum[self.index % self.size] + val
        self.index += 1
        if self.size <= self.index:
            return (self.sum[(self.index) % self.size] - self.sum[(self.index - self.size + 1) % self.size]) / (
                    self.size - 1)
        else:
            return self.sum[self.index] / self.index
