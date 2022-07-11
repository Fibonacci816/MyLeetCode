# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归
    # 时间O(n) 空间O(n)
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif not root.left or not root.right:
            root = root.left if root.left else root.right
        else:
            succ = root.right
            while succ.left:
                succ = succ.left
            succ.right = self.deleteNode(root.right, succ.val)
            succ.left = root.left
            return succ
        return root