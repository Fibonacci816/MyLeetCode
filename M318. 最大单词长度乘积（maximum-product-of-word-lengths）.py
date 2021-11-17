class Solution:
    # 暴力求解，两两判断是否有相同字母
    # 时间O(l1l2n^2) 空间O(1)
    def maxProduct(self, words: List[str]) -> int:
        def has_no_common(str1, str2):
            return len(set(str1) & set(str2)) == 0
        n = len(words)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                if has_no_common(words[i], words[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        return res

    # 位运算判断两个单词有没有相同字母
    # 时间O(L+n^2) 空间O(n)，其中L是数组中的全部单词长度之和
    def maxProduct(self, words: List[str]) -> int:
        masks = [reduce(lambda c1, c2: c1 | (1 << ord(c2) - ord('a')), word, 0) for word in words]
        return max([len(word1[0]) * len(word2[0]) for word1, word2 in product(zip(words, masks), repeat=2) if word1[1] & word2[1] == 0], default=0)

    # 位运算判断两个单词有没有相同字母，哈希表去重
    # 时间O(L+n^2) 空间O(n)，其中L是数组中的全部单词长度之和
    def maxProduct(self, words: List[str]) -> int:
        masks = defaultdict(int)
        for word in words:
            mask = reduce(lambda c1, c2: c1 | (1 << ord(c2) - ord('a')), word, 0)
            masks[mask] = max(masks[mask], len(word))
        return max([masks[mask1] * masks[mask2] for mask1, mask2 in product(masks, repeat=2) if mask1 & mask2 == 0], default=0)
