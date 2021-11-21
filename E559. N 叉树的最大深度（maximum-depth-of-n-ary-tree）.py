"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # dfs
    # 时间O(n) 空间O(depth)
    def maxDepth(self, root: 'Node') -> int:
        return 1 + max([self.maxDepth(child) for child in root.children], default=0) if root else 0