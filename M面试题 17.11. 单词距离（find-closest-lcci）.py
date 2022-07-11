class Solution:
    # 遍历 + 更新记录
    # 时间O(n) 空间O(1)
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        word1_idx, word2_idx = None, None
        ans = len(words)
        for i, word in enumerate(words):
            if word == word1:
                word1_idx = i
            elif word == word2:
                word2_idx = i
            if word1_idx is not None and word2_idx is not None:
                ans = min(ans, abs(word1_idx - word2_idx))
        return ans