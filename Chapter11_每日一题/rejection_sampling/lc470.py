# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            nums = (rand7() - 1) * 7 + rand7()
            if nums <= 40:
                return nums % 10 + 1

            a = nums - 40
            b = rand7()
            nums = (a - 1) * 7 + b
            if nums <= 60:
                return nums % 10 + 1

            a = nums - 60
            b = rand7()
            nums = (a - 1) * 7 + b
            if nums <= 20:
                return nums % 10 + 1
