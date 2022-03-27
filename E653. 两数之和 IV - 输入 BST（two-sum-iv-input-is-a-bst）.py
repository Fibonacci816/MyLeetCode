# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 中序遍历 + 双指针
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ordered_seq = []
        def in_order(root):
            if not root:
                return
            in_order(root.left)
            ordered_seq.append(root.val)
            in_order(root.right)
        in_order(root)
        start, end = 0, len(ordered_seq) - 1
        while start < end:
            _sum = ordered_seq[start] + ordered_seq[end]
            if _sum == k:
                return True
            elif _sum < k:
                start += 1
            elif _sum > k:
                end -= 1
        return False

# 哈希表
class Solution:
    def __init__(self):
        self.vals = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return (k - root.val in self.vals or self.vals.add(root.val)) or self.findTarget(root.left, k) or self.findTarget(root.right, k) if root else False
