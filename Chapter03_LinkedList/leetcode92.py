# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        if not head or m == n:
            return head
        node_m_before = dummy = ListNode(-1)
        dummy.next = head

        for i in range(m - 1):
            node_m_before = node_m_before.next
        node_m = node_m_before.next

        prev = None
        cur = node_m_before.next
        for i in range(n - m + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        node_m_before.next = prev
        node_m.next = cur

        return dummy.next
