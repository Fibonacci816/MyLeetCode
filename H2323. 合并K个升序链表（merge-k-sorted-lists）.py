# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two(head1, head2):
            cur = dummy_head = ListNode()
            p, q = head1, head2
            while p and q:
                if p.val < q.val:
                    node = ListNode(p.val)
                    p = p.next
                else:
                    node = ListNode(q.val)
                    q = q.next
                cur.next = node
                cur = cur.next
            if not p:
                cur.next = q
            else:
                cur.next = p
            return dummy_head.next

        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        # if n == 2:
        #     return merge_two(lists[0], lists[1])
        half = n // 2
        return merge_two(self.mergeKLists(lists[:half]), self.mergeKLists(lists[half:]))