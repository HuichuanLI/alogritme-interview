from collections import Counter


class Solution:
    def intersect(self, nums1, nums2):
        a = Counter(nums1)
        b = Counter(nums2)
        result = []
        for ele in a.keys():
            if ele in b.keys():
                result.extend([ele] * min(a[ele], b[ele]))
        return result
