class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]

        max_res = 0
        stack = [0]
        heights = heights + [0]
        for right in range(len(heights)):
            while stack and heights[stack[-1]] > heights[right]:
                cur = stack.pop()
                if stack:
                    max_res = max(max_res, heights[cur] * (right - stack[-1] - 1))
                else:
                    max_res = max(max_res, heights[cur] * (right))
            stack.append(right)
        return max_res
