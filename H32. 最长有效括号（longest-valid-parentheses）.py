class Solution:
    # 栈（栈底元素为最后一个没有被匹配的右括号的下标）
    # 时间O(n) 空间O(n)
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans

    # dp(dp[i] 表示以下标i字符结尾的最长有效括号的长度)
    # s[i] = '(': f(i) = 0
    # s[i] = ')': f(i) = f(i-2) + 2 if s[i-1] == '(' else f(i-2) + 2 + f(i-f(i-1)-2) if s[i-f(i-1)-1] == '('
    # 时间O(n) 空间O(n)
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        ans = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                ans = max(ans, dp[i])
        return ans