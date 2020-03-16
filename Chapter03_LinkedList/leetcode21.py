from collections import Counter


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next

        order = Counter(res)
        a = head = ListNode(None)
        for key, value in order.items():
            if value == 1:
                head.next = ListNode(key)
                head = head.next
        return a.next

    def deleteDuplicates(self, head):

        if head and head.next:
            dummyEnd = dummyHead = ListNode(0)
            dummyHead.next = head
            prev = dummyHead
            cur = head
            while prev.next:
                cur_val = cur.val
                if cur.next and cur.next.val == cur_val:
                    cur = cur.next
                prev.next = cur
                prev = prev.next
            return dummyHead.next

        else:
            return head
