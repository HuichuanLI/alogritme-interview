class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution:
    def rightSideView(self, root):
        res = []
        if not root:
            return res
        queue = deque()
        queue.append((root, 0))
        while len(queue) > 0:
            ele = queue.popleft()
            level = ele[1]
            if len(res) == level:
                res.append(ele[0].val)
            else:
                res[level] = ele[0].val
            if ele[0].left:
                queue.append((ele[0].left,level+1))
            if ele[0].right:
                queue.append((ele[0].right,level+1))
        return  res