# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	# 判断当前节点的值和下一个节点的值是否相等，相等则删除，否则移动到下一个节点
	# 时间O(n) 空间O(1)
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head