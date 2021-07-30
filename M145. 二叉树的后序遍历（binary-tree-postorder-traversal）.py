# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 两状态转移
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        postorder = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append([node, 1])
                node = node.left
            node, state = stack.pop()
            if state:
                stack.append([node, 0])
                node = node.right
            else:
                postorder.append(node.val)
                node = None           
        return postorder

    # 三状态转移
    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        stack1 = []
        stack2 = []
        if root is None:
            return []
        postorder = []
        stack1.append(root)
        stack2.append(0)
        while stack1 != []:
            status = stack2.pop()
            if status == 0:
                stack2.append(1)
                if stack1[-1].left:
                    stack1.append(stack1[-1].left)
                    stack2.append(0)
            elif status == 1:
                stack2.append(2)
                if stack1[-1].right:
                    stack1.append(stack1[-1].right)
                    stack2.append(0)
            else:
                postorder.append(stack1.pop().val)
        return postorder