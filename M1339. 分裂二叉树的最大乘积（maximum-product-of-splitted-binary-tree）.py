# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self._sum = 0
        self.sub = 0

    # dfs
    # 时间O(n) 空间O(1)
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs_sum(root):
            return root.val + dfs_sum(root.left) + dfs_sum(root.right) if root else 0

        self._sum = dfs_sum(root)

        def dfs(root):
            if not root:
                return 0
            sub = root.val + dfs(root.left) + dfs(root.right)
            if abs(2 * sub - self._sum) < abs(2 * self.sub - self._sum):
                self.sub = sub
            return sub

        dfs(root)
        return self.sub * (self._sum - self.sub) % int(1e9 + 7)
