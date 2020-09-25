class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0
        dp = [0] * (len(nums) + 1)
        n = len(nums)
        dp[1] = nums[0]
        lcs = 1

        for i in range(1, n):
            if nums[i] > dp[lcs]:
                lcs += 1
                dp[lcs] = nums[i]
            else:
                l = 0
                r = lcs
                while l + 1 < r:
                    mid = l + (r - l) // 2
                    if dp[mid] >= nums[i]:
                        r = mid
                    else:
                        l = mid + 1
                if dp[l] >= nums[i]:
                    dp[l] = min(dp[l], nums[i])
                else:
                    dp[r] = min(dp[r], nums[i])
        return lcs
