# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getLen(self, head):
        n = 0
        while head:
            n += 1
            head= head.next
        return n

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        # 一次翻转
        def reverseK(head, k):
            q = head.next
            p = None
            for i in range(k):
                q.next, p, q = p, q, q.next
            head.next.next = q
            tmp_head = head.next
            head.next = p
            return tmp_head
        n = self.getLen(head)
        head = ListNode(next=head)
        tmp_head = head
        for i in range(0, n, k):
            if n - i < k:
                break
            tmp_head = reverseK(tmp_head, k)
        return head.next
