class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        if k == 0 or not head or k == 1:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        prev = dummyHead
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        cur = head
        next = head.next
        while length >= k:

            index = 0
            first = cur
            next = cur.next

            while index < k - 1:
                index += 1
                length -= 1
                next_next = next.next
                next.next = cur
                cur = next
                next = next_next
            prev.next = cur
            first.next = next
            cur = next
            # print(dummyHead.next,cur)
            prev = first
            length -= 1

        return dummyHead.next