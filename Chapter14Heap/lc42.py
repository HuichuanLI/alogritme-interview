class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """

    def trap(self, heights):
        if not heights:
            return 0

        left_max = []
        curt_max = -sys.maxsize
        for height in heights:
            curt_max = max(curt_max, height)
            left_max.append(curt_max)

        right_max = []
        curt_max = -sys.maxsize
        for height in reversed(heights):
            curt_max = max(curt_max, height)
            right_max.append(curt_max)

        right_max = right_max[::-1]

        water = 0
        n = len(heights)
        for i in range(n):
            water += (min(left_max[i], right_max[i]) - heights[i])
        return water
