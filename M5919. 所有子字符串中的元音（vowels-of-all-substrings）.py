class Solution:
    # 时间O(n) 空间O(1)
    def countVowels(self, word: str) -> int:
        n = len(word)
        # 如果位置下标i的字符为元音，则包含该字符的所有子串数量为(i + 1) * (n - i)
        return sum((i + 1) * (n - i) for i, c in enumerate(word) if c in "aeiou")

    # 时间O(n) 空间O(1)
    def countVowels(self, word: str) -> int:
        res = 0
        cnt = 0  # 表示以当前位置为结尾的所有子串的元音计数
        for i, c in enumerate(word):
            if c in "aeiou":
                cnt += i + 1
            res += cnt
        return res
        