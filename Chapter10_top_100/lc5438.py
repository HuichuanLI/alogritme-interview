from sklearn.preprocessing import PolynomialFeatures

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        left = max(1, min(bloomDay))
        right = min(10 ** 9, max(bloomDay))
        memo = -1
        while left <= right:
            mid = left + (right - left) // 2
            bloomDay_ok = list(map(lambda x: x <= mid, bloomDay))
            r = 0
            ans = 0
            s = 0
            while r < len(bloomDay_ok):
                if not bloomDay_ok[r]:
                    ans += (r - s) // k
                    s = r + 1
                r += 1
            ans += (r - s) // k
            if ans >= m:
                memo = mid
                right = mid - 1
            else:
                left = mid + 1

        return memo


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(day):
            n = len(bloomDay)
            flower = [True if v <= day else False for v in bloomDay]
            s, t = 0, 0
            count = 0
            while t < n:
                if not flower[t]:
                    count += (t - s) // k
                    s = t + 1
                t += 1
            count += (t - s) // k
            return count >= m

        left, right = min(bloomDay), max(bloomDay)
        while left <= right:
            day = (left + right) // 2
            if check(day):
                right = day - 1
            else:
                left = day + 1
        return left if check(left) else -1
