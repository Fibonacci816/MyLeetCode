# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 找到根节点，递归建立左右子树
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root_val = preorder[0]
        # 在中序遍历序列中查找根节点位置（可以通过建立Hash表优化时间复杂度）
        for i in range(len(inorder)):
            if inorder[i] == root_val:
                break
        root = TreeNode(val=root_val)
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root
