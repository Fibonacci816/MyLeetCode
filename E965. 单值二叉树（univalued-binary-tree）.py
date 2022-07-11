# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.val = None

    # 时间O(n) 空间O(n)
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root:
            if self.val is None:
                self.val = root.val
            return root.val == self.val and self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        return True