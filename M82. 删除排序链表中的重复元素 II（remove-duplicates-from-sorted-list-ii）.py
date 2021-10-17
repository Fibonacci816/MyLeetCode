# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 设置虚头，遍历过程中寻找有重复的节点全部删除
    # 时间O(n) 空间O(1)
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        head = ListNode(next=head)
        p, q = head, head.next
        while q and q.next:
            if q.val == q.next.val:
                target = q.val
                while q and q.val == target:
                    p.next = p.next.next
                    q = p.next
                continue
            p, q = p.next, q.next
        return head.next