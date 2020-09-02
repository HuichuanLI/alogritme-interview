class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n == 0:
            return False
        res = [0] * (n + 1)
        for i in range(n):
            res[i + 1] = res[i] + nums[i]
            for j in range(i):
                if k != 0 and (res[i + 1] - res[j]) % k == 0:
                    return True
                if k == 0 and res[i + 1] - res[j] == 0:
                    return True
        return False
