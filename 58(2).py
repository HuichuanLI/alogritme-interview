import math


class Solution:
    def question(self, a, b):
        # write code here
        for i in range(1, 501):
            if self.carre(a + i) and self.carre(b + i):
                return i

    def carre(self, number):
        if int(math.sqrt(number)) == math.sqrt(number):
            return True

