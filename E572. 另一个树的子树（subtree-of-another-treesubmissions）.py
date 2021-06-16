# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def isEqual(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return isEqual(root1.left, root2.left) and isEqual(root1.right, root2.right)
        
        # def getHead(root):
        #     if not root:
        #         return []
        #     return ([root] if root.val == subRoot.val else []) + getHead(root.left) + getHead(root.right)

        # heads = getHead(root)
        # flag = False
        # for head in heads:
        #     if isEqual(head, subRoot):
        #         flag = True
        # return flag

        def isSub(root):
            if not root:
                return False
            return (isEqual(root, subRoot) if root.val == subRoot.val else False) or isSub(root.left) or isSub(root.right)

        return isSub(root)


