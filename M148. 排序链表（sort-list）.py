# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 合并两个有序链表
    def merge(self, head1: Optional[ListNode], head2: Optional[ListNode]):
        head = ListNode(next=head1)
        p, q = head, head2
        while p.next and q:
            if p.next.val < q.val:
                p = p.next
            else:
                tmp = q.next
                p.next, q.next = q, p.next
                p, q = q, tmp
        if p.next is None:
            p.next = q
        return head.next
    # 归并排序
    # 时间O(nlogn) 空间O(1)
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        p, q = head, head.next
        while q and q.next:
            p, q = p.next, q.next.next
        half, p.next = p.next, None
        return self.merge(self.sortList(head), self.sortList(half))
