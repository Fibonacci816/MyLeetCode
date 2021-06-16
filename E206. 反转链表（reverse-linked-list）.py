# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, cur = None, head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        return prev

    # 递归
    def reverseList2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        r = head.next
        head.next = None
        new_head = self.reverseList(r)
        r.next = head
        return new_head