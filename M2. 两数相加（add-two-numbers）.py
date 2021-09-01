# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 时间O(max(m, n)) 空间O(1)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        _add = 0
        head = c = ListNode()
        while p or q or _add:
            num1 = p.val if p else 0
            num2 = q.val if q else 0
            _sum = num1 + num2 + _add
            _add = _sum // 10
            c.next = ListNode(val=_sum%10)
            c = c.next
            if p:
                p = p.next
            if q:
                q = q.next
        return head.next
