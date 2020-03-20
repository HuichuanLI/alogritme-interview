class Solution:
    def canPartition(self, nums):
        if not nums:
            return False
        sum_value = sum(nums)
        if sum_value % 2 != 0:
            return False
        return self.tryPartion(nums, len(nums) - 1, sum_value / 2)

    def tryPartion(self, nums, index, sum_1):
        if sum_1 == 0:
            return True
        if sum < 0 or index < 0:
            return False
        return self.tryPartion(nums, index - 1, sum_1) or self.tryPartion(nums, index - 1, sum_1 - nums[index])


class Solution:
    def canPartition(self, nums):
        if not nums:
            return False
        sum_value = sum(nums)
        self.res = [[-1 for _ in range(sum_value // 2 + 1)] for _ in range(len(nums))]
        if sum_value % 2 != 0:
            return False
        return self.tryPartion(nums, len(nums) - 1, sum_value // 2)

    def tryPartion(self, nums, index, sum_1):
        if sum_1 == 0:
            return True
        if sum_1 < 0 or index < 0:
            return False
        if self.res[index][sum_1] != -1:
            return self.res[index][sum_1] == 1
        if self.tryPartion(nums, index - 1, sum_1) or self.tryPartion(nums, index - 1, sum_1 - nums[index]):
            self.res[index][sum_1] = 1
            return True
        else:
            self.res[index][sum_1] = 0
            return False


class Solution:
    def canPartition(self, nums):
        if not nums:
            return False
        sum_value = sum(nums)
        if sum_value % 2 != 0:
            return False
        c = sum_value // 2
        self.res = [False] * (c + 1)
        for i in range(c + 1):
            self.res[i] = (nums[0] == i)
        for i in range(1, len(nums)):
            for j in range(c, nums[i] - 1, -1):
                self.res[j] = self.res[j] or self.res[j - nums[i]]
        return self.res[c]
