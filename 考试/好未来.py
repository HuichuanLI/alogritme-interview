class Solution:
    def rotateRight(self, head, k):
        # base cases
        if not head:
            return None
        if not head.next:
            return head

        dummyHead = head
        n = 1
        while dummyHead.next:
            dummyHead = dummyHead.next
            n += 1
        dummyHead.next = head

        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        new_tail.next = None

        return new_head
