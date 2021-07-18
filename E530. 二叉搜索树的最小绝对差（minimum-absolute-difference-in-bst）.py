# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.min_abs = float('inf')
        self.inorder_list = []  # 存放中序遍历序列
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.inorder_list.append(root.val) 
        self.inorder(root.right)
    # 中序遍历得到递增序列，然后后减前的到差值，取最小差值即为所求
    # 也可以声明一个pre存放前一个访问的节点值，中序遍历过程中用当前节点值减去pre也能得到递增序列差值
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.inorder(root)
        n = len(self.inorder_list)
        for i in range(1, n):
            self.min_abs = min(self.min_abs, self.inorder_list[i] - self.inorder_list[i-1])
        return self.min_abs