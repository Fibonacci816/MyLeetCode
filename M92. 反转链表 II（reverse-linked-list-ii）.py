# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 时间O(n)， 空间O(1)
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        head = ListNode(next=head)
        pre = head
        for i in range(left-1):
            pre = pre.next
        # 循环结束后，pre指向待翻转链表的前一个节点
        q = r = pre.next  # 待翻转链表的第一个节点
        p = None
        for i in range(left, right+1):
            q.next, p, q = p, q, q.next
        # 循环结束后，p指向待翻转链表的最后一个节点，q指向p的下一个节点
        pre.next = p
        r.next = q
        return head.next

    # 时间O(n)， 空间O(1)
    def reverseBetween2(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse_n(head, n):
            if n == 1:
                return head
            nex = head.next
            tail = reverse_n(nex, n-1)
            head.next = nex.next
            nex.next = head
            return tail
        head = ListNode(next=head)
        p = head
        for i in range(left-1):
            p = p.next
        p.next = reverse_n(p.next, right-left+1)
        return head.next
        
        