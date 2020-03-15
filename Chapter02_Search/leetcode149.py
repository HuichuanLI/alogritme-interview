from collections import Counter


class Solution:
    def maxPoints(self, points):

        def K(i, j):
            return float('Inf') if i[1] - j[1] == 0 else (i[0] - j[0]) / (i[1] - j[1])

        if len(points) <= 2:
            return len(points)

        maxans = 0
        for i in points:
            same = sum(1 for j in points if j == i)
            hashmap = Counter([K(i, j) for j in points if j != i])
            tempmax = hashmap.most_common(1)[0][1] if hashmap else 0
            maxans = max(same + tempmax, maxans)

        return maxans

