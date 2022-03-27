class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        ans = ""
        tmp_word = ""
        for word in words:
            if word == "" or len(word) > len(tmp_word) + 1:
                continue
            # 找前缀
            for i, c in enumerate(word):
                if i == len(tmp_word) or c != tmp_word[i]:
                    break
            if i == len(word) - 1:
                tmp_word = word
            if len(ans) < len(tmp_word):
                ans = tmp_word
        return ans

    def longestWord(self, words: List[str]) -> str:
        words.sort()
        ans, candidate = "", {""}
        for word in words:
            if word and word[:-1] in candidate:
                candidate.add(word)
                if len(ans) < len(word):
                    ans = word
        return ans
