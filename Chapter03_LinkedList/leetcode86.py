class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """       
        dummy1_start = dummy1_end = ListNode(None) # before
        dummy2_start = dummy2_end = ListNode(None) # behind
        while head:
            if head.val < x:
                dummy1_end.next = head
                dummy1_end = dummy1_end.next
            else:
                dummy2_end.next = head
                dummy2_end = dummy2_end.next
            head = head.next
        # 从例子来看,因为dummy2_end最后指向5,它最开始还连着2呢,所以要置为空
        dummy2_end.next = None 
        dummy1_end.next = dummy2_start.next
        return dummy1_start.next