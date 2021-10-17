# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path_len = 0
    # 深度优先遍历求深度的过程中保存结果
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def get_path_len(root):
            if not root:
                return 0
            left_len = right_len = 0
            if root.left:
                left_len = get_path_len(root.left) + 1
            if root.right:
                right_len = get_path_len(root.right) + 1
            if (res := left_len + right_len) > self.path_len:
                self.path_len = res
            return max(left_len, right_len)
        get_path_len(root)
        return self.path_len
