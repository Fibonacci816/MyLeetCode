# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# 双指针，其中一个先移动k位
	# 时间O(n) 空间O(1)
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p = q = head
        for i in range(k):
            q = q.next
        while q:
            p = p.next
            q = q.next
        return p