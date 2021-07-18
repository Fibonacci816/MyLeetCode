"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # 广度优先遍历
    # 时间O(n) 空间O(n)
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        que = deque([(root, 1)])
        res = [[root.val]]
        while que:
            node, level = que.popleft()
            for child in node.children:
                que.append((child, level+1))
                if len(res) == level:
                    res.append([])
                res[level].append(child.val)
        return res

    # 每一层循环一次，每次循环得到当前层节点的所有children
    def levelOrder2(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        level_nodes = [root]
        while level_nodes:
            childrens = []
            for node in level_nodes:
                childrens.extend(node.children)
            level_nodes = childrens
            if level_nodes:
                res.append([child.val for child in childrens])
        return res