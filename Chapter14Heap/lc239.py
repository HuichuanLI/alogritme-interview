import bisect


class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """

    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if n < k:
            return []
        deck = nums[:k]
        deck.sort()
        ans = [deck[-1]]
        for i in range(k, len(nums)):
            out = nums[i - k]
            inn = nums[i]
            deck.pop(bisect.bisect_left(deck, out))
            deck.insert(bisect.bisect_left(deck, inn), inn)
            ans.append(deck[-1])
        return ans
