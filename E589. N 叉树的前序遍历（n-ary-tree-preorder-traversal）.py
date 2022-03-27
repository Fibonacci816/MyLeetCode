"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # 递归
    def preorder(self, root: 'Node') -> List[int]:
        pre_list = []
        def pre_search(root):
            if root:
                pre_list.append(root.val)
                for child in root.children:
                    pre_search(child)
        pre_search(root)
        return pre_list

    # 迭代
    def preorder(self, root: 'Node') -> List[int]:
        pre_list = []
        if root:
            s = [root]
            while s:
                node = s.pop()
                pre_list.append(node.val)
                if node.children:
                    s.extend(reversed(node.children))
        return pre_list