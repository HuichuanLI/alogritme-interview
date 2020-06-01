class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new_res = []
        index_i = 0
        index_j = 0
        mid = (len(nums1) + len(nums2)) // 2
        while index_i < len(nums1) or index_j < len(nums2):
            while index_i >= len(nums1):
                new_res.append(nums2[index_j])
                index_j += 1

            while index_j >= len(nums2):
                new_res.append(nums1[index_i])
                index_i += 1

            while index_i < mid and nums1[index_i] < nums2[index_j]:
                new_res.append(nums1[index_i])
                index_i += 1

            while index_j < mid and nums1[index_j] < nums2[index_i]:
                new_res.append(nums2[index_j])
                index_j += 1

        return new_res[mid]
