# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 中序遍历 + 归并
    # 时间O(m+n) 空间O(m+n)
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def in_order(root):
            return in_order(root.left) + [root.val] + in_order(root.right) if root else []

        def merge(seq1, seq2):
            n1, n2 = len(seq1), len(seq2)
            i1, i2 = 0, 0
            ans = []
            while i1 < n1 or i2 < n2:
                if i1 < n1 and (i2 >= n2 or seq1[i1] < seq2[i2]):
                    ans.append(seq1[i1])
                    i1 += 1
                else:
                    ans.append(seq2[i2])
                    i2 += 1
            return ans
        
        return merge(in_order(root1), in_order(root2))