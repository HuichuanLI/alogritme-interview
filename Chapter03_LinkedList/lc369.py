# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        not_nine = sentinel

        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

        not_nine.val += 1
        not_nine = not_nine.next

        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next

        return sentinel if sentinel.val else sentinel.next
