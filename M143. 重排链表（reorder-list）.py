# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverseList(head):
            p, q = None, head
            while q:
                q.next, p, q = p, q, q.next
            return p
            
        if not head:
            return None
        h1 = h2 = head
        # 寻找链表中间节点（h1所指位置）
        while h2.next and h2.next.next:
            h1, h2 = h1.next, h2.next.next
        
        # 分割链表（l1.length == l2.length or l1.length == l2.length + 1）
        l2 = h1.next
        h1.next = None
        l1 = head
        # 翻转后半部分链表
        l2 = reverseList(l2)
        # 合并前后两部分链表
        while l2:
            l1.next, l2.next, l1, l2 = l2, l1.next, l1.next, l2.next
        return head


    # 二刷
    def reorderList2(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(head):
            p, q = None, head
            while q:
                q.next, p, q = p, q, q.next
            return p

        def find_half(head):
            p, q = head, head.next
            while q and q.next:
                p = p.next
                q = q.next.next
            return p

        half = find_half(head)
        head2 = reverse(half.next)
        half.next = None
        head1 = head
        while head2:
            head1.next, head2.next, head1, head2 = head2, head1.next, head1.next, head2.next
        return head