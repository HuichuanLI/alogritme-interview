class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """

    def firstWillWin(self, n):
        # write your code here
        if n == 0:
            return False
        if n <= 2:
            return True

        res = [False] * (n + 1)
        res[0] = False
        res[1] = True
        res[2] = True
        for i in range(2, n + 1):
            # 只有-1，-2 都是必胜的情况下，则当前必败，否则只要一个必败则你必胜
            if res[i - 1] and res[i - 2]:
                res[i] = False
            else:
                res[i] = True
        return res[-1]
