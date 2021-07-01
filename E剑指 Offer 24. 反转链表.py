# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# 递归 时间O(n), 空间O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        p, q = None, head
        while q:
            q.next, p, q = p, q, q.next
        return p

    # 迭代 时间O(n), 空间O(n)
    def reverseList2(self, head: ListNode) -> ListNode:
    	if not head or not head.next:
            return head
        tail = self.reverseList(head.next)
        head.next.next, head.next = head, None
        return tail