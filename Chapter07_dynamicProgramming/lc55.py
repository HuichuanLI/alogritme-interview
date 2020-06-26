class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = [False] * (len(nums))
        res[0] = True
        for i in range(len(nums)):
            for j in range(i, -1, -1):
                if res[j] and j + nums[j] >= i:
                    res[i] = True
                    break
        return res[-1]


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # 从倒数第二个数往前遍历
        end = len(nums) - 1
        i = len(nums) - 2

        while i >= 0:
            if nums[i] >= end - i:
                end = i
            i -= 1

        return end == 0
