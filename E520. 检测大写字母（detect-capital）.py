class Solution:
    # 时间O(n)
    def detectCapitalUse(self, word: str) -> bool:
        return word.upper() == word or word.lower() == word or word[1:].lower() == word[1:]