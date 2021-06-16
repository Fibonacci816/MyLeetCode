# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        fathers = {root.val: (-1, -1)}
        def get_father(root, level):
            if root.left:
                fathers[root.left.val] = (root, level)
                get_father(root.left, level+1)
            if root.right:
                fathers[root.right.val] = (root, level)
                get_father(root.right, level+1)
        
        get_father(root, 0)
        while p.val != q.val:
            if fathers[p.val][1] > fathers[q.val][1]:
                p = fathers[p.val][0]
            else:
                q = fathers[q.val][0]
        return p