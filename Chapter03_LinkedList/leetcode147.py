class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        # dumy 是一个新的节点
        cur = head
        while cur:
            nxt = cur.next
            temp = dummy
            while temp.next and temp.next.val < cur.val:
                temp = temp.next
            cur.next = temp.next
            temp.next = cur
            cur = nxt
        return dummy.next