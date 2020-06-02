from collections import defaultdict


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        return self.length(root.left) + self.length(root.right)

    def length(self, root):
        if not root:
            return 0
        left = self.length(root.left)
        right = self.length(root.right)
        return max(left, right) + 1


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        c = collections.defaultdict(int)
        c[0] = 1
        for num in nums:
            nxt = collections.defaultdict(int)
            for k, v in c.items():
                nxt[k - num] += v
                nxt[k + num] += v
            c = nxt
        return c[S]
