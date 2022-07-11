# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 中序遍历
    # 时间O(n) 空间O(n)
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        stack = []
        node = root
        pre = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if pre == p: 
                return node
            pre, node = node, node.right
        return None

    # 利用二叉搜索树性质，当前节点值大于目标节点值时，移到左子树，否则移到右子树
    # 时间：平均O(logn)， 最差O(n) 空间 O(1)
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        ans, cur = None, root
        while cur:
            if cur.val > p.val:
                ans, cur = cur, cur.left
            else:
                cur = cur.right
        return ans