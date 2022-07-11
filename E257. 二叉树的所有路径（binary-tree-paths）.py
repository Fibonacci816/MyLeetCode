# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # dfs + 回溯
    # 时间O(nlogn) 空间O(logn) 其中path存储根到叶子节点的路径，空间复杂度为logn；遍历到叶子节点join的时间复杂度为logn
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path, paths = [], []
        def dfs(root):
            if root:
                path.append(root.val)
                if not root.left and not root.right:
                    paths.append('->'.join(map(str, path)))
                else:
                    dfs(root.left)
                    dfs(root.right)
                path.pop()
        dfs(root)
        return paths
