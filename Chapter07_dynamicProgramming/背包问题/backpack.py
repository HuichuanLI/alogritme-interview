class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    # 这个是去统计最多能放多少的
    def backPack(self, m, A):
        # write your code here
        res = [[False] * (m + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) + 1):
            res[i][0] = True
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    res[i][j] = res[i - 1][j] or res[i - 1][j - A[i - 1]]
                else:
                    res[i][j] = res[i - 1][j]
        for index, elem in enumerate(res[-1][::-1]):
            if elem:
                return len(res[-1]) - 1 - index
