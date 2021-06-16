# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 获得第一个大于等于target的结点位置
    def get_greater(self, lists: List[ListNode], target: int) -> int:
        left, right = 0, len(lists) - 1
        while left <= right:
            mid = (left + right) >> 1
            if lists[mid].val == target:
                return mid
            if lists[mid].val < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        # 删除空链表
        i = 0
        while i < n:
            if not lists[i]:
                lists.pop(i)
                n -= 1
            else:
                i += 1
        res = ListNode()
        p = res
        # 排序以便二分查找插入结点
        lists.sort(key=lambda x: x.val)
        while len(lists) > 0:
            p.next = lists[0]
            p = p.next
            lists[0] = lists[0].next
            # 如果链表移动到末尾则删除它
            if not lists[0]:
                lists.pop(0)
                continue
            # 根据头结点数值大小，将当前链表插入到列表的合适位置以保证链表按头结点数值排序
            if len(lists) > 1:
                target = lists.pop(0)
                insert_idx = self.get_greater(lists, target.val)
                lists.insert(insert_idx, target)
        return res.next

    # 以下是较为简单粗暴的方法，每次查找最小的头结点
    def getMinIdx(self, lists: List[ListNode]) -> int:
        min_idx = -1
        min_val = float('inf')
        for idx, node in enumerate(lists):
            if node and node.val < min_val:
                min_val = node.val
                min_idx = idx
        return min_idx

    def mergeKLists_Rough(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        res = ListNode()
        p = res
        while n > 0:
            min_idx = self.getMinIdx(lists)
            if min_idx == -1:
                break
            p.next = lists[min_idx]
            p = p.next
            lists[min_idx] = lists[min_idx].next
            if lists[min_idx] is None:
                n -= 1
        return res.next