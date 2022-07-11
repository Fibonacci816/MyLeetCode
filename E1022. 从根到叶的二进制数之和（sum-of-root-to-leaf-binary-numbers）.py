# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    
    # dfs
    # 时间O(n) 空间O(n)
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    self.ans += int(path, 2)
                dfs(root.left, path)
                dfs(root.right, path)
        dfs(root, "")
        return self.ans

    # dfs
    # 时间O(n) 空间O(n)
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], val: int) -> int:
            if node is None:
                return 0
            val = (val << 1) | node.val
            if node.left is None and node.right is None:
                return val
            return dfs(node.left, val) + dfs(node.right, val)
        return dfs(root, 0)
