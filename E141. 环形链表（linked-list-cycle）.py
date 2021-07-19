# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# 快慢指针
	# 时间O(n) 空间O(1)
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        p, q = head, head.next
        while p != q and q and q.next:
            p, q = p.next, q.next.next
        return p == q
