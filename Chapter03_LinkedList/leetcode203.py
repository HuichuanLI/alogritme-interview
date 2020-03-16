# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        dummyHead = dummyEnd = ListNode(None)
        dummyHead.next = head
        while dummyEnd.next:
            if dummyHead.next.val == val:
                dummyHead.next = dummyHead.next.next
            dummyHead = dummyHead.next
        return dummyEnd.next

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head != None:
            temp = ListNode(0)
            temp.next = head

            pp = temp
            pt = temp.next
            while pt != None:
                if pt.val == val:
                    pp.next = pt.next
                else:
                    pp = pt
                pt = pt.next
            return temp.next
