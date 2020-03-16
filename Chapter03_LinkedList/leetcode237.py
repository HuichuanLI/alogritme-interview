class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node:
            return

        node.val = node.next.val
        node.next = node.next.next

        return 