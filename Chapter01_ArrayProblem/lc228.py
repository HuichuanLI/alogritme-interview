class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        index = 0
        res = []
        while index < len(nums):
            start = index
            while index + 1 < len(nums) and nums[index + 1] - nums[index] == 1:
                index += 1
            res.append(self.getString(nums[start], nums[index]))
            index += 1
        return res

    def getString(self, left, end):
        if left > end:
            return ""
        elif left == end:
            return str(left)
        else:
            return str(left) + "->" + str(end)
