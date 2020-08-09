# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        Flag = 1
        res = []
        while len(queue) > 0:
            size = len(queue)
            cur_res = []
            for _ in range(size):
                cur_ = queue.popleft()

                cur_res.append(cur_.val)
                if cur_.left:
                    queue.append(cur_.left)
                if cur_.right:
                    queue.append(cur_.right)

            Flag = 1 - Flag
            if Flag == 0:
                res.append(cur_res)
            else:
                res.append(list(reversed(cur_res)))
        return res


    def difference(a,b):
        dif = 0
        for i,j in zip(a,b):
            if i != j:
                dif+=1
        return dif