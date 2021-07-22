# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 时间O(n) 空间O(1)
    def detectCycle(self, head: ListNode) -> ListNode:
        p = q = head
        while q and q.next:
            p, q = p.next, q.next.next
            if p == q:
                p = head
                while p != q:
                    p, q = p.next, q.next
                return p
        return None
