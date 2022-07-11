# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = -inf

    # 递归
    # 时间O(n) 空间O(n)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def path_sum(root):
            if not root:
                return 0
            left_sum = max(0, path_sum(root.left))
            right_sum = max(0, path_sum(root.right))
            self.ans = max(self.ans, root.val + left_sum + right_sum)
            return root.val + max(left_sum, right_sum)
    
        path_sum(root)
        return self.ans