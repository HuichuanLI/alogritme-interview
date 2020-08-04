# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        start = 0
        end = 1
        while reader.get(end) < target:
            end *= 2

        while start + 1 < end:
            mid = start + (end - start) // 2
            if target <= reader.get(mid):
                end = mid
            else:
                start = mid

        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end

        return -1
