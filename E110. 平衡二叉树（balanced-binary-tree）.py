# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag = True
    def isBalanced(self, root: TreeNode) -> bool:
        def get_height(root):
            if not root:
                return 0
            height_left = get_height(root.left)
            height_right = get_height(root.right)
            if abs(height_left - height_right) > 1:
                self.flag = False
            return max(height_left, height_right) + 1
        
        get_height(root)
        return self.flag
