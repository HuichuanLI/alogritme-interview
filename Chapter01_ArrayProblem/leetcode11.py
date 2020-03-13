class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        sum = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            if area > sum:
                sum = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return sum


if __name__ == "__main__":
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
