"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        return [node for child in root.children for node in self.postorder(child)] + [root.val] if root else []
        # return list(chain(*[self.postorder(child) for child in root.children])) + [root.val] if root else []
        # return (list(reduce(list.__add__, [self.postorder(child) for child in root.children])) if root.children else []) + [root.val] if root else []