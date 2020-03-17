from queue import PriorityQueue


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

    def mergeKLists(self, lists):
        head = point = ListNode(0)
        q = PriorityQueue()

        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            _, node = q.get()
            point.next = ListNode(node.val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next