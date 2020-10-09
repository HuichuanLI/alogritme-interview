class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l + 1 < r:
            mid = l + (r - l) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                r = mid - 1
            else:
                l = mid + 1
        if guess(l) == 0:
            return l
        if guess(r) == 0:
            return r
        return -1
