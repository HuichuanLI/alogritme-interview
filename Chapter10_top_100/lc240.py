class Solution:
    def search_bi(self, nums, a, left, right):
        if left > right:
            return False
        mid = left + (right - left) // 2
        if nums[mid] == a:
            return True
        elif nums[mid] > a:
            return self.search_bi(nums, a, left, mid - 1)
        else:
            return self.search_bi(nums, a, mid + 1, right)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for elm in matrix:
            if self.search_bi(elm,target,0,len(elm)-1):
                return True
        return False
