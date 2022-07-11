class Solution:
    # 哈希表
    # 时间O(S) 空间O(S)
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
         "....", "..", ".---", "-.-", ".-..", "--", "-.",
         "---", ".--.", "--.-", ".-.", "...", "-", "..-",
         "...-", ".--", "-..-", "-.--", "--.."]
        return len(set("".join(MORSE[ord(ch) - ord('a')] for ch in word) for word in words))
