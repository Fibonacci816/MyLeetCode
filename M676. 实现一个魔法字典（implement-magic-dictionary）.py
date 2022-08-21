class MagicDictionary:

    def __init__(self):
        self.words = defaultdict(set)

    # 时间O(N)，N为词典中词的个数；空间O(Nl)，其中l为词的平均长度
    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.words[len(word)].add(word)

    # 哈希 + 逐位比较
    # 时间O(nl)，其中n为字典中与搜索词长度相同的词的数量；l为搜索词长度，空间O(1)
    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.words:
            return False
        for word in self.words[len(searchWord)]:
            diff_num = 0
            for c1, c2 in zip(word, searchWord):
                if c1 != c2:
                    diff_num += 1
                if diff_num > 1:
                    break
            if diff_num == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)