class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """

        right = 1
        while reader.get(k) < target:
            right *= 2
        left = 0
        while left + 1 < right:
            mid = left + (right - left) // 2
            if reader.get(mid) > target:
                right = mid
            else:
                left = mid
        if reader.get(left):
            return left
        return right