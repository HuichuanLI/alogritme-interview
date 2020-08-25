class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        n = len(A)
        res = [[False] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            res[i][0] = True
            for w in range(1, m + 1):
                if w >= A[i - 1]:
                    res[i][w] = res[i - 1][w] or res[i - 1][w - A[i - 1]]
                else:
                    res[i][w] = res[i - 1][w]

        for index, elem in enumerate(res[n][::-1]):
            if elem:
                return len(res[n]) - 1 - index
