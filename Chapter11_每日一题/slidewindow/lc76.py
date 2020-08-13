from collections import Counter


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0:
            return ""
        res = ""
        ans = sys.maxsize
        j = 0
        target_hash = Counter(t)
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        for i in range(len(s)):
            while j < len(s) and not needCnt == 0:
                if need[s[j]] > 0:
                    needCnt -= 1
                need[s[j]] -= 1
                j += 1
            if needCnt == 0:
                if ans > j - i + 1:
                    ans = j - i + 1
                    res = s[i:j]
                need[s[i]] += 1
                if need[s[i]] > 0:
                    needCnt += 1
        return res