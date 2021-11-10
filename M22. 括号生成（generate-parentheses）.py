class Solution:
    # dfs生成所有括号序列，判断每个是否有效
    # 时间O(n2^(2n)) 空间O(n)
    def generateParenthesis(self, n: int) -> List[str]:
        def is_valid(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                else:
                    if cnt == 0:
                        return False
                    cnt -= 1
            return cnt == 0
        res = []
        def dfs(n, generated):
            if len(generated) == 2 * n:
                if is_valid(generated):
                    res.append(generated)
                return
            for c in ['(', ')']:
                dfs(n, generated + c)
        dfs(n, '')
        return res

    # 只生成有效的序列（递归过程中判断该步生成左括号还是有括号，相当于dfs剪枝）
    # 时间O(2^(2n)/√n)（参考卡特兰数） 空间O(n)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # left和right分别为左括号和有括号的可用数量
        def generate(left, right, generated):
            if left == 0 and right == 0:
                res.append(generated)
            if left > 0:
                generate(left - 1, right, generated + '(')
            if right > left:
                generate(left, right - 1, generated + ')')
        generate(n, n, '')
        return res
        