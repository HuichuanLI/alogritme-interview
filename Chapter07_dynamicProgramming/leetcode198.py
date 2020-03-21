class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        res = []
        self.combination(nums, 0, 0, res)
        return res[0]

    def combination(self, nums, index, sum, res):
        if index >= len(nums):
            res.append(sum)
            return
        for i in range(index, len(sum)):
            self.combination(nums, i + 2, sum + nums[i], res)
        return


class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 2:
            return max(nums)
        self.res = [0 for _ in range(len(nums))]
        self.combination(nums, 0)
        # print(self.res)
        return self.res[0]

    def combination(self, nums, index):
        if index == len(nums) - 1 or index == len(nums) - 2:
            self.res[index] = nums[index]
            return nums[index]
        if index >= len(nums):
            return 0
        # print(index)
        for i in range(index, len(nums)):
            if i >= len(nums) - 2:
                self.res[i] = nums[i]
            elif self.res[i + 2] == 0:
                self.res[i + 2] = self.combination(nums, i + 2)
            self.res[i] = self.combination(nums, i + 2) + nums[i]

        self.res[index + 1] = self.combination(nums, index + 1)
        self.res[index] = max(self.res[index + 1], max(self.res[index + 2:]) + nums[index])
        return self.res[index]


class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 2:
            return max(nums)
        self.memo = [-1] * len(nums)
        return self.combination(nums, 0)
        # print(self.res)
        # return self.res[0]

    def combination(self, nums, index):
        if index >= len(nums):
            return 0
        if self.memo[index] != -1:
            return self.memo[index]
        res = 0
        for i in range(index, len(nums)):
            res = max(res, self.combination(nums, i + 2) + nums[i])
        self.memo[index] = res
        return res


class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        memo = [-1] * n
        memo[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            for j in range(i, n):
                memo[i] = max(memo[i], nums[j] + (0 if j + 2 >= n else memo[j + 2]))

        return memo[0]
