class Solution:
    # 先整体翻转，再翻转每个单词
    # 时间O(n) 空间O(n)
    # 逻辑不变改为C/C++，空间O(1)
    def reverseWords(self, s: str) -> str:
        # 翻转一个单词s[l:r+1]
        def reverse_word(s, l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        s = list(reversed(s))
        n = len(s)
        idx = 0
        left = 0
        while left < n:
            if s[left] == ' ':
                left += 1
                continue
            # 寻找一个单词
            if idx != 0:
                s[idx] = ' '
                idx += 1
            right = left
            while right < n and s[right] != ' ':
                s[idx] = s[right]
                idx += 1
                right += 1
            # 翻转一个单词
            reverse_word(s, idx-(right-left), idx-1)
            left = right
        s = s[:idx]
        return ''.join(s)