class Solution:
    # 模拟
    def toGoatLatin(self, sentence: str) -> str:
        cnt, word, vowel = 0, "", False
        ans = ""
        sentence += ' '
        for c in sentence:
            if c == ' ':
                cnt += 1
                if not vowel and len(word) > 1:
                    word = word[1:] + word[0]
                ans += ('' if cnt == 1 else ' ') + word + 'ma' + 'a' * cnt
                word, vowel = "", False
            else:
                if not word:
                    if c.lower() in {'a', 'e', 'i', 'o', 'u'}:
                        vowel = True
                word += c
        return ans