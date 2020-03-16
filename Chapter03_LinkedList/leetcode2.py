class Solution:
    def addTwoNumbers(self, l1, l2):
        i = 0
        flag = False
        head1 = l1
        head2 = l2
        reshead = res = ListNode(None)
        while head1 or head2:
            if not head1:
                if flag:
                    head2.val += 1
                    if head2.val >= 10:
                        head2.val = 0
                        flag = True
                    else:
                        flag = False
                res.next = head2
                res = res.next
                head2 = head2.next
            elif not head2:
                if flag:
                    head1.val += 1
                    if head1.val >= 10:
                        head1.val = 0
                        flag = True
                    else:
                        flag = False
                res.next = head1
                res = res.next
                head1 = head1.next
            else:
                if flag:
                    res.next = ListNode(head1.val + head2.val + 1)
                    if res.next.val >= 10:
                        res.next.val = (head1.val + head2.val + 1) % 10
                        flag = True
                    else:
                        flag = False
                else:
                    res.next = ListNode(head1.val + head2.val)
                    if head1.val + head2.val >= 10:
                        res.next.val = (head1.val + head2.val) % 10
                        flag = True
                head1 = head1.next
                head2 = head2.next
                res = res.next
        if flag:
            res.next = ListNode(1)
        return reshead.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 获得 l1 和 l2 的 integer 表示
        val1, val2 = [l1.val], [l2.val]

        while l1.next:
            val1.append(l1.next.val)
            l1 = l1.next
        while l2.next:
            val2.append(l2.next.val)
            l2 = l2.next

        # 求出 l1 和 l2 代表的数字
        num1 = ''.join([str(i) for i in val1[::-1]])
        num2 = ''.join([str(i) for i in val2[::-1]])

        # 得到 l1 和 l2 相加之和
        sums = int(num1) + int(num2)

        # 将 sums 转成题目中 linkedlist 所对应的表示形式
        sums = str(sums)[::-1]

        # dummy 作为返回结果
        dummy = head = ListNode(int(sums[0]))
        for i in range(1, len(sums)):
            head.next = ListNode(int(sums[i]))
            head = head.next
        return dummy

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 因为处理到最后的时候，可能输入的 l1 和 l2 都不是一个 ListNode 而是 None 了
        if not l1 and not l2:
            return
        elif not (l1 and l2):  # l1 和 l2 其中一个是 None
            return l1 or l2
        else:  # l1 和 l2 都不是 None
            if l1.val + l2.val < 10:  # 个位数相加没有进位
                l3 = ListNode(l1.val + l2.val)
                l3.next = self.addTwoNumbers(l1.next, l2.next)  # 递归调用
            else:  # # 个位数相加有进位
                l3 = ListNode(l1.val + l2.val - 10)
                # 递归调用，记得加上进位
                l3.next = self.addTwoNumbers(l1.next, self.addTwoNumbers(l2.next, ListNode(1)))
        return l3
