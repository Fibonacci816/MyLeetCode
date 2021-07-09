"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    # 后序遍历
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def postorder(root):
            if not root:
                return None, None
            head_l, tail_l = postorder(root.left)
            head_r, tail_r = postorder(root.right)
            # 改变指针，使成为有序双向链表
            if tail_l:
                root.left = tail_l
                tail_l.right = root
            if head_r:
                root.right = head_r
                head_r.left = root
            # 双向链表的头尾
            head = head_l if head_l else root
            tail = tail_r if tail_r else root
            return head, tail
        if not root:
            return None
        head, tail = postorder(root)
        # 使尾部节点的后继为头部节点，头部节点的前驱为尾部节点
        # 这一步非常重要！因为后序遍历过程中没有这一步操作
        tail.right = head
        head.left = tail
        return head

    # 中序遍历
    def treeToDoublyList2(self, root: 'Node') -> 'Node':
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            # 只有遍历到最左节点条件才成立，该节点为head
            if not self.pre:
                self.head = root
            else:
                self.pre.right, root.left = root, self.pre
            self.pre = root
            inorder(root.right)
        if not root:
            return None
        self.pre = None  # 记录上一次访问节点
        inorder(root)  # 执行后self.pre为最右节点，即tail
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
        