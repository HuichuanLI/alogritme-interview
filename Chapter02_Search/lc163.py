class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        tempString = []
        if not nums:
            return [self.getString(lower, upper)]
        if self.getString(lower, nums[0] - 1) != "":
            tempString.append(self.getString(lower, nums[0] - 1))
        for i in range(1, len(nums)):
            temp = self.getString(nums[i - 1] + 1, nums[i] - 1)
            if temp != "":
                tempString.append(temp)
        temp = self.getString(nums[-1] + 1, upper)
        if temp != "":
            tempString.append(temp)
        return tempString

    def getString(self, left, end):
        if left > end:
            return ""
        elif left == end:
            return str(left)
        else:
            return str(left) + "->" + str(end)
