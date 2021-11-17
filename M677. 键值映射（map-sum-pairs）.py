# sum时扫描字典中所有元素
# 时间复杂度参照for循环 空间复杂度为map大小
class MapSum:

    def __init__(self):
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        return sum(v for k, v in self.map.items() if k.startswith(prefix))


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


# 字典树
class TrieNode:
    def __init__(self):
        self.val = 0
        self.next = [None for _ in range(26)]


# 使用字典树，插入时遍历key的每个字符更新字典树节点值，sum时从根节点找到prefix对应节点，返回该节点的值
# 时间复杂度参照for循环 空间复杂度为map大小+字典树大小
class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        node = self.root
        for c in key:
            if not node.next[ord(c) - ord('a')]:
                node.next[ord(c) - ord('a')] = TrieNode()
            node = node.next[ord(c) - ord('a')]
            node.val += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if not node.next[ord(c) - ord('a')]:
                return 0
            node = node.next[ord(c) - ord('a')]
        return node.val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)