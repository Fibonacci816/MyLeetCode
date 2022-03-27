class Solution:
    # 字符计数比较
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # return not Counter(ransomNote) - Counter(magazine)
        mag_counter = Counter(magazine)
        return all(k in mag_counter and mag_counter[k] >= v for k, v in Counter(ransomNote).items())