class Solution:
    def canCross(self, stones: List[int]) -> bool:

        # corner case
        if len(stones) <= 1:
            return True
        if not (stones[0] == 0 and stones[1] == 1):
            return False
            # 初始化dp数组
        dp = {}
        for stone in stones:
            dp[stone] = set()
        dp[0].add(1)

        for s in stones:
            for step in dp[s]:
                if step > 1 and s + step - 1 in dp:
                    dp[s + step - 1].add(step - 1)
                if step + s in dp:
                    dp[s + step].add(step)
                if step + s + 1 in dp:
                    dp[s + step + 1].add(step + 1)
        return len(dp[stones[-1]]) > 0
