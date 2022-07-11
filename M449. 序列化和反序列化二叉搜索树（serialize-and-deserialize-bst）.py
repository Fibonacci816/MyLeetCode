# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # 前/后序遍历（前/后 + 中 -> Tree，中序排序可得）
    # 时间O(n) 空间O(n)
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        arr = []
        def post_order(root):
            if root:
                post_order(root.left)
                post_order(root.right)
                arr.append(root.val)
        post_order(root)
        return ' '.join(map(str, arr))
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        arr = list(map(int, data.split()))
        def construct(low, up):
            if not arr or arr[-1] < low or arr[-1] > up:
                return None
            val = arr.pop()
            node = TreeNode(val)
            node.right = construct(val, up)
            node.left = construct(low, val)
            return node
        return construct(-inf, inf)

        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans