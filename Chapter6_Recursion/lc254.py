class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        self.dfs(n, 2, [], res)
        return res

    def dfs(self, number, i, path, res):
        if len(path):
            res.append(path[:] + [number])

        for i in range(i, int(math.sqrt(number) + 1)):
            if number % i == 0:
                self.dfs(number // i, i, path + [i], res)

