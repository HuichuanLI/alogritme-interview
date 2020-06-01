class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        SUM, tmp, high = 0, 0, 1
        while (left <= right):
            while (left <= right and height[left] < high):
                SUM += height[left]
                left += 1
            while (right >= left and height[right] < high):
                SUM += height[right]
                right -= 1
            high += 1
            tmp += right - left + 1
        return tmp - SUM
