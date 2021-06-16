# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodes_by_level = []
        def levelOrder(root, level):
            if len(nodes_by_level) == level:
                nodes_by_level.append([])
            if level % 2:
                nodes_by_level[level].insert(0, root.val)
            else:
                nodes_by_level[level].append(root.val)
            if root.left:
                levelOrder(root.left, level+1)
            if root.right:
                levelOrder(root.right, level+1)
        
        if root:
            levelOrder(root, 0)
        return nodes_by_level
