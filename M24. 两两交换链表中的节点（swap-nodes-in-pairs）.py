# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 迭代
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre, p = None, head
        head = head.next
        while p and p.next:
            q = p.next
            if pre:
                pre.next = q
            q.next, p.next = p, q.next
            pre, p = p, p.next
        return head

    # 递归
    def swapPairs2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = head.next
        head.next, new_head.next = self.swapPairs(new_head.next), head
        return new_head