# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        max_value = max(nums)
        node = TreeNode(max_value)
        node.left = self.constructMaximumBinaryTree(nums[:nums.index(max_value)])
        node.right = self.constructMaximumBinaryTree(nums[nums.index(max_value) + 1:])
        return node
