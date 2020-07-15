class Solution:
    def FindCircleNum(self, CircleList):
        # write code here
        n = len(CircleList)
        if n == 0:
            return 0
        res = [i for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if CircleList[i][j] == 1:
                    self.union(res, i, j)
        return len(set(res))

    def union(self, res, a, b):
        if res[a] == res[b]:
            return
        elemb = res[a]
        elema = res[b]
        for index in range(len(res)):
            if res[index] == elemb:
                res[index] = elema

        return res


if __name__ == "__main__":
    print(Solution().FindCircleNum([[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
