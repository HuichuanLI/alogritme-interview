# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # O(N) O（1）
    def reverseList(self, head):
        prev = None
        cur = head
        while cur != None:
            ne = cur.next
            cur.next = prev
            prev = cur
            cur = ne
        return prev
