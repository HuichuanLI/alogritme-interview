class Solution:
    def combine(self, n, k):
        if n == 0 or k == 0 or k > n:
            return []
        res = []

        self._generate(n, k, 1, [], res)
        return res

    def _generate(self, n, k, start, path, res):
        if k == len(path):
            res.append(path)
            return

        for ele in range(start, n + 1):
            self._generate(n, k, ele + 1, path + [ele], res)

        return


class Solution:
    def combine(self, n, k):
        if n == 0 or k == 0 or k > n:
            return []
        res = []

        self._generate(n, k, 1, [], res)
        return res

    def _generate(self, n, k, start, path, res):
        if k == len(path):
            res.append(path)
            return
        # 剪枝
        for ele in range(start, n - (k-len(path))+2):
            self._generate(n, k, ele + 1, path + [ele], res)

        return