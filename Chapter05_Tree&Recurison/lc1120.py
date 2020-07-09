import sys


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        path = []
        self.dfs(root, path)
        return max(path)

    def dfs(self, node, averages):
        if not node:
            return -sys.maxsize, 0
        left_average = self.dfs(node.left, averages)
        right_average = self.dfs(node.right, averages)

        current_average = (left_average[0] * left_average[1] + right_average[0] * right_average[1] + node.val) / (
                left_average[1] + right_average[1] + 1)
        averages.append(current_average)

        return current_average, (left_average[1] + right_average[1] + 1)
