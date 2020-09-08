# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        ov = 0
        while p1 and p2:
            p1.val += p2.val + ov
            ov = p1.val // 10
            p1.val = p1.val % 10
            if not p1.next or not p2.next: break
            p1 = p1.next
            p2 = p2.next

        if not p1.next and p2:
            p1.next = p2.next

        while p1.next and ov:
            p1.next.val += ov
            ov = p1.next.val // 10
            p1.next.val = p1.next.val % 10
            p1 = p1.next

        if ov:
            p1.next = ListNode(ov)
        return l1
