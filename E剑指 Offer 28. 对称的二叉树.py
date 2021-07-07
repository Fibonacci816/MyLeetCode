# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 判断每一层的节点值序列是否是对称
    def isSymmetric(self, root: TreeNode) -> bool:
        nodes_by_level = []  # 每一层一个数组存放所有节点值（包括None）
        def get_nodes_by_level(root, level):
            if len(nodes_by_level) == level:
                nodes_by_level.append([])
            if root:
                nodes_by_level[level].append(root.val)
                get_nodes_by_level(root.left, level + 1)
                get_nodes_by_level(root.right, level + 1)
            else:
                nodes_by_level[level].append(None)
        
        def is_symmetric(nodes):
            n = len(nodes)
            left, right = 0, n-1
            while left < right:
                if nodes[left] != nodes[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        get_nodes_by_level(root, 0)
        for nodes in nodes_by_level:
            if not is_symmetric(nodes):
                return False
        return True

    # 先判断左右子树是否对称，再判断左子树的左子树和右子树的右子树是否对称，且左子树的右子树和右子树的左子树是否对称
    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_symmetric(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return is_symmetric(left.left, right.right) and is_symmetric(left.right, right.left)
        return True if not root else is_symmetric(root.left, root.right)