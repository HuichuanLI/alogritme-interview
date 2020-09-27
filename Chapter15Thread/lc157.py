class Solution:

    def __init__(self):
        self.buf4, self.i4, self.n4 = [None] * 4, 0, 0

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        # Write your code here
        i = 0
        while i < n:
            if self.i4 == self.n4:
                self.i4, self.n4 = 0, read4(self.buf4)
                if not self.n4:
                    break
            buf[i], i, self.i4 = self.buf4[self.i4], i + 1, self.i4 + 1
        return i