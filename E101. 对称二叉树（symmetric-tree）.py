# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return root1.val == root2.val and self.isSame(root1.left, root2.right) and self.isSame(root1.right, root2.left)
    # 时间O(n) 空间O(n) 
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isSame(root.left, root.right)