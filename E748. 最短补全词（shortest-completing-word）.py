class Solution:
    # 字符计数
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_counter = Counter(c for c in licensePlate.lower() if c.isalpha())
        return min([word for word in words if not license_counter - Counter(word)], key=len)
