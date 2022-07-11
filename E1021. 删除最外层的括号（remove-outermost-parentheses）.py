class Solution:
    # 遍历 + 计数
    # 时间O(n) 空间O(1)
    def removeOuterParentheses(self, s: str) -> str:
        ans, primitive, cnt = "", "", 0
        for c in s:
            primitive += c
            if c == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                ans += primitive[1:-1]
                primitive = ""
        return ans
