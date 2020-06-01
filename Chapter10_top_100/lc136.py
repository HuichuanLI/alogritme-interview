class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return(sum(set(nums))*2-sum(nums))


from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return(Counter(nums).most_common(len(nums))[-1][0])