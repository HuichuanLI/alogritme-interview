from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(s) < len(p):
            return ans
        cntP = Counter(p)
        cnt = Counter(s[:len(s)])

        if cnt == cntP:
            ans.append(0)
        for i in range(len(p), len(s)):
            cnt[s[i]] += 1
            cnt[s[i - len(p)]] -= 1
            if cnt == cntP:
                ans.append(i - len(p) + 1)

        return  ans
