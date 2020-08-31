#
# 根据给定的参数n（10>n>=0），得到0-n之间的整数组成的不含有重复数字的偶数的个数（0为偶数）
# @param n int整型 10>n>=0
# @return int整型
#
class Solution:
    def get_even_num(self, n):
        # write code here
        if n == 0:
            return 1
        res = set()
        self.permuation(res, "", n)
        return len(res)

    def permuation(self, res, path, n):
        if len(path) > n + 1:
            return
        if len(path) > 0 and int(path) % 2 == 0:
            res.add(int(path))

        for i in range(0, n + 1):
            if str(i) not in path:
                self.permuation(res, path + str(i), n)


print(Solution().get_even_num(2))
