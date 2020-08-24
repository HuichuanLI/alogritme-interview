class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # 第i个位置的信息
        res = [0] * (n + 1)
        res[1] = nums[0]

        for i in range(2, n + 1):
            res[i] = max(res[i - 1], res[i - 2] + nums[i - 1])
        return res[-1]


# imporoved


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # 第i个位置的信息
        res = [0] * (3)
        res[1] = nums[0]

        for i in range(2, n + 1):
            res[i % 3] = max(res[(i - 1) % 3], res[(i - 2) % 3] + nums[i - 1])
        return res[n % 3]
