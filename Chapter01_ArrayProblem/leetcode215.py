import heapq


class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, -nums[i])
        for i in range(k):
            if i == k - 1:
                return -heapq.heappop(heap)
            heapq.heappop(heap)

    # - 时间复杂度: O(Nlgk) - 空间复杂度: O(k)
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        from heapq import *
        heap = []
        for i in range(len(nums)):
            heappush(heap, nums[i])
            if len(heap) > k:
                heappop(heap)
        return heap[0]

    def findKthLargest(self, nums, k):
        pivot = nums[0]
        smaller = [num for num in nums if num < pivot]
        equal = [num for num in nums if num == pivot]
        greater = [num for num in nums if num > pivot]
        if len(greater) >= k:
            return self.findKthLargest(greater, k)  # k may be there
        elif len(equal) >= (k - len(greater)):  # k may be in equal or smaller
            return equal[0]  # any number from equal
        else:
            return self.findKthLargest(smaller, k - len(greater) - len(equal))
