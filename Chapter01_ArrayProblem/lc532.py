class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n == 0:
            return False
        res = [0] * (n + 1)
        result = set()
        for i in range(n):
            res[i + 1] = res[i] + nums[i]
            if (res[i + 1] - k) in result:
                return True
            result.add(res[i + 1])
        return False
