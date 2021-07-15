class Solution:
    # 栈
    # 时间O(n) 空间O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        left = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                if not stack or stack[-1] != left[ch]:
                    return False
                stack.pop()
        return stack == []
