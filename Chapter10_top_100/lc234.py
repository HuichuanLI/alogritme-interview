class Solution:
    def isPalindrome(self, head: ListNode):
        res = []
        while head:
            res.append(head.val)
            head = head.next

        return res == list(reversed(res))