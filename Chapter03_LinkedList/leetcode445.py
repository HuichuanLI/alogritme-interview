class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):

        val1, val2 = [l1.val], [l2.val]

        while l1.next:
            val1.append(l1.next.val)
            l1 = l1.next
        while l2.next:
            val2.append(l2.next.val)
            l2 = l2.next
        num1 = "".join([str(i) for i in val1])
        num2 = "".join([str(i) for i in val2])
        res = str(int(num1) + int(num2))

        dummy = head = ListNode(int(res[0]))
        for i in range(1, len(res)):
            head.next = ListNode(int(res[i]))
            head = head.next
        return dummy

    class Solution:
        def addTwoNumbers(self, l1, l2):
            nums1 = []
            nums2 = []
            res = []
            while l1:
                nums1.append(l1.val)
                l1 = l1.next
            while l2:
                nums2.append(l2.val)
                l2 = l2.next
            Flag = False
            while len(nums1) > 0 or len(nums2) > 0 or Flag:
                x = 0
                if len(nums1) > 0:
                    x += nums1.pop()
                if len(nums2) > 0:
                    x += nums2.pop()
                if Flag:
                    x += 1
                    Flag = False
                if x >= 10:
                    x = x - 10
                    Flag = True
                res.append(x)
            dummy = head = ListNode(None)

            for i in range(len(res)):
                head.next = ListNode(res[len(res) - i - 1])
                head = head.next
            return dummy.next