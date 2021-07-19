# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def get_len(head):
            p = head
            n = 0
            while p:
                n += 1
                p = p.next
            return n
        
        l1, l2 = get_len(headA), get_len(headB)
        # 交换，使得headA为较短链表
        if l1 > l2:
            l1, l2 = l2, l1
            headA, headB = headB, headA
        p, q = headA, headB
        # 较长链表（headB）先移动比较短链表（headA）多的长度
        for i in range(l2 - l1):
            q = q.next
        # 一起移动直到相遇或都为空
        while q and q and p != q:
            p, q = p.next, q.next
        return p
