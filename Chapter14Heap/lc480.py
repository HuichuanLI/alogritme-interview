import bisect


class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """

    def medianSlidingWindow(self, nums, k):
        n = len(nums)
        if n < k:
            return []
        deck = nums[:k]
        deck.sort()
        if k % 2 != 0:
            mid = (k - 1) // 2
            ans = [deck[mid]]
        else:
            mid = ((k - 1) // 2, (k - 1) // 2 + 1)
            ans = [(deck[mid[0]] + deck[mid[1]]) / 2]

        for i in range(k, len(nums)):
            out = nums[i - k]
            inn = nums[i]
            deck.pop(bisect.bisect_left(deck, out))
            deck.insert(bisect.bisect_left(deck, inn), inn)
            if k % 2 != 0:
                ans.append(deck[mid])
            else:
                ans.append((deck[mid[0]] + deck[mid[1]]) / 2)
        return ans
