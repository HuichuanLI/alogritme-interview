# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        dummy = head
        cur = head
        while cur != None:
            next = cur.next
            while next != None and cur.val == next.val:
                next = next.next
            cur.next = next
            cur = next
        return dummy