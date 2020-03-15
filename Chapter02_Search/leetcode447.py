from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points):
        def getDistance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + abs(p1[1] - p2[1]) ** 2

        res, lookup = 0, defaultdict(int)
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:  # 不能取同一个点
                    continue
                lookup[getDistance(points[i], points[j])] += 1
            res += sum(v * (v - 1) for k, v in lookup.items())
            lookup = defaultdict(int)
        return res


if __name__ == "__main__":
    Solution().numberOfBoomerangs([[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]])
