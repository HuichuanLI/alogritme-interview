class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        arr = []
        Dummy_head = new_head = head
        while head:
            arr.append(head.val)
            head = head.next
        arr = list(sorted(arr))
        for elem in  arr:
            new_head.val = elem
            new_head = new_head.next
        return Dummy_head
            