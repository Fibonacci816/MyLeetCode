# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	# 存数组，再判断
	# 时间O(n) 空间O(n)
    def isPalindrome(self, head: ListNode) -> bool:
        nodes = []
        n = 0
        p = head
        while p:
            nodes.append(p.val)
            p = p.next
            n += 1
        for i in range(n//2):
            if nodes[i] != nodes[n-i-1]:
                return False
        return True

    # 找中点，反转后半部分，再判断
    # 时间O(n) 空间O(1)
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse_list(head):
            p, q = None, head
            while q:
                q.next, p, q = p, q, q.next
            return p
        def find_half(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        half = find_half(head)
        new_head = reverse_list(half.next)
        p, q = head, new_head
        while q:
            if p.val != q.val:
                return False
            p, q = p.next, q.next
        return True
