from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        queue = deque()
        res = []
        if not root:
            return res
        queue.append((root, 0))
        while len(queue) > 0:
            ele = queue.popleft()
            level = ele[1]
            if len(res) == level:
                res.append([])
            res[level].append(ele[0].val)
            if ele[0].left:
                queue.append((ele[0].left, level + 1))
            if ele[0].right:
                queue.append((ele[0].right, level + 1))
        return res

    def levelOrder(self, root):
        res = []
        if not root:
            return res
        cur_index = deque()
        next_level = []
        cur_index.append(root)
        level = 0
        while len(cur_index) > 0:
            res.append([])
            while len(cur_index) > 0:
                ele = cur_index.popleft()
                res[level].append(ele.val)
                if ele.left:
                    next_level.append(ele.left)
                if ele.right:
                    next_level.append(ele.right)
                cur_index = next_level
                next_level = []
        return res