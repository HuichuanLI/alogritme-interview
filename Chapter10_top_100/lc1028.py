import re


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        self.match = [(len(i[0]), int(i[1])) for i in re.findall(r'(-*)(\d+)', S)]
        root = TreeNode(self.match[0][1])
        stack = [(0, root)]
        for i in range(1, len(self.match[1:]) + 1):
            while self.match[i][0] != stack[-1][0] + 1:
                stack.pop()
            if not stack[-1][1].left:
                stack[-1][1].left = TreeNode(self.match[i][1])
                stack.append((self.match[i][0], stack[-1][1].left))
            else:
                stack[-1][1].right = TreeNode(self.match[i][1])
                stack.append((self.match[i][0], stack[-1][1].right))
        return stack[0][1]


if __name__ == "__main__":
    Solution().recoverFromPreorder("1-2--3--4-5--6--7")
