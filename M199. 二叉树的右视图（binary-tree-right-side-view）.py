# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root, level):
            if not root:
                return 
            if len(res) == level:
                res.append(root.val)
            if root.right:
                dfs(root.right, level+1)
            if root.left:
                dfs(root.left, level+1)
        
        dfs(root, 0)
        return res