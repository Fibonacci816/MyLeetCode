# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.paths = []
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def get_path(root, path, targetSum):
            if not root:
                return
            path.append(root.val)
            targetSum -= root.val
            if not root.left and not root.right:
                if targetSum == 0:
                    self.paths.append(path.copy())
            else:
                get_path(root.left, path, targetSum)
                get_path(root.right, path, targetSum)
            path.pop()
        get_path(root, [], targetSum)
        return self.paths
