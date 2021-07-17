# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self._sum = 0
    
    def dfs(self, root, _sum):
        _sum = 10 * _sum + root.val
        if not root.left and not root.right:
            self._sum += _sum
            return
        if root.left:
            self.dfs(root.left, _sum)
        if root.right:
            self.dfs(root.right, _sum)

    def sumNumbers(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return self._sum