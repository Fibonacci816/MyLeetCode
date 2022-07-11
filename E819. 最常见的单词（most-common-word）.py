class Solution:
    # 哈希 计数
    # 时间O(m+n) 空间O(m+n)
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub(r"[!?',;.]", ' ', paragraph.lower()).split()
        counter = Counter(words)
        counter -= dict([(b, 1000) for b in banned])
        return counter.most_common(1)[0][0]