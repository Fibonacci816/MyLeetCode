# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = None
        self.flag = True
        
    def inorder(self, root):
        if root:
            if root.left:
                self.inorder(root.left)
            if self.pre is not None:
                self.flag = self.flag and root.val > self.pre
            self.pre = root.val
            if root.right:
                self.inorder(root.right)
        
    def isValidBST(self, root: TreeNode) -> bool:
        self.inorder(root)
        return self.flag
