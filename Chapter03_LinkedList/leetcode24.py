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


class Solution:
    def swapPairs(self, head):
        if head and head.next:
            dummyHead = ListNode(0)
            dummyHead.next = head
            pre = dummyHead
            cur = head
            next = head.next
            while cur and next:
                next_next = next.next
                pre.next = next
                next.next = cur
                cur.next = next_next
                cur = cur.next
                next = cur.next
            return dummyHead.next
        else:
            return head
