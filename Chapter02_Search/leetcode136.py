class Solution:
    # - 时间复杂度: O(1)- 空间复杂度: O(1)
    def isHappy(self, n):
        if n == 1:
            return True
        result = set()
        while len(result) == 1 or n not in list(result):
            result.add(n)
            n = self.calculate(n)
            if n == 1:
                return True
        return False

    def calculate(self, n):
        res = 0
        while n > 0:
            res += (n % 10) ** 2
            n = n // 10
        return res


if __name__ == "__main__":
    print(Solution().isHappy(19))
