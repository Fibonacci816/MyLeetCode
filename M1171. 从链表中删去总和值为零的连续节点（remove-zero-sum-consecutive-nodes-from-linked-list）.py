# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 第一次遍历存放前缀和的位置，相同前缀和保留最后的位置
    # 第二次遍历将节点的next指向和其前缀和相同的节点的下一个节点，因为前缀和相等意味着中间连续节点的和为0
    # 时间O(n) 空间O(n)
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        head = ListNode(next=head)
        pre_sum = {}
        p = head
        s = 0
        while p:
            s += p.val
            pre_sum[s] = p
            p = p.next
        p = head
        s = 0
        while p:
            s += p.val
            p.next = pre_sum[s].next
            p = p.next
        return head.next