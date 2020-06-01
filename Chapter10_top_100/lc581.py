class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        array = list(sorted(nums))
        index_start = -1
        index_end = -1
        for index, (elemx, elemy) in enumerate(zip(array, nums)):
            if elemx != elemy and index_start == -1:
                index_start = index
            if elemx != elemy and index_start != -1:
                index_end = index
        return index_end - index_start

