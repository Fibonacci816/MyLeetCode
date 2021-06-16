# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def levelOrderByLevel(root, level):
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            if root.left:
                levelOrderByLevel(root.left, level+1)
            if root.right:
                levelOrderByLevel(root.right, level+1)
        if root:
            levelOrderByLevel(root, 0)
        return res

    # 迭代
    def levelOrder2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        que = []
        if root:
            que.append(root)
        while que:
            n = len(que)
            res.append([])
            for i in range(n):
                node = que.pop(0)
                res[-1].append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return res