class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt, n = 0, len(nums)
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1]
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if (pre[j] - pre[i - 1] == k): cnt += 1
        return cnt


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        acc = count = 0
        for num in nums:
            acc += num
            if acc == k:
                count += 1
            if acc - k in d:
                count += d[acc - k]
            if acc in d:
                d[acc] += 1
            else:
                d[acc] = 1
        return count
