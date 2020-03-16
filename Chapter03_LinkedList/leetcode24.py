# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        if head and head.next:
            dummyHead = ListNode(0)
            dummyHead.next = head
            p = dummyHead
            node1 = head
            node2 = head.next
            while node1 and node2:
                next = node2.next
                node2.next = node1
                p.next = node2
                node1.next = next
                p = node1
                node1 = p.next
                node2 = p.next.next
            return dummyHead
        else:
            return head
