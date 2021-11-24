class Solution:
    # 回溯+剪枝
    # 时间O(n·2^n) 空间O(n^2)
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    if cnt == 0:
                        return False
                    cnt -= 1
            return cnt == 0

        l_delete = r_delete = 0
        for c in s:
            if c == '(':
                l_delete += 1
            elif c == ')':
                if l_delete == 0:
                    r_delete += 1
                else:
                    l_delete -= 1

        res = []
        def delete(s, start, l_delete, r_delete):
            if l_delete == 0 and r_delete == 0:
                if is_valid(s):
                    res.append(s)
            else:
                n = len(s)
                for i in range(start, n):
                    if l_delete + r_delete > n:
                        break
                    if i > 0 and s[i] == s[i-1]:
                        continue
                    if s[i] == '(' and l_delete > 0:
                        delete(s[:i]+s[i+1:], i, l_delete-1, r_delete)
                    elif s[i] == ')' and r_delete > 0:
                        delete(s[:i]+s[i+1:], i, l_delete, r_delete-1)
        delete(s, 0, l_delete, r_delete)
        return res