class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 为了方便编写代码，这里将第 k 大转换成第 k 小问题。
        k = n - k
        return self.partition(nums, 0, n - 1, k)

    def partition(self, nums, start, end, k):
        left, right = start, end
        pivot = nums[left]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if k < right:
            return self.partition(nums, start, right, k)
        if k > left:
            return self.partition(nums, left, end, k)
        return nums[k]
