class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """

    def maxCoins(self, nums):
        if not nums:
            return 0

        # [4,1,5] => [1,4,1,5,1]
        nums = [1, *nums, 1]
        return self.memo_search(nums, 0, len(nums) - 1, {})

    def memo_search(self, nums, i, j, memo):
        if i == j:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        best = 0
        for k in range(i + 1, j):
            left = self.memo_search(nums, i, k, memo)
            right = self.memo_search(nums, k, j, memo)
            best = max(best, left + right + nums[i] * nums[k] * nums[j])

        memo[(i, j)] = best
        return best
