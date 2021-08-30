# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 时间O(n) 空间O(1)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head = ListNode(next=head)
        p = q = head
        for i in range(n):
            q = q.next
        while q.next:
            p, q = p.next, q.next
        p.next = p.next.next
        return head.next
