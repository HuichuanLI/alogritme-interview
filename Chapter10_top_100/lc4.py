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
        mid = (len(nums1) + len(nums2))
        two_res = False
        if mid % 2 == 0:
            two_res = True

        mid = mid // 2
        while len(new_res) <= mid:
            if index_i >= len(nums1):
                new_res.append(nums2[index_j])
                index_j += 1
            elif index_j >= len(nums2):
                new_res.append(nums1[index_i])
                index_i += 1
            elif nums1[index_i] <= nums2[index_j]:
                new_res.append(nums1[index_i])
                index_i += 1
            else:
                new_res.append(nums2[index_j])
                index_j += 1
        if two_res:
            return (new_res[-1] + new_res[-2]) / 2
        return new_res[-1]

        return 0