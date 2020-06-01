class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        import functools
        @functools.lru_cache(None)
        def back_track(s):
            if (not s):
                return True
            res = False
            for i in range(1, len(s) + 1):
                if (s[:i] in wordDict):
                    res = back_track(s[i:]) or res
            return res

        return back_track(s)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if (dp[i] and (s[i:j] in wordDict)):
                    dp[j] = True
        return dp[-1]


if __name__ == "__main__":
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    print(Solution().wordBreak(s, wordDict))
