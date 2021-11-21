# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tilt_sum = 0
    # 后序遍历
    # 时间O(n) 空间O(n)
    def findTilt(self, root: TreeNode) -> int:
        def post_order(root):
            if not root:
                return 0
            val_left= post_order(root.left)
            val_right = post_order(root.right)
            self.tilt_sum += abs(val_left - val_right)
            return root.val + val_left + val_right

        post_order(root)
        return self.tilt_sum
