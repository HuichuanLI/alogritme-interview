# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         arr = []
#         Dummy_head = new_head = head
#         while head:
#             arr.append(head.val)
#             head = head.next
#         arr = list(sorted(arr))
#         for elem in arr:
#             new_head.val = elem
#             new_head = new_head.next
#         return Dummy_head
#
#
# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         h, length, intv = head, 0, 1
#         while h: h, length = h.next, length + 1
#         res = ListNode(0)
#         res.next = head
#         # merge the list in different intv.
#         while intv < length:
#             pre, h = res, res.next
#             while h:
#                 # get the two merge head `h1`, `h2`
#                 h1, i = h, intv
#                 while i and h: h, i = h.next, i - 1
#                 if i: break  # no need to merge because the `h2` is None.
#                 h2, i = h, intv
#                 while i and h: h, i = h.next, i - 1
#                 c1, c2 = intv, intv - i  # the `c2`: length of `h2` can be small than the `intv`.
#                 # merge the `h1` and `h2`.
#                 while c1 and c2:
#                     if h1.val < h2.val:
#                         pre.next, h1, c1 = h1, h1.next, c1 - 1
#                     else:
#                         pre.next, h2, c2 = h2, h2.next, c2 - 1
#                     pre = pre.next
#                 pre.next = h1 if c1 else h2
#                 while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
#                 pre.next = h
#             intv *= 2
#         return res.next
#
#
# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         self.sort(head, None)
#         return head
#
#     def sort(self, left, right):
#         if left == right or left.next == right:
#             return left
#         index = self.partition(left, right)
#         self.sort(left, index)
#         self.sort(index.next, right)
#
#     def partition(self, left, right):
#         # 前后指针法
#         value = left.val
#         pre = left
#         cur = left
#         while cur != right:
#             if cur.val < value:
#                 pre = pre.next
#                 pre.val, cur.val = cur.val, pre.val
#             cur = cur.next
#         pre.val, left.val = left.val, pre.val
#         return pre


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        # 归并排序--递归
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        print_node_list(mid)

        left = self.sortList(head)
        right = self.sortList(mid)
        # print(mid.val, left.val, right.val)
        return self.merge(left, right)

    def getMid(self, head):
        if not head or not head.next:
            return head
        pre = head
        slow = head.next
        fast = head.next
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        print(slow.val)
        pre.next = None
        return slow

    def merge(self, left, right):
        res = ListNode(-1)
        pre = res
        while left and right:
            if left.val <= right.val:
                pre.next = left
                left = left.next
            else:
                pre.next = right
                right = right.next
            pre = pre.next
            # 这一步是在消除left,right原链表的连接
            pre.next = None
        if left:
            pre.next = left
        if right:
            pre.next = right
        return res.next


def create_node_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head


def print_node_list(head):
    while head:
        print(head.val, '->', end=' ')
        head = head.next
    print('NULL')


if __name__ == "__main__":
    arr = [4, 2, 1, 3, 5, 6]
    head = create_node_list(arr)
    print_node_list(head)

    solution = Solution2()
    result = solution.sortList(head)
    print_node_list(result)
