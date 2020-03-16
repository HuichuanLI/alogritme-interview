class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        start1 = head
        index = 0
        while head:
            head = head.next
            index += 1
        n = index - n + 1
        start = prev = ListNode(0)
        prev.next = start1
        index = 0
        while index < n - 1:
            prev = prev.next
            index += 1
        prev.next = prev.next.next
        return start.next

    def removeNthFromEnd(self, head, n):

        if n <= 0:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        q = p = dummyHead

        for i in range(n + 1):
            p = p.next
        while p:
            p = p.next
            q = q.next
        q.next = q.next.next
        return dummyHead.next
