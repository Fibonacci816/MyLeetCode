class Solution:
    def find_right(self, s, n, left):
        assert s[left] == '['
        cnt = 1
        for i in range(left+1, n):
            if s[i] == '[':
                cnt += 1
            elif s[i] == ']':
                cnt -= 1
            if cnt == 0:
                return i
        return -1

    def decodeString(self, s: str) -> str:
        n = len(s)
        res = ''
        start = 0
        while start < n:
            number = 0
            while ord('0') <= ord(s[start]) <= ord('9'):
                number = number * 10 + int(s[start])
                start += 1
            if s[start] == '[':
                right = self.find_right(s, n, start)
                res += number * self.decodeString(s[start+1:right])
                start = right + 1
            else:
                res += s[start]
                start += 1
        return res